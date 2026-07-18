# Multi-agency CAD and related records

![Call sheet related records](images/cad-call-sheet.png)

How live CAD behaves when more than one agency’s units share a board, and how Create / Link incident work stays agency-scoped.

Single-agency dispatch can skim: the same Create Incident and Link rules apply with one agency.

## Shared board basics

- The live CAD console can show **calls and units from multiple agencies** when your implementation links them.  
- Your header **agency** still matters for what you create and which Create Incident button enables.  
- Product mode must be **CAD** ([Live CAD overview](live-cad-overview.md)).

Confirm agency context with [Working across agencies](../getting-started/working-across-agencies.md) before you assume the board is “empty” or a button is broken.

## Units by agency

| Rule | Why it matters |
|------|----------------|
| Units belong to an agency | Drag-assign and status updates follow that unit’s agency |
| Do not clear another agency’s unit | Unless policy and permissions explicitly allow it ([Assign and clear](assign-and-clear-units.md)) |
| Self-dispatch uses **your** assigned unit | Officer path stays on the officer’s agency unit ([Self-dispatch](self-dispatch.md)) |

## Create Incident (per agency on the call)

1. Open the call sheet → **Related Incidents & Citations**.  
2. Work the agency section for the agency that should own the RMS incident.  
3. **Create Incident** stays disabled until **at least one unit from that agency** is on the call.  
4. After create, open the incident number and finish the report in RMS.

Details: [Related incidents and citations](related-incidents-and-citations.md).

## Link Existing Record

When the incident or citation already exists:

1. **Link Existing Record**.  
2. Choose **Incident** or **Citation**.  
3. Select the **agency** and enter the record number.  
4. **Link** — confirm it appears on the call.

Use Link to avoid a second incident for the same call.

## Empty board or missing call

| Check | Action |
|-------|--------|
| Header agency | Switch to the dispatch agency that owns the board |
| Filters / call lists | Clear filters; confirm you are on Live CAD, not only CAD Records |
| Permissions | Full CAD access + agency `cadFull` (or equivalent) — ask admin |
| Historical call | Use left-rail **CAD Records**, not the live board |

## Tips

- Rehearse Create Incident in training with a call that already has **your** agency’s unit assigned.  
- Prefer one incident per reportable call — check Related before Create.  
- Citations are linked from CAD after they exist in Citations / mobile — Create Citation from CAD is not a live customer path in current builds.

## Related

- [Related incidents and citations](related-incidents-and-citations.md)
- [Journey: CAD call to incident](../getting-started/journeys/cad-call-to-incident.md)
- [Working across agencies](../getting-started/working-across-agencies.md)
- [CAD Records](records/README.md)
