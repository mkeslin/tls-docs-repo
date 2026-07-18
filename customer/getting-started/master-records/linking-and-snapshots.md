# Linking and snapshots

![Masters linking](images/getting-started-modules-rail.png)

How modules attach to masters, and why you sometimes see “module record” data.

## Linking from a module

When an incident, citation, warrant, jail booking, or similar screen asks you to pick a person, vehicle, location, or property:

1. The UI opens master search in **lookup / select** mode.
2. You search and choose an existing master (or add one carefully).
3. The module stores a **snapshot** reference (a point-in-time link to that master).

That keeps the case readable even if someone later edits the live master — but it also means the case may show older values until updated.

## Live master vs module copy

| View | Meaning |
|------|---------|
| **Live master** (reference snapshot) | The shared Persons/Vehicles/… record in the right rail — editable with modify rights |
| **Module record copy** | Data stored on the incident/citation/etc. — may show a notice that you are viewing module-stored data |

If you see a message like *you are viewing data stored on the module record*, use **Master Record** (or equivalent) to jump to the live master. Edit the live master when the shared file should change; update the module link/fields when the case copy must change.

## Where masters are used (examples)

| Module | Typical masters |
|--------|-----------------|
| **Incidents** | Persons, organizations, locations, property (→ evidence) |
| **Citations** | Person, vehicle, location |
| **Warrants** | Person |
| **Evidence** | Property |
| **Jail intake** | Person, location |
| **Court** | Person context via citations / violations |

## Tips

- Fix identity errors on the **live master**, then confirm critical cases still show the right data.
- Do not create a second master “just for this case” to avoid snapshot confusion — that creates duplicates.
- Associations on the master (person↔vehicle) help future lookups but do not automatically rewrite every old case.

## Related

- [Search and add](search-and-add.md)
- [Duplicates and merge](duplicates-and-merge.md)
