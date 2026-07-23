# Acquire authority matrix

**Document type:** Policy (operating)  
**Status:** v0.1 — <mark style="color:red;">Draft</mark>  
**Audience:** Internal — Acquire, founders  
**Related:** [Go-to-market](../strategy/go-to-market.md) · [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md) · [Run product demo](../sops/acquire/run-product-demo.md) · [Prepare proposal](../sops/acquire/prepare-proposal.md) · [Execute contract](../sops/acquire/execute-contract.md)

> <mark style="color:red;">**Decision needed:**</mark> Founder confirmation of each row before treating this as binding. Amounts and named signers intentionally left as TODOs where not yet agreed.

---

## Purpose

Define what Acquire may decide alone versus what requires founder approval, so demo → proposal → contract is not a fire drill and not silently founder-owned.

---

## Principle

**Standard path = Acquire owns end-to-end.**  
**Exception path = escalate early with a clear ask.**  
Do not promise custom product work, non-standard legal terms, or below-floor pricing without approval.

---

## Authority matrix

| Decision | Acquire owns alone | Escalate to founder |
|----------|--------------------|---------------------|
| Qualify lead against ICP | Yes | Edge cases / strategic exceptions |
| Schedule demo | Yes | Demo environment unavailable / broken |
| Run standard module demo (RMS/CAD; Court/Jail when kit ready) | Yes | Deep custom workflow demos not in kit |
| Discover needs / log in Pipedrive | Yes | — |
| Issue proposal **within** pricing card + standard scope | Yes | Below discount floor; non-standard scope |
| Quote **migration** fee | No — assessment / policy gate | Per [Migration Pricing Policy](migration-pricing.md) |
| Promise custom features / one-off development | **Never** | Always |
| Send standard SaaS contract (Dropbox Sign) | Yes | Customer redlines; non-standard SLAs/terms |
| CJIS / security addendum path | Follow standard packet | Unusual agency requirements |
| Multi-year / strategic discount beyond card | No | Yes |
| Accept deal outside ICP (e.g. standalone court today) | No | Yes |
| Sales handoff to Implementation | Yes (checklist) | Scope disputes after signature |

---

## Turnaround expectations (standard path)

| Trigger | Target |
|---------|--------|
| Hot / qualified lead → demo offered | Same day or next business day |
| Demo complete → proposal out (in-card pricing) | **48 business hours** |
| Verbal/email accept of proposal → contract sent | **24–48 business hours** |
| Customer redline received | Escalate within **1 business day** with summary of asks |

Missed SLAs should be visible in Pipedrive (overdue activities), not discovered at the weekly review.

---

## Pipedrive stage hygiene (recommended)

Advance only when exit criteria are met. Exact stage names <mark style="color:red;">**TODO**</mark> — align to live Pipedrive.

| Stage (concept) | Exit before advancing |
|-----------------|------------------------|
| Qualified | ICP fit noted; buyer/contact; budget not an immediate hard no |
| Demo scheduled | Date/time; attendees; modules; demo env OK |
| Demo complete | Notes logged; proposal go/no-go |
| Proposal out | File/link + send date; pricing path (in-card / escalated) |
| Contract out | Dropbox Sign sent; signer identified |
| Won | Fully executed; handoff checklist started |

---

## Related

- [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md)  
- [Migration Pricing Policy](migration-pricing.md)  
- [Sales handoff](../sops/deliver/sales-handoff.md)
