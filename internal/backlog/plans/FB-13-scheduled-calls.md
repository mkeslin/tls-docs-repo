---
backlog: "FB-13 · CAD · Scheduled / future calls"
status: implemented
created: 2026-07-10
---

# Plan: Scheduled / future calls

## Goal

Dispatchers can pre-create calls for known future events (e.g. funeral processions) that **do not appear on the active open board** until activated. A **Scheduled** expansion on the Calls column (shown only when at least one exists) holds those calls. **Manual Activate** is required for v1; auto-promote at scheduled time is an optional follow-up.

## Context

- **Field feedback:** product-repo `Docs/CAD-Field-Feedback-Outstanding.md#fb-13--scheduled--timed-call-appearance` (FB-13) — Ashlee 6/18 / Gibson (funeral start time).
- **Related (do not conflate):** product-repo `Docs/CAD-Architectural-Audit.md` (BL-022-16) — call *queue* / pending stack for calls that are “pending now,” not future-dated. Scheduled is a **time-gated board bucket**, not a work queue.
- **Risk / lane:** Feature work. Touches `Call` lifecycle and dispatch-board queries — migration required; stay clear of auth/billing. Follow ``AGENTS.md`` (product repo `AGENTS.md`) for EF migrations (`dotnet ef migrations add` only).
- **Baseline today:**
  - Open = `CallStatusCode == null`; closed = disposition set (cannot clear).
  - `GetDispatchBoardOpenCallsAsync` returns all open calls; future `CallDateTime` still lands on the open board.
  - Board UI: open list + **Closed Calls** expansion in product-repo `ThinLine.UI/src/components/cad/CadCallContainer.vue`.
  - Create path: product-repo `ThinLine.UI/src/components/cad/CadAddCallSplitButton.vue` + templates.

## Product decisions (v1)

| Decision | Choice |
|----------|--------|
| Entity | Real `Call` (gets a call number); not a separate draft table |
| Hide from open | Explicit scheduled state — **not** “future `CallDateTime` alone” |
| Board placement | Expansion **Scheduled** above **Closed Calls**; render only if count > 0 |
| Create UX | Extend add-call control: **Schedule call** (alongside Add / templates) — prompt for activate-at datetime |
| Activate | **Manual “Activate now”** on scheduled card / sheet → moves to open board |
| CallDateTime on activate | Set **`CallDateTime` to activation time** (agency/UTC now per existing CAD conventions); clear `ScheduledActivateAt` |
| CallDateTime while scheduled | May mirror intended event / activate-at on create for display; **authoritative “call started” time is set only on Activate** |
| Cancel scheduled | **Soft-delete** (`IsDeleted`) — already filtered out of board queries; confirm UI on card/sheet |
| Past `ScheduledActivateAt` | **Allowed** (no server reject); optional mild UI warning only |
| Auto-promote at time | **Out of scope for v1** (see Follow-ups) |
| Units on scheduled calls | **No unit assign** until activated (reject assign / drag with clear message) |
| Disposition | Only after activate (normal close path). Do **not** disposition a still-scheduled call — cancel via soft-delete instead |
| Search / RMS | Scheduled (non-deleted) calls appear in call-sheet search with a Scheduled indicator; soft-deleted follow existing deleted-call search rules |
| Mobile / self-dispatch | Out of scope for v1 (dispatcher board only) |
| Webhooks | Do not fire “active call” style events until activate (confirm against existing webhook triggers) |

## Approach

### 1. Data model

Add nullable `DateTime? ScheduledActivateAt` on `Call` (UTC, same convention as other CAD datetimes).

**Board membership rule:**

| Bucket | Predicate |
|--------|-----------|
| **Open (active)** | `CallStatusCode == null` **and** `ScheduledActivateAt == null` |
| **Scheduled** | `CallStatusCode == null` **and** `ScheduledActivateAt != null` |
| **Closed** | `CallStatusCode != null` (unchanged). Soft-deleted calls are excluded from all board buckets via existing `!IsDeleted` filter |
| **Canceled (scheduled)** | Soft-delete while still scheduled — drops off Scheduled; never appears as Closed |

**Activate:** set `ScheduledActivateAt = null`, set **`CallDateTime` to activation time**, sync auto-created notes that key off call datetime (same pattern as other `CallDateTime` updates), persist + SignalR so boards refresh.

**Cancel:** soft-delete the call (reuse existing soft-delete path if one exists for calls; otherwise add a guarded delete for scheduled-only or general call soft-delete with confirm). Auto-note optional (“SCHEDULED CALL CANCELED”).

**Why not a new status code:** Disposition (`CallStatusCode`) already means closed. Reusing it for SCHEDULED would break `IsClosed` and closed-call queries. A dedicated nullable timestamp is the smallest clear signal and doubles as the display “when.”

Scaffold migration via CLI only; customize `Up`/`Down` as needed.

### 2. API / domain

- **Queries**
  - Change `GetDispatchBoardOpenCallsAsync` to exclude `ScheduledActivateAt != null`.
  - Add `GetDispatchBoardScheduledCallsAsync()` (open + scheduled, ordered by `ScheduledActivateAt` ascending).
- **Create**
  - Extend create / create-from-template with optional `scheduledActivateAt`.
  - When set: call is created as scheduled; auto-note e.g. “CALL SCHEDULED FOR {time}”.
- **Activate**
  - `POST calls/{id}/activate-scheduled` (or equivalent) with `rowVersion`: clears `ScheduledActivateAt`, sets `CallDateTime` to now, writes auto-note (“CALL ACTIVATED”), notifies hub.
  - Idempotent if already active; 400 if closed or deleted.
- **Cancel (soft-delete)**
  - Soft-delete scheduled call from card/sheet with confirm; hub removes from `scheduledCallCards`.
  - Prefer allowing soft-delete primarily for scheduled shells in v1 UI; do not invent a separate “cancel schedule → stay open” path.
- **Guards**
  - Unit assign / primary unit / drag-assign: fail validation while scheduled.
  - Updating `ScheduledActivateAt` allowed while still scheduled (reschedule); clearing it only via Activate (not by patching null).
- **View models**
  - Card + sheet: `scheduledActivateAt`, `isScheduled` (computed).
  - Factory methods for scheduled board cards (mirror open/closed dispatch-board factories).
- **Hub / store sync**
  - Ensure create/activate/update events move cards between open and scheduled collections on clients (same pattern as open ↔ closed).

### 3. UI

- product-repo `ThinLine.UI/src/components/cad/CadCallContainer.vue`
  - New expansion **Scheduled** above Closed; header shows count and/or next activate time; `v-if` when `scheduledCalls.length > 0`.
  - Cards in scheduled list: show activate-at; **Activate** and **Cancel** (soft-delete) actions; muted/distinct styling vs active open cards.
- product-repo `ThinLine.UI/src/components/cad/CadAddCallSplitButton.vue` (or sibling)
  - Menu item **Schedule call** → datetime dialog → create with `scheduledActivateAt`.
  - Optional: schedule from template (same dialog after template pick).
- product-repo `ThinLine.UI/src/stores/cadStore.ts`
  - `scheduledCallCards` collection; load with board; handlers for create/activate/hub.
- Call sheet: banner “Scheduled for {time}” + Activate + Cancel; disable unit assignment UI while scheduled.
- Call card: compact scheduled chip / datetime.

### 4. Tests

- Data store: open query excludes scheduled; scheduled query returns only scheduled.
- Service: create scheduled; activate sets `CallDateTime`; soft-delete removes from scheduled query; cannot assign unit while scheduled; cannot activate closed/deleted.
- View model / controller unit tests as needed for new endpoints.
- UI: store partitioning tests if existing cadStore specs cover open/closed.

### 5. Docs

- Update FB-13 status in product-repo `Docs/CAD-Field-Feedback-Outstanding.md` (`CAD-Field-Feedback-Outstanding.md`) when implemented (Deferred → shipped / Partial if auto-promote still pending).
- Note relationship to BL-022-16 in audit doc if that slice is revisited (scheduled ≠ queue).

## Files / areas (expected)

| Area | Paths |
|------|--------|
| Entity / migration | `ThinLine.Data.Model/CAD/Entities/Call.cs`, `Migrations/ThinLine/*` (CLI scaffold) |
| Store / contracts | `CallDataStore`, `ICallDataStore`, `ICallService`, `CallService` |
| API | `CallController`, call create DTOs, `CallViewModel` / `CallCardViewModel`, dispatch-board factory |
| Hub | CAD SignalR notifier paths that push call card updates |
| UI | `CadCallContainer.vue`, `CadAddCallSplitButton.vue`, `cadStore.ts`, `cadApi.ts`, call card/sheet |
| Tests | `ThinLine.API.UnitTests/CAD/*`, optional `ThinLine.UI/tests/unit/cadStore*` |

## Implementation order

1. Migration + open-query filter + scheduled query (board stays correct even before UI).
2. Create-with-schedule + Activate (sets `CallDateTime`) + soft-delete cancel + unit-assign guard + auto-notes.
3. Hub/client store: third collection + move on activate / remove on cancel.
4. UI: expansion + schedule create + activate/cancel affordances + sheet banner.
5. Tests + FB-13 doc update.

## Verification

- [x] `dotnet build ThinLine.API/ThinLine.Server.slnx` (via unit test build)
- [x] `dotnet test … --filter "FullyQualifiedName~ThinLine.API.UnitTests.CAD"` (382 passed)
- [x] Targeted scheduled create/activate/query tests
- [x] UI: eslint on touched files; `npm run build` in `ThinLine.UI`
- [ ] Manual: schedule funeral-style call → absent from open → visible in Scheduled → Activate → `CallDateTime` is activation time → assign unit works; Cancel soft-deletes and removes from Scheduled

## Resolved decisions

1. **CallDateTime on activate:** Set to activation time when the call is activated.
2. **Cancel:** Soft-delete (`Call.IsDeleted`); board queries already exclude deleted rows.
3. **Past `ScheduledActivateAt`:** Allowed on create/reschedule; optional UI warning only — no API rejection.

## Open questions (remaining)

1. **Permissions:** Same as `canModifyCadFull` for schedule / activate / cancel? (Default: yes.)
2. **Keyboard nav (BL-022-11):** Include Scheduled panel in panel cycle later; not required for v1.
3. **BL-022-16:** If queue ships later, keep Scheduled as a separate bucket. Do not merge concepts in v1.
4. **Create-time `CallDateTime`:** Placeholder until activate (e.g. copy of `ScheduledActivateAt`, or create-time “now”)? Does not matter for board membership; Activate overwrites. Default: set to `ScheduledActivateAt` on create for sheet display consistency before activate.

## Follow-ups (explicitly out of v1)

- **Auto-promote:** Background job (or poll) when `ScheduledActivateAt <= UtcNow` → activate + SignalR. Product rules for units/webhooks already deferred in FB-13 notes.
- Mobile / self-dispatch scheduled list.
- Recurring scheduled calls.
- Drag-and-drop activate.

## Notes

- Design discussion: Cursor thread 2026-07-10 (scheduled expansion + manual activate preferred over full scheduler).
- Workaround today: create the call at service time (FB-13 doc).
- Assign a **`BL-###`** in [`PRIORITIZED.md`](../prioritized.md) when this enters a sprint; rename plan file to `BL-###-scheduled-calls.md` if desired.
