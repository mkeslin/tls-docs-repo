# Vendor Conversion Guides

**Document type:** Reference index  
**Status:** v1 — catalog (detailed per-vendor runbooks live in product Git)  
**Next review:** <mark style="color:red;">**TODO:**</mark> Set date (suggested: 2026-10-17)

Referenced by: [Legacy System Migration](../legacy-system-migration.md) (Phases 1 and 5) · [Migration Package Standards](../migration-package-standards.md)

---

## Purpose

Index supported legacy vendors/products, typical extract methods, and where the **Migration Package** lives in the product monorepo.

Detailed Pipeline docs, AgencyChecklist, and Override templates are **not** duplicated here—they are versioned with the code under:

`Utilities/Migration Tools/<Vendor>/`

---

## Supported vendors (Migration Tools)

| Vendor (folder) | Product / alias | Typical extract | Staging | Package notes |
|-----------------|-----------------|-----------------|---------|---------------|
| **CrimeStar** | CrimeStar RMS (FoxPro / DBF) | Agency DBF + FPT folder | StagingImporter → `cs_*` then adapter to `Stg_CopSync_*` | AgencyChecklist + SqlPackage helpers |
| **CopSync** | COPsync / **Kologik** | SQL Server CopSync DB (cloud export or backup) | Stage into `Stg_CopSync_*` | Backfill pattern; officer/court Overrides |
| **IncodeCourt** | Tyler / INCODE court; Thin Line Common V14 Access | CTFILES fixed files and/or `.accdb` set | StagingImporter (CTFILES) and/or Access→SQL | Two paths on AgencyChecklist |
| **Xpediter** | XPEDITER (often `XPEDITER.GDB`) | Firebird/InterBase → SQL ConvTemp | ConvTemp tables (`CAGENCY`, `DFOLDER`, …) | Checklist placeholders in `01`; Override templates for duplicates / final cleanup |

**Converted agencies register:** each package includes `ConvertedAgencies.md` (agency, date, package `VERSION`).

---

## How to start an engagement

1. Confirm vendor on the [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md).
2. Open `Utilities/Migration Tools/<Vendor>/` and note `VERSION`.
3. Follow `Utilities/Migration Tools/PROCESS.md` (copy → checklist → Overrides → promote).
4. Use that vendor’s `AgencyChecklist.md` as the agency evaluation form.

Do **not** copy the last customer’s filled Overrides as the new default. Start from the vendor package templates.

---

## Known gaps

| Gap | Notes |
|-----|-------|
| Full Pipeline SQL still in some `Clients/.../Conversion/` folders | Promote common steps into vendor packages over time |
| Jail / JP CSV (e.g. Crosby County Jail) | Not a CopSync package; separate path <mark style="color:red;">**TODO**</mark> |
| Per-vendor narrative guides in GitBook | Optional deeper pages later; package README + PIPELINE.md are source of truth for execution |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Placeholder index |
| 2026-07-17 | v1 catalog — CrimeStar, CopSync/Kologik, IncodeCourt, Xpediter; links to Migration Tools |
