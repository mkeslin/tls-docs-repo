# Go-live decision record

**Document type:** Template  
**Phase:** Deliver · lifecycle 7  
**Status:** v1  
**Audience:** Thin Line implementation · customer final acceptance authority  

Complete this in the **engagement workspace** after (or with) the [Go-live readiness assessment](../assessments/go-live-readiness-assessment.md). Do not store filled customer decisions permanently in GitBook.

---

## Header

| Field | Value |
|-------|--------|
| **Customer / agency** | |
| **Planned go-live date / window** | |
| **Assessment date** | |
| **Decision meeting date** | |
| **Products / modules in scope** | |
| **Environment** | |
| **Linked readiness assessment** | |
| **Linked action register** | |

---

## Readiness summary

| Area | Status | Blocking open? | Notes |
|------|--------|:--------------:|-------|
| Project and scope | | ☐ | |
| Infrastructure | | ☐ | |
| Data migration | | ☐ / N/A | |
| Configuration | | ☐ | |
| Integration and hardware | | ☐ / N/A | |
| User and access | | ☐ | |
| Training | | ☐ | |
| Operational | | ☐ | |
| Support and communications | | ☐ | |
| Risk and exception | | ☐ | |
| Cutover and rollback | | ☐ | |

**Narrative summary (3–5 sentences):**

>

---

## Blocking issues

List any blocking criteria still incomplete. If none, write **None**.

| ID / criterion | Description | Owner | Mitigation or waiver? |
|----------------|-------------|-------|------------------------|
| | | | |
| | | | |

---

## Accepted exceptions

Authorized exceptions that allow proceed despite incomplete non-waived items—or waived blockers with approval.

| Exception | Residual risk | Approved by | Date |
|-----------|---------------|-------------|------|
| | | | |
| | | | |

---

## Remaining risks

| Risk | Likelihood *(H/M/L)* | Impact | Owner | Plan |
|------|----------------------|--------|-------|------|
| | | | | |
| | | | | |

---

## Thin Line recommendation

| Field | Value |
|-------|--------|
| **Recommendation** | ☐ Go · ☐ Conditional Go · ☐ No Go |
| **Recommended by** | Name / role (Implementation lead required) |
| **Date** | |
| **Consulted** | |
| **Rationale** | |

This is **not** customer authorization.

---

## Customer authorization

| Field | Value |
|-------|--------|
| **Authorization** | ☐ Authorize Go · ☐ Authorize Conditional Go · ☐ No Go |
| **Authorized by** | Name / title (Final acceptance authority required) |
| **Date** | |
| **Customer project lead acknowledgment** | |

Production use must not begin without customer authorization.

---

## Decision

| Field | Value |
|-------|--------|
| **Decision** | ☐ **Go** · ☐ **Conditional Go** · ☐ **No Go** |
| **Effective for planned go-live** | Yes / No / Revised date: ________ |

| Decision | Meaning |
|----------|---------|
| **Go** | Proceed with cutover as planned |
| **Conditional Go** | Proceed only if [Conditions](#conditions) are satisfied |
| **No Go** | Do not begin production use; complete [Next review](#next-review-if-no-go) |

---

## Conditions

*Required for Conditional Go; optional notes for Go.*

| # | Condition | Must be done by | Owner | Status |
|---|-----------|-----------------|-------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## Decision makers

| Role | Name | Present / recorded approval |
|------|------|-----------------------------|
| Thin Line implementation lead | | ☐ |
| Thin Line technical consult *(if any)* | | ☐ |
| Customer final acceptance authority | | ☐ |
| Customer project lead | | ☐ |
| Customer executive sponsor *(if required)* | | ☐ |
| Other | | ☐ |

---

## Sign-off or recorded approval

| Party | Signature / email confirmation reference | Date |
|-------|------------------------------------------|------|
| Thin Line recommendation | | |
| Customer authorization | | |

Electronic approval (email, signed PDF, or workspace acknowledgment) is acceptable. Paste **references**, not passwords or secrets.

---

## Next review if No Go

| Field | Value |
|-------|--------|
| **Next review date** | |
| **Owner to reconvene** | |
| **What must change before re-assessment** | |
| **Staff communication plan** | Customer project lead will… |

---

## After the decision

| If | Then |
|----|------|
| **Go** or conditions met for **Conditional Go** | Execute [Go-live runbook](../sops/deliver/go-live-runbook.md); issue/update [Customer go-live and hypercare brief](../../customer/implementation/go-live-and-hypercare-brief.md) |
| **No Go** | Do not cut over; update lifecycle board; notify staff via customer project lead |
| **Rollback after start** | Record outcome here or in a linked addendum; schedule next review |

---

## Related

- [Go-live readiness assessment](../assessments/go-live-readiness-assessment.md)  
- [Go-live runbook](../sops/deliver/go-live-runbook.md)  
- [Go live](../sops/deliver/go-live.md)  
- [Implementation action register](../../customer/implementation/implementation-action-register.md)  

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — initial template |
