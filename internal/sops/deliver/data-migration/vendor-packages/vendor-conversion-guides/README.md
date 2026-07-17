# Vendor Conversion Guides

**Document type:** Reference index  
**Status:** v1 — catalog + per-vendor guides  
**Next review:** <mark style="color:red;">**TODO:**</mark> Set date (suggested: 2026-10-17)

Referenced by: [Legacy System Migration](../../legacy-system-migration.md) · [Migration Package Standards](../migration-package-standards.md) · [Migration Architecture](../../migration-architecture.md)

---

## Purpose

**Vendor-specific knowledge lives here** (and in the product package)—not inside the Legacy System Migration SOP.

Each guide covers: supported versions, access, known issues, schema notes, extraction, special mappings, validation emphasis, common problems, lessons learned, and **package backlog**.

Detailed Pipeline SQL stays versioned with the code:

`Utilities/Migration Tools/<Vendor>/`

---

## Guides

| Guide | Product / alias | Package folder |
|-------|-----------------|----------------|
| [CrimeStar](crimestar.md) | CrimeStar RMS (FoxPro / DBF) | `CrimeStar/` |
| [CopSync / Kologik](copsync-kologik.md) | COPsync / Kologik | `CopSync/` |
| [IncodeCourt (Tyler / INCODE)](incode-court.md) | Municipal court CTFILES / Access | `IncodeCourt/` |
| [Xpediter](xpediter.md) | XPEDITER GDB | `Xpediter/` |

**Converted agencies register:** each package includes `ConvertedAgencies.md` (agency, date, package `VERSION`).

---

## How to start an engagement

1. Confirm vendor on the [Legacy System Migration Assessment](../../../../../assessments/legacy-system-migration-assessment.md).
2. Open the vendor guide above + product `Utilities/Migration Tools/<Vendor>/` and note `VERSION`.
3. Follow `Utilities/Migration Tools/PROCESS.md` (copy → checklist → Overrides → promote).
4. Configure per [Customer Configuration Standard](../../migration-customer-configuration.md).
5. Validate per [Migration Validation Standard](../../migration-validation-standard.md).

Do **not** copy the last customer’s filled Overrides as the new default. Start from the vendor package templates.

---

## Cross-cutting migration docs

| Document | Role |
|----------|------|
| [Migration Philosophy](../../migration-philosophy.md) | Beliefs |
| [Migration Architecture](../../migration-architecture.md) | One-page flow |
| [Migration Decision Matrix](../../migration-decision-matrix.md) | Package vs config |
| [Migration Package Standards](../migration-package-standards.md) | Manifest · versioning · backlog |
| [Migration Metrics](../../migration-metrics.md) | Lightweight tracking |

---

## Known gaps

| Gap | Notes |
|-----|-------|
| Full Pipeline SQL still in some `Clients/.../Conversion/` folders | Promote common steps into vendor packages over time |
| Jail / JP CSV (e.g. Crosby County Jail) | Not a CopSync package; separate path <mark style="color:red;">**TODO**</mark> |
| Supported legacy version matrices | Incomplete — fill from each engagement into the vendor guide |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Placeholder index |
| 2026-07-17 | v1 catalog — CrimeStar, CopSync/Kologik, IncodeCourt, Xpediter |
| 2026-07-17 | Per-vendor guide pages + cross-links |
| 2026-07-17 | Moved under Data Migration → Vendor Packages |
