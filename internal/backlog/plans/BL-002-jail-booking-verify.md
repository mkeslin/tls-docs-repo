---
backlog: "BL-002 · Jail · Finish booking"
status: draft
created: 2026-03-30
---

# Plan: BL-002 — Jail booking verification (checklist)

## Goal

While **finishing** the booking experience (**BL-002**), systematically **verify and test** the end-to-end **intake / booking** flow. This document is a **manual QA checklist** only — **no implementation** here.

**Related backlog:** **BL-003** (Jail Command Center / JCC) — full board checklist: [`BL-003-jcc-verify.md`](BL-003-jcc-verify.md). This plan overlaps **JLM** where booking meets the board; use **BL-003** for roster, moves, passes, and hub behavior.

---

## Context (Thin Line RMS)

- **Jail Intake** (`JailIntake*` routes): multi-step **booking details** (`JailIntakeBookingDetails.vue` + `details/steps/*`), timeline, autosave, step status (complete / defer / etc.).
- **JLM Command Center** (`JlmBoardContainer.vue`): **Add Booking**, **In Booking Process** (draft / in-process / ready-for-acceptance), **`JlmBookingDrawer`**, checklist rail, link to full intake.
- Step definitions and labels live in product-repo `ThinLine.UI/src/composables/jailIntake/useJailIntakeBookingSteps.ts` (`STEP_LABELS`, `STEP_HELP`, required vs conditional steps).

**UI flags (may change):** `IDENTITY_STEP_HIDDEN`, `SEARCH_STEP_HIDDEN`, `HOUSING_STEP_HIDDEN` can hide steps from the sidebar while still affecting **Accept** validation rules — when those flags flip, re-run the matching checklist rows.

---

## Per-step verification rubric (apply to every step in C–E)

For **each** booking step you exercise (required, conditional, or Docs), verify **all three** dimensions below. Use **Pass / Fail / N/A** per dimension; **N/A** is OK when a step has no printout yet or layout is unchanged from a prior sign-off.

### Fields

- [ ] **Correct controls** — Required vs optional fields match product intent; dropdowns/codes show expected options.
- [ ] **Validation** — Required field enforcement, formats (dates, numbers), cross-field rules, and error messages are clear and accurate.
- [ ] **Persistence** — Values save, reload, and appear correctly on timeline/related views after navigation or refresh.
- [ ] **Edge cases** — Empty state, long text, “unknown” / provisional paths, and defer / not-applicable flows still behave correctly for that step.

### Layout

- [ ] **Structure** — Section order, grouping, and labels match the design; no overlapping or clipped content at common breakpoints.
- [ ] **Readability** — Typography, spacing, and alignment are consistent with the rest of Jail Intake; dense steps remain scannable.
- [ ] **Responsive** — Step is usable on **tablet** and desktop widths; horizontal scroll is only intentional (e.g. wide tables).
- [ ] **States** — Loading, validation errors, disabled fields, and “read only after complete” (if any) present clearly.

### Reports and printouts

- [ ] **Coverage** — Any **report, print, or PDF** tied to this booking step (or to the booking package as a whole) includes the **right data** for fields completed on that step.
- [ ] **Accuracy** — Printed labels, codes, dates/times, and units match what the user sees on screen and what is stored (no stale or missing critical fields).
- [ ] **Branding / headers** — Agency/facility headers, footers, and pagination (if applicable) look correct.
- [ ] **Regression** — After layout or field changes, re-print or re-export and compare to a known-good sample.

---

## Checklist — first pass

Use a **test agency / facility** and **non-production** data where possible. Mark **Pass / Fail / N/A** and note build or date.

### A. Entry and booking lifecycle

- [ ] **Create booking** — From JLM: **Add Booking** opens drawer; booking is created and appears under **In Booking Process** (or equivalent list).
- [ ] **Open full intake** — From drawer / **Open booking**, **Jail Intake** booking details load with correct **booking id** and **agency**.
- [ ] **States** — Observe transitions: **DRAFT** → **IN_PROCESS** → **READY_FOR_ACCEPTANCE** (or your agency’s rules) and that lists (`getBookingsAsync` with those filters) stay consistent with the board.
- [ ] **Void / cancel** — If applicable: void path clears expectations and removes episode from “in progress” without orphan data (only if in scope for your test).

### B. Step sidebar and progress

- [ ] **Step list** — Required vs optional (conditional) steps match expectations; icons/colors reflect **complete** vs **in progress** vs **deferred**.
- [ ] **Navigation** — Clicking each step loads the right panel; **no lost context** when switching steps (autosave — see H).
- [ ] **Banner / status** — `JailIntakeStepStatusBanner` (or equivalent) shows correct status and reasons for deferred/blocked steps.

### C. Required steps (per `REQUIRED_STEP_CODES` in code)

For **each** row below, apply the **[Per-step verification rubric](#per-step-verification-rubric-apply-to-every-step-in-ce)** (**fields**, **layout**, **reports/printouts**).

Verify **complete** path for each **visible** step; for **hidden** steps (Identity / Search / Housing flags), note **N/A** or validate when flags are enabled.

| Area | Code | Functional notes (add rubric on top) |
|------|------|--------------------------------------|
| Person | `PERSON` | Aliases, SMT, mugshot flows; validation when Identity is prerequisite (per help text). |
| Custody | `CUSTODY` | Required fields; hold types; timestamps/agency as designed. |
| Identity | `IDENTITY` | Partial/provisional identity path if used; matches product rules. |
| Charges | `CHARGES` | Add/edit/delete charge; **hold-only** / no new charge scenarios per help text. |
| Search | `SEARCH` | Search performed + outcome recorded; no silent skip. |

### D. Conditional / deferrable steps (`CONDITIONAL_STEP_CODES`)

For **each** bullet: apply the **[Per-step verification rubric](#per-step-verification-rubric-apply-to-every-step-in-ce)** for **fields**, **layout**, and **reports/printouts** — including **deferred** / **not applicable** outcomes on printouts (labels should reflect actual status, not imply completed screening).

For each: **complete**, **defer** (with **reason**), **not applicable**, **preliminary/temporary** where allowed — then confirm **Accept** gating matches rules.

- [ ] **Property** — Bags/items; seal/open; “none collected” / agency-retained paths.
- [ ] **Mental health** — Screening; **defer** requires reason when policy says so.
- [ ] **Medical** — Screening; medications/withdrawal; defer with reason.
- [ ] **Classification** — Factors / recommendation; **PRELIMINARY** / **DEFERRED** options per `getStepStatusOptionsForStep`.
- [ ] **Housing** — Temporary placement / awaiting classification; **TEMPORARY** / **DEFERRED** as applicable.

### E. Documents (if exposed)

- [ ] **Docs step** — If present in UI: upload/metadata; does not block Accept incorrectly; apply the **[Per-step verification rubric](#per-step-verification-rubric-apply-to-every-step-in-ce)** (including any **document inventory** or **cover sheet** printouts).

### F. Accept into custody

- [ ] **Accept disabled** until **all required** steps satisfy validation (including hidden-step rules if they still apply server-side).
- [ ] **Accept succeeds** — Booking moves to accepted state; **timeline** shows `BOOKING_ACCEPTED_INTO_CUSTODY` (or equivalent).
- [ ] **Post-accept** — Episode appears on **JLM board** / roster as expected; **In Booking Process** clears for that booking.
- [ ] **Incident hooks** — If your flow creates incident/arrestee on accept: verify one happy path and note edge cases.
- [ ] **Whole-booking printouts** — Any **master booking report**, **intake packet PDF**, or **labels** generated at or after accept: confirm **all step sections** that should appear are present, accurate, and match the **[Reports and printouts](#reports-and-printouts)** expectations from each step.

### G. JLM board integration (overlap with BL-003)

- [ ] **In Booking Process** card — Count matches list; selecting card highlights; **Open booking** / **Open person** work.
- [ ] **Checklist rail** (`JlmBookingChecklistRail`) — Required/optional lines match intake; **Accept** from rail if shown — same outcome as intake.
- [ ] **SignalR / realtime** — Board refreshes when booking state changes (or manual refresh acceptable — document actual behavior).

### H. Persistence and collaboration

- [ ] **Autosave** — Navigate away and back; data persists (or explicit save warnings appear).
- [ ] **Step lock / takeover** — If two users open same booking: lock message, **takeover**, and timeline event `STEP_LOCK_TAKEN_OVER` (per `EVENT_TYPE_LABELS`).
- [ ] **Set step status** — Supervisor override / defer from `SetStepStatus` dialog behaves as expected.

### I. Timeline and audit

- [ ] **JailIntakeBookingTimeline** — Events appear in order: create, step complete, status changes, accept.
- [ ] **Significant field changes** — Key edits log as expected for compliance review.

### J. Non-functional

- [ ] **Responsive** — Usable at **tablet** width (intake is often used on floor devices).
- [ ] **Errors** — Network failure shows recoverable message; no silent data loss on save.
- [ ] **Permissions** — User without jail claims cannot access; with claims can complete flow.

### K. Regression triggers (after code changes)

- [ ] Re-run **C–F** after any change to `useJailIntakeBookingSteps.ts`, Accept API, or step components — including the **full per-step rubric** (fields, layout, printouts).
- [ ] Re-run **G** after JLM / SignalR changes.
- [ ] Re-run **reports/printouts** portions of the rubric after any change to booking reports, PDF templates, or merge fields.

---

## Out of scope for this checklist (unless you add them)

- **Command Center**-only features (full **BL-003**): drag/drop moves, location prompts, visitor log — track separately.
- **Jail Intake Search** admin lists, **health** dashboards, **locations** CRUD — optional smoke only.

---

## Changelog

| Date | Notes |
|------|--------|
| 2026-03-30 | First-pass manual QA checklist; grounded in `useJailIntakeBookingSteps` + JLM booking UI. |
| 2026-03-30 | Added per-step rubric: fields, layout, reports/printouts; linked from C–E and K. |
| 2026-03-30 | Linked related plan **BL-003** (JCC). |
