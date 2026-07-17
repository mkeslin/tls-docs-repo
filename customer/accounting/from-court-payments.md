# From Court payments

How money on a court case becomes work in Accounting.

## Cashier path (Court)

1. Open the court violation ([Court](../court/README.md)).
2. **Apply Payment/Credit** (or your build’s Apply Payment action) — amount, method, date.
3. Payment sits **pending acceptance** until accepted.
4. Accept from the payment acceptance work queue (**Accept Payment** / **Batch Accept Payments** as your agency uses).
5. Issue the **final receipt** only after acceptance.

Details: [Court — Payments](../court/payments.md).

## What Accounting receives

Accepted payments become **transaction sets** that appear in pending batches for:

| Accounting tool | Role |
|-----------------|------|
| [Deposit batches](deposit-batches.md) | Group clearing / cash / check / processor amounts for bank deposit |
| [Revenue allocation](revenue-allocation.md) | Move court trust liability into revenue by fee allocation |
| [Online payments and payouts](online-payments-and-payouts.md) | Track Stripe online payments and bank payouts |

If a payment never appears in a pending deposit batch, check **acceptance**, **agency**, and **date** first — not the deposit screen alone.

## Payment plans

Create and manage plans on the **Court** case ([Payment plans](../court/payment-plans.md)). Accounting **Payment Plans** search is primarily **inquiry** across plans.

## Fees and balances on the case

Court **Manage Fees/Balances** (when used) changes what is owed on the violation. Fee schedule definitions live under Accounting [Fees & Schedules](accounts-fees-and-plans.md).

## Tips

- Train cashiers to stop at apply + accept; finance owns Create & Post Batches.
- One physical drawer day should map cleanly to deposit date and agency — avoid mixing agencies in one close-out.

## Related

- [Deposit batches](deposit-batches.md)
- [Journey: Court payment to accounting](../getting-started/journeys/court-payment-to-accounting.md)
