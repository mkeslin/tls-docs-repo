# Publish product update

**Document type:** SOP  
**Phase:** Operate · Product updates  
**Status:** v0.1  
**Next review:** 2026-10-01 (owner: Product)  
**Audience:** Internal — product owner, engineering, Support  
**Related:** [Product updates](../../customer-value-engine/operate/product-updates.md) · [Operate authority](../../policies/operate-authority.md) · [Customer release email](../../templates/customer-release-email.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Ship improvements and tell customers in a way they can use — not only dump release notes |
| **Typical duration** | Deploy 1–2 days when ready; customer comms 30–60 min when warranted |
| **Owner (role)** | Product owner decides priority/content; engineering deploys |
| **Current incumbent (priority)** | **Matthew Keslin** |
| **Success criteria** | Production updated; in-app New features current when user-visible; email sent when criteria met; Support aware |
| **Related** | [Customer release email](../../templates/customer-release-email.md) |

---

## Responsibility swimlane

| Step | Product (Keslin) | Engineering | Support |
|------|------------------|-------------|---------|
| Prioritize (module / fire / roadmap) | Owns | Advises effort | Surfaces customer pain |
| Build / test / deploy | Approves go | Owns | — |
| In-app New features blurb | Owns / approves | May draft | — |
| Customer email decision + send | Owns | — | Aware; answers follow-ups |
| Hotfix comms | Owns message | Owns deploy | Customer-facing |

---

## 1. Purpose

Connect **what we ship** to **what customers hear**, with a light email strategy on top of the existing in-app New features section.

## 2. Scope

**In scope:** Prioritization habits, release rhythm, in-app notes, customer email rules, Support briefing.

**Out of scope:** Full CI/CD redesign; marketing campaigns; Acquire sales announcements (unless product-critical).

## 3. Owner

**Product priority / customer message:** Keslin  
**Deploy execution:** Engineering (as today)

## 4. Trigger

- Planned work ready to ship  
- Hotfix / fire  
- End of a week with several user-visible changes (digest candidate)

## 5. Preconditions

- Change tested enough for production judgment  
- Know which agencies/modules are affected  
- [Customer release email](../../templates/customer-release-email.md) template available when emailing  

## 6. Inputs

| Input | Source |
|-------|--------|
| Bugs / feedback / fires | Support, customers, founders |
| Roadmap / module themes | Product |
| Build artifacts | Azure DevOps |

## 7. Outputs

- Production release  
- Updated in-app New features (when user-visible)  
- Optional customer email  
- Support heads-up  

## 8. Tools

| Tool | Use |
|------|-----|
| Azure DevOps | Work items, pipelines, releases |
| In-app New features | Always-on customer surface (improve copy quality) |
| Email | Notable updates ([template](../../templates/customer-release-email.md)) |
| Teams / verbal | Support brief |

## 9. Current state

Keslin organizes roughly by module but often responds to the loudest fire. Releases are frequent (about weekly / 1–2 day cycle when active). Customers see New features → boring release notes. No consistent email strategy. Maturity 1.

## 10. Target state

Still responsive to fires, but each ship asks: **email, in-app only, or silent?** Customer emails are short and benefit-led. Support knows what changed before the inbox lights up. Weekly engineering rhythm; customer email only when it earns attention.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| Raw release notes in-app | Rewrite New features as 2–5 bullet **benefits** |
| No email | Use send criteria below |
| Fire-only prioritization | Keep fire lane; protect one “module theme” slice per week when possible |
| Support surprised | 5-minute brief or shared “shipped today” note |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Email fatigue | Send only when criteria met; prefer monthly digest over daily pings |
| Overpromising in email | Product approves; no ship dates for unreleased work |
| Silent breaking change | Always email + Support brief |

## 13. Decision trees

```text
User-visible change shipped?
    │
    ├─ No (internal only) ──► No customer comms
    │
    └─ Yes ──► Update in-app New features (benefit language)
                │
                ├─ Security / action required / breaking / highly requested ──► Email + Support brief
                │
                ├─ Several small wins this month ──► Optional monthly digest email
                │
                └─ Minor fix / polish ──► In-app only
```

## 14. Time expectations / cadence (guided)

| Rhythm | Guidance |
|--------|----------|
| **Engineering** | Ship **when ready** — do not hold a fix for a “Tuesday train” if customers are hurting |
| **Target heartbeat** | Aim for a **weekly** ship habit when there is real user-visible work (not empty releases) |
| **Customer email** | **Event-driven** (see criteria) + optional **monthly digest** if the month was busy |
| **Hotfix** | Deploy ASAP; email only if customers must act or were impacted |

## 15. Automation score

| Step | Today | Target |
|------|------:|-------:|
| Prioritize | 1 | 2 |
| Deploy | 3–4 | 4 |
| In-app notes | 2 | 3 |
| Customer email | 1 | 3 |
| Support brief | 1 | 3 |

## 16. Procedure

1. **Prioritize** — Keslin: balance fire vs module theme; write the outcome in the work item.  
2. **Build & verify** — Engineering; smoke check affected modules.  
3. **Deploy** — Production per current pipeline practice.  
4. **In-app New features** — Replace ticket-speak with short benefit bullets (what / why it matters).  
5. **Email decision** — Use [Customer release email](../../templates/customer-release-email.md) checklist; send only if warranted.  
6. **Support brief** — Tell Gibson (and Fugate if hypercare agencies affected) what customers might ask.  
7. **Watch** — First hours/day: watch Quo/email for fallout; hot-fix if needed.

## 17. Verification

- [ ] Production confirmed  
- [ ] In-app updated when user-visible  
- [ ] Email sent **or** explicit “in-app only / silent” decision  
- [ ] Support aware  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| Bad deploy | Hotfix; customer email if impact was user-visible |
| Customer confused by email | Support + improve template |
| Fire consumes every week | Keslin protects a minimum non-fire slice or consciously defer with note |

## 19. KPIs (starting)

| KPI | Definition |
|-----|------------|
| User-visible ships / month | Count |
| Emails sent / month | Should stay low (quality > volume) |
| Support tickets in 48h after a noted release | Spike = comms or quality issue |

## 20. Related documents

- [Operate authority](../../policies/operate-authority.md)  
- [Product updates (CVE)](../../customer-value-engine/operate/product-updates.md)  
- [Triage support request](triage-support-request.md)  
- [Customer release email](../../templates/customer-release-email.md)  

---

## Continuous improvement

### Weaknesses

- New features surface still feels like engineer notes  
- No mailing list hygiene / segment by module yet  

### Automation opportunities

- Release pipeline → draft New features stub  
- Customer segment lists by module  
- “Shipped” Teams webhook for Support  

### Product impact

- Richer in-app New features (screenshots, deep links)  
- Optional release RSS / Help article  

### Process maturity

| Item | Value |
|------|--------|
| Current level | 1 |
| Next milestone | Every user-visible ship has benefit-led in-app notes + explicit email yes/no |
| Future goal | Monthly digest habit + Support never surprised |

### Next review date

2026-10-01  
