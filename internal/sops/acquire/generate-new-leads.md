# Generate new leads

**Document type:** SOP  
**Phase:** Acquire (Awareness → Cold / Warm leads)  
**Status:** v0.1  
**Next review:** <mark style="color:red;">**TODO:**</mark> set date (owner: Acquire)  
**Audience:** Internal — Acquire owner and anyone creating new sales conversations  
**Related:** [Go-to-market](../../strategy/go-to-market.md) · [Cold leads](../../customer-value-engine/acquire/cold-leads.md) · [Warm leads](../../customer-value-engine/acquire/warm-leads.md) · [Capture referral](../advocate/capture-referral.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Create new ICP conversations and log them in Pipedrive with a clear next activity |
| **Typical duration** | Varies by channel (see Time expectations) |
| **Owner (role)** | Acquire |
| **Stakeholders** | Founders (messaging / ICP), Advocate (referrals), Delivery (capacity awareness) |
| **Success criteria** | New lead or org in Pipedrive; origin set; next activity scheduled; first contact attempted or completed |
| **Related SOPs** | [Capture referral](../advocate/capture-referral.md) |

---

## Responsibility swimlane

| Step | Thin Line Acquire | Thin Line other | Customer / prospect |
|------|-------------------|-----------------|---------------------|
| Choose channel and target list | Owns | Advises on ICP / capacity | — |
| Log org and person in Pipedrive | Owns | — | — |
| First outreach (visit, call, email, mail) | Owns | — | Receives / responds |
| Qualify interest | Owns | — | Shares need / timing |
| Hand warm path to discovery / demo | Owns | — | Schedules |

---

## 1. Purpose

Create a repeatable way to **generate new leads and start conversations** using approved channels, with Pipedrive as the system of record.

## 2. Scope

**In scope:** Choosing targets within [Go-to-market](../../strategy/go-to-market.md) priorities; association-list outreach; field / territory days; event follow-up; logging and first-touch cadence.

**Out of scope:** Demo delivery, proposals, contracts, implementation handoff (separate Acquire / Deliver SOPs).

## 3. Owner

**Role:** Acquire  
**Current incumbent:** Fugate  

## 4. Trigger

Any of:

- Weekly outbound block on the calendar  
- Monthly territory / field day  
- New or refreshed association list segment  
- Referral received ([Capture referral](../advocate/capture-referral.md))  
- Event / conference follow-up owed  

## 5. Preconditions

- ICP and geographic priority understood ([Go-to-market](../../strategy/go-to-market.md))  
- Access to Pipedrive  
- For list work: access to the agreed list storage location  
- For field days: stop list prepared ([Field-day stop list](../../templates/field-day-stop-list.md))  

## 6. Inputs

| Input | Source |
|-------|--------|
| ICP / region priority | Go-to-market |
| Association mailing list (e.g. South Plains Police Chiefs Association) | Agreed storage location <mark style="color:red;">**TODO**</mark> |
| Referral intro | Advocate SOP / Pipedrive |
| Event attendee notes | Conference / networking |
| Existing Pipedrive orgs (avoid duplicates) | Pipedrive |

## 7. Outputs

- Organization and person (contact) in Pipedrive  
- Lead / deal as appropriate for current Pipedrive process <mark style="color:red;">**TODO:**</mark> confirm when a Deal is created vs Person/Org only  
- **Lead origin** set  
- Activity logged + **next activity** scheduled  
- Conversation started or documented attempt  

## 8. Tools

| Tool | Use |
|------|-----|
| Pipedrive | System of record — orgs, people, deals, activities |
| Email / phone / Quo | Outreach and follow-up |
| Field-day stop list | Pre-plan in-person visits |
| Maps / travel | Territory routing |

## 9. Current state

Lead generation is a mix of referrals, network, research, and ad hoc outreach. Association list exists but usage is not yet standardized. Field visits occur but are not always planned as a repeating territory rhythm. Pipedrive is the intended CRM.

## 10. Target state

Every new conversation is created through a known channel, logged in Pipedrive the same day, tagged with origin, and has a next activity. Texas only; Lubbock / West Texas first, then clusters near existing customers. Weekly outbound and monthly field cadence are normal operating rhythm.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| List storage and usage rules unclear | Document location + quarterly touch process |
| Origin not always recorded | Required Pipedrive field + this SOP |
| Field days not pre-planned | Stop list template + monthly cadence |
| Pipeline stages / Deal rules informal | Decision needed on Pipedrive hygiene |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Duplicate orgs / people in Pipedrive | Search before create |
| Outreach without next step | No close of activity without scheduling next |
| Spreading too thin geographically | Prefer Priority 1, then Priority 2 clusters ([Go-to-market](../../strategy/go-to-market.md)) |
| List used without ICP filter | Skip non-ICP agencies; prefer Priority 1–2 for cold outbound |
| Conversations only in email | Log summary activity in Pipedrive |

## 13. Decision trees

```text
New outreach opportunity
    │
    ├─ Came from a customer/champion? ──► Capture referral SOP, then this SOP for first touch
    │
    ├─ In-person territory day planned? ──► Build stop list → visit → log same day
    │
    ├─ Working association / mailing list? ──► Filter ICP + geo priority (P1 then P2) → batch outreach → log each
    │
    └─ Event / inbound / other? ──► Log origin → first response → schedule next
```

```text
After first touch
    │
    ├─ Interested / willing to talk ──► Move toward discovery / demo; keep Pipedrive stage current
    │
    ├─ Not now ──► Schedule future follow-up (date in Pipedrive)
    │
    └─ No fit / do not contact ──► Mark lost or disqualified with reason; do not keep fake open activities
```

## 14. Time expectations

| Channel | Planning | Execution (starting estimates) |
|---------|----------|--------------------------------|
| Referral first touch | 10–20 min | Same day when possible |
| Association list batch | 30–60 min prep | <mark style="color:red;">**TODO:**</mark> batch size per session |
| Field / territory day | 30–60 min stop-list prep | Full day on site / in region |
| Event follow-up | 15–30 min | Within 5 business days of event |

Refine estimates at next review.

## 15. Automation score

| Step | Score (1–5) | Notes |
|------|------------:|-------|
| Target selection | 2 | Lists help; judgment remains |
| Pipedrive create / update | 2 | Templates / required fields help |
| Outreach send | 1–2 | Personalization expected for chiefs |
| Follow-up reminders | 3 | Pipedrive activities |
| Reporting by origin | 1 | Needs consistent origin field |

## 16. Procedure

### A. Always — Pipedrive hygiene (every channel)

1. Search Pipedrive for the agency (organization) and contact.  
2. Create or update Organization and Person.  
3. Set **Lead origin** (Referral, Association list, Field visit, Conference / event, Inbound, Other network).  
4. Add a short note: why this agency, what was said or attempted.  
5. Create or complete an **Activity**; always leave a **next Activity** with a due date.  
6. If interest is confirmed, advance per current pipeline rules and pursue discovery / demo.

### B. Channel — Customer referral

1. Complete [Capture referral](../advocate/capture-referral.md) so the intro is logged.  
2. First touch the referred contact promptly (same day when possible).  
3. Mention the referring agency only if the referrer agreed to be named.  
4. Continue from Procedure A.

### C. Channel — Association / mailing list (South Plains Police Chiefs Association)

1. Open the list from the agreed storage location (<mark style="color:red;">**TODO:**</mark> document path / drive location).  
2. Filter to the matching ICP profile ([Go-to-market](../../strategy/go-to-market.md)); prefer geographic Priority 1, then Priority 2 clusters. Other Texas OK when quality is high.  
3. For each target in today’s batch: Procedure A, then outreach (call, email, and/or planned visit).  
4. Record message theme used (keep copy snippets in Pipedrive or a shared draft location — <mark style="color:red;">**TODO:**</mark> approved first-touch language).  
5. Do not paste the full mailing list into GitBook or public tools.

### D. Channel — Field / territory day

1. Pick a hub and date; block the calendar.  
2. Build a stop list of agencies ([Field-day stop list](../../templates/field-day-stop-list.md)) — aim for a realistic door count for the day.  
3. Pre-create or update Pipedrive orgs for planned stops when practical.  
4. On site: introduce Thin Line, leave appropriate materials if any, exchange contact info.  
5. **Same day:** log each stop (visited / not available / follow-up) and schedule next activities in Pipedrive.

### E. Channel — Conference / event follow-up

1. Within five business days, enter each promising contact in Pipedrive (Procedure A).  
2. Origin = Conference / event; note event name.  
3. Send follow-up and schedule next activity.

### F. Channel — Inbound

1. Respond promptly; log in Pipedrive if not already present.  
2. Origin = Inbound.  
3. Qualify and schedule discovery / demo as appropriate.

## 17. Verification

- [ ] Org + person exist in Pipedrive  
- [ ] Origin set  
- [ ] Activity history reflects outreach  
- [ ] Next activity has a due date  
- [ ] Duplicate check done  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| No response after agreed follow-up attempts | <mark style="color:red;">**TODO / Decision needed:**</mark> max attempts / recycle timing |
| Prospect requests no contact | Honor immediately; mark accordingly in Pipedrive |
| Capacity conflict with delivery | Escalate to founders before promising dates  
| Messaging or pricing questions beyond Acquire authority | Escalate to founders / product as appropriate |

## 19. KPIs

| KPI | Starting definition |
|-----|---------------------|
| New Pipedrive leads (or orgs touched) per month | Count with origin set |
| Conversations started | First meaningful reply or in-person conversation |
| Field days completed | Per go-to-market rhythm |
| Conversion to discovery / demo | Downstream (track in Pipedrive) |

<mark style="color:red;">**TODO:**</mark> Bind KPIs to quarterly scorecard if desired.

## 20. Related documents

- [Go-to-market](../../strategy/go-to-market.md)  
- [Awareness](../../customer-value-engine/acquire/awareness.md) · [Cold leads](../../customer-value-engine/acquire/cold-leads.md) · [Warm leads](../../customer-value-engine/acquire/warm-leads.md)  
- [Capture referral](../advocate/capture-referral.md)  
- [Field-day stop list](../../templates/field-day-stop-list.md)  
- [Two-week sales plan](../../templates/sales-plan-two-week.md)  

---

## Continuous improvement

### Weaknesses

- Association list operational details incomplete  
- Approved outreach language not yet standardized  
- Pipedrive required fields not fully specified  

### Automation opportunities

- Pipedrive activity reminders and email sync  
- Filtered views by region / origin  
- Import path for association list segments (careful with duplicates)  

### Product impact

- Public website / one-pagers that make first conversations easier  
- Demo environment readiness for faster follow-up after interest  

### Process maturity

| Item | Value |
|------|--------|
| Current level | 1–2 (founder / early documentation) |
| Next milestone | Origin + next-activity hygiene on every new lead; one completed territory day using the stop list |
| Future goal | Predictable monthly lead creation by channel without reinventing the plan each week |

### Next review date

Owner: Acquire · Questions: Is Priority 1 still right? Are list and field cadences realistic? Which origin produces discovery/demo?

### Change history

| Date | Change |
|------|--------|
| 2026-07-22 | v0.1 — initial SOP |
