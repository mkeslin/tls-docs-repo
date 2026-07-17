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

## Admin Master Merge

Administrators may also use **Admin → Master Merge** (exact duplicates / scored duplicates, merge selected or merge all patterns). That screen is for systematic cleanup — not every officer’s daily tool.

| Path | Who |
|------|-----|
| Merge from right-rail search | Users with merge claims |
| Admin Master Merge | Administrators running duplicate campaigns |

## Tips

- Agree which record is primary before merging (best identifiers, most attachments, correct DOB).
- After merge, spot-check a few [Records](persons.md) links and open a recent incident/citation.
- If you lack merge rights, report duplicates to your administrator — do not keep using both files.

## Related

- [Search and add](search-and-add.md)
- [Property](property.md)
- [Support](../../support/README.md)
