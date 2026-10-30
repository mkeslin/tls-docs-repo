# Direct LETS queries

Run **driver license** and **vehicle registration** inquiries when your agency is configured for **direct LETS** through Thin Line.

## Where to open TLETS

| Place | Who sees it | What it does |
|-------|-------------|--------------|
| **LETS Query** page | Users with LETS query access | Full workspace: Query, Devices, and History |
| Right-edge **TLETS** button | Your agency has direct queries on, and you can run a query | Same Query, Devices, and History workspace in a slideout |
| CAD notes **TLETS** button | Direct queries are on for the environment and at least one agency, and you can view LETS queries | Bottom sheet of this agency’s queries from the **last 24 hours**, from every user |

The CAD sheet is a monitor. It does not replace the query form. Expand a row to read the switch response. Attempts that failed device verification are left off that list. Refresh reloads the last 24 hours.

## Open the LETS Query workspace

The screen title is **TLETS** on the slideout and **LETS Query** on the page. It has three tabs:

| Tab | Purpose |
|-----|---------|
| **Query** | Submit a new inquiry and read the stored response |
| **Devices** | See devices registered to you and their approval status |
| **History** | Search past queries for your agency |

You also need **LETS query** access and a working agency configuration. If direct LETS is not ready, the **Query** tab shows a warning listing what is still missing.

## User and device authorization (Query tab)

Before **Run Query**, two cards summarize whether you are allowed to run a direct query:

| Card | What it reflects |
|------|------------------|
| **User authorization** | Your TLETS query permissions, whether **CHRI** queries are allowed for you, and whether **direct LETS queries** are enabled for the agency |
| **Device authorization** | This browser’s registered device — approved, pending, suspended, revoked, or not registered |

Each card is **green** when that side is ready, **amber** when something is pending or needs attention, and **red** when the query will be blocked. Fix what the card describes before retrying.

Thin Line **full-support** staff inherit TLETS query permissions for troubleshooting; device rules still apply for them.

## Register and approve devices

1. On **LETS Query** → **Devices**, register this browser when prompted (choose device type; the system assigns the device label and ID).
2. An agency admin approves the device on **Admin** → **TLETS Devices** (administrators with device-approval rights only).
3. On **Approve**, the dialog lists the **permissions** that approval will grant — the same permission checkboxes shown on that device’s row (TLETS queries are always included on approval). Adjust the row’s checkboxes before approving if CHRI or other permissions should differ.
4. Each signed-in session must **verify the device once** before the first direct query in that session. If verification is required, follow the step-up prompt for this browser’s device.

Shared terminals may be enrolled without a single assigned user; policy still requires an approved device and valid user permissions.

## Run a query (Query tab)

| Field | Notes |
|-------|--------|
| **Query Type** | **DQ - DRIVER LICENSE** or **RQ - VEHICLE REGISTRATION** |
| **Query Reason** | Agency query-reason code list (clearable when optional) |
| **Requesting Officer** | **Optional** — use when the inquiry is on behalf of an officer; dispatchers may leave it blank |
| **Note** | Optional free text |

The signed-in user is always recorded as the operator running the query.

Field labels show **\*** for required values and **(optional)** for optional values. **Run Query** applies the same required-field rules as the server.

### Driver license (DQ)

Provide **one** of:

- **License Number**, or
- **Last Name**, **First Name**, and **Date of Birth** together

**Sex** is optional. A caption under the driver-license fields describes the search options.

### Vehicle registration (RQ)

Provide **one** of:

- **Plate** and **Plate State**, or
- **VIN**

**Plate Year** and **Plate Type** are optional. **Plate Type** uses NCIC license plate types. A caption under the registration fields describes the search options.

### After Run Query

- **Stored response** shows validation messages, mode, status, and formatted result JSON when present.
- When the gateway returns a failure reason, it appears in the stored response (alongside status) so you can see why the inquiry did not complete.
- A denied query shows an error alert with the message returned by the system.

## History tab

The history grid lists date, type, reason, officer, note, and TLETS outcome columns. **Parameters** and **Result** are not shown inline — expand a row to see:

- Parameters as label/value pairs
- A short result summary (mode, status, hit, extracted fields)
- Raw response and full result JSON in a scrollable block

## Agency enablement

**Enable Direct LETS Queries** on the agency (Law Enforcement Details) turns on direct LETS for that agency. Only Thin Line support can change that switch; agency admins see it as read-only. The environment also has its own direct-query switch. The agency also needs a valid **9-character ORI** and remaining gateway configuration before the readiness check passes.

## DPS user id

**Admin → TLETS → Operators** stores the **DPS user id** for each person at this agency. A direct query sends that id. Leave the field empty to remove it. A query cannot run until the signed-in user has an id stored for this agency.

## TLETS mailbox

**Admin → TLETS Mailbox** lists messages the switch delivered to this agency’s terminal. View a message, then **Dismiss** or **Restore**. Dismissed messages stay in the record. Turn on **Show Dismissed** to see them. A search result stays on the query; it is not moved into the mailbox. Thin Line Support marks which agency **Operates the TLETS Terminal** and which **Terminal Device** receives that mail.

## Tips

- Follow CJIS and agency policy for every query and result.
- Use [CAD Records — Impound and LETS](records/impound-and-lets.md) to research older logged activity alongside this workspace.
- Device approval and permission changes are audited; work only on approved equipment.

## Related

- [Impound and LETS (CAD Records)](records/impound-and-lets.md)
- [Call sheet activity](../call-sheet-activity.md)
- [Support](../../support/README.md)
