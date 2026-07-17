# Customer Configuration Standard

**Document type:** Standard  
**Status:** v1  

Philosophy: [Migration Philosophy](migration-philosophy.md) — **Package + Configuration = Migration**.

---

## Equation

```text
Vendor Migration Package
        +
Customer configuration (this engagement)
        =
Runnable migration for that agency
```

| Layer | Contains | Must not contain |
|-------|----------|------------------|
| **Package** | Common Pipeline, StagingImporter, Override **templates**, AgencyChecklist questions, `VERSION` | Agency names, phones, ORIs, one-off key fixes, customer email domains |
| **Configuration** | Filled checklist answers, filled Overrides, engagement parameters (DB names, TargetAgencyId) | “New default” logic that belongs in the shared package |

---

## What counts as configuration

| Configuration | Typical home |
|---------------|--------------|
| Modules in / out of scope | Filled `AgencyChecklist.md` |
| Staging / ConvTemp / target DB names | Checklist + client PARAMETERS / script params |
| TargetAgencyId / agency seed | Overrides / ensure-agency scripts in **client** copy |
| Officer identity maps | Client Overrides |
| Court / agency maps | Client Overrides |
| Duplicate-key or one-off remediations | Client Overrides |
| Number patterns, email domain, hist prefixes | Checklist → Overrides |

---

## What is not configuration

| Change | Belongs in |
|--------|------------|
| Shared transform bug fix | Package (promote + bump `VERSION`) |
| New common Pipeline step | Package |
| New checklist **question** (reusable) | Vendor `AgencyChecklist.md` |
| New Override **template** shape | Package `Overrides/*.TEMPLATE` |

See [Migration Decision Matrix](migration-decision-matrix.md).

---

## Engagement layout (canonical)

```text
Clients/<Client>/Conversion/<Engagement>/
  AgencyChecklist.md     ← filled configuration decisions
  Overrides/             ← filled from package templates
  (working Pipeline copy)
```

Start from package templates every time. **Do not** copy the previous customer's filled Overrides as the new baseline.

Authoritative process: product-repo `Utilities/Migration Tools/PROCESS.md`.

---

## Future tooling

Hub may eventually store configuration as structured data (answers + maps) and render Overrides. Until then, checklist + SQL Overrides **are** the configuration standard.

---

## Related documents

| Document | Role |
|----------|------|
| [Migration Package Standards](vendor-packages/migration-package-standards.md) | Package side of the equation |
| [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md) | Per-vendor checklist / extract notes |
| [Legacy System Migration](legacy-system-migration.md) | SOP execution |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — package + configuration model |
