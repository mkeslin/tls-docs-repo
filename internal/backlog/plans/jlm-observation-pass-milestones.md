---
backlog: "TBD · JLM / JMS · Observation pass milestones and ROUND cadence"
status: implemented
created: 2026-05-12
---

## Implementation summary (2026-05-12)

- Added three NOT NULL milestone columns on `TaskSchedules` plus a new `jms.JlmObservationRoundCadences` table for sliding cadence anchors (migration `20260512190839_AddObservationPassMilestonesAndRoundCadence`). Backfill seeds CELL/SUICIDE/other ROUND types with the canonical `(20/10/0)` and `(10/5/0)` triples.
- New `IJlmObservationRoundCadenceService` (`Business.Objects/Jlm/JlmObservationRoundCadenceService.cs`) handles first-observation slip and projects boundaries from `SeriesOriginUtc`. Hooked into `JlmObservationService.RecordEntriesAsync` (detects first entry via pre-batch count).
- `JlmTaskInstanceGenerationHostedService` now flows the cadence service through `GenerateRoundScopeInstancesAsync`, honours per-schedule `ObservationPassUpcomingLeadMinutes` for auto-open (`AutoManageRoundPassesAsync`, `BackfillObservationPassesForLast24HoursAsync`), and per-schedule `ObservationPassOverdueAfterMinutes` for `MarkOverdueAsync`.
- `JlmTaskService.GetTaskQueueAsync` and `GetQueueCountsAsync` resolve overdue/auto-open from the schedule columns instead of `JlmConstants.RoundOverdueGraceMinutes`.
- `JlmOpenPassViewModel` exposes `UpcomingLeadMinutes`/`DueNowLeadMinutes`/`OverdueAfterMinutes`; `GetOpenPassesAsync` resolves them from the linked ROUND `TaskInstance`'s schedule, falling back to per-type defaults for manual passes.
- UI (`JlmWorkQueuePanel.vue`) implements the three-phase Upcoming/Due Now/Overdue model from server-provided milestones; automated Upcoming passes now appear in the JCC card list and heartbeat counts, and Hidden phase suppresses cards before the upcoming threshold.
- Tests: `JlmObservationRoundCadenceService_Tests` (boundary projection, slip behaviour, idempotency) and `JlmObservationPassMilestones_Tests` (default triples, invariants). Full suite: 2489 pass.
- **Follow-up (post-milestones):** reduced future ROUND `TaskInstance` materialisation per (schedule, group) from 4 to 1 via shared `JlmConstants.RoundFutureInstancesToMaintain`. The cadence anchor row remains the source of truth; the JCC "Next scheduled" footer already renders one per chain.


# Plan: Observation pass milestones and sliding ROUND cadence

## Goal

- Replace the coarse before/after “due window” with **three explicit milestone offsets** tied to scheduled time \(T\) (same as today’s `ObservationPass.TimeWindowStart` / ROUND `DueAtUtc`).
- Persist those milestones **per `TaskSchedule` in the database** — migration assigns NOT NULL values for every schedule row (`CELL_CHECK`, `SUICIDE_CHECK`, and any other ROUND interval types per backfill rules).
- **Sliding ROUND cadence:** after the **first observation entry** on an automated ROUND pass, set the chain so the next ROUND boundary is `firstObservationObservedAtUtc + IntervalMinutes`, and regenerate forward `TaskInstance` horizons accordingly (Texas-style interval from first observation).

## Resolved decisions

- **Milestones storage:** Fully implemented in DB on product-repo `ThinLine.API/ThinLine.Data.Model/Jms/Entities/TaskSchedule.cs` — add three **NOT NULL** integer columns after migration backfill (`null` rows are disallowed once shipped; every schedule has explicit milestones).
- **Backfill rules:**  
  - `CELL_CHECK`: **20 / 10 / 0** (upcoming lead / due-now lead / overdue after scheduled).  
  - `SUICIDE_CHECK`: **10 / 5 / 0**.  
  - **Any other** `TaskTypeCode` on `TaskSchedules` that participates in ROUND interval generation — **same as CELL** (**20 / 10 / 0**) until overridden per schedule in the DB.

## Milestone semantics (scheduled time \(T\))

| Property (DB column)                    | Meaning |
|----------------------------------------|---------|
| `ObservationPassUpcomingLeadMinutes` | Show as **Upcoming** when `now >= T − this`. |
| `ObservationPassDueNowLeadMinutes`     | Show as **Due Now** when `now >= T − this` until overdue starts. |
| `ObservationPassOverdueAfterMinutes` | **Overdue** when `now >= T + this` (default **0**). |

Non-overlapping phases:

- **Hidden:** `now < T − upcomingLead`
- **Upcoming:** `T − upcomingLead <= now < T − dueNowLead`
- **Due Now:** `T − dueNowLead <= now < T + overdueAfter`
- **Overdue:** `now >= T + overdueAfter`

Validate at save time (API/admin): `upcomingLead >= dueNowLead`; all `>= 0`.

**Manual passes:** unchanged rule — treat as Due Now while open / no overdue (same as today’s client behavior).

### Coupling auto-open pass creation to milestones

Observation pass rows appear only once hosted logic crosses the auto-open lead. **`GetRoundAutoOpenLeadMinutes`** (and backfill equivalents) must use **`max(structural minimum, ObservationPassUpcomingLeadMinutes`** for that schedule) so an OPEN pass exists for the entire **Upcoming** window.

### First-observation cadence slip

- **Trigger once per pass:** transition from zero entries → at least one entry; pass is **`IsAutomated`** and linked to a ROUND `TaskInstance` whose schedule is interval-based cell/suicide round scope (product-repo `ThinLine.API/ThinLine.RMS.WebAPI/HostedServices/JlmTaskInstanceGenerationHostedService.cs`).
- **Timestamp:** use **earliest `ObservedAt`** among newly persisted entries for that write; batch record today assigns one UTC instant per batch (product-repo `ThinLine.API/ThinLine.Business.Objects/Jms/ObservationPassService.cs`) — document that precision is batch-time unless extended to per-row `ObservedAt` from client later.
- **Persist cadence anchor** keyed by `(TaskScheduleId, GroupKey)` — new table entity under `jms` schema; see original design (e.g. `JlmObservationRoundCadences` with `SeriesOriginUtc` matching “first observation” instant used to project `+ IntervalMinutes` chains).
- **Reshape futures:** cancel or MISS non-completed future ROUND instances for that schedule+group (policy: preserve `COMPLETED` history); host tick (`GenerateRoundScopeInstancesAsync`) emits next N boundaries from slipped series when cadence row exists, else product-repo `ThinLine.API/ThinLine.RMS.Common/Jlm/JlmRoundBoundaryHelper.cs` (**`JlmRoundBoundaryHelper`**).

**Operational note:** Slip runs on **first** observation even if census incomplete; aligns with regulatory “clock starts,” with operational risk documented.

## API / UI

- Extend product-repo `ThinLine.API/ThinLine.API/Jlm/IJlmObservationService.cs` with resolved milestone minutes **from the linked schedule** (product-repo `ThinLine.API/ThinLine.Business.Objects/Jlm/JlmObservationService.cs`).
- product-repo `ThinLine.UI/src/components/modules/jlm/JlmWorkQueuePanel.vue`: three-phase logic; automated **Upcoming** included in visible cards (`passesForJccDisplay`); heartbeat counts aligned.
- Mirror fields in product-repo `ThinLine.UI/src/models/jail/jlmObservationPass.ts`.
- ROUND `MarkOverdue` / board stats: align ROUND overdue with **`DueAtUtc + schedule.ObservationPassOverdueAfterMinutes`** where applicable (product-repo `ThinLine.API/ThinLine.RMS.WebAPI/HostedServices/JlmTaskInstanceGenerationHostedService.cs`, product-repo `ThinLine.API/ThinLine.Business.Objects/Jlm/JlmTaskService.cs`).

## Migration and data

- Add three **NOT NULL** columns on `TaskSchedules` with EF defaults if needed until backfill completes in the same migration; backfill SQL by `TaskTypeCode` per rules above (**other types → CELL match 20 / 10 / 0**).
- Update EF snapshot; follow team migration review process (``AGENTS.md`` (product repo `AGENTS.md`) risk boundaries).
- Future admin UX to edit milestones can be backlog; persistence is implemented now.

## Files / areas (expected)

- Entity + migration: `TaskSchedule`, `ThinLine.Data.Store/Migrations`
- Constants product-repo `ThinLine.API/ThinLine.RMS.Common/Constants/JlmConstants.cs`: align with migrated defaults for CELL/SUICIDE/“other”; used for validation messages, seed scripts, tests, **not** as the runtime source of truth once the row has NOT NULL columns
- Services: product-repo `ThinLine.API/ThinLine.Business.Objects/Jlm/JlmObservationService.cs`, product-repo `ThinLine.API/ThinLine.Business.Objects/Jms/ObservationPassService.cs`, hosted service cadence/generation paths
- Cadence entity + reshaping helper service (new, thin domain type)
- UI: product-repo `ThinLine.UI/src/components/modules/jlm/JlmWorkQueuePanel.vue`

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test` on `ThinLine.API.UnitTests` — phase math, open-pass payloads, cadence reshaping, migration assumptions where testable
- [ ] UI: `npm run lint` and `npm run build` in `ThinLine.UI/` for touched files

## Notes

- Consider linking this plan to a `BL-###` row in [`PRIORITIZED.md`](../prioritized.md) when one exists.
