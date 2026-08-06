---
backlog: "BL-027 · Court / Accounting · Collections eligibility (Art. 103.0031) rewrite"
status: done
created: 2026-08-06
related:
  - collections-eligibility-date-audit.md
  - BL-022-collections-supplemental-item-referrals.md
  - court-violation-third-party-collections.md
---

# Plan: Collections eligibility (Art. 103.0031) rewrite

## Goal

Replace CPF-warrant-based collections eligibility with statute-aligned triggers, make `ComplianceDueDateTime` the adjudicated paid-in-full clock, age amounts separately for TPC, and update violation health + CV|13 so clerks see correct candidates.

**Done when:** a case/item becomes collections-eligible on the 61st day after the correct source date; TPC is assessed only on eligible referred amounts; active referrals are healthy in `CONVICTED` / `CPF_FTC` / `CPF_WARRANT`; unit tests cover the audit matrix.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-027**
- **Audit:** [collections-eligibility-date-audit.md](collections-eligibility-date-audit.md) (§7 tree, §12 decisions)
- **Risk / lane:** Feature; billing/collections — high. Follow product-repo `AGENTS.md` (EF migrations via `dotnet ef` only; unit tests for API behavior).

## Locked product defaults

| Topic | Decision |
| ----- | -------- |
| Day count | Statute: eligible on **61st day after** source (strict `> 60`) |
| Warrant gate | Not required to refer |
| Unadjudicated source | `AppearanceDateTime` |
| Adjudicated source | `ComplianceDueDateTime` |
| Compliance due default | Judgment + **5 business days** |
| Plans / CS | Sync compliance due; cancel → judgment+5BD |
| Acceleration | On first missed installment → that installment due date |
| Amount-level aging | Yes |
| DISMISSED + TPC | Refer residual OK; **no TPC** while `DISMISSED` |
| Health allow-list | `CONVICTED`, `CPF_FTC`, `CPF_WARRANT` |
| Eligible-not-referred health | No (CV\|13 only) |
| Auto-refer days | ≥ 60 |

## Approach

1. **Phase 1** — `ComplianceDueDateTime` default (judgment+5BD), plan/CS sync, accelerate-on-miss, fix ModifyComplianceDueDate.
2. **Phase 2** — Eligibility evaluator; drop CPF warrant gate; referral snapshot columns; CV\|13; feature flag; clamp auto-refer days.
3. **Phase 3** — Pre-referral amount-level clocks; refer/TPC only eligible items.
4. **Phase 4** — Health allow-list + missing-date rules; UI/docs; health rebuild notes.

## Files / areas (expected)

- `ThinLine.API/.../CollectionsReferralEligibilityRules.cs`, `CourtViolationCollectionsService.cs`
- `ThinLine.API/.../StateUpdateService.cs`, `ComputeFunctions.cs`
- Payment-plan / disposition-plan writers (ComplianceDue sync)
- `CourtViolationDataStore.cs` (CV\|13)
- Health detector / candidate / UI issue codes
- Unit tests (collections, health, compliance-due)

## Verification

- [x] `dotnet build ThinLine.API/ThinLine.Server.slnx` (WebAPI / Data.Store build green; migrations scaffolded)
- [x] `dotnet test` filter collections + health + compliance-due / StateUpdateService / evaluator (426 passed)
- [x] UI lint for touched files (quiet pass)

## Cutover / ops

- After deploy: run **agency court violation health rebuild** so missing-date and referral-state issues refresh.
- Clerks: CV|13 membership will reshuffle (appearance / compliance due instead of CPF warrant enter date).
- Existing referrals keep historical basis; new referrals snapshot `CollectionsEligibilityBasis` / source / eligibility dates.
- Eligibility is always statutory Art. 103.0031 (appearance / compliance due); no agency legacy CPF mode.

## Open questions

- None for implementation defaults (locked above). Counsel may later revisit TPC-on-DISMISSED if residual fees should carry the fee.

## Notes

Execution tracked from Cursor plan `collections_eligibility_rewrite`. Audit remains the detailed gap analysis.

