# IncodeCourt (Tyler / INCODE) Migration Guide

**Vendor folder:** `Utilities/Migration Tools/IncodeCourt/`  
**Package VERSION:** see product-repo `IncodeCourt/VERSION`  
**Aliases:** Tyler · INCODE · municipal court CTFILES · Thin Line Common V14 Access packages  
**Status:** Package exists — GitBook guide v1  

Execution: product `PROCESS.md` + `IncodeCourt/AgencyChecklist.md` (two paths).

---

## Supported versions

| Path | Source | Notes |
|------|--------|-------|
| **CTFILES** | Fixed-layout court files | StagingImporter → SQL staging |
| **Common V14 Access** | `.accdb` court package set | Access → SQL path on checklist |
| Tyler / INCODE product years | <mark style="color:red;">**TODO:**</mark> document years/builds actually converted |

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] CTFILES **or** Access court package (per path)
- [ ] SQL Server for staging + Thin Line court/RMS target
- [ ] Court agency / LE agency relationship understood

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| Two extract paths | Choose on AgencyChecklist; do not mix blindly |
| Court vs RMS agency Ids | Explicit maps in client Overrides |
| <mark style="color:red;">**TODO:**</mark> | Docket / fee / disposition quirks by INCODE version |

---

## Schema notes

- StagingImporter owns CTFILES → staging shape.
- Court violation / citation targets in Thin Line may require post-steps beyond RMS incident packages—confirm modules on assessment.
- Breaking staging layout = **MAJOR** package bump.

---

## Extraction process

### Path A — CTFILES

1. Obtain CTFILES set.  
2. Run `IncodeCourt/StagingImporter/`.  
3. Pipeline / Overrides per `SqlPackage`.  

### Path B — Access (Common V14–style)

1. Obtain `.accdb` set.  
2. Follow AgencyChecklist Access→SQL steps.  
3. Pipeline / Overrides.  

---

## Special mappings

| Mapping | Where |
|---------|-------|
| Court agency | Client Overrides |
| Offense / statute maps | Checklist → Overrides / package common if reusable |
| Person / defendant identity | Overrides + validation spot checks |

---

## Validation checklist

Apply [Migration Validation Standard](../migration-validation-standard.md), plus:

- [ ] Case / citation / violation counts vs source  
- [ ] Defendant person linkage spot checks  
- [ ] Fee / disposition samples if in scope  
- [ ] Court UI open of sample cases  

---

## Common problems

| Problem | Likely cause |
|---------|----------------|
| Empty staging | Wrong CTFILES set or Access path mismatch |
| Cases in wrong court agency | Agency map error |
| RMS-only validation applied | Use court-focused samples |

---

## Lessons learned

| Date | Lesson |
|------|--------|
| <mark style="color:red;">**TODO:**</mark> | Add from ConvertedAgencies + assessments |

Register: `IncodeCourt/ConvertedAgencies.md`.

---

## Package backlog

- [ ] Document supported Tyler/INCODE years explicitly  
- [ ] Expand offense mapping guidance  
- [ ] Attachment / image support matrix for court packages  
- [ ] Shared validation queries for docket counts  

---

## Manifest snapshot

| Field | Value |
|-------|-------|
| Vendor | IncodeCourt (Tyler / INCODE) |
| Requires | CTFILES and/or Access · SQL Server · StagingImporter (CTFILES) |
| Typical modules | Court / citations / violations *(confirm)* |
| Validation emphasis | Case counts · defendant links · dispositions |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 GitBook guide |
