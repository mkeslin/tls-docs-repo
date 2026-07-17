# CopSync / Kologik Migration Guide

**Vendor folder:** `Utilities/Migration Tools/CopSync/`  
**Package VERSION:** see product-repo `CopSync/VERSION`  
**Product labels:** COPsync · **Kologik** (same family; staging uses `Stg_CopSync_*`)  
**Status:** Package exists (often `draft`) — GitBook guide v1  

Execution: product `PROCESS.md` + `CopSync/AgencyChecklist.md`.

---

## Supported versions

| Legacy | Notes |
|--------|-------|
| COPsync / Kologik SQL Server databases | Cloud export or backup restore to SQL |
| Specific vendor schema versions | <mark style="color:red;">**TODO:**</mark> list known schema generations from Crosby / Crosbyton / Petersburg work |

---

## Required access

- [ ] SaaS + CJIS signed
- [ ] SQL Server CopSync DB (export or backup) readable by Implementation
- [ ] Thin Line target DB / tenant
- [ ] Clarity on **backfill** vs greenfield agency

---

## Known issues

| Issue | Mitigation |
|-------|------------|
| Jail / JP CSV is **not** this package | Separate path (e.g. Crosby County Jail) |
| Partial historical backfills | Track status Partial on `ConvertedAgencies.md`; re-validate counts |
| Officer / court maps differ per agency | Client Overrides — never bake last customer into common scripts |
| <mark style="color:red;">**TODO:**</mark> | Schema drift across Kologik versions |

---

## Schema notes

- Stage into `Stg_CopSync_*` then backfill / migrate into ThinLineRMS per Pipeline docs.
- Preserve conversion tags (`ImportSource`, etc.) for validation and utilities.
- Common helpers live under `SqlPackage/Common/scripts/`.

---

## Extraction process

1. Obtain CopSync SQL backup or cloud export.
2. Restore / attach to a working SQL instance.
3. Run staging → Pipeline in `SqlPackage` order (client copy).
4. Apply Overrides from checklist (officers, courts, agency).

---

## Special mappings

| Mapping | Where |
|---------|-------|
| Officers | Client Overrides |
| Courts / agencies | Client Overrides |
| Backfill vs new agency seed | Checklist + ensure scripts in client copy |

---

## Validation checklist

Apply [Migration Validation Standard](../../migration-validation-standard.md), plus:

- [ ] Incident / person / citation counts vs source (document deltas)  
- [ ] Backfill: confirm no unintended overwrite of live Thin Line rows  
- [ ] Post-conversion utilities  
- [ ] Exception list for Partial historical years  

---

## Common problems

| Problem | Likely cause |
|---------|----------------|
| Wrong agency Id on converted rows | TargetAgencyId / ensure-agency misconfigured |
| Live data damaged on backfill | Missing conversion tags / wrong filter — stop and escalate |
| “Copy Crosbyton Overrides” | Forbidden as package default — start from templates |

---

## Lessons learned

| Date | Lesson |
|------|--------|
| 2026 | Crosby COSO completed pre-package; Crosbyton / Petersburg used as backfill patterns — promote only reusable bits |
| <mark style="color:red;">**TODO:**</mark> | Add post-acceptance lessons with package VERSION |

Register: `CopSync/ConvertedAgencies.md`.

---

## Package backlog

- [ ] Harden schema-version notes for Kologik exports  
- [ ] Improve officer mapping templates from multi-agency lessons  
- [ ] Automate citation validation helpers where reusable  
- [ ] Clarify attachment extraction support matrix  

---

## Manifest snapshot

| Field | Value |
|-------|-------|
| Vendor | CopSync / Kologik |
| Requires | SQL Server (source + target) |
| Typical modules | RMS / incidents, citations, related masters *(confirm per DB)* |
| Validation emphasis | Incident counts · person counts · backfill safety |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 GitBook guide |
