---
backlog: "BL-015 · Accounting · Grid prints"
status: ready
created: 2026-03-30
---

# Plan: BL-015 — Accounting grid prints

## Scope (locked)

**In scope:** Standard **client-facing search grids** under **`/module/accounting/**`** — inventory rows **2–12** below (Deposit Batch through Transactions).

**Out of scope (excluded by product choice):**

| # | Nav label | Reason |
|---|-----------|--------|
| **1** | Dashboard (`AccountingSimpleDashboard`) | Not a standard search grid. |
| **13** | Payment Cleanup (`PaymentCleanup`) | Admin/support tool; not a standard search pattern. |

**UI rule:** Implement grid print for every **in-scope** screen **whether `hide-print` is currently `true` or `false`**. If print is hidden, **enable** the standard search print affordance (`hide-print` off, `@click:print` + store `printSearchResultsAsync` or equivalent). If print is already shown, **verify** backend + PDF match search criteria and fix gaps.

---

## Decisions (confirmed)

| Topic | Decision |
|-------|----------|
| **Scope** | PDF **grid print** of **current search results** (filters + sort as executed by search), same pattern as other modules. **Not** row-level receipts or bespoke reports as part of BL-015. |
| **Nav** | **`/module/accounting/**` only** (Accounting nav drawer). Excludes Court Violation payment-plan work queues under `/module/court-violation/...` even though those components live under `accounting/` in source. |
| **UX** | Match **existing patterns** elsewhere in RMS (`search-container` / `tls-search` print affordance, `usePrintHelper.continuePrintWarningAsync` where other searches use it, same PDF download flow). |
| **Filters** | **No special rules** — print reflects whatever the search API returns for current criteria (same as other modules). |
| **Delivery** | **Single work set** — one coordinated implementation pass (not phased releases). |
| **`hide-print`** | **Do not skip** a screen because the print button is hidden today — **implement anyway** (UI + API as needed). |

---

## Reporting engine note (discovery)

Under `ThinLine.Reporting.Engine/ReportModels/Accounting/`, **grid models** currently include:

- `AccountingTransactionSetGridModel` (+ data row) — **used** by `GET …/transactionsets/print`.
- `PaymentPlanWorkQueueGridModel` — **used** by `GET …/paymentplans/work-queues/print` (work queues, not accounting nav search).

There are **no** fee / schedule / transaction line / payment plan **search** grid models in that folder yet. Several accounting search screens already call `printSearchResultsAsync` in the UI, but **backend `…/print` routes may be missing or incomplete** — part of implementation is **verify each in-scope screen**, add **controller + grid model + template** where needed, mirroring `AccountingTransactionsController.CreateTransactionSetSearchPdfAsync` and existing unit test patterns.

---

## Inventory — in scope only (Accounting nav)

| # | Nav label | Route name | Entry component | Notes |
|---|-----------|------------|-----------------|--------|
| 2 | Deposit Batch | `AccountingDepositBatchSearch` | `accountingDepositBatch/search/AccountingDepositBatchSearch.vue` | `hide-print` was true — enable + API |
| 3 | Revenue Allocation Batch | `AccountingRevenueAllocationBatchSearch` | `accountingRevenueAllocationBatch/search/AccountingRevenueAllocationBatchSearch.vue` | same |
| 4 | Payment Ledger | `AccountingSettlementLedgerSearch` | `accountingSettlementLedger/search/AccountingSettlementLedgerSearch.vue` | same |
| 5 | Payout Batch | `AccountingSettlementBatchSearch` | `accountingSettlementBatch/search/AccountingSettlementBatchSearch.vue` | same |
| 6 | Payment Reconciliation | `AccountingReconciliationSearch` | `accountingReconciliation/search/AccountingReconciliationSearch.vue` | same |
| 7 | Payout Reconciliation | `AccountingPayoutReconciliationSearch` | `accountingPayoutReconciliation/search/AccountingPayoutReconciliationSearch.vue` | same |
| 8 | Accounts | `AccountingAccountSearch` | `accountingAccount/AccountingAccountSearch.vue` | same |
| 9a | Fees & Schedules → **Fees** | `AccountingFeeScheduleSearch` (tab) | `accountingFee/search/AccountingFeeSearch.vue` | print may already show — verify API |
| 9b | Fees & Schedules → **Schedules** | same (tab) | `accountingSchedule/search/AccountingScheduleSearch.vue` | same |
| 10 | Transaction Sets | `AccountingTransactionSetSearch` | `accountingTransactionSet/search/AccountingTransactionSetSearch.vue` | regression + parity |
| 11 | Payment Plans | `AccountingPaymentPlanSearch` | `accountingPaymentPlan/search/AccountingPaymentPlanSearch.vue` | verify `paymentplans/print` vs UI |
| 12 | Transactions | `AccountingTransactionSearch` | `accountingTransaction/search/AccountingTransactionSearch.vue` | verify `transactions/print` vs UI |

---

## Implementation approach (single work set)

1. **Per in-scope screen** — Enable **`hide-print`** where it is `true` today; wire **`@click:print`** / **`printSearchResultsAsync`** (or custom print for non–`useSearchBase` screens) consistent with other modules.
2. **API parity** — For each screen, ensure **`GET …/print`** exists, uses the **same criteria** as search, returns PDF, and builds rows from the same data path as search. Add **`ReportGridModel` + Razor template** where missing.
3. **Tests** — Follow product-repo `ThinLine.API/ThinLine.API.UnitTests/Accounting/` (`AccountingTransactionsController_TransactionSetPrint_Tests` / `AccountingPaymentPlansController_Print_Tests`) style for new/changed endpoints.
4. **UI verification** — `npm run lint` + `npm run build` in `ThinLine.UI`; manual smoke: search → sort → print → PDF matches grid.

**Do not implement** until explicitly requested; this file is the plan only.

---

## Per-screen checklists (2–12 only)

### 2 — Deposit Batch

- [ ] `hide-print` removed; print wired to store/API.
- [ ] `GET` print endpoint + grid model + PDF template + tests.
- [ ] Manual: filter → sort → print matches.

### 3 — Revenue Allocation Batch

- [ ] Same pattern as §2.

### 4 — Payment Ledger

- [ ] Same pattern as §2.

### 5 — Payout Batch

- [ ] Same pattern as §2.

### 6 — Payment Reconciliation

- [ ] Same pattern as §2.

### 7 — Payout Reconciliation

- [ ] Same pattern as §2 (may need custom print handler if not on `useSearchBase`).

### 8 — Accounts

- [ ] Same pattern as §2 (list load may differ from paginated search — align PDF with on-screen table).

### 9a — Fees

- [ ] Backend print verified or implemented; UI print verified.
- [ ] Manual: filter → sort → print matches.

### 9b — Schedules

- [ ] Same as §9a.

### 10 — Transaction Sets

- [ ] Backend print present — regression + UI parity.
- [ ] Manual: filter → sort → print matches.

### 11 — Payment Plans (accounting search)

- [ ] Backend route aligned with UI (`paymentplans/print` or as implemented).
- [ ] Manual: filter → sort → print matches.

### 12 — Transactions

- [ ] Backend `transactions/print` aligned with UI; add if missing.
- [ ] Manual: filter → sort → print matches.

---

## Verification (global)

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test` on affected `ThinLine.API.UnitTests` accounting print tests + new tests
- [ ] `npm run lint` and `npm run build` in `ThinLine.UI`

---

## Changelog

| Date | Notes |
|------|--------|
| 2026-03-30 | Draft with discovery. |
| 2026-03-30 | User decisions; inventory + checklists. |
| 2026-03-30 | Scope locked: **2–12 in**, **1 Dashboard** and **13 Payment Cleanup** out. Clarified: implement print even when **`hide-print`** is true today. **No code until user requests implementation.** |
