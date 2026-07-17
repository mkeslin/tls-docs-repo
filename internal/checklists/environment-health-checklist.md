# Environment Health Checklist

**Document type:** Checklist  
**Status:** v1  
**Use after:** [Bootstrap Environment SOP](../sops/deliver/infrastructure/bootstrap-environment.md) Phase 5 · before Configuration handoff · after major Upgrade  

Reusable verification that an environment's **platform wiring** works. Does **not** cover agency business configuration (ORI, officers, courts) — see [Bootstrap vs Configuration](../sops/deliver/infrastructure/bootstrap-vs-configuration.md).

Naming/URLs must match [Bootstrap Environment Standard](../sops/deliver/infrastructure/bootstrap-environment-standard.md).

---

## Identity

| Field | Value |
|-------|--------|
| AgencyName | |
| Environment | ★ dev · ★ test · ★ prod |
| FriendlyAgencyName | |
| VersionBranch / BuildId | |
| Checked by / date | |

---

## Checklist

### Azure / apps

- [ ] SQL database exists: `tls-{agency}-{env}-rms`
- [ ] API app exists: `tls-{agency}-{env}-api`
- [ ] UI app exists: `tls-{agency}-{env}-ui`
- [ ] File share exists: `tls-{agency}-{env}-fileshare`

### DNS / gateway / TLS

- [ ] UI hostname resolves / routes: `https://{agency}.thinline.app`
- [ ] API hostname resolves / routes: `https://{agency}-api.thinline.app`
- [ ] HTTPS / certificate OK in browser (no unexpected cert errors)
- [ ] App Gateway listeners present **or** intentional deferral documented

### Runtime

- [ ] **UI loads** (shell / login page)
- [ ] **API responds** (health or authenticated call as appropriate)
- [ ] **Login works** (Descope / agency context)
- [ ] **SQL reachable** from API (any authenticated data read that hits DB)
- [ ] **Directory reachable** (tenant config returned for this agency/env)
- [ ] **Descope working** (tenant exists; login completes)
- [ ] **File storage** usable (upload or known file path smoke test if required for go-live)

### Seed

- [ ] Agency display name reflects FriendlyAgencyName (when post-import ran)
- [ ] Baseline import completed (not empty unintended DB)

---

## Outcome

| Result | Next |
|--------|------|
| ★ Pass | Proceed to **Configuration** ([Bootstrap vs Configuration](../sops/deliver/infrastructure/bootstrap-vs-configuration.md)) |
| ★ Pass with deferrals | List deferrals (e.g. DNS): |
| ★ Fail | Stop; fix via Bootstrap SOP partial `-Steps` / escalate |

Deferrals / failures:

>

---

## Related documents

| Document | Role |
|----------|------|
| [Environment Inventory Standard](../sops/deliver/infrastructure/environment-inventory-standard.md) | What should exist |
| [Environment Lifecycle](../sops/deliver/infrastructure/environment-lifecycle.md) | When to re-run |
| [Hub Environment Integration](../sops/deliver/infrastructure/hub-environment-integration.md) | Future attach results to Hub |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — reusable environment health checks |
