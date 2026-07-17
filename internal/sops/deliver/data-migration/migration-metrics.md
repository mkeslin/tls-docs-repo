# Migration Metrics

**Document type:** Reference  
**Status:** v1 â€” lightweight  
**Audience:** Implementation Lead Â· leadership

Purpose: know whether **packages are improving**, not build a heavy BI program.

---

## What to track (minimum)

Per accepted conversion (or at close-out), record:

| Metric | Where to capture |
|--------|------------------|
| Customer / agency | Assessment Â· `ConvertedAgencies.md` |
| Vendor + **package VERSION** | Assessment Â· register |
| Conversion date | `ConvertedAgencies.md` |
| Status (Completed / Partial) | Register |
| Approx. Thin Line hours (implementation) | <mark style="color:red;">**TODO:**</mark> choose home (assessment close-out vs simple sheet) |
| Reruns (count of full/partial re-imports) | Close-out notes |
| Material bugs found post-import | Exception report / close-out |
| Package improvements promoted? | Assessment Â§ Knowledge / package backlog |
| Engineering package work (hours or Y/N) | Assessment |

Optional later: average hours by vendor, defect rate by `VERSION`, attachment failure rate.

---

## Sources of truth (today)

| Source | Holds |
|--------|-------|
| Vendor `ConvertedAgencies.md` | Agency Â· date Â· VERSION Â· status |
| [Legacy System Migration Assessment](../../../assessments/legacy-system-migration-assessment.md) | Scope Â· risk Â· package backlog |
| Conversion summary / exception list | Counts Â· defects |
| <mark style="color:red;">**TODO:**</mark> | Single rollup sheet or Hub registry for hours / reruns |

Do **not** invent a second competing register of agencies. Extend `ConvertedAgencies.md` + assessment close-out first.

---

## Review cadence

| Cadence | Question |
|---------|----------|
| After each conversion | Did package VERSION improve? Backlog items closed? |
| Quarterly | Hours / reruns trend by vendor; which packages are draft vs current? |

See [Migration Architecture](migration-architecture.md) â€” metrics feed **package improvement**.

---

## Related documents

| Document | Role |
|----------|------|
| [Migration Package Standards](vendor-packages/migration-package-standards.md) | VERSION / backlog |
| [Migration Validation Standard](migration-validation-standard.md) | Quality bar |
| [Migration Pricing Policy](../../../policies/migration-pricing.md) | Commercial outcomes |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 â€” lightweight metric set |
