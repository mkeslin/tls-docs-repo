# Court refund disbursement

![Court refund disbursement batches](images/accounting-court-refunds.png)

Pay refund dues owed back to violators after fee corrections or payment overpayments.

## When to use refunds

Use **Create Refund Due** on a court violation when:

- A fee correction leaves money owed back to the violator after you adjusted fees/balances, or
- A payment overpaid what the case still owed (including online payments).

Create Refund Due posts the accounting correction and queues a **pending refund due**. It does **not** change fee amounts — adjust fees first on the case when needed.

## Create Refund Due (case)

1. Open the court violation → **Accounting**.
2. Choose **Create Refund Due**.
3. Confirm amount and payee (defaults to the violator; change with the person picker when needed).
4. Save — the due appears as pending until paid in a disbursement batch.

Refund events also appear on the case **History** / timeline.

## Court Refund Disbursement Batches

Pay pending refund dues by check (default for all payment methods unless your agency enables card-back refunds).

### Create a batch

1. Open **Accounting** → **Court Refund Disbursement Batches**.
2. Choose **New Batch**.
3. Set search criteria and **Find Eligible**.
4. Select refund dues and **Create Batch**.

### Post the batch

1. Open batch detail — items group by **payee** when one batch pays multiple people.
2. In **DRAFT**, enter **Check #** for each payee group.
3. Set **Disbursement Date** and **Post Batch**.

### Exports

Posted batches support CSV, Tyler ERP, CentralSquare, **City GL**, and accountant PDF exports (same pattern as bond refund batches).

### Void

**Void** reverses GL and returns dues toward pending. **Void Reason** is required. Coordinate with court before voiding.

## Related

- [From Court payments](from-court-payments.md)
- [Bonds](bonds.md)
- [Deposit batches](deposit-batches.md)
