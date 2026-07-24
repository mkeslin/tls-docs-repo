# Tyler (INCODE CTFILES) Migration Guide

**Vendor folder:** `Utilities/Migration Tools/Tyler/`  
**Package VERSION:** see product-repo `Tyler/VERSION`  
**Aliases:** Tyler · INCODE · municipal court CTFILES  
**Status:** Package draft — GitBook guide v1  

Execution: product `PROCESS.md` + `Tyler/AgencyChecklist.md`.

---

## Supported versions

| Path | Source | Notes |
|------|--------|-------|
| **CTFILES** | Fixed-layout court files | StagingImporter → SQL staging |
| Tyler / INCODE product years | <mark style="color:red;">**TODO:**</mark> document years/builds actually converted |

For **Common V14 Access** packages, use [Asyst](asyst.md). For **FundView**, use [FundView](fundview.md).

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] CTFILES extract available
- [ ] SQL Server for staging + Thin Line court/RMS target
- [ ] Court agency / LE agency relationship understood

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| Shallowater migrate SQL purged | StagingImporter + layout reference remain; recover migrate scripts from history when needed |
| Court vs RMS agency Ids | Explicit maps in client Overrides |
| CTFILES LRECL vs SQL column widths | See StagingImporter README — do not naive-map from restored SQL |

---

## Schema notes

- StagingImporter owns CTFILES → staging shape.
- Breaking staging layout = **MAJOR** package bump.

---

## Extraction process

1. Obtain CTFILES set.  
2. Run `Tyler/StagingImporter/`.  
3. Pipeline / Overrides per `Tyler/SqlPackage` *(migrate Pipeline TBD)*.  

---

## Special mappings

| Mapping | Where |
|---------|-------|
| Court agency | Client Overrides |
| Offense / statute maps | Checklist → Overrides |
| Person / defendant identity | Overrides + validation spot checks |

---

## Validation checklist

Apply [Migration Validation Standard](../../migration-validation-standard.md), plus:

- [ ] Case / citation / violation counts vs source  
- [ ] Defendant person linkage spot checks  
- [ ] Fee / disposition samples if in scope  
- [ ] Court UI open of sample cases  

---

## Lessons learned

| Date | Lesson |
|------|--------|
| 2026-07-23 | Split from former IncodeCourt umbrella into Tyler / FundView / Asyst |

Register: `Tyler/ConvertedAgencies.md` (Shallowater Municipal Court historical).

---

## Package backlog

- [ ] Document supported Tyler/INCODE years explicitly  
- [ ] Promote recovered migrate SQL into `SqlPackage/Pipeline/`  
- [ ] Attachment / image support matrix for court packages  

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-23 | v1 — split from IncodeCourt guide |
