# Prioritized backlog

**Source:** Processed from product-repo `Backlog/raw/BacklogWorkItems.csv`. Numeric **Priority** in the dump is treated as **lower = more urgent** (1 = highest).

**Archived copy (product monorepo):** `Backlog/archive/2026-03-30-042748-BacklogWorkItems.csv`

**Canonical location:** Internal Docs — [Backlog & design](README.md).

## Backlog IDs (`BL-###`)

Each work item has a stable **`BL-###`** identifier (zero-padded three digits). IDs are assigned once and **do not change** when you reorder priorities or edit wording. Use them in commits, plans, and chat (“pick up **BL-015**”).

| ID | Module | Work item |
|----|--------|-----------|
| **BL-001** | Court Violations | OCA Report — verify February data |
| **BL-002** | Jail | Finish booking |
| **BL-003** | Jail | Finish jail command center |
| **BL-004** | Accounting | Bonds — create bond batch/export |
| **BL-005** | Court Violations | Bonds — finish bond logic |
| **BL-006** | Court Violations | DPS conviction report |
| **BL-007** | Court Violations | State quarterly accounting report |
| **BL-008** | General | Device fingerprinting |
| **BL-009** | Accounting | Refund batch |
| **BL-010** | Data | Bad images causing 500 (ShallowaterPD) |
| **BL-011** | Masters | Add relationships to reports |
| **BL-012** | Court Violations | Omnibase |
| **BL-013** | Court Violations | UI for editing speeding ranges |
| **BL-014** | Person | Criminal trespass |
| **BL-015** | Accounting | Grid prints (all accounting grids/tables) |
| **BL-016** | General | Default values table |
| **BL-017** | Court Violations | OCA Report — finish PDF |
| **BL-018** | Court Violations | Warrant project — finish testing |
| **BL-019** | Court / Accounting | Shallowater Municipal Court — go-live |
| **BL-020** | Security | Harden Descope cookie revocation on logout (CJIS IA-11 defense-in-depth) |
| **BL-021** | UI | Classic layout — `TlsPage` main-column shell (Web Awesome migration seam) |
| **BL-022** | CAD | Large-agency remediation — dispatch board, SignalR scale-out, UX/ops ([`plans/BL-022-cad-large-agency-remediation.md`](plans/BL-022-cad-large-agency-remediation.md)) |
| **BL-023** | Court / Accounting | Collections — supplemental item-level referrals (Art. 103.0031) |

---

## P0 — Now (priority 1)

| ID | Module | Work item | Notes |
|----|--------|-----------|--------|
| BL-001 | Court Violations | OCA Report | Verify February data + OCA upload. **→ Plan:** [`plans/BL-001-oca-february-verify.md`](plans/BL-001-oca-february-verify.md) |
| BL-002 | Jail | Finish Booking | Finalize each part. **→ Plan:** [`plans/BL-002-jail-booking-verify.md`](plans/BL-002-jail-booking-verify.md) |
| BL-003 | Jail | Finish Jail Command Center | Finalize each part. **→ Plan:** [`plans/BL-003-jcc-verify.md`](plans/BL-003-jcc-verify.md) |
| BL-018 | Court Violations | Warrant project — finish testing | In testing; **→ Plan:** [`plans/BL-018-warrant-project-testing.md`](plans/BL-018-warrant-project-testing.md) |
| BL-019 | Court / Accounting | Shallowater Municipal Court — go-live | Exclusive court/accounting; **→ Plan:** [`plans/BL-019-shallowater-municipal-court-golive.md`](plans/BL-019-shallowater-municipal-court-golive.md) |

---

## P1 — Next (priority 2–3)

| ID | Module | Work item | Notes |
|----|--------|-----------|--------|
| BL-005 | Court Violations | Bonds | Finish implementing bond logic. |
| BL-004 | Accounting | Bonds | Create bond batch/export. |
| BL-007 | Court Violations | State Quarterly Accounting Report | Finish implementing. |
| BL-006 | Court Violations | DPS Conviction Report | **Waiting on specs** before completion. |

---

## P2 — Soon (priority 4–6)

| ID | Module | Work item | Notes |
|----|--------|-----------|--------|
| BL-008 | General | Device Fingerprinting | AuthDevices table and new claims. |
| BL-011 | Masters | Add relationships to reports | Display relationships on master printouts. |
| BL-009 | Accounting | Refund Batch | Create refund batch/export. |
| BL-010 | Data | Bad images causing 500 | Handle image errors in UI. **Client:** ShallowaterPD. |
| BL-013 | Court Violations | UI for editing speeding ranges | New table + UI for fine ranges. |
| BL-012 | Court Violations | Omnibase | **Blocked** — confirm dependency. |
| BL-014 | Person | Criminal trespass | Best way to show on person. **→ Plan:** [`plans/BL-014-criminal-trespass.md`](plans/BL-014-criminal-trespass.md) |
| BL-020 | Security | Harden Descope cookie revocation on logout | CJIS IA-11 defense-in-depth: close the cross-tab cap-reset edge case if `sdk.logout()` fails to revoke the session cookie. **→ Plan:** [`plans/BL-020-cjis-logout-cookie-revocation.md`](plans/BL-020-cjis-logout-cookie-revocation.md) |
| BL-021 | UI | Classic layout — `TlsPage` shell | Stable main-column wrapper for Classic (`banners` + default); future `wa-page` backing. **→ Plan:** [`plans/BL-021-tls-page-shell-classic-layout.md`](plans/BL-021-tls-page-shell-classic-layout.md) |
| BL-022 | CAD | Large-agency remediation | Dispatch board read model, SignalR scale-out, notifier parity (notes/modules), UX/ops. **→ Plan:** [`plans/BL-022-cad-large-agency-remediation.md`](plans/BL-022-cad-large-agency-remediation.md) |
| BL-023 | Court / Accounting | Collections — supplemental item-level referrals | Per-fee/item past-due clocks + referral status under Art. 103.0031(b)/(f). **Interim today:** recall → (reverse unpaid TPC if needed) → re-refer. **→ Plan:** [`plans/BL-022-collections-supplemental-item-referrals.md`](plans/BL-022-collections-supplemental-item-referrals.md) |

---

## P3 — Later (priority 7+)

| ID | Module | Work item | Notes |
|----|--------|-----------|--------|
| **BL-015** | **Accounting** | **Grid prints** | All accounting module grids/tables should have grid prints. **→ Plan:** [`plans/BL-015-accounting-grid-prints.md`](plans/BL-015-accounting-grid-prints.md) |
| BL-017 | Court Violations | OCA Report | Finish PDF (see BL-001 for February verification). |
| BL-016 | General | Default values table | Customize defaults by agency. |

---

## Blocked / waiting / needs clarification

| ID | Item | Issue |
|----|------|--------|
| BL-012 | Omnibase | Marked blocked — confirm dependency or approval. |
| BL-006 | DPS Conviction Report | Waiting on specs. |

---

## Full import (reference)

Sorted by **Priority** (asc), then **Module**, **Name**.

| ID | Priority | Module | Name | Description | Client |
|----|----------|--------|------|-------------|--------|
| BL-001 | 1 | Court Violations | OCA Report | Verify data for February | |
| BL-002 | 1 | Jail | Finish Booking | Need to go through and finalize each part | |
| BL-003 | 1 | Jail | Finish Jail Command Center | Need to go through and finalize each part | |
| BL-018 | 1 | Court Violations | Warrant project — finish testing | Manual regression; warrant/court lifecycle in testing | |
| BL-019 | 1 | Court / Accounting | Shallowater Municipal Court — go-live | Setup, smoke tests, training — exclusive RMS use | Shallowater Municipal Court |
| BL-004 | 2 | Accounting | Bonds | Create bond batch/export | |
| BL-005 | 2 | Court Violations | Bonds | Finish implementing bond logic | |
| BL-006 | 3 | Court Violations | DPS Conviction Report | Implement and test - waiting on specs | |
| BL-007 | 3 | Court Violations | State Quarterly Accounting Report | Finish implementing | |
| BL-008 | 4 | General | Device Fingerprinting | Implement AuthDevices table and figure out new claims | |
| BL-009 | 5 | Accounting | Refund Batch | Create refund batch/export | |
| BL-010 | 5 | Data | Bad Images causing 500 error | Need to handle 500 error when processing image instead of throwing in UI | ShallowaterPD |
| BL-011 | 5 | Masters | Add relationships to reports | When printing master records in reports, please display relationships | |
| BL-012 | 6 | Court Violations | Omnibase | Need to implement; blocked | |
| BL-013 | 6 | Court Violations | UI for editing speeding ranges | Move speeding (fine ranges) to new table and create UI | |
| BL-014 | 6 | Person | Implement criminal trespass | Figure out best way to get criminal trespass information on person | |
| BL-015 | 8 | Accounting | Grid Prints | Make sure all of the grids/tables in the accounting module have grid prints. | |
| BL-016 | 9 | General | Default Values Table | Need to add a table and logic to be able to customize default values by agency | |
| BL-017 | 10 | Court Violations | OCA Report | Finish implementing PDF | |
| BL-020 | 5 | Security | Harden Descope cookie revocation on logout | CJIS IA-11 defense-in-depth: close the cross-tab cap-reset edge case when `sdk.logout()` fails server-side. | |
| BL-021 | 11 | UI | Classic layout — `TlsPage` shell | Introduce `TlsPage` (`banners` + default slots) inside Classic `v-main` for a stable seam toward Web Awesome `wa-page`. | |
| BL-022 | 6 | CAD | Large-agency remediation | Dispatch board, SignalR, notifier parity, UX/ops. **→ Plan:** [`plans/BL-022-cad-large-agency-remediation.md`](plans/BL-022-cad-large-agency-remediation.md) | |
| BL-023 | 6 | Court / Accounting | Collections — supplemental item-level referrals | Art. 103.0031 per-item clocks/referral; schema today is case-level snapshot only. Interim: recall/re-refer. | |

---

## Active plans

| ID | Backlog item | Plan file |
|----|--------------|-----------|
| BL-001 | OCA — verify February data | [`plans/BL-001-oca-february-verify.md`](plans/BL-001-oca-february-verify.md) |
| BL-002 | Jail — booking verification checklist | [`plans/BL-002-jail-booking-verify.md`](plans/BL-002-jail-booking-verify.md) |
| BL-003 | Jail — JCC (command center) verification checklist | [`plans/BL-003-jcc-verify.md`](plans/BL-003-jcc-verify.md) |
| BL-018 | Court — warrant project manual testing | [`plans/BL-018-warrant-project-testing.md`](plans/BL-018-warrant-project-testing.md) |
| BL-019 | Shallowater Municipal Court — go-live | [`plans/BL-019-shallowater-municipal-court-golive.md`](plans/BL-019-shallowater-municipal-court-golive.md) |
| BL-015 | Accounting — grid prints | [`plans/BL-015-accounting-grid-prints.md`](plans/BL-015-accounting-grid-prints.md) |
| BL-014 | Person — criminal trespass | [`plans/BL-014-criminal-trespass.md`](plans/BL-014-criminal-trespass.md) |
| BL-020 | Security — harden Descope cookie revocation on logout | [`plans/BL-020-cjis-logout-cookie-revocation.md`](plans/BL-020-cjis-logout-cookie-revocation.md) |
| BL-021 | UI — Classic `TlsPage` shell | [`plans/BL-021-tls-page-shell-classic-layout.md`](plans/BL-021-tls-page-shell-classic-layout.md) |
| BL-022 | CAD — large-agency remediation | [`plans/BL-022-cad-large-agency-remediation.md`](plans/BL-022-cad-large-agency-remediation.md) |
| BL-023 | Court / Accounting — collections supplemental item referrals | [`plans/BL-022-collections-supplemental-item-referrals.md`](plans/BL-022-collections-supplemental-item-referrals.md) |

---

## Changelog

| Date | Source | Notes |
|------|--------|--------|
| 2026-03-30 | `raw/BacklogWorkItems.csv` → `archive/2026-03-30-042748-BacklogWorkItems.csv` | First import; priority scale: lower number = more urgent. |
| 2026-03-30 | — | Added stable **BL-###** IDs; BL-015 plan stub + discovery notes. |
| 2026-03-30 | — | **BL-018** (warrant testing) + **BL-019** (Shallowater Municipal Court go-live); P0 plans added. |
| 2026-05-12 | — | **BL-014** criminal trespass plan added. |
| 2026-05-13 | — | **BL-020** added — CJIS IA-11 defense-in-depth follow-up to the session re-auth audit (harden Descope cookie revocation on logout). |
| 2026-05-17 | — | **BL-021** added — Classic layout `TlsPage` main-column shell; plan [`plans/BL-021-tls-page-shell-classic-layout.md`](plans/BL-021-tls-page-shell-classic-layout.md). |
| 2026-05-25 | — | **BL-022** added — CAD large-agency remediation aligned with product-repo `Docs/CAD-Architectural-Audit.md`; plan [`plans/BL-022-cad-large-agency-remediation.md`](plans/BL-022-cad-large-agency-remediation.md). Audit doc updated with May 2026 remediation status. |
| 2026-07-18 | — | Migrated canonical backlog + plans to Internal Docs (`internal/backlog/`). |
| 2026-07-15 | — | **BL-023** added — collections supplemental / per-item referrals (Art. 103.0031); interim recall/re-refer documented. (Master briefly used BL-022 for this item; renumbered on merge with CAD’s earlier BL-022.) |
