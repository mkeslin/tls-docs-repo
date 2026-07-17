# Migration Package Standards

**Phase:** Deliver  
**Document type:** Reference / Standard  
**Status:** v1 — aligned with product-repo Migration Tools  
**Next review:** <mark style="color:$danger;">**TODO:**</mark> Set date (suggested: 2026-10-17)

---

## Purpose

Define what a **Thin Line Migration Package** is, how it is versioned, how agency work is separated from common logic, and how reusable improvements are promoted after each engagement.

**Authoritative implementation:** product monorepo  
`Utilities/Migration Tools/`  
Process file: `Utilities/Migration Tools/PROCESS.md`

Referenced by:

- [Legacy System Migration SOP](legacy-system-migration.md)
- [Vendor Conversion Guides](vendor-conversion-guides/README.md)
- [Migration Pricing Policy](../../policies/migration-pricing.md)

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
| `VERSION` file | Secrets, connection strings |

---

## Two-layer model

| Layer | What | Where |
|-------|------|--------|
| **Common** | Reusable conversion logic | `Utilities/Migration Tools/<Vendor>/` Pipeline, Common scripts, StagingImporter |
| **Agency** | Decisions and customer-specific SQL | Client engagement folder: filled checklist + `Overrides/` |

**Rule:** Never leave agency-specific hardcodes in the shared vendor Pipeline. If a fix is reusable across agencies, **promote** it into the package and bump `VERSION`.

---

## Layout (canonical)

```text
Utilities/Migration Tools/
  PROCESS.md                      ← agent-led engagement procedure
  <Vendor>/
    VERSION
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

## VERSION

Each vendor package has a `VERSION` file (not a path segment).

| When | Action |
|------|--------|
| Starting an engagement | Record package `VERSION` on the assessment / checklist |
| Promoting a reusable fix | Bump `VERSION` and note what changed |
| Closing an accepted conversion | Write agency, date, and package `VERSION` into `ConvertedAgencies.md` |

Historical runs before Migration Tools versioning use `pre-package` on the register.

---

## Engagement procedure (summary)

Full steps: product-repo `PROCESS.md`. Short form:

1. Identify vendor package + `VERSION`
2. Copy template into client engagement folder
3. Complete AgencyChecklist; fill Overrides
4. Execute StagingImporter (if any) + Pipeline order
5. Validate; customer acceptance
6. Promote reusable fixes; bump `VERSION`; update `ConvertedAgencies.md`

Cursor agents are expected to **lead** this procedure when a conversion is requested.

---

## Current vendor packages

See [Vendor Conversion Guides](vendor-conversion-guides/README.md).

| Vendor folder | Typical source |
|---------------|----------------|
| CrimeStar | Visual FoxPro / DBF → StagingImporter |
| CopSync | Kologik COPsync SQL → `Stg_CopSync_*` |
| IncodeCourt | Tyler / INCODE CTFILES and/or Common V14 Access |
| Xpediter | Firebird/InterBase `XPEDITER.GDB` → ConvTemp |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Placeholder created |
| 2026-07-17 | v1 — package definition, two-layer model, VERSION, promote rules (aligned with product Migration Tools) |
