# Slaton PD (`slatontx`) — Azure inventory & Q1–Q9 vendor notes

> Moved from TLS-App `Docs/TLETS/agencies/slaton-pd/azure-inventory.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Purpose:** Vol 03 appendix for Slaton PD TLETS attestation kit. CPSO-ready resource naming from **`az` CLI** (Azure Government subscription **TLS Azure Subscription 1**).

**Phase 1:** For first submission, export only the **Resource naming**, **Encryption & backup**, and **Published URLs** sections (or use the compact inventory pattern in [`../crosby-county-so/azure-inventory.md`](../crosby-county-so/azure-inventory.md)). Full Q1–Q9 content is **Phase 2** — see [`../../phase-2-kickback/README.md`](../../phase-2-kickback/README.md).

**Agency folder:** [`README.md`](./README.md)

**Last refreshed (inventory core):** 2026-05-12 · **TDE/LTR verified:** 2026-07-06

**⚠ Sensitive:** Connection strings/credentials elsewhere in tooling must **never** ship in this packet — use MFA-restricted portals for assessor verification.

---

## Q1 — Slaton-specific resource names (Thin Line-hosted RMS)

Recorded **2026-05-12** via `az` against the Thin Line gov subscription unless noted.

### Subscription & cloud

| Item | Value |
|------|--------|
| Subscription (display name) | TLS Azure Subscription 1 |
| Tenant | thinlinesoftware (`.onmicrosoft.us`) |
| Azure cloud | **Azure Government** |

### Resource group (`tls`)

| Azure resource name | Type | Primary region (`location` from Azure) |
|---------------------|------|---------------------------------------|
| `tls-slatontx-prod-api` | App Service (**Web/site**) | **usgovtexas** |
| `tls-slatontx-prod-ui` | App Service (**Web/site**) | **usgovtexas** |
| `tls-slatontx-prod-api-ai` | Application Insights | **usgovvirginia** |
| Failure Anomalies detector for **`tls-slatontx-prod-api-ai`** | Smart detector alert rule | global |
| **`tls-db2`** | Azure SQL logical server | **usgovtexas** |
| **`tls-slatontx-prod-rms`** | SQL Database (under `tls-db2`) | **usgovtexas** |

Default hostnames (public App Service URLs):

| App | `.azurewebsites.us` hostname |
|-----|-------------------------------|
| API | **tls-slatontx-prod-api.azurewebsites.us** |
| UI | **tls-slatontx-prod-ui.azurewebsites.us** |

SQL logical server FQDN: **`tls-db2.database.usgovcloudapi.net`**

### Transparent Data Encryption (TDE)

Database **`tls-slatontx-prod-rms`** on **`tls-db2`**: **`state`** = **`Enabled`** (Azure SQL transparent data encryption at rest — Microsoft-managed).

### Long-term backup retention (LTR)

`az sql db ltr-policy show` Snapshot for **`tls-slatontx-prod-rms`**:

| Policy field | ISO 8601 / value |
|--------------|-------------------|
| `weeklyRetention` | **P8W** (~8 weeks) |
| `monthlyRetention` | **P1Y** (~1 year) |
| `yearlyRetention` | **P10Y** (~10 years) |
| `timeBasedImmutability` | **Disabled** (**⚠** if assessors insist on **immutable** vault semantics — reconcile with OPS/CPSO wording) |

**Point-in-time restore (automatic):** Thin Line OPS should screenshot **configured PITR window** per database from Portal (CLI short-term retention command failed in this environment).

### Published URLs (Thin Line–managed)

Tooling snapshot (**⚠ omit secrets**) in the TLS-Directory config `slatontx` / prod (the old `Clients/__Tools/Config` copy was retired):

| Role | HTTPS URL |
|------|-----------|
| API (custom hostname) | `https://slatontx-api.thinline.app` |
| UI hosting | `https://tls-slatontx-prod-ui.azurewebsites.us` plus custom **`https://slatontx.thinline.app`**, **`https://slatontx.thinlinesoftware.com`** |
| Separate **Keymaster** URL | Listed in tooling (**⚠ OPS** reconcile): **`https://tls-slatontx-prod-keymaster.azurewebsites.us`** — ARM object **`tls-slatontx-prod-keymaster`** **not** seen in **`tls`** RG scrape (verify **alive vs retired). |
| Attachment **file-share** label | **`tls-slatontx-prod-fileshare`** (**⚠** map to storage ARM object via Portal export). |

---

## Q2 — On-prem Thin Line RMS infrastructure

**Vendor answer:** **No Thin Line RMS server/appliance deployed at PD.** Access is via **agency computers**, **HTTPS**, plus **agency-owned peripherals** (**mobile printers** and **mobile scanners** DL / registration stickers—not Thin Line RMS application servers).

Diagram / narrative boundary: peripherals connect to agency PCs or workstations; RMS remains **browser + Azure Gov backends**.

---

## Q3 — AI-related functionality ("check Azure")

**Operational synopsis (Generate Synopsis on incidents)**

- RMS calls **`IncidentService.GetIncidentSummaryAsync`** which sends the **primary (or first) incident narrative HTML** through **`ThinLine.Framework.TextAnalytics.TextAnalyticsService`** **abstractive summarization**.
- Hosted Microsoft surface: **`https://tls-ai-language-service.cognitiveservices.azure.us/`** (**Azure AI Language** in **Government** cloud taxonomy).
- This path is distinct from **`ThinLineAiService`** / **`AiController`** (Azure OpenAI chat assistant UX).

**CPSO-facing short statement:** Incident **synopsis** text is derived by **Azure AI Language** summarize API from **narrative content** uploaded to RMS; Thin Line OPS should cite **tenant region**, **encryption in transit**, and **data-processing** attestations matching Microsoft CJIS-aligned documentation for AI services deployed in gov cloud.

**(Security engineering — out of CPSO appendix but CRITICAL)**

- [`ThinLine.API/ThinLine.Framework/TextAnalytics/TextAnalyticsService.cs`](../../../ThinLine.API/ThinLine.Framework/TextAnalytics/TextAnalyticsService.cs) currently embeds a **plaintext API credential** inline. **`Clients/__Tools__/Config/SlatonTX/slatontx.prod.config.json`** also stores **plaintext SQL password** tooling-side. **`Rotate`** Azure keys/passwords ASAP, **`purge`** secrets from commits per security policy**,** migrate callers to **`Key Vault` + MSI**/`user-secrets`/pipeline variables.

---

## Q4–Q5 — V5.9.5 on-prem vs cloud assessment

**Status:** User confirmed a **cloud assessment is required** for Thin Line Software LLC's hosted/vendor RMS scope. Thin Line OPS should still confirm whether a separate agency on-prem questionnaire remains required in parallel.

Suggestion: Ask CJISO whether the **agency on-prem questionnaire** is also required while RMS is SaaS-hosted, and how DPS wants the Thin Line cloud assessment cross-referenced to the agency packet.

---

## Q6 — "Partner endpoints without logging"

**Explanation:** Assessors flagged **integrations that leave your trusted boundary** (**Descope**, **Stripe**, maps, AI Language, SMTP, webhook targets, Redis if external, Payment processors, webhook consumers, etc.). **SIEM/control expectation:** each category should tie to **logged + reviewed** egress (Firewall logs, Azure diagnostic settings, ASC recommendations).  

**Thin Line homework:** Maintain table **Hostname / purpose / logs owner / reviewer frequency** (**weekly** excerpt for CPSO SI-4 story).

---

## Q7–Q8 — DR / backups / encryption (Azure-checked vs OPS follow-up)

| Topic | Automated pull | Follow-up OPS |
|-------|-----------------|---------------|
| **SQL backups** | LTR durations above (**weekly/monthly/yearly**) | Confirm **GEO-DR failover** posture + **immutable** wording if CPSO mandates immutability (LTR **`timeBasedImmutability`** today **Disabled**). |
| **App Service resilience** | not scripted here | OPS ARR/multi-instance + regional DR narrative.
| **Encrypt at rest DB** | **TDE Enabled** ✅ | CPSO wording on Always Encrypted CMK necessity for selected columns — **agency decision**.
| **Metadata** | MSSQL encrypts `.mdf` via TDE; **metadata ABOUT data** CPSO clarification | Document column-level classifications if CPSO distinguishes.

---

## Q9 — FIPS 140-3 / Sep 2026

**Thin Line posture:** Use Microsoft Azure FIPS 140 language. Microsoft states that FIPS 140 validation applies to **cryptographic modules**, not to a cloud service as a whole. Microsoft also states that cloud service providers can obtain and operate **FIPS 140 validated cryptographic modules** for the computing elements that comprise their cloud services, and that Azure services use **FIPS 140 approved algorithms** for data security.

For Slaton RMS, Thin Line should submit the Azure Government service inventory, diagrams, Azure TLS policy screenshots, certificate information, and Azure SQL TDE evidence. Microsoft states that Azure SQL Database transparent data encryption relies on FIPS 140 validated encryption through underlying operating-system cryptographic modules; Thin Line should not represent the Thin Line RMS application or Azure cloud service itself as FIPS 140 validated.

**Customer responsibility:** Validate **Operating Environment**, **termination**, **accepted cipher suites**, and any **FIPS-approved mode of operation** claims with configuration evidence for the relevant module/service. Track the 2026-09-21 transition of FIPS 140-2 module validations to the CMVP historical list and coordinate final wording with Azure Government guidance, Thin Line OPS/counsel, and **DPS/CPSO**.
