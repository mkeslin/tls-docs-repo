# Creating a new implementation

**Document type:** Process  
**Status:** v1  
**Audience:** Implementation lead · Sales (handoff) · founders  
**Parent:** [Implementation overview](implementation-overview.md)

This is the missing “how we open the books” step: what to do **after** a contract is signed—or after an **approved discovery** engagement is authorized to proceed—before Phase 1 work is underway.

It does not replace the [Implementation lifecycle](implementation-lifecycle.md). It starts the **workspace** that the lifecycle runs in.

---

## When to use this page

Start a new implementation when **either**:

1. **Contract path** — SaaS (and CJIS path when required) is clear enough that Implementation has accepted ownership ([Sales handoff](sales-handoff.md)), or  
2. **Approved discovery path** — discovery was authorized separately and Thin Line has agreed to open a delivery workspace (still record commercial status honestly).

Do **not** create a full delivery workspace for an unqualified lead. Use a light sales/discovery note until handoff or approval exists.

---

## Process

### 1. Create the customer folder / workspace

Create one engagement workspace for this customer (tool-neutral: shared folder, project board, Hub record later—same contents).

Minimum layout intent:

- Customer / agency identity  
- Lifecycle board (phases 0–8)  
- Action register  
- Place for artifacts (extracts, logos, checklists)—**links**, not a dump of every email  

Rules and required contents: [Implementation workspace standard](implementation-workspace-standard.md).  
Typical file home when using folders: `Clients/<Client>/…` (see workspace standard)—not GitBook `customer/`.

### 2. Copy templates

Copy reusable templates **into the workspace** (do not fill agency answers in GitBook).

| Copy from | Into workspace as |
|-----------|-------------------|
| [Discovery brief template](../../../customer/implementation/discovery-brief-template.md) | Agency discovery brief *(customer pre-read)* |
| [Working session workbook template](../../templates/working-session-workbook.md) | Thin Line meeting notebook *(not customer-facing)* |
| [Implementation kickoff agenda](../../../customer/implementation/implementation-kickoff-agenda.md) | Kickoff agenda |
| [Customer implementation workbook](../../../customer/implementation/customer-implementation-workbook.md) | Implementation workbook *(or section copies)* |
| [Configuration discovery workbook](../../../customer/implementation/configuration-discovery-workbook.md) | Configuration decisions *(later)* |
| [Preliminary implementation plan](../../../customer/implementation/preliminary-implementation-plan.md) | Preliminary plan *(after discovery)* |
| [Implementation action register](../../../customer/implementation/implementation-action-register.md) | Living action register |
| [Go-live and hypercare brief](../../../customer/implementation/go-live-and-hypercare-brief.md) | Go-live brief *(near cutover only)* |
| Internal assessments / checklists as needed | Engagement copies linked from the board |

Internal SOPs stay in GitBook; only **filled** copies and evidence live in the workspace.

### 3. Rename them

Rename copies for the agency and engagement (e.g. agency name + document purpose + date or version). Keep names stable enough that links in the action register do not rot weekly.

### 4. Record customer metadata

Fill the workspace header from handoff / CRM. At minimum:

| Metadata | Notes |
|----------|--------|
| Legal / customer name | |
| Agency display name | |
| AgencyName slug *(when known)* | See bootstrap standard |
| Products / modules in scope | Confirmed / preliminary / pending assessment |
| Migration in / out / unknown | |
| Integrations / hardware flags | |
| Customer project lead | |
| Final acceptance authority | |
| Thin Line implementation lead | |
| Sales owner / CRM reference | |
| Target go-live window | Or explicit TBD |

Statuses use the engagement set (Not started, Waiting on customer, Complete, Deferred, Not applicable, …)—not document maturity labels. See [Workspace standard](implementation-workspace-standard.md).

### 5. Schedule kickoff

- Confirm invitees (customer project lead, acceptance authority as needed, Thin Line lead; Sales for commercial Q&A)  
- Send agenda and, when useful, a customized discovery brief  
- Put the kickoff date on the lifecycle board  

Use: [Implementation kickoff agenda](../../../customer/implementation/implementation-kickoff-agenda.md) · [Kickoff and discovery](kickoff-and-discovery.md)

### 6. Begin Phase 1

Mark Phase 1 **In progress**. Run kickoff and discovery. Do not pretend later phases are Complete.

If Sales handoff (Phase 0) is not yet Complete, finish acceptance of the handoff packet first—or record what is still open with owners.

### 7. Update the workspace throughout the engagement

Standing habit for every implementation meeting:

- Review open actions ([Action register](../../../customer/implementation/implementation-action-register.md))  
- Update phase statuses only when exit criteria change  
- Record decisions; link artifacts  
- Keep Waiting on customer vs Waiting on Thin Line honest  

Advance phases 2–8 per the [lifecycle](implementation-lifecycle.md). Overlap work when useful; do not fake phase Complete.

### 8. Archive the workspace after transition

When [Hypercare and transition](hypercare-and-transition.md) exits:

- Mark Phase 8 Complete  
- Confirm Operate / Support ownership  
- Set the workspace to **read-only / archived** per the workspace standard  
- New production issues go to Support—not a reopened implementation board  

### 9. Complete an implementation retrospective

Short internal retro (Implementation lead; invite Sales, Migration, Training, CS as useful):

| Prompt | Capture |
|--------|---------|
| What slowed us down? | |
| What should we reuse next time? | |
| Customer friction we should prevent? | |
| Product gaps filed to backlog? | |
| Doc / checklist gaps? | |

Keep the retro in the archived workspace (internal section). Do not put customer-identifying operational detail into public customer docs.

### 10. Feed improvements back into GitBook

Promote reusable learning into methodology—not into one-off agency pages under `customer/`:

| If you learned… | Update |
|-----------------|--------|
| A better phase exit or checklist step | Lifecycle, phase overview, or checklist |
| A vendor conversion gotcha | Vendor conversion guide + package `VERSION` when code changes |
| A clearer customer template | Template under `customer/implementation/` (still blank/reusable) |
| A pricing or policy issue | Policy / assessment—not a silent scope change |

GitBook remains **how we implement**. The workspace remains **what happened for this agency**.

---

## Quick checklist

- [ ] Workspace created  
- [ ] Templates copied and renamed  
- [ ] Metadata recorded  
- [ ] Kickoff scheduled  
- [ ] Phase 0 accepted (or gaps owned)  
- [ ] Phase 1 In progress  
- [ ] Action register live  
- [ ] *(Later)* Workspace archived after Phase 8  
- [ ] *(Later)* Retrospective done  
- [ ] *(Later)* GitBook / package improvements filed  

---

## Related

| Document | Role |
|----------|------|
| [Implementation overview](implementation-overview.md) | Principles; GitBook vs workspace |
| [Implementation workspace standard](implementation-workspace-standard.md) | What the workspace must contain |
| [Implementation lifecycle](implementation-lifecycle.md) | Phases 0–8 |
| [Sales handoff](sales-handoff.md) | Contract path into Deliver |
| [Kickoff and discovery](kickoff-and-discovery.md) | Phase 1 |
| [Implementation roles and responsibilities](implementation-roles-and-responsibilities.md) | Who owns the board |
| [Customer — Implementation](../../../customer/implementation/README.md) | Customer-facing template pack |
| [Deliver index](README.md) | Full TOC |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | v1 — open engagement process (workspace through retrospective) |
