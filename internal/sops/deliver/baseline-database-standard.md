# Baseline Database Standard

**Document type:** Standard  
**Status:** v1  

Defines the **seed databases** used when bootstrapping a new agency environment. Separate from the [Bootstrap Environment SOP](bootstrap-environment.md) (which imports them) and from [Legacy System Migration](legacy-system-migration.md) (which loads customer history).

---

## Purpose

A **baseline** (bacpac) is a known-good Thin Line RMS database used to create a new tenant DB quickly: schema, codes, seed agency placeholder, and platform defaults — **not** customer historical data.

---

## Canonical baseline (today)

| Field | Value |
|-------|--------|
| **Default path** | `Clients\_Base\Databases\_Base_ThinLineRMS.bacpac` |
| **Used by** | `Infrastructure/scripts/03-deploy-database.ps1` / `bootstrap-client.ps1` (default `-BacpacPath`) |
| **After import** | `sql/post-import-auth-users.sql`; optional `sql/post-import-agency-name.sql` when FriendlyAgencyName is set |
| **Elastic pool** | Per tier profile after import (prod typically moves to pool) |

Special seeds (if any) must be **explicit** on the engagement — do not silently substitute an old customer bacpac as the “base.”

---

## Ownership

| Role | Responsibility |
|------|----------------|
| **Engineering / platform** | Own baseline quality, schema currency, and publish path under `Clients\_Base\` |
| **Implementation** | Use the approved baseline (or documented exception) on bootstrap; never treat a finished customer DB as the new global base without promotion |

<mark style="color:red;">**TODO:**</mark> Name a single accountable owner (role + incumbent) for baseline refresh.

---

## When baselines are created / refreshed

| Event | Action |
|-------|--------|
| Major platform release needing new empty-tenant shape | Refresh baseline bacpac from an approved clean DB |
| Critical seed/code fix that all new tenants need | Refresh baseline **or** ensure migrations/deploy handle it for new DBs |
| After every customer conversion | **Do not** replace `_Base_ThinLineRMS.bacpac` with that customer’s DB |

<mark style="color:red;">**TODO:**</mark> Document refresh cadence (e.g. each release train) once practice is stable.

---

## Naming

| Artifact | Convention |
|----------|------------|
| Global RMS baseline | `_Base_ThinLineRMS.bacpac` |
| Future module-specific baselines | `_Base_<Product>.bacpac` under `Clients\_Base\Databases\` |
| Customer exports / backups | **Never** under `_Base_` — use client / backup locations |

---

## Retention and storage

| Topic | Today |
|-------|--------|
| Where the baseline lives | Product repo / deployment machine path `Clients\_Base\Databases\` |
| Azure backup of baseline file | <mark style="color:red;">**TODO:**</mark> confirm off-repo backup / artifact store |
| Retention of old baseline versions | <mark style="color:red;">**TODO:**</mark> keep N prior bacpacs vs overwrite only |

---

## Restore / import

| Action | How |
|--------|-----|
| **New environment** | Bootstrap Database step (SqlPackage Import) — see Bootstrap SOP |
| **Rebuild DB only** | `bootstrap-client.ps1 -Steps "Database"` (destructive reimport for that DB name) |
| **Point-in-time customer restore** | Not this standard — Azure SQL / backup ops <mark style="color:red;">**TODO:**</mark> link when documented |

Import **replaces** the database for that agency tier (script deletes/recreates via import). Treat as destructive for existing data in that DB.

---

## Related documents

| Document | Role |
|----------|------|
| [Bootstrap Environment Standard](bootstrap-environment-standard.md) | DB naming after import |
| [Bootstrap Environment SOP](bootstrap-environment.md) | Import procedure |
| [Environment Health Checklist](../../checklists/environment-health-checklist.md) | SQL reachable after bootstrap |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — baseline path, ownership, restore vs bootstrap |
