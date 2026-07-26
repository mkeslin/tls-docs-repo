---
backlog: "BL-024 · Masters · Master search coalesce + faster person merge"
status: ready
created: 2026-07-26
---

# Plan: Master search coalesce + faster person merge

## Goal

Stop merge-driven `Update*Search` storms and search-index R-FAULTs, and make person-merge FK rewrites cheaper, without changing the survivor/soft-delete domain model.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-024**.
- **Risk / lane:** feature/perf; touches SQL procs/triggers (EF migration), merge path, MassTransit consumer. No outbox / auth / billing.

## Approach

1. **Phase A — Coalesce + safe proc (Person):** `SESSION_CONTEXT(N'MasterSearchSuppress')` around merge; CodeCommons trigger guard; ambient skip of root search publishes; applock-serialized `UpdateMasterPersonSearch`; consumer 2601/2627 retry; distinct end-of-merge publishes. **Do not** keep child-table AFTER triggers (EF `OUTPUT` conflict).
2. **Phase B — Faster person rewrites:** set-based `ExecuteUpdateAsync` / SQL for simple FKs and association dedupe; set-based current-location flip instead of reload+`CommitAsync`.
3. **Phase C — Location / Org / Property / Vehicle:** same suppress + applock procs + CodeCommons suppress + distinct merge publishes + consumer retry; no child-table search triggers.
4. **UI freshness:** `MergeRebuildSearchTablesAsync` rebuilds search **synchronously** for survivor/loser ids before HTTP returns (bus publish kept for secondary listeners / location→person cascade).
5. **Metrics:** baseline helpers in product-repo `Scripts/MasterSearchTriggers/metrics-baseline.sql`; merge duration logs on merge services.
6. **Merge undo journal (tracking only):** `MasterMergeChange` + ambient `MasterMergeJournal` capture per-row remaps, soft-deleted association dupes, survivor before-image JSON, and structural reparents. No undo API yet — journal enables a future reverse path.

## Files / areas

- `Scripts/MasterSearchTriggers/{Person,Location,Organization,Property,Vehicle}.sql`
- Migrations: `*CoalesceMasterPersonSearchRefresh*`, `*DropMasterPersonSearchChildTriggers*`, `*CoalesceMasterSearchRefreshNonPerson*`, `*AddMasterMergeChangeJournal*`
- `IMasterSearchRefreshSuppressor` / `MasterSearchRefreshSuppress`
- `MasterMergeJournal` / `MasterMergeChangeRecord` / `IMasterMergeChangeDataStore`
- Merge services + roots for Person / Location / Org / Property / Vehicle
- `MasterSearchConsumer` (retry for all master types)

## Verification

- [x] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [x] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj` (person work; Phase C consumer + rebuild tests)
- [x] Apply `CoalesceMasterPersonSearchRefresh` + `DropMasterPersonSearchChildTriggers` to local ThinLineRMS
- [x] Phase C migration `CoalesceMasterSearchRefreshNonPerson` scaffolded / applied locally
- [x] Manual: person merge + bulk merge — losers deleted; search rows correct; no EF OUTPUT trigger failures
- [ ] Manual: Location/Org/Property/Vehicle merge smoke (optional parity check)
- [ ] Correctness smoke: survivor associations, history, attachments, search row for survivor

## Open questions

- Optional MassTransit outbox if durability across recycle becomes a requirement.
- Undo API / UI: apply `MasterMergeChange` descending by `Sequence` for a `MergeId`; block if a later merge touched the same masters.

## Notes

### Lessons (critical)

1. **Do not add AFTER triggers** on tables EF updates — SQL Server rejects `OUTPUT` without `INTO` → merge `SaveChanges` fails.
2. `ExecuteUpdate` only on **mapped** columns.
3. Service Bus `MessageSizeExceeded` can be a **secondary** Serilog failure logging a huge exception graph; middleware must not mask the real error.

### Local baseline (2026-07-26)

~40k `MasterPersonSearch` rows; child-table person search triggers dropped after brief reintroduction; only CodeCommons person search trigger remains. Phase C scripts/migration deploy applock procs + CodeCommons suppress for Location/Org/Property/Vehicle and drop any leftover location/vehicle child search triggers.
