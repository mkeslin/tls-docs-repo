# Implementation workspace standard

**Phase:** Deliver  
**Document type:** Standard  
**Status:** v1  

Defines where engagement work lives (folders, naming, artifacts) so Implementation does not reinvent layout per customer.

---

## Purpose

Keep **shared product assets** separate from **customer-specific work**, and keep environment identity consistent with bootstrap naming.

---

## Product vs engagement

| Layer | Location (product monorepo unless noted) | Contains |
|-------|------------------------------------------|----------|
| **Shared packages / scripts** | `Utilities/Migration Tools/<Vendor>/` | Vendor Pipeline, StagingImporter, Override **templates**, `AgencyChecklist.md` questions, `VERSION` |
| **Infrastructure automation** | `Infrastructure/scripts/`, `environments/*.profile.json` | Bootstrap / teardown |
| **Customer engagement** | `Clients/<Client>/Conversion/<Engagement>/` (+ Team Drive as used) | Filled checklist, filled Overrides, extracts, working notes |
| **Docs (this repo)** | `internal/sops/deliver/` | Methodology, phase SOPs, standards |

Never leave agency-specific hardcodes in shared vendor packages. Promote reusable fixes and bump package `VERSION` — see [Migration Overrides & Mapping Standard](data-migration/migration-customer-configuration.md).

---

## Environment identity

Use bootstrap identity for every environment in the engagement:

| Concept | Rule | Example |
|---------|------|---------|
| **AgencyName** (slug) | Lowercase hostname-safe token | `thinlinepd` |
| **FriendlyAgencyName** | Human display name | `Thin Line PD` |
| **Environment** | `dev` \| `test` \| `prod` | `prod` |

Full naming and Azure layout: [Bootstrap Environment Standard](infrastructure/bootstrap-environment-standard.md).

---

## Migration engagement layout

```text
Clients/<Client>/Conversion/<Engagement>/
  AgencyChecklist.md     ← filled configuration decisions
  Overrides/             ← filled from package templates
  (working Pipeline copy / extracts as needed)
```

- Start from package templates every time.  
- Do **not** copy the previous customer’s filled Overrides as the new baseline.  
- Authoritative process: product-repo `Utilities/Migration Tools/PROCESS.md`.  

Detail: [Migration Overrides & Mapping Standard](data-migration/migration-customer-configuration.md) · [Migration Package Standards](data-migration/vendor-packages/migration-package-standards.md).

---

## Documentation artifacts (GitBook)

| Artifact | Typical home |
|----------|--------------|
| Phase exit / board | Engagement notes + Hub (future) |
| Sales handoff packet | [Sales handoff checklist](../../checklists/sales-handoff-checklist.md) |
| Environment health | [Environment health checklist](../../checklists/environment-health-checklist.md) |
| Agency configuration | [Agency configuration checklist](../../checklists/agency-configuration-checklist.md) |
| Migration acceptance | [Customer acceptance](data-migration/customer-acceptance.md) · templates |

---

## Out of scope for this standard

- Agency **business** configuration in the product (ORI, officers, modules) — [Configuration](configuration/README.md)  
- Platform Hub Environment object design — [Hub Environment Integration](infrastructure/hub-environment-integration.md)  

---

## Related

| Document | Role |
|----------|------|
| [Implementation overview](implementation-overview.md) | Parent |
| [Bootstrap Environment Standard](infrastructure/bootstrap-environment-standard.md) | Azure / URL naming |
| [Roles and responsibilities](roles-and-responsibilities.md) | Who owns the workspace |
