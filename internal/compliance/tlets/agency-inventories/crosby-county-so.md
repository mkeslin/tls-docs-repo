# Crosby County SO (`crosbytx`) — Azure inventory

> Moved from TLS-App `Docs/TLETS/agencies/crosby-county-so/azure-inventory.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Purpose:** Vol 03 appendix for Crosby County SO TLETS attestation kit. Resource names from **`az` CLI** (Azure Government, subscription **TLS Azure Subscription 1**).

**Last refreshed:** 2026-07-06

**⚠ Sensitive:** Do not ship connection strings, keys, or credentials. Verify in MFA-restricted portals for assessors.

---

## Resource naming (Thin Line-hosted RMS)

### Subscription & cloud

| Item | Value |
|------|--------|
| Subscription | TLS Azure Subscription 1 |
| Azure cloud | **Azure Government** |
| Resource group | `tls` |
| SQL logical server | `tls-db2` (`tls-db2.database.usgovcloudapi.net`) |

### App Services & database

| Azure resource name | Type | Region |
|---------------------|------|--------|
| `tls-crosbytx-prod-api` | App Service | USGov Texas |
| `tls-crosbytx-prod-ui` | App Service | USGov Texas |
| `tls-crosbytx-prod-rms` | SQL Database (on `tls-db2`) | USGov Texas |

Default hostnames:

| App | Hostname |
|-----|----------|
| API | `tls-crosbytx-prod-api.azurewebsites.us` |
| UI | `tls-crosbytx-prod-ui.azurewebsites.us` |

### Published URLs (custom domains)

Per internal tooling config — **omit secrets** in packet:

| Role | URL |
|------|-----|
| API | `https://crosbytx-api.thinline.app` |
| UI | `https://crosbytx.thinline.app`, `https://crosbytx.thinlinesoftware.com` |
| Keymaster | `https://tls-crosbytx-prod-keymaster.azurewebsites.us` |
| File share label | `tls-crosbytx-prod-fileshare` |

---

## Encryption & backup (2026-07-06)

| Control | Value |
|---------|--------|
| SQL TDE | **Enabled** |
| LTR weekly | P8W |
| LTR monthly | P1Y |
| LTR yearly | P10Y |
| Time-based immutability | **Disabled** |

---

## Vendor posture (shared across tenants)

- **No on-prem Thin Line RMS appliance** at agency — browser HTTPS + Azure Gov backends.  
- **Direct TLETS interface (proposed)** — in-app TCIC/NCIC queries via Thin Line as interface vendor; see `Docs/TLETS/application/`.  
- Full architecture: [`../../attestation-kit/03-architecture-and-data-flow.md`](../../attestation-kit/03-architecture-and-data-flow.md)

---

## Refresh

```powershell
./../../scripts/update-azure-inventories.ps1 -Tenant crosbytx
```
