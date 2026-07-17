# Infrastructure

**Lifecycle step:** 2 · Infrastructure  
**Milestone outcome:** Infrastructure Ready  
**Document type:** Phase overview  
**Status:** v1  

Engagement status: ☐ Not started · ☐ In progress · ☐ Complete

CVE stage: [Infrastructure](../../../customer-value-engine/deliver/infrastructure.md)

---

## Purpose

Provision a working Thin Line **environment** for the agency so apps, auth, Directory, and database seed exist and pass health checks. This phase ends when the platform is usable for configuration—not when the agency is fully configured.

---

## Inputs

| Input | Source |
|-------|--------|
| AgencyName (slug) + FriendlyAgencyName | Kickoff |
| Environment tier (`dev` / `test` / `prod`) | Kickoff / [Classification](environment-classification.md) |
| VersionBranch | Kickoff / release plan |
| Secrets / PAT / Azure access | Implementation |
| Baseline bacpac | [Baseline Database Standard](baseline-database-standard.md) |

---

## Activities

1. Confirm parameters against [Bootstrap Environment Standard](bootstrap-environment-standard.md).  
2. Run bootstrap per [Bootstrap Environment SOP](bootstrap-environment.md) (`bootstrap-client.ps1`).  
3. Complete [Environment Health Checklist](../../../checklists/environment-health-checklist.md).  
4. Hand off to Configuration (and/or Data Migration if in scope).  

---

## Outputs

| Output | Notes |
|--------|--------|
| Azure apps + SQL DB + file share | Per inventory / naming standard |
| Descope tenant + Directory config | Platform wiring |
| App Gateway hostnames | Or documented deferral |
| Deployed VersionBranch | Build/Deploy |
| Passed health checklist | Required |

---

## Exit criteria

Milestone **Infrastructure Ready** when:

- [ ] Environment matches [Bootstrap Environment Standard](bootstrap-environment-standard.md)  
- [ ] [Environment Health Checklist](../../../checklists/environment-health-checklist.md) passes  
- [ ] Agency business configuration has **not** been mistaken for bootstrap completion ([Bootstrap vs Configuration](bootstrap-vs-configuration.md))  

---

## Referenced SOPs / standards / checklists

| Doc | Type |
|-----|------|
| [Bootstrap Environment](bootstrap-environment.md) | SOP |
| [Bootstrap Environment Standard](bootstrap-environment-standard.md) | Standard |
| [Environment Inventory Standard](environment-inventory-standard.md) | Standard |
| [Environment Lifecycle](environment-lifecycle.md) | Reference |
| [Environment Classification](environment-classification.md) | Reference |
| [Baseline Database Standard](baseline-database-standard.md) | Standard |
| [Bootstrap vs Configuration](bootstrap-vs-configuration.md) | Reference |
| [Hub Environment Integration](hub-environment-integration.md) | Future |
| [Environment Health Checklist](../../../checklists/environment-health-checklist.md) | Checklist |

**Previous:** [Kickoff and discovery](../kickoff-and-discovery.md)  
**Next:** [Data migration](../data-migration/README.md) (if in scope) or [Configuration](../configuration/README.md)
