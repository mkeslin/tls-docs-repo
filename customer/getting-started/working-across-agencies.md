# Working across agencies

How **agency context** differs from **product mode** (RMS / CAD / JAIL), when to switch agencies, and how to recover when lists look empty or actions are missing.

Use this page if your login can open more than one agency (PD + court, shared dispatch, jail facility, multi-city CAD, and similar). Single-agency users can skim the checklist and skip the rest.

## Agency vs product mode

| Concept | Where it lives | What it controls |
|---------|----------------|------------------|
| **Agency** | Header name / logo; **Agency** in the [user menu](header-and-user-menu.md) | Which agency’s records, codes, and queues you create and search in |
| **Product mode** | Header **RMS** / **CAD** / **JAIL** | Which shell and tools you see (records vs live dispatch vs Command Center) |

Switching to **CAD** does **not** change your agency. Switching agency does **not** open Jail for you if that agency is not a jail facility.

Always confirm **both** the mode and the agency name before you create a record.

## Agency types you will meet

Exact labels vary by implementation. Conceptually:

| Kind of agency | Typical work | Common gates |
|----------------|--------------|--------------|
| **Law enforcement (RMS)** | Incidents, citations, warrants, evidence, CAD Records | Module claims; LE numbering |
| **Court** | Court Violations, payments, FTA/CPF warrants | Court module; [Accounting](../accounting/README.md) only on court agencies |
| **Jail facility** | Command Center, intake, Accept into Custody | Must be on the **facility** agency — not only the arresting PD |
| **Shared / multi-agency CAD** | Live board with units from more than one agency | Units and Create Incident are agency-scoped — see [Multi-agency CAD](../cad/multi-agency-and-related-records.md) |

Your administrator and Thin Line implementation team decide which agencies your user can open. Multi-agency **record sharing** (seeing another agency’s masters or modules without switching) is Support-configured — see [Agency settings](../admin/agency-settings.md).

## Before you create or search

1. Read the **agency name** in the header.  
2. Confirm **RMS / CAD / JAIL** mode matches the task.  
3. Switch agency from the user menu if needed; wait for the header to update.  
4. Then open Search, Add, Accept, Accounting, or the live CAD board.

### Quick checklist by task

| Task | Agency you usually need |
|------|-------------------------|
| Add / search LE incident, citation, warrant, evidence | Arresting / records **PD** (or the LE agency that owns the record) |
| Court violation, plea, payment, deposit | **Court** agency |
| Accounting dashboard / deposits | **Court** agency with accounting |
| Accept into Custody / housing / meds | **Jail facility** agency |
| Create Incident from a CAD call | Agency that has a **unit on the call** |
| Dashboard Tasks | Filter by agency when you have more than one — see [Dashboard](dashboard.md#tasks-across-modules-and-agencies) |

## Wrong agency — common symptoms

| What you see | Likely cause | What to try |
|--------------|--------------|-------------|
| Empty Search / “no records” for a number you know | Wrong agency in header | Switch agency; search again |
| Empty CAD board or Jail Command Center | Wrong dispatch / facility agency | Switch; confirm with supervisor which agency owns the board |
| No **Accounting** / deposit tools | Not on a court agency (or missing claims) | Switch to court agency; ask admin for claims |
| No **Accept into Custody** | Not on jail facility agency, or booking not ready | Switch to facility; finish [intake](../jail/intake-steps.md) |
| **Create Incident** disabled on CAD | No unit from **your** target agency on the call | Assign that agency’s unit first — [Related incidents](../cad/related-incidents-and-citations.md) |
| “I see the number in a note but cannot open the record” | Record owned by another agency; no access or wrong header | Switch agency; if still blocked, ask admin whether sharing is enabled |

If you already **created** a record under the wrong agency, do **not** create a duplicate under the correct one without supervisor policy. Escalate — Support or your admin may need to correct ownership.

## Opening or linking another agency’s record

- **CAD → Link Existing** — choose agency + incident/citation number ([Related incidents and citations](../cad/related-incidents-and-citations.md)).  
- **Module Search** — only returns what your current agency context (and sharing rules) allow.  
- **Deep links / Tasks** — opening a task may land you in the owning module; still confirm the header agency matches the record.  
- **Masters** — treated as that agency’s indexes unless Support configured sharing ([Master records](master-records/README.md)). Prefer search-before-add in the agency you are working.

## Journeys that cross agencies or modules

| Journey | Why agency matters |
|---------|-------------------|
| [CAD call to incident](journeys/cad-call-to-incident.md) | Units and Create Incident are per agency on the call |
| [Arrest to jail booking](journeys/arrest-to-jail-booking.md) | PD incident vs jail **facility** agency for Accept |
| [Court warrant to LE service](journeys/court-warrant-to-le-service.md) | Court issues; LE serves in WAR — often two agencies |
| [Citation to court](../rms/citations/citation-to-court.md) | LE issues citation; clerks work court agency |
| [Court payment to accounting](journeys/court-payment-to-accounting.md) | Court / finance on court agency |

## What Support owns

Ask Thin Line Support (via your admin) for:

- Which agencies a user may access  
- Shared masters or cross-agency record visibility  
- Multi-agency CAD board design  
- Moving or correcting a record created under the wrong agency  

Day-to-day users should **switch agency and re-search** before assuming the system is broken.

## Related

- [Header and user menu](header-and-user-menu.md)
- [Dashboard](dashboard.md)
- [Multi-agency CAD and related records](../cad/multi-agency-and-related-records.md)
- [Troubleshooting — Wrong agency or empty lists](../support/troubleshooting.md#wrong-agency-or-empty-lists)
- [Journeys](journeys/README.md)
