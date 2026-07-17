# Implementation workspace standard

**Document type:** Standard  
**Status:** v1  
**Audience:** Implementation · Sales · Customer Success · Engineering · founders  

---

## Purpose

Define the **authoritative project record** used to manage each customer implementation.

The workspace is the **operational source of truth** for implementation status: what was agreed, what is done, what is waiting, who owns the next action, and what must be true before a phase exits.

This standard is **tool-neutral**. The workspace may be represented today with documents, spreadsheets, a project tool, shared folders, or a mix—and later as part of Thin Line Hub. The **content and rules** stay the same; only the container changes.

---

## What the workspace is

| The workspace **is** | The workspace **is not** |
|----------------------|---------------------------|
| The engagement’s system of record for status, ownership, decisions, and readiness | A dump of every email |
| Where phase gates and open work are visible | A substitute for GitBook methodology |
| Where customer-facing and internal items are separated on purpose | The product Admin configuration itself |
| Closed when hypercare transitions and records are complete | Abandoned when go-live “feels done” |

**GitBook** explains *how* Thin Line implements (methodology, standards, SOPs, checklists).  
**The workspace** tracks *this* customer’s execution, status, ownership, and collaboration.

---

## Minimum contents

Every implementation workspace must be able to answer the following. Representation can be tabs, sheets, lists, or Hub records—as long as the information is findable and current.

### 1. Customer and agency identity

- Legal / customer name  
- Agency display name and **AgencyName** slug (when known)  
- Agency type / products in use (LE, court, jail, etc.)  
- Environment tiers in scope (`test`, `prod`, …)  
- Primary location / jurisdiction notes as needed  

Bootstrap naming rules: [Bootstrap environment standard](infrastructure/bootstrap-environment-standard.md).

### 2. Contract and purchased products

- Contract / CRM reference  
- Purchased modules and options  
- Migration in/out of scope and fee commitments (summary—not a substitute for Finance)  
- Material commercial constraints that affect delivery  

### 3. Implementation contacts (customer)

- Sponsor / go-live authority  
- Day-to-day coordinator  
- IT / technical contact  
- Operational leads by area (dispatch, records, court, jail, …) as relevant  

### 4. Thin Line project team

- Implementation lead  
- Other named roles (migration, infrastructure, configuration, training, integrations)  
- Escalation path  

See [Implementation roles and responsibilities](implementation-roles-and-responsibilities.md).

### 5. Target timeline and go-live date

- Target go-live date (or window)  
- Key intermediate dates (kickoff, UAT, training, cutover)  
- Explicit “date unknown” when true—do not invent false precision  

### 6. Implementation phases and phase status

Track phases **0–8** from the [Implementation lifecycle](implementation-lifecycle.md). Each phase has a status from the required set below (or **Not applicable**).

### 7. Tasks and owners

Customer-facing field model and rules: [Implementation action register](../../../customer/implementation/implementation-action-register.md).

- Work items with a single owner  
- Due date when a date matters  
- Link to the phase they serve  
- Status from the required set  

### 8. Customer requests

- Asks from the customer that are not yet decisions or tasks  
- Intake date, requester, disposition (accept / defer / decline / convert to task)  

### 9. Decisions and approvals

- Decision statement  
- Who decided / who approved  
- Date  
- Alternatives considered when material  
- Link to related phase or task  

### 10. Risks, blockers, and dependencies

- Description, severity, owner, mitigation  
- Whether the item blocks a phase gate  
- Dependency on customer, Thin Line, vendor, or product  

### 11. Data migration status

- In scope / N/A  
- Vendor / package / engagement folder pointer  
- Validation and acceptance state  
- Exception summary  

### 12. Configuration status

- Checklist progress or equivalent  
- Deferred config items with owners  
- Pointers to filled worksheets—not a second copy of Admin data  

### 13. Integration and hardware status

- Integration matrix (pass / fail / deferred / N/A)  
- Hardware readiness  
- Vendor dependencies  

### 14. Training plan and attendance

- Audiences / roles  
- Sessions planned and completed  
- Attendance or acknowledgment  
- Gaps that affect go-live  

### 15. Documents and customer-provided files

- Index of artifacts (contracts extracts, org charts, code lists, logos, extracts)  
- **Link** to storage location; do not duplicate large files inside status boards  

### 16. Open product gaps or commitments

- Gaps that require product change  
- Commitments made to the customer (with who promised what)  
- Link to engineering backlog item when one exists—do not treat the workspace as the product backlog  

### 17. Go-live readiness

- Readiness assessment / checklist state  
- Go / no-go recommendation and approver  
- Cutover plan pointer  

### 18. Hypercare activity

- Window dates  
- Issues opened/closed during hypercare  
- Check-in notes  

### 19. Acceptance and transition records

- Migration acceptance (when in scope)  
- Training / go-live acknowledgments  
- Hypercare exit and Operate / Customer Success handoff  

---

## Document maturity vs engagement status

| Kind | Examples | Where used |
|------|----------|------------|
| **Document maturity** | Placeholder · Draft · v1 | GitBook page headers only—describes how finished the *methodology page* is |
| **Engagement status** | Values in the table below | Phases, tasks, assessment rows, action register for *this customer* |

Do not put Placeholder or Draft on engagement boards.

## Required status values

Use these values for **phases**, **tasks**, and other work items unless a field truly needs a narrower set. Do not invent synonyms (e.g. “Done” vs “Complete”, or “Ready for review” vs “Ready for validation”).

| Status | Meaning |
|--------|---------|
| **Not started** | Agreed work; no meaningful progress yet |
| **Waiting on customer** | Thin Line cannot advance without a customer action |
| **Waiting on Thin Line** | Customer is waiting on Thin Line |
| **In progress** | Active work by the owner |
| **Blocked** | Cannot proceed; blocker must be recorded under risks/blockers |
| **Ready for validation** | Build/config done; awaiting check, UAT, or acceptance |
| **Complete** | Exit criteria met (or task acceptance criteria met) |
| **Deferred** | Intentionally postponed with owner, reason, and follow-up; not a silent skip |
| **Not applicable** | Out of scope for this engagement; do not leave blank |

**Blocked** always requires a linked risk/blocker.  
**Deferred** always requires an owner and a reason (and, at phase gates, authorized exception when it would otherwise block).  
**Complete** on a **phase** means lifecycle exit criteria are met—not that “most tasks are done.”

---

## Kinds of information (keep them separate)

Mixing these categories is how workspaces become unusable.

| Kind | What it is | Belongs in workspace? | Notes |
|------|------------|------------------------|-------|
| **Configuration data** | Values that make the product behave for this agency (ORI, codes, number patterns, officers) | Pointers and status only | Authoritative values live in the product (and migration Overrides where used)—not retyped into status boards |
| **Project-management data** | Phases, tasks, owners, dates, risks, decisions | **Yes — primary** | This is the core of the workspace |
| **Customer-provided artifacts** | Extracts, PDFs, logos, policy docs, spreadsheets from the agency | Index + link | Store in the engagement file location; link from the workspace |
| **Internal implementation notes** | Thin Line working notes, scripts used, “how we got unstuck” | Yes, marked internal | Not for customer-visible views by default |
| **Product backlog items** | Defects or features for Engineering | Link / ID only | Do not run the product roadmap inside the engagement board |
| **Support issues** | Tickets after Operate owns the customer | Link after transition | During hypercare, track in hypercare activity; after transition, Support’s system is authoritative |

---

## Operating rules

### Ownership

- Every phase has an accountable Thin Line owner (see [Implementation roles and responsibilities](implementation-roles-and-responsibilities.md)).  
- Every open task has **one** owner (person), not a team name.  
- Customer-owned actions use **Waiting on customer** and name the customer contact when known.  

### Due dates

- Put a due date on work that affects the go-live window or a phase gate.  
- If the date slips, update the date and note why—do not leave stale dates.  
- “ASAP” is not a due date.  

### Status updates

- The owner updates status when it changes—not only in weekly meetings.  
- Moving to **Blocked** or **Waiting on…** requires a one-line reason.  
- Phase status is updated by the Implementation lead (or delegate) when exit criteria change.  

### Customer-visible vs internal-only

| Typically **customer-visible** | Typically **internal-only** |
|--------------------------------|-----------------------------|
| Shared timeline and go-live window | Internal estimates and margin notes |
| Tasks waiting on the customer | Thin Line staffing / capacity |
| Decisions they participated in | Unvalidated product gossip |
| Training schedule and attendance they own | Internal implementation notes |
| Migration validation they must perform | Package internals and promotion debate |

If the workspace tool cannot separate views, keep internal notes in an internal section or document and link them. Do not paste internal-only procedures into customer-facing materials (see [Implementation overview](implementation-overview.md)).

### Recording decisions

- Write the decision as a sentence the next person can apply.  
- Include who approved and the date.  
- Link related tasks or phases.  
- Changing a decision creates a new decision record; do not silently edit history away.  

### Closing tasks

- Close only when the acceptance criteria for that task are met.  
- Prefer **Complete** over deleting the task—history matters for hypercare and disputes.  
- Convert leftover work to a deferred item with an owner, or to a product backlog link—not a zombie **In progress**.  

### Link rather than duplicate

- Point to checklists, Overrides folders, extracts, and Hub/CRM records.  
- Do not paste full configuration tables into the status board.  
- Do not maintain two competing “sources of truth” for the same artifact.  

### Phase completion

- A phase becomes **Complete** only when [lifecycle](implementation-lifecycle.md) exit criteria are satisfied.  
- Overlapping work on the next phase is allowed; marking the prior phase complete early is not.  
- Use **Not applicable** when the phase is out of scope—with a short reason.  

### Workspace closure

Close the workspace when:

1. Phase 8 (Hypercare and transition) is **Complete**.  
2. Acceptance and transition records are filed.  
3. Open items are owned by Operate / Customer Success or explicitly accepted as residual risk.  
4. Product gaps are linked to backlog items (or declined in writing).  

After closure, the workspace remains a **read-only historical record**. New production issues go through Support—not by reopening the engagement as if go-live never happened.

---

## Relationship to GitBook and Thin Line Hub

| Layer | Role |
|-------|------|
| **GitBook** | How implementation work is performed—overview, lifecycle, standards, SOPs, checklists |
| **Implementation workspace** | Execution for one customer—status, ownership, decisions, collaboration |
| **Thin Line Hub (future)** | Intended home for execution, status, ownership, and customer collaboration; may also hold Environment records |

Today the workspace may be folders and trackers. Later, Hub should make the same minimum contents first-class—without changing this standard’s meaning.

Environment provisioning design (separate from this engagement record): [Hub environment integration](infrastructure/hub-environment-integration.md).

---

## Engagement file locations (when using folders)

Tool-neutral status can still point at conventional file homes in the product monorepo and shared drives. These are **artifact locations**, not a requirement to use a particular PM tool.

| Layer | Typical location | Contains |
|-------|------------------|----------|
| Shared migration packages | `Utilities/Migration Tools/<Vendor>/` | Templates, Pipeline, `VERSION`—not agency fills |
| Infrastructure automation | `Infrastructure/scripts/`, `environments/*.profile.json` | Bootstrap / teardown |
| Customer engagement files | `Clients/<Client>/Conversion/<Engagement>/` (+ shared drive as used) | Filled checklist, Overrides, extracts |
| Methodology | GitBook `internal/sops/deliver/` | This standard and related docs |

Never leave agency-specific hardcodes in shared vendor packages. Promote reusable fixes and bump package `VERSION` — [Migration overrides & mapping standard](data-migration/migration-customer-configuration.md).

---

## Related

| Document | Role |
|----------|------|
| [Implementation overview](implementation-overview.md) | Knowledge vs execution |
| [Creating a new implementation](creating-a-new-implementation.md) | How to open, run, archive, and improve from a workspace |
| [Implementation lifecycle](implementation-lifecycle.md) | Phases and gates |
| [Implementation roles and responsibilities](implementation-roles-and-responsibilities.md) | Who owns what |
| [Sales handoff checklist](../../checklists/sales-handoff-checklist.md) | Early packet fields |
| [Bootstrap environment standard](infrastructure/bootstrap-environment-standard.md) | AgencyName / environment identity |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Initial folder-focused stub |
| 2026-07-17 | Tool-neutral workspace standard: minimum contents, statuses, rules, Hub relationship |
