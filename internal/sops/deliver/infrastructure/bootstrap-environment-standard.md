# Bootstrap Environment Standard

**Document type:** Standard  
**Status:** v1  
**Audience:** Implementation Â· Engineering  

Defines **what every Thin Line agency environment must look like** after bootstrap (and what names/URLs mean).

**How to execute:** [Bootstrap Environment SOP](bootstrap-environment.md) â€” bootstrap **according to this standard**.  
**Authoritative code:** product monorepo `Infrastructure/` (`main.bicep`, `TlsBicepResourceNames.ps1`, `environments/*.profile.json`).

Related: [Environment Inventory Standard](environment-inventory-standard.md) Â· [Environment Classification](environment-classification.md) Â· [Bootstrap vs Configuration](bootstrap-vs-configuration.md)

---

## Cloud and region

| Rule | Value |
|------|--------|
| Azure cloud | **Azure US Government** (`AzureUSGovernment`) |
| Supported script tiers | `dev` Â· `test` Â· `prod` (see [Environment Classification](environment-classification.md)) |
| Defaults | Per-tier `Infrastructure/environments/<tier>.profile.json` (`location`, subscription, RG, SQL server, Directory/Descope URLs) |
| Shared App Gateway | `environments/shared.profile.json` (`appGatewayResourceGroup`, `appGatewayName`) |

Do not invent a new region or subscription for a standard customer bootstrap without an explicit platform decision.

---

## Agency identity

| Concept | Rule | Example |
|---------|------|---------|
| **AgencyName** (slug) | Lowercase hostname-safe token; used in Azure names and DNS | `thinlinepd` |
| **FriendlyAgencyName** | Human display name; Descope tenant name / Directory Name | `Thin Line PD` |
| **Environment** | One of `dev` \| `test` \| `prod` | `prod` |

Slug is stable for the life of the environment. Renaming after go-live is a migration, not a parameter tweak.

---

## Resource naming

Prefix (must match `main.bicep` / `TlsBicepResourceNames.ps1`):

```text
tls-{AgencyName}-{Environment}
```

| Resource | Name pattern | Example (`thinlinepd` / `prod`) |
|----------|--------------|----------------------------------|
| SQL database | `{prefix}-rms` | `tls-thinlinepd-prod-rms` |
| API App Service | `{prefix}-api` | `tls-thinlinepd-prod-api` |
| UI App Service | `{prefix}-ui` | `tls-thinlinepd-prod-ui` |
| File share | `{prefix}-fileshare` | `tls-thinlinepd-prod-fileshare` |

| Shared (not per-agency) | Source |
|-------------------------|--------|
| SQL **server** | Profile `sqlServerNameDefault` (e.g. prod `tls-db2`, test `tls-test`) |
| Storage account | Profile `storageAccountNameDefault` |
| Elastic pool | Profile `elasticPoolNameDefault` (empty = skip pool move) |
| App Service Plan / RG | Profile `resourceGroup` (+ Bicep params) |
| Application Gateway | Shared profile |

If Bicep naming changes, update `TlsBicepResourceNames.ps1` in the **same** change.

---

## DNS / hostnames

Default hostname suffix: **`thinline.app`**

| Role | Hostname |
|------|----------|
| UI | `{AgencyName}.thinline.app` |
| API | `{AgencyName}-api.thinline.app` |

Test-tier Directory / auth hosts use test platform URLs from the **test** profile (e.g. `directory-api-test.thinline.app`, `auth-test.thinline.app`)â€”agency UI/API hostnames still follow the pattern above unless a profile/Directory override says otherwise.

App Gateway: HTTPS listeners + SNI for both hostnames (`04-update-app-gateway.ps1`). Optional `-SkipListeners` only when DNS is intentionally deferred.

---

## TLS certificates

| Rule | Today |
|------|--------|
| Customer hostnames | Terminated on **shared** Application Gateway (SNI) |
| Certificate ownership | Platform / shared gateway cert for `*.thinline.app` (and related) |
| Per-agency certs | Not created by bootstrap |

<mark style="color:red;">**TODO:**</mark> Link internal runbook for cert renewal / wildcard scope when documented elsewhere.

---

## Tags

| Rule | Today |
|------|--------|
| Required Azure tags on per-agency resources | <mark style="color:red;">**TODO:**</mark> Confirm whether Bicep applies standard tags (`Agency`, `Environment`, `ManagedBy`) â€” if not, add to platform backlog |

Until confirmed, do not assume tags exist for cost allocation.

---

## Directory and Descope

| Component | Convention |
|-----------|------------|
| Descope tenant | Named from **FriendlyAgencyName** (create-or-resolve) |
| Directory API config | Keyed by agency + environment; API/UI URLs prefer custom `*.thinline.app` hosts |
| Platform Directory / auth base URLs | From tier profile (`directoryApiUrlCustom`, `descopeBaseUrl`, project id) |

Secrets are **never** in profiles: use session env vars (`TLS_DESCOPE_*`, `TLS_DIRECTORY_API_*`, `TLS_SQL_*`, DevOps PAT). See Bootstrap SOP.

---

## Database seed

| Rule | Value |
|------|--------|
| Default bacpac | `Clients\_Base\Databases\_Base_ThinLineRMS.bacpac` |
| Post-import | Auth users SQL; agency name SQL when FriendlyAgencyName provided |
| Ownership of baseline | [Baseline Database Standard](baseline-database-standard.md) |

---

## Application version

| Rule | Value |
|------|--------|
| Deployed from | `-VersionBranch` (e.g. `release/x.y.z`) via Build + Deploy pipelines |
| Record | Engagement notes / future Hub Environment record |

---

## Definition of â€œbootstrap completeâ€

An environment meets this standard when:

1. Named resources exist per tables above  
2. Hostnames are on App Gateway (or deferral is documented)  
3. Database imported from an approved baseline  
4. Descope tenant + Directory config present  
5. Apps deployed for the chosen VersionBranch  
6. [Environment Health Checklist](../../../checklists/environment-health-checklist.md) passes  

**Bootstrap stops** at infrastructure + platform wiring. Agency business configuration is **not** part of this standard â€” see [Bootstrap vs Configuration](bootstrap-vs-configuration.md).

---

## Related documents

| Document | Role |
|----------|------|
| [Bootstrap Environment SOP](bootstrap-environment.md) | How to run scripts |
| [Environment Inventory Standard](environment-inventory-standard.md) | What an environment contains |
| [Environment Lifecycle](environment-lifecycle.md) | Request â†’ destroy |
| Product `Infrastructure/README.md` | Command detail |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 â€” naming, DNS, tiers, completion criteria |
