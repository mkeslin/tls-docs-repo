# Legacy System Migration

**Phase:** Deliver  
**Document type:** SOP  
**Status:** v1 — model SOP for Thin Line OS  
**Next review:** <mark style="color:red;">**TODO:**</mark> Set date (suggested: 2026-10-17)

---

## Executive Summary

| | |
|--|--|
| **Objective** | Migrate a customer's legacy data into Thin Line Platform safely and repeatably. |
| **Typical duration** | 1–10 business days (depending on vendor and data size). <mark style="color:red;">**TODO:**</mark> Refine from completed migrations. |
| **Owner** | Implementation Lead *(current incumbent: Matthew Keslin)* |
| **Primary stakeholders** | Customer Administrator · Implementation · Engineering |
| **Success criteria** | Data migrated · Utilities completed · Customer validated · Migration accepted |
| **Related SOPs** | [Customer Onboarding](../customer-onboarding.md) · [Bootstrap Environment](../infrastructure/bootstrap-environment.md) · [Post-Conversion Utilities](post-conversion-utilities.md) |
| **Required assessment** | [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) → Approved Conversion Plan |

Migration includes more than importing records: assessment, extraction, transformation, validation, workflow transition, customer review, and final acceptance.

---

## Responsibility swimlane

Who owns which work across the engagement:

```mermaid
flowchart LR
  subgraph Customer
    C1[Sign agreements]
    C2[Provide access / export]
    C3[Validate data]
    C4[Approve migration]
  end

  subgraph ThinLine["Thin Line"]
    T1[Assessment]
    T2[Extraction]
    T3[Mapping]
    T4[Import]
    T5[Utilities]
    T6[Corrections]
    T7[Close]
  end

  C1 --> T1
  T1 --> C2
  C2 --> T2
  T2 --> T3
  T3 --> T4
  T4 --> T5
  T5 --> C3
  C3 --> T6
  T6 --> C4
  C4 --> T7
```

| Lane | Responsibilities |
|------|------------------|
| **Customer** | Sign agreements; provide access or vendor export; validate data; approve migration |
| **Thin Line** | Assessment; extraction; mapping; import; utilities; corrections; close |

---

## 1. Purpose

Successfully migrate customer data from a legacy Records Management System (RMS), CAD, Court, Jail, or related application into **Thin Line Platform** while maintaining data integrity, minimizing implementation risk, and providing a repeatable, scalable migration process.

---

## 2. Scope

### In scope

All customer migrations involving historical data from a legacy vendor or custom system into Thin Line Platform.

Examples (not exhaustive): CopSync / Kologik, CrimeStar (FoxPro), Tyler / INCODE (court), Xpediter, and future vendors as encountered. See [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md).

### Out of scope

- Routine imports performed by customers themselves after go-live
- <mark style="color:red;">**TODO:**</mark> Clarify whether limited customer-driven imports need a separate SOP

---

## 3. Owner

| Role | Assignment |
|------|------------|
| **Accountable owner** | Implementation Lead |
| **Current incumbent** | Matthew Keslin |

### Current responsibilities (incumbent)

- Customer coordination
- Technical planning
- Data extraction
- Data mapping
- Conversion execution
- Validation support

Future ownership should allow standard migrations without founder involvement. See [Process maturity](#process-maturity).

---

## 4. Trigger

The process begins after **all** of the following are true:

1. Signed SaaS Agreement
2. Signed CJIS Security Addendum
3. Customer requests historical data migration

**No legacy data should be accessed until both agreements are complete.**

---

## 5. Preconditions

| Precondition | Notes |
|--------------|-------|
| SaaS Agreement executed | Required before any legacy access |
| CJIS Security Addendum executed | Required before any legacy access |
| Migration requested by customer | Trigger event |
| Target Thin Line environment available | <mark style="color:red;">**TODO:**</mark> Confirm whether UAT and/or Production must exist before import |
| Access path identified | On-prem remote access **or** vendor export path |

---

## 6. Inputs

- Signed SaaS Agreement
- Signed CJIS Security Addendum
- Legacy database (or vendor export)
- Customer credentials / access method (as applicable)
- Existing vendor package under product-repo **Migration Tools** (if available) — see [Migration Package Standards](vendor-packages/migration-package-standards.md)

---

## 7. Outputs

- Converted customer database (chosen target environment)
- Conversion scripts and customer conversion folder artifacts
- Conversion documentation for the engagement
- Customer notification that migration is complete
- Validation / acceptance result (informal today; formal in target state)

---

## 8. Tools

| Tool | Use |
|------|-----|
| SQL Server | Extraction, transformation, load, validation queries |
| Azure | Tenant / environment context |
| Cursor | Lead conversion execution per Migration Tools `PROCESS.md`; schema compare; mapping; SQL |
| Product Git — `Utilities/Migration Tools/` | Vendor packages (common Pipeline, StagingImporter, AgencyChecklist, VERSION) |
| Product Git / Team Drive — `Clients/<Client>/Conversion/` | Engagement working copy (checklist answers + agency Overrides) |
| GitBook | This SOP, assessment, vendor guides, package standards |

**Authoritative conversion tooling path (product monorepo):** `Utilities/Migration Tools/` — see [Migration Package Standards](vendor-packages/migration-package-standards.md).

---

## Current state

How Thin Line performs legacy migrations **today**:

| Area | Today |
|------|-------|
| **Assessment** | [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) exists; adoption still maturing toward consistent Approved Conversion Plans |
| **Pricing** | [Migration Pricing Policy](../../../policies/migration-pricing.md) draft; historically often bundled with multi-year SaaS |
| **Acquisition** | On-prem: remote server extract (often before go-live). Cloud: customer requests vendor export (may backfill after go-live) |
| **Preparation** | **Vendor packages** in product Git (`Utilities/Migration Tools/<Vendor>/`) with common Pipeline + agency checklist; engagement copies under `Clients/<Client>/Conversion/` (and Team Drive). Agents follow `PROCESS.md` (copy template → checklist → Overrides → promote reusable fixes) |
| **Execution** | Either UAT-then-Production **or** direct Production with tagged converted records — choice is judgment-based |
| **Utilities** | Admin → Data Utilities: module workflow transitions + CAD call master snapshot ([Post-Conversion Utilities](post-conversion-utilities.md)) |
| **Validation** | Implementation Lead emails customer; customer validates; corrections via follow-up. Acceptance is informal (typically email) |
| **Close** | Informal when corrections and acknowledgement are done; vendor `ConvertedAgencies.md` should record agency, date, and package VERSION |
| **Visibility** | Limited customer visibility into migration progress |
| **Dependence** | Founder / Implementation Lead still involved for many paths; Cursor agents expected to **lead** standard package-driven runs |

---

## Target state

Where this process should operate when Thin Line OS is mature:

| Area | Target |
|------|--------|
| **Assessment** | Formal [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) → **Approved Conversion Plan** before pricing/execution |
| **Pricing** | [Migration Pricing Policy](../../../policies/migration-pricing.md) (Draft — professional service tiers; assessment required before quote) |
| **Acquisition** | Documented cloud vs on-prem path with clear go-live timing rules |
| **Preparation** | Vendor packages in `Utilities/Migration Tools/<Vendor>/` (common only) + client engagement folders for checklist answers and Overrides; promote reusable fixes and bump package `VERSION` |
| **Execution** | Explicit decision matrix for UAT vs Production |
| **Utilities** | Complete [Post-Conversion Utilities](post-conversion-utilities.md) SOP; checklist-driven |
| **Validation** | Customer receives summary, counts, exceptions, and checklist; signs [Customer Acceptance Form](../../../templates/customer-acceptance-form.md) |
| **Close** | Formal [Migration Close-Out Checklist](../../../checklists/migration-close-out-checklist.md) |
| **Visibility** | Customer/internal progress tracking (portal or status dashboard) |
| **Dependence** | Implementation specialists complete **standard** vendor migrations using documented tooling without founder involvement |

---

## Gap analysis

| Gap | Current → Target | Priority |
|-----|------------------|----------|
| No formal assessment | Informal → [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) + Approved Conversion Plan | High |
| Pricing not standardized | Bundled practice → Approved policy | High |
| Folder model | Customer-only copies → Vendor packages + client Overrides (**in progress** via Migration Tools) | High |
| Validation / acceptance | Email informal → Checklist + signed acceptance | High |
| Close-out | Informal → Close-out checklist | Medium |
| Decision clarity | Tribal knowledge → Decision diagrams + UAT/Prod matrix | High |
| Progress visibility | Opaque → Status tracking | Medium |
| Utility catalog | Partial examples → Full SOP | High |
| Delegation | Founder-dependent → Role-based ownership for standard paths | High |

---

## Common risks

| Risk | Why it matters | Mitigation (current / needed) |
|------|----------------|--------------------------------|
| Corrupt or incomplete export | Blocks or corrupts load | Validate export integrity before mapping; <mark style="color:red;">**TODO:**</mark> standard checks |
| Missing tables / modules | Incomplete history | Scope modules in assessment; exception report |
| Customer delays (access, export, validation) | Extends cycle time; blocks go-live or backfill | Set expectations at trigger; track wait states |
| Vendor export limitations | Cloud path constrained | Document vendor-specific limits in [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md) |
| Unexpected schema changes | Breaks reused converters | Schema compare every engagement; version notes |
| Access before agreements | CJIS / contractual exposure | **Hard stop** until SaaS + CJIS addendum signed |
| Direct-to-Production defects | Live data risk | Prefer UAT when risk is high; <mark style="color:red;">**TODO:**</mark> decision matrix |
| Mapping defects discovered late | Rework after customer validation | Earlier sample validation; <mark style="color:red;">**TODO:**</mark> checklist |

---

## Decision trees

### Decision 1 — Acquisition path and converter reuse

```mermaid
flowchart TD
  A[Legacy system identified] --> B{Cloud hosted?}
  B -->|Yes| C[Customer requests vendor export]
  B -->|No| D[Remote server access and direct extract]
  C --> E{Existing converter for vendor/product?}
  D --> E
  E -->|Yes| F[Reuse vendor template / prior converter]
  E -->|No| G[Build new converter]
  F --> H[Prepare conversion for this customer]
  G --> H
  H --> I{Typical timing}
  B -->|Yes| J[May go live first then backfill]
  B -->|No| K[Convert before go-live - typical]
```

### Decision 2 — UAT versus Production import

```mermaid
flowchart TD
  A[Ready to execute import] --> B{High risk?}
  B -->|Large volume / new vendor / weak sample quality| C[Option A: Import to UAT]
  B -->|Known converter / low risk / schedule pressure| D[Option B: Import to Production with tags]
  C --> E[Customer validates in UAT]
  E --> F[Migrate accepted data to Production]
  D --> G[Customer validates in Production]
  F --> H[Run post-conversion utilities]
  G --> H
```

> <mark style="color:red;">**TODO:**</mark> Replace the “high risk” heuristic with an approved decision matrix (risk, schedule, customer preference, data volume, go-live timing).

---

## Time expectations

Starting estimates for planning and future KPIs. <mark style="color:red;">**TODO:**</mark> Replace with measured averages from real engagements.

| Phase | Typical duration |
|-------|------------------|
| Assessment | 30–60 minutes |
| Pricing / commercial alignment | <mark style="color:red;">**TODO:**</mark> |
| Data acquisition (Thin Line extract) | 1–3 hours (excludes customer/vendor wait time) |
| Customer/vendor export wait (cloud) | Customer dependent |
| Mapping / script preparation | Variable (hours to days for new converters) |
| Import | 15–60 minutes |
| Post-conversion utilities | Minutes–hours (volume / year filters); see [Post-Conversion Utilities](post-conversion-utilities.md) |
| Customer validation | Customer dependent |
| Corrections + close | Variable |

**Overall engagement:** typically **1–10 business days** excluding extended customer or vendor wait states.

---

## Automation score

Score each major process step **1–5** (1 = fully manual / founder-driven, 5 = scalable automation). Aligns with Customer Value Engine maturity language.

| Process | Automation level | Notes |
|---------|-----------------:|-------|
| Assessment | 3 / 5 | Assessment form exists; consistent use still maturing |
| Pricing | 2 / 5 | Draft policy; not fully operationalized |
| Extraction | 3 / 5 | StagingImporters + extracts; still engagement-specific |
| Mapping / prep | 3 / 5 | Vendor packages + Cursor `PROCESS.md`; agency Overrides required |
| Import | 4 / 5 | Scripted load; environment choice still manual |
| Utilities | 3 / 5 | Known utilities; catalog incomplete |
| Validation | 1 / 5 | Email + ad hoc customer review |
| Close | 2 / 5 | Still informal; `ConvertedAgencies.md` register started |

**Investment signal:** Validation, assessment, and close are the lowest-scoring steps — highest leverage for standardization before heavy automation.

---

## 9. Procedure

### Phase 1 — Identify legacy platform

Determine vendor, product version, cloud vs on-prem, modules in scope, and whether an existing converter exists.

Examples: CopSync / Kologik, CrimeStar, Tyler / INCODE (IncodeCourt), Xpediter.

Living catalog: [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md). Package layout: [Migration Package Standards](vendor-packages/migration-package-standards.md).

### Phase 2 — Legacy System Migration Assessment

Perform the [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md). **Today assessment is informal;** the target is a completed assessment form with an **Approved Conversion Plan**.

That assessment is the bridge between Sales, Implementation, and Engineering. It answers: can we convert, what to charge, how long, what risks, whether Sales can quote, what engineering is required, and whether to build or extend a reusable converter.

Do not treat pricing, schedule, or engineering commitments as final until the assessment recommendation is approved.

### Phase 3 — Pricing

Apply the [Migration Pricing Policy](../../../policies/migration-pricing.md) (Draft): migration is a one-time professional service; complete the [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) before quoting; select Tier 1–4 (or discount/waiver with documented justification).

> <mark style="color:red;">**Decision needed:**</mark> Approve the draft policy before using tier amounts as binding customer quotes. Discounts (including multi-year SaaS) must be recorded on the assessment.

### Phase 4 — Data acquisition

Follow [Decision 1](#decision-1--acquisition-path-and-converter-reuse).

- **On-prem (e.g. Tyler):** remote access; extract directly; usually before go-live.
- **Cloud (e.g. CopSync):** customer requests vendor export; may go live first and backfill.

### Phase 5 — Prepare conversion

Follow product-repo **`Utilities/Migration Tools/PROCESS.md`** (agents **lead** this phase):

1. Identify vendor package under `Utilities/Migration Tools/<Vendor>/` and record package **`VERSION`** on the assessment.
2. Create the engagement folder: `Clients/<Client>/Conversion/<Engagement>/` (and/or Team Drive client tree).
3. **Copy** from the vendor package into that folder: Pipeline / SqlPackage scripts, `AgencyChecklist.md`, and Override **templates**.
4. Complete the **client** `AgencyChecklist.md`; fill Overrides from checklist answers (agency names, courts, officers, one-off key fixes).
5. Do **not** put agency-specific hardcodes into the shared vendor Pipeline. If a fix is reusable, **promote** it into the vendor package and bump `VERSION`.

**Folder model (authoritative):**

```text
Utilities/Migration Tools/          ← vendor packages (common only)
  <Vendor>/
    VERSION
    AgencyChecklist.md
    ConvertedAgencies.md
    StagingImporter/                ← when applicable
    SqlPackage/
      Pipeline/ or Common/scripts/
      Overrides/*.TEMPLATE.sql

Clients/<Client>/Conversion/...     ← engagement working copy
  AgencyChecklist.md                ← filled
  Overrides/                        ← filled agency SQL
  (pipeline scripts customized for this run)
```

See [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md) and [Migration Package Standards](vendor-packages/migration-package-standards.md).

### Phase 6 — Execute conversion

Follow [Decision 2](#decision-2--uat-versus-production-import).

- **Option A:** Import to UAT → validate → Production  
- **Option B:** Import to Production with converted-record tags  

### Phase 7 — Run post-conversion utilities

After import, use **Admin → Data Utilities** to:

- Advance converted **Incident / Citation / Warrant / Notepad** workflow statuses  
- **Snapshot** CAD call master records (`ConvertedOn` pending marker)  

Full procedure: [Post-Conversion Utilities](post-conversion-utilities.md).

### Phase 8 — Customer validation

**Thin Line first:** Complete [Migration Validation Standard](migration-validation-standard.md) Layers A–B (counts, relationships, spot checks).

**Today:** Implementation Lead notifies customer by email; customer validates; corrections via follow-up; informal acceptance.

**Target:** Deliver Conversion Summary, record counts, exception report, and [Customer Validation Checklist](../../../checklists/customer-validation-checklist.md); obtain [Customer Acceptance Form](../../../templates/customer-acceptance-form.md). Templates: [Conversion Summary](../../../templates/conversion-summary.md).

### Phase 9 — Close migration

Complete when corrections are done, customer has acknowledged, and internal documentation is updated.

**Target:** [Migration Close-Out Checklist](../../../checklists/migration-close-out-checklist.md).

---

## 10. Verification

Migration is complete when:

- [ ] Customer data has been successfully migrated
- [ ] Required post-conversion utilities have completed
- [ ] Customer has been notified
- [ ] Customer has had an opportunity to validate
- [ ] Outstanding conversion issues have been addressed
- [ ] Migration is closed (informal today; formal checklist in target state)

---

## 11. Failure and escalation

| Situation | Current practice | Escalation |
|-----------|------------------|------------|
| Cannot obtain legacy access or export | <mark style="color:red;">**TODO:**</mark> | <mark style="color:red;">**TODO:**</mark> |
| Conversion fails mid-run | <mark style="color:red;">**TODO:**</mark> | <mark style="color:red;">**TODO:**</mark> |
| Customer rejects validation findings | <mark style="color:red;">**TODO:**</mark> | <mark style="color:red;">**TODO:**</mark> |
| CJIS / security concern during access | **Stop.** Do not proceed without agreements and approved access | <mark style="color:red;">**Decision needed:**</mark> Named security / executive contact |

See also [Common risks](#common-risks).

---

## 12. KPIs

> <mark style="color:red;">**TODO:**</mark> Confirm definitions, owners, and reporting cadence.

| KPI | Definition | Target |
|-----|------------|--------|
| Average migration duration | Trigger → close (business days), excluding wait states | <mark style="color:red;">**TODO:**</mark> |
| Customer validation turnaround | Notification → acknowledgement | <mark style="color:red;">**TODO:**</mark> |
| Corrections after migration | Post-notification defect cycles | <mark style="color:red;">**TODO:**</mark> |
| Reuse rate | % using reusable vendor converter | <mark style="color:red;">**TODO:**</mark> |
| Manual effort per migration | Implementation hours | <mark style="color:red;">**TODO:**</mark> |
| Phase duration vs estimate | Actual vs [time expectations](#time-expectations) | <mark style="color:red;">**TODO:**</mark> |

---

## 13. Related documents

| Document | Relationship |
|----------|--------------|
| [Data conversion (CVE stage)](../../../customer-value-engine/deliver/data-conversion.md) | Stage context |
| [Customer Onboarding](../customer-onboarding.md) | Related Deliver SOP (placeholder) |
| [Bootstrap Environment](../infrastructure/bootstrap-environment.md) | Provision tenant before/with import (Infrastructure scripts) |
| [Post-Conversion Utilities](post-conversion-utilities.md) | Phase 7 — Admin Data Utilities (workflow + call snapshot) |
| [Migration Philosophy](migration-philosophy.md) | Principles |
| [Migration Architecture](migration-architecture.md) | One-page flow |
| [Migration Decision Matrix](migration-decision-matrix.md) | Package vs configuration |
| [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md) | Phase 1 / 5 — per-vendor knowledge |
| [Migration Package Standards](vendor-packages/migration-package-standards.md) | Manifest · VERSION · backlog |
| [Customer Configuration Standard](migration-customer-configuration.md) | Package + config = migration |
| [Migration Validation Standard](migration-validation-standard.md) | Definition of success |
| [Migration Metrics](migration-metrics.md) | Lightweight tracking |
| [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) | Phase 2 — required decision document |
| [Migration Pricing Policy](../../../policies/migration-pricing.md) | Phase 3 |
| [Customer Validation Checklist](../../../checklists/customer-validation-checklist.md) | Phase 8 |
| [Conversion Summary Template](../../../templates/conversion-summary.md) | Phase 8 |
| [Customer Acceptance Form](../../../templates/customer-acceptance-form.md) | Phase 8 |
| [Migration Close-Out Checklist](../../../checklists/migration-close-out-checklist.md) | Phase 9 |

---

## Continuous improvement system

Thin Line OS SOPs are not static manuals. Each SOP ends with the same improvement loop.

### Weaknesses

- No formal Legacy System Migration Assessment (or Approved Conversion Plan)  
- Pricing not standardized  
- Vendor packages started, but not every historical engagement promoted yet  
- Customer validation informal  
- No formal acceptance event  
- No standardized completion checklist  
- Limited customer visibility into migration progress  
- Founder-dependent execution for most paths  

### Automation opportunities

| Opportunity | Relieves |
|-------------|----------|
| Vendor catalog | Assessment / reuse decisions |
| Conversion registry | Status tracking, handoffs |
| Automated schema comparison | Mapping prep |
| AI-assisted field mapping | Mapping effort |
| Automated SQL generation | Preparation |
| Customer migration portal | Validation / visibility |
| Migration status dashboard | Customer and internal wait-state clarity |

### Product impact

How Thin Line Platform (or internal platform) improvements could **reduce or eliminate** work in this SOP — input to product planning, not a commitment list.

| If we build… | Work removed or reduced in this SOP |
|--------------|-------------------------------------|
| Supported Vendor Catalog | Manual “does a converter exist?” research |
| Migration Registry | Ad hoc status tracking and artifact hunting |
| Schema Comparison + Mapping Engine | Cursor-only / tribal mapping cycles |
| Customer Migration Portal | Email-driven validation and opaque progress |
| One-click / guided post-conversion utilities | Manual utility sequencing and tribal checklists |
| Stronger import tagging + environment tooling | Risky judgment calls on UAT vs Production |

> <mark style="color:red;">**TODO:**</mark> Rank which items belong on the product roadmap vs. internal-only tooling.

### Process maturity

| | |
|--|--|
| **Current level** | **2–3 / 5** |
| **Description** | Documented SOP + vendor Migration Tools packages with checklist-driven engagements. Assessment/pricing forms exist; validation and close still informal; founder still involved for many runs. |
| **Next milestone** | Delegate **standard** migrations (known vendor + existing package) to an Implementation specialist using this SOP, `PROCESS.md`, and vendor AgencyChecklist — without founder involvement. |
| **Future goal** | Any implementation specialist can complete a standard migration using documented tooling, with formal assessment, validation, and acceptance — without founder involvement. |

| Score | Meaning |
|------:|---------|
| 1 | Founder-driven |
| 2 | Documented |
| 3 | Standardized |
| 4 | Automated |
| 5 | Scalable |

### Next review date

| Field | Value |
|-------|-------|
| **Next review** | <mark style="color:red;">**TODO:**</mark> Set date (suggested 90 days from v1: **2026-10-17**) |
| **Review owner** | Implementation Lead |
| **Review questions** | Did measured phase times match estimates? Did any standard migration run without founder involvement? Which gaps closed? |

---

## Change history

| Date | Change | Author |
|------|--------|--------|
| 2026-07-17 | Initial draft — model SOP | Documentation draft |
| 2026-07-17 | v1 enrichment — executive summary, swimlane, decision trees, current/target/gap, risks, timing, automation score, product impact, process maturity | Documentation draft |
| 2026-07-17 | Phase 2 elevated to [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) (Assessments category) | Documentation draft |
| 2026-07-17 | Aligned with product-repo Migration Tools: vendor packages, PROCESS.md, checklist/Overrides, ConvertedAgencies, package standards | Documentation draft |
