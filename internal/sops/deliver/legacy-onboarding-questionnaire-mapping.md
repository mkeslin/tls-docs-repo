# Legacy onboarding questionnaire mapping

**Document type:** Mapping report  
**Status:** v1  
**Source reviewed:** `Clients/BloomburgPD/TLS_OnBoarding.docx` (*Customer Onboarding Questionnaire*)  
**Original file:** Do **not** delete. Retain as historical engagement artifact.  
**Purpose:** Map every question, field, table, and requested artifact into the Deliver methodology and customer-facing workbooks—without a naive Word→Markdown conversion.

Related destinations:

| Destination | Path |
|-------------|------|
| Customer implementation workbook | [`customer/implementation/customer-implementation-workbook.md`](../../../customer/implementation/customer-implementation-workbook.md) |
| Working session workbook (Thin Line) | [`internal/templates/working-session-workbook.md`](../../templates/working-session-workbook.md) |
| Configuration discovery workbook | [`customer/implementation/configuration-discovery-workbook.md`](../../../customer/implementation/configuration-discovery-workbook.md) |
| Agency configuration checklist (internal) | [`checklists/agency-configuration-checklist.md`](../../checklists/agency-configuration-checklist.md) |
| Hardware readiness checklist | [`checklists/hardware-readiness-checklist.md`](../../checklists/hardware-readiness-checklist.md) |
| Implementation workspace | [`implementation-workspace-standard.md`](implementation-workspace-standard.md) |

---

## Classification legend

| New destination / type | Meaning |
|------------------------|---------|
| Kickoff and discovery | Early alignment / identity / scope |
| Infrastructure | Environment, URL, bootstrap inputs |
| Data migration | History, redaction, legacy codes |
| Configuration | Product settings and policy decisions |
| Integrations and hardware | Devices and external systems |
| Users and access | Rosters, roles, approvers (not project contacts) |
| Training | Audiences and readiness |
| Go-live planning | Cutover planning |
| Project-management task | Action item / follow-up, not a config field |
| Customer-provided artifact | File or export to attach/link |
| No longer needed | Drop or replace with defaults/discussion |
| Needs clarification | Ambiguous in the legacy form |

**Disposition:** Keep in named template · Move to discussion · Replace with defaults · Task only · Drop · Clarify with product/process owner

---

## Findings summary

### Missing in the legacy questionnaire (add in new method)

| Gap | Where it belongs now |
|-----|----------------------|
| Explicit project lead / acceptance authority | Kickoff · Contacts · Roles |
| Workflow discovery (how work actually runs) | Working session workbook |
| Timeline / phase board | Workspace · Preliminary timeline |
| Training plan | Training planning section |
| Go-live / hypercare plan | Go-live planning |
| Integration inventory beyond hardware | Integrations section |
| Migration assessment gate (scope/pricing) | Data migration discovery + assessment |
| Configuration **approval** sign-off | Configuration workbook §16 |
| Waiting-on-customer vs Thin Line | Workspace statuses |

### Duplicate information in the legacy form

| Duplication | Recommendation |
|-------------|----------------|
| Agency name + address appear under Primary Agency **and** Report Header | Collect identity once; derive report header defaults; override only if different |
| Court address repeated for Municipal and JP (same judge/address in Bloomburg example) | One court facility table + “also used as JP?” flag |
| Citation number format under Module formats **and** Mobile Citations | Single numbering section; mobile subsection for court-driven constraints |
| Officer list vs “users who need logins” | Contacts ≠ users; roster artifact for personnel + separate access cohort |

### Overly large or burdensome

| Item | Problem | New approach |
|------|---------|--------------|
| **Call Types** include/exclude matrix (80+ values) | Customers treat it as a quiz; many X/☑ without discussion | Defaults + import-if-migrating + **exception list** only; discuss in CAD session |
| Full officer/dispatcher tables in the same PDF as ORI and printers | Mixes config, HR roster, and procurement | Roster **artifact** + Users/access decisions; hardware in hardware checklist |
| Asking for every module number format whether unused | Noise | Only modules in purchase; N/A otherwise |

### Questions customers are unlikely to understand

| Item | Issue | Better approach |
|------|-------|-----------------|
| Fine-grained number format tokens (`YY-XXXX`) without examples | Format language is internal | Thin Line proposes pattern + sample; customer confirms “looks like our tickets” |
| Agency sharing read/write without examples of product behavior | Easy to over-promise | Discussion with concrete scenarios |
| NIBRS validate on submit vs approve | Policy + product nuance | Recommend both; explain officer vs approver workload in session |
| “CAD Agencies” if they do not buy full CAD | Confusing | Conditional on CAD purchase |

### Defaults should replace a checklist

| Area | Default stance |
|------|----------------|
| Call types | Thin Line defaults; import legacy if converting; customize exceptions |
| NIBRS validation | Validate on submit **and** approve (legacy “best practice”) unless agency opts out |
| Report header | Copy from primary agency identity unless overridden |
| Module number formats | Propose standard; align to legacy if migrating |
| Theme / unused modules | Do not ask |

### Discussion vs asynchronous

| Prefer **discussion** (working session) | OK **async** (send ahead / artifact) |
|----------------------------------------|--------------------------------------|
| Workflows, sharing, NIBRS validation tradeoffs, court appearance rules | Logo files, letterhead, ordinance PDFs/links, personnel roster spreadsheet, property location list, hardware counts |
| Call-type exceptions | Preferred URL preference (short text) |
| What “manual tickets for now” means for go-live | Address / phone / email facts |

### Belongs on a project task list (not configuration workbook)

| Item | Why |
|------|-----|
| “Please send email with logos” | Artifact delivery task |
| Hardware quote / purchase | Procurement task → Hardware readiness |
| “Eventually want MDT + printer for e-tickets” | Roadmap / future phase request—not current config |
| Grant funding dependency for mobile citations | Risk / constraint on timeline |
| Get migration assessment scheduled | Project task |

---

## Mapping table

| Existing section | Existing item | New destination | Information type | Recommended disposition | Reason | Required / Optional / Conditional | Customer owner | Thin Line owner | When collected |
|------------------|---------------|-----------------|------------------|-------------------------|--------|-----------------------------------|----------------|-----------------|----------------|
| Instructions | Complete questionnaire for initial configuration | Customer implementation workbook (how to use) | Project-management | Keep as principle; drop “one big form” framing | Async mega-form is burdensome | Required (process) | Project lead | Implementation lead | Kickoff |
| Preferred URL | Preferred hostname (e.g. `agency.thinline.app`) | Infrastructure; Kickoff identity | Fact + decision | Keep; short async OK | Needed for bootstrap / DNS | Optional (Thin Line can assign) | Project lead / IT | Infrastructure operator | Kickoff → Infrastructure |
| Primary Agency | Agency display name | Configuration §1; Kickoff | Fact | Keep once; reuse for headers | Core identity | Required | Project lead | Configuration | Kickoff / Configuration |
| Primary Agency | Agency abbreviation | Configuration §1 | Fact | Keep | Used in UI/short labels | Required | Project lead | Configuration | Kickoff / Configuration |
| Primary Agency | Agency address (physical + PO Box) | Configuration §1–2 | Fact | Keep; split physical vs mailing if different | Report/document headers | Required | Project lead | Configuration | Configuration |
| Primary Agency | ORI | Configuration §5 | Fact | Keep | LE reporting / NIBRS | Conditional (LE) | Records / chief | Configuration | Configuration |
| Primary Agency | Logo (“email logos”) | Customer-provided artifact; Project task | Artifact | Task: deliver files; Config verifies upload | Not a config “decision” | Optional but recommended | Project lead | Configuration | Before Configuration sign-off |
| Report Header Info | Agency name | Configuration §2 | Fact / decision | Default from display name; override if different | Avoid re-typing | Required | Records / admin | Configuration | Configuration |
| Report Header Info | Address / City State ZIP / County | Configuration §2 | Fact | Keep | Printed reports | Required | Records / admin | Configuration | Configuration |
| Report Header Info | Phone / Fax / Email | Configuration §2 | Fact | Keep | Printed reports | Required | Records / admin | Configuration | Configuration |
| Module Number Formats | Intro / samples | Configuration §5; Working session | Decision | Discussion with samples; not blank essay | Customers struggle with tokens | Conditional (per module) | Records lead | Configuration | Configuration (after modules known) |
| Module Number Formats | Incident format | Configuration §5 | Decision | Keep; prefer legacy if migrating | Affects migration/training | Conditional (RMS) | Records lead | Configuration | Configuration |
| Module Number Formats | Citations (paper) | Configuration §5 / §8 | Decision | Keep; note “manual entry” as operational choice | Distinct from mobile | Conditional | Records / patrol | Configuration | Configuration |
| Module Number Formats | Citations (mobile) | Configuration §5 / §8 | Decision | Keep; court may constrain | Integrations/court | Conditional (mobile citations) | Records / court contact | Configuration | Configuration |
| Module Number Formats | Citations (non-printed) | Configuration §5 | Decision | Keep if product uses; else N/A | Often unused | Conditional | Records | Configuration | Configuration |
| Module Number Formats | Warrants | Configuration §5 | Decision | Keep; “judge-assigned” is valid decision | May be external numbering | Conditional | Records | Configuration | Configuration |
| Module Number Formats | Close Patrols | Configuration §5 | Decision | Keep only if module purchased | Avoid unused modules | Conditional | Patrol lead | Configuration | Configuration |
| Module Number Formats | Calls for Service | Configuration §5 / §7 | Decision | Keep if CAD | CAD | Conditional (CAD) | Dispatch lead | Configuration | Configuration |
| Module Number Formats | Code Enforcement | Configuration §5 / §12 | Decision | Keep if CE purchased | CE | Conditional (CE) | CE lead | Configuration | Configuration |
| Module Number Formats | Lost and Found | Configuration §5 | Decision | Keep if module used | Often N/A | Conditional | Records | Configuration | Configuration |
| Module Number Formats | Field Contacts | Configuration §5 / §6 | Decision | Keep if licensed | RMS | Conditional | Records | Configuration | Configuration |
| Module Number Formats | Notes | Configuration §5 / §6 | Decision | Keep if notepad licensed | RMS | Conditional | Records | Configuration | Configuration |
| CAD Agencies | Agencies you can dispatch for | Configuration §3 / §7 | Decision | Keep; **conditional on full CAD** | Confusing if no CAD | Conditional (CAD) | Dispatch lead | Configuration | Configuration discussion |
| Agency Sharing | Read/write relationships narrative | Configuration §3; Working session | Decision | Discussion with examples; then record decision | Easy to mis-specify async | Conditional (multi-agency) | Executive / project lead | Implementation lead | Working session |
| Users / Officers | Name, email, badge, unit, supervisor, approver | Users and access; **roster artifact** | Fact + policy | Spreadsheet artifact + approver policy in Config §4 | Not a page of the config workbook | Required for go-live cohort | Project lead | Configuration | Before training |
| Users / Dispatchers | Name, email, supervisor | Users and access; roster artifact | Fact | Same as officers | Conditional (CAD/dispatch) | Dispatch lead | Configuration | Before training |
| Users / Jailers | Name, email, supervisor | Users and access; roster artifact | Fact | Same pattern | Conditional (Jail) | Jail lead | Configuration | Before training |
| Hardware | Narrative (Thin Line can quote) | Integrations and hardware; Hardware checklist | Project-management | Keep as optional procurement path | Not configuration | Optional | Project lead / IT | Integrations owner | Kickoff → Hardware phase |
| Hardware | # Mobile printers (+ RJ-4250WBL note) | Hardware readiness checklist | Fact / request | Counts + models in hardware checklist | Device plan | Conditional | IT / project lead | Integrations owner | Integrations and hardware |
| Hardware | # Barcode scanners | Hardware readiness checklist | Fact / request | Keep | Evidence / citations | Conditional | IT / property | Integrations owner | Integrations and hardware |
| Hardware | # Barcode/label printers | Hardware readiness checklist | Fact / request | Keep | Evidence | Conditional | Property | Integrations owner | Integrations and hardware |
| Hardware | Other hardware / MDT future wish | Project task / risk / future request | Project-management | Timeline/risk—not current config | Bloomburg “eventually e-tickets” | Optional | Project lead | Implementation lead | Kickoff / ongoing |
| CJIS | CJIS Compliance Officer name | Kickoff contacts; Config §14 | Fact | Keep in contacts + security section | Compliance contact | Required (typical LE) | Executive / CJIS contact | Implementation lead | Kickoff |
| NIBRS Validation | Validate on submission | Configuration §6 | Decision | Default **on**; confirm in session | Officer workload | Conditional (NIBRS agency) | Records / command | Configuration | Configuration discussion |
| NIBRS Validation | Validate on approval | Configuration §6 | Decision | Default **on**; confirm in session | Approver workload | Conditional | Records / command | Configuration | Configuration discussion |
| NIBRS Validation | “Best practice both” guidance | Configuration §6 recommended default | Decision aid | Keep as Thin Line recommendation | Educates without quiz | — | — | Configuration | During session |
| Mobile Citations | Citation number format (long prose) | Configuration §5 / §8 | Decision | Merge with numbering; propose default YY-##### | Duplicate of module formats | Conditional | Records / court | Configuration | Configuration |
| Mobile Citations | Special requirements / handwritten now | Configuration §8; Go-live planning; Risk | Decision + constraint | Record operational posture + future intent as deferred | Affects training/hardware | Conditional | Patrol / project lead | Implementation lead | Discovery + Configuration |
| Court Info | Municipal court judge/address/hours | Configuration §8 / §11 | Fact + decision | Court facility table; reuse across citation/court | Printed on citations | Conditional (citations/court) | Court clerk / PD liaison | Configuration | Configuration |
| Court Info | JP court judge/address/hours | Configuration §8 / §11 | Fact + decision | Same; flag if identical to municipal | Avoid duplicate entry | Conditional | Court / PD | Configuration | Configuration |
| Complaints and Complements | Email for mobile citations | Configuration §13 | Fact | Keep | Mobile citation feature | Conditional (mobile citations) | Project lead | Configuration | Configuration |
| Codes / Call Types | Large include/exclude matrix | Configuration §15 (approach only); CAD session | Decision | **Replace matrix** with defaults/import/exceptions | Burdensome; low understanding | Conditional (CAD) | Dispatch lead | Configuration | CAD working session |
| Codes / Call Types | Extra custom values (Incident - …) | Exception list attachment | Decision / artifact | Attach short add/remove list | Exceptions only | Conditional | Dispatch / records | Configuration | CAD session |
| Property Room Locations | Room / sublocation list | Configuration §9 | Fact | Keep as short list or import | Evidence setup | Conditional (Evidence) | Property custodian | Configuration | Configuration |
| Code Enforcement | Email certified letter samples | Customer-provided artifact; task | Artifact | Task to send samples | CE documents | Conditional (CE) | CE lead | Configuration | Configuration |
| Code Enforcement | Common citations / ordinance link | Configuration §12; artifact | Fact / artifact | Link or attach; not full codebook in form | CE | Conditional (CE) | CE lead | Configuration | Configuration |
| Code Enforcement | Ordinance number/description table | Exception / common list attachment | Artifact | Small “most common” list only | Avoid full ordinance dump | Conditional (CE) | CE lead | Configuration | Configuration |
| Data Redaction | Note data that must not appear / special handling | Data migration discovery | Decision / constraint | Keep; required when migrating | Legal/operational | Conditional (migration) | Project lead / counsel as needed | Migration owner | Migration discovery |
| (Implicit) | Site “configured as best we can initially” | Configuration approval §16; change control | Project-management | Explicit approval + change control | Replaces vague promise | Required | Acceptance authority | Implementation lead | End of Configuration |

---

## Priority attention items (crosswalk)

| Legacy focus | New home |
|--------------|----------|
| Preferred URL | Kickoff / Infrastructure (workspace + bootstrap inputs) |
| Primary agency information | Kickoff facts → Configuration §1 |
| Report headers | Configuration §2 (default from identity) |
| Numbering formats | Configuration §5 (+ migration alignment) |
| CAD agencies | Configuration §7 (CAD only) |
| Agency sharing | Working session → Configuration §3 |
| Officers, dispatchers, jailers | Roster **artifact** + Configuration §4 / Users |
| Hardware | Hardware readiness checklist + Integrations phase |
| CJIS compliance officer | Contacts + Configuration §14 |
| NIBRS validation | Configuration §6 (defaults both on) |
| Mobile citations | Configuration §8 (+ hardware/future tasks) |
| Court information | Configuration §8 / §11 |
| Complaints and compliments email | Configuration §13 |
| Call types | §15 approach + exception list—**not** full matrix |
| Property-room locations | Configuration §9 |
| CE ordinances and letters | Artifacts + Configuration §12 |
| Data redaction | Data migration discovery |

---

## Template coverage checklist

| Legacy theme | Covered in customer templates | Status |
|--------------|-------------------------------|:------:|
| Preferred URL | Customer implementation workbook §3/§5; Working session project overview | Done |
| Identity + headers | Configuration workbook §1–2 | Done |
| Numbering | Configuration §5 (per-module rows; samples not tokens) | Done |
| Sharing / CAD agencies | Configuration §3, §7 | Done |
| Users roster | Configuration §4 + artifact note; Implementation workbook §10 | Done |
| Hardware | Implementation workbook §9; Working session hardware table | Done |
| CJIS officer | Implementation workbook §4; Configuration §14; Working session overview | Done |
| NIBRS | Configuration §6 (defaults both on) | Done |
| Mobile + court + complaints email | Configuration §8, §11, §13 | Done |
| Call types approach | Configuration §7, §15; Working session (no full matrix) | Done |
| Property locations | Configuration §9 | Done |
| CE letters/ordinances | Configuration §12 + artifacts | Done |
| Data redaction | Customer implementation workbook §7; Working session migration | Done |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Initial mapping from BloomburgPD `TLS_OnBoarding.docx` |
| 2026-07-17 | Customer workbooks updated; checklist marked Done; linked from Deliver TOC |
