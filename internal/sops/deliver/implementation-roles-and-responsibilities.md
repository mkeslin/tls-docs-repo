# Implementation roles and responsibilities

**Document type:** Reference  
**Status:** v1  
**Audience:** Sales · Implementation · Engineering · Customer Success · founders · customer project teams  

Who owns what across Deliver. Names change per engagement; **roles** do not. One person may hold multiple Thin Line roles on a small project—record that explicitly at kickoff.

### Specialist responsibilities (hats)

Lifecycle pages may name **Infrastructure**, **Migration**, **Configuration**, **Integrations / hardware**, or **Training** work. Those are **responsibilities (hats)**, not separate mandatory headcount.

| Hat | Typical accountabilities | Default assignee |
|-----|--------------------------|------------------|
| Infrastructure | Bootstrap, environment health, cutover backups | Implementation lead unless a Technical/engineering owner is assigned |
| Data migration | Package, Overrides, validation support | Data migration owner when named; else Implementation lead |
| Configuration | Agency & module settings, users/roles, device *software settings* | Implementation lead unless delegated |
| Integrations / hardware | Live integration proof; device install, connectivity, compatibility, end-to-end tests | Implementation lead and/or Technical owner; customer IT for on-site devices |
| Training | Plan, delivery, readiness gaps | Training owner when named; else Implementation lead |

Always record the real person wearing each hat in the workspace. Do not leave ownership as “the configuration team.”

---

## Principles

1. **Every implementation has one Thin Line implementation lead.** That person owns the lifecycle board and phase exits.  
2. **Every customer has one accountable project lead.** Thin Line does not coordinate through an undefined committee.  
3. **Every task must have one clear owner.** Teams are not owners; people are.  
4. **Customer delay and Thin Line delay must be distinguishable.** Use workspace statuses **Waiting on customer** vs **Waiting on Thin Line** ([Implementation workspace standard](implementation-workspace-standard.md)).  
5. **Sales commitments must be visible to implementation.** Scope, dates, and promises live in the handoff and workspace—not only in Sales memory.  
6. **Engineering should not silently own customer decisions.** Engineers advise and build; authorized customer roles decide operational policy.  
7. **Customer acceptance must come from an authorized person.** Validation and go-live sign-off require the final acceptance authority (or a written delegate).  

---

## Thin Line roles

### Sales owner

| | |
|--|--|
| **Responsibilities** | Close commercial clarity; assemble handoff; surface scope, fees, risks, and promises; introduce Implementation. |
| **Decisions owned** | What was sold (modules, migration, integrations, hardware expectations); commercial concessions that affect delivery. |
| **Required participation** | Sales handoff; kickoff (at least for commercial Q&A); escalation when scope disputes return to the contract. |
| **Expected deliverables** | Complete handoff packet; CRM/deal references; written flags for migration/integrations/hardware; kickoff scheduled with Implementation. |
| **Escalation** | Escalates commercial disputes to executive sponsor (Thin Line) / customer executive sponsor; does not silently redefine scope mid-project. |

### Implementation lead

| | |
|--|--|
| **Responsibilities** | Run the engagement end-to-end: board, phase gates, customer coordination, risk visibility, hypercare transition. |
| **Decisions owned** | Phase exit (Complete / N/A); task prioritization within agreed scope; go/no-go recommendation to acceptance authority. |
| **Required participation** | All phases; primary Thin Line voice in kickoff, go-live, and hypercare. |
| **Expected deliverables** | Current workspace; named owners; phase statuses; cutover plan; hypercare handoff package. |
| **Escalation** | Escalates blockers to Thin Line executive sponsor and customer project lead; escalates product gaps to engineering with a tracked backlog link—not tribal “someone will fix it.” |

### Technical or engineering owner

| | |
|--|--|
| **Responsibilities** | Platform/bootstrap support, package or product defects, environment and integration technical advice; keep Hub/infra guidance accurate. |
| **Decisions owned** | Technical approach inside Thin Line systems; what is a product defect vs configuration; package VERSION promotions (with migration owner). |
| **Required participation** | Infrastructure as needed; migration package issues; integration failures; go-live if technical risk is material. |
| **Expected deliverables** | Fixes or clear workarounds; backlog items for durable gaps; guidance that Implementation can execute. |
| **Escalation** | Escalates platform risk to engineering leadership / Thin Line executive sponsor; does **not** decide agency policy (ORI rules, charging practice, who may approve records). |

### Data migration owner

| | |
|--|--|
| **Responsibilities** | Assessment inputs, package/Overrides, execution, validation support, exception disposition recommendations. |
| **Decisions owned** | Technical migration approach within approved plan; what to promote into the shared package. |
| **Required participation** | When migration is in scope: discovery, mapping sessions, validation cycles, acceptance review. |
| **Expected deliverables** | Engagement configuration (checklist + Overrides); validation evidence; exception report; acceptance package ready for authorized sign-off. |
| **Escalation** | Escalates data-quality or access blockers to Implementation lead and customer project lead; package gaps to engineering. |

### Training owner

| | |
|--|--|
| **Responsibilities** | Training plan by role; delivery; materials aligned to customer guides; readiness gaps that affect go-live. |
| **Decisions owned** | Session design and sequencing within the agreed plan; which gaps block go-live vs defer. |
| **Required participation** | Training phase; input at kickoff on audiences; go-live readiness discussion. |
| **Expected deliverables** | Training plan; attendance/acknowledgment records; list of residual training follow-ups. |
| **Escalation** | Escalates no-shows or unfit audiences to customer training coordinator and project lead. |

### Customer Success owner

| | |
|--|--|
| **Responsibilities** | Receive hypercare transition; own post-implementation relationship and expansion posture; ensure Support knows the customer. |
| **Decisions owned** | Post-transition engagement model (check-ins, expansion timing)—not go-live cutover mechanics. |
| **Required participation** | Late hypercare; transition meeting; as needed during go-live for relationship continuity. |
| **Expected deliverables** | Accepted handoff; named Support/CS path for the customer after Phase 8. |
| **Escalation** | Escalates adoption or relationship risk to Thin Line executive sponsor; routes production defects through Support after transition. |

### Executive sponsor (Thin Line), when applicable

| | |
|--|--|
| **Responsibilities** | Unblock commercial or political deadlocks; protect delivery capacity commitments; approve material scope changes with Sales. |
| **Decisions owned** | Whether Thin Line accepts out-of-scope work; executive-level date or fee tradeoffs. |
| **Required participation** | Escalations; optional kickoff/go-live for strategic accounts. |
| **Expected deliverables** | Written decisions on escalated items. |
| **Escalation** | Final Thin Line escalation for the engagement. |

---

## Customer roles

### Executive sponsor

| | |
|--|--|
| **Responsibilities** | Authority for the agency’s commitment to the project; remove internal customer blockers. |
| **Decisions owned** | Go-live authorization at the executive level when required by the agency; major scope or timing changes. |
| **Required participation** | Kickoff (recommended); go-live approval; escalation path when the project lead cannot unblock. |
| **Expected deliverables** | Named project lead and acceptance authority; timely decisions on escalations. |
| **Escalation** | Escalates within the agency; engages Thin Line executive sponsor on commercial disputes. |

### Customer project lead

| | |
|--|--|
| **Responsibilities** | Single accountable customer coordinator; drive customer tasks; keep Thin Line informed. |
| **Decisions owned** | Day-to-day customer prioritization within executive guidance; who attends which sessions. |
| **Required participation** | Kickoff through hypercare; primary customer voice on the board. |
| **Expected deliverables** | Customer task completion; meeting attendance; consolidated customer questions. |
| **Escalation** | Escalates to customer executive sponsor when peers do not deliver; flags Thin Line delays clearly. |

### Technical or IT contact

| | |
|--|--|
| **Responsibilities** | Network, identity, device, VPN/firewall, and vendor credential logistics. |
| **Decisions owned** | Customer IT constraints (what can be allowed on their network)—not Thin Line product design. |
| **Required participation** | Infrastructure as needed; integrations/hardware; go-live technical checks. |
| **Expected deliverables** | Access, credentials, device readiness support, change windows. |
| **Escalation** | Escalates IT policy blockers to customer project lead / executive sponsor. |

### CJIS compliance contact

| | |
|--|--|
| **Responsibilities** | Agency CJIS posture for the engagement (personnel, access, and policy questions Thin Line cannot answer for them). |
| **Decisions owned** | Agency compliance acceptances related to how they use the system. |
| **Required participation** | When CJIS questions affect access, training audience, or go-live. |
| **Expected deliverables** | Timely compliance answers; named LASO/CJISO path as the agency requires. |
| **Escalation** | Escalates compliance holds to customer executive sponsor; Thin Line does not “approve” agency CJIS programs. |

### Records or RMS administrator

| | |
|--|--|
| **Responsibilities** | Records workflows, numbering preferences, code lists, report/document headers, validation participation. |
| **Decisions owned** | Operational records policy inside the agency’s authority. |
| **Required participation** | Discovery, configuration, migration validation (when in scope), training for records staff. |
| **Expected deliverables** | Configuration answers; validation sign-off inputs; trained records users. |
| **Escalation** | Escalates workflow conflicts to customer project lead. |

### Dispatch lead

| | |
|--|--|
| **Responsibilities** | CAD/dispatch workflows, call types, unit/agency practices that affect configuration and training. |
| **Decisions owned** | Dispatch operational choices for the agency. |
| **Required participation** | When CAD/dispatch is in scope: discovery, configuration, training, go-live coverage. |
| **Expected deliverables** | Call-type and workflow answers; dispatch trainee list; go-live shift readiness. |
| **Escalation** | Escalates coverage or policy conflicts to customer project lead. |

### Court, jail, code-enforcement, or other module lead (as applicable)

| | |
|--|--|
| **Responsibilities** | Module-specific workflows, defaults, and acceptance for that product area. |
| **Decisions owned** | Operational decisions for that module within agency authority. |
| **Required participation** | Discovery, configuration, training, and validation for that module. |
| **Expected deliverables** | Module configuration answers; trained users; module-specific acceptance inputs. |
| **Escalation** | Escalates to customer project lead when module needs conflict with agency-wide decisions. |

### Training coordinator

| | |
|--|--|
| **Responsibilities** | Schedule trainees; ensure attendance; gather role lists. |
| **Decisions owned** | Who attends which session (within sponsor guidance). |
| **Required participation** | Training planning and delivery window. |
| **Expected deliverables** | Rosters; attendance; makeup plan for misses. |
| **Escalation** | Escalates no-shows to project lead before go-live. |

### Final acceptance authority

| | |
|--|--|
| **Responsibilities** | Formally accept migration (when in scope), training readiness, and go-live. |
| **Decisions owned** | Customer acceptance and go/no-go for production use. |
| **Required participation** | Acceptance reviews; go-live decision. |
| **Expected deliverables** | Written acceptance (email, form, or workspace decision record). |
| **Escalation** | May be the executive sponsor or a written delegate; if unclear, Implementation stops at the gate. |

Often the executive sponsor and final acceptance authority are the same person. If not, name both in the workspace.

---

## RACI matrix

**R** = Responsible (does the work) · **A** = Accountable (one owner of the outcome) · **C** = Consulted · **I** = Informed  

Thin Line roles abbreviated: **SO** Sales owner · **IL** Implementation lead · **TE** Technical/engineering owner · **DM** Data migration owner · **TR** Training owner · **CS** Customer Success owner · **ES-T** Thin Line executive sponsor  

Customer roles abbreviated: **ES-C** Executive sponsor · **PL** Project lead · **IT** Technical/IT · **AA** Final acceptance authority · **ML** Module/records/dispatch leads (as applicable) · **TC** Training coordinator  

| Activity | SO | IL | TE | DM | TR | CS | ES-T | ES-C | PL | IT | AA | ML | TC |
|----------|:--:|:--:|:--:|:--:|:--:|:--:|:----:|:----:|:--:|:--:|:--:|:--:|:--:|
| Sales handoff | A/R | C | I | I | | | I | I | I | | | | |
| Kickoff | C | A/R | C | C | C | I | I | C | A/R* | C | C | C | C |
| Infrastructure | I | A | R/C | I | | | I | I | C | C | | | |
| Migration | I | A | C | R | | | I | I | C | C | C | C | |
| Configuration | I | A | C | C | I | | I | I | C | I | I | R/C | I |
| Integrations | I | A | R/C | I | | | I | I | C | R/C | I | C | |
| Training | I | A | I | I | R | I | I | I | C | I | C | C | R |
| Go-live approval | I | R | C | C | C | C | C | C | C | C | A | C | I |
| Hypercare | I | A/R | C | C | C | C | I | I | C | C | I | C | I |
| Transition to support | I | R | I | I | I | A | I | I | C | I | I | I | I |

\* At kickoff, Thin Line Implementation lead is **A** for Thin Line outcomes; customer **Project lead** is **A** for customer-side outcomes. Both must agree the phase can exit.

Notes:

- If migration or integrations are **N/A**, those rows do not apply.  
- **ES-T** participates when escalated or for strategic accounts.  
- Module leads (**ML**) are Consulted/Responsible only for their product areas.  

---

## Naming owners in the workspace

At kickoff, record real names for:

| Required | Role |
|----------|------|
| Always | Thin Line implementation lead |
| Always | Customer project lead |
| Always | Final acceptance authority |
| When migration in scope | Data migration owner |
| When integrations/hardware in scope | Technical owner + customer IT contact |
| Recommended | Sales owner, Training owner, Customer Success owner (for transition) |

See [Implementation workspace standard](implementation-workspace-standard.md) · [Kickoff and discovery](kickoff-and-discovery.md).

---

## Related

| Document | Role |
|----------|------|
| [Implementation overview](implementation-overview.md) | Principles and completion |
| [Implementation lifecycle](implementation-lifecycle.md) | Phase gates |
| [Implementation workspace standard](implementation-workspace-standard.md) | Status values and visibility |
| [Sales handoff](sales-handoff.md) | Handoff packet |
| [Hypercare and transition](hypercare-and-transition.md) | Handoff to Operate / CS |

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-17 | Initial RACI stub |
| 2026-07-17 | Full Thin Line + customer roles, principles, RACI matrix |
| 2026-07-17 | Specialist responsibilities as hats; default to Implementation lead |
