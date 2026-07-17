# Migration Package Standards

**Phase:** Deliver  
**Document type:** Reference / Standard  
**Status:** v1  
**Next review:** <mark style="color:red;">**TODO:**</mark> Set date (suggested: 2026-10-17)

---

## Purpose

Define what a **Thin Line Migration Package** is, how it is versioned, what metadata it should carry, how agency work is separated from common logic, and how reusable improvements are promoted after each engagement.

**Authoritative implementation:** product monorepo  
`Utilities/Migration Tools/`  
Process file: `Utilities/Migration Tools/PROCESS.md`

**Principles:** [Migration Philosophy](../migration-philosophy.md) · **Flow:** [Migration Architecture](../migration-architecture.md)

Referenced by:

- [Legacy System Migration SOP](../legacy-system-migration.md)
- [Vendor Conversion Guides](vendor-conversion-guides/README.md)
- [Migration Overrides & Mapping Standard](../migration-customer-configuration.md)
- [Migration Pricing Policy](../../../../policies/migration-pricing.md)

---

## What is a Migration Package?

A **vendor package** is a self-contained folder for one legacy product family. It contains everything needed to start a **standard** conversion for that vendor—except agency-specific values.

| Included | Not included |
|----------|--------------|
| Common Pipeline / SqlPackage scripts | Agency names, phones, ORIs, email domains |
| StagingImporter (when extract format needs it) | One-off source-key remediations |
| `AgencyChecklist.md` (questions) | Filled checklist answers |
| Override **templates** (`.TEMPLATE`) | Filled Overrides for a customer |
| `ConvertedAgencies.md` register | Customer data / GDB / exports |
| `VERSION` (+ manifest fields below) | Secrets, connection strings |

---

## Two-layer model

| Layer | What | Where |
|-------|------|--------|
| **Common** | Reusable conversion logic | `Utilities/Migration Tools/<Vendor>/` Pipeline, Common scripts, StagingImporter |
| **Agency** | Decisions and customer-specific SQL | Client engagement folder: filled checklist + `Overrides/` |

**Rule:** Never leave agency-specific hardcodes in the shared vendor Pipeline. If a fix is reusable across agencies, **promote** it into the package and bump `VERSION`.

Equation: [Migration Overrides & Mapping Standard](../migration-customer-configuration.md) — **Package + Configuration = Migration**.

---

## Layout (canonical)

```text
Utilities/Migration Tools/
  PROCESS.md                      ← agent-led engagement procedure
  <Vendor>/
    VERSION                       ← semver + notes (required today)
    README.md
    AgencyChecklist.md
    ConvertedAgencies.md
    StagingImporter/              ← optional
    SqlPackage/
      PIPELINE.md
      PARAMETERS.md
      Pipeline/ or Common/scripts/
      Overrides/*.TEMPLATE.sql
```

Engagement working copy:

```text
Clients/<Client>/Conversion/<Engagement>/
  AgencyChecklist.md              ← filled
  Overrides/                      ← filled from templates
  (copied pipeline scripts)
```

Team Drive client trees may host the same engagement assets when that is the operational home.

---

## Package manifest

Every package should expose **metadata** so humans (and later Hub) know what it supports without reading all SQL.

### Today (required)

The `VERSION` file is the version authority. Capture the rest in the vendor **GitBook guide** and/or package `README.md`:

| Field | Example | Where |
|-------|---------|-------|
| Vendor / product | CopSync / Kologik | Guide + README |
| Package version | `0.3.1-draft` | `VERSION` |
| Status | `current` / `draft` | `VERSION` notes |
| Supported legacy versions | <mark style="color:red;">**TODO:**</mark> per vendor | Vendor guide |
| Modules supported | Incidents, Citations, … | Vendor guide + checklist |
| Entities supported | Persons, Vehicles, … | Vendor guide |
| Requires | SQL Server, Firebird tools, … | Vendor guide |
| Validation emphasis | Incident counts, … | Vendor guide → [Validation Standard](../migration-validation-standard.md) |

### Target (optional file)

When tooling is ready, add `MANIFEST.yaml` (or `.json`) beside `VERSION`, e.g.:

```yaml
vendor: CopSync
product: COPsync / Kologik
packageVersion: 0.3.1-draft
status: draft
supportedLegacyVersions: []   # fill as known
modules: [RMS, Citations]     # example
entities: [Persons, Vehicles, Incidents]
requires: [SQL Server]
validation:
  - Incident counts
  - Person counts
```

Hub may eventually read this file. Until then, **do not** invent a second version number—`VERSION` remains canonical.

---

## Package versioning

Each vendor package has a `VERSION` file (not a path segment). Prefer semver (`MAJOR.MINOR.PATCH`) with optional `-draft` suffix.

### When to bump

| Change | Bump | Example |
|--------|------|---------|
| Reusable Pipeline / StagingImporter / Common script fix or new common step | **MINOR** (or PATCH if tiny) | Better join; new shared cleanup step |
| Breaking change to how engagements must be configured (template rename, required new Override, incompatible staging shape) | **MAJOR** | Staging table rename; checklist section required |
| Docs / checklist wording only | **PATCH** or note-only if truly cosmetic | Clarify question text |
| Agency-only Override in client folder | **No bump** | Customer config |

### Draft vs current

| Status | Meaning |
|--------|---------|
| `draft` | Usable but not fully hardened; expect checklist gaps |
| `current` | Default package for new engagements of that vendor |

### Retiring versions

- Do **not** delete historical path snapshots lightly if they document what shipped (`v1.0.0/` folders may exist for archive).  
- New work uses the **root** vendor folder `VERSION`.  
- `ConvertedAgencies.md` records which `VERSION` was used for acceptance—that is the audit trail.  
- Retire a major line only when no in-flight engagement depends on it; note retirement in the vendor guide changelog.

### Engagement rules

| When | Action |
|------|--------|
| Starting an engagement | Record package `VERSION` on the assessment / checklist |
| Promoting a reusable fix | Bump `VERSION` and note what changed |
| Closing an accepted conversion | Write agency, date, and package `VERSION` into `ConvertedAgencies.md` |

Historical runs before Migration Tools versioning use `pre-package` on the register.

---

## Package backlog

Reusable improvements are **package backlog**, not customer notes.

### Sources

1. End of every [Legacy System Migration Assessment](../../../../assessments/legacy-system-migration-assessment.md) — **Package backlog** section  
2. Lessons during execution (Phase E promote in `PROCESS.md`)  
3. Validation exceptions that imply a package gap  

### Shape (per vendor)

Track in the vendor GitBook guide (Backlog section) and/or a short list in package `README.md`:

```text
Improvements identified:
★ Add property support
★ Improve officer mapping
★ Automate citation validation
★ Fix attachment extraction
```

| Item type | Action |
|-----------|--------|
| Package backlog | Fix in `Migration Tools/<Vendor>/`; bump `VERSION` when done |
| Customer-only follow-up | Stay on engagement notes / exception report |

Closing a backlog item without a `VERSION` bump is incomplete.

---

## Engagement procedure (summary)

Full steps: product-repo `PROCESS.md`. Short form:

1. Identify vendor package + `VERSION`
2. Copy template into client engagement folder
3. Complete AgencyChecklist; fill Overrides ([configuration](../migration-customer-configuration.md))
4. Execute StagingImporter (if any) + Pipeline order
5. [Post-conversion utilities](../post-conversion-utilities.md); [validate](../migration-validation-standard.md); customer acceptance
6. Promote reusable fixes; bump `VERSION`; update `ConvertedAgencies.md`; close package backlog items

Cursor agents are expected to **lead** this procedure when a conversion is requested.

---

## Current vendor packages

See [Vendor Conversion Guides](vendor-conversion-guides/README.md).

| Vendor folder | Typical source | Package VERSION *(product repo — verify)* |
|---------------|----------------|---------------------------------------------|
| CrimeStar | Visual FoxPro / DBF → StagingImporter | See `VERSION` |
| CopSync | Kologik COPsync SQL → `Stg_CopSync_*` | See `VERSION` |
| IncodeCourt | Tyler / INCODE CTFILES and/or Common V14 Access | See `VERSION` |
| Xpediter | Firebird/InterBase `XPEDITER.GDB` → ConvTemp | See `VERSION` |

---

## Related standards

| Document | Role |
|----------|------|
| [Migration Validation Standard](../migration-validation-standard.md) | Success criteria |
| [Migration Decision Matrix](../migration-decision-matrix.md) | Package vs config |
| [Migration Metrics](../migration-metrics.md) | VERSION / hours / reruns |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Placeholder created |
| 2026-07-17 | v1 — package definition, two-layer model, VERSION, promote rules |
| 2026-07-17 | Manifest fields, versioning/retire rules, package backlog |
