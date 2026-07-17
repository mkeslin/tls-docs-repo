# Go-live runbook

**Document type:** SOP  
**Phase:** Deliver · lifecycle 7  
**Status:** v1  
**Audience:** Thin Line implementation · technical hats as assigned  
**Related:** [Go live](go-live.md) · [Go-live readiness assessment](../../assessments/go-live-readiness-assessment.md) · [Go-live decision record](../../templates/go-live-decision-record.md)

---

## Purpose

Execute a controlled cutover so the customer begins **production use** of Thin Line for agreed modules, with clear go/no-go, validation, triage, and rollback rules—then hand into **hypercare**.

Copy this runbook into the **engagement workspace** and fill times, names, and results there. Do not store customer-specific completion records in GitBook.

---

## Scope and assumptions

| Field | Value *(engagement copy)* |
|-------|---------------------------|
| Customer / agency | |
| Go-live modules | |
| Go-live environment | prod / other: |
| Planned cutover window | |
| Freeze applicable? | Yes / No |
| Final migration sync applicable? | Yes / No / N/A |
| Integrations in scope? | Yes / No / N/A |
| Hardware in scope? | Yes / No / N/A |
| Decision record outcome | Go / Conditional Go / No Go |

**Assumptions (confirm or adjust):**

1. [Go-live readiness assessment](../../assessments/go-live-readiness-assessment.md) is Complete (or Conditional Go conditions are listed and tracked).  
2. Prior phases are Complete or **Not applicable** per the lifecycle board.  
3. Specialist work (infrastructure, migration, configuration, integrations, training) may be performed by the **Implementation lead** unless separately assigned—see [Roles](implementation-roles-and-responsibilities.md).  
4. Configuration owns device **software settings**; Integrations and Hardware owns install, connectivity, compatibility, and end-to-end proof.  
5. Rollback is a last resort; triggers are agreed before cutover.

---

## Roles and communication channel

| Role | Name | Responsibility during cutover |
|------|------|-------------------------------|
| Thin Line cutover lead *(usually Implementation lead)* | | Owns checklist, go/no-go facilitation, triage |
| Thin Line technical support *(Infrastructure / Integrations hat)* | | Environment, integrations, devices |
| Thin Line migration support *(if applicable)* | | Final sync / migration checks |
| Customer project lead | | Customer communications, freeze compliance, user questions |
| Customer IT contact | | Network, device, identity issues on customer side |
| Customer acceptance authority | | Authorization; major go/no-go |
| Hypercare coverage (Thin Line) | | Post-cutover monitoring window |

**Primary communication channel for cutover day:** _______________  
**Backup channel:** _______________  
**Customer broadcast method** *(email / briefing / radio note—agency choice):* _______________

---

## Chronological execution checklist

Use engagement statuses for Result when useful: Complete · Blocked · Deferred · Not applicable.  
**Planned time** = planned clock time or sequence order (e.g. T−24h)—do not invent agency-specific times in the methodology copy.

| # | Task | Owner | Planned time | Actual completion | Result | Evidence or notes |
|---|------|-------|--------------|-------------------|--------|-------------------|
| | **A. Pre-cutover preparation** | | | | | |
| A1 | Confirm decision record is Go or Conditional Go; conditions listed | Cutover lead | | | | Decision record |
| A2 | Issue / reconfirm [Customer go-live and hypercare brief](../../../customer/implementation/go-live-and-hypercare-brief.md) | Cutover lead | | | | Sent copy |
| A3 | Confirm cutover team contacts and channel | Cutover lead | | | | |
| A4 | Confirm go-live cohort roster and admin coverage | Cutover lead + Customer project lead | | | | Roster |
| A5 | Stage runbook copy in workspace; assign hats | Cutover lead | | | | |
| | **B. Customer data freeze *(when applicable)*** | | | | | |
| B1 | Communicate freeze start (what stops in legacy / who may still read) | Customer project lead | | | | Brief / email |
| B2 | Confirm freeze observed (spot-check) | Customer project lead | | | | |
| B3 | Mark B\* **Not applicable** if no freeze | Cutover lead | | | | |
| | **C. Final migration or synchronization *(when applicable)*** | | | | | |
| C1 | Execute final sync / import per conversion plan | Migration hat | | | | Run log |
| C2 | Spot-check critical record counts / samples | Migration hat | | | | |
| C3 | Confirm exceptions unchanged or newly accepted | Migration hat + Customer AA | | | | |
| C4 | Mark C\* **Not applicable** if no migration sync | Cutover lead | | | | |
| | **D. Backup and recovery points** | | | | | |
| D1 | Confirm pre-cutover backup / restore point exists for go-live environment | Infrastructure hat | | | | Ticket / portal note (no secrets) |
| D2 | Record restore contact and approximate RTO expectation for the window | Infrastructure hat | | | | |
| | **E. Infrastructure health verification** | | | | | |
| E1 | Re-run critical items from [Environment health checklist](../../checklists/environment-health-checklist.md) on go-live environment | Infrastructure hat | | | | Checklist |
| E2 | Confirm URL, auth, and basic app load | Infrastructure hat | | | | |
| | **F. Configuration verification** | | | | | |
| F1 | Confirm modules, numbering, headers for go-live scope | Configuration hat | | | | Config checklist |
| F2 | Confirm device **software settings** (enables, print routes) for in-scope devices | Configuration hat | | | | |
| F3 | Confirm no last-minute config change without decision record update | Configuration hat | | | | |
| | **G. Integration and hardware verification** | | | | | |
| G1 | Re-test in-scope integrations required for day one | Integrations hat | | | | Matrix |
| G2 | Confirm device install/connectivity; print/scan/mobile smoke for go-live roles | Hardware hat | | | | Hardware checklist |
| G3 | Mark G\* **Not applicable** if none in scope | Cutover lead | | | | |
| | **H. User activation** | | | | | |
| H1 | Confirm go-live cohort accounts active with correct roles | Configuration hat | | | | |
| H2 | Spot-check login for at least one user per critical role | Cutover lead + Customer project lead | | | | |
| H3 | Confirm admin / approver access for day one | Configuration hat | | | | |
| | **I. Final smoke tests** | | | | | |
| I1 | Smoke each in-scope module family (create/open critical path) | Cutover lead | | | | Smoke notes |
| I2 | Search / find known sample (migrated or training) if applicable | Cutover lead | | | | |
| I3 | Confirm no Sev-1 defect open without workaround | Cutover lead | | | | Action register |
| | **J. Go/no-go meeting** | | | | | |
| J1 | Review readiness rollup and open blockers | Cutover lead | | | | Assessment |
| J2 | Confirm Thin Line recommendation still stands | Cutover lead | | | | |
| J3 | Obtain / reconfirm customer authorization | Customer acceptance authority | | | | Decision record |
| J4 | If No Go: stop; set next review; communicate delay | Cutover lead | | | | |
| | **K. Customer communication** | | | | | |
| K1 | Notify agency that cutover is proceeding (or delayed) | Customer project lead | | | | |
| K2 | Remind issue-reporting path and hypercare hours | Cutover lead | | | | Brief |
| | **L. Production cutover** | | | | | |
| L1 | Execute agreed exclusive-use steps (DNS, bookmarks, “use Thin Line” directive, legacy write freeze as planned) | Cutover lead + Customer project lead | | | | |
| L2 | Confirm users directed to production URL | Customer project lead | | | | |
| L3 | Record cutover complete timestamp | Cutover lead | | | | |
| | **M. Immediate post-cutover validation** | | | | | |
| M1 | Repeat critical smoke paths in production use | Cutover lead | | | | |
| M2 | Customer supervisor confirms staff can work | Customer project lead | | | | |
| M3 | Log issues found; severity | Cutover lead | | | | Action register |
| | **N. Issue triage** | | | | | |
| N1 | Triage new issues (workaround / fix / rollback evaluate) | Cutover lead | | | | |
| N2 | Escalate Sev-1 per contacts | Cutover lead | | | | |
| | **O. Rollback *(only if triggered)*** | | | | | |
| O1 | Declare rollback per triggers below | Cutover lead + Customer AA | | | | |
| O2 | Execute rollback steps (engagement-specific list) | Infrastructure / Migration hats | | | | |
| O3 | Communicate rollback to users; restore legacy posture as planned | Customer project lead | | | | |
| O4 | Schedule after-action and next go-live attempt | Cutover lead | | | | |
| | **P. Day-one monitoring** | | | | | |
| P1 | Monitor agreed channel through first production shift / window | Hypercare coverage | | | | |
| P2 | Check in with customer project lead at agreed intervals | Cutover lead | | | | |
| | **Q. Completion and handoff into hypercare** | | | | | |
| Q1 | Mark Phase 7 Complete on lifecycle board (or document rollback / No Go) | Cutover lead | | | | Workspace |
| Q2 | Open hypercare window (start time, duration, coverage) | Cutover lead | | | | Brief / workspace |
| Q3 | Transfer open cutover issues into hypercare tracking | Cutover lead | | | | Action register |
| Q4 | Confirm Customer Success aware hypercare started | Cutover lead | | | | |

---

## Rollback triggers and process

### Triggers *(engage Customer acceptance authority before declaring)*

Declare **rollback evaluation** when any of the following is true and cannot be mitigated quickly:

1. Production environment unavailable for the go-live cohort and not restorable within the agreed window.  
2. Data integrity failure that makes records unusable for required day-one work (especially after a final sync).  
3. Critical integration required for day-one public-safety workflow failed with no workaround.  
4. Customer acceptance authority orders stop / revert.  
5. Security incident that requires isolating the environment.

### Process

1. Cutover lead states the trigger and severity on the cutover channel.  
2. Customer acceptance authority confirms rollback vs continue-with-workaround.  
3. Execute engagement-specific rollback steps (restore point, DNS/bookmarks, legacy write re-enable as planned)—**list those steps in the workspace copy**, not in GitBook.  
4. Validate legacy or prior posture is usable.  
5. Record outcome on the decision record / action register; schedule next review.

Rollback is not a substitute for a **No Go** before cutover. Prefer No Go when readiness is incomplete.

---

## Issue severity *(cutover / day one)*

| Severity | Meaning | Response |
|----------|---------|----------|
| Sev-1 | Cannot perform required day-one work | Immediate triage; consider rollback |
| Sev-2 | Major workaround required | Fix or workaround same day if possible |
| Sev-3 | Limited impact | Track in hypercare |
| Sev-4 | Cosmetic / enhancement | Future enhancement / deferred |

---

## Completion criteria for this SOP

- [ ] Decision was Go or Conditional Go and conditions satisfied (or No Go / rollback recorded)  
- [ ] Checklist sections applicable to scope completed  
- [ ] Production use underway for agreed modules **or** explicit stop recorded  
- [ ] Hypercare window opened with named coverage **or** stop path documented  
- [ ] Engagement workspace updated; GitBook left as reusable methodology only  

---

## Related

| Document | Role |
|----------|------|
| [Go live](go-live.md) | Phase overview |
| [Go-live readiness assessment](../../assessments/go-live-readiness-assessment.md) | Phase gate |
| [Go-live decision record](../../templates/go-live-decision-record.md) | Authorization |
| [Customer go-live and hypercare brief](../../../customer/implementation/go-live-and-hypercare-brief.md) | Customer notice |
| [Hypercare and transition](hypercare-and-transition.md) | Next phase |
| [Environment health checklist](../../checklists/environment-health-checklist.md) | Infra verify |
| [Hardware readiness checklist](../../checklists/hardware-readiness-checklist.md) | Device proof |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — initial go-live runbook |
