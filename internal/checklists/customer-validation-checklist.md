# Customer Validation Checklist

**Document type:** Checklist  
**Status:** v1  
**Referenced by:** [Legacy System Migration](../sops/deliver/data-migration/legacy-system-migration.md) (Phase 8) Â· [Migration Validation Standard](../sops/deliver/data-migration/migration-validation-standard.md) (Layer C)

Thin Line completes **technical validation** (counts, relationships, spot checks) before inviting the customer. This checklist is what the **customer** walks for acceptance.

---

## Before the customer starts

Implementation confirms:

- [ ] [Migration Validation Standard](../sops/deliver/data-migration/migration-validation-standard.md) Layers Aâ€“B complete for agreed scope  
- [ ] [Post-Conversion Utilities](../sops/deliver/data-migration/post-conversion-utilities.md) run where required  
- [ ] Customer has URL, login, and list of sample record numbers (optional but helpful)  
- [ ] Exception report shared for any accepted known gaps  

---

## Customer checks (by module in scope)

Adjust to the modules on the assessment. For each in-scope module:

### Incidents / cases

- [ ] Can find a known historical case by number or name  
- [ ] Case opens; narrative / offenses / persons look reasonable  
- [ ] No obvious missing years that should have been converted  

### Citations / court (if in scope)

- [ ] Known citation / case opens  
- [ ] Defendant and violation information present  
- [ ] Status looks usable for day-to-day work  

### CAD / calls (if in scope)

- [ ] Known call opens  
- [ ] Location / persons / vehicles present when expected  

### Warrants / other modules (if in scope)

- [ ] Sample records open and look complete enough to work  

### Attachments (if in scope)

- [ ] Spot-check that expected files open or that missing files were disclosed  

### Search / day-one confidence

- [ ] Search returns expected hits for a few known people or cases  
- [ ] Nothing blocking go-live training / use that was promised in scope  

---

## Exceptions

List anything wrong or incomplete:

| # | What | Module | OK to accept? |
|---|------|--------|---------------|
| 1 | | | â˜ Yes Â· â˜ No â€” fix first |

---

## Acknowledgement

| Field | Value |
|-------|-------|
| Agency | |
| Validator name | |
| Date | |
| Outcome | â˜ Accepted Â· â˜ Accepted with exceptions Â· â˜ Not accepted â€” rework needed |

Formal form (target): [Customer Acceptance Form](../templates/customer-acceptance-form.md).

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Placeholder |
| 2026-07-17 | v1 â€” customer-facing checks aligned with Validation Standard |
