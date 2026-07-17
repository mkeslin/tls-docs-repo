# FAQ

Common questions. Answers often depend on local permissions, codes, and agency type — ask your administrator when unsure.

## Access and login

### Can I add a user if I do not know their final email yet?

**Yes.** Enter a temporary email and change it later in [Users, roles, and claims](../admin/users-roles-claims.md).

### Why am I not seeing a module that others see?

- **Claims** and agency licenses control the left rail — see [Admin](../admin/README.md).
- Confirm the **agency** in the header ([Header and user menu](../getting-started/header-and-user-menu.md)).
- Some tools appear only for **court** agencies (Accounting) or **jail facility** agencies (Accept into Custody).

### Why don’t some dropdowns have the values I need?

Agency codes are maintained under [Admin — Codes](../admin/codes.md). Descriptions should be ALL UPPERCASE. Locked (system) lists cannot be edited locally — contact Thin Line.

## Dashboard and reports

### Can I retrieve a report that was run in the past?

**Yes.** From [Dashboard](../getting-started/dashboard.md) → **Report History** (commonly retained up to about three years). Elevated report claims may see other users’ history.

### Where is Self-Dispatch / Mobile Citations?

On the [Dashboard](../getting-started/dashboard.md) when CAD mobile / citation mobile is enabled for you. Otherwise use full [CAD](../cad/README.md) or [Citations](../rms/citations/README.md).

## Masters and records

### Someone created a duplicate person / plate. What now?

Prefer [search before add](../getting-started/master-records/search-and-add.md). Merge from Masters search when you have merge rights — [Duplicates and merge](../getting-started/master-records/duplicates-and-merge.md). Admin bulk Master Merge is Thin Line Support only.

### Why does an incident show old person data?

You may be viewing a **module snapshot**. Open the live master from the notice — [Linking and snapshots](../getting-started/master-records/linking-and-snapshots.md).

## Court and finance

### I took a card payment but there is no final receipt.

The payment may still be **pending acceptance**. Accept from the court work queue — [Payments](../court/payments.md). Then finance posts [deposit batches](../accounting/deposit-batches.md).

### Create & Post Batches shows nothing pending.

Nothing accepted is waiting for that agency/date — confirm acceptance and agency ([From Court payments](../accounting/from-court-payments.md)).

### Should I enter a collections remittance in Court and Collections?

**No.** Use one path. Vendor remittances belong in [Collections](../collections/README.md); window payments in Court Apply/Accept.

## CAD

### Create Incident is disabled on the call.

Assign a unit from that agency onto the call first — [Related incidents and citations](../cad/related-incidents-and-citations.md).

### Disposition does not appear.

Clear **all** units from the call first — [Dispose and close a call](../cad/dispose-and-close-a-call.md).

### Self-Dispatch says I am not assigned to a unit.

Ask an administrator to link your user/officer to a CAD unit — [Self-dispatch](../cad/self-dispatch.md).

## Jail

### Accept into Custody is missing.

You may not be in a **jail facility** agency, or the booking is not ready — [Accept into Custody](../jail/accept-into-custody.md).

### Cell check cannot include an inmate.

They may be **Unassigned**, or their location has **Include in cell checks** off — [Manage locations](../jail/manage-locations.md).

## Import/Export

### DPS / OCA says not configured.

Agency identifiers must be set during implementation — escalate to Admin / Thin Line ([DPS](../import-export/dps-conviction-report.md), [OCA](../import-export/oca-report.md)).

### IBRS will not download.

Fix incident errors, then **Rebuild & Validate** until clean — [IBRS](../import-export/ibrs.md).

## Related

- [Troubleshooting](troubleshooting.md)
- [Training by role](../training/roles/README.md)
- [Journeys](../getting-started/journeys/README.md)
