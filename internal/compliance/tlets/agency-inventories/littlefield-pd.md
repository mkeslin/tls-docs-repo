# Littlefield PD (`littlefieldtx`) — Azure inventory

> Moved from TLS-App `Docs/TLETS/agencies/littlefield-pd/azure-inventory.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Purpose:** Vol 03 appendix for Littlefield PD TLETS attestation kit. Resource names from **`az` CLI** (Azure Government, subscription **TLS Azure Subscription 1**).

**Last refreshed:** 2026-07-06

**⚠ Sensitive:** Do not ship connection strings, keys, or credentials.

---

## Resource naming (Thin Line-hosted RMS)

### Subscription & cloud

| Item | Value |
|------|--------|
| Subscription | TLS Azure Subscription 1 |
| Azure cloud | **Azure Government** |
| Resource group | `tls` |
| SQL logical server | `tls-db2` |

### App Services & database

| Azure resource name | Type | Region |
|---------------------|------|--------|
| `tls-littlefieldtx-prod-api` | App Service | USGov Texas |
| `tls-littlefieldtx-prod-ui` | App Service | USGov Texas |
| `tls-littlefieldtx-prod-rms` | SQL Database | USGov Texas |

Default hostnames:

| App | Hostname |
|-----|----------|
| API | `tls-littlefieldtx-prod-api.azurewebsites.us` |
| UI | `tls-littlefieldtx-prod-ui.azurewebsites.us` |

### Published URLs (custom domains)

| Role | URL |
|------|-----|
| API | `https://littlefieldtx-api.thinline.app` |
| UI | `https://littlefieldtx.thinline.app`, `https://littlefieldtx.thinlinesoftware.com` |
| Keymaster | `https://tls-littlefieldtx-prod-keymaster.azurewebsites.us` |
| File share label | `tls-littlefieldtx-prod-fileshare` |

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

## Vendor posture (shared)

See [`../../attestation-kit/03-architecture-and-data-flow.md`](../../attestation-kit/03-architecture-and-data-flow.md).

---

## Refresh

```powershell
./../../scripts/update-azure-inventories.ps1 -Tenant littlefieldtx
```
