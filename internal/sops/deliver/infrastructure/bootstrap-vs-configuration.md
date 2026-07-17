# Bootstrap vs Configuration

**Document type:** Reference  
**Status:** v1  

Keeps the boundary crisp for Implementation: **what bootstrap creates** vs **what configuration sets**.

---

## One-line rule

| | |
|--|--|
| **Bootstrap** | Infrastructure and platform wiring exist; apps run; someone can log in. |
| **Configuration** | The agency is set up to do **their** work (ORI, officers, courts, codes, device *software settings*, policies). |

Bootstrap **stops** when the [Bootstrap Environment Standard](bootstrap-environment-standard.md) and [Environment Health Checklist](../../../checklists/environment-health-checklist.md) are satisfied.

---

## Bootstrap includes

| Area | Examples |
|------|----------|
| Azure | SQL DB, API/UI apps, file share, App Gateway routes |
| Data seed | Baseline bacpac import; seed agency **name** from FriendlyAgencyName |
| Auth | Descope tenant |
| Directory | Tenant config (API/UI URLs, identity pointers) |
| Deploy | Build/Deploy of VersionBranch |

---

## Configuration begins (not bootstrap)

Primary product surface: Admin → **Agency & Module Settings** — see [Agency & Module Settings](../configuration/agency-settings.md) and [Agency Configuration Checklist](../../../checklists/agency-configuration-checklist.md).

| Area | Examples |
|------|----------|
| Agency profile | ORI, addresses, branding, theme, report/document headers |
| Modules | Enable modules; record number patterns; next numbers |
| Workflow | Dashboard notifications; IBRS validate on submit/approve |
| People | Officers, users, roles (separate Admin screens) |
| Courts | Court settings, appearance defaults, program due dates, payments |
| Codes | Violation / offense / local code lists beyond baseline |
| Device software settings | Admin enables, print routes, mobile citation options—**not** physical install |
| Comms | Email SMTP / notification settings |
| Policies | Agency validation flags, IBRS options, sharing |
| Integration *settings* in Admin | OmniBase, Stripe, CAD webhook configuration cards |

These belong to **Configuration Complete** and related Admin work, not `bootstrap-client.ps1`.

### Configuration vs Integrations and Hardware (devices and interfaces)

| Owns | Phase | Examples |
|------|-------|----------|
| **Device software settings** | 4 · Configuration | Turn on printing/payments features; select printers in Admin; citation mobile options |
| **Installation, connectivity, compatibility, end-to-end proof** | 5 · Integrations and hardware | Drivers, pairing, network path, print/scan/mobile smoke tests, partner API live test |
| **Integration Admin cards** | Configured in 4; **proven** in 5 | Stripe/OmniBase/CAD webhooks: settings may be entered in Configuration; live verify is Phase 5 |

See [Integrations and hardware](../integrations-and-hardware.md) · [Hardware readiness checklist](../../../checklists/hardware-readiness-checklist.md).

---

## Grey areas (decide explicitly)

| Item | Guidance |
|------|----------|
| FriendlyAgencyName on Agencies.Name | **Bootstrap** (post-import SQL) |
| Full agency record / ORI | **Configuration** |
| Baseline codes in bacpac | **Bootstrap** seed |
| Customer-specific code adds | **Configuration** (or migration) |
| Directory URL pointers | **Bootstrap** |
| Directory feature flags for agency prefs | Prefer **Configuration** unless script must set for deploy |

---

## Lifecycle placement

```text
Infrastructure (bootstrap) → Data migration (optional) → Configuration
  → Integrations and hardware (optional) → Training → Go live → Hypercare
```

See [Implementation lifecycle](../implementation-lifecycle.md) · [Environment lifecycle](environment-lifecycle.md).

---

## Why this matters

- Prevents “bootstrap” scripts from becoming a dumping ground for every agency preference.  
- Lets Implementation SOPs own configuration checklists.  
- Clarifies Hub: Environment record (bootstrap) vs Configuration record (agency setup).

---

## Related documents

| Document | Role |
|----------|------|
| [Bootstrap Environment SOP](bootstrap-environment.md) | How to bootstrap |
| [Configuration](../configuration/README.md) | Phase overview |
| [Agency & Module Settings](../configuration/agency-settings.md) | Admin Agency inventory |
| [Agency Configuration Checklist](../../../checklists/agency-configuration-checklist.md) | Engagement checklist |
| [Integrations and Hardware](../integrations-and-hardware.md) | Devices + interfaces |
| [Kickoff and Discovery](../kickoff-and-discovery.md) | Scope / discovery |
| [Hub Environment Integration](hub-environment-integration.md) | Future Environment vs Configuration objects |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — boundary definition |
| 2026-07-17 | Linked Agency & Module Settings + configuration checklist |
| 2026-07-17 | Device settings vs Phase 5 proof; corrected lifecycle order |
