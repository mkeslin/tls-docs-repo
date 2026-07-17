# Migration Philosophy

**Document type:** Principles  
**Status:** v1  
**Audience:** Everyone who assesses, prices, executes, or improves migrations

This is **not** a procedure. For how to run a conversion, see [Legacy System Migration](legacy-system-migration.md). For the mental model, see [Migration Architecture](migration-architecture.md).

---

## Why this exists

Migrations fail when people treat every customer as a one-off engineering project. Thin Line treats migration as a **product capability**: reusable packages, explicit configuration, validation before acceptance, and continuous improvement of the package—not just the customer folder.

---

## Beliefs

1. **We build reusable migration packages.**  
   Vendor-specific knowledge belongs in a versioned package under `Utilities/Migration Tools/<Vendor>/`, not only in someone's head or a single client tree.

2. **Customer-specific behavior should be configuration.**  
   Agency names, ORIs, officer maps, court maps, and one-off key fixes live in the engagement folder (checklist + Overrides). They do not belong in shared Pipeline scripts.

3. **Package + configuration = migration.**  
   Execution is: take the package, apply this customer's configuration, run, validate. See [Migration Overrides & Mapping Standard](migration-customer-configuration.md).

4. **Every migration should improve the package.**  
   If the next agency would need the same fix, promote it and bump `VERSION`. Customer notes stay in the client folder; package backlog items are reusable improvements. See [Migration Package Standards](migration-package-standards.md#package-backlog).

5. **We validate before acceptance.**  
   Success is defined by the [Migration Validation Standard](migration-validation-standard.md), not by “the scripts finished.”

6. **We price outcomes, not engineering hours.**  
   Assessment and [Migration Pricing Policy](../../../policies/migration-pricing.md) quote conversion outcomes and risk—not an open-ended time-and-materials dump of tribal debugging.

7. **We minimize manual intervention.**  
   Prefer checklist-driven Overrides and Admin utilities over ad-hoc SQL. Automate after the process is documented and stable.

8. **We document before we automate.**  
   Hub / registry features come after the package model, validation standard, and vendor guides are clear enough to encode.

---

## What this implies in practice

| Situation | Do this |
|-----------|---------|
| Fix only this agency needs | Client `Overrides/` |
| Fix the next CrimeStar agency will need | Promote into package; bump `VERSION` |
| Unsupported vendor | Assess build-vs-decline; new package if we proceed |
| “Just copy the last customer's scripts” | No — start from package templates |
| Scripts ran green | Still run validation + customer acceptance |

---

## Related documents

| Document | Role |
|----------|------|
| [Migration Architecture](migration-architecture.md) | One-page flow |
| [Migration Decision Matrix](migration-decision-matrix.md) | Where work belongs |
| [Migration Package Standards](vendor-packages/migration-package-standards.md) | Package definition |
| [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md) | Vendor knowledge homes |
| [Legacy System Migration](legacy-system-migration.md) | Executable SOP |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — principles for reusable packages and configuration |
