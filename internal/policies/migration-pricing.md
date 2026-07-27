# Migration Pricing Policy

**Phase:** Deliver  
**Document Type:** Policy  
**Status:** <mark style="color:red;">Draft</mark> 
**Owner:** Matthew Keslin

> <mark style="color:red;">**Decision needed:**</mark> Founder / commercial approval before this draft is used as binding quote guidance with customers.  
> **Working commercial rates (2026-07):** migration-type fee table below matches [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md) — keep both docs aligned when amounts change.

---

## Purpose

This policy establishes how Thin Line Software prices legacy system migration services.

The objectives are to:

- Recover the cost of migration work.
- Set consistent customer expectations.
- Reduce founder-only pricing decisions.
- Encourage standardization and reusable migration tooling.
- Ensure migration pricing reflects the complexity and value of the work performed.

---

## Guiding Principles

### Migration is a Professional Service

Data migration is not included as part of the recurring software subscription.

Migration is a one-time professional service that requires planning, engineering, validation, and customer coordination.

---

### Simplicity

Pricing should be easy for customers and sales staff to understand.

Avoid quoting based solely on estimated engineering hours whenever possible.

---

### Reward Standardization

Customers migrating from systems with established Thin Line Migration Packages should generally receive lower pricing than customers requiring custom engineering.

---

### Encourage Long-Term Partnerships

Thin Line may choose to discount or waive migration fees when justified by:

- Multi-year SaaS agreements
- Strategic customer value
- Reference opportunities
- Product development value
- Executive approval

These decisions should be documented.

---

## Policy

Every customer requesting historical data migration must complete a **[Legacy System Migration Assessment](../assessments/legacy-system-migration-assessment.md)** before pricing is finalized.

No migration quote should be provided until the assessment is complete.

---

## Migration Pricing Factors

Migration pricing should consider:

- Legacy vendor
- Vendor version
- Existing Migration Package availability
- Hosting model (Cloud vs On-Premises)
- Number of modules
- Data volume
- Data quality
- Required engineering effort
- Customer timeline
- Validation requirements

---

## Pricing Tiers

Canonical one-time fees (also in [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md)):

| Migration type | One-time fee |
|----------------|-------------:|
| Customer-completed template import | $2,500 |
| Simple structured migration | $5,000–$7,500 |
| Standard legacy-system migration | $10,000–$15,000 |
| Complex records and attachments | $15,000–$30,000 |
| Multiple source systems | Custom |

### Customer-completed template import — $2,500

Typical characteristics:

- Customer fills Thin Line import templates
- Thin Line validates and loads
- Minimal mapping / engineering
- Good data quality

---

### Simple structured migration — $5,000–$7,500

Typical characteristics:

- Small agency
- Supported vendor or clean structured export
- Existing or light Migration Package work
- Minimal customization
- Good data quality

---

### Standard legacy-system migration — $10,000–$15,000

Typical characteristics:

- Supported legacy vendor
- Established or moderate Migration Package effort
- Multiple modules and/or moderate volume
- Normal validation and customer coordination

---

### Complex records and attachments — $15,000–$30,000

Typical characteristics:

- Large attachment volumes or complex record shapes
- Significant data volume / quality issues
- Custom mappings and extensive validation
- High engineering and coordination effort

---

### Multiple source systems — Custom

Applies when:

- More than one source system / vendor to consolidate
- No existing Migration Package and significant new tooling
- Unsupported vendor with custom engineering
- Scope cannot be reasonably categorized in the rows above

Pricing:

Prepared as a custom professional services estimate (founder / deal desk).

---

## Pricing Adjustments

The following may justify adjustments.

### Increase

- Unsupported vendor
- Poor data quality
- Large attachment volumes
- Aggressive timeline
- Customer-requested custom transformations
- Multiple conversion iterations

---

### Decrease

- Existing Migration Package
- Small data volume
- Strategic customer
- Product development opportunity
- Multi-year agreement
- Executive-approved promotion

---

## Included Services

Unless otherwise specified, migration pricing includes:

- Migration assessment
- Legacy data extraction guidance
- Data mapping
- Standard transformations
- Data import
- Standard post-conversion utilities
- Customer validation support
- Reasonable post-migration corrections

---

## Excluded Services

Unless specifically quoted:

- Extensive manual data cleanup
- Custom reporting
- Customer training
- Additional conversion iterations caused by changing customer requirements
- Development unrelated to migration

---

## Reusable Engineering

Whenever engineering work creates reusable value, the resulting improvements must be incorporated into the appropriate Migration Package.

Examples:

- Improved mappings
- Bug fixes
- Additional supported tables
- Better validation
- New utilities

Customer-funded migration work should improve future migrations whenever practical.

See [Migration Package Standards](../sops/deliver/data-migration/vendor-packages/migration-package-standards.md).

---

## Approval Authority

| Migration type | Approval |
|----------------|----------|
| Customer-completed template import | Acquire (after assessment) |
| Simple structured migration | Acquire (after assessment) |
| Standard legacy-system migration | Acquire (after assessment) |
| Complex records and attachments | Acquire with caution; founder if scope is unclear |
| Multiple source systems / custom estimate | Founder / deal desk |
| $0 waiver or heavy discount (show full fee → net) | Founder / deal desk |

Aligns with [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md).

---

## Discounts

Discounts should be documented. On the proposal, show **full fee → incentive → net** (same pattern as implementation in the SaaS guardrails) — do not quote only $0.

Examples include:

- Multi-year SaaS agreement
- Strategic market opportunity
- Beta customer
- Product partnership
- Reference customer

The reason for the discount should be recorded in the [Legacy System Migration Assessment](../assessments/legacy-system-migration-assessment.md).

---

## Customer Communication

Migration pricing should be presented as:

> A one-time professional service that ensures historical data is successfully migrated into Thin Line Platform.

Avoid describing migration as "copying data."

Emphasize that migration includes:

- Assessment
- Engineering
- Validation
- Workflow transition
- Customer review
- Quality assurance

---

## Future State

Long-term, migration pricing should become increasingly standardized as Thin Line expands its library of Migration Packages.

Goals include:

- Faster assessments
- Predictable pricing
- Reduced engineering effort
- Higher reuse
- Shorter implementation timelines

---

## Related Documents

| Document | Relationship |
|----------|--------------|
| [Legacy System Migration SOP](../sops/deliver/data-migration/legacy-system-migration.md) | Execution procedure |
| [Legacy System Migration Assessment](../assessments/legacy-system-migration-assessment.md) | Required before pricing; records tier, fee, discounts |
| [Migration Philosophy](../sops/deliver/data-migration/migration-philosophy.md) | Price outcomes, not open-ended hours |
| [Migration Architecture](../sops/deliver/data-migration/migration-architecture.md) | Assessment → pricing → package flow |
| [Migration Package Standards](../sops/deliver/data-migration/vendor-packages/migration-package-standards.md) | Vendor package VERSION / reuse (affects effort tier) |
| [Vendor Conversion Guides](../sops/deliver/data-migration/vendor-packages/vendor-conversion-guides/README.md) | Supported vendor catalog |
| [Kickoff and Discovery](../sops/deliver/kickoff-and-discovery.md) | Implementation discovery |
| [Data Migration](../sops/deliver/data-migration/README.md) | Migration phase |
| [Business Systems Architecture](../operating-system/business-systems-architecture.md) | Systems of record context |

---

## Review

This policy should be reviewed:

- Annually
- Whenever pricing changes
- Whenever a new Migration Package significantly changes implementation effort

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-07-17 | Initial draft | Thin Line OS |
