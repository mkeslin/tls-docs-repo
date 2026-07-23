# Capture referral

**Document type:** SOP  
**Phase:** Advocate · Referral  
**Status:** v0.1  
**Next review:** <mark style="color:red;">**TODO:**</mark> set date (owner: Advocate / Acquire)  
**Audience:** Internal — anyone closing success moments with customers  
**Related:** [Referral](../../customer-value-engine/advocate/referral.md) · [Go-to-market](../../strategy/go-to-market.md) · [Generate new leads](../acquire/generate-new-leads.md) · [Referral ask script](../../templates/referral-ask.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Turn customer success into named introductions logged in Pipedrive |
| **Typical duration** | 5–15 minutes for the ask; follow-up per Acquire |
| **Owner (role)** | Advocate (ask) · Acquire (first touch of referred lead) |
| **Stakeholders** | Customer success / delivery (timing of ask), founders |
| **Success criteria** | Ask made at a defined moment; outcome logged; referred contact in Pipedrive with origin **Referral** and next activity |
| **Related SOPs** | [Generate new leads](../acquire/generate-new-leads.md) |

---

## Responsibility swimlane

| Step | Thin Line | Customer |
|------|-----------|----------|
| Identify success moment | Owns | — |
| Ask for referral | Owns | Considers / responds |
| Permission to use name | Owns (ask) | Grants or declines |
| Log referrer + referred in Pipedrive | Owns | — |
| First touch referred contact | Acquire owns | Prospect responds |

---

## 1. Purpose

Make asking for referrals a **repeatable** step after real customer success — not an informal afterthought.

## 2. Scope

**In scope:** When to ask, what to ask, how to log, handoff to first outreach.

**Out of scope:** Running the full sales cycle with the referred agency (see Generate new leads and later Acquire SOPs). Formal reference calls / case studies (separate reference SOP — not yet written).

## 3. Owner

**Role:** Advocate for the ask and logging; Acquire for working the referred lead.  
**Current incumbent (both stages today):** Fugate  

## 4. Trigger

Ask at least once when any of these occur:

- Go-live success / hypercare exit with a satisfied customer  
- Strong check-in or expansion conversation  
- Customer spontaneously praises the product or support  
- Customer offers “you should talk to…” (capture immediately)

<mark style="color:red;">**TODO / Decision needed:**</mark> Whether the ask is mandatory at hypercare exit for every engagement.

## 5. Preconditions

- Relationship is in good standing (do not ask during active severity-1 disputes)  
- Pipedrive access  
- Clarity on whether Thin Line may use the customer’s name when contacting the referral  

## 6. Inputs

| Input | Source |
|-------|--------|
| Satisfied customer / champion | Deliver / Operate / Expand |
| Optional ask language | [Referral ask script](../../templates/referral-ask.md) |

## 7. Outputs

- Pipedrive note on the **referring** organization (ask made + result)  
- Person/org for the **referred** contact (or clear note if only an agency name was given)  
- Lead origin = **Referral**  
- Link or note connecting referred lead ↔ referring agency  
- Next activity for Acquire first touch  

## 8. Tools

| Tool | Use |
|------|-----|
| Pipedrive | System of record |
| Phone / email / in person | Ask and intro |

## 9. Current state

Referral requests are informal. Wins sometimes produce introductions; there is no standard trigger, script, or Pipedrive logging pattern.

## 10. Target state

Every successful customer is asked at defined moments. Every referral is in Pipedrive with origin Referral, referrer attribution, and a scheduled first touch.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| No standard trigger | This SOP’s trigger list |
| No standard logging | Required Pipedrive fields / notes |
| Ask language ad hoc | Referral ask template |
| Follow-up of referrals inconsistent | Handoff into Generate new leads |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Asking at a bad moment | Skip or defer if relationship is strained |
| Using customer name without permission | Explicit ask; record yes/no |
| Referral never contacted | Next activity required same day |
| Vague “talk to someone in Lubbock” | Capture best available name, agency, and context; still log |

## 13. Decision trees

```text
Success moment reached?
    │
    ├─ Relationship strained ──► Do not ask now; set reminder to revisit
    │
    └─ Relationship healthy ──► Ask (template) ──►
            │
            ├─ Named intro ──► Log + first touch (Generate new leads)
            │
            ├─ “Let me think” ──► Schedule follow-up ask in Pipedrive
            │
            └─ Declines ──► Log decline; do not pressure; remain helpful
```

## 14. Time expectations

| Step | Estimate |
|------|----------|
| Ask conversation | 5–15 min |
| Pipedrive logging | 5–10 min |
| First touch of referred lead | Same day when possible |

## 15. Automation score

| Step | Score (1–5) | Notes |
|------|------------:|-------|
| Trigger detection | 1 | Manual until checklist/hub prompts exist |
| Ask | 1 | Human conversation |
| Logging | 2 | Pipedrive habits / required fields |
| First-touch reminder | 3 | Pipedrive activity |

## 16. Procedure

1. **Confirm timing** — success moment from Triggers; relationship healthy.  
2. **Ask** — use [Referral ask script](../../templates/referral-ask.md) or equivalent plain language. Request:
   - Agency name  
   - Person name / role if known  
   - Why they might be a fit  
   - Permission to use the referrer’s name  
3. **Log the ask on the referring org** in Pipedrive (date, who asked, outcome).  
4. **Create or update the referred org/person** in Pipedrive:
   - Origin = **Referral**  
   - Note referring agency and name-permission yes/no  
5. **Schedule next activity** for first touch (Acquire).  
6. **Execute first touch** per [Generate new leads](../acquire/generate-new-leads.md) § B.  
7. **Close the loop** (optional but preferred): thank the referrer after a good conversation — without sharing confidential deal detail.

## 17. Verification

- [ ] Ask outcome logged on referrer  
- [ ] Referred party in Pipedrive (as complete as information allows)  
- [ ] Origin = Referral  
- [ ] Name-permission recorded  
- [ ] Next activity scheduled  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| Customer angry or at risk | Do not ask; focus on recovery |
| Referral is outside ICP | Log; Acquire decides pursue vs polite decline |
| Duplicate of existing open deal | Link notes; do not create conflicting ownership |

## 19. KPIs

| KPI | Starting definition |
|-----|---------------------|
| Referral asks made | Count logged on customer orgs |
| Referrals captured | New Pipedrive leads with origin Referral |
| Referral → discovery / demo | Downstream conversion |

## 20. Related documents

- [Go-to-market](../../strategy/go-to-market.md)  
- [Referral stage](../../customer-value-engine/advocate/referral.md)  
- [Generate new leads](../acquire/generate-new-leads.md)  
- [Referral ask script](../../templates/referral-ask.md)  
- [Annual operating plan — 2026 H2](../../strategy/annual-operating-plan-2026-h2.md) (reference / referral priorities)  

---

## Continuous improvement

### Weaknesses

- Mandatory hypercare-exit ask not yet decided  
- Pipedrive referrer-link field may not exist yet  

### Automation opportunities

- Checklist item on hypercare exit / customer success cadence  
- Pipedrive custom field: Referring organization  

### Product impact

- Customer community or user group that naturally surfaces peer intros (longer term)

### Process maturity

| Item | Value |
|------|--------|
| Current level | 1 |
| Next milestone | Ask logged for each go-live success in Priority 1 |
| Future goal | Material share of new qualified leads from referrals |

### Next review date

Owner: Advocate · Questions: Are triggers right? Is the ask comfortable for customers? Conversion quality of referred leads?

### Change history

| Date | Change |
|------|--------|
| 2026-07-22 | v0.1 — initial SOP |
