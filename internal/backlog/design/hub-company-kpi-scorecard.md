---
title: "Hub company KPI scorecard hierarchy"
status: draft
created: 2026-08-02
modules: [Hub, Desks, Funding RT]
backlog: []
---

# Design: Hub company KPI scorecard hierarchy

## Goal

Keep the full Funding RT metric catalog in Hub, but present a **focused biweekly company scorecard** (12–15 measures). Everything else stays as **operating metrics** (drill-down) or **strategic milestones** (not perpetual recurring KPIs).

Automation remains prefill → human review → immutable confirmation. Prefill never overwrites entered Actuals. Confirmed snapshots must not recalculate when formulas later change.

## Hierarchy

| Layer | Purpose | Count |
|-------|---------|-------|
| **Company scorecard** | Biweekly review: where to look | 12–15 |
| **Operating metrics** | Why a scorecard cell is red/yellow | Rest of catalog, by category |
| **Milestones** | Strategic projects (Court GA, Jail GA) while active | Few; status + % complete |
| **Source records** | What happened (deals, tickets, releases) | Systems of record |

Scorecard tells you where to look. Operating metrics tell you why. Source records tell you what happened.

## Biweekly company scorecard (recommended)

| Category | KPI |
|----------|-----|
| Growth | ARR |
| Growth | ARR added **quarter-to-date** (period add as drill-down) |
| Growth | Weighted pipeline coverage |
| Growth | New qualified opportunities (**rolling 30 days**) |
| Growth | Win rate (trailing 12 months) |
| Product | Strategic product milestones on track |
| Product | Open critical production defects |
| Customer | Active implementations vs capacity |
| Customer | Go-lives quarter-to-date (**manual** until authoritative date/status) |
| Customer | Implementation cycle time |
| Customer | Customer satisfaction (avg + response count) |
| Operations | Tenant deployment time |
| Operations | Data-conversion effort |
| Operations | Founder implementation hours (raw hours preferred) |
| Market | Referral-sourced qualified opportunities |

Move off the primary screen (keep as operating metrics): proposals outstanding, high-priority bugs, production deployments, training completion, conferences, speaking, customer stories, % automated deployments, internal documentation complete.

## Formula corrections (accepted)

### Weighted pipeline coverage

**Correct:** `weighted open pipeline ÷ remaining ARR gap`  
where gap = `$250K target − current Hub ARR`.

Example: ARR $205K, gap $45K, weighted pipeline $90K → **2.0×**.

Also exclude open deals whose **expected close** is outside the planning horizon (current calendar year). Deals with unset expected close remain included.

Implemented in TLS-Hub (`KpiPrefillCoordinator` + Pipedrive horizon filter).

### Go-lives

**Do not** prefill from Pipedrive Closed Won. That measures sales success, not delivery success.

Leave **manual** until one of: GoLiveDate in Pipedrive, completed implementation phase in Hub, or client environment production-activation status.

Implemented: collector removed; catalog marked non-collectable.

## Definition sharpening (next waves)

| Topic | Direction |
|-------|-----------|
| ARR added | Scorecard = **QTD** vs quarterly target; plan-period add as supporting detail. Prefer contract-executed / committed recurring ARR (Hub/Pipedrive) over Stripe created-at when they diverge. |
| New qualified opps | Align target to window (1–2 / two weeks **or** rolling 30-day actual). Require explicit qualification rules, not merely “left lead stage.” |
| Customer-requested features | Rename toward **roadmap / strategic delivery**; avoid rewarding reactive ticket volume. |
| Production deployments | Prefer “days since last release” / on-cadence status over raw release counts. |
| Implementations in progress | Capacity bands (e.g. green 1–2) not a fixed “2 forever.” |
| Avg implementation days | Segment by complexity; clock from implementation-ready → go-live; track customer-wait separately later. |
| CSAT | Show average **and** response count. |
| Support response | Median / P90; first **meaningful human** response. |
| Documentation | Controlled process inventory as denominator. |
| Founder hours | Prefer raw plan-period hours over unstable % of total. |
| Referrals | Structured Pipedrive lead source / referring customer — not title text match. |
| Court / Jail GA | Model as **milestone health** (On track / At risk / Off track) + supporting %; remove from recurring scorecard when complete. |

## Metric metadata (Hub model target)

Each metric should eventually carry: metric type (stock/flow/rate/milestone/status), target horizon, actual window, source, source status (current/stale/unavailable/fallback), confidence (authoritative/proxy/estimated/manual), last refreshed, formula version, owner, notes, confirmed by/date.

Visible badge when fallback/proxy was used (e.g. Stripe authoritative vs Pipedrive fallback).

## Snapshot immutability

Confirmed periods store Actual, Target, formula version, source, source window, human adjustment, and confirmation metadata. Later formula changes must not rewrite history.

## Implementation status

| Item | Status |
|------|--------|
| Pipeline coverage ÷ remaining gap + year horizon | Done (Hub) |
| Remove Closed Won go-live prefill | Done (Hub) |
| Scorecard vs operating UI split | Not started |
| Milestone type for Court/Jail GA | Not started |
| ARR QTD vs plan-period split | Not started |
| Metadata / confidence badges | Not started |
| Qualification rules / referral fields | Depends on Pipedrive hygiene |

## Related

- TLS-Hub: `CompanyKpiCatalog`, `KpiPrefillCoordinator`, `PipedriveDealMetricsService`, Desks Overview Scorecard / Trends tabs.
- Desk designs: [Acquire](hub-acquire-desk.md), [Deliver](hub-deliver-desk.md), [Operate](hub-operate-desk.md), [Expand](hub-expand-desk.md), [Advocate](hub-advocate-desk.md).
