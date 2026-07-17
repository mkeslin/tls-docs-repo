# Infrastructure

**Phase:** Deliver  
**Document type:** Section index  

Provision and operate the agency **environment** (Azure, auth, Directory, apps). Business configuration is out of scope here — see [Configuration](../configuration.md) and [Bootstrap vs Configuration](bootstrap-vs-configuration.md).

## Primary SOP

| Doc | Status |
|-----|--------|
| [Bootstrap Environment](bootstrap-environment.md) | v1 — `bootstrap-client.ps1` |

## Standards & references

| Doc | Status |
|-----|--------|
| [Bootstrap Environment Standard](bootstrap-environment-standard.md) | v1 — naming, DNS, done criteria |
| [Environment Inventory Standard](environment-inventory-standard.md) | v1 — bill of materials |
| [Environment Lifecycle](environment-lifecycle.md) | v1 — request → destroy |
| [Environment Classification](environment-classification.md) | v1 — dev/test/prod/demo/training |
| [Baseline Database Standard](baseline-database-standard.md) | v1 — seed bacpac |
| [Bootstrap vs Configuration](bootstrap-vs-configuration.md) | v1 — boundary |
| [Hub Environment Integration](hub-environment-integration.md) | v1 draft |
| [Environment Health Checklist](../../../checklists/environment-health-checklist.md) | v1 |

## In the Deliver sequence

**Previous:** [Kickoff](../kickoff.md)  
**Next:** [Data Migration](../data-migration/README.md) (if in scope) or [Configuration](../configuration.md)
