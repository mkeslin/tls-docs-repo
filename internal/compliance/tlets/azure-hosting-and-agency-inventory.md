# tls-lets Azure hosting and agency inventory (internal)

**Status:** Working draft — **internal only**

How **tls-lets** is built, deployed, and networked toward DPS, and how per-agency Azure evidence fits the TLETS application packet. **Never** paste secrets, API keys, connection strings, production IP addresses, or credentials into GitBook — name roles and configuration keys only.

Monorepo packet sources: `ThinLineSoftware` → `Docs/TLETS/` (attestation kit, application, **agencies/** inventories).

---

## Hosting model

| Piece | Pattern |
|-------|---------|
| **Cloud** | **Azure Government** subscription dedicated to the LETS gateway project |
| **Compute** | Linux **VMs** per environment (test and production names in pipeline: e.g. `tls-lets-test`, `tls-lets-prod`) |
| **Install path** | `/opt/thinline-lets` — self-contained `ThinLine.LETS.Api` executable |
| **Process manager** | **systemd** unit `thinline-lets` (stop before file replace on deploy; restart after unzip) |
| **Database** | Azure SQL logical servers in US Gov cloud (`tls-test` / `tls-prod` naming in pipeline — **LetsDb** migrations applied at deploy) |
| **Artifact storage** | Deploy zip uploaded to a **deploy storage account** container (`releases`); VM install script pulls build artifact by URL |

---

## CI/CD pipeline (summary)

**Trigger:** `master` branch (batch; PRs do not deploy).

| Stage | Purpose |
|-------|---------|
| **Build** | `dotnet test` with coverage threshold (~80%), `dotnet publish` linux-x64 self-contained, EF idempotent migration script, copy `Configs/config.*.json`, zip app |
| **DeployTest** | Azure DevOps **environment: test** — deploy template with test SQL server, test resource group, test VM, `config.Test.json` |
| **DeployProduction** | Depends on test; **environment: production** with approval gate — production SQL server, production resource group, production VM, `config.Production.json` |

**Service connection:** Azure Government subscription alias used by the pipeline (e.g. `TLS-Azure-Gov-TLS-LETS`).

Pipeline replaces placeholder tokens in `appsettings.Production.json` (API key, connection strings, DPS host placeholders) from the environment-specific JSON in `Configs/` at deploy time — those files stay **out of GitBook**.

---

## Networking toward DPS

| Topic | Internal guidance |
|-------|-------------------|
| **Path** | Gateway VM → **site-to-site VPN / SD-WAN** (agency or Thin Line–operated) → **DPS-approved** endpoint on the message switch |
| **Satellite / county edge** | Some agencies document a **satellite router** or county tunnel in kit diagrams; gateway config must match the approved circuit for that ORI |
| **IP allowlist** | Two layers: (1) **gateway** `Security.AllowedCidrs` for Thin Line API callers; (2) **Thin Line API** staff-configurable agency TLETS IP allowlist for direct query attempts — see [Direct LETS operations](direct-lets-operations.md) |
| **FoxTalk** | TCP sessions initiated from adapter; test switch typically unencrypted until encryption is implemented |
| **Terminal circuits** | Production **per-ORI** host/port map in gateway config (`TerminalCircuitRouter`) — describe as “assigned circuit” in forms, not literal addresses in docs |

Agency-facing diagram templates: [Agency network diagram template](agency-network-diagram-template.md), [Thin Line network diagram insert](thin-line-network-diagram-insert.md).

---

## CJIS / Azure Government notes

- Gateway and LetsDb live in **Azure Government** regions (agency RMS inventories document USGov Texas / Virginia patterns for app data; gateway SQL servers are Gov cloud endpoints in pipeline parameters).
- **FIPS / TLS** evidence for interface packets is collected per tenant (cipher suite exports referenced in attestation kit — not duplicated here).
- **Service Bus** (optional): centralized security/event log sink from gateway Serilog — connection string name `EventLogServiceBusConnectionString`; invalid config must not prevent the API from running.

---

## Per-agency Azure inventory pattern

Under `Docs/TLETS/agencies/{agency}/`:

| Artifact | Purpose |
|----------|---------|
| `README.md` | Coordinator, tenant key, kit status |
| `azure-inventory.md` | Resource inventory for disclosure templates (SQL, storage, monitoring regions) |

**Active rollout set** (internal dashboard): Slaton PD, Crosby County SO, Littlefield PD, Crystal City PD, Levelland PD — each with tenant key and parallel Phase 1 / Phase 2 tasks.

OPS refreshes inventories via scripted export (`update-azure-inventories.ps1` in monorepo) for **cloud data storage disclosure** and CJIS packets — compact inventory for Phase 1, full refresh on Phase 2 kickback.

---

## Thin Line API ↔ gateway configuration

On the **RMS/CAD** side (not on the gateway VM):

```json
"LetsGateway": {
  "BaseUrl": "",
  "ApiKey": "",
  "TimeoutSeconds": 20
}
```

Unresolved **BaseUrl** = direct LETS not configured. Failures return reasons shown in the UI error field.

---

## Related

- [tls-lets gateway service](tls-lets-gateway.md)
- [End-to-end direct query round trip](end-to-end-direct-query.md)
- [Direct-interface scope](direct-interface-scope.md)
- [TLETS application home](README.md)
