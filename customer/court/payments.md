# Payments

![Court case with balance](images/court-payments.png)

Collecting payments on court violations and accepting them into the court accounting flow.

Step-by-step: [Take and accept a payment](how-tos/take-and-accept-a-payment.md).

## Important concept: apply vs accept

| Step | Who | What it means |
|------|-----|----------------|
| **Apply payment** | Authorized user (see below) | External / off-platform payment is recorded on the case but not final |
| **Court acceptance** | Clerk / judge (per agency practice) | Payment becomes official — final receipt boundary |

A payment can be successfully recorded (including card processor success on other payment paths) and still wait in **Pending acceptance**. Final receipts are produced **after** acceptance.

## Apply an external / off-platform payment

Use **Apply Payment** on the court violation **Accounting** dialog when money was collected **outside** Thin Line (for example cash or check at the counter, or a third-party processor) and you need the case balance updated without posting to the general ledger or deposit/revenue batches.

1. Open the court violation (search by case number or defendant).
2. Open **Accounting** and choose **Apply Payment/Credit** (wording may vary slightly).
3. Confirm the informational notice: balance only — no GL / deposit batch posting.
4. Enter amount, method, and date.
5. Submit. The payment appears in **Payment - Accept New** until accepted.

When paying multiple related violations for the same defendant, select the cases your court allows to combine before applying.

**Access:** On current builds, **Apply Payment/Credit** on Accounting is available to Thin Line **full support** users. Day-to-day window and online collection continue to use your agency’s in-person / online citation payment flows when those are enabled.

## Off-plan amounts on a payment plan

If the violation has an active payment plan and additional balance that is **not** covered by remaining installments, Apply Payment and public citation payment flows can collect that **off-plan** portion without treating it as an installment payment. See [Payment plans](payment-plans.md#paying-amounts-outside-the-plan-off-plan).

## Accept pending payments

1. Open **Work queues** (or the payment-accept shortcut your court uses).
2. Open the queue for **new / pending payments** (payment acceptance).
3. Review each payment (amount, method, case).
4. Accept (or follow your agency’s reject / correct process if something is wrong).

Clear this queue daily so receipts and deposits stay current.

Until acceptance, do not treat the payment as fully posted for close-out or official receipt purposes.

## Receipts and balances

- Print or provide the **final receipt** after acceptance. Receipts summarize payment-plan installment vs direct / off-plan application when both apply.
- Case **statements** show chronological activity with a **running balance**.
- Case balances and closure logic update as accepted payments, jail credit, adjustments, and fees are applied.
- Paying in full does not always close the case automatically if other conditions (compliance, plans, state rules) remain open — check the case state and any health warnings.

## Jail credit and adjustments

When authorized, clerks may **Apply Jail Credit** (separate from Apply Payment) or other adjustments from convicted / compliance contexts. These can change balances and may contribute to closure. Use only with proper court authority; document the reason when the dialog requires it.

## Related accounting

Accepted payments flow into broader accounting processes (deposits, settlements, payouts) outside the individual case screen. Cashiers generally stop at apply + acceptance; finance staff use [Accounting](../accounting/README.md) for deposit batches and reconciliation. Referred balances may also appear in [Collections](../collections/README.md).

## Related

- [How-to: Take and accept a payment](how-tos/take-and-accept-a-payment.md)
- [Journey: Court payment to accounting](../getting-started/journeys/court-payment-to-accounting.md)
- [From Court payments](../accounting/from-court-payments.md)
- [Court finance workshop](../training/court-finance-workshop.md)
- [Payment plans](payment-plans.md)
- [Work queues](work-queues.md)
- [Case lifecycle](case-lifecycle.md)
- [Accounting](../accounting/README.md)
- [Collections](../collections/README.md)
