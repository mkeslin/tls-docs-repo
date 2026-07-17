# Online payments and payouts

Track card/online payments (Stripe) from intent through bank payout.

## Payment Ledger

1. Open **Accounting** → **Payment Ledger**.
2. Search online payments (amount, fees, transaction set, payment intent, dates).
3. Use results when researching a specific online payment or fee.

Ledger rows are typically created automatically when online payments flow through the system.

## Payout Batch

1. Open **Accounting** → **Payout Batch**.
2. Search payout batches that represent Stripe payouts to the agency bank.
3. Use **Create Payout Batches** when your process requires creating from ledger activity.
4. Use **Sync Stripe Payouts** with a lookback window (for example 1–90 days) when a webhook was missed and payouts did not appear.

Filter for issues-only views when your screen offers that option during troubleshooting.

## Tips

- Sync is a recovery tool — if payouts normally appear overnight, investigate Connect/webhook health with Thin Line when sync is constantly required.
- Pair payout research with [Reconciliation and disputes](reconciliation-and-disputes.md).

## Related

- [Deposit batches](deposit-batches.md)
- [Court — Payments](../court/payments.md)
