---
backlog: "unassigned · Court · Manual regression wt-court → master (full surface)"
status: ready
created: 2026-07-29
updated: 2026-07-29
duration: 90 minutes
companion_canvas: "wt-court-release-testing.canvas.tsx"
environment: "Dev ThinLineRMS (Slaton Municipal Court samples) + remittance migrations"
---

# Manual regression — full wt-court merge (90 minutes)

## Goal

One timed pass covering **everything shipped on wt-court toward master**:

1. **Remittance / CD40** (newer) — State Quarterly create/post/JE/exports + RAR  
2. **Prior canvas use cases** — Source citations, Warrant Map, Collections vendor, Analytics, Health  

Interactive twin: open canvas **`wt-court-release-testing`** (checklist key `test-checklist-90m`).

## GO / NO-GO

| Result | Rule |
|--------|------|
| **GO** | Remittance **R4–R6** P0 green + Warrant Map / Collections / Citations smoke without crash |
| **NO-GO** | Wrong Col2/JE, Omni-L on form, void succeeds, export before post, Warrant Map hard error, vendor export **500** |
| **GO with notes** | P0 green; analytics empty charts or SFTP not configured |

### Locked remittance rules

- Collected = **banked** (deposit / settled card)  
- Family B Col2 = **0%**  
- **`IM_OMNI-L` off form**  
- RAR Apply = **new JE only**  
- **Void disabled** this release  

---

## 90-minute schedule

| Block | Min | Focus | If behind |
|-------|-----|--------|-----------|
| **R** Remittance | **30** | Bank SCF → SQR → post/JE/void/exports → RAR VerifyOnly | Never skip R4–R6 |
| **A** Citations | **10** | Source citation search + CV drill-through | A1+A4 only |
| **C** Warrant Map | **15** | Compare panel, cancel dialog, blocked reason | C1+C2; avoid live transfer |
| **B** Collections | **12** | Referred CV + Vendor File Export UI | B1+B3 |
| **D** Analytics | **8** | Charts + Programs modes | D1 only |
| **E** Health | **5** | Balance filter + plan smoke | E1 only |
| Buffer | **10** | Findings / retest / GO decision | Write decision |

---

## Block R — Remittance + RAR (30 min) · P0

**Nav:** Import/Export → State Quarterly Report · Accounting → Remittance allocation reconciliations  

| ID | Step | Expect | ✓ |
|----|------|--------|---|
| R1 | Bank **SCF $100** on a test CV — pay + **posted deposit** in an **unused** quarter | Collected/banked | |
| R2 | Create SQR for that quarter | Line 1 Col1≈100, Col2=**10** | |
| R3 | (Optional) Omni-L also banked | **No** `IM_OMNI-L` on detail/summary | |
| R4 | Rebuild while Created OK → **Post ON_TIME** | Posted; RetentionAmount = Σ Col2; JE balanced ≈ Col2 | |
| R5 | Void · rebuild-while-Posted · re-post | Void **fails**; rebuild blocked; **no** second JE | |
| R6 | Exports after post | GL CSV + Tyler + CentralSquare + accountant PDF **non-empty** | |
| R7 | RAR **VerifyOnly** | Run completes; list/detail OK (Apply only if you have drift) | |

**SQL (optional):**

```sql
SELECT LineNumber, Column1Amount, Column2Amount
FROM dbo.StateQuarterlySummaries WHERE StateQuarterlyHeaderId = @Id ORDER BY LineNumber;

SELECT AccountCode, DebitAmount, CreditAmount
FROM dbo.AccountingTransactionLines
WHERE TransactionSetId = @JeSetId AND IsDeleted = 0;
```

---

## Block A — Source citations (10 min)

**Nav:** Court → Citations (source citations) · samples below  

| ID | Step | Expect | ✓ |
|----|------|--------|---|
| A1 | Search **26-00798** (has CV); note **26-00796/797** PD-only | Hit with CV vs no CV | |
| A2 | Clear # · cited date last 30–90 days | Grid updates | |
| A3 | Open linked court violation from hit | Header / source-citation path works | |
| A4 | Search **ZZZ-NOPE-999** | Empty state, no crash | |

---

## Block C — Warrant Map (15 min)

**Nav:** `/module/warrant/warrant-map` · **do not** commit ownership transfer unless you will reverse  

| ID | Step | Expect | ✓ |
|----|------|--------|---|
| C1 | Search / open **26-00542-01**, **26-00589-01**, **100581-01** | Compare panel: warrant + CV | |
| C2 | Row with Transfer / Adopt / Link → open dialog → **cancel** | Dialog dismisses cleanly | |
| C3 | Unlinked **25-00697** or **100523-01** | Blocked reason visible | |
| C4 | High balance FTA/CPF **044032** or **CT 00528** | Case/warrant context loads | |

---

## Block B — Collections + vendor export (12 min)

| ID | Step | Expect | ✓ |
|----|------|--------|---|
| B1 | Open referred CV **052426** (-02/-03) or 052415 / 052373 | Collections card / status / amounts | |
| B2 | Collections → Referred Accounts · find 052426 | Drill-through | |
| B3 | Vendor File Export · preview/test/history | Loads; **no 500** if SFTP off | |
| B4 | Admin → Agency · collections SFTP fields | Present (toggle only if you’ll revert) | |

---

## Block D — Analytics (8 min)

**Nav:** `/analytics/court-violations`  

| ID | Step | Expect | ✓ |
|----|------|--------|---|
| D1 | Charts · Slaton · 2025–2026 | Summary + chart (or honest empty) | |
| D2 | Narrow date range | Summaries change; refresh/reset OK | |
| D3 | Programs · STARTED → IN_PROGRAM → COMPLETED · 25-01684 / 26-00423 / 25-01624 | Buckets change | |
| D4 | Optional `/analytics/accounting` | Smoke same range | |

---

## Block E — Health (5 min)

| ID | Step | Expect | ✓ |
|----|------|--------|---|
| E1 | Court Health · balance filter · 044032 / 046532 · print | Grid changes; print OK | |
| E2 | Plan CV **050551** or **049565V** | Payment plan still visible | |

---

## Example data (Slaton / ThinLineRMS)

| Area | Keys |
|------|------|
| Citations | 26-00798 (has CV); 26-00796/797 PD-only; ZZZ-NOPE-999 |
| Warrant Map linked | 26-00542-01, 26-00589-01, 100581-01 |
| Warrant unlinked | 25-00697, 100523-01 |
| FTA/CPF balance | 044032 (~$810), CT 00528 (~$959) |
| Collections | 052426, 052415, 052373 |
| Programs | 25-01684, 26-00423, 25-01624 |
| Plans | 050551 ALFAR, 049565V SANCHEZ |

---

## Findings

| ID | Sev | Block | Expected | Actual |
|----|-----|-------|----------|--------|
| 1 | | | | |
| 2 | | | | |

**Decision:** GO / GO with notes / NO-GO  
**Tester:** ____________  **Build:** ____________  

---

## Related

- Canvas: `canvases/wt-court-release-testing.canvas.tsx`  
- Warrant deep dive: [`BL-018-warrant-project-testing.md`](BL-018-warrant-project-testing.md)  
- Remittance IT plan: [`sqr-remittance-integration-tests.md`](sqr-remittance-integration-tests.md)  
- Fee mapping decisions canvas: `m4b-fee-decisions.canvas.tsx` (mapping locks — not timed QA)
