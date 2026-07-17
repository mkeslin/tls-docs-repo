# Complete intake steps

Working through the Jail Intake booking wizard.

## How steps work

Booking details show a **step list** (sidebar) and a panel for the selected step. Values typically **autosave** as you work. Step status shows whether work is complete, in progress, deferred, skipped, or not applicable — depending on the step and your agency rules.

## Steps you will commonly see

Exact visibility can vary by product configuration. In current Thin Line builds, **Identity** and **Search** steps may be hidden from the sidebar while still affecting acceptance rules behind the scenes.

| Step | Role | Notes |
|------|------|-------|
| **Person** | Required | Demographics, aliases, marks/scars/tattoos, mugshot-related work as configured |
| **Custody** | Required | Hold type, times, arresting context — must be complete before Accept; no skip |
| **Charges** | Required | Add/edit charges; hold-only scenarios when no new charge applies |
| **Property** | Conditional | Bags and items; seal/open; “none collected” / retained paths |
| **Mental Health** | Conditional | Screening; defer usually requires a reason |
| **Medical** | Conditional | Screening, medications, withdrawal notes; defer with reason when allowed |
| **Classification** | Conditional | Factors and recommended custody level; preliminary / deferred options when allowed |

## Completing a step

1. Open the step from the sidebar.
2. Fill required fields until validation is clear.
3. Mark the step **complete** (or follow the status control your UI provides).
4. Move to the next incomplete required step.

## Defer, skip, reopen

| Action | Typical use |
|--------|-------------|
| **Defer** | Screening cannot finish yet; capture a **reason** when required |
| **Not applicable / skip** | Step does not apply for this booking (when the product allows it) |
| **Reopen** | Correct or finish a previously completed step (permissions may limit this) |

Deferred or incomplete **required** work blocks **Accept Into Custody**. Conditional steps may block accept depending on agency readiness rules — resolve banners on the booking before accepting.

## Tips

- Watch the **status banner** on the booking — it explains what still blocks acceptance.
- Print or preview step PDFs after key sections when your agency keeps paper packets (see [Reports and printouts](reports.md)).
- If another user is editing the same booking, you may see lock / takeover behavior for supervisors — coordinate before overwriting.

## Related

- [Start a booking](start-a-booking.md)
- [Accept Into Custody](accept-into-custody.md)
