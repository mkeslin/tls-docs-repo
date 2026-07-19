# Security Command Center — Design Document

> **Source of truth:** Internal Docs (GitBook). Paths under `ThinLine.UI/` and `ThinLine.API/` refer to the product monorepo.


**Thin Line Platform — CJIS & Identity Oversight Cockpit**

Placeholder / demo shell matching Patrol, Investigation, Supervisor, Data Integrity, and Chief command centers. Tuned for LASO / CJISO / RMS admin workflows: CJIS readiness, access & identity, security event triage, and audit evidence export.

---

## Screen Structure Overview

Three-column command center layout:

| Left Column | Center Column | Right Column |
|-------------|---------------|--------------|
| Security Queues & Alerts | Workspace (tabs) | Context & Security Actions |
| ~1fr | ~2fr | ~1fr |

Full-width **Top Bar** above all columns.

### Center tabs

1. **CJIS Readiness** — policy area coverage and gaps (links to Help → Compliance → CJIS)
2. **Access & Identity** — failed logins, MFA, access reviews, dormant accounts
3. **Security Events** — triage feed (future: Admin Security Log)
4. **Audit Trail** — recent audit actions and export packet actions

### Left queues

- CJIS readiness gaps
- Access & identity issues
- Security events
- Access review queue

---

## Route & visibility

| Item | Value |
|------|--------|
| Route | `/security` |
| Module key | `SEC` |
| Classic nav | Hidden (commented with other stubs) |
| Modern nav | Full-support users only |

---

## Boundaries

- **Not** Data Integrity (record quality / duplicates / NIBRS fields)
- **Not** Chief compliance headlines (executive rollup)
- **Does** own who accessed what, who is privileged, and CJIS control evidence readiness

Placeholder data lives in `ThinLine.UI/src/data/placeholderData.ts` (`securityPlaceholder`).
