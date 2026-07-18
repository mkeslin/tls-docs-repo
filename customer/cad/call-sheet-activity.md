# Call sheet activity

Notes, people, vehicles, and organizations on the live call sheet.

![Call sheet — header, quick entry, activity](images/cad-call-sheet.png)

## Call sheet layout

The call sheet is **not** a classic tab strip. You get:

1. **Header fields** — Call Type, Priority, How Reported, Location ([Create and update a call](create-and-update-a-call.md))
2. **Quick entry** — add note / person / vehicle / organization
3. **Activity timeline** — running log of units, call info, notes, and linked entities

Use **Hide Inputs** / **Show Inputs** when you need more room for the timeline. Quick entry is hidden when the call is disposed.

## Add a note

1. Open the call sheet.
2. In **Add note...**, type the note.
3. Choose **Add Note** (or **Add Extended Note** for longer narrative entry).
4. Confirm the note appears on the timeline.

Draft text may be retained in the browser session while the call stays open — finish or clear drafts deliberately on shared consoles.

**Call notes** ≠ [Dispatcher notes](dispatcher-notes.md) (agency-wide floating notes).

## Add a person, vehicle, or organization

1. Use the matching quick field (**Add person…**, **Add vehicle…**, **Add organization…**).
2. **Search** masters first — [search before add](../getting-started/master-records/search-and-add.md).
3. **Associate** the selected master to the call.
4. On the entity card, set type / details as shown (for example person type).

| Entity | Typical quick fields |
|--------|----------------------|
| **Person** | Name, DOB; person type; optional LETS when enabled |
| **Vehicle** | Year, make, model, plate; optional LETS / impound tools when enabled |
| **Organization** | Name via organization master |

## Activity timeline filters

Filter the log to focus on Units, Call Info, Notes, Persons, Vehicles, and/or Organizations (All / None / Solo patterns as shown). Use filters during busy calls so critical updates stay visible.

## Related Incidents & Citations

The call sheet also hosts **Related Incidents & Citations** — see [Related incidents and citations](related-incidents-and-citations.md).

## Tips

- Prefer master links over free-text-only parties so the later incident inherits clean data.
- LETS and impound actions are claim- and agency-gated — follow CJIS policy; history also appears under [CAD Records — Impound and LETS](records/impound-and-lets.md).
- Closed-call maintenance options (for example adjusting note/unit times) appear under More Options when the call is closed — use only with supervisor guidance.

## Related

- [Dispose and close a call](dispose-and-close-a-call.md)
- [Master records](../getting-started/master-records/README.md)
