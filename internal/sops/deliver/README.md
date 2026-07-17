# SOPs — Deliver

SOPs for data conversion through go-live. Stage overviews: [Customer Value Engine — Deliver](../../customer-value-engine/deliver/README.md).

## Before you execute

| Assessment | Status |
|------------|--------|
| [Legacy System Migration Assessment](../../assessments/legacy-system-migration-assessment.md) | v1 form — required before migration work / quoting |
| [Implementation Readiness Assessment](../../assessments/implementation-readiness-assessment.md) | <mark style="color:red;">Placeholder</mark> |
| [Go-Live Readiness Assessment](../../assessments/go-live-readiness-assessment.md) | <mark style="color:red;">Placeholder</mark> |

See [Assessments](../../assessments/README.md).

## Procedures in this folder

| SOP | Status |
|-----|--------|
| [Legacy System Migration](legacy-system-migration.md) | v1 model SOP (aligned with Migration Tools) |
| [Customer Onboarding](customer-onboarding.md) | <mark style="color:red;">Placeholder</mark> |
| [Bootstrap Environment](bootstrap-environment.md) | v1 — Infrastructure PowerShell (`bootstrap-client.ps1`) |
| [Post-Conversion Utilities](post-conversion-utilities.md) | v1 — Admin Data Utilities (workflow + call snapshot) |

## Bootstrap / environment domain (standards)

| Document | Status |
|----------|--------|
| [Bootstrap Environment Standard](bootstrap-environment-standard.md) | v1 — naming, DNS, completion criteria |
| [Environment Inventory Standard](environment-inventory-standard.md) | v1 — bill of materials |
| [Environment Lifecycle](environment-lifecycle.md) | v1 — request ? destroy |
| [Environment Classification](environment-classification.md) | v1 — dev/test/prod/demo/training |
| [Baseline Database Standard](baseline-database-standard.md) | v1 — seed bacpac |
| [Bootstrap vs Configuration](bootstrap-vs-configuration.md) | v1 — boundary |
| [Hub Environment Integration](hub-environment-integration.md) | v1 draft — future Hub |
| [Environment Health Checklist](../../checklists/environment-health-checklist.md) | v1 |

## Migration domain (standards & guides)

| Document | Status |
|----------|--------|
| [Migration Philosophy](migration-philosophy.md) | v1 — principles |
| [Migration Architecture](migration-architecture.md) | v1 — one-page flow |
| [Migration Decision Matrix](migration-decision-matrix.md) | v1 |
| [Migration Package Standards](migration-package-standards.md) | v1 — manifest · versioning · backlog |
| [Customer Configuration Standard](migration-customer-configuration.md) | v1 |
| [Migration Validation Standard](migration-validation-standard.md) | v1 |
| [Migration Metrics](migration-metrics.md) | v1 — lightweight |
| [Vendor Conversion Guides](vendor-conversion-guides/README.md) | v1 — catalog + per-vendor guides |

## Suggested next SOPs

- Implementation workspace / end-to-end implementation (Contract ? Go-live ? Support)
- `go-live.md`
- `deliver-training.md`
