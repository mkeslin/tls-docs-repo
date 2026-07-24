# Cardinal Badge Migration Guide

**Vendor folder:** `Utilities/Migration Tools/CardinalBadge/`  
**Package VERSION:** see product-repo `CardinalBadge/VERSION`  
**Aliases:** Cardinal Tracking Badge · CTI · BFW/CAD/CRT · (not modern Kologik CopSync)  
**Status:** Package exists — GitBook guide v1  

Execution: product `PROCESS.md` + `CardinalBadge/AgencyChecklist.md` + `SOURCE-SCHEMA.md`.

---

## Supported versions

| Path | Source | Notes |
|------|--------|-------|
| On-prem Badge SQL | `BFW` + `CAD` + `CRT` modules | Stage to `Stg_Badge_*` |

Do **not** confuse with [`CopSync / Kologik`](copsync-kologik.md) (`AgencyCases` / `pk_*`).

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] Badge SQL database available
- [ ] ThinLineRMS target agency configured
- [ ] Hub / environment confirmed

---

## Extraction process

1. Confirm Badge fingerprint (see product `SOURCE-SCHEMA.md`).  
2. Run `CardinalBadge/SqlPackage/Pipeline` staging + migrate (engagement copy).  
3. Agency Overrides for officers / courts as needed.  

Register: `CardinalBadge/ConvertedAgencies.md`.

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-23 | v1 GitBook guide (product package already existed) |
