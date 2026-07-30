# Epic KPIs (two-week plan collection)

**Document type:** Operating metric set  
**Status:** v0.1  
**Audience:** Epic owners · founders  
**Related:** [Quarterly scorecard](quarterly-scorecard.md) · [Hub epic plans](../backlog/design/hub-epic-plans.md) · [Go-to-market](go-to-market.md)

## Purpose

Give every CVE epic a **small, fixed KPI set** that seeds Hub two-week plans (`SalesPlanPeriod` goals: Target / Actual). This is where we **start collecting** period-level numbers—not a BI warehouse.

- **Cadence:** each current two-week plan period (fill Actuals by Friday check-in).
- **Source:** rolled up from SOP KPI sections, GTM leading indicators, and the quarterly scorecard themes.
- **Rule:** prefer few metrics you can honestly fill; refine targets after 2–3 periods.

Hub blanks and plan templates must stay aligned with this page (manual sync when this doc bumps).

---

## Acquire

| KPI (plan goal label) | Definition | Source |
|-----------------------|------------|--------|
| New conversations started (reply, call connect, or in-person) | First meaningful reply or in-person conversation | [Generate new leads](../sops/acquire/generate-new-leads.md) |
| Association-list / outbound emails sent (ICP-filtered) | Count sent in period | GTM outbound rhythm · lead SOP |
| Demos held or scheduled | Completed sessions + firm calendar holds | [Run product demo](../sops/acquire/run-product-demo.md) · GTM |
| Referral asks completed + logged | Asks logged on customer orgs | [Capture referral](../sops/advocate/capture-referral.md) (Acquire rhythm) |
| Field / territory day (half or full) | 1 = done; 0.5 = half-day | Lead SOP · GTM |
| Pipedrive: every touched org has origin + next activity | Hygiene % for orgs touched this period | GTM |

**Starting targets (illustrative):** conversations 8 · outbound 20 · demos 2 · referral asks 3 · field day 1 · Pipedrive 100%.

---

## Deliver

| KPI (plan goal label) | Definition | Source |
|-----------------------|------------|--------|
| Engagements with a clear next action dated in the workspace | % of named priorities | [Workspace standard](../sops/deliver/implementation-workspace-standard.md) |
| Phase exits completed (or explicitly N/A with reason) | Count of phase exits this period | [Lifecycle](../sops/deliver/implementation-lifecycle.md) |
| Go-lives / cutovers this period | Count | [Go live](../sops/deliver/go-live.md) · scorecard |
| UAT / training / customer sessions completed | Count of customer-facing sessions | Training / go-live SOPs |
| Hypercare exits / Operate handoffs | Count | [Hypercare](../sops/deliver/hypercare-and-transition.md) |

Set numeric targets per period from the portfolio (do not invent false precision).

---

## Operate

| KPI (plan goal label) | Definition | Source |
|-----------------------|------------|--------|
| Support requests logged in shared list (%) | Logged / received; target → 100% | [Triage support](../sops/operate/triage-support-request.md) |
| P1 incidents this period | Count | Triage SOP |
| Time to first response (P2/P3) — sample | Hours or business hours (note sample size) | Triage SOP |
| Reopened issues | Count (quality signal) | Triage SOP |
| User-visible ships this period | Count | [Publish product update](../sops/operate/publish-product-update.md) |

---

## Expand

| KPI (plan goal label) | Definition | Source |
|-----------------------|------------|--------|
| Customer success check-ins completed | Count of structured check-ins | [Expand CVE](../customer-value-engine/expand/README.md) |
| At-risk accounts with dated next action | Count (or 100% of known at-risk) | Customer success stage |
| Expansion conversations started | Modules/sites/upsell talks started | [Expansion](../customer-value-engine/expand/expansion.md) |
| Expansion opportunities logged | Pipedrive (or equivalent) opportunities created/updated | Expand CVE |

<mark style="color:red;">**TODO:**</mark> Replace with SOP KPI tables when Expand SOPs exist.

---

## Advocate

| KPI (plan goal label) | Definition | Source |
|-----------------------|------------|--------|
| Referral asks made | Count logged on customer orgs | [Capture referral](../sops/advocate/capture-referral.md) |
| Referrals captured | New leads with origin Referral | Referral SOP |
| Referral → discovery / demo | Downstream conversions this period | Referral SOP |
| Reference champions confirmed or refreshed | Count of usable references | [Reference](../customer-value-engine/advocate/reference.md) · AOP “10 references” |

---

## Internal

Company ops (not a CVE customer phase). Starting set until Internal SOPs exist:

| KPI (plan goal label) | Definition | Source |
|-----------------------|------------|--------|
| Payroll / finance ops completed on time | Period payroll and required finance closes | Hub Internal epic (board design) |
| Employee CJIS / security items closed | Count closed this period | Internal epic |
| Internal process / tooling blockers cleared | Count | Internal epic |
| Cross-epic dependencies unblocked | Count of deps cleared for Acquire–Advocate | Internal epic |

---

## How Hub uses this

1. Creating a current plan for an epic seeds these rows into **Goals** (shown as **KPIs** in the plan UI): Label, Target, Actual.
2. Friday check-in: fill **Actual** and tick check-in items.
3. Quarterly scorecard rolls up themes; this page is the **period collection** layer.

## Change history

| Date | Change |
|------|--------|
| 2026-07-30 | v0.1 — initial sets from SOPs, GTM, scorecard themes, Deliver/Acquire plan templates |
