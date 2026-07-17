# Environment Classification

**Document type:** Reference  
**Status:** v1  

Purpose of each environment **type**. Script parameter `-Environment` today accepts `dev` | `test` | `prod` only.

---

## Types

| Type | Purpose | Script tier today | Typical use |
|------|---------|-------------------|-------------|
| **Development** | Internal engineering | `dev` | Feature work, non-customer sandboxes |
| **Test** | QA, demos, migration UAT, canaries | `test` | Pre-prod validation; `AgencyName` e.g. `canary` |
| **Production** | Customer live | `prod` | Go-live and ongoing operations |
| **Demo** | Sales demonstrations | Usually **`test`** (or dedicated test agency) | <mark style="color:red;">**TODO:**</mark> formalize dedicated demo tenants vs shared |
| **Training** | Customer training | Usually **`test`** or temporary prod-like | <mark style="color:red;">**TODO:**</mark> formalize vs using customer UAT |

---

## Rules

1. **Customer go-live** uses **`prod`** (or an explicitly approved exception).  
2. **Migration UAT** prefers **`test`** (or a dedicated non-prod agency) before Production import — see Legacy System Migration Decision 2.  
3. Do not use a shared **Demo** tenant as a customer’s Production.  
4. Classification is about **purpose**; naming still follows [Bootstrap Environment Standard](bootstrap-environment-standard.md).

---

## Profile alignment

| Tier | Profile file | Notes |
|------|--------------|--------|
| `prod` | `environments/prod.profile.json` | Production Directory/auth hosts, SQL defaults |
| `test` | `environments/test.profile.json` | Test Directory/auth hosts, separate RG/SQL |
| `dev` | `environments/dev.profile.json` | Fill before use — may be empty until configured |

---

## Related documents

| Document | Role |
|----------|------|
| [Environment Inventory Standard](environment-inventory-standard.md) | Components |
| [Environment Lifecycle](environment-lifecycle.md) | Stages |
| [Bootstrap Environment SOP](bootstrap-environment.md) | `-Environment` parameter |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — types and script-tier mapping |
