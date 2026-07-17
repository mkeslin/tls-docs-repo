# Preliminary implementation plan

**Audience:** Your agency’s project team · Thin Line implementation team  
**Purpose:** Share a working plan **after discovery** and **before** all technical assessments are complete  
**Reusable template:** Replace header fields and section values for each engagement. Do not invent firm dates or commitments where assessment is still required.

---

## Document control

| Field | Value |
|-------|--------|
| **Customer / agency** | |
| **Plan version** | Preliminary · v____ |
| **Date issued** | |
| **Prepared by (Thin Line)** | |
| **Customer project lead** | |
| **Based on** | Kickoff · working session · notes dated ________ |
| **Next formal update expected** | |

### Confidence legend

Use these labels everywhere a fact, date, or commitment appears:

| Label | Meaning |
|-------|---------|
| **Confirmed** | Agreed by both parties; safe to plan around unless change control applies |
| **Preliminary** | Best current understanding from discovery; may change after assessment or further sessions |
| **Pending assessment** | Cannot commit until a named assessment or technical review finishes |
| **Out of scope** | Explicitly not part of this engagement (or deferred to a later phase/contract) |

**Rule:** If a milestone depends on migration, integrations, hardware, or vendor work that is not yet assessed, mark the date **Pending assessment** (or leave blank) and name the dependency—do not invent a firm commitment.

---

## 1. Customer

| Field | Value | Confidence |
|-------|--------|------------|
| Legal / customer name | | Confirmed / Preliminary |
| Agency display name | | Confirmed / Preliminary |
| County / state | | Confirmed / Preliminary |
| Primary site / location | | Confirmed / Preliminary |
| Preferred site URL *(if any)* | | Confirmed / Preliminary / TBD by Thin Line |

---

## 2. Products and modules

Check only what applies. Mark confidence for the engagement as a whole.

| Product / module | In this engagement? | Confidence |
|------------------|:-------------------:|------------|
| RMS | ☐ | Confirmed / Preliminary / Out of scope |
| CAD | ☐ | Confirmed / Preliminary / Out of scope |
| Mobile citations | ☐ | Confirmed / Preliminary / Pending assessment / Out of scope |
| Evidence / property | ☐ | Confirmed / Preliminary / Out of scope |
| Jail | ☐ | Confirmed / Preliminary / Out of scope |
| Court | ☐ | Confirmed / Preliminary / Out of scope |
| Code enforcement | ☐ | Confirmed / Preliminary / Out of scope |
| Other: _______________ | ☐ | |

**Notes on modules**

-

---

## 3. Project objectives

| # | Objective | Confidence |
|---|-----------|------------|
| 1 | | Confirmed / Preliminary |
| 2 | | Confirmed / Preliminary |
| 3 | | Confirmed / Preliminary |

---

## 4. Known scope

### In scope *(working understanding)*

| Item | Confidence |
|------|------------|
| | Confirmed / Preliminary |
| | Confirmed / Preliminary |
| | Confirmed / Preliminary |

### Boundary notes

| Topic | Notes | Confidence |
|-------|--------|------------|
| What “day one” must include | | Preliminary / Pending assessment |
| What can wait until after go-live | | Preliminary |

---

## 5. Assumptions

List assumptions the plan depends on. If an assumption fails, dates and scope may change.

| # | Assumption | If wrong, impact | Confidence |
|---|------------|------------------|------------|
| A1 | | | Preliminary |
| A2 | | | Preliminary |
| A3 | | | Preliminary |

---

## 6. Dependencies

| # | Dependency | Needed for | Owner | Status | Confidence |
|---|------------|------------|-------|--------|------------|
| D1 | | | Customer / Thin Line / Vendor | Open / In progress / Done | Confirmed / Preliminary / Pending assessment |
| D2 | | | | | |
| D3 | | | | | |

---

## 7. Proposed implementation phases

High-level sequence only. Detail lives in the milestone table below.

| Phase | Applies? | Outcome (one line) | Confidence |
|-------|:--------:|--------------------|------------|
| Kickoff and discovery | ☐ | Alignment and working plan | Confirmed / Preliminary |
| Infrastructure | ☐ | Environment ready for configuration | Confirmed / Preliminary / Pending assessment |
| Data migration | ☐ / N/A | Converted history accepted—or N/A | Pending assessment / Out of scope / Preliminary |
| Configuration | ☐ | Agency configured for go-live scope | Preliminary |
| Integrations and hardware | ☐ / N/A | Required connections and devices ready—or N/A | Pending assessment / Out of scope / Preliminary |
| Training | ☐ | Users ready for go-live cohort | Preliminary |
| Go live | ☐ | Production use begins | Preliminary / Pending assessment |
| Hypercare and transition | ☐ | Stable operations; handoff to support model | Preliminary |

---

## 8. Target milestone windows

Use **windows** (e.g. “week of…”, “month of…”) or **TBD**. Prefer **Pending assessment** over a fake date.

| Phase | Outcome | Target start | Target completion | Owner | Dependencies | Status |
|-------|---------|--------------|-------------------|-------|--------------|--------|
| Kickoff and discovery | Discovery complete; preliminary plan shared | | | Thin Line + Customer | | ☐ Not started · ☐ In progress · ☐ Complete |
| Infrastructure | Environment available for configuration | | | Thin Line | Preferred URL / naming inputs | ☐ Not started · ☐ In progress · ☐ Complete · ☐ Pending assessment |
| Data migration | Migration accepted **or** marked N/A | TBD / N/A | TBD / N/A | Thin Line + Customer | Formal migration assessment; source access | ☐ N/A · ☐ Pending assessment · ☐ In progress · ☐ Complete |
| Configuration | Configuration approved for go-live scope | | | Thin Line + Customer | Infrastructure; migration posture | ☐ Not started · ☐ In progress · ☐ Complete |
| Integrations and hardware | Required integrations/devices ready **or** N/A | TBD / N/A | TBD / N/A | Thin Line + Customer / IT | Device plan; vendor access | ☐ N/A · ☐ Pending assessment · ☐ In progress · ☐ Complete |
| Training | Go-live cohort trained | | | Thin Line + Customer | Configuration stable enough to train | ☐ Not started · ☐ In progress · ☐ Complete |
| Go live | Production cutover | TBD | TBD | Customer acceptance + Thin Line | Training; blocking risks closed | ☐ Pending assessment · ☐ Planned · ☐ Complete |
| Hypercare | Hypercare complete; transition agreed | | | Thin Line + Customer | Successful go-live | ☐ Not started · ☐ In progress · ☐ Complete |

**Milestone confidence (overall timeline):** ☐ Preliminary · ☐ Pending assessment · ☐ Confirmed *(only after assessments and mutual agreement)*

---

## 9. Customer responsibilities

| Responsibility | When | Confidence |
|----------------|------|------------|
| Provide a single project lead and decision path | Ongoing | Confirmed / Preliminary |
| Attend scheduled working sessions | Per calendar | Confirmed / Preliminary |
| Deliver requested artifacts (logos, rosters, exports) when asked | As requested | Confirmed / Preliminary |
| Validate migrated data *(if migration in scope)* | During migration | Pending assessment / Out of scope |
| Confirm configuration decisions and approve go-live readiness | Configuration / go-live | Preliminary |
| Coordinate staff for training and cutover | Training / go-live | Preliminary |
| Other: | | |

---

## 10. Thin Line responsibilities

| Responsibility | When | Confidence |
|----------------|------|------------|
| Lead implementation coordination and facilitation | Ongoing | Confirmed / Preliminary |
| Provision and maintain the implementation environment | Infrastructure | Confirmed / Preliminary |
| Guide configuration using defaults + exceptions | Configuration | Confirmed / Preliminary |
| Conduct or coordinate migration assessment and conversion *(if in scope)* | Migration | Pending assessment / Out of scope |
| Support integrations and hardware readiness *(as in scope)* | Integrations | Pending assessment / Out of scope |
| Deliver agreed training | Training | Preliminary |
| Support go-live and hypercare | Go-live / hypercare | Preliminary |
| Other: | | |

---

## 11. Data migration status

| Field | Value |
|-------|--------|
| **Status** | ☐ Out of scope · ☐ Pending assessment · ☐ Assessment scheduled · ☐ In progress · ☐ Complete / accepted · ☐ N/A |
| **Confidence** | Confirmed / Preliminary / Pending assessment / Out of scope |
| **Source system(s)** | |
| **What history is desired on day one** *(preliminary)* | |
| **Known exclusions / redaction needs** | |
| **Customer validation contact** | |
| **Assessment / pricing note** | Firm migration scope, timeline, and pricing require a **formal migration assessment**. Until then, milestone dates for migration and go-live remain **Pending assessment**. |

---

## 12. Integration and hardware status

| Field | Value |
|-------|--------|
| **Status** | ☐ Out of scope · ☐ Pending assessment · ☐ Discovery only · ☐ In progress · ☐ Ready for go-live · ☐ N/A |
| **Confidence** | Confirmed / Preliminary / Pending assessment / Out of scope |

| Item | Needed? | Status | Confidence | Notes |
|------|---------|--------|------------|-------|
| Mobile printers | Y / N / Maybe / N/A | | | |
| Barcode / label devices | Y / N / Maybe / N/A | | | |
| MDTs / field devices | Y / N / Maybe / N/A | | | |
| Court / payments / other vendors | Y / N / Maybe / N/A | | | |
| State / CJIS connectivity | Y / N / Maybe / N/A | | | |
| Other | | | | |

**IT / device contact:** _______________

---

## 13. Training approach

| Field | Value | Confidence |
|-------|--------|------------|
| Training coordinator (customer) | | Preliminary / Confirmed |
| Audiences | | Preliminary |
| Format *(on-site / remote / mix)* | | Preliminary |
| Timing relative to go-live | Before / staggered / TBD | Preliminary / Pending assessment |
| Materials approach | Thin Line standard workshops + agency-specific notes | Preliminary |

---

## 14. Go-live approach

| Field | Value | Confidence |
|-------|--------|------------|
| Target go-live window | TBD / week of… / month of… | Preliminary / Pending assessment |
| Cutover style *(single cutover / phased modules / parallel run)* | | Preliminary |
| Acceptance authority (customer) | | Confirmed / Preliminary |
| Fallback if a blocker appears | Delay go-live / reduce day-one scope / other | Preliminary |
| Hypercare expected length *(working)* | | Preliminary |

**Do not treat a target window as a commitment** while migration, integrations, or hardware remain **Pending assessment**.

---

## 15. Known risks

| # | Risk | Impact | Likelihood *(H/M/L)* | Owner | Mitigation / next step | Confidence |
|---|------|--------|----------------------|-------|------------------------|------------|
| R1 | | | | | | Preliminary |
| R2 | | | | | | Preliminary |
| R3 | | | | | | Preliminary |

---

## 16. Open decisions

| # | Decision needed | Options / notes | Who decides | Needed by | Blocks |
|---|-----------------|-----------------|-------------|-----------|--------|
| O1 | | | | | Migration / Config / Go-live / Other |
| O2 | | | | | |
| O3 | | | | | |

---

## 17. Exclusions

Items that are **Out of scope** for this engagement (or deferred). Listing them here prevents silent scope creep.

| # | Exclusion | Deferred to *(later phase / future purchase / never)* | Confidence |
|---|-----------|--------------------------------------------------------|------------|
| E1 | | | Out of scope |
| E2 | | | Out of scope |
| E3 | | | Out of scope |

---

## 18. Change-control statement

This document is a **preliminary plan**, not a fixed contract schedule.

- **Confirmed** items may still change if both parties agree, or if a dependency fails.  
- **Preliminary** items are expected to tighten after working sessions and assessments.  
- **Pending assessment** items must not be treated as delivery commitments until the assessment is complete and results are accepted.  
- Material changes to products, migration scope, integrations, training volume, or go-live date should be recorded as an explicit decision (who approved, when) and reflected in the next plan version.  
- Commercial or contract changes follow your Thin Line agreement and order process—this plan does not amend pricing by itself.

| Field | Value |
|-------|--------|
| Customer acknowledgment of preliminary nature | ☐ Discussed · ☐ Acknowledged |
| Thin Line implementation lead | |
| Date | |

---

## 19. Next steps

Immediate actions only. Prefer owners and dates that are real; otherwise mark **TBD**. Track ongoing work in the [Implementation action register](implementation-action-register.md).

### Customer next steps

| # | Action | Owner | Due | Confidence |
|---|--------|-------|-----|------------|
| C1 | | | | Confirmed / Preliminary |
| C2 | | | | |
| C3 | | | | |

### Thin Line next steps

| # | Action | Owner | Due | Confidence |
|---|--------|-------|-----|------------|
| T1 | | | | Confirmed / Preliminary |
| T2 | | | | |
| T3 | | | | |

### Assessments to schedule

| Assessment | Needed? | Target to schedule by | Status |
|------------|---------|----------------------|--------|
| Data migration assessment | Y / N / Maybe | | ☐ Not needed · ☐ To schedule · ☐ Scheduled · ☐ Complete |
| Hardware / device validation | Y / N / Maybe | | ☐ Not needed · ☐ To schedule · ☐ Scheduled · ☐ Complete |
| Integration discovery (IT / vendors) | Y / N / Maybe | | ☐ Not needed · ☐ To schedule · ☐ Scheduled · ☐ Complete |

---

## Related

- [Implementation kickoff agenda](implementation-kickoff-agenda.md)  
- [Implementation action register](implementation-action-register.md)  
- [Customer implementation workbook](customer-implementation-workbook.md)  
- [Configuration discovery workbook](configuration-discovery-workbook.md)  
- [Getting started](../getting-started/README.md) · [Training](../training/README.md)  

*Thin Line Software · Preliminary implementation plan · Customer-facing · Reusable*
