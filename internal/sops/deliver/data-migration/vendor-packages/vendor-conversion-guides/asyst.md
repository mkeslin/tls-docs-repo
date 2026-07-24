# Asyst (Common V14 Access) Migration Guide

**Vendor folder:** `Utilities/Migration Tools/Asyst/`  
**Package VERSION:** see product-repo `Asyst/VERSION`  
**Aliases:** Asyst · Thin Line Common V14 Access court packages  
**Status:** Package draft — Pipeline promoted from New Deal  

Execution: product `PROCESS.md` + `Asyst/AgencyChecklist.md`.

---

## Supported versions

| Path | Source | Notes |
|------|--------|-------|
| **Common V14 Access** | `.accdb` court package set | Access → SQL → `Stg_CommonV14_*` → migrate |

First engagement: New Deal Municipal Court (`Clients/NewDealMunicipalCourt/Conversion/Conversion-NewDealMunicipalCourt/`).

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] Common V14 `.accdb` set (Master Name, Citations, Municipal Court, Personnel, Common)
- [ ] Microsoft Access Database Engine for import
- [ ] SQL Server for staging + Thin Line court/RMS target

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| Agency fines / GL / municipal codes | Use Overrides templates (`11_*`, `18b`/`18c`, `19c_MunicipalOrdinances`) — not common Pipeline hardcodes |
| State offense missing from catalog | Leave `OffenseId` null; **do not** insert state rows into `dbo.Offenses` |
| Municipal offenses | Conversion may create Offenses only with statute **`CO` / `CITY ORDINANCES`** |

---

## Schema notes

- Staging via Access import + `15_LegacyTables` → `Stg_CommonV14_*`.
- Offense map: `19c` DPS crosswalk + optional municipal seed Override; `19d` creates municipal Offenses only.
- Post-import health (`Conversion6-Health`) stays engagement-only.

---

## Extraction process

1. Obtain `.accdb` set.  
2. Run Access→SQL import (`Import-CommonV14AccessToSql.ps1`).  
3. Fill Overrides (GL, municipal ordinances, fine tables).  
4. Run Pipeline order in `Asyst/SqlPackage/PIPELINE.md`.  

---

## Special mappings

| Mapping | Where |
|---------|-------|
| Court / citation agency Ids | Parameters / Overrides |
| Municipal ordinances | `Overrides/19c_MunicipalOrdinances.TEMPLATE.sql` |
| GL chart | `Overrides/11_AccountingAccounts_GLMap.TEMPLATE.sql` |
| Speeding fines | `Overrides/18b` / `18c` TEMPLATEs |

---

## Validation checklist

Apply [Migration Validation Standard](../../migration-validation-standard.md), plus:

- [ ] Case / citation / violation counts vs source  
- [ ] Defendant person linkage spot checks  
- [ ] Fee / disposition / balance samples  
- [ ] Confirm no conversion-created **state** offenses in `dbo.Offenses`  

Register: `Asyst/ConvertedAgencies.md`.

---

## Package backlog

- [ ] Strip remaining New Deal–specific comments from Pipeline as further agencies land  
- [ ] Shared court validation queries  
- [ ] Attachment / image support matrix  

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-23 | v1 — split from IncodeCourt; Pipeline from New Deal engagement |
