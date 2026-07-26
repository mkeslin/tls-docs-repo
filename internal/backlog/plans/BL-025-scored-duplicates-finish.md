---
backlog: "BL-025 · Masters · Finish scored duplicates (Build Table + person merge-from-cluster)"
status: done
created: 2026-07-26
---

# Plan: Finish scored duplicates

## Goal

Make Admin **Build Table** trustworthy by honoring `fullRebuild` (clear stale candidates before rescoring), then ship **Person** merge-from-cluster end-to-end (plan → field picker → execute → mark cluster/candidates **Merged**).

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-025**.
- **Risk / lane:** Feature work on masters duplicates + merge; reuse existing `MergePersonsAsync` / `MasterMergeDialog` (no scoring redesign).
- Product plan origin: Cursor plan “Scored duplicates finish” (do not revamp scoring in this item).

## Approach

1. **Phase 1 — Honor `fullRebuild`**
   - `DeleteAllAsync` on all five candidate data stores.
   - Generators clear candidates when `fullRebuild == true`, then rescore; dedupe pairs across blocking buckets.
   - Unit tests: person FullRebuild clears stale; incremental preserves.
2. **Phase 2 — Person merge-from-cluster**
   - Show merge plan on scored cluster expand.
   - Open `MasterMergeDialog` with suggested survivor + losers; execute via existing person merge API.
   - `MarkClusterMergedAsync` sets cluster + member-pair candidates to **Merged**.
3. Later (out of this MVP): review lifecycle (Dismissed preserve), clone UX to other master types, Build Table ops caps.

## Files / areas (expected)

- `ThinLine.API/ThinLine.Business.Objects/Masters/Master*Duplicates/`
- `ThinLine.API/ThinLine.Data.Store/DataStore/Masters/*DuplicateCandidateDataStore.cs`
- `ThinLine.API/ThinLine.RMS.WebAPI/Controllers/Masters/MasterPerson/MasterPersonDuplicatesController.cs`
- `ThinLine.UI/src/components/admin/AdminMasterMerge.vue`
- `ThinLine.UI/src/api/masterPersonDuplicateApi.ts`
- `ThinLine.UI/src/components/masters/shared/MasterMergeDialog.vue`

## Verification

- [x] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj --filter "FullyQualifiedName~MasterPersonDuplicate"` (29 passed)
- [x] Full unit suite: 3539 passed
- [x] UI ESLint on touched Admin merge / dialog / API files
- [ ] Manual: Admin → Master Merge → Scored → expand person cluster → Merge cluster

## Open questions

- Preserve **Dismissed** clusters across rebuild (Phase 3).
- When to clone merge-from-cluster to Org/Location/Property/Vehicle (Phase 4).

## Notes

Scoring weights/thresholds remain as-is; smarter scoring is a separate future phase.
