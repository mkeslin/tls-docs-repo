# Bootstrap environment

**Phase:** Deliver  
**Desired outcome:** Provision agency tenant (Azure + auth + Directory + apps) to the Bootstrap Environment Standard

## Inputs

- Agency slug (`AgencyName`) and display name (`FriendlyAgencyName`)
- Environment tier: `dev` | `test` | `prod` ([classification](../../sops/deliver/infrastructure/environment-classification.md))
- Release / version branch (e.g. `release/6.1.0`)
- Session secrets (SQL, Descope, DevOps PAT, Directory API as required)
- Approved baseline bacpac ([Baseline Database Standard](../../sops/deliver/infrastructure/baseline-database-standard.md))

## Outputs

- Environment matching [inventory](../../sops/deliver/infrastructure/environment-inventory-standard.md) + [naming standard](../../sops/deliver/infrastructure/bootstrap-environment-standard.md)
- Passed [Environment Health Checklist](../../checklists/environment-health-checklist.md)
- Ready for **Configuration** (not done by bootstrap) â€” [boundary](../../sops/deliver/infrastructure/bootstrap-vs-configuration.md)

## Owner

Keslin (Implementation Lead)

## Current process

1. Confirm parameters against Bootstrap Environment Standard  
2. Azure US Government login; set secrets  
3. Run `Infrastructure/scripts/bootstrap-client.ps1` (Infra â†’ Database â†’ AppGateway â†’ DescopeTenant â†’ DirectoryConfig â†’ Build â†’ Deploy)  
4. Complete Environment Health Checklist  
5. Hand off to Configuration â†’ (optional Migration) per [Environment Lifecycle](../../sops/deliver/infrastructure/environment-lifecycle.md)

**SOP:** [Bootstrap Environment](../../sops/deliver/infrastructure/bootstrap-environment.md)

## Tooling

- Product repo `Infrastructure/scripts/` + `environments/*.profile.json`
- Azure CLI (US Government), SqlPackage, Azure DevOps PAT
- Descope Â· Directory API

## Capacity (today)

4â€“8/mo

## Cycle time

30â€“60 min (full bootstrap; excludes DNS / customer wait)

## Maturity

**3 / 5 â€” Standardized**

## What would break first?

Missing secrets Â· wrong AgencyName/Environment Â· SqlPackage/Directory unreachable Â· treating configuration as part of bootstrap

## Continuous improvement (10x ideas)

| Lens | Idea |
|------|------|
| Standardize | Bootstrap Environment Standard + health checklist (done) |
| Automate | Hub Environment record + probes ([Hub integration](../../sops/deliver/infrastructure/hub-environment-integration.md)) |
| Delegate | Specialists run SOP + Standard without founder |

## Product responsibility

Hub Environment as system of record â€” see [Hub Environment Integration](../../sops/deliver/infrastructure/hub-environment-integration.md).

## Related documents

- [Bootstrap Environment SOP](../../sops/deliver/infrastructure/bootstrap-environment.md)
- [Bootstrap Environment Standard](../../sops/deliver/infrastructure/bootstrap-environment-standard.md)
- [Environment Inventory Standard](../../sops/deliver/infrastructure/environment-inventory-standard.md)
- [Environment Lifecycle](../../sops/deliver/infrastructure/environment-lifecycle.md)
- [Bootstrap vs Configuration](../../sops/deliver/infrastructure/bootstrap-vs-configuration.md)
- [Environment Health Checklist](../../checklists/environment-health-checklist.md)
- [Legacy System Migration](../../sops/deliver/data-migration/legacy-system-migration.md)
