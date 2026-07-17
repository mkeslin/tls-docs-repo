# CrimeStar Migration Guide

**Vendor folder:** `Utilities/Migration Tools/CrimeStar/`  
**Package VERSION:** see product-repo `CrimeStar/VERSION` (verify at engagement start)  
**Status:** Package exists â€” GitBook guide v1  

Execution: product `PROCESS.md` + `CrimeStar/AgencyChecklist.md`. Do not duplicate Pipeline SQL here.

---

## Supported versions

| Legacy | Notes |
|--------|-------|
| CrimeStar RMS (Visual FoxPro / xBase `.dbf` + `.fpt`) | Primary path |
| Specific CrimeStar product builds | <mark style="color:red;">**TODO:**</mark> document known build/version strings from past engagements |

---

## Required access

- [ ] SaaS + CJIS signed (hard stop)
- [ ] Agency CrimeStar data folder (DBF + FPT pairs)
- [ ] SQL Server for StagingImporter output + Thin Line target
- [ ] Thin Line tenant ready ([Bootstrap Environment](../../../infrastructure/bootstrap-environment.md))

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| Memo / FPT pairing missing | Confirm complete DBF+FPT set before StagingImporter |
| Module not in export | Scope on checklist; do not assume full RMS |
| <mark style="color:red;">**TODO:**</mark> | Capture engagement-specific gotchas here after each run |

---

## Schema notes

- Source is **file-based FoxPro**, not a live SQL RMS schema.
- StagingImporter loads to `cs_*` staging, then adapter path toward `Stg_CopSync_*` / migrate helpers (see package `SqlPackage/`).
- Treat staging table shapes as package-owned; breaking staging changes = **MAJOR** version bump.

---

## Extraction process

1. Obtain full DBF/FPT folder from agency (or vendor export).
2. Run `CrimeStar/StagingImporter/` against that folder â†’ staging SQL DB.
3. Spot-check table counts vs checklist modules.
4. Continue Pipeline order in `SqlPackage/PIPELINE.md` (client working copy).

---

## Special mappings

| Mapping | Where |
|---------|-------|
| Agency / ORI / court | Client Overrides / ensure-agency scripts |
| Officers / badges / usernames | Client Overrides (`21a`-style) |
| Hist / number prefixes | Checklist â†’ Overrides |

Reusable mapping **logic** â†’ promote into package.

---

## Validation checklist

Apply [Migration Validation Standard](../../migration-validation-standard.md), plus:

- [ ] Staging table counts vs modules present in export  
- [ ] Incident / citation / call samples (as in scope)  
- [ ] Attachments if converted  
- [ ] Post-conversion utilities for modules imported  

---

## Common problems

| Problem | Likely cause |
|---------|----------------|
| Empty staging tables | Wrong folder / incomplete DBF set |
| Agency hardcodes in shared Pipeline | Violates package rules â€” move to Overrides |
| UI records stuck in conversion workflow | Run [Post-Conversion Utilities](../../post-conversion-utilities.md) |

---

## Lessons learned

| Date | Lesson |
|------|--------|
| <mark style="color:red;">**TODO:**</mark> | Add after each accepted conversion |

Register: product `CrimeStar/ConvertedAgencies.md`.

---

## Package backlog

Improvements identified (reusable â€” not customer notes):

- [ ] <mark style="color:red;">**TODO:**</mark> Seed from recent assessments / engagements  
- [ ] Document supported CrimeStar build strings  
- [ ] Strengthen attachment extraction notes  

When done: implement in package, bump `VERSION`, check off here.

---

## Manifest snapshot *(human-readable)*

| Field | Value |
|-------|-------|
| Vendor | CrimeStar |
| Requires | DBF/FPT folder Â· SQL Server Â· StagingImporter |
| Typical modules | Incidents, citations, CAD, vehicles, property, warrants, attachments *(confirm per export)* |
| Entities | Persons, vehicles, locations *(via involvements / masters â€” confirm per run)* |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 GitBook guide (points at Migration Tools package) |
