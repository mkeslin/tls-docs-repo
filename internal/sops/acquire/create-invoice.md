# Create invoice

**Document type:** SOP  
**Phase:** Acquire · Invoice  
**Status:** v0.1  
**Next review:** 2026-10-01 (owner: Finance / founder)  
**Audience:** Internal — Finance (day-to-day), Acquire (commercial handoff)  
**Related:** [Invoice](../../customer-value-engine/acquire/invoice.md) · [Execute contract](execute-contract.md) · [SaaS pricing and discount guardrails](../../policies/saas-pricing-and-discount-guardrails.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Start the financial relationship promptly after signature with accurate amounts and terms |
| **Typical duration** | ~10 minutes when terms are clear |
| **Owner (role)** | Finance / founder (day-to-day invoicing) |
| **Current incumbent** | Matthew Keslin |
| **Stakeholders** | Acquire (terms, deal context), customer AP |
| **Success criteria** | Invoice created in billing tools; customer notified; Pipedrive note with invoice date/amount; payment path clear |
| **Tools** | Stripe, Xero (per CVE) |

---

## Responsibility swimlane

| Step | Acquire | Finance (Keslin) | Customer |
|------|---------|------------------|----------|
| Confirm commercial terms match signed order | Owns | Confirms | — |
| Create invoice / subscription | Flags ready | Owns | — |
| Send / notify customer | May intro AP contact | Owns | Pays |
| Chase past-due | Supports relationship | Owns collections path | — |

---

## 1. Purpose

Begin billing without re-discovering the deal — invoice matches the signed proposal/order form.

## 2. Scope

**In scope:** First invoice / subscription setup after contract execution; documenting what was billed.

**Out of scope:** Collections litigation; changing commercial terms (that returns to Acquire / founder).

## 3. Trigger

Deal reaches **fully executed** contract (typically when Pipedrive moves to **Onboarding Scheduled/Started**, or same day as full signature).

## 4. Preconditions

- Executed SaaS (and exhibits) available in Pipedrive / SharePoint  
- Legal entity name, billing contact, amount, term, and escalator / year-by-year schedule known  
- Implementation / migration / one-time fees called out if invoiced separately  

## 5. Procedure

1. **Pull terms** from signed order form / proposal (annual SaaS, one-time fees, due timing — default **annual billing in advance**).  
2. **Create invoice / subscription** in Stripe and/or Xero per current finance practice.  
3. **Align one-time fees** (implementation, migration, integrations) on separate lines or separate invoices — do not bury them.  
4. **Notify** billing contact; note invoice ID/date/amount on the Pipedrive deal.  
5. **If payment timing is unclear** (PO, council calendar), set a Pipedrive activity to follow up; do not assume silence means paid.  

## 6. Verification

- [ ] Amounts match signed commercial terms  
- [ ] Annual vs one-time lines correct  
- [ ] Pipedrive note added  
- [ ] Customer has a clear pay / AP path  

## 7. Failure and escalation

| Situation | Action |
|-----------|--------|
| Terms ambiguous vs signature | Pause invoice; Acquire clarifies with founder if needed |
| Customer disputes amount | Finance + Acquire; do not silently rewrite the deal |
| Non-payment past notice period | Per SaaS agreement; founder for suspension decisions |

## 8. Related documents

- [Execute contract](execute-contract.md)  
- [SaaS pricing and discount guardrails](../../policies/saas-pricing-and-discount-guardrails.md)  
- [Contract terms](../../policies/saas-pricing-and-discount-guardrails.md#contract-terms)  
