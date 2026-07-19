# Gap analysis: Court, Accounting, Collections (P0)

**Document type:** Reference (behavior-contract step 3)  
**Status:** Snapshot — update as scenarios are locked  
**Convention:** [Behavior contract flywheel](../behavior-contract-flywheel.md)  
**Pilot complete:** [Court PRE-PLEA](court-preplea-pilot.md)

Inventory of **P0 journeys** vs automated locks and GitBook. Legend:

| Cell | Meaning |
|------|---------|
| **YES** | Exists and reasonably locks the journey |
| **PARTIAL** | Related coverage; not scenario-aligned or not the full path |
| **NO** | Missing |

Focus: happy path + critical fail paths. Out of scope here: BL-023 item-level collections design (except as a note), obscure edges, Support-only reverse/reallocate as day-to-day clerk work.

---

## Priority summary

| Priority | Gap | Why |
|----------|-----|-----|
| **P0** | `court-payment-accept` — API unit + integration | Documented clerk accept path; essentially untested |
| **P0** | Clerk `court-payment-apply` (not only PayIt) | Customer P0 is Apply dialog; tests lean public PayIt |
| **P0** | `collections-refer` / `collections-recall` HTTP | Unit-strong; no integration facts |
| **P1** | Scenario ids + thin Cancel e2e for activate, judgment, FTA | API already strong; flywheel alignment |
| **P1** | Bond HTTP integration | Unit-heavy; no Court bond HTTP IT |
| **P1** | Work-queue / calendar HTTP (thin) | Docs + screenshots exist; API surface thin |
| **P2** | Playwright journeys for apply→accept, remittance entry | After API locks; keep Cancel-only on canary |
| **P2** | Deposit/revenue/disbursement **post** HTTP | Unit exists; full Create & Post HTTP thin |
| — | `accounting-payment-refund-batch` (BL-009) | Backlog / not customer day-to-day — do not treat as shipped P0 |

**Already in good shape:** Court state-machine unit + integration (activate, plea, dismiss, judgment, FTA cycle); collections remittance HTTP; customer GitBook for most P0 topics; docs screenshots for many **surfaces** (not Save mutations); PRE-PLEA Cancel e2e pilot.

---

## Court

| Scenario id | Journey | API unit | API IT | Playwright | Screenshots | Customer docs | Internal scenario map | Notes |
|-------------|---------|----------|--------|------------|-------------|---------------|----------------------|-------|
| `court-preplea-*` | PRE-PLEA menu / Cancel dialogs / Enter NCO / dismiss / appearance | YES / PARTIAL | YES | YES (Cancel) | PARTIAL | YES | YES — [pilot](court-preplea-pilot.md) | Template for other verticals |
| `court-activate-new-to-preplea` | NEW → ProceedToPrePlea | PARTIAL | YES | NO | YES (detail) | YES — activate how-to | NO | Add scenario Trait; optional Cancel e2e |
| `court-activate-blocked-no-mapping` | Activate blocked without offense mapping | YES | YES | NO | NO | PARTIAL | NO | Strong API fail-path |
| `court-enter-judgment-guilty` | Post-plea → Enter judgment → CONVICTED | YES | YES | NO | YES | YES | NO (pilot said out of scope) | Next vertical after activate |
| `court-enter-judgment-blocked-ngl` | Judgment disabled when NGL | YES | YES | NO | NO | PARTIAL | NO | |
| `court-fta-mark-failure` | PRE_PLEA → FTA | PARTIAL | YES | NO | YES | YES | NO | |
| `court-fta-issue-warrant` | FTA → FTA_WARRANT | PARTIAL | YES | NO | PARTIAL | YES (+ RMS FTA warrant) | BL-018 plan ≠ scenario map | |
| `court-fta-clear-appearance` | Clear FTA → PRE_PLEA | PARTIAL | YES | NO | NO | YES | NO | |
| `court-bond-enter-basics` | Enter/modify/resolve bond | YES | **NO** | NO | YES (search/detail) | YES | NO | **HTTP IT hole** |
| `court-work-queues-triage` | Open/triage work queues | YES | **NO** | NO | YES | YES | NO | |
| `court-calendar-docket-day` | Calendar → case → date actions | PARTIAL | PARTIAL | NO | YES | YES | NO | Appearance via state machine IT only |
| `court-payment-apply-from-case` | Apply payment from case | PARTIAL | PARTIAL (PayIt lean) | NO | PARTIAL (dialog Escape) | YES | NO | See Accounting table |
| `court-payment-accept-queue` | Accept pending from queue | PARTIAL / **NO** accept | **NO** accept | NO | NO | YES | NO | See Accounting — **highest risk** |
| `court-dismiss-validation-fail` | Dismiss rejected without required fields | YES | PARTIAL | NO | NO | PARTIAL | NO | |

---

## Accounting

| Scenario id | Journey | API unit | API IT | Playwright | Screenshots | Customer docs | Internal scenario map | Notes |
|-------------|---------|----------|--------|------------|-------------|---------------|----------------------|-------|
| `court-payment-apply` | Clerk Apply payment → pending | PARTIAL | PARTIAL (PayIt ≠ clerk Apply) | NO | PARTIAL | YES | NO | Align tests to clerk path |
| `court-payment-accept` | Accept pending → final receipt | **NO** | **NO** | NO | NO | YES | NO | **Top gap** |
| `court-payment-plan-create` | Create installment plan | PARTIAL | PARTIAL (SQL-seeded plan, not create HTTP) | NO | YES | YES | NO | |
| `court-payment-plan-installment-pay` | Pay against plan | YES | YES | NO | NO | YES | NO | Stronger than create |
| `accounting-deposit-batch-create-post` | Create & Post deposit batches | YES | PARTIAL | NO | YES | YES | NO | |
| `accounting-deposit-batch-void` | Void deposit batch | YES | NO | NO | NO | YES | NO | |
| `accounting-revenue-allocation-create-post` | Create & Post revenue allocation | YES | PARTIAL | NO | YES | YES | NO | |
| `accounting-bond-refund-batch` | Bond refund disbursement batch | YES | NO | NO | YES (surface) | YES | BL-004 vs shipped docs — reconcile | |
| `accounting-bond-refund-batch-void` | Void bond refund batch | YES | NO | NO | NO | YES | NO | |
| `accounting-payment-refund-batch` | Agency payment refund batch | NO | NO | NO | NO | NO (Support-only) | BL-009 | Not clerk P0 |

---

## Collections

| Scenario id | Journey | API unit | API IT | Playwright | Screenshots | Customer docs | Internal scenario map | Notes |
|-------------|---------|----------|--------|------------|-------------|---------------|----------------------|-------|
| `collections-past-due-eligible` | Eligibility / ELIGIBLE queue | YES | NO | NO | NO | YES | plans (collections module / TPC) | Case-level today; BL-023 = future item-level |
| `collections-refer` | Refer → IN COLLECTIONS | YES | **NO** | NO | NO | YES | YES (plans) | Unit-strong; add HTTP |
| `collections-batch-refer` | Batch refer from queues | YES | NO | NO | NO | YES | YES | |
| `collections-recall` | Recall from collections | YES | NO | NO | NO | YES | BL-023 interim recall/re-refer | |
| `collections-remittance-entry` | Remittance entry → CLR post | YES | YES | NO | YES | YES | YES | Best financial lock in Collections |
| `collections-remittance-import` | CSV vendor remittance import | NO | NO | NO | NO | YES | Phase 4 in TPC plan | Docs ahead of tests |
| `collections-disbursement-batch` | Vendor disbursement create/post/void | YES | NO | NO | YES | YES | YES | |
| `collections-referred-portfolio` | Portfolio search/export | PARTIAL | PARTIAL | NO | YES | YES | YES | Read-mostly |

---

## Layer verdicts

| Layer | Court | Accounting | Collections |
|-------|-------|------------|-------------|
| Customer GitBook | Strong | Strong | Strong |
| API unit | Strong (state machine); uneven elsewhere | Uneven; accept missing | Strong refer/remit/disburse units |
| API integration | Strong state machine; weak bond/queues/calendar HTTP | PayIt/plan pay OK; accept/clerk apply/post batches thin | Remittance YES; refer/recall NO |
| Playwright e2e | PRE-PLEA Cancel only | None | None |
| Docs screenshots | Many surfaces | Many surfaces | Portfolio/remit/disburse surfaces |
| Internal scenario maps | PRE-PLEA pilot only | None | Plans exist; no scenario-id map |

---

## How to run existing P0 locks (Docker)

Product monorepo root — Docker Desktop on; stop RMS Web API / Aspire first:

| Scope | Command |
|-------|---------|
| Court state machine | `npm run api:test:itest:court` |
| Court ↔ accounting | `npm run api:test:itest:court-accounting` |
| Collections HTTP | `npm run api:test:itest:collections` |
| All three | `npm run api:test:itest:scoped` |

Policy: **unit = mocks/InMemory**; **integration = Docker SQL**. See product-repo `ThinLine.API/ThinLine.API.IntegrationTests/README.md` and [behavior-contract-flywheel.md](../behavior-contract-flywheel.md).

## Suggested order of work

1. **Lock `court-payment-accept`** (unit + HTTP) — then thin Cancel e2e on accept queue if stable.  
2. **Clerk `court-payment-apply`** integration (owned fixture) — distinguish from PayIt.  
3. **`collections-refer` / `collections-recall` HTTP** — mirror existing unit cases.  
4. **Flywheel maps** for activate + judgment (API already ready) using the PRE-PLEA pilot template.  
5. Bond / deposit-post / disbursement HTTP as capacity allows.  
6. Playwright only for journeys that docs promise and API already locks — keep canary non-destructive.

## Related product paths

| Area | Typical roots |
|------|----------------|
| Court state machine | `ThinLine.API/.../Court/CourtViolations/`, `IntegrationTests/Court/StateMachine/` |
| Court accounting / payments | `IntegrationTests/Court/CourtAccounting/`, `UnitTests/.../Accounting/` |
| Collections | `CourtViolationCollectionsService`, `IntegrationTests/Court/Collections/` |
| UI e2e | `ThinLine.UI/tests/e2e/` |
| Docs screenshots | `ThinLine.UI/tests/docs-screenshots/captures/court-*.spec.ts`, `remaining-modules.spec.ts` |
| Customer | `customer/court/`, `customer/accounting/`, `customer/collections/` |
