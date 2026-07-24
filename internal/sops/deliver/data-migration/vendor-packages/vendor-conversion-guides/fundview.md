# FundView Migration Guide

**Vendor folder:** `Utilities/Migration Tools/FundView/`  
**Package VERSION:** see product-repo `FundView/VERSION`  
**Aliases:** FundView municipal court  
**Status:** Package scaffold — Pipeline SQL not yet promoted  

Execution: product `PROCESS.md` + `FundView/AgencyChecklist.md`.

---

## Supported versions

| Path | Source | Notes |
|------|--------|-------|
| FundView extract | <mark style="color:red;">**TODO:**</mark> document format(s) from next engagement | Slaton scripts purged historically |

Do not invent a fake pipeline. Recover reusable SQL from git history / Team Drive on the next engagement, then promote into `SqlPackage/Pipeline/`.

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] FundView source extract available
- [ ] SQL Server for staging + Thin Line court/RMS target
- [ ] Court agency / LE agency relationship understood

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| No Pipeline SQL in package yet | Scaffold only; recover from Slaton history when starting next FundView court |
| Slaton prod patterns cited by Asyst/New Deal | TMCEC `DpsCode` conventions — see Asyst package docs |

---

## Extraction process

1. Confirm source format on AgencyChecklist.  
2. Stage into SQL.  
3. Promote common migrate scripts into the vendor package after first successful reuse.  

---

## Validation checklist

Apply [Migration Validation Standard](../../migration-validation-standard.md), plus court-focused samples (cases, defendants, fees).

Register: `FundView/ConvertedAgencies.md` (Slaton Municipal Court historical).

---

## Package backlog

- [ ] Recover and promote Pipeline SQL from Slaton engagement history  
- [ ] Document FundView extract formats  
- [ ] Offense / fine mapping guidance  

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-23 | v1 scaffold — split from IncodeCourt umbrella |
