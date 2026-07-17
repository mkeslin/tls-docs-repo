# Xpediter Migration Guide

**Vendor folder:** `Utilities/Migration Tools/Xpediter/`  
**Package VERSION:** see product-repo `Xpediter/VERSION`  
**Source:** Firebird / InterBase `XPEDITER.GDB` â†’ SQL **ConvTemp** â†’ ThinLineRMS  
**Status:** Package exists (`draft` typical) â€” GitBook guide v1  

Execution: product `PROCESS.md` + `Xpediter/AgencyChecklist.md`.

---

## Supported versions

| Legacy | Notes |
|--------|-------|
| XPEDITER GDB (Firebird/InterBase) | Primary |
| Specific GDB ODS / app versions | <mark style="color:red;">**TODO:**</mark> record from LCISD / Shallowater / later engagements |

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] `XPEDITER.GDB` (or approved extract) + Firebird tooling as required by Pipeline docs
- [ ] SQL Server ConvTemp + Thin Line target
- [ ] Agree ConvTemp database name (checklist placeholder in `01` scripts)

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| Agency hardcodes in shared Pipeline | Package scrubbed â€” use Override templates (`07a`, `13`, etc.) |
| Duplicate folders / final cleanup | Client Overrides from templates â€” not common Pipeline |
| Large GDB | Plan time; year filters on utilities |

---

## Schema notes

- ConvTemp tables (`CAGENCY`, `DFOLDER`, â€¦) are the staging contract.
- Pipeline under `SqlPackage/Pipeline/` is **common only**.
- Parameterize ConvTemp DB name in the **client** copy.

---

## Extraction process

1. Obtain GDB; restore/access per package docs.  
2. Load / transform into SQL ConvTemp.  
3. Run Pipeline in `PIPELINE.md` order (client copy).  
4. Fill Overrides from checklist (duplicates, cleanup, agency seed).  

---

## Special mappings

| Mapping | Where |
|---------|-------|
| Agency / ORI | Checklist + client Overrides |
| Duplicate folder remediation | Override template `07a` (client) |
| Final cleanup | Override template `13` (client) |
| Officers | Checklist â†’ Overrides |

---

## Validation checklist

Apply [Migration Validation Standard](../../migration-validation-standard.md), plus:

- [ ] ConvTemp counts vs Thin Line for in-scope modules  
- [ ] Incident / call / citation samples as scoped  
- [ ] Duplicate-folder remediation verified if used  
- [ ] Post-conversion utilities  

---

## Common problems

| Problem | Likely cause |
|---------|----------------|
| Scripts still point at prior agency ConvTemp name | Forgot client parameter replace |
| Shared Pipeline edited for one agency | Revert; move to Overrides; promote only if reusable |
| Masters missing on calls | Snapshot utility not run |

---

## Lessons learned

| Date | Lesson |
|------|--------|
| 2026-07 | LCISD / Shallowater used to seed package; hardcodes removed in favor of placeholders + Override templates |
| <mark style="color:red;">**TODO:**</mark> | Post-acceptance VERSION-tagged lessons |

Register: `Xpediter/ConvertedAgencies.md`.

---

## Package backlog

- [ ] Document supported GDB / app versions  
- [ ] Improve officer mapping from multi-agency runs  
- [ ] Property / evidence support matrix  
- [ ] Attachment extraction hardening  

---

## Manifest snapshot

| Field | Value |
|-------|-------|
| Vendor | Xpediter |
| Requires | Firebird/InterBase GDB access Â· SQL Server ConvTemp Â· Thin Line target |
| Typical modules | RMS modules present in GDB *(confirm on checklist)* |
| Validation emphasis | Module counts Â· duplicate cleanup Â· call snapshots |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 GitBook guide |
