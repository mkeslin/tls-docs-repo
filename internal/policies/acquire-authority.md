# Acquire authority matrix

**Document type:** Policy (operating)  
**Status:** v0.4 — <mark style="color:red;">Draft</mark>  
**Audience:** Internal — Acquire, founders  
**Related:** [Go-to-market](../strategy/go-to-market.md) · [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md) · [Run product demo](../sops/acquire/run-product-demo.md) · [Prepare proposal](../sops/acquire/prepare-proposal.md) · [Execute contract](../sops/acquire/execute-contract.md)

> Working matrix from founder input (2026-07). Confirm any row that should differ before treating as final.

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
| Run standard **RMS/CAD** demo | Yes | Deep custom workflows not in kit |
| Demo **Court** or **Jail** | Schedule / co-facilitate | **Pull in founder for now** (until Court/Jail demo kit is Acquire-ready) |
| Discover needs / log in Pipedrive | Yes | — |
| Issue proposal **within** pricing card + standard scope | Yes — quote **list price**; close in **normal close range**; at/above ordinary min / band floor | Court **$5k** or custom; LE below ordinary min; Jail **41+**; hidden concessions; skip combined-package upgrade; 41+ officers |
| Quote **migration** fee | Yes within migration-type table after assessment ([SaaS pricing](saas-pricing-and-discount-guardrails.md)) | Multi-source / custom, $0 waiver, or hard number demanded before assessment |
| Included training + priced extras from training table | Yes | Waiving paid extras to $0 / nonstandard package |
| Promise custom features / one-off development | **Never** | Always |
| Send standard SaaS + CJIS packet (Dropbox Sign) | Yes — **Eric signs for Thin Line first**, then agency | Customer redlines; non-standard SLAs/terms |
| CJIS / security addendum path | Include whenever the agency deals with **criminal justice information** (typical LE / Jail / Court); Eric (TLS) + chief (agency) | Explicitly no-CJI edge cases; unusual agency requirements |
| 3-year ≤5% / 5-year ≤8% term discount with prepay or non-cancellable | Yes if still at/above **strategic floor** | Deeper discount; waive/freeze escalator; no commitment |
| State annual escalator on order form (default 5%) | Yes | Silent renewal pricing; 0% escalator |
| Accept deal outside ICP (e.g. standalone court today) | No | Yes |
| Sales handoff to Implementation | Yes (checklist) | Scope disputes after signature |

---

## Turnaround expectations (standard path)

| Trigger | Target |
|---------|--------|
| Hot / qualified lead → demo offered | Same day or next business day |
| Demo complete → proposal out (in-card pricing) | **48 business hours** |
| Escalated pricing / discount decision from founder | Usually **under 24 hours** |
| Verbal/email accept of proposal → contract sent | **24–48 business hours** |
| Customer redline received | Escalate within **1 business day** with summary of asks |

Missed SLAs should be visible in Pipedrive (overdue activities), not discovered at the weekly review.

---

## Pipedrive pipeline stages (live)

Canonical deal stages (confirmed from live Pipedrive, 2026-07). Advance only when exit criteria are met. There is **no separate Contract / Won column** — contracting happens in **Proposal Sent/Decision Pending**; after full execution, move to **Onboarding Scheduled/Started**.

| Stage | Meaning | Exit before advancing |
|-------|---------|------------------------|
| **Dialog Established** | Conversation underway; org/deal logged | ICP fit noted; buyer/contact; next activity set; ready to schedule demo (or nurture/disqualify) |
| **Demo Scheduled** | Live demo on the calendar | Date/time; attendees; modules; demo env OK (`demo` / `demo2` or provisioned tenant) |
| **Demo Completed** | Demo held | Same-day notes logged; proposal go/no-go; next activity set |
| **Proposal Sent/Decision Pending** | Proposal out and/or decision / contract in flight | Proposal file/link + send date; pricing path documented; while here: Dropbox Sign may be sent and tracked; do **not** advance until terms are accepted **and** packet is fully executed (or deal lost) |
| **Onboarding Scheduled/Started** | Won — implementation path started | Executed docs in Pipedrive + SharePoint; [Sales handoff](../sops/deliver/sales-handoff.md) checklist started |

**Hygiene:** every open deal has a next activity; stage name matches reality (e.g. do not leave deals in Demo Scheduled after the call happens).

---

## Related

- [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md)  
- [Migration Pricing Policy](migration-pricing.md)  
- [Sales handoff](../sops/deliver/sales-handoff.md)
