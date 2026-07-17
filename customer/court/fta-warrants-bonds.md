# FTA, warrants, and bonds

Failure to appear, warrant-related paths, and bond handling on court violations.

## Failure to appear (FTA)

When a defendant misses a required appearance:

1. Open the court violation.
2. Choose **Mark failure to appear** (or the equivalent enabled action).
3. Set or confirm **show-cause** information when prompted.
4. The case moves onto the **FTA** track (workflow often treats this as an inactive / enforcement bucket until resolved).

From FTA, common next steps include issuing an **FTA warrant**, scheduling or updating show cause, or returning the case when the defendant appears / bond is resolved — according to the actions enabled for that state.

## Warrants

Court Violations coordinates with the **Warrants** module for FTA and related enforcement. Issuing or updating warrant work from a court case should follow your agency’s warrant procedures and the actions available on the case.

LE-facing warrant search, service attempts, and court-owned behavior: [Warrants — Court-owned FTA and CPF](../rms/warrants/court-owned-fta-cpf.md).

Post-judgment non-compliance may follow a **CPF** (capias pro fine) track, including CPF warrant and CPF failed-to-comply states. Treat those as enforcement paths after conviction / compliance failure, not as a first-appearance FTA.

## Bonds

Bond actions are available on most active states (typically not on brand-new unactivated cases):

| Action | Purpose |
|--------|---------|
| **Enter bond** | Record a new bond on the case |
| **Modify bond** | Update an existing bond |
| **Resolve bond** | Close out the bond per court outcome |

Use **Bond search** when you need to find bonds across cases. Surety bond show-cause work often appears in a dedicated work queue.

Bond rules can **block** other transitions until the bond situation is consistent with the next court action. If a plea or disposition action is disabled, check for an outstanding bond requirement.

## Returning from FTA

Typical resolution patterns (availability depends on state):

- Defendant appears at show cause → record appearance and return to the appropriate pre-plea / post-plea state
- Bond hearing / bond posted → use bond actions and enabled FTA-resolution actions
- Warrant recalled / case resumed → follow the enabled transition and update dates

## Related

- [Case lifecycle](case-lifecycle.md)
- [Calendar and appearances](calendar-and-appearances.md)
- [Work queues](work-queues.md)
