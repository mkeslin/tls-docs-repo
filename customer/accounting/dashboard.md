# Accounting dashboard

![Accounting dashboard](images/accounting-dashboard.png)

1. Open **Accounting** from the left rail (court agency + accounting access).
2. Choose **Dashboard**.
3. Use the summary for the selected date to see close-out posture (pending work, day status — as your build shows).
4. Drill into **Deposit Batch**, **Revenue Allocation**, or other menu items to act.

The dashboard is an overview — day-to-day posting happens on the batch screens.

## Card payments

From the dashboard you can open **card payments** for the selected day (and related deposit-batch transactions) to see how online card items allocated. Use this to reconcile Stripe / card activity against the day’s deposit without leaving the dashboard.

## Deposit tender breakdown

Deposit batch cards show a **tender matrix** (cash, checks, money orders, and other) with amounts and counts for payments, collections, and bonds. Use it to reconcile what landed in the day’s deposit before Create & Post.

## Deposit vs revenue mismatch

When fee totals on the deposit do not match revenue allocation, the dashboard shows a **mismatch** alert (expected, actual, and difference). **Bond escrow** in the deposit is excluded from that fee comparison — if fees match but the deposit still includes bond money, you may see an informational bond-escrow note while Create & Post remains available. Treat bond deposits separately from fee/revenue close-out.

## Related

- [Deposit batches](deposit-batches.md)
- [From Court payments](from-court-payments.md)
