# Accept into Custody

![Booking / accept path](images/jail-intake-add.png)

Move a completed booking from intake into live custody on the Command Center.

## Who can accept

**Accept into Custody** is available when:

- The current header agency is a **jail facility** agency (not a typical PD-only partner login)
- You have jail modify rights as your agency assigns them
- The booking is **Ready for Acceptance** (or equivalent)

Partner agencies that only create bookings generally **cannot** accept.

## What “ready” means

Required intake steps are complete. Conditional steps are completed, deferred, skipped, or marked not applicable as your rules allow.

| Where you check readiness | Note |
|---------------------------|------|
| Booking sidebar / banner | Full readiness messaging |
| Command Center checklist rail | May emphasize required steps — if Accept fails, return to booking details |

## Accept

1. Open the booking (**In Booking Process** → **Open booking**, or Booking Search).
2. Confirm person, charges, and custody details.
3. Choose **Accept into Custody**.
4. Confirm any final prompt.

On success you typically see that the booking was accepted (for example **Accepted on {datetime}** / toast **Booking accepted**):

- A **custody episode** appears on the Command Center
- The booking leaves active acceptance work in **In Booking Process**

## After accept

1. Assign housing if still **Unassigned** ([Housing and moves](housing-and-moves.md)).
2. Set **Critical Flags** / **Alerts** as needed ([Flags, alerts, and medication](flags-alerts-medication.md)).
3. Watch **Passes** and **Medications** queues on the board.

## If Accept fails

| Check | Action |
|-------|--------|
| Required step incomplete | Finish and **Mark Complete** |
| Conditional step still blocking | Complete, defer with reason, or skip per policy |
| Not a jail facility agency | Switch agency or hand off to facility staff |
| Concurrent edit | Coordinate and retry |

Do **not** create a second booking to bypass a blocked accept.

## Related

- [Complete intake steps](intake-steps.md)
- [Command Center basics](command-center.md)
- [Housing and moves](housing-and-moves.md)
