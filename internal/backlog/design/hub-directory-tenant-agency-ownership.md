---
title: "Hub / Directory — tenant, agency, and environment ownership"
status: accepted
created: 2026-07-19
modules: [Hub, Directory, Platform]
backlog: []
---

# Design: Hub / Directory — tenant, agency, and environment ownership

## Goal

Freeze who owns **install (tenant)**, **agency (client)**, and **environment** data so Hub can manage Directory tenants/envs without duplicating current-state rows in the Hub database.

## Context

- Hub `Clients` today are **agency-shaped** CRM rows (e.g. Crosby County SO, Crosbyton PD). Several share one `FriendlyName`, which already behaves as a **tenant slug** (e.g. `crosbytx`, `slatontx`).
- Directory `Tenants` / `TenantEnvironments` are the deploy/runtime source of truth (pipelines use `GET/PUT …/config`).
- Hub also stores `ClientEnvironments` (manual version, Azure account, etc.) — overlapping Directory and prone to drift.
- Related plan: [hub-directory-source-of-truth-migration.md](../plans/hub-directory-source-of-truth-migration.md).
- Product repos: `TLS-Hub`, `TLS-Directory`; deploy scripts/pipelines in Thin Line Software.

## Decisions

1. **Tenant = install (Directory)** — Logical Azure/resource install identified by a **slug** (`TenantCode`, e.g. `crosbytx`). Directory owns name, resource name, active flag, and all `TenantEnvironment` rows (config bag, `CurrentVersion`, env type/resource, etc.).
2. **Client = agency (Hub)** — One Hub `Clients` row per agency. Hub owns CRM: display name, ORI, contact organization, ARR, contract date, invoices, work-item linkage, active flag for CRM purposes.
3. **Tenant 1 → many Clients** — Each agency references exactly one tenant slug. Shared installs (Crosby, Slaton, New Deal, …) keep multiple Hub clients under one Directory tenant.
4. **Environments belong to the tenant** — Not to the agency. Hub’s Environments UI is driven by Directory `TenantEnvironments`. Hub must not remain the source of truth for env current-state.
5. **No mirrored current-state in Hub** — Do not add or expand Hub columns that copy Directory tenant/env config. Hub may **link** and **display** via API. Optional live “AutoVersion” probes are operational checks, not a second write store.
6. **RMS agencies stay in RMS** — Runtime agencies inside a shared customer DB remain product data. Hub `Clients` is the **internal ops catalog** of agencies we sell to / support, linked to the install slug — not a sync of every RMS `Agencies` row.
7. **Tenant slug on Client** — Today’s Hub `Client.FriendlyName` **is** the tenant slug (maps to Directory `TenantCode`). Later phases may rename the property for clarity; until then, treat `FriendlyName` as the slug in product language and UI labels where practical.

### Alternatives considered

| Alternative | Why not |
|-------------|---------|
| Hub Client = Directory Tenant (1:1) | Breaks shared installs; contradicts existing multi-agency `FriendlyName` data. |
| Sync/mirror Directory into Hub tables | Drift and dual writes; pipelines already trust Directory. |
| Environments stay on Hub `ClientEnvironments` | Wrong parent (agency vs install); duplicates Directory. |

### Consequences

- New Hub **Tenants** page (Directory-backed); existing **Clients** page stays agency CRM.
- **Environments** page keeps similar UX but reads/writes Directory.
- `ClientEnvironments` is legacy and will be retired after cutover.
- Directory APIs must expose tenant + env metadata (including `CurrentVersion`) with service auth Hub can use.

## Scope

### In scope (ownership freeze)

- Domain vocabulary and cardinality.
- Which system is source of truth for which fields.
- Hub UI intent: Clients / Tenants / Environments.
- Ban on new Hub mirrors of Directory current-state.

### Out of scope (later phases)

- Directory CRUD API implementation details.
- Hub proxy/UI implementation.
- Schema rename of `FriendlyName` → `TenantSlug`.
- Dropping `ClientEnvironments` columns/tables.
- Applying Directory migration `DropTenantOriContractDateIdentityId` (already scaffolded; deploy separately).

## Approach (high level)

1. Accept this ownership design (Phase 0).
2. Extend Directory APIs for tenant/env metadata + auth (Phase 1).
3. Hub: keep Clients; add Tenants page; point Environments at Directory (Phases 2–3).
4. Retire Hub `ClientEnvironments` as SoT; cutover (Phases 4–5).

## Open questions

- Whether to rename `FriendlyName` → `TenantSlug` in Hub API/UI in the same phase as Tenants page, or label-only first.
- Whether Hub should soft-validate that a Client’s tenant slug exists in Directory before save (recommended once proxy exists).

## Follow-on work

| Work item | Plan |
|-----------|------|
| Hub ↔ Directory source-of-truth migration (phased) | [hub-directory-source-of-truth-migration.md](../plans/hub-directory-source-of-truth-migration.md) |

## Notes

- Directory recently removed unused `Tenants.ORI`, `ContractDate`, and `IdentityId` — commercial ORI/contract stay on Hub agency CRM; Descope tenant id stays on env config (`Identity.TenantId`), not on Directory `Tenants`.
- Descope “tenants” exposed via Hub `tlsapi/tenants` are **identity** tenants, not Directory installs — keep naming distinct in UI (“Identity tenants” vs “Installs / Tenants”).
