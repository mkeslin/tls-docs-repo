---
backlog: "BL-003 · Jail · Finish jail command center"
status: draft
created: 2026-03-30
---

# Plan: BL-003 — Jail Command Center (JCC) verification (checklist)

## Goal

While **finishing** the Jail Command Center (**BL-003**), systematically **verify and test** the **JLM ops board** experience: roster/layout, moves, passes, episodes, booking handoff, and related modals. This document is a **manual QA checklist** only — **no implementation** here.

**Related backlog:** **BL-002** covers **Jail Intake booking** steps, fields, and printouts in depth. When testing **Add Booking**, **In Booking Process**, or **Open booking** from JCC, follow **[`BL-002-jail-booking-verify.md`](BL-002-jail-booking-verify.md)** for the intake side; use this plan for **board-specific** behavior.

---

## Context (Thin Line RMS)

- **Primary shell:** product-repo `ThinLine.UI/src/components/modules/jlm/JlmBoardContainer.vue` — agency-scoped **command center** (`jlm` route): heartbeat bar, **roster** vs **layout** view, filters, **In Booking Process**, episode cards/chips, drag-and-drop moves, **location rail**, **episode drawer**, **work queue**, passes (pass runner / cell check UI), SignalR (`jlmHubService`) for live updates, move **undo** toast, sticky **error** toast.
- **API:** Board and moves go through product-repo `ThinLine.UI/src/api/jlmApi.ts`; bookings in progress use product-repo `ThinLine.UI/src/api/jailIntakeApi.ts`. Backend unit tests exist under product-repo `ThinLine.API/ThinLine.API.UnitTests/Jlm/` and related **Jms** tests (observation pass, transfer log, etc.) — they **do not replace** this UI checklist.

**Feature flags / config:** e.g. `JLM_VISITOR_LOG_ENABLED` in product-repo `ThinLine.UI/src/config/jlmFeatureFlags.ts` affects **visitor log** and move prompts for **VISITATION** — test both states if your deployment toggles it.

---

## Per-surface verification rubric (apply to each major section below)

For **each** area you exercise (heartbeat, roster row, layout cell, drawer, modal, rail), verify **all three** where they apply. Use **Pass / Fail / N/A**; **N/A** is OK when there is no printout or the surface is read-only chrome.

### Fields (data entry surfaces)

- [ ] **Controls** — Dropdowns, date/time, flags, and free text match intended behavior; codes display as expected.
- [ ] **Validation** — Required fields, allowed transitions, and error text are clear; destructive actions confirm when appropriate.
- [ ] **Persistence** — After save/submit, reopening the same flow shows the same data; server errors surface without silent loss.

### Layout

- [ ] **Structure** — Grid columns (passes | center | overview | location monitor on large screens), stacking on small screens, and **no** clipped critical controls.
- [ ] **Density** — Roster and layout remain readable at typical **floor** resolutions; scroll regions behave (headers sticky where designed).
- [ ] **States** — Loading, empty, filtered-empty, and error states are obvious; **drag/drop** affordances (highlight targets, “no location configured” messages) are clear.

### Reports and printouts

- [ ] **Roster report** — **Print Roster** (heartbeat) produces **correct roster** for current facility context (filters, date range if applicable — confirm behavior).
- [ ] **Transfer log** — **Transfer Log** modal: date range, preview/download, and output match **facility/agency** and **selected window**.
- [ ] **Other** — Any **print** or **export** from episode drawer, passes, or admin paths: data matches on-screen values.

---

## Checklist — first pass

Use a **test agency / facility** and **non-production** data where possible. Mark **Pass / Fail / N/A** and note build or date.

### A. Entry, agency, and realtime

- [ ] **agencyId** — With no agency selected, empty state prompts to select an agency; with agency, board loads.
- [ ] **Hub lifecycle** — `joinFacility` on enter, `leaveFacility` on exit; **reconnect** after simulated disconnect refreshes board and bookings in progress (or document if manual refresh is required).
- [ ] **Live updates** — Episode moves, cell occupancy, location state, and episode flags update the UI without full page reload (verify at least one event path per category).

### B. Heartbeat bar and top actions

- [ ] **Stats / metrics** — Heartbeat counts (or stats) match reality; **metric click** filters or focuses as designed (if applicable).
- [ ] **Search** — Search narrows roster/inmates consistently; **clear** restores full list.
- [ ] **Add Booking** — Opens **`JlmBookingDrawer`**; new booking appears in **In Booking Process** (see **BL-002** for intake completion).
- [ ] **Print Roster** — See rubric **Reports**; loading state; no duplicate downloads on double-click.
- [ ] **Transfer Log** — Modal opens; date range defaults; **generate** succeeds; **Reports** rubric.
- [ ] **Jail Intake** — Navigates to **Jail Intake Search** (or configured entry) without losing agency context unexpectedly.

### C. View mode and filters

- [ ] **Roster vs Layout** — Toggle switches between **roster** and **layout** grid; selection and selected episode stay coherent (or reset is intentional).
- [ ] **Filter toggles** — Exercise **suicide watch**, **unassigned**, **onsite** / **offsite**, **hide empty locations** (and any other banners on the board); counts and visible rows match filter intent.
- [ ] **Clear filters** — Restores default view.
- [ ] **Refresh** — Manual refresh control (if present) reloads board without breaking selection (or document behavior).

### D. In booking process

- [ ] **List** — Draft / in-process / ready-for-acceptance bookings appear with correct counts; **loading** state shown.
- [ ] **Cards** — **Open booking** / **Open person** work; selection highlights; **BL-002** for intake completion and Accept.

### E. Roster and layout (episodes)

- [ ] **Episode cards/chips** — Name, location, flags (e.g. suicide watch) display; **open person** slideout works.
- [ ] **Selection** — Selecting an episode opens **`JlmEpisodeDrawer`** (or rail) with matching **custody episode** and **person** context.
- [ ] **Drag to move** — Drag episode to **location rail** or **cell**; drop applies move; **invalid** targets rejected with clear feedback.
- [ ] **Move picker fallback** — Click-handle / **open picker** path when drag is not used (`JlmDragLocationPicker` / move modal).
- [ ] **Concurrent moves** — Double-drop or rapid clicks do not duplicate moves (idempotency / `moveInProgress` behavior).

### F. Location rail and location monitor

- [ ] **Rail** — Destination types (holding, intake, rec, gym, court, offsite, visitation, etc.) match configuration; **missing location** shows actionable error (e.g. “Add one in Jail Intake → Locations”).
- [ ] **Location monitor** — Column reflects occupancy/state; **live feed** opens **`JlmFeedModal`** when triggered.

### G. Typed move prompts (VISITATION, COURT, OFFSITE_HOLDING)

- [ ] **`JlmMovePromptModal`** — Opens when required; **context fields** (per location type) validate; submit completes move with **moveContext** passed through.
- [ ] **Visitor log** — If `JLM_VISITOR_LOG_ENABLED`: **Visitor log** path from episode flow **VisitorLogCreateDialog**; if disabled, behavior matches flag (no broken prompts).

### H. Release from custody

- [ ] **`JlmReleaseDialog`** — Opens from episode drawer; required fields; submit **releases** episode and **board updates** (episode removed or status updated).
- [ ] **Cancel / close** — No partial state on cancel.

### I. Episode drawer (detail)

- [ ] **Move** — Triggers picker or move flow consistent with **E**/**F**.
- [ ] **Release** — Hooks to **H**.
- [ ] **View booking** — Opens booking drawer for linked booking when applicable.
- [ ] **Medications / flags** — Panels (e.g. **`JlmEpisodeMedicationsPanel`**, critical flags) show **correct** data and updates after hub events.

### J. Work queue and tasks

- [ ] **`JlmWorkQueuePanel`** — Tasks/schedules appear; complete/snooze/open flows as designed; counts match API.

### K. Passes and observation (left column)

- [ ] **Pass runner / cards** — Start/pass flows; **PassCard** / **JlmPassRunner** complete a round without stale state.
- [ ] **Cell check** — **CellCheck** components: inmate list, observation picker, **exceptions** detail; entries match **observation** service behavior.
- [ ] **Integration** — Pass completion does not leave board inconsistent (refresh episode/location if required).

### L. Booking checklist rail (when episode + booking linked)

- [ ] **`JlmBookingChecklistRail`** — Required/optional steps match intake; **Accept** (if shown) matches **BL-002** acceptance rules.

### M. Undo, errors, and toasts

- [ ] **Move undo** — **`JlmMoveUndoToast`**: countdown, **undo** reverts move; expiry clears state.
- [ ] **Sticky errors** — **`JlmErrorToast`**: user can dismiss; message is actionable.

### N. Non-functional

- [ ] **Responsive** — Usable at **tablet** and desktop; **lg** breakpoint grid vs stacked layout.
- [ ] **Permissions** — User without **`Rms.JailIntake.Access`** (or module-specific claims) cannot access JCC; **Modify** / **Approve** behaviors match roles (e.g. `canApproveJailIntake` for settings if enabled).
- [ ] **Performance** — Board with many episodes remains usable (scroll, no runaway hub handlers).

### O. Regression triggers (after code changes)

- [ ] Re-run **C–F** after roster/layout or filter changes.
- [ ] Re-run **G–H** after move prompt or release API changes.
- [ ] Re-run **A** after SignalR or `jlmHubService` changes.
- [ ] Re-run **Reports** portions of the rubric after **roster** or **transfer log** report template changes.

---

## Out of scope (unless you extend the checklist)

- **Jail Intake** step-by-step intake **fields/layout/prints** — **BL-002**.
- **Jlm Settings** — If re-enabled (`JlmSettingsView`), add a dedicated subsection or separate plan.
- **Deep observation/medical log search** (Jail Observation module screens not hosted on the board shell).

---

## Changelog

| Date | Notes |
|------|--------|
| 2026-03-30 | First-pass JCC manual QA checklist; grounded in `JlmBoardContainer` + related JLM components. |
