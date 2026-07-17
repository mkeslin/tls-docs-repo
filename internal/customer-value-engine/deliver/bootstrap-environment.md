# Bootstrap environment

**Phase:** Deliver  
**Desired outcome:** Provision agency tenant (Azure + auth + Directory + apps)

## Inputs

- Agency slug (`AgencyName`) and display name (`FriendlyAgencyName`)
- Environment tier: `dev` | `test` | `prod`
- Release / version branch (e.g. `release/6.1.0`)
- Session secrets (SQL, Descope, DevOps PAT, Directory API as required)

## Outputs

- Live tenant: SQL DB, API/UI apps, App Gateway hostnames, Descope tenant, Directory config, deployed build

## Owner

Keslin (Implementation Lead)

## Current process

Orchestrated PowerShell from the product monorepo:

1. Azure US Government login (`az cloud set` / `az login`)
2. Set required env vars (`TLS_SQL_*`, `TLS_DESCOPE_*`, `TLS_DEVOPS_PAT`, Directory overrides as needed)
3. Run `Infrastructure/scripts/bootstrap-client.ps1` with `-Environment`, `-AgencyName`, `-FriendlyAgencyName`, `-VersionBranch` (default Steps: Infra → Database → AppGateway → DescopeTenant → DirectoryConfig → Build → Deploy)
4. Verify URLs and smoke login
5. Proceed to configuration / training / [Legacy System Migration](../../sops/deliver/legacy-system-migration.md) when historical data is in scope

Partial re-runs use `-Steps`. Teardown: `teardown-client.ps1`.

## Tooling

- Product repo `Infrastructure/scripts/` (`bootstrap-client.ps1`, `01`–`07`, profiles under `environments/`)
- Azure CLI (US Government), SqlPackage, Azure DevOps PAT for Build/Deploy
- Descope management API · Directory API

## Capacity (today)

4–8/mo

## Cycle time

30–60 min (full bootstrap; excludes DNS / customer wait)

## Maturity

**3 / 5 — Standardized**

| Score | Meaning |
|------:|---------|
| 1 | Founder-driven |
| 2 | Documented |
| 3 | Standardized |
| 4 | Automated |
| 5 | Scalable |

## What would break first?

Missing secrets / PAT · wrong AgencyName or Environment · SqlPackage or Directory API unreachable · Deploy without BuildId

## Continuous improvement (10x ideas)

| Lens | Idea |
|------|------|
| Reduce / Simplify | Fewer manual secret steps |
| Standardize | Profiles + this SOP (done for orchestration) |
| Automate | OIDC / service principal; post-bootstrap smoke script |
| Delegate | Implementation specialists run from SOP alone |
| Scale | Hub-triggered tenant provision with prod approval gates |

## Product responsibility

<mark style="color:red;">**TODO / Decision needed:**</mark> Not yet assigned in the source Customer Value Engine worksheet.

## Related documents

- **SOP (executable procedure):** [Bootstrap Environment](../../sops/deliver/bootstrap-environment.md)
- Product monorepo: `Infrastructure/README.md`
- [Legacy System Migration](../../sops/deliver/legacy-system-migration.md) — data after/with environment
- [Customer Onboarding](../../sops/deliver/customer-onboarding.md)
