# Data Migration

**Lifecycle step:** 3 · Data Migration  
**Milestone outcome:** Customer Data Migrated (or N/A)  
**Document type:** Phase overview  
**Status:** v1  

Engagement status: ☐ Not started · ☐ In progress · ☐ Complete · ☐ N/A (no historical migration)

CVE stage: [Data Migration](../../../customer-value-engine/deliver/data-migration.md)

This phase is **broader than “running conversion scripts.”** It includes assessment, pricing, vendor packages, execution, validation, acceptance, versioning, and package improvement.

---

## Purpose

Move agreed historical data from the customer’s legacy system into Thin Line, validate quality, and obtain acceptance—so the agency can use their history in production (or UAT, per plan).

---

## Inputs

| Input | Source |
|-------|--------|
| Infrastructure (or equivalent target DB) | [Infrastructure](../infrastructure/README.md) |
| Approved Conversion Plan | [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) |
| Vendor package + VERSION | [Vendor Packages](vendor-packages/README.md) |
| Legacy extract / access (after SaaS + CJIS) | Customer / vendor |
| Agency configuration for conversion (checklist / Overrides) | [Migration Overrides & Mapping Standard](migration-customer-configuration.md) |

---

## Activities

1. Assess and price (if not done).  
2. Acquire data; copy package → engagement folder; complete checklist / Overrides.  
3. Execute StagingImporter / Pipeline ([Legacy System Migration](legacy-system-migration.md)).  
4. Run [Post-Conversion Utilities](post-conversion-utilities.md).  
5. Validate per [Validation](migration-validation-standard.md); customer acceptance.  
6. Promote reusable fixes; register conversion; close package backlog items.  

---

## Outputs

| Output | Notes |
|--------|--------|
| Converted data in agreed environment | UAT and/or Production |
| Exception report | Accepted gaps documented |
| Customer acceptance | [Customer Acceptance](customer-acceptance.md) |
| Updated `ConvertedAgencies.md` + package VERSION | Package hygiene |
| Package backlog updates | Reusable improvements |

---

## Exit criteria

Milestone **Customer Data Migrated** when:

- [ ] In-scope modules meet [Migration Validation Standard](migration-validation-standard.md)  
- [ ] Required post-conversion utilities completed  
- [ ] Customer validation / acceptance recorded ([Customer Acceptance](customer-acceptance.md))  
- [ ] Material exceptions dispositioned (fixed / accepted / deferred)  
- [ ] Register / VERSION updated for accepted run  

If migration is out of scope: mark **N/A** and proceed to Configuration.

---

## Referenced SOPs / standards / checklists

| Doc | Type |
|-----|------|
| [Migration Philosophy](migration-philosophy.md) | Principles |
| [Legacy System Migration](legacy-system-migration.md) | SOP |
| [Vendor Packages](vendor-packages/README.md) | Standards + guides |
| [Migration Validation Standard](migration-validation-standard.md) | Standard |
| [Customer Acceptance](customer-acceptance.md) | Acceptance index |
| [Post-Conversion Utilities](post-conversion-utilities.md) | SOP |
| [Migration Architecture](migration-architecture.md) | Overview |
| [Migration Decision Matrix](migration-decision-matrix.md) | Reference |
| [Migration Overrides & Mapping Standard](migration-customer-configuration.md) | Standard |
| [Migration Metrics](migration-metrics.md) | Reference |
| [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) | Assessment |
| [Migration Pricing Policy](../../../policies/migration-pricing.md) | Policy |
| [Customer Validation Checklist](../../../checklists/customer-validation-checklist.md) | Checklist |

**Previous:** [Infrastructure](../infrastructure/README.md)  
**Next:** [Configuration](../configuration/README.md)
