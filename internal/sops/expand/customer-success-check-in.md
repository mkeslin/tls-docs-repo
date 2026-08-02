# Customer success check-in

**Document type:** SOP  
**Phase:** Expand · Customer success  
**Status:** v0.1 (target-state)  
**Next review:** 2026-10-01 (owner: Expand)  
**Audience:** Internal — Expand owner, Support, Deliver (handoff)  
**Related:** [Customer success (CVE)](../../customer-value-engine/expand/customer-success.md) · [Deliver → Expand handoff](deliver-to-expand-handoff.md) · [Expand account](expand-account.md) · [Customer success check-in checklist](../../checklists/customer-success-check-in-checklist.md) · [Account health / risk checklist](../../checklists/account-health-risk-checklist.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Keep live customers healthy: confirm adoption, surface risk early, and open expansion only when appropriate |
| **Typical duration** | 20–40 minutes prep + call; 10 minutes to log |
| **Owner (role)** | Expand owner |
| **Success criteria** | Health score recorded; cadence met; Pipedrive activity logged; at-risk accounts have a dated next action ≤ 14 days |
| **Related** | [Expand account](expand-account.md) · [Hub Expand Desk](../../backlog/design/hub-expand-desk.md) |

---

## Responsibility swimlane

| Step | Expand owner | Support | Deliver | Customer |
|------|--------------|---------|---------|----------|
| Maintain cadence list | Owns | Surfaces pain spikes | Hands off at hypercare exit | — |
| Run check-in | Owns | May join if open issues | — | Attends / responds |
| Health / risk score | Owns | Advises ticket history | Advises go-live context | — |
| Log Pipedrive activity | Owns | — | — | — |
| Open expansion path | Owns (if healthy or inquiry) | — | — | May inquire |
| Escalate product / billing | Routes | Owns product bugs per triage | — | — |

---

## 1. Purpose

Make post-go-live success **repeatable**: every live account has a known health state, a next touch date, and a clear owner — without waiting for a crisis.

## 2. Scope

**In scope:** Scheduled and triggered check-ins for live (post-hypercare) customers; health scoring; at-risk recovery planning; logging in Pipedrive; optional expansion handoff to [Expand account](expand-account.md).

**Out of scope:** Hypercare day-to-day support ([Triage](../operate/triage-support-request.md) / Deliver); pre-sales; running the full expansion sale (see Expand account).

## 3. Owner

**Expand owner** — owns cadence, scoring, and Pipedrive logging for success.

## 4. Trigger

- Cadence due (see Time expectations)  
- Support or founder flags risk  
- Customer inquiry that implies adoption or expansion  
- Completing [Deliver → Expand handoff](deliver-to-expand-handoff.md)

## 5. Preconditions

- Agency is **live** (or hypercare exit completed / handoff done)  
- Expand owner has Pipedrive org access  
- Recent Support context available when scoring risk  

## 6. Inputs

| Input | Source |
|-------|--------|
| Last check-in / notes | Pipedrive activity |
| Open tickets / severity | Shared support log / Support |
| Modules in contract | Hub / contract / Pipedrive |
| Champion / contacts | Pipedrive / Hub |

## 7. Outputs

- Health band: **Healthy** · **Watch** · **At-risk**  
- Pipedrive **activity** on the org (summary + next step)  
- Next check-in date on the cadence  
- If At-risk: recovery next action ≤ 14 days  
- If expansion appropriate: follow [Expand account](expand-account.md)

## 8. Tools

| Tool | Use |
|------|-----|
| Hub Expand Desk | Coaching plan + checklists |
| Pipedrive | SoR for activities and opportunities |
| Email / Quo | Preferred customer channels |
| Support log | Ticket history for risk scoring |

## 9. Current state

Periodic / founder-driven check-ins; little formal scoring; opportunities often reactive. Maturity 1.

## 10. Target state

Every live account has a **health band**, a **next touch date**, and a Pipedrive activity trail. New accounts taper from monthly post-hypercare to quarterly. At-risk never sits without a dated next action. Expansion is intentional (healthy check-in or customer inquiry), not vibes.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| Ad hoc check-ins | Cadence table below + Hub plan priorities |
| No shared health language | [Account health / risk checklist](../../checklists/account-health-risk-checklist.md) |
| Notes in heads / chat | Pipedrive activity every check-in |
| Expansion only when loud | Offer modules when Healthy (or inquiry) |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Check-in becomes a support dump | Park P1/P2 to Support triage; keep Expand on adoption / relationship |
| False “healthy” | Require risk checklist when any red flag appears |
| At-risk without next step | Hard rule: ≤ 14 days next action |
| Pitching while on fire | No expansion conversation while At-risk unless customer initiates |

## 13. Decision trees

```text
Cadence bucket?
    │
    ├─ Post-hypercare new account (first 90 days after handoff)
    │     ──► Day 30 · Day 60 · Day 90, then quarterly
    │
    ├─ At-risk
    │     ──► At least monthly until Healthy for 2 consecutive check-ins
    │           + next action ≤ 14 days always
    │
    └─ Healthy / Watch
          ──► Quarterly (Watch: prefer earlier if signals worsen)
```

```text
After scoring health?
    │
    ├─ At-risk ──► Recovery plan + dated next action; no Expand pitch
    │                (unless customer asks — then acknowledge and schedule later)
    │
    ├─ Watch ──► Address gaps; keep quarterly or pull forward
    │
    └─ Healthy ──► Optional expansion probe → Expand account SOP if interest
```

## 14. Time expectations

| Segment | Cadence |
|---------|---------|
| **Healthy** | Quarterly |
| **Watch** | Quarterly (default); pull forward if new red flags |
| **At-risk** | Monthly minimum until Healthy × 2; next action ≤ 14 days |
| **New after hypercare** | Day **30 / 60 / 90**, then follow health band (usually quarterly) |

Check-in call: target **30 minutes**. Log same day.

## 15. Automation score

| Step | Today | Target |
|------|------:|-------:|
| Cadence reminders | 1 | 3 (Hub plan / calendar) |
| Health scoring | 1 | 3 |
| Pipedrive log | 1 | 3 |
| Risk from tickets | 1 | 4 (later) |

## 16. Procedure

### A. Prepare

1. Confirm cadence bucket (new / healthy / watch / at-risk).  
2. Skim last Pipedrive notes, open Support items, modules in use vs contracted.  
3. Run or refresh [Account health / risk checklist](../../checklists/account-health-risk-checklist.md).  
4. Book or confirm touch (call preferred; email/Quo OK if customer constrained).

### B. Conduct check-in

Use [Customer success check-in checklist](../../checklists/customer-success-check-in-checklist.md):

1. Relationship / champion still valid?  
2. Adoption: are sold modules in daily use? Training gaps?  
3. Friction: recurring Support themes (without taking over triage).  
4. Outcomes: are they getting the operational win they bought?  
5. If **Healthy** (or customer inquires): light expansion probe — “Any modules or sites on the radar?”  
6. Agree **next step** and date.

### C. Log and schedule

1. Pipedrive **activity** on the org: health band, summary, next step, next check-in date.  
2. If At-risk: set next activity ≤ 14 days; add to Expand two-week plan priorities.  
3. If expansion interest: [Expand account](expand-account.md) (create opportunity).  
4. Update Hub Expand plan day-block / priority as needed.

## 17. Verification

- [ ] Health band recorded (Healthy / Watch / At-risk)  
- [ ] Pipedrive activity logged same day  
- [ ] Next check-in date set per cadence  
- [ ] At-risk ⇒ next action ≤ 14 days  
- [ ] Expansion path started only if Healthy or customer inquiry  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| Customer unresponsive 2× | Escalate via known champion + Support context; mark Watch/At-risk |
| Contract / billing dispute | Founder + billing path; Expand stays relationship owner |
| Product defect blocking adoption | Support triage + product; Expand tracks adoption unblock |

## 19. KPIs (starting)

| KPI | Definition |
|-----|------------|
| % live accounts with next check-in date | Target → 100% |
| At-risk with next action ≤ 14 days | Target → 100% |
| Check-ins completed vs plan | Expand two-week goals |

## 20. Related documents

- [Customer success check-in checklist](../../checklists/customer-success-check-in-checklist.md)  
- [Account health / risk checklist](../../checklists/account-health-risk-checklist.md)  
- [Deliver → Expand handoff](deliver-to-expand-handoff.md)  
- [Expand account](expand-account.md)  
- [Two-week expand plan](../../templates/expand-plan-two-week.md)  

---

## Continuous improvement

### Weaknesses

- No automated usage signals yet — scoring is judgment + Support history  
- Cadence depends on Expand owner discipline  

### Next review date

2026-10-01  
