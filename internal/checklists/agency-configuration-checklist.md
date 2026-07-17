# Agency Configuration Checklist

**Document type:** Checklist  
**Status:** v1  
**Use during:** [Configuration](../sops/deliver/configuration/README.md) (lifecycle 4)  
**Primary UI:** Admin → **Agency & Module Settings** — see [Agency & Module Settings](../sops/deliver/configuration/agency-settings.md)

Engagement checklist for agency **business configuration**. Does **not** replace [Environment Health Checklist](environment-health-checklist.md) (platform wiring) or migration validation.

Mark **N/A** where the agency type or contract excludes a module.

---

## Identity

| Field | Value |
|-------|--------|
| AgencyName | |
| Environment | ★ test · ★ prod · other: |
| Configured by / date | |
| Reviewed by / date | |

---

## A. Agency & Module Settings — General

### Branding

- [ ] Agency image (logo) uploaded or confirmed not required
- [ ] Agency seal / signature configured if used on documents
- [ ] Code Enforcement letterhead configured if CE in scope
- [ ] Agency theme (palette) selected

### Agency Details

- [ ] Agency type set
- [ ] Agency name and abbreviation set
- [ ] State and county set
- [ ] Latitude / longitude set (if maps / location features used)
- [ ] Master / pinned location configured if required

### Law Enforcement *(LE agencies)*

- [ ] ORI set
- [ ] Default court facility set
- [ ] NIBRS / State IBRS versions and IBRS start date set (or N/A)

### Mobile Citation / court appearance *(if citations in scope)*

- [ ] Court appearance defaults (judge, hours, day offset, time) set
- [ ] Violator / child address statement text reviewed
- [ ] Online payment for court violations enabled or explicitly off

### Court Reporting / OmniBase / Court Settings *(court or as used)*

- [ ] OCA / DPS identifiers set or N/A
- [ ] OmniBase FTA integration configured or N/A
- [ ] VPTA / citation import warning settings set as required

### Court programs & payments *(court)*

- [ ] Program default due-date days set for programs in use
- [ ] Credit rates set if used
- [ ] In-person / Stripe / processing fee configured or N/A
- [ ] Third-party collections vendor / auto-refer days set or N/A

### CAD

- [ ] CAD webhooks configured or N/A (full support)

---

## B. Modules

For each **in-scope** module: enabled, number pattern, next/manual numbering, delete/mobile flags as applicable.

- [ ] Incident
- [ ] Fire Incident
- [ ] Citation (paper / random / mobile patterns)
- [ ] Warrant
- [ ] Criminal Trespass
- [ ] Close Patrol
- [ ] Notepad
- [ ] Equipment
- [ ] Fleet
- [ ] Evidence
- [ ] Call (CAD)
- [ ] Code Enforcement
- [ ] Court Violation
- [ ] Collections
- [ ] Jail Intake
- [ ] Out-of-scope modules left disabled

Number patterns aligned with migration Overrides when historical data was imported.

---

## C. Notifications & Workflow

- [ ] Dashboard notification toggles set for modules in use
- [ ] Validate on Submit / Validate on Approve (IBRS) set per agency preference

---

## D. Record Sharing

- [ ] Cross-agency sharing configured or N/A (full support)

---

## E. Reports & Documents

- [ ] **Reports** header: name, address, phone, fax, email
- [ ] **Documents** block: name, physical/mailing address, contact, website as needed
- [ ] Spot-check a sample report and document for correct header

---

## F. Related Admin (outside Agency settings)

- [ ] Officers / dispatchers created for go-live cohort
- [ ] Users and roles assigned; login verified for key roles
- [ ] Required codes configured (e.g. call types, agency-specific lists)
- [ ] CAD dispatch agencies linked if multi-agency CAD
- [ ] Evidence locations created if Evidence in scope
- [ ] Code Enforcement ordinances documented if CE in scope
- [ ] Deployment / tenant URL confirmed for this environment

## G. Compliance / other (confirm in product)

- [ ] CJIS Compliance Officer designated (as used by the agency)
- [ ] Complaints / compliments email for mobile citations set or N/A
- [ ] Hardware (mobile printers, scanners) quoted/ordered or N/A — detail in [Hardware Readiness Checklist](hardware-readiness-checklist.md)

---

## Sign-off

| Role | Name | Date | Notes |
|------|------|------|-------|
| Implementation | | | |
| Customer sponsor (optional) | | | |

**Exit:** Sections A–E complete or N/A for in-scope agency type; Sections F–G complete enough for training and Integrations and Hardware.

---

## Related documents

| Document | Role |
|----------|------|
| [Agency & Module Settings](../sops/deliver/configuration/agency-settings.md) | Field inventory |
| [Configuration](../sops/deliver/configuration/README.md) | Phase overview |
| [Bootstrap vs Configuration](../sops/deliver/infrastructure/bootstrap-vs-configuration.md) | Boundary |
| [Environment Health Checklist](environment-health-checklist.md) | Platform only |
