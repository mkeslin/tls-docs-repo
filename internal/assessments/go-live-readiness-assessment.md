# Go-live readiness assessment

**Document type:** Assessment  
**Phase:** Deliver · lifecycle 7  
**Status:** v1  
**Related:** [Go live](../sops/deliver/go-live.md) · [Go-live runbook](../sops/deliver/go-live-runbook.md) · [Go-live decision record](../templates/go-live-decision-record.md)

---

## Purpose

Provide the **formal phase gate** that determines whether a customer is ready to begin **production use** of Thin Line for the agreed modules.

This assessment is completed in the **engagement workspace** (copy or linked form)—not filled as a permanent customer record inside GitBook.

**Required outputs:**

1. Completed readiness rows (or **Not applicable** / authorized **Deferred** with exception)  
2. [Go-live decision record](../templates/go-live-decision-record.md) with two distinct decisions:  
   - **Thin Line go-live recommendation**  
   - **Customer authorization** to begin production use  

---

## Document vs engagement status

| Kind | Examples | Where used |
|------|----------|------------|
| **Document maturity** | Placeholder · Draft · v1 | GitBook page header only |
| **Engagement status** | Not started · Waiting on customer · Waiting on Thin Line · In progress · Blocked · Ready for validation · Complete · Deferred · Not applicable | Assessment rows, workspace, action register |

Do not use Placeholder/Draft as row statuses on an engagement.

---

## Engagement header

| Field | Value |
|-------|--------|
| **Customer / agency** | |
| **Assessment date** | |
| **Planned go-live date / window** | |
| **Products / modules in go-live scope** | |
| **Thin Line implementation lead** | |
| **Customer project lead** | |
| **Customer final acceptance authority** | |
| **Environment** *(prod / other)* | |
| **Migration in scope?** | Yes / No / N/A |
| **Integrations / hardware in scope?** | Yes / No / N/A |
| **Assessment prepared by** | |
| **Linked workspace / action register** | |

---

## How to complete each row

| Column | Meaning |
|--------|---------|
| **Criterion** | What must be true |
| **Evidence or linked artifact** | Checklist, workbook, URL, decision ID, or file link in the workspace—not pasted secrets |
| **Owner** | One person accountable for this criterion |
| **Status** | One engagement status from the list below |
| **Exception or risk** | Blank if none; otherwise short note + action-register ID |
| **Required approver** | Who must accept this criterion (may match Owner for Thin Line-only items) |

### Allowed engagement statuses

| Status | Meaning |
|--------|---------|
| **Not started** | Not yet addressed |
| **Waiting on customer** | Blocked on customer action |
| **Waiting on Thin Line** | Blocked on Thin Line action |
| **In progress** | Active work |
| **Blocked** | Cannot proceed; must link a blocker |
| **Ready for validation** | Owner believes done; awaiting check or acceptance |
| **Complete** | Criterion met |
| **Deferred** | Intentionally postponed with authorized exception (see Blocking rules) |
| **Not applicable** | Out of scope for this go-live |

---

## Blocking criteria

A customer **must not** be marked ready for production use while any **blocking** criterion is incomplete—unless an **authorized exception** is documented (exception text, approver, and residual risk on the [decision record](../templates/go-live-decision-record.md)).

### Always blocking (when the area applies)

| ID | Blocking rule |
|----|---------------|
| B-SCOPE | Go-live module scope is not agreed in writing |
| B-AUTH | Customer final acceptance authority is unnamed |
| B-INFRA | Production (or agreed go-live) environment has not passed health verification |
| B-MIG | Migration is in scope and acceptance is not recorded (or N/A not recorded) |
| B-CFG | Configuration checklist incomplete for go-live scope without authorized deferral |
| B-INT | In-scope integration or hardware proof incomplete without authorized deferral |
| B-USER | Go-live cohort cannot log in with correct roles |
| B-TRAIN | Agreed training audiences incomplete without authorized deferral and makeup plan |
| B-OPS | No named coverage for day-one operations / issue reporting |
| B-COMM | Customer go-live brief not issued (or equivalent written notice) |
| B-CUT | Cutover / freeze / rollback approach not agreed when applicable |
| B-DEC | Thin Line recommendation **or** customer authorization missing |

### May be Deferred only with authorization

Non-blocking nice-to-haves, post-go-live enhancements, and explicitly accepted gaps may be **Deferred** if:

1. They are **not** in the Always blocking list (or a waiver is signed by the Required approver + customer AA for that item), and  
2. Residual risk is listed on the decision record, and  
3. An owner and follow-up exist in the [action register](../../customer/implementation/implementation-action-register.md).

**Product gaps** are not closed by go-live alone—track as type Product gap; go-live may proceed only if workaround or acceptance is recorded.

---

## 1. Project and scope readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Purchased products and go-live modules agreed | Contract / preliminary plan / workspace scope | Implementation lead | | | Implementation lead + Customer project lead | Yes |
| Explicit out-of-scope / later-phase items listed | Preliminary plan § Exclusions / workspace | Implementation lead | | | Customer project lead | Yes |
| Target go-live window agreed (or Conditional Go conditions clear) | Preliminary plan / decision record | Implementation lead | | | Customer acceptance authority | Yes |
| Open commercial disputes closed or escalated | Handoff / Sales notes | Sales owner | | | Thin Line executive sponsor (if open) | Yes if open dispute |
| Action register reviewed; no unmanaged blockers | Action register | Implementation lead | | | Implementation lead | Yes |

---

## 2. Infrastructure readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Go-live environment exists and matches bootstrap standard | Environment inventory / bootstrap notes | Implementation lead *(Infrastructure hat)* | | | Implementation lead | Yes |
| [Environment health checklist](../checklists/environment-health-checklist.md) passed on go-live environment | Completed checklist link | Implementation lead *(Infrastructure hat)* | | | Implementation lead | Yes |
| Production URL / access path confirmed for users | Customer brief / workspace | Implementation lead | | | Customer project lead | Yes |
| Backup / recovery point identified for cutover window | Runbook prep notes | Implementation lead *(Infrastructure hat)* | | | Implementation lead | Yes |
| Secrets and admin access available to cutover team | Internal secure store (do not paste here) | Implementation lead | | | Implementation lead | Yes |

---

## 3. Data migration readiness

*If migration is out of scope, mark every row **Not applicable** and record N/A on the decision record.*

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Migration in/out of scope recorded | Workspace / assessment | Implementation lead | | | Customer project lead | Yes |
| Approved conversion plan (when migration used) | [Legacy system migration assessment](legacy-system-migration-assessment.md) | Data migration owner *(hat)* | | | Implementation lead | Yes if migrating |
| Technical validation complete for agreed scope | Validation standard evidence | Data migration owner *(hat)* | | | Implementation lead | Yes if migrating |
| Customer validation / acceptance recorded | [Customer validation checklist](../checklists/customer-validation-checklist.md) / acceptance | Customer acceptance authority | | | Customer acceptance authority | Yes if migrating |
| Material exceptions dispositioned (fixed / accepted / deferred with owner) | Exception report | Data migration owner *(hat)* | | | Customer acceptance authority | Yes if migrating |
| Final sync / freeze plan agreed (when applicable) | Runbook + customer brief | Implementation lead | | | Customer project lead | Yes if migrating |

---

## 4. Configuration readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| [Agency configuration checklist](../checklists/agency-configuration-checklist.md) complete for go-live scope (or deferred with owners) | Checklist link | Implementation lead *(Configuration hat)* | | | Implementation lead | Yes |
| Customer configuration decisions approved for go-live scope | [Configuration discovery workbook](../../customer/implementation/configuration-discovery-workbook.md) §16 | Customer acceptance authority / project lead | | | Customer acceptance authority | Yes |
| Identity, numbering, headers, modules match agreed workflows | Smoke notes / workbook | Implementation lead *(Configuration hat)* | | | Module leads as needed | Yes |
| Device **software settings** in Admin complete for go-live devices (print routes, enables)—not physical install | Agency settings / config checklist | Implementation lead *(Configuration hat)* | | | Implementation lead | Conditional |
| Config debt list has owners; no silent gaps | Workspace config status | Implementation lead | | | Implementation lead | Yes if unowned |

*Device installation and end-to-end print/scan proof belong under Integration and hardware readiness (section 5).*

---

## 5. Integration and hardware readiness

*If none in scope, mark **Not applicable**.*

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| In-scope integrations listed and each Pass / Fail / Deferred | Integration matrix in workspace | Implementation lead *(Integrations hat)* | | | Implementation lead | Yes if in scope |
| End-to-end test completed for each required integration (or authorized deferral) | Test notes | Implementation lead *(Integrations hat)* | | | Customer IT / module lead as applicable | Yes if in scope |
| [Hardware readiness checklist](../checklists/hardware-readiness-checklist.md) complete or N/A | Checklist link | Implementation lead *(Hardware hat)* | | | Customer IT / project lead | Yes if hardware in scope |
| Install, connectivity, compatibility, and print/scan/mobile smoke tests done for go-live roles | Hardware checklist + notes | Implementation lead *(Hardware hat)* | | | Customer project lead | Yes if hardware in scope |
| Known integration/hardware limits documented for Operate | Workspace / handoff notes | Implementation lead | | | Implementation lead | No |

---

## 6. User and access readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Go-live user cohort identified | Roster artifact | Customer project lead | | | Customer project lead | Yes |
| Accounts created with correct roles for go-live cohort | Admin / roster check | Implementation lead *(Configuration hat)* | | | Customer project lead | Yes |
| Users can authenticate to the go-live environment | Spot-check logins | Implementation lead | | | Customer project lead | Yes |
| Approvers / admins named for day-one workflows | Config workbook / roster | Customer project lead | | | Customer acceptance authority | Yes |
| Contacts ≠ assumed users; no orphan critical role | Roster vs contacts list | Customer project lead | | | Implementation lead | No |

---

## 7. Training readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Training plan executed for agreed audiences | Training plan / attendance | Training owner *(hat)* | | | Customer training coordinator | Yes |
| No training gap that blocks production use (or makeup plan + acceptance) | Training follow-ups list | Training owner *(hat)* | | | Customer acceptance authority | Yes |
| Customer acknowledges readiness to proceed from a training perspective | Email / decision / brief ack | Customer acceptance authority | | | Customer acceptance authority | Yes |
| Reference materials pointed (getting started / workshops) | Customer brief links | Training owner *(hat)* | | | Customer project lead | No |

*Depends on Phase 6 completeness. If facilitation SOP is still thin, record attendance and acknowledgment in the workspace.*

---

## 8. Operational readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Day-one shift / coverage plan named (who works in Thin Line) | Customer brief / notes | Customer project lead | | | Customer acceptance authority | Yes |
| Supervisors know how work is done on day one (legacy freeze / parallel if any) | Customer brief | Customer project lead | | | Module leads | Yes |
| Core workflows smoke-tested in go-live environment for in-scope modules | Smoke checklist / notes | Implementation lead | | | Implementation lead | Yes |
| Legacy system posture agreed (freeze, read-only, retire later) | Customer brief / runbook | Implementation lead | | | Customer project lead | Yes if legacy still exists |

---

## 9. Support and communications readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| [Customer go-live and hypercare brief](../../customer/implementation/go-live-and-hypercare-brief.md) issued | Sent brief / workspace copy | Implementation lead | | | Customer project lead | Yes |
| Issue-reporting path clear for hypercare | Brief § reporting | Implementation lead | | | Customer project lead | Yes |
| Escalation contacts named both sides | Brief / workspace | Implementation lead | | | Customer project lead | Yes |
| Hypercare duration and coverage hours agreed | Brief / decision record | Implementation lead | | | Customer acceptance authority | Yes |
| Customer Success / Operate aware of impending handoff | Internal note | Implementation lead | | | Customer Success owner *(hat)* | No |

---

## 10. Risk and exception review

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Open blockers reviewed; none unmanaged | Action register (Blocker) | Implementation lead | | | Implementation lead | Yes |
| Accepted exceptions listed with residual risk | Decision record | Implementation lead | | | Customer acceptance authority | Yes if any exception |
| Product gaps dispositioned (workaround / accept / block) | Action register (Product gap) | Implementation lead | | | Customer acceptance authority + Engineering as needed | Yes if gap blocks workflow |
| Deferred items have owners and do not silently block day one | Action register / plan | Implementation lead | | | Customer project lead | Yes if unowned |

---

## 11. Cutover and rollback readiness

| Criterion | Evidence or linked artifact | Owner | Status | Exception or risk | Required approver | Blocking? |
|-----------|----------------------------|-------|--------|-------------------|-------------------|:---------:|
| Cutover steps agreed ([Go-live runbook](../sops/deliver/go-live-runbook.md) filled for this engagement) | Engagement runbook copy | Implementation lead | | | Implementation lead | Yes |
| Data-entry freeze window communicated (when applicable) | Customer brief | Implementation lead | | | Customer project lead | Yes when freeze used |
| Rollback triggers and process understood by cutover team | Runbook § rollback | Implementation lead | | | Implementation lead | Yes |
| Go/no-go meeting scheduled before cutover | Calendar | Implementation lead | | | Customer project lead | Yes |
| Immediate post-cutover validation steps named | Runbook checklist | Implementation lead | | | Implementation lead | Yes |

---

## 12. Authorization

Complete only after sections 1–11 are reviewed.

### Thin Line go-live recommendation

| Field | Value |
|-------|--------|
| **Recommendation** | ☐ Recommend Go · ☐ Recommend Conditional Go · ☐ Recommend No Go |
| **Recommended by (name / role)** | Implementation lead (required); others consulted: |
| **Date** | |
| **Summary rationale** | |
| **Conditions (if Conditional)** | |
| **Blocking items still open** | None / list |

### Customer authorization to begin production use

| Field | Value |
|-------|--------|
| **Authorization** | ☐ Authorize Go · ☐ Authorize Conditional Go · ☐ No Go (do not begin production use) |
| **Authorized by (name / title)** | Final acceptance authority (required) |
| **Date** | |
| **Conditions acknowledged** | |
| **Customer project lead acknowledgment** | |

### Combined decision

Record the formal outcome on the [Go-live decision record](../templates/go-live-decision-record.md):

| Decision | Meaning |
|----------|---------|
| **Go** | Proceed with cutover as planned |
| **Conditional Go** | Proceed only if listed conditions are met before or at cutover |
| **No Go** | Do not begin production use; set next review date |

**Rule:** Thin Line may **recommend** Go while the customer chooses No Go. Production use does **not** begin without customer authorization. Thin Line must **not** recommend Go while any blocking criterion is incomplete without an authorized exception.

---

## Readiness rollup

| Area | Overall status | Blocking open? | Notes |
|------|----------------|:--------------:|-------|
| 1. Project and scope | | ☐ | |
| 2. Infrastructure | | ☐ | |
| 3. Data migration | | ☐ | |
| 4. Configuration | | ☐ | |
| 5. Integration and hardware | | ☐ | |
| 6. User and access | | ☐ | |
| 7. Training | | ☐ | |
| 8. Operational | | ☐ | |
| 9. Support and communications | | ☐ | |
| 10. Risk and exception | | ☐ | |
| 11. Cutover and rollback | | ☐ | |
| 12. Authorization | | ☐ | |

**Assessment outcome:** ☐ Ready to proceed to decision record · ☐ Not ready · ☐ Ready with conditions listed on decision record  

---

## Related

| Document | Role |
|----------|------|
| [Go live](../sops/deliver/go-live.md) | Phase overview |
| [Go-live runbook](../sops/deliver/go-live-runbook.md) | Cutover SOP |
| [Go-live decision record](../templates/go-live-decision-record.md) | Formal Go / Conditional Go / No Go |
| [Customer go-live and hypercare brief](../../customer/implementation/go-live-and-hypercare-brief.md) | Customer communications |
| [Implementation lifecycle](../sops/deliver/implementation-lifecycle.md) | Phase 7 gates |
| [Environment health checklist](../checklists/environment-health-checklist.md) | Infrastructure evidence |
| [Customer validation checklist](../checklists/customer-validation-checklist.md) | Migration evidence |
| [Agency configuration checklist](../checklists/agency-configuration-checklist.md) | Configuration evidence |
| [Hardware readiness checklist](../checklists/hardware-readiness-checklist.md) | Hardware evidence |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — full readiness gate replacing Placeholder |
