# Data Migration

**Phase:** Deliver · lifecycle 3  
**Desired outcome:** Customer Data Migrated (historical data in Thin Line, validated and accepted) — or N/A

> **Naming:** Historically “Data conversion.” The implementation phase is **[Data Migration](../../sops/deliver/data-migration/README.md)**—broader than running scripts (assessment, packages, validation, acceptance, versioning).

## Inputs

- Signed SaaS + CJIS (hard stop before legacy access)
- Legacy database or vendor export
- [Legacy System Migration Assessment](../../assessments/legacy-system-migration-assessment.md) — Approved Conversion Plan
- Vendor Migration Package (when available)
- Infrastructure Ready (or equivalent target)

## Outputs

- Converted database (UAT and/or Production)
- Engagement conversion folder artifacts
- Customer validation / acceptance
- Updated vendor `ConvertedAgencies.md` (package VERSION)
- Package backlog / VERSION bumps when reusable improvements ship

## Owner

Implementation Lead *(current incumbent: Matthew Keslin)*

## Current process

1. Assess and price per SOP / policy  
2. Acquire data (on-prem extract or cloud vendor export)  
3. Copy vendor package → client engagement folder; complete AgencyChecklist; fill Overrides  
4. Execute Pipeline / StagingImporter; run post-conversion utilities  
5. Validate; customer accepts; promote reusable fixes; register conversion  

**Phase overview:** [Data Migration](../../sops/deliver/data-migration/README.md)  
**SOP:** [Legacy System Migration](../../sops/deliver/data-migration/legacy-system-migration.md)  
**Package standards:** [Migration Package Standards](../../sops/deliver/data-migration/vendor-packages/migration-package-standards.md)  
**Vendor guides:** [Vendor Conversion Guides](../../sops/deliver/data-migration/vendor-packages/vendor-conversion-guides/README.md)  
**Validation:** [Migration Validation Standard](../../sops/deliver/data-migration/migration-validation-standard.md)

## Tooling

| Tool | Role |
|------|------|
| Product Git `Utilities/Migration Tools/` | Vendor packages, PROCESS.md, VERSION |
| `Clients/.../Conversion/` (+ Team Drive) | Engagement working copy (configuration) |
| SQL Server | Load / transform / verify |
| Cursor | Lead PROCESS.md execution |

## Capacity (today)

2–4 / mo *(planning estimate — <mark style="color:red;">**TODO:**</mark> measure)*

## Cycle time

Typically 1–10 business days excluding customer/vendor wait states (see SOP time expectations).

## Maturity

**3 / 5 — Standardized (docs + packages; metrics/automation still light)**

## What would break first?

- New / unsupported vendor with no package  
- Agency Overrides skipped or agency hardcodes merged into shared templates  
- Access before SaaS + CJIS  
- Skipping validation (scripts-green ≠ success)

## Related documents

- [Data Migration (phase overview)](../../sops/deliver/data-migration/README.md)
- [Implementation Methodology](../../sops/deliver/implementation-methodology.md)
- [Legacy System Migration SOP](../../sops/deliver/data-migration/legacy-system-migration.md)
- [Legacy System Migration Assessment](../../assessments/legacy-system-migration-assessment.md)
