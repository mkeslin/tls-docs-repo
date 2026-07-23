# Prepare proposal

**Document type:** SOP  
**Phase:** Acquire · Proposal  
**Status:** v0.1  
**Next review:** <mark style="color:red;">**TODO:**</mark> set date (owner: Acquire)  
**Audience:** Internal — Acquire  
**Related:** [Proposal](../../customer-value-engine/acquire/proposal.md) · [SaaS pricing and discount guardrails](../../policies/saas-pricing-and-discount-guardrails.md) · [Acquire authority](../../policies/acquire-authority.md) · [Execute contract](execute-contract.md) · [Migration Pricing Policy](../../policies/migration-pricing.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Issue a clear, standard-scope proposal without founder involvement when pricing is in-card |
| **Typical duration** | 2–4 hours assemble; **48 business hours** SLA from demo complete when in-card |
| **Owner (role)** | Acquire |
| **Stakeholders** | Founders (exceptions), prospect |
| **Success criteria** | Proposal sent; Pipedrive updated; pricing path documented (in-card or approved exception) |
| **Related** | [Execute contract](execute-contract.md) |

---

## Responsibility swimlane

| Step | Acquire | Founder | Prospect |
|------|---------|---------|----------|
| Assemble from template + discovery | Owns | — | — |
| Price within card | Owns | — | — |
| Price / scope exception | Prepares ask | Approves / rejects | — |
| Migration quote | Flags TBD or assessment | Per migration policy | Provides legacy info |
| Send proposal | Owns | — | Reviews |

---

## 1. Purpose

Turn demo outcomes into a **repeatable proposal** using templates and the pricing card, so every deal is not a custom fire drill.

## 2. Scope

**In scope:** Drafting and sending the commercial proposal (Word or approved format); documenting assumptions; logging in Pipedrive.

**Out of scope:** Contract/e-sign (next SOP); binding migration quotes before assessment allows; legal redlines.

## 3. Owner

**Role:** Acquire  
**Current incumbent:** Fugate  

## 4. Trigger

Demo (or equivalent discovery) complete with go-ahead to propose; or expansion quote for existing customer under same rules.

## 5. Preconditions

- Discovery notes sufficient (modules, rough size, timeline)  
- Access to proposal template (<mark style="color:red;">**TODO:**</mark> path)  
- [SaaS pricing and discount guardrails](../../policies/saas-pricing-and-discount-guardrails.md) card filled enough to quote **or** founder approval in hand  
- Packaging matches [Go-to-market](../../strategy/go-to-market.md)  

## 6. Inputs

| Input | Source |
|-------|--------|
| Demo / discovery notes | Pipedrive |
| Pricing card | SaaS pricing policy |
| Proposal template | <mark style="color:red;">TODO</mark> storage location |
| Migration stance | N/A · TBD after assessment · approved tier |

## 7. Outputs

- Proposal document sent to prospect  
- Pipedrive: proposal out date, link/file location, amount/term summary, next follow-up activity  
- Exception approvals noted when used  

## 8. Tools

| Tool | Use |
|------|-----|
| Microsoft Word (current CVE tooling) | Proposal body |
| Pipedrive | Tracking |
| Email / Teams | Delivery |
| Pricing card | Numbers |

## 9. Current state

Proposals are customized in Word; maturity listed as 3 in CVE but kit/path not fully documented for Acquire-only execution. Cycle 2–4 hours when information is ready; delays when pricing/scope need founder.

## 10. Target state

Most proposals are template + pricing card within 48 business hours of demo; founder only for floor breaches, custom scope, or migration binding quotes.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| List prices not in GitBook yet | Fill pricing card or private sheet link |
| Template location tribal | Document path + version |
| Migration quoted ad hoc | Force assessment language |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Underpricing | Discount bands + approval |
| Over-promising product | No custom features in proposal |
| Migration surprise later | Explicit migration section |
| Silent scope (integrations/hardware) | Call out in/out / TBD |

## 13. Decision trees

```text
Ready to propose?
    │
    ├─ Pricing within card + standard scope ──► Draft → send → follow up
    │
    ├─ Needs discount below Acquire band ──► Founder approval → then send
    │
    ├─ Custom product / non-ICP packaging ──► Founder; may stop deal
    │
    └─ Migration fee requested now ──► “After assessment” OR approved tier only
```

## 14. Time expectations

| Step | Target |
|------|--------|
| In-card proposal after demo | **48 business hours** |
| Escalated pricing turnaround | <mark style="color:red;">TODO</mark> founder response expectation |
| Follow-up after send | Activity at +3 to +5 business days |

## 15. Automation score

| Step | Score (1–5) |
|------|------------:|
| Template fill | 2 |
| Pricing | 2–3 when card exists |
| Send / track | 2 |

## 16. Procedure

1. **Confirm scope** — Modules, agency size basis, term, go-live hopes, migration Y/N/TBD, integrations/hardware flags.  
2. **Check authority** — [Acquire authority](../../policies/acquire-authority.md) + pricing card. Escalate before drafting if outside.  
3. **Open template** — <mark style="color:red;">**TODO:**</mark> master proposal filename/path.  
4. **Fill commercial section** — Prices from card; note any approved exception ID/date in Pipedrive.  
5. **Write assumptions** — What is included / excluded; implementation expectations at high level; migration per policy.  
6. **Internal sanity pass** — Use pricing checklist in [SaaS pricing policy](../../policies/saas-pricing-and-discount-guardrails.md).  
7. **Send** — To buyer + cc as appropriate; store file in agreed deal folder (<mark style="color:red;">TODO</mark>).  
8. **Pipedrive** — Stage = Proposal out; next activity = follow-up; attach or link proposal.  
9. **Follow up** — Per activity; if accepted → [Execute contract](execute-contract.md).  

### Proposal template pointers

| Element | Guidance |
|---------|----------|
| Agency / contacts | From Pipedrive |
| Modules | Only what was demoed / agreed |
| Pricing table | From card |
| Term | Standard unless approved |
| Migration | N/A · TBD after assessment · approved amount |
| Validity | <mark style="color:red;">TODO</mark> (e.g. 30 days) |
| Next step | Contract via Dropbox Sign |

## 17. Verification

- [ ] Scope matches demo notes  
- [ ] Pricing in-card or approval logged  
- [ ] Migration language correct  
- [ ] Sent + Pipedrive updated  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| Prospect asks for custom features in writing | Remove; escalate; do not send as-is |
| Numbers disputed | Re-check card; founder if strategic |
| Stale proposal | Re-validate pricing before re-send |

## 19. KPIs

| KPI | Definition |
|-----|------------|
| Time demo → proposal | Business hours |
| % proposals without founder touch | In-card share |
| Proposal → contract rate | Downstream |

## 20. Related documents

- [Run product demo](run-product-demo.md)  
- [Execute contract](execute-contract.md)  
- [SaaS pricing and discount guardrails](../../policies/saas-pricing-and-discount-guardrails.md)  
- [Migration Pricing Policy](../../policies/migration-pricing.md)  

---

## Continuous improvement

### Weaknesses

- Master template and list prices still TODO  

### Automation opportunities

- Proposal generator / CPQ later; Pipedrive quote fields  

### Product impact

- Clear module packaging pages reduce proposal ambiguity  

### Process maturity

| Item | Value |
|------|--------|
| Current | ~2–3 (practice exists; kit incomplete) |
| Next milestone | 48h in-card proposals without founder |
| Future | Near-instant standard quotes |

### Change history

| Date | Change |
|------|--------|
| 2026-07-22 | v0.1 — initial SOP |
