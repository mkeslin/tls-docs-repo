# Migration Validation Standard

**Document type:** Standard  
**Status:** v1  
**Audience:** Implementation Â· Engineering Â· anyone signing off a conversion

This document answers: **How do we know a migration succeeded?**

It is **not** how to migrate. Execution: [Legacy System Migration](legacy-system-migration.md). Customer-facing steps: [Customer Validation Checklist](../../../checklists/customer-validation-checklist.md).

Reusable for **every** vendor package.

---

## Definition of success

A migration is successful when **all** of the following are true for the agreed scope:

1. **Coverage** â€” In-scope modules have expected record presence (not empty when source had data).  
2. **Integrity** â€” Critical relationships hold; orphans and broken FKs are understood or fixed.  
3. **Usability** â€” Sample records open in Thin Line UI after [post-conversion utilities](post-conversion-utilities.md) where required.  
4. **Traceability** â€” Converted rows carry agreed import / conversion tagging where the package uses it.  
5. **Acceptance** â€” Customer has had a chance to validate and has acknowledged (informal today; formal form in target state).

â€œPipeline finished without SQL errorsâ€ is **necessary but not sufficient**.

---

## Validation layers

| Layer | Owner | When |
|-------|-------|------|
| **A. Technical (Thin Line)** | Implementation / Engineering | Immediately after import (+ utilities) |
| **B. Spot checks (Thin Line)** | Implementation | Before inviting customer |
| **C. Customer validation** | Customer + Implementation support | Phase 8 |
| **D. Acceptance** | Customer | Close of validation window |

---

## A. Technical checks (required)

Run against the **target** database (UAT or Production per engagement decision). Adjust module list to assessment scope.

### A1. Record counts

Compare **source (or staging)** vs **Thin Line** for each in-scope entity. Exact 1:1 is not always required (filters, voids, duplicates)â€”document deltas.

| Entity (examples) | Source / staging count | Thin Line count | Delta / notes |
|-------------------|------------------------:|----------------:|---------------|
| Incidents | | | |
| Citations | | | |
| CAD calls | | | |
| Persons (masters or involvements) | | | |
| Vehicles | | | |
| Warrants | | | |
| Property / evidence | | | |
| Attachments / binary refs | | | |
| Officers / users mapped | | | |

**Pass:** Counts are explained; unexplained gaps are treated as defects.

### A2. Relationships

Spot-query or script checks for critical links (examples; vendor packages may add more):

| Check | Intent |
|-------|--------|
| Incident â†’ primary offense / involvements | No silent loss of core case structure |
| Citation â†’ person / violation where expected | Court / RMS usability |
| Call â†’ location / units when source had them | CAD usability |
| Converted row â†’ AgencyId | Correct tenant agency |
| Master snapshot FKs on calls after utilities | Post-snapshot integrity |

**Pass:** No material orphan rate without documented exception list.

### A3. Orphan / broken reference detection

At minimum, sample or query for:

- Module rows pointing at missing master persons/vehicles/locations  
- History / child rows with missing parent  
- Attachments with missing parent or missing blob/path  

**Pass:** Orphans are zero, or listed in an exception report with disposition (fix / accept / defer).

### A4. Duplicate detection (lightweight)

| Check | Notes |
|-------|-------|
| Duplicate incident / citation / call numbers in scope | Unexpected dupes = defect |
| Duplicate master persons created by conversion | May need merge later; flag volume |

**Pass:** Unexpected duplicates explained or fixed.

### A5. Attachments

If attachments were in scope:

- [ ] Count of attachment rows vs source expectation  
- [ ] Sample open / download in UI or storage path  
- [ ] Known failures listed (missing files from vendor export)

### A6. Conversion tagging

Where the package sets `ImportSource` / `ConvertedOn` / `ConversionSource`:

- [ ] In-scope converted rows are tagged as agreed  
- [ ] After [Post-Conversion Utilities](post-conversion-utilities.md), workflow / snapshot state matches that SOP

---

## B. Spot checks (required before customer)

Pick a small set of **known real cases** from the agency (not only Id = 1):

| Module | Checks |
|--------|--------|
| Incident | Opens; narrative/offenses present; persons linked; workflow usable after utilities |
| Citation | Opens; defendant/violation; Issued path after utilities |
| Call | Opens; masters present after snapshot utility |
| Warrant / Notepad | Opens; Completed after utilities if applicable |
| Search | Find by number / name returns expected hit |

Document which samples were used (numbers / dates) on the conversion summary.

---

## C. Customer validation

Customer walks [Customer Validation Checklist](../../../checklists/customer-validation-checklist.md) (or equivalent email checklist today).

Thin Line supports questions; material defects return to Implementation for fix / re-run.

---

## D. Acceptance

| Today | Target |
|-------|--------|
| Email acknowledgement / informal sign-off | [Customer Acceptance Form](../../../templates/customer-acceptance-form.md) |

Do not mark `ConvertedAgencies.md` **Completed** until acceptance criteria for this engagement are met (or status is explicitly Partial with notes).

---

## Exception report (minimum)

Every engagement should produce a short exception list:

| Item | Module | Severity | Disposition |
|------|--------|----------|-------------|
| â€¦ | â€¦ | Blocker / Major / Minor | Fixed / Accepted / Deferred |

Blockers prevent acceptance. Accepted exceptions need customer awareness.

---

## Vendor-specific additions

Vendor guides may add checks (e.g. court docket fields, FoxPro memo quirks). Those **add to** this standard; they do not replace layers Aâ€“D.

See [Vendor Conversion Guides](vendor-packages/vendor-conversion-guides/README.md).

---

## What we do not require (yet)

Leave these as future maturityâ€”not blockers for v1 of this standard:

- Fully automated schema-diff scorecard in Hub  
- Perfect person-dedup across the entire master index  
- Bit-identical binary parity for every historical attachment when the vendor export was incomplete  

Track package improvements that close these gaps in the [package backlog](migration-package-standards.md#package-backlog).

---

## Related documents

| Document | Role |
|----------|------|
| [Migration Architecture](migration-architecture.md) | Where validation sits |
| [Post-Conversion Utilities](post-conversion-utilities.md) | Workflow / snapshot before usability checks |
| [Conversion Summary](../../../templates/conversion-summary.md) | Record counts / exceptions |
| [Migration Metrics](migration-metrics.md) | Reruns / defects over time |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 â€” reusable success criteria and check layers |
