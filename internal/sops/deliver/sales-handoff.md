# Sales handoff

**Lifecycle step:** 0 · Sales handoff  
**Document type:** Phase overview  
**Status:** v0.2  
**Audience:** Internal — Acquire (Sales) and Implementation  

Engagement status: ☐ Not started · ☐ In progress · ☐ Complete

CVE stage: [Sales handoff](../../customer-value-engine/deliver/sales-handoff.md)  
Checklist: [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md)  
Upstream: [Execute contract](../acquire/execute-contract.md)

---

## Purpose

Transfer a **signed** customer from Acquire to Implementation with enough commercial and scope clarity to start kickoff without re-discovering the deal.

---

## RACI (working)

| Activity | Acquire (Sales) | Implementation | Founder |
|----------|-----------------|----------------|---------|
| Complete handoff checklist | **R** | C | I |
| Attach / link executed contract | **R** | I | I |
| Confirm modules + migration flags | **R** | C | C if dispute |
| Accept ownership / capacity | C | **R** | A if conflict |
| Open engagement workspace | I | **R** | — |
| Schedule kickoff | C | **R** | — |
| Scope vs contract dispute | C | C | **A** |

R = Responsible · A = Accountable · C = Consulted · I = Informed

---

## Inputs

| Input | Source |
|-------|--------|
| Signed SaaS (+ CJIS path as required) | [Execute contract](../acquire/execute-contract.md) |
| Scope summary (modules, migration Y/N, integrations, hardware) | Proposal / contract / Pipedrive |
| Contacts (customer + Sales) | Pipedrive |
| Migration assessment status (if any) | [Legacy System Migration Assessment](../../assessments/legacy-system-migration-assessment.md) |
| Pricing / fee commitments | Proposal; [Migration Pricing Policy](../../policies/migration-pricing.md); [SaaS pricing guardrails](../../policies/saas-pricing-and-discount-guardrails.md) |

---

## Pipedrive / CRM fields (minimum)

Create/use the GTM custom fields ([Go-to-market](../../strategy/go-to-market.md)). At handoff:

| Field / concept | Required at handoff |
|-----------------|---------------------|
| Deal / org | Yes |
| **Modules of interest** (final sold scope in notes) | Yes |
| Migration Y/N/TBD (note + assessment link if any) | Yes |
| Executed contract link / file location | Yes |
| Primary customer contact | Yes |
| **Sworn officers** / **Rated beds** / **Citations / month** as applicable | Yes when that product sold |
| **Market-share program** used (if any) | Yes |
| Target go-live window (if known) | Preferred |
| Known risks | Yes (even if “none”) |

---

## Activities

1. Acquire completes [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md) (commercial, scope flags, contacts, risks).  
2. Acquire notifies Implementation owner (Teams/email + Pipedrive).  
3. Implementation confirms capacity and **accepts** ownership (date on checklist).  
4. Implementation opens the engagement per [Creating a new implementation](creating-a-new-implementation.md).  
5. Kickoff scheduled; Acquire joins for commercial Q&A as needed ([Roles](implementation-roles-and-responsibilities.md)).  

If checklist items are unknown, mark **Unknown** and schedule discovery — do not invent scope.

---

## Outputs

- Handoff acknowledged by Implementation  
- Kickoff scheduled  
- Open questions / risks listed  

---

## Exit criteria

- [ ] Contract / commercial path is clear enough to proceed  
- [ ] Implementation has accepted ownership  
- [ ] Kickoff date set  
- [ ] Migration, integrations, and hardware in/out of scope stated  
- [ ] [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md) complete  

---

## Referenced SOPs / standards / checklists

| Doc | Role |
|-----|------|
| [Execute contract](../acquire/execute-contract.md) | Upstream Acquire |
| [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md) | Checklist |
| [Acquire authority](../../policies/acquire-authority.md) | Escalation for scope fights |
| [Implementation overview](implementation-overview.md) | Parent |
| [Kickoff and discovery](kickoff-and-discovery.md) | Next phase |

**Previous:** [Execute contract](../acquire/execute-contract.md) · **Next:** [Kickoff and discovery](kickoff-and-discovery.md)

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-22 | v0.2 — RACI, Pipedrive minimums, link to Acquire contract SOP |
| — | v0.1 placeholder |
