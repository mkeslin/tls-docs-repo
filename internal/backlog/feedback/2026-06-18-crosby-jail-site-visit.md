# Crosby Jail feedback — organized analysis

**Source:** Eric Gibson site visit, 6/18/2026  
**Agency:** Crosby (Crosby TX)  
**Original notes:** Eric Gibson field notes (Jail.md, 6/18/2026 visit)  
**Format:** Bugs, enhancements, and configuration requests from field staff

---

## Executive summary

Feedback clusters around **JCC / cell checks** (timer behavior, audio, manual starts, stuck passes, released-inmate history) and **booking / intake** (print data, charges, DPS/grade display, cross-agency visibility). One **ops/config** item remains (**PC Affidavit** access for Heather).

The highest-impact **remaining** bugs are **Heather's add/edit charges pain** (recurring, workflow-heavy — **not fixed**; post-accept charge changes still blocked). Several cell-check issues likely shared one root cause: **aggressive reload/polling + notification logic** when passes queue or timers fire (**CROSBY-002** fixed). **CROSBY-001** (full-screen refresh wiping booking work) is **closed — not reproducible** by anyone on the team as of 2026-07-08.

---

## Remaining (open / not done)

| ID | Status | What staff need | What exists today | Next step |
|----|--------|-----------------|-------------------|-----------|
| **CROSBY-006** | **Open** | Add/correct charges without constant workflow pain (Heather) | Charges editable **only while booking is DRAFT** and Charges step unlocked; **no add/edit/delete after accept**; DPS/grade **display** fixed (**CROSBY-012**) but not post-accept workflow | **Booking Amendments** design (supervisor append-only charges after accept) was implemented in a Cursor session but **never committed to git** — see plan `booking_amendments_system_29d83260.plan.md`. Does **not** include editing/deactivating accepted-era charges (by design). |
| **CROSBY-007** | **Fixed (verify at Crosby)** | Deputy-started drafts visible on CC Jail **In Booking Process** without manual refresh | **SignalR** `BookingInProgressChanged` on JLM facility group reloads in-progress list when deputy creates/accepts/voids/deletes (`6ecba0986`). Visibility rule unchanged: `JailAgencyId` = CC Jail. | Confirm: deputy creates draft, jail JCC open → row appears within ~1s without page refresh. |
| **CROSBY-014** | **Deferred (future version)** | Heather → PC Affidavit | Access still blocked after prior fix attempt | **Deferred to a future version**; revisit permission/menu/report audit when scheduled |

**Not in this visit but related:** Post-accept **booking amendments** (charges, property, classification/medical/MH worksheets) — planned and built in chat, **not in `wt-jail`**. Would address the **after-accept add charges** slice of **CROSBY-006** only; intake-time edit UX and correcting accepted-era charge rows remain separate.

---

## Fix status

| ID | Status | Summary |
|----|--------|---------|
| **CROSBY-001** | **Closed — not reproducible** | Reported full UI refresh on cell-check timer wiping in-progress booking work. **Not reproducible by anyone on the team** (2026-07-08). Related annoyance paths addressed by **CROSBY-002** (audio on reload). Reopen if Crosby provides steps + booking ID + device/browser. |
| **CROSBY-004** | **Fixed** | Manual cell/suicide check start: **Start Pass** (and cancel on manual passes) shown for users with `Rms.JailObservation.Modify`, not only full-support users (`JlmWorkQueuePanel.vue`). Manual passes also **reset the interval clock** on first observation (same cadence slip as automated passes). |
| **CROSBY-005** | **Fixed** | Booking Detail and Custody PDFs resolve **arresting officer** via officer catalog (or free text for jail-code/other source), not logged-in user lookup (`JailIntakeViewModelFactory.ResolveBookingArrestingOfficerDisplayAsync`). |
| *(related)* | **Fixed** | **Transporting officer** on Booking Detail and Custody PDFs had the same officer-vs-user ID bug; now uses `ResolveOfficerIdDisplayAsync` (officer catalog). Full audit of jail report factories: all other `*UserId` fields correctly use user lookup; JLM cell-check / transfer log reports verified. |
| **CROSBY-008** | **Fixed** | Mental health / suicide screening PDF and notification timestamps convert UTC → jail agency local (`FormatUtcToAgencyLocal`). UI auto-fill for notification datetimes uses `dateTimeHelper.getUtcDateTime()` (agency-local clock stored as UTC), not raw `toISOString()` UTC. |
| **CROSBY-009** | **Fixed** | Historical cell-check pass views merge **live board scope** with **pass entry episodes** so released inmates who were observed still appear (`GetPassWithRemainingAsync`, enriched pass grid entries, `observationPassStore` merge). |
| **CROSBY-010** | **Fixed** | Mid-pass release / stuck pass: **Cancel Pass** in pass runner (and on queue cards for all open passes) closes incomplete pass as **CANCELED**; recorded entries kept. **Complete Pass** sets pass **COMPLETED** (all inmates observed). System timeout at next round remains **MISSED**. Cancel reverts cadence slip so the next automatic check stays on the pre-slip schedule. |
| **CROSBY-011** | **Fixed** | Faster common observation codes: **quick-select buttons** (LAYING, SIT/STAND, FEEDING, TV, TALKING) beside the Observations dropdown in the cell-check pass runner (`jlmCellCheckConfig.ts`, `CellCheckInmateRow.vue`). Crosby prod top codes; full list remains in the dropdown. |
| **CROSBY-002** | **Fixed** | Cell-check / task audio no longer tied to unrelated refresh paths: **shared Notification sounds** dialog with global **Play Sounds** (browser permission), separate **JAIL** and **RMS Tasks** module prefs; playback gated by `canPlayJlmNotificationSound` / `canPlayRmsTaskNotificationSound` (global + permission + module + per-event). Task count sounds use RMS Tasks settings only (`NavBarNotifications.vue`). |
| **CROSBY-003** | **Fixed** | Louder defaults and per-module volume: shipped JAIL/RMS module volume **0.7**, JAIL playback rate **1.7**; volume sliders with preview in shared dialog; entry from JCC toolbar and system user popover (`AppAudioSettingsDialog.vue`, module tabs). |
| **CROSBY-007** | **Fixed (verify at Crosby)** | Deputy drafts not appearing on CC Jail **In Booking Process** while JCC left open: **JLM hub** event `BookingInProgressChanged` triggers `loadBookingsInProgress()` on facility group (`JlmBoardContainer.vue`, `JailIntakeService` broadcast on create/accept/void/delete). Not an agency-filter bug when `JailAgencyId` = CC Jail — was stale UI. Commit `6ecba0986`. |
| **CROSBY-012** | **Fixed** | DPS code and offense grade on booking charge display (magistrate workflow). |
| **CROSBY-013** | **Fixed** | Michael Marshall (`MMARSHALL`, AuthUsers Id 13) has **`JMS_SUPERVISOR`** (also `JMS_OFFICER`) in `AuthUserRoles` on ThinLineRMS — jail intake supervisor role includes `Rms.JailIntake.Approve` (step overrides, supervisor workflows). Verified 2026-06-24. |

**Does not satisfy CROSBY-006:** **CROSBY-012** improves charge **display** only. Accepted bookings still reject charge add/edit via `EnsureBookingWritableByCurrentUser`. Post-accept supervisor amendments were **designed but not merged** (see Remaining table).

**Verification:** `JailIntakeViewModelFactory_ArrestingOfficerReport_Tests` (6 tests); `JlmObservationRoundCadenceService_Tests` (slip + revert cadence); `JailIntakeViewModelFactory_ReportDateTime_Tests` (3 tests); `JlmObservationService_PassHistory_Tests` (released inmate on historical pass); `JlmObservationService_ClosePass_Tests` (cancel reverts cadence / complete preserves slip); `useAppPlaySounds.spec.ts`, `jlmNotificationRules.spec.ts`, `rmsTaskNotificationRules.spec.ts`, `appSoundDefaultsSnippet.spec.ts` (notification sound settings); `JailIntakeService_BookingInProgressHub_Tests` (JLM hub broadcast → in-progress list refresh).

---

## Priority matrix

| Priority | Item | Why |
|----------|------|-----|
| **P0 — data loss / workflow break** | Full screen refresh on cell-check timer | Can destroy unsaved booking work — **closed (CROSBY-001): not reproducible** |
| **P0 — workflow break** | Cannot finish cell check after mid-pass release | Pass stuck with no recovery — **fixed (CROSBY-010)** |
| **P1 — incorrect output** | Booking sheet wrong officer name | Legal/paper trail mismatch — **fixed (CROSBY-005 + transporting officer)** |
| **P1 — high user pain** | Add/edit charges | Heather: constant correction work — **still open (CROSBY-006)**; no post-accept charge path in prod |
| **P1 — visibility** | Deputy bookings not on CC Jail board | **Fixed (CROSBY-007):** SignalR refresh; verify at site |
| **P2 — functional gap** | Cannot start cell check manually | Lunch / ad-hoc schedule — **fixed (CROSBY-004)** |
| **P2 — incorrect display** | Suicide screening date/time (UTC) | Wrong timestamps on screening — **fixed (CROSBY-008)** |
| **P2 — regression / bug** | Released inmates missing from past cell checks | They value historical logs — **fixed (CROSBY-009)** |
| **P2 — annoyance** | Audio on every refresh | Noise fatigue; undermines useful alerts — **fixed (CROSBY-002)** |
| **P3 — polish** | Bigger/louder audio | Enhancement on liked feature — **fixed (CROSBY-003)** |
| **P3 — UX** | Sort observation codes by recent use | Reduces code lookup friction — **fixed (CROSBY-011):** quick-select buttons for top codes |
| **P3 — display** | DPS code + offense grade on booking | Magistrate workflow |
| **Ops** | Michael → Jail Admin | **Fixed (CROSBY-013):** `MMARSHALL` has `JMS_SUPERVISOR` |
| **Ops / investigate** | Heather → PC Affidavit | Reported broken after prior discussion — **deferred to a future version (CROSBY-014)** |

---

## By product area

### 1. JCC — cell checks & observation passes

| # | Type | Issue | Interpretation |
|---|------|-------|----------------|
| 1a | **Bug** | Whole screen refreshes when cell-check timer fires | Not a subtle data refresh — staff perceive a **full UI reset**. If booking is open, **in-progress work is lost**. Likely tied to pass/timer hub events, `loadPasses()` / `loadQueue()` cascades, or an overly broad parent remount — not just row-level updates. **Closed (CROSBY-001): not reproducible** by anyone on the team (2026-07-08). Reopen with repro steps if it recurs. |
| 1b | **Bug** | Audio plays on every refresh, even when no cell check | Notification logic probably fires on **queue/pass reload**, not only when a pass is actually due. Coupled with 1a. **Fixed (CROSBY-002):** global Play Sounds + module prefs; JAIL vs RMS Tasks separation; playback rules require global, permission, and per-event toggles. |
| 1c | **Enhancement** | Bigger, louder audio | They like alerts; want **stronger visual + volume** for kiosk/tablet use. **Fixed (CROSBY-003):** shared Notification sounds dialog, module volume sliders, tuned shipped defaults (0.7 volume, JAIL 1.7× playback). |
| 1d | **Bug / gap** | Cannot start a check unless the timer starts it | Need **manual/ad-hoc pass start** (e.g. 11:45 check + separate 12:00 lunch check). **Fixed (CROSBY-004):** Start Pass for `Rms.JailObservation.Modify`; manual pass resets interval on first observation. |
| 1e | **Bug** | Released inmates no longer in **past** cell check logs | Historical pass view should still show inmates who were in custody during that pass, even after release. **Fixed (CROSBY-009):** pass runner and pass grid union live scope with entry-backed rows for released episodes. |
| 1f | **Bug** | Mid-pass release after entering a code → pass cannot be completed | Need **cancel / abandon pass** and restart. **Fixed (CROSBY-010):** Cancel Pass in runner + queue; Complete Pass still requires all inmates observed; cancel reverts cadence slip so the next automatic check stays on the pre-slip schedule. |
| 1g | **Enhancement** | Sort observation codes by **most recently used** | Reduces debate over search/order during checks. **Fixed (CROSBY-011):** one-click **quick-select buttons** for Crosby’s top codes (L, D, F, P, T) beside the full Observations dropdown — no MRU sort in the list. |

**Likely code touchpoints:** `JlmWorkQueuePanel.vue` (timer-driven `loadPasses`/`loadQueue`, 30s poll fallback), `JlmPassRunner.vue` (`loadPass` on observation events), JLM task/pass generation services, cell-check notification composable.

---

### 2. Jail booking & intake

| # | Type | Issue | Interpretation |
|---|------|-------|----------------|
| 2a | **Bug** | Booking **print** shows wrong officer (Eric's name) while UI shows correct arresting officer | Eric's "wrong ID" guess is plausible: print may use **current user / booking officer** instead of **arresting officer**, or mis-map `ArrestingOfficerId` vs free text vs jail-code source. **Fixed (CROSBY-005):** arresting officer + transporting officer on Booking Detail / Custody PDFs use officer catalog (or arresting free text by source). |
| 2b | **Bug / recurring** | Add/edit charges — major pain for Heather | Not new; she's **fixing upstream errors** repeatedly. **Still open (CROSBY-006):** charges only editable in **DRAFT**; after **accept**, API throws *"no further edits are allowed"* for add/update/delete. **CROSBY-012** added DPS/grade on display but not post-accept workflow. Planned **Booking Amendments** (supervisor append-only charges after accept) was never committed — see Remaining table. |
| 2c | **Bug** | Deputy-started bookings not on **CC Jail** board | Staff saw missing rows while JCC stayed open. **Fixed (CROSBY-007):** in-progress list did not auto-refresh; JLM hub `BookingInProgressChanged` reloads list. Bookings with correct `JailAgencyId` were always visible after refresh/search. |
| 2d | **Enhancement** | Show **DPS code** and **offense grade** on booking | Today mostly description; magistrate workflow needs grade + DPS/offense number. |

**Likely code touchpoints:** `BookingDetailReportModel` / `JailIntakeViewModelFactory` (print officer fields), `JlmBoardContainer.vue` ("In Booking Process"), booking charge UI and offense display models.

---

### 3. Suicide screening

| # | Type | Issue | Interpretation |
|---|------|-------|----------------|
| 3a | **Bug** | Wrong date/time on suicide screening | Classic **UTC displayed without agency-local conversion** (or missing timezone on print/display). **Fixed (CROSBY-008):** mental health PDF + notification fields; UI default notification timestamps. |

---

### 4. Configuration & access (no code required until investigated)

| # | Type | Request | Notes |
|---|------|---------|-------|
| 4a | **Config** | Michael → **Jail Admin** | Heather approved — role/permission assignment. **Fixed (CROSBY-013):** `MMARSHALL` assigned **`JMS_SUPERVISOR`** (+ `JMS_OFFICER`) in `AuthUserRoles`. |
| 4b | **Config / bug** | Heather → **PC Affidavit** access | She says prior discussion with Matt didn't fix it. **Deferred to a future version (CROSBY-014).** When revisited, needs a **permission audit**: role, feature flag, agency module, report route, or incident/court module gate. |

---

## Cross-cutting themes

1. **Cell-check timer = disruptive event** — refresh, audio, and possibly navigation shared one trigger path; **CROSBY-002** fixed audio-on-reload. **CROSBY-001** (full-screen wipe) **not reproducible** (2026-07-08).
2. **Agency boundaries** — wrong officer on print and missing CC Jail bookings both smell like **identity/agency field confusion** (who booked vs who arrested vs which agency owns the row).
3. **Historical accuracy** — past cell checks and suicide screening timestamps are **audit/compliance** issues, not cosmetic.
4. **Heather as power user** — charges + PC Affidavit + admin approvals cluster on **intake/supervisor** workflow.

---

## Suggested investigation order

1. ~~**Reproduce cell-check timer refresh** — booking form open, wait for due/overdue/pass event; confirm whether it's component remount, route navigation, or full `location.reload`.~~ **Closed — CROSBY-001: not reproducible (2026-07-08).**
2. ~~**Trace audio trigger** — log when notifications fire vs when `loadPasses` runs.~~ **Done — CROSBY-002 (shared sound settings + gated playback).**
3. ~~**Booking print officer** — compare UI binding (`arrestingOfficerId` / `arrestAgencySource`) to report model `ArrestingOfficer` vs `BookingOfficerName`.~~ **Done — CROSBY-005 (+ transporting officer audit).**
4. ~~**CC Jail board filter** — deputy booking: `jailAgencyId`, `arrestAgencyId`, and "in booking process" query.~~ **Addressed — CROSBY-007:** SignalR refresh for in-progress list; verify at Crosby.
5. ~~**Past cell check with released inmates** — pass snapshot vs live episode list.~~ **Done — CROSBY-009.**
6. ~~**Cancel pass API/UI** — does abandon exist but hidden, or missing entirely?~~ **Done — CROSBY-010.**
7. ~~**Heather PC Affidavit** — effective permissions vs menu entry.~~ **Deferred to a future version — CROSBY-014.**
8. ~~**Michael Jail Admin** — assign role in admin.~~ **Done — CROSBY-013:** `MMARSHALL` → `JMS_SUPERVISOR`.
9. **CROSBY-006 charges** — confirm with Heather: pain is **during draft** vs **after accept**; prioritize restoring **Booking Amendments** (post-accept add-only) from plan if after-accept.

---

## Backlog mapping (existing repo)

| Feedback | Related backlog / plans |
|----------|-------------------------|
| JCC / cell checks | **BL-003** JCC verify plan (`JlmBoardContainer`, pass runner, cell check UI) |
| Booking charges | **BL-002** jail booking verify (charges step); **Booking Amendments** plan (post-accept add — not in repo) |
| DPS on booking | **BL-006** DPS conviction report is court-side; booking DPS display may be separate work |

---

## Open questions for Eric / Crosby

1. **Booking sheet** — which report/template (booking detail PDF, custody sheet, etc.) and a booking ID for the officer mismatch?
2. ~~**Refresh** — tablet JCC only, or desktop too? Does the URL change or only form content clear?~~ **CROSBY-001 closed — not reproducible;** keep question if staff report again.
3. **CC Jail** — specific deputy agency vs Crosby jail agency names/IDs?
4. **PC Affidavit** — exact menu path Heather uses and error (hidden menu vs denied vs empty report)?
5. **Manual cell check** — policy: any user anytime, or supervisor-only?

---

## Numbered ticket titles (ready to paste)

| ID | Title | Status |
|----|-------|--------|
| **CROSBY-001** | BUG: Cell-check timer causes full screen refresh and loses in-progress booking | **Closed — not reproducible** (2026-07-08) |
| **CROSBY-002** | BUG: Cell-check audio fires on pass queue refresh, not only when check is due | **Fixed** |
| **CROSBY-003** | ENH: Increase cell-check alert size and volume | **Fixed** |
| **CROSBY-004** | BUG: Cannot manually start cell check outside scheduled timer | **Fixed** |
| **CROSBY-005** | BUG: Booking print shows logged-in user instead of arresting officer | **Fixed** |
| **CROSBY-006** | BUG: Add/edit charges workflow — recurring correction pain (Crosby) | **Open** — no post-accept charges; amendments plan not merged |
| **CROSBY-007** | BUG: Deputy bookings from other agency not visible on CC Jail board | **Fixed (verify)** — JLM SignalR in-progress refresh |
| **CROSBY-008** | BUG: Suicide screening displays UTC instead of agency local time | **Fixed** |
| **CROSBY-009** | BUG: Released inmates missing from historical cell check logs | **Fixed** |
| **CROSBY-010** | BUG: No way to cancel/abandon stuck cell check after mid-pass release | **Fixed** |
| **CROSBY-011** | ENH: Sort cell-check observation codes by most recently used | **Fixed** (quick-select buttons) |
| **CROSBY-012** | ENH: Show DPS code and offense grade on booking charge display | **Fixed** |
| **CROSBY-013** | CONFIG: Grant Michael Jail Admin (Heather approved) | **Fixed** — `MMARSHALL` has `JMS_SUPERVISOR` |
| **CROSBY-014** | CONFIG/INVESTIGATE: Heather PC Affidavit access still blocked | **Deferred (future version)** |

### Flat list (copy/paste)

1. ~~BUG: Cell-check timer causes full screen refresh and loses in-progress booking~~ **Closed (CROSBY-001 — not reproducible, 2026-07-08)**
2. ~~BUG: Cell-check audio fires on pass queue refresh, not only when check is due~~ **Fixed (CROSBY-002)**
3. ~~ENH: Increase cell-check alert size and volume~~ **Fixed (CROSBY-003)**
4. ~~BUG: Cannot manually start cell check outside scheduled timer~~ **Fixed (CROSBY-004)**
5. ~~BUG: Booking print shows logged-in user instead of arresting officer~~ **Fixed (CROSBY-005)**
6. BUG: Add/edit charges workflow — recurring correction pain (Crosby) — **Open (CROSBY-006)**
7. ~~BUG: Deputy bookings from other agency not visible on CC Jail board~~ **Fixed (CROSBY-007 — verify SignalR refresh at site)**
8. ~~BUG: Suicide screening displays UTC instead of agency local time~~ **Fixed (CROSBY-008)**
9. ~~BUG: Released inmates missing from historical cell check logs~~ **Fixed (CROSBY-009)**
10. ~~BUG: No way to cancel/abandon stuck cell check after mid-pass release~~ **Fixed (CROSBY-010)**
11. ~~ENH: Sort cell-check observation codes by most recently used~~ **Fixed (CROSBY-011 — quick-select buttons)**
12. ~~ENH: Show DPS code and offense grade on booking charge display~~ **Fixed (CROSBY-012)**
13. ~~CONFIG: Grant Michael Jail Admin (Heather approved)~~ **Fixed (CROSBY-013 — `MMARSHALL` / `JMS_SUPERVISOR`)**
14. ~~CONFIG/INVESTIGATE: Heather PC Affidavit access still blocked~~ **Deferred to a future version (CROSBY-014)**

---

## Original raw notes

```text
Eric Gibson went to visit with Jail staff at Crosby on 6/18/2026 to get feedback from their time using the software.

Bugs:
- Booking sheet prints the incorrect officer name. UI shows correct arresting officer; print shows my user name (Thin Line Support / Eric G). Wrong ID?
- Constant screen refreshes when cell-check timer fires; wipes in-progress booking work.
- Audio: love it but want bigger/louder; audible on every refresh even when no cell check.
- Cell check cannot be started manually (only when timer starts) — lunch schedule example 11:45 + 12:00.
- Add/Edit Charges — big deal to Heather; correcting errors constantly.
- Deputy bookings not showing on CC Jail — different agency?
- Suicide screening wrong date/time — UTC vs local?
- Released prisoners no longer in past cell check logs (they love seeing those logs).
- Started cell check, entered code, released inmate mid-pass, could not finish — need cancel/restart.

Enhancements:
- Cell check codes: sort by most recently used?
- DPS code and offense grade on booking (not just description).

Configuration:
- Michael → Jail Admin (Heather OK).
- Heather → PC Affidavit access (talked to Matt, still broken).
```
