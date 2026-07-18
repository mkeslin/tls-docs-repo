---
backlog: "BL-019 · Court / Accounting · Shallowater Municipal Court go-live"
status: draft
created: 2026-03-30
client: Shallowater Municipal Court
---

# Plan: BL-019 — Shallowater Municipal Court — exclusive go-live

## Goal

**Shallowater Municipal Court** is moving to **Thin Line RMS court and accounting** as the **system of record**. This plan captures:

1. **Setup and validation** — configuration, users, and smoke tests before relying on production traffic.
2. **Training outlines** — one combined **clerk / judge** role and a separate **accountant** track.
3. **Credit card decision** — confirm whether they want **card payments** in RMS; if yes, schedule **Stripe** setup, **mobile citation QR** (or equivalent), and related training (**section H**).

**Not implementation** — operational checklist. Adjust rows to match your **actual** chart of accounts, banks, and court processes.

**Related:** **BL-010** (bad images / 500) references **ShallowaterPD** — confirm image-heavy workflows during UAT if still open.

---

## A. Environment and access

- [ ] **Production URL(s)** — Bookmarked; **HTTPS** valid; **PWA** / offline expectations communicated if used.
- [ ] **Agency record** — **Shallowater Municipal Court** (or correct legal name) in **Admin → Agency**: address, **seal**, **signature** for **electronic** documents, **time zone**, **court** vs **municipal** flags per your deployment.
- [ ] **User accounts** — **Clerk/judge** login(s), **accountant** login(s), **backup** admin; **password policy** and **MFA** if enabled.
- [ ] **Claims / roles** — Court Violations (view/modify/approve as needed), **Accounting** (posting, batches, reports), **Masters** if they maintain persons; **no excess** privilege.
- [ ] **Support path** — Who to call for **P1** issues (internal escalation list).

---

## B. Court module — configuration

- [ ] **Fine schedules / codes** — Speeding ranges, offense codes, **FTA** / **warrant** fees align with **ordinance** and **state reporting** needs.
- [ ] **Workflow** — Court violation **procedural states** understood for daily docket (FTA, judgments, warrants, **payment plans**, etc.).
- [ ] **Calendar / docket** — **Hearing** and **show cause** dates; work queue if used.
- [ ] **OCA / state reporting** — If required: **agency IDs**, **report periods**, **upload** credentials (see **BL-001** / **BL-017** as applicable).
- [ ] **Prints** — Citation detail PDF, **court violation** search PDF, **payment plan** PDFs — **letterhead** and **signature** correct.

---

## C. Accounting module — configuration

- [ ] **Third-party collections fee code** — Legacy INCODE conversion used **`IM_COLAGY`**; RMS collections requires **`TPC`**. Before go-live on collections UI/remittance/disbursement, run product-repo `Scripts/CourtViolation/Shallowater-Reclassify-ImColagy-To-Tpc.sql` (preflight, then apply with real vendor name via product-repo `Scripts/CourtViolation/Invoke-Shallowater-ColagyToTpcApply.ps1`). Set **Collection vendor** in Admin; replace any placeholder vendor string. Finance: review historical GL for `IM_COLAGY` posted to `AGENCY_FEE_REVENUE`.
- [ ] **Fiscal setup** — **Funds**, **GL mapping** (or equivalent), **revenue** accounts for fines/fees/costs.
- [ ] **Payment methods** — Cash, check, and **card** only if integrated (**section H** — confirm their intent); **waiver** / **community service** as used.
- [ ] **Bank accounts** — **Deposit** accounts tied correctly; **reconciliation** owner named.
- [ ] **Fees and distributions** — Court fees post to intended **accounts**; **bond** / **refund** paths if municipal court uses them (**BL-004** / **BL-005** / **BL-009** awareness).
- [ ] **Batches** — **Daily** or **period** batch process agreed; **cutoff** time for “day’s receipts.”
- [ ] **Grid prints** — Key accounting grids have **print** where staff expect (**BL-015**).

---

## D. Integration between court and accounting

- [ ] **Payment on a case** — Fine payment flows from **court violation** into **accounting** (receipt, allocation, balance).
- [ ] **Refunds / voids** — Process and **audit trail** understood; permissions restricted.
- [ ] **Reporting** — **Court** revenue reports tie to **accounting** totals for a **test day** (reconcile sample).

---

## E. End-to-end smoke tests (go / no-go)

Run in **production** only after **A–D**; prefer a **pilot morning** with low volume.

**Court / clerk**

- [ ] Log in; open **court violation** list and **one** case by number.
- [ ] Create or update a **citation-linked** (or test) violation through a **harmless** transition (or **training** copy in **non-prod** first).
- [ ] Record a **payment**; print **receipt**; verify **balance**.
- [ ] **Warrant path** (if used): issue → **recall** or **execute** on **test** case in **non-prod** first; production only if policy allows.

**Accounting**

- [ ] Post **sample** payment batch (or first real batch with **double-check**).
- [ ] Run **end-of-day** / **period** report; compare to **court** cash summary.
- [ ] **Export** to bookkeeping tool if used (CSV, GL, etc.).

**Data**

- [ ] **Backup** / **restore** expectations confirmed with host (who runs backups, RPO/RTO).
- [ ] **Person** / **master** data — **Duplicate** person policy (merge vs alias).

---

## F. Training — clerk / judge (same person)

*Single schedule block or split days; tailor depth to prior system.*

| Topic | Objective |
|-------|-----------|
| **Navigation** | Modules, **court violation** search, **person** lookup, **calendar** / docket. |
| **Case lifecycle** | Pleas, judgments, **FTA**, **payment plans**, **disposition** programs (if enabled). |
| **Financial actions** | Assess fines/fees, **waive** per policy, **payments**, **receipts**, **refunds** (who approves). |
| **Warrants** | Issue, **recall**, **mark executed**, relationship to **LE** / warrant service (if applicable). |
| **Documents** | Generate **PDFs**, **attachments**, **electronic signature** / seal on prints. |
| **Reporting** | **OCA** or state reports, **ad hoc** lists, **audit** / timeline reading. |
| **Support** | When to call IT vs vendor; **known issues** (e.g. **BL-010** image errors). |

**Hands-on:** 2–3 **guided** exercises with **checklists** (open case, take payment, print receipt, find timeline entry).

---

## G. Training — accountant

| Topic | Objective |
|-------|-----------|
| **Chart / funds** | Where **fine** and **fee** revenue lands; **restricted** vs **general**. |
| **Receipting** | Matching **court** receipts to **batches**; **corrections** process. |
| **Deposits** | **Bank** reconciliation cadence; **undeposited** funds report. |
| **Bonds / refunds** | If used: **bond** batches (**BL-004**), **refund** batches (**BL-009**) — awareness. |
| **Period close** | **Month-end** steps; **variance** investigation. |
| **Exports** | **GL** or **CPA** handoff format and **schedule**. |

**Hands-on:** Build **one** batch from **court** activity; run **two** standard reports and **tie** to court **cash**.

---

## H. Credit card payments — inquiry and follow-on

**Day-one go-live** can be **cash/check only**. Use this block to **discover** intent and to track **follow-on work** if they choose card acceptance in RMS.

### Inquiry (conversation with court / accountant)

- [ ] **Do they want credit/debit card payments** through Thin Line RMS (vs cash/check only, or vs a separate terminal outside RMS)?
- [ ] **Who pays** — window only, **online** / defendant self-service, or both?
- [ ] **Settlement** — expectations for **deposit timing**, **fees** (Stripe/processing), and **reconciliation** with daily court receipts.
- [ ] **PCI / policy** — Any municipal or card-network constraints; who approves turning on **electronic** payments.

### If they decide to proceed — implementation checklist

*Not part of exclusive go-live unless explicitly scheduled; coordinate with billing/security boundaries per ``AGENTS.md`` (product repo `AGENTS.md`) (Stripe / payments are risk-sensitive).*

- [ ] **Stripe** — Configure **Stripe** for the court/agency context (keys, webhooks, fee handling, environment separation).
- [ ] **Mobile citations** — Add **QR code** (or payment **deep link**) on **mobile citation** output so defendants can pay electronically, consistent with product patterns.
- [ ] **Court / accounting linkage** — Card payments **post** to the same **receipting** and **batch** flows as other methods; **test** in non-production first.
- [ ] **Training add-on** — Clerk/judge and accountant: taking a **card** payment, **refunds**/voids, and reading **Stripe** settlement vs **RMS** batches.

---

## I. Sign-off

| Item | Owner | Date |
|------|-------|------|
| Court config complete | | |
| Accounting config complete | | |
| Clerk/judge training done | | |
| Accountant training done | | |
| Go-live approval | | |
| Credit card decision (inquiry complete; Stripe/QR scheduled or N/A) | | |

---

## Changelog

| Date | Notes |
|------|--------|
| 2026-03-30 | Initial go-live checklist and training outlines for Shallowater Municipal Court. |
| 2026-03-30 | Section H: credit card inquiry + follow-on (Stripe, mobile citation QR, training). Sign-off renumbered to I. |
