# Bootstrap vs Configuration

**Document type:** Reference  
**Status:** v1  

Keeps the boundary crisp for Implementation: **what bootstrap creates** vs **what configuration sets**.

---

## One-line rule

| | |
|--|--|
| **Bootstrap** | Infrastructure and platform wiring exist; apps run; someone can log in. |
| **Configuration** | The agency is set up to do **their** work (ORI, officers, courts, codes, devices, policies). |

Bootstrap **stops** when the [Bootstrap Environment Standard](bootstrap-environment-standard.md) and [Environment Health Checklist](../../checklists/environment-health-checklist.md) are satisfied.

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

| Area | Examples |
|------|----------|
| Agency profile | ORI, addresses, time zone, branding beyond display name |
| People | Officers, users, roles, shifts |
| Courts | Court agencies, judges, dockets setup |
| Codes | Violation / offense / local code lists beyond baseline |
| Devices | Printers, scanners, mobile |
| Comms | Email SMTP / notification settings |
| Policies | Agency validation flags, IBRS options, workflow policy toggles |
| Integrations | Third-party endpoints specific to the customer |

These belong to **Implementation / configuration** SOPs (and eventually Hub configuration), not `bootstrap-client.ps1`.

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
Bootstrap  →  Configuration  →  Migration (optional)  →  Training  →  Go Live
```

See [Environment Lifecycle](environment-lifecycle.md).

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
| [Customer Onboarding](customer-onboarding.md) | Broader Deliver sequence *(placeholder)* |
| [Hub Environment Integration](hub-environment-integration.md) | Future Environment vs Configuration objects |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — boundary definition |
