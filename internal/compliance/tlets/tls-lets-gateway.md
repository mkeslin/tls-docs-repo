# tls-lets gateway service (internal)

**Status:** Working draft — **internal only**  
**Scope:** Thin Line **tls-lets** (`ThinLine.LETS.*`) — the Law Enforcement Message Switch **gateway** that sits between Thin Line RMS/CAD and state message switches (Texas DPS TLETS first).

Customer-facing query steps stay in [Direct LETS queries](../../customer/cad/direct-lets-queries.md). Thin Line API device enforcement: [Direct LETS operations](direct-lets-operations.md).

---

## What it is

**tls-lets** is a dedicated .NET service that:

- Exposes a **versioned REST API** (`POST /v1/queries`, `GET /v1/queries/{id}`, optional cancel) for outbound switch traffic.
- Routes work by **state code** through an **adapter registry** (Texas = `TexasDpsAdapter`).
- Maintains **persistent TCP sessions** to external switches (FoxTalk framing for Texas).
- Persists query status and optional response payloads in a **SQL Server query store** (`LetsDb`).
- Emits **CJIS-friendly audit** events (Serilog; optional **Service Bus** sink for centralized event log).

Thin Line **does not** embed FoxTalk or DPS wire protocol in the main API process for direct LETS; the API calls the gateway over HTTPS with a configured **API key** and timeout.

---

## Solution components

| Layer | Project | Responsibility |
|-------|---------|----------------|
| **API** | `ThinLine.LETS.Api` | HTTP surface, middleware pipeline, DI host, Kestrel on the gateway VM |
| **Core** | `ThinLine.LETS.Core` | Domain models (`GatewayQuery`, `StoredQuery`, `QueryStatus`), adapter and store interfaces — no infrastructure dependencies |
| **Infrastructure** | `ThinLine.LETS.Infrastructure` | `QueryPipeline`, `SqlServerQueryStore`, `SerilogAuditLogger`, `RedactionHelper`, `TerminalCircuitRouter`, security middleware, `TexasDpsOptions` binding |
| **Texas adapter** | `ThinLine.LETS.Adapters.TexasDps` | `TexasDpsAdapter`, `TcpSession` / `FakeTcpSession`, FoxTalk framing, message build/parse, test-switch vs production routing |
| **Tests** | `ThinLine.LETS.Tests` | Unit and integration tests (coverage gate in CI) |

---

## API middleware and auth

Request order (conceptual):

1. **Bearer API key** — `AuthStubMiddleware` validates `Authorization: Bearer …` against the environment **Security.ApiKey** (deployed from `Configs/config.Test.json` / `config.Production.json`; token replacement in `appsettings.Production.json` at deploy). Missing or invalid key → **401**.
2. **IP allowlist** — `IpAllowlistMiddleware` when `Security.AllowedCidrs` is configured. Client IP not in CIDR list → **403**.

These are **gateway** controls (Thin Line API → tls-lets). They are separate from Thin Line **user/device** TLETS authorization (`TletsDeviceAuthorizationFilter`, agency switch, claims) documented in [Direct LETS operations](direct-lets-operations.md).

---

## Query pipeline (gateway)

`QueryPipeline.SubmitAsync`:

1. Assign **query id** and **correlation id**.
2. Persist `StoredQuery` with status **Accepted**.
3. **Fire-and-forget** background execution (API returns immediately).
4. Background: resolve adapter by state → **serialized send** (one outbound at a time per adapter semantics) → update store → audit.

Outcomes map to **Completed**, **Timeout**, **Failed**, or **Cancelled**. `AuditOptions` control whether full response text is persisted in the store vs metadata-only audit.

**Redaction:** `RedactionHelper` hashes or redacts PII in audit log fields per configured field names and salt.

---

## Texas DPS adapter highlights

| Concern | Behavior |
|---------|----------|
| **FoxTalk** | Length-prefixed frames over TCP; session negotiation with server/device mnemonics |
| **Test switch** | When test mode and test host/port are configured, queries use a dedicated test identity and an unencrypted FoxTalk session to the **TLETS test switch** |
| **Production** | Circuit map routes **requesting ORI** to a **terminal circuit** (host/port per route). Recent behavior: production sends can share the **same FoxTalk TCP session** as the test-switch path where configured (agency ORI and user remain on the inquiry; production device mnemonic stamped per route) |
| **Encryption flag** | `EncryptionEnabled` — test bed starts unencrypted; gateway refuses encrypted mode until implemented |
| **Retries** | Configurable retry count on send/receive failures; connection backoff on test-switch connect failures |

Do **not** copy hostnames, ports, mnemonics, or API keys from `Configs/` or agency-specific production notes into GitBook — reference **role names** only in customer or shared internal docs.

---

## Persistence and logging

| Store | Role |
|-------|------|
| **LetsDb (SQL Server)** | Query lifecycle, status, optional `responsePayload`, error messages |
| **Serilog** | Structured audit lines per query outcome |
| **Service Bus** (optional) | `EventLogServiceBusConnectionString` — Serilog sink; malformed connection string must not crash startup (service stays up; local logging remains) |

---

## Related internal docs

- [End-to-end direct query round trip](end-to-end-direct-query.md) — Thin Line UI through DPS and back
- [Azure hosting and agency inventory](azure-hosting-and-agency-inventory.md) — deploy pipeline, VMs, networking pattern
- [Direct LETS operations](direct-lets-operations.md) — API-side device model and SecurityLog
- [TLETS application home](README.md)
