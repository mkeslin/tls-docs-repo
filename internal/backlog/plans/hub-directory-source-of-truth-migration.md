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

### Phase 1 — Directory Hub-ready APIs

1. Tenant metadata GET/PUT (Name, ResourceName, IsActive); optional POST.
2. Environments list/update including `CurrentVersion`, `EnvironmentType`, Azure/resource fields.
3. Keep `…/config` for deploy settings only.
4. Apply `ConfigAuth` (JWT or API key) to tenant/env list + write.

### Phase 2 — Hub proxy + Clients + Tenants (read-first)

1. Real Directory HTTP client in Hub (replace stale `/clients` DirectoryStore).
2. Clients page stays; treat `FriendlyName` as tenant slug (label/validate).
3. New Tenants page — Directory-backed, start read-only.
4. Show agencies under a tenant via Clients filtered by slug.

### Phase 3 — Environments → Directory + writes

1. Environments page reads Directory `TenantEnvironments`.
2. Writes for env metadata / `CurrentVersion` → Directory.
3. Config edits → existing config PUT.
4. Pipelines bump Directory `CurrentVersion` on deploy.
5. Optional: keep live AutoVersion probe as “running” only.

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
