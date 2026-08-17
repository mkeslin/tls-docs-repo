---
backlog: "BL-009 · Accounting · Refund Batch"
status: shipped
created: 2026-08-11
---

# Plan: BL-009 — Court refund due + disbursement batch

## Goal

Clerks can create a **refund due** after an overcharge/fee correction and pay outstanding refunds (including payment-time overpayments on `REFUNDS_PAYABLE`) via a **check disbursement batch** with GL, CSV, Tyler/CentralSquare exports, and accountant PDF.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — BL-009 Accounting · Refund Batch (priority 5).
- **Client trigger:** Citation paid $284, correct amount $144 → refund $140 (Incode journal entry today).
- **Risk / lane:** Feature; touches migrations + financial posting (review before merge). No Stripe changes in first pass.
- **Cursor plan:** `bl-009_court_refund_batch_fd33cdba.plan.md` (authoritative locked decisions).

## Locked decisions (first pass)

- Check refund only for **all** payment methods (including `ONL`); no Stripe partial.
- Liability from **Create Refund Due** corrections **and** payment-time overpayments.
- Exports: CSV, Tyler GL, CentralSquare GL, accountant PDF (mirror bond refund batches).

## Approach

1. Domain: `AccountingCourtRefundDue` + disbursement batch/junction; type code `BRF`; overpayment creates PENDING due.
2. Create Refund Due API + CV Accounting dialog (GL + fee subledger + due row).
3. Batch service/API/UI (DRAFT/POSTED/VOIDED) paying `Dr REFUNDS_PAYABLE` / `Cr OPERATING_BANK`.
4. Unit tests + feature index / release note.

## Files / areas (expected)

- `ThinLine.API/` — entities, DataStore, services, controllers, unit tests
- `ThinLine.UI/` — refundBatches UI, Create Refund Due dialog, routes/nav
- Product pattern: clone bond refund disbursement batch

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj --filter "FullyQualifiedName~CourtRefund"`
- [ ] `npm run lint` / `npm run build` in `ThinLine.UI`
- [ ] Manual: $284→$144 refund due → batch post; exports download

## Open questions

- None for first pass (check-for-all-methods locked). Stripe card-back is a later enhancement.

## Notes

Operational caveat: issuing a check for an `ONL` payment while Connect settlement stands may leave agency cash vs payer refund timing mismatched; accepted for v1.
