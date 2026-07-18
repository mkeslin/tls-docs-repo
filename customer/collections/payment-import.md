# Payment import

![Collections remittance / import](images/collections-payment-entry.png)

Import a vendor remittance CSV (requires Collections **modify**).

## Expected columns

Provide a CSV with (headers as the import screen documents):

`ViolationNumber,CourtCash,VendorTpc,Note`

| Column | Meaning |
|--------|---------|
| ViolationNumber | Violation number or ID |
| CourtCash | Court cash portion |
| VendorTpc | Collections fee withheld |
| Note | Optional |

## Steps

1. Open **Collections** → **Payment Import**.
2. Enter **Vendor reference number** and **Payment received date**.
3. Optional batch note.
4. Paste or upload CSV content as the screen allows.
5. **Preview** — review matched / unmatched chips and line errors.
6. Fix source CSV for unmatched critical lines (unmatched lines may appear in preview but post needs at least one match).
7. **Post payments** when matches and header fields are valid.

## Tips

- Agree the file layout with your vendor and Thin Line during implementation — ad-hoc columns fail matching.
- Spot-check [Payment history](payment-history.md) after post.

## Related

- [Payment entry](payment-entry.md)
- [Referred accounts](referred-accounts.md)
