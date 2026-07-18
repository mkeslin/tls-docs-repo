# Start a booking

Create a jail booking and open intake.

## Ways to start

| Path | When to use it |
|------|----------------|
| Header **JAIL** → **Add Booking** | Starting from the live Command Center |
| **Jail Intake** → **Booking Add** | Starting from intake navigation |

Both create a **booking** that appears under **In Booking Process** on the Command Center.

## Create Booking wizard

1. Choose **Add Booking** or **Booking Add**.
2. Walk the wizard steps:
   1. **Select Person** — **Scan Driver License** (when configured), or **PERSON LOOKUP (LAST FIRST)...** with **Search/Add** ([Master records](../getting-started/master-records/README.md)).
   2. **Enter Arrest Details**
   3. **Enter Facility Details**
   4. **Review Information**
3. Choose **Create Booking**.
4. Continue into booking details to complete [intake steps](intake-steps.md).

Agencies may also start from an incident / arrestee path when that integration is used. Full path from street arrest: [Arrest to jail booking](../getting-started/journeys/arrest-to-jail-booking.md). Confirm the header agency is the **jail facility** before Accept — [Working across agencies](../getting-started/working-across-agencies.md).

## After create

| Status (typical) | Meaning |
|------------------|---------|
| **Draft** | Just created / early |
| **In Progress** | Intake steps underway |
| **Ready for Acceptance** | Required work satisfied — ready for [Accept into Custody](accept-into-custody.md) |

The booking stays in **In Booking Process** until accepted or removed.

## Delete a draft booking

If a booking should not proceed **before** accept, use **Delete booking** (not labeled “void” in the product). Success feedback is typically that the booking was removed.

- Only delete when policy allows.
- Do **not** delete to “fix” an accepted custody episode — use [Release](release.md) or supervisor procedures.

## Related

- [Complete intake steps](intake-steps.md)
- [Accept into Custody](accept-into-custody.md)
- [Command Center basics](command-center.md)
