# Agency & Module Settings

**Phase:** Deliver · 4 · Configuration  
**Document type:** Reference  
**Status:** v1  
**UI:** Admin → **Agency & Module Settings** (`AdminAgency`)

Inventory of what Implementation configures in agency settings after [Infrastructure](../infrastructure/README.md). Complements officers, users, and codes (separate Admin screens)—see [Agency Configuration Checklist](../../../checklists/agency-configuration-checklist.md).

**Access:** Users with agency-admin claim (`canAccessAdminAgency`). Some cards require **full support** (Thin Line Support).

---

## Purpose

Define the agency’s identity, enabled modules, numbering, notifications/workflow validation, report/document headers, and court/CAD options so day-to-day product behavior matches the customer.

This is **configuration**, not bootstrap ([Bootstrap vs Configuration](../infrastructure/bootstrap-vs-configuration.md)).

---

## Tabs (product UI)

| Tab | Query `?tab=` | Who | What |
|-----|---------------|-----|------|
| **General** | `general` (default) | Agency admin; many LE/court cards = full support | Identity, images, ORI, court/mobile/CAD options |
| **Modules** | `modules` | Agency admin | Enable modules; record number patterns; next numbers |
| **Notifications & Workflow** | `notifications` | Agency admin | Dashboard notification toggles; IBRS validate on submit/approve |
| **Record Sharing** | `sharing` | Full support only | Cross-agency read/write sharing |
| **Reports** | `reports` | Agency admin | Report header block (name, address, phone, fax, email) |
| **Documents** | `documents` | Agency admin | Document/letterhead identity block |

---

## General tab — cards

Configure only what is in scope for the agency type (LE vs court) and licensed modules.

### Branding / images

| Card | Configure |
|------|-----------|
| Agency Image | Upload / clear agency logo image |
| Code Enforcement Letter Head Image | CE letterhead (if CE in scope) |
| Agency Seal | Seal image |
| Agency Signature | Signature image |

### Agency Details

| Field / area | Notes |
|--------------|--------|
| Type | Agency type code (`_AGT`); full support to change |
| Name | Display name |
| Abbreviation | Short name |
| Latitude / Longitude | Agency location |
| State / County Name | Geography |
| Agency Theme | Primary/accent palette (applies to all users in agency) |
| Pinned master location | Location module card on General |

### Law Enforcement Details *(LE agency types)*

| Field | Notes |
|-------|--------|
| ORI | Required for LE go-live |
| Default Court | Default court facility |
| NIBRS Version / State IBRS Version / IBRS Start Date | IBRS reporting setup |

### Mobile Citation *(when citations / mobile in scope)*

| Area | Notes |
|------|--------|
| Court appearance defaults | Judge name, hours description, appearance day offset, business days, appearance time |
| Statement text | Violator statement; child address obligation text |
| Online payment | Enable online payment for court violations; QR on mobile citations |
| Document court hours | Related document setting |

### Court Reporting *(court agencies)*

| Field | Notes |
|-------|--------|
| OCA Court Identifier | OCA reporting |
| DPS Conviction Location Code | DPS conviction export |
| DPS Conviction File Name Court Token | File naming token |

### OmniBase Integration *(when used)*

| Field | Notes |
|-------|--------|
| Enable OmniBase FTA Integration | On/off |
| OmniBase PSID / file format | Integration identity |
| SFTP username / password | Credentials (treat as secrets) |

### Court Settings

| Field | Notes |
|-------|--------|
| Enable VPTA Filing | Court filing option |
| Import All Citation Warnings / Import Citation Warnings | Citation import behavior |

### Program Default Due Date Days *(court programs)*

Default due-date offsets for programs such as chemical dependency treatment, tobacco awareness, DSC (incl. under 25), deferral, teen court, community service, default disposition, FTA show cause, etc. Set for programs the court uses.

### Credit Rates *(court, when applicable)*

Community service / credit rate settings used by court accounting.

### Court Violation Payments *(court)*

| Field | Notes |
|-------|--------|
| Enable in-person payment | Court payments |
| Stripe Connect Account ID | Online payments (requires online payment enabled in Mobile Citation) |
| Processing fee percent | Online fee |

Online payment / Stripe also belongs under [Integrations and Hardware](../integrations.md) when verifying live payment flows.

### Third-Party Collections *(court, when collections in scope)*

| Field | Notes |
|-------|--------|
| Collection vendor name / contact | Vendor identity |
| Auto-refer after (days past due) | Automation threshold |

Also enable **Collections** on the Modules tab when used.

### CAD Webhooks *(active CAD)*

Partner webhook endpoints for CAD (full support to change). Verify under Integrations when partners are live.

---

## Modules tab

For each module in scope:

| Control | Meaning |
|---------|---------|
| **Enabled** | Module available to the agency |
| **Record number pattern** | Number format (e.g. incident, citation, warrant, call) |
| **Manual number / next number** | Numbering behavior where offered |
| **Delete enabled** | Soft-delete / delete permission flags where offered |
| **Mobile enabled** | e.g. citation mobile, code enforcement mobile |

Typical modules surfaced here: Incident, Fire Incident, Citation (paper / random / mobile patterns), Warrant, Criminal Trespass, Close Patrol, Notepad, Equipment, Fleet, Evidence, Call (CAD), Code Enforcement, Court Violation, Collections, Jail Intake.

Enable only licensed / contracted modules. Align number patterns with migration Overrides when historical data was imported.

---

## Notifications & Workflow tab

| Section | Configure |
|---------|-----------|
| **Dashboard Notifications** | Toggles for draft/follow-up/review style alerts (citations, incidents, field contact, notepad, code enforcement, etc.) |
| **Workflow Validation** | **Validate on Submit** / **Validate on Approve** (IBRS validation gates) |

---

## Record Sharing tab

Cross-agency record sharing (read/write). Full support only. Configure when multi-agency / shared CAD or records are in scope.

---

## Reports tab — Report Header Info

Used on printed/exported reports:

- Agency name (line 1 / line 2)
- Address lines, city, state, ZIP
- Phone, fax, email

---

## Documents tab — Document Information

Used on formal documents / letter-style output:

- Agency name
- Physical and mailing addresses
- City, state, ZIP, county
- City designation
- Phone, fax, email, website

---

## Related Admin areas (not this screen)

Still part of **Configuration Complete**, configured elsewhere:

| Area | Admin entry |
|------|-------------|
| Officers / dispatchers | Admin → Officers |
| Users / roles | Admin → Users |
| Codes (e.g. call types) | Admin → Codes |
| CAD dispatch agencies | Admin → CAD |
| Evidence locations | Admin → Evidence |
| Tenant / deployment URL | Admin → Deployment (platform) |

---

## Exit criteria (agency settings slice)

- [ ] General: name, abbreviation, type; ORI if LE; theme/logo as agreed  
- [ ] Reports + Documents headers populated for go-live communications  
- [ ] Modules enabled and number patterns set for in-scope modules  
- [ ] Notifications / IBRS validation set per agency preference  
- [ ] Court / mobile / payments / collections / OmniBase / CAD webhooks configured or explicitly N/A  
- [ ] Record sharing configured or N/A  

Full milestone checklist: [Agency Configuration Checklist](../../../checklists/agency-configuration-checklist.md).

---

## Related documents

| Document | Role |
|----------|------|
| [Configuration](README.md) | Phase overview |
| [Agency Configuration Checklist](../../../checklists/agency-configuration-checklist.md) | Engagement checklist |
| [Bootstrap vs Configuration](../infrastructure/bootstrap-vs-configuration.md) | Boundary |
| Product UI | `ThinLine.UI` → `AdminAgency*.vue` · onboarding items in `useOnboardingChecklist.ts` |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — inventory from Admin Agency & Module Settings |
