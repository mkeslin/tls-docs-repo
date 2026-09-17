# Accounting dashboard

![Accounting dashboard](images/accounting-dashboard.png)

1. Open **Accounting** from the left rail (court agency + accounting access).
2. Choose **Dashboard**.
3. Use the summary for the selected date to see close-out posture (pending work, day status — as your build shows).
4. Drill into **Deposit Batch**, **Revenue Allocation**, or other menu items to act.

The dashboard is an overview. **Create & Post Batches** from here (or from Deposit / Revenue Allocation search) posts the deposit and its matching revenue allocation as one step. If the allocation cannot post, the deposit is rolled back too — you will not be left with a posted deposit and no allocation.

## Card payments

From the dashboard you can open **card payments** for the selected day (and related deposit-batch transactions) to see how online card items allocated. Use this to reconcile Stripe / card activity against the day’s deposit without leaving the dashboard.

## Batch detail reports

Deposit and settlement batch cards can download a **batch detail** PDF for the selected posted batch (line items including card-processor **CC Fee** where applicable). Use it as a companion print when reconciling the day’s batches. The same companion PDFs are available from the matching row on the **GL Export Queue**.

## Deposit tender breakdown

Deposit batch cards show a **tender matrix** (cash, checks, money orders, and other) with amounts and counts for payments, collections, and bonds. Use it to reconcile what landed in the day’s deposit before Create & Post.

## Deposit vs revenue mismatch

When fee totals on the deposit do not match revenue allocation, the dashboard shows a **mismatch** alert (expected, actual, and difference). **Bond escrow** in the deposit is excluded from that fee comparison — if fees match but the deposit still includes bond money, you may see an informational bond-escrow note while Create & Post remains available. Treat bond deposits separately from fee/revenue close-out.

## Related

- [Deposit batches](deposit-batches.md)
- [From Court payments](from-court-payments.md)
