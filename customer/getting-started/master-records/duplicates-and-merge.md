# Duplicates and merge

Cleaning up duplicate master records.

## Prevent first

Use [Search and add](search-and-add.md) — **Use Existing** whenever the person, plate, or serial already exists. Prevention is cheaper than merge.

## Merge from master search (day-to-day)

When you have **merge** rights:

1. Open the master type search (for example Persons).
2. Select **two or more** duplicate candidates (merge toggle / multi-select as shown).
3. Choose **Merge (N)** / **Merge Master Records**.
4. Pick the **primary** record and which field values to keep.
5. Confirm the merge.

Only merge records that are truly the same real-world entity. Wrong merges are hard to untangle.

## Property merge caveat

You generally **cannot merge** two property masters that are tied to the **same incident through evidence**. Resolve evidence/custody first or keep them separate per the product rule.

## Who can merge

| Path | Who |
|------|-----|
| Merge from right-rail Masters search | Users with the appropriate **Master … Merge** claims |
| Bulk / scored duplicate tools inside Thin Line Admin | Thin Line Support only — not an agency Admin menu item |

Agency administrators do **not** rely on **Admin → Master Merge** for day-to-day cleanup. That bulk tool is for Thin Line staff. Your path is Masters search → select duplicates → **Merge**.

## Tips

- Agree which record is primary before merging (best identifiers, most attachments, correct DOB).
- After merge, spot-check a few [Records](persons.md) links and open a recent incident/citation.
- If you lack merge rights, report duplicates to your administrator — do not keep using both files.
- Large conversion cleanup may be coordinated with Thin Line Support during implementation.

## Related

- [Search and add](search-and-add.md)
- [Property](property.md)
- [Admin](../../admin/README.md)
- [Support](../../support/README.md)
