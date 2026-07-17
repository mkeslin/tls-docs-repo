# Data conversion

**Phase:** Deliver  
**Desired outcome:** Migrate historical data into Thin Line Platform

## Inputs

- Signed SaaS + CJIS (hard stop before legacy access)
- Legacy database or vendor export
- [Legacy System Migration Assessment](../../assessments/legacy-system-migration-assessment.md) ? Approved Conversion Plan
- Vendor Migration Package (when available)

## Outputs

- Converted database (UAT and/or Production)
- Engagement conversion folder artifacts
- Customer validation / acceptance
- Updated vendor `ConvertedAgencies.md` (package VERSION)

## Owner

Implementation Lead *(current incumbent: Matthew Keslin)*

## Current process

1. Assess and price per SOP / policy  
2. Acquire data (on-prem extract or cloud vendor export)  
3. Copy vendor package ? client engagement folder; complete AgencyChecklist; fill Overrides  
4. Execute Pipeline / StagingImporter; run post-conversion utilities  
5. Customer validates; promote reusable fixes; register conversion  

**SOP:** [Legacy System Migration](../../sops/deliver/legacy-system-migration.md)  
**Package standards:** [Migration Package Standards](../../sops/deliver/migration-package-standards.md)  
**Vendor index:** [Vendor Conversion Guides](../../sops/deliver/vendor-conversion-guides/README.md)

## Tooling

| Tool | Role |
|------|------|
| Product Git `Utilities/Migration Tools/` | Vendor packages, PROCESS.md, VERSION |
| `Clients/.../Conversion/` (+ Team Drive) | Engagement working copy |
| SQL Server | Load / transform / verify |
| Cursor | Lead PROCESS.md execution |

## Capacity (today)

2–4 / mo *(planning estimate — TODO: measure)*

## Cycle time

Typically 1–10 business days excluding customer/vendor wait states (see SOP time expectations).

## Maturity

**2–3 / 5 — Documented / standardizing**

| Score | Meaning |
|------:|---------|
| 1 | Founder-driven |
| 2 | Documented |
| 3 | Standardized |
| 4 | Automated |
| 5 | Scalable |

Vendor packages and checklists exist; validation/close and consistent assessment adoption still maturing.

## What would break first?

- New / unsupported vendor with no package  
- Agency Overrides skipped or agency hardcodes merged into shared templates  
- Access before SaaS + CJIS  

## Continuous improvement (10x ideas)

| Lens | Idea |
|------|------|
| Reduce / Simplify | Fewer one-off client script forks; promote into packages |
| Standardize | AgencyChecklist + Override templates for every vendor |
| Automate | Schema compare + converter registry |
| Delegate | Implementation specialists run standard packages via PROCESS.md |
| Scale | Customer validation portal |

## Product responsibility

**TODO / Decision needed:** Supported Vendor Catalog and Migration Registry (see SOP product impact).

## Related documents

- [Legacy System Migration SOP](../../sops/deliver/legacy-system-migration.md)
- [Migration Package Standards](../../sops/deliver/migration-package-standards.md)
- [Vendor Conversion Guides](../../sops/deliver/vendor-conversion-guides/README.md)
- [Legacy System Migration Assessment](../../assessments/legacy-system-migration-assessment.md)
- [Customer Validation Checklist](../../checklists/customer-validation-checklist.md)
- [Migration Close-Out Checklist](../../checklists/migration-close-out-checklist.md)
