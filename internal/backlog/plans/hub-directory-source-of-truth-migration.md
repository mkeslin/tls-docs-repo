---
backlog: "Hub / Directory · Source-of-truth migration (no BL-### yet)"
status: in-progress
created: 2026-07-19
---

# Plan: Hub ↔ Directory source-of-truth migration

## Goal

Hub manages Directory **tenants** and **tenant environments** (including deployed versions) without duplicating that current-state data in Hub. Hub **Clients** remain the agency CRM catalog, each linked to a tenant slug.

## Context

- **Design (Phase 0 — accepted):** [hub-directory-tenant-agency-ownership.md](../design/hub-directory-tenant-agency-ownership.md)
- **Risk / lane:** Platform / Hub + Directory; auth and API contract changes; avoid dual-write of env config.
- **Repos:** `TLS-Hub`, `TLS-Directory`, Thin Line Software deploy pipelines.

## Domain (frozen)

| Concept | System | Cardinality |
|---------|--------|-------------|
| Tenant (install slug) | Directory `Tenants` | 1 tenant → many agencies |
| Agency | Hub `Clients` | many → 1 tenant via slug (`FriendlyName` today) |
| Environment | Directory `TenantEnvironments` | 1 tenant → many envs |
| CRM (ORI, contract, ARR, contacts, invoices) | Hub | per agency |

**Hub UI intent**

| Page | Target |
|------|--------|
| Clients | Mostly unchanged — agency CRM + tenant slug |
| Tenants | **New** — Directory Tenants |
| Environments | Same kind of data — Directory `TenantEnvironments` |

## Approach

### Phase 0 — Freeze ownership ✅

- [x] Design doc accepted and linked from GitBook SUMMARY / design README.
- [x] Implementation plan captured here.
- [x] Canvas updated to match.
- [x] Hub `Client.FriendlyName` documented in code as tenant slug.

### Phase 1 — Directory Hub-ready APIs ✅

1. [x] Tenant metadata: `GET/POST /tenants`, `GET/PUT /tenants/{tenantCode}` (`ConfigAuth`).
2. [x] Environments: `GET /environments`, `GET/POST /tenants/{code}/environments`, `GET/PUT …/environments/{resource}` (no `CurrentVersion` — Hub probes live apps).
3. [x] Keep `…/config` for deploy settings only.
4. [x] `ConfigAuth` on `/tenants`, `/directory`, and new metadata routes (JWT or API key).
5. [x] Directory WebAPI tests passing.

### Phase 2 — Hub proxy + Clients + Tenants (read-first) ✅

1. [x] `IDirectoryApiClient` → Directory with Descope service JWT (same as Logs); pipelines keep `X-API-Key`.
2. [x] Hub proxy: `tlsapi/directory/tenants`, `tlsapi/directory/environments` (avoids clash with Descope `tlsapi/tenants`).
3. [x] Clients page: Tenant slug column + dialog label; filter `?tenantSlug=`.
4. [x] New Tenants page (`/directory-tenants`) read-only from Directory; Agencies link filters Clients.
5. [x] Obsolete stale `DirectoryStore` (`/clients`); removed from DI.

### Phase 3 — Environments → Directory + writes ✅

1. [x] Environments page reads Directory `TenantEnvironments` for catalog metadata.
2. [x] **Version** = live probe of each environment’s running API (`UrlApi` or `{tenant}-api` fallback) — not stored/edited in Directory for Hub.
3. [x] Writes for env metadata (resource, type, Azure, name) → Directory via Hub proxy.
4. [x] Config edits → Directory `…/config` PUT via Hub proxy (JSON editor).
5. [x] Directory metadata responses include non-secret `UrlApi` / `UrlUi1` for probes and links.

### Phase 4 — Retire Hub `ClientEnvironments` SoT

1. Stop catalog create/edit against Hub `ClientEnvironments`.
2. Ignore unused Hub `Client` URL/DB columns.
3. Later drop/archive Hub env table when unused.

### Phase 5 — Cutover

1. Inventory tenant slug ↔ Client mapping (1→many).
2. Dual-run then remove Hub env writes.
3. Deploy order: Directory API → Hub UI/proxy → pipeline version write → retire.

## Files / areas (expected)

| Phase | Areas |
|-------|--------|
| 0 | `tls-docs-repo/internal/backlog/design/…`, `plans/…`; Hub `Client.cs` comment |
| 1 | `TLS-Directory` … `Endpoints.cs`, view models, auth, tests |
| 2–4 | `TLS-Hub` API services/controllers, UI Clients/Tenants/Environments |
| 3 | Thin Line Software deploy pipelines (version bump) |

## Verification

- [ ] Directory: build + `ThinLine.Directory.WebAPI.Tests`
- [ ] Hub: build + relevant API/UI checks for touched screens
- [ ] Manual: Tenants list matches Directory; Environments for `crosbytx` / `slatontx` are tenant-scoped; multiple Clients share one slug
- [ ] Pipelines still fetch config from Directory only

## Open questions

- Rename `FriendlyName` → `TenantSlug` timing (API break vs label-only).
- Soft-validate slug exists in Directory on Client save.

## Notes

- Do not invent Hub tables that mirror Directory current-state.
- Hub `tlsapi/tenants` (Descope) ≠ Directory installs — keep UI naming distinct.
