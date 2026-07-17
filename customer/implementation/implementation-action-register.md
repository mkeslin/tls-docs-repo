# Implementation action register

**Audience:** Your agency’s project team · Thin Line implementation team  
**Purpose:** Single shared list of actions, decisions, risks, and gaps during implementation  
**Reusable template:** Copy this page (or its table) into the engagement workspace; keep one living register per customer.

---

## Document header

| Field | Value |
|-------|--------|
| **Customer / agency** | |
| **Register version / last reviewed** | |
| **Thin Line implementation lead** | |
| **Customer project lead** | |
| **Reviewed every** | Every implementation meeting *(required)* |

---

## How to use this register

1. Log new items during or immediately after meetings—do not rely on chat memory.  
2. Give every item a stable **ID** (see [ID convention](#id-convention)).  
3. Review **all open items** at the start or end of every implementation meeting.  
4. Close items only when status and completion rules below are met.  
5. Link artifacts (rosters, logos, assessment notes, config workbook rows) instead of pasting large content into **Notes**.

Related: [Implementation kickoff agenda](implementation-kickoff-agenda.md) · [Preliminary implementation plan](preliminary-implementation-plan.md) · [Customer implementation workbook](customer-implementation-workbook.md) · [Configuration discovery workbook](configuration-discovery-workbook.md)

---

## Rules

### One clear owner

- Every row has **exactly one Owner**—the person accountable for moving it to the next status.  
- **Supporting participant** may help or review; they are not a second owner.  
- If ownership is unclear, the item stays **Not started** until an owner is named.  
- Prefer a named person over a role (“Records clerk”) when possible; roles are acceptable only until a name is known.

### Explicit due dates where appropriate

- **Customer action**, **Thin Line action**, **Joint action**, and **Blocker** items should have a **Due date** (or an explicit “TBD — dependency …” note in **Dependency**).  
- **Decision** items need a due date when they block a phase or go-live; otherwise target the next working session.  
- **Risk** items may use a review date instead of a completion due date.  
- **Product gap** and **Future enhancement** may be **Deferred** without a hard due date, but must still have an owner for triage.  
- Do not invent fake dates to fill the column—use a real date or document why it is open-ended.

### Separate product gaps from implementation tasks

| If the issue is… | Use type | Do not |
|------------------|----------|--------|
| Work the agency or Thin Line must do on this engagement | Customer / Thin Line / Joint **action** | Call it a product gap |
| Software cannot do what was expected (capability missing or wrong) | **Product gap** | Track only as a vague “action” with no product follow-up |
| Nice-to-have after go-live | **Future enhancement** | Block go-live unless reclassified |
| Something that stops progress now | **Blocker** (and optionally link a related Product gap) | Leave as a soft risk with no owner |

Product gaps may spawn implementation workarounds (separate **action** rows). Keep the gap row open until product disposition is recorded (fix planned / workaround accepted / out of scope).

### Close decisions only after they are recorded

- A **Decision** is not **Complete** until the decision text is written in **Action or decision** (or **Notes**) clearly enough that someone absent from the meeting can apply it.  
- Prefer also recording the decision in the [Configuration discovery workbook](configuration-discovery-workbook.md), [Preliminary implementation plan](preliminary-implementation-plan.md), or other linked artifact—then set **Linked artifact**.  
- “We talked about it” is not enough to close a Decision.

### Review open actions in every implementation meeting

- Standing agenda item: walk **Not started**, **Waiting on …**, **In progress**, **Blocked**, and **Ready for validation**.  
- Update **Status**, **Due date**, and **Owner** in the meeting when they change.  
- Call out anything **Waiting on customer** or **Waiting on Thin Line** older than its due date.  
- **Complete**, **Deferred**, and **Not applicable** rows stay in the register for history; filter them out of the live review view if your tool allows.

---

## Field definitions

| Field | Meaning |
|-------|---------|
| **ID** | Stable unique identifier (see below) |
| **Date created** | Date the item was first logged |
| **Customer** | Agency / engagement name (repeat on each row if the register is exported or filtered) |
| **Implementation phase** | Lifecycle phase the item belongs to (see list below) |
| **Action or decision** | One clear statement of the work or the decision to make/record |
| **Type** | One of the [allowed types](#allowed-types) |
| **Owner** | Single accountable person |
| **Supporting participant** | Helper or reviewer (optional) |
| **Due date** | Target date, or blank only when rules above allow |
| **Dependency** | What must happen first (ID of another row, assessment, vendor, etc.) |
| **Status** | One of the [allowed statuses](#allowed-statuses) |
| **Date completed** | Set when status becomes **Complete**, **Deferred** (with disposition), or **Not applicable** |
| **Notes** | Short context; not a substitute for Linked artifact |
| **Linked artifact** | Path, filename, ticket, or workbook section reference |

### Implementation phase values *(recommended)*

Use one per row:

- Sales handoff  
- Kickoff and discovery  
- Infrastructure  
- Data migration  
- Configuration  
- Integrations and hardware  
- Training  
- Go live  
- Hypercare and transition  
- Cross-phase / project management  

---

## Allowed types

| Type | Use when |
|------|----------|
| **Customer action** | Agency must deliver, decide, attend, or validate |
| **Thin Line action** | Thin Line must deliver, configure, schedule, or follow up |
| **Joint action** | Both sides must act together in the same step (e.g. joint validation session) |
| **Decision** | A choice must be made and recorded before work proceeds correctly |
| **Risk** | Something that might harm timeline, quality, or go-live; needs watch or mitigation |
| **Blocker** | Progress is stopped until this is resolved |
| **Product gap** | Product capability issue—not solvable by configuration alone |
| **Future enhancement** | Desired later; not required for current go-live scope |

---

## Allowed statuses

| Status | Meaning |
|--------|---------|
| **Not started** | Logged; work has not begun |
| **Waiting on customer** | Thin Line (or joint work) cannot proceed until the customer acts |
| **Waiting on Thin Line** | Customer (or joint work) cannot proceed until Thin Line acts |
| **In progress** | Owner is actively working it |
| **Blocked** | Cannot proceed because of a dependency or **Blocker** (name it in Dependency) |
| **Ready for validation** | Owner believes it is done; awaiting check, UAT, or acceptance from the other party or lead |
| **Complete** | Finished; Decision types also have the outcome recorded |
| **Deferred** | Intentionally postponed with owner and reason in Notes |
| **Not applicable** | No longer relevant; reason in Notes |

These match the [Implementation workspace standard](../../internal/sops/deliver/implementation-workspace-standard.md) engagement statuses. Do not use document maturity labels (Placeholder, Draft, v1) as row statuses.

---

## ID convention

Suggested pattern (adjust if your workspace already has IDs):

| Prefix | Type |
|--------|------|
| `CA-###` | Customer action |
| `TL-###` | Thin Line action |
| `JA-###` | Joint action |
| `DEC-###` | Decision |
| `RSK-###` | Risk |
| `BLK-###` | Blocker |
| `GAP-###` | Product gap |
| `ENH-###` | Future enhancement |

Number sequentially within the engagement. Do not reuse IDs after closure.

---

## Register

*Add rows as needed. Keep completed items for audit trail.*

| ID | Date created | Customer | Implementation phase | Action or decision | Type | Owner | Supporting participant | Due date | Dependency | Status | Date completed | Notes | Linked artifact |
|----|--------------|----------|----------------------|--------------------|------|-------|------------------------|----------|------------|--------|----------------|-------|-----------------|
| | | | | | | | | | | Not started | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |

---

## Meeting review checklist

Use at every implementation meeting:

- [ ] Open items reviewed (all statuses except Complete / Deferred / Not applicable, unless reopened)  
- [ ] **Deferred** items still have owners and reasons  
- [ ] Each open item still has **one** owner  
- [ ] Overdue items have a new due date or an explicit Blocked/Deferred reason  
- [ ] **Waiting on customer** / **Waiting on Thin Line** called out  
- [ ] New **Decision** items have outcome text before marking Complete  
- [ ] **Product gap** vs implementation **action** types still correct  
- [ ] **Linked artifact** filled when a file or workbook section exists  

**Reviewed by:** _______________ **Date:** ________  

---

## Optional views *(for spreadsheet copies)*

If you maintain this register in a spreadsheet or board, useful filters:

| View | Filter |
|------|--------|
| Meeting review | Status not in Complete, Deferred, Not applicable |
| Customer queue | Status = Waiting on customer **or** Type = Customer action and Status open |
| Thin Line queue | Status = Waiting on Thin Line **or** Type = Thin Line action and Status open |
| Blockers and risks | Type in Blocker, Risk |
| Product backlog handoff | Type in Product gap, Future enhancement |

---

## Related

- [Implementation kickoff agenda](implementation-kickoff-agenda.md) — seed actions from kickoff  
- [Preliminary implementation plan](preliminary-implementation-plan.md) — next steps and open decisions  
- [Customer implementation workbook](customer-implementation-workbook.md)  
- [Configuration discovery workbook](configuration-discovery-workbook.md)  

*Thin Line Software · Implementation action register · Customer-facing · Reusable*
