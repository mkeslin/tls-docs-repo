# Disbursements

Pay the collections vendor their share and document the outbound check.

## Disbursement Report

Shows court-collected activity where a vendor share is still owed. It is **not** the same as vendor remittances entered on [Payment entry](payment-entry.md) (those are money the vendor already collected).

1. Open **Collections** → **Disbursement Report**.
2. Set period / filters.
3. Export **PDF** / **CSV** for finance review before cutting a check.

## Disbursement Batches

Requires Collections **modify**. Creates the outbound disbursement batch (check to vendor for TPC liability).

### Create

1. Open **Collections** → **Disbursement Batches**.
2. **New Batch** — set period, disbursement date, optional vendor.
3. **Find Eligible** → select lines → **Create**.

### Post

1. Open the batch detail.
2. Enter **Check #** and post.
3. Print disbursement **PDF** / **CSV** as needed.
4. Export GL to **Tyler ERP** / **CentralSquare Asyst** when your city uses those paths.

Posting narrative (conceptually): due-to-collections liability decreases; operating bank decreases.

### Void

Void with **Void Reason** when the check must be reversed — coordinate with finance.

## Tips

- Run Disbursement Report before creating a batch so the period is agreed.
- Keep check numbers unique and retained with the batch for audit.

## Related

- [Payment history](payment-history.md)
- [Accounting](../accounting/README.md)
