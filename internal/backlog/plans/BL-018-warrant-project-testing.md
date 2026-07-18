---
backlog: "BL-018 · Court Violations · Warrant project — finish testing"
status: draft
created: 2026-03-30
client: internal
---

# Plan: BL-018 — Warrant project (manual test plan)

## Goal

The **warrant / court-violation warrant** work is **in testing**. Use this document as a **manual regression checklist** for the changes shipped over roughly the **past week** (relative to branch activity), before calling the warrant project **done** for the current release.

**This is not implementation** — it is **verification**. Pair with **`dotnet test`** on `ThinLine.API.UnitTests` for warrant/court lifecycle coverage; this plan covers **end-to-end** and **UI/PDF** behavior.

---

## Scope (from recent change themes)

Derived from recent commits on the court/warrant line, including:

| Theme | What to exercise |
|-------|-------------------|
| **Lifecycle + state machine** | `CourtViolationWarrantLifecycleService` — issue FTA warrant, CPF warrant paths, **recall**, **Mark warrant executed**, **Modify show cause date**, sync after transitions. |
| **Capias Pro Fine (CPF)** | CPF warrant state, **Capias Pro Fine** document rendering, transitions involving CPF FTC / hearings. |
| **MarkWarrantExecuted** | Court UI transition (**show cause** date, default **+21 calendar days** where applicable), optional **waive/remove** fees and OmniBase hold, **FTA** vs **CPF** post-states. |
| **PD / service completion** | `WarrantServiceCompletionOrchestrator` — completing warrant service triggers **MarkWarrantExecuted** when eligible (**FTA_WARRANT** / **CPF_WARRANT**); verify court violation updates and **best-effort** behavior if transition fails. |
| **Warrant service fields** | **Arresting officer 1 / 2**, **service attestation** / **service officer** fields (per current model), **WarrantDetailsTabServices** initialization. |
| **Issuance & attachments** | **Issued warrant PDF** attachment; **officer’s return** attachment flow. |
| **Fees** | **Warrant fee** handling in workflow + UI where applicable (**waive** paths in MarkWarrantExecuted dialog). |
| **Reports / PDFs** | Warrant-related **report models**: officer **badge number**, **electronic signature** / **agency seal**, **UserDisplayNameForElectronicRecord**, conditional **officer’s return** by document mode, **ElectronicIssuedTimestamp**. |
| **UI** | Court violation timeline / warrant tab (**badges**, service sections), attachment/PDF viewer behavior if touched. |

Adjust sections if your test environment does not use **OmniBase** or certain fee codes — mark **N/A** and note why.

---

## Preconditions

- [ ] Test **court agency** and **LE agency** (if PD completes service) configured with **seal/signature** attachments if you are validating PDFs.
- [ ] Users with appropriate **court** and **LE** roles for warrant issue, recall, mark executed, and warrant service completion.
- [ ] At least one **non-production** court violation that can move through **FTA** and/or **CPF** warrant states without affecting real cases (or use demo reset scripts only where allowed).

---

## A. Issue and recall warrants (court)

- [ ] **Issue FTA warrant** — Transition **Issue Fta Warrant** (or equivalent UI): violation enters **FTA warrant** state; **new warrant record** created; **warrant number** assigned per product rules.
- [ ] **Issue / reinstate CPF warrant** — Paths that create or reinstate **CPF warrant** (e.g. **Failed To Appear Reinstate Cpf Warrant** where applicable): **Capias Pro Fine** warrant type behaves correctly.
- [ ] **Recall warrant** — **RecallWarrant**: active warrant closed/recalled per lifecycle; linked violation state matches expectation.
- [ ] **Attachments on issue** — **Issued warrant PDF** attaches to the case/warrant as designed; opens in viewer; correct **warrant number** on document.

---

## B. Mark warrant executed (court UI)

- [ ] **Eligible states** — From **FTA_WARRANT** and **CPF_WARRANT**, **MarkWarrantExecuted** appears and runs.
- [ ] **Show cause date** — User can set **show cause**; verify **default +21 calendar days** from agency “today” when left blank (per state definition / `ComputeMarkWarrantExecutedShowCauseDate`).
- [ ] **Optional fee / hold actions** — Where enabled: **remove OmniBase fee**, **waive FTA fee**, **waive warrant fee**, **remove OmniBase hold** — each combination updates **financial** and **timeline** as expected (no duplicate fees).
- [ ] **Event note** — Note persists on timeline / internal history.
- [ ] **Post-transition state** — Case lands in correct **FTA** or **CPF FTC** (failure to comply / show cause) per definition; **workflow status** matches.
- [ ] **Linked warrants cleared** — After execute: active warrants move to **cleared** / workflow completed per `ClearLinkedWarrantsAfterMarkExecutedAsync`; **recalled** warrants skipped as designed.

---

## C. PD / warrant service completion (LE)

- [ ] **Complete service** — Record warrant service through LE workflow through **completion** with **officer’s return** as required.
- [ ] **Auto MarkWarrantExecuted** — When linked **court violation** is still in **FTA_WARRANT** or **CPF_WARRANT**, completion triggers **MarkWarrantExecuted** (empty payload path); court side shows updated state and **show cause** handling.
- [ ] **Idempotency** — Completing service when warrant already cleared does not corrupt data.
- [ ] **Failure path** — If transition fails (simulate validation): **officer’s return** still saved; **warning logged** — user-visible outcome documented (no silent rollback of LE data).

---

## D. Warrant service record (fields & UI)

- [ ] **Arresting officer 1 / 2** — Save, reload, and appear on warrant service detail and **reports**.
- [ ] **Service attestation / service officer** — Fields match current API/UI names; required validation when policy requires it.
- [ ] **WarrantDetailsTabServices** — Tab loads without error; **service** section initializes when opening existing vs new service.

---

## E. Reports and PDFs (warrant-related)

- [ ] **Officer badge** — Badge appears on warrant/officer return output where implemented.
- [ ] **Electronic signature / seal** — Agency **signature** and **seal** images render on **electronic** court documents; missing assets fail gracefully.
- [ ] **User display name** — Clerk/judge/officer names format correctly on **electronic** records (`UserDisplayNameForElectronicRecord` behavior).
- [ ] **Officer’s return** — Renders or suppresses based on **document mode** / rules; matches preview vs print.
- [ ] **Electronic issued timestamp** — Present when expected on issued documents.
- [ ] **Capias Pro Fine** — Specific document type renders **correct template** and content blocks.

---

## F. Financial and timeline

- [ ] **Warrant fees** — Issuance and waiver paths post correct **ledger** / **timeline** entries (pair with accounting if fees post to GL).
- [ ] **Waivers** — **Waive FTA / warrant fee** from **MarkWarrantExecuted** dialog reflects on **court violation financial** summary.

---

## G. Master person warrant visibility (PD parity)

Verify court-owned warrants visible in **warrant search** also appear on the **master person** card for PD users **without** a court→PD agency share configured.

- [ ] **Warrant search** — As **PD user**, issue or locate an active **court-generated** warrant (FTA/CPF); confirm it appears in warrant search (default **ACT** filter).
- [ ] **ACTIVE WARRANT chip** — Open the subject's master person card; **ACTIVE WARRANT** chip is visible; popover lists warrant number / summary lines.
- [ ] **Records tab** — Same person → **Records** tab lists the warrant row (all statuses: active, cleared, recalled after lifecycle events).
- [ ] **No agency share required** — Repeat with **no** explicit share from court agency to PD; PD still sees warrant on person card and records.
- [ ] **Court user scope** — As **court user**, master person shows **only that court's** warrants — not another court's or unshared PD warrants.
- [ ] **WAR tag sync** — After issue/clear/recall, person search **WAR** tag and person-card chip stay consistent when viewed as PD (lifecycle refresh).

---

## H. Regression and non-functional

- [ ] **Court violation timeline** — No duplicate or missing entries after warrant issue, recall, execute, and PD completion.
- [ ] **Code descriptions** — Any new/changed codes display **ALL CAPS** descriptions in UI and reports (per project rule).
- [ ] **Attachments** — Large PDFs; **AttachmentPdfViewerDialog** selection behavior if users switch between multiple warrant attachments.

---

## I. Sign-off

| Role | Name | Date | Notes |
|------|------|------|--------|
| Tester | | | |
| Product / court SME | | | |

---

## Changelog

| Date | Notes |
|------|--------|
| 2026-05-28 | Added master person warrant visibility parity scenarios (PD vs court, Records tab, ACTIVE WARRANT chip). |
