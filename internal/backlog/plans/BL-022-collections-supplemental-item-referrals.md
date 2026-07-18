---
backlog: "BL-023 · Court / Accounting · Collections — supplemental item-level referrals"
status: draft
created: 2026-07-15
---

# Plan: Collections supplemental item-level referrals

## Goal

Support Art. 103.0031-style **per-item** referral: when new fees/costs are assessed after a case is already referred, track each balance item’s past-due clock and referral status, and assess **incremental** TPC only on newly referred amounts — without tearing down the whole case referral.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-023** (P2).
- **Related plan:** [court-violation-third-party-collections.md](court-violation-third-party-collections.md).
- **Statute:** Tex. CCP Art. 103.0031(b)/(f) — 30% on each **item** that is both >60 days past due **and** referred.
- **Risk / lane:** Feature; touches accounting/collections (financial). Migrations required when implementing — follow ``AGENTS.md`` (product repo `AGENTS.md`) / EF scaffold rules.
- **Schema today:** Case-level only — `CourtViolationCollectionsReferrals` stores aggregated `ReferralAmount` / `TpcAmount` / `StatusCode` on `CourtViolationId`. No per-fee due dates or referral-line table. Ledger balances are fee-code aggregates without obligation due dates.

## Interim process (good enough until BL-023 ships)

When a new fee is added to an **already REFERRED** case and the court wants that amount (and possibly TPC) included in collections:

1. **Recall** the active referral (Collections card → Recall). Unpaid TPC is **not** auto-reversed.
2. If a **fresh TPC** on the new total is required: **reverse** the unpaid TPC assessment via existing accounting reversal tools.
3. **Refer again** — eligibility uses current non-TPC principal; TPC is assessed only if unpaid TPC is gone (and defendant is not indigent).

**Do not** expect referred balance or TPC to auto-update when fees are posted. Live case balance may grow; the collections snapshot stays frozen until recall/re-refer.

**Tradeoff vs ideal:** Recall/re-refer is a blunt case-level reset (vendor churn, history rows). It is workable for infrequent post-referral fees; BL-023 replaces it with supplemental referral lines.

## Approach (when implementing)

1. Design child table (e.g. `CourtViolationCollectionsReferralItems`) keyed to fee/assessment identity + due/eligibility date + status + amounts.
2. Keep case header for portfolio/vendor lifecycle; lines for incremental placements and TPC.
3. Eligibility: queue or auto-detect unreferred principal past 60 days; assess incremental TPC only.
4. UI: show referred vs unreferred principal; “refer additional amount” without full recall.
5. Vendor file/update expectations per agency contract (out of band until export exists).

## Files / areas (expected)

- `ThinLine.API/ThinLine.Data.Model/Court/Entities/CourtViolations/`
- `ThinLine.API/ThinLine.Data.Store/Migrations/ThinLine/` (via `dotnet ef migrations add`)
- `ThinLine.API/ThinLine.Business.Objects/Court/CourtViolations/CourtViolationCollectionsService.cs`
- `ThinLine.API/ThinLine.API/Court/CourtViolations/CollectionsReferralEligibilityRules.cs`
- `ThinLine.UI/src/components/modules/courtViolation/collections/`

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj` (collections + eligibility)
- [ ] UI: `npm run lint` / `npm run build` in `ThinLine.UI` when UI changes

## Open questions

- Item identity: fee-code line vs assessment `AccountingTransaction.Id` (same fee assessed twice)?
- Due date source when fees lack an explicit due date (use assessment date? judgment/CPF warrant? fee-specific rule)?
- Auto-supplement vs clerk queue (agency setting)?
- Should recall continue to avoid auto-reversing TPC, or revisit that carry-over with this work?

## Notes

- Auto-reversal of unpaid TPC on recall remains a separate Phase 1 carry-over in the collections plan; it is the main friction in the interim recall/re-refer path.
- Do not silently inflate `ReferralAmount` / assess TPC on fee add — that would skip the 60-day gate.
