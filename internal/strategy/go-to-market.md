# Go-to-market

**Document type:** Strategy  
**Status:** v0.2  
**Audience:** Internal — sales, founders, customer success  
**Related:** [Vision and principles](vision-and-principles.md) · [Annual operating plan — 2026 H2](annual-operating-plan-2026-h2.md) · [Generate new leads](../sops/acquire/generate-new-leads.md) · [Capture referral](../sops/advocate/capture-referral.md) · [Two-week sales plan](../templates/sales-plan-two-week.md)

---

## Purpose

Define **where** Thin Line focuses commercially and **which channels** create new conversations. Procedures live in SOPs; this page sets priorities so pipeline work stays aligned with company strategy.

---

## Support boundary

**Texas only.** Thin Line does not support agencies outside Texas.

---

## Geographic priority (within Texas)

Principle: **Regional dominance before national expansion** ([Vision and principles](vision-and-principles.md)).

| Priority | Focus | Intent |
|---------:|--------|--------|
| 1 | Close to **Lubbock** / **West Texas** (incl. South Plains) | Highest density of relationships, travel efficiency, reference network |
| 2 | Close to **existing customers** | Build geographic **clusters** around live references |
| — | Other Texas | Allowed when opportunity quality is high; not the default outbound focus |

Outbound, list work, and field days should prefer Priority 1, then Priority 2. Opportunities elsewhere in Texas are open when they fit ICP and capacity.

---

## Disqualifiers (all segments)

Walk away or pause (even if interested) when:

- Budget is immovable / no realistic path to afford Thin Line  
- The deal requires **substantial custom development** to close or implement  

Warm exceptions still need founder agreement before promising custom scope.

---

## Module packaging (current commercial rule)

| Rule | Current state |
|------|----------------|
| **RMS / CAD** | Primary LE entry. Almost all PD customers use RMS; CAD/RMS may sell separately if needed. |
| **Court** | Sold to customers who use (or will use) **RMS/CAD** — existing Thin Line customers or new customers buying the LE + court path. |
| **Jail** | Same pattern: jail with RMS/CAD path (existing or new). |
| **Standalone court** | Desired later; **not ready** — do not pursue as primary outbound. |
| **Legacy displacement** | Strong recent traction with **CopSync** customers — prioritize when present. |

---

## Ideal customer profiles (ICP)

Use the matching profile when filtering lists, planning field days, or qualifying inbound. Size bands are working guidance, not hard engineering limits.

### Law enforcement (municipal PD and similar)

| Dimension | ICP (current) |
|-----------|----------------|
| **Who** | Texas municipal / local police departments (and similar LE agencies) |
| **Size** | Core base around **~15 officers**; actively pursuing **larger** agencies (example direction: Levelland-scale and up from the ~15 core) |
| **Products** | RMS and/or CAD; court/jail only under the packaging rules above |
| **Strong signal** | Existing **CopSync** (or similar displaceable) customer |
| **Buyer** | Chief / command; city stakeholders as needed |
| **Not now** | Enterprise-sized pursuits that overwhelm delivery or force heavy custom work |

Keep **soft** size guidance (no hard min/max officer cutoff) until leadership wants a hard gate.

### Municipal court

| Dimension | ICP (current) |
|-----------|----------------|
| **Who** | Texas municipal courts tied to an RMS/CAD Thin Line path (same city / agency relationship) |
| **Size** | **One clerk and one judge** — do not pursue larger court staffing models for now |
| **Products** | Court with RMS/CAD (existing customer expansion or new combined deal) |
| **Buyer** | Court clerk / judge; city admin as needed; coordinate with LE relationship |
| **Not now** | **Standalone court** (no RMS/CAD path) · multi-clerk / multi-judge courts |

### County sheriff / jail

| Dimension | ICP (current) |
|-----------|----------------|
| **Who** | Texas county jails / sheriff jail operations on an RMS/CAD Thin Line path |
| **Size** | Current proven scale ~**15-bed** jail; larger jails are a future capability (more product/test work) — do not treat large jails as default outbound ICP yet |
| **Products** | Jail with RMS/CAD (existing or new) |
| **Buyer** | Sheriff / jail admin; county stakeholders as needed |
| **Not now** | Large jail pursuits that assume unbuilt capacity · jail-only with no RMS/CAD path without founder agreement |

Sheriff **LE** (RMS/CAD) opportunities follow the **Law enforcement** profile; jail module follows this jail profile.

---

## Commercial coverage (current vs target)

| Segment | Current coverage | Target |
|---------|------------------|--------|
| Law enforcement | Acquire owner (Fugate) primary | Sustainable LE ownership on Acquire |
| Municipal court | Founder-led (Keslin) today | Phased handoff to Acquire (see [Court selling handoff](#court-selling-handoff)) |
| Jail / sheriff | Limited; tied to platform readiness | Expand as jail product capacity grows |

This is an operating-coverage note, not an ICP substitute.

---

## System of record

**Pipedrive** is the system of record for leads, deals, activities, and follow-up.

Rules of thumb:

1. Every new conversation-worthy contact or agency is logged in Pipedrive **before or immediately after** first outreach.  
2. Channel of origin is recorded (see Lead origin below).  
3. Next activity is always scheduled — no “orphan” leads.  
4. Do not track pipeline only in email, notes apps, or memory.

**Deal pipeline stages** (live): **Dialog Established** → **Demo Scheduled** → **Demo Completed** → **Proposal Sent/Decision Pending** → **Onboarding Scheduled/Started**. Exit criteria: [Acquire authority](../policies/acquire-authority.md#pipedrive-pipeline-stages-live).

**When to create a Deal:** when a conversation reaches **fit + real possibility of moving forward** (not at first cold touch). Until then, keep **Organization / Person** (and Pipedrive **Leads** inbox items) with next activities. Creating the Deal usually lands it in **Dialog Established**.

**Pipedrive custom fields (create these):**

| Field | Type | Required when | Values / notes |
|-------|------|---------------|----------------|
| **Lead origin** | Single select | Org or Deal created | Referral · Association list · Field visit · Conference / event · Inbound · Other network |
| **GTM region** | Single select | Deal created | Priority 1 — Lubbock / West Texas · Priority 2 — cluster · Other Texas |
| **ICP profile** | Single select | Deal created | LE · Court · Jail · Multi-product |
| **Referring agency** | Text (or org link) | Origin = Referral | Who introduced us |
| **Association source** | Text | Origin = Association list | e.g. South Plains Police Chiefs — Pipedrive Leads |
| **Sworn officers** | Number | LE in scope | Sizing input |
| **Rated beds** | Number | Jail in scope | Sizing input |
| **Citations / month** | Number | Court in scope | Sizing input |
| **Modules of interest** | Multi / text | Deal created | RMS, CAD, Court, Jail |
| **Demo site access** | Yes/No | Before or after first deep conversation | Prospects often explore before the live call |
| **Market-share program** | Single select | If used | None · Founding agency · Competitive replacement · Regional cohort · Accessibility |

---

## Lead origin (channels)

Field name in Pipedrive: **Lead origin** (create if missing). Values:

| Origin | Description | Primary phase |
|--------|-------------|----------------|
| Referral | Introduced by a customer or champion | Advocate → Acquire |
| Association list | South Plains Police Chiefs Association (or similar) — sourced from Pipedrive **Leads** | Acquire |
| Field visit | In-person agency visit / territory day | Acquire |
| Conference / event | Met or followed up from an event | Acquire / Awareness |
| Inbound | Website, phone, email, or other inbound | Awareness → Acquire |
| Other network | Personal or professional network not covered above | Acquire |

Procedures: [Generate new leads](../sops/acquire/generate-new-leads.md) · [Capture referral](../sops/advocate/capture-referral.md) · [First-touch outreach](../templates/first-touch-outreach.md).

---

## Channel mix (working priorities)

Prioritize in this order (no hard % targets until Q4 review):

1. **Referrals** from successful customers (repeatable ask).  
2. **Association and list outreach** (Pipedrive **Leads** / South Plains chiefs).  
3. **Scheduled field / territory days** with a pre-built stop list.  
4. **Conference and event follow-up** into Pipedrive.  
5. **Inbound** response and qualification.

**Starting mix intent (guide, not quota):** roughly half of new qualified conversations from referrals + association; field days feed the rest; inbound opportunistic.

---

## Operating rhythm (company standard)

| Cadence | Activity | Guided default |
|---------|----------|----------------|
| Weekly | Pipedrive review: open activities, stalled leads, next actions | 30–45 min |
| Weekly | Structured **outbound block** (list, referral follow-up, or field prep) | **4 hours** (one block, same weekday when possible) |
| Per outbound block | Association / Leads batch | **10–15** agencies researched + touched (not 50 spray-and-pray) |
| Monthly | **Territory / field day** in Priority 1 | **1 day** (or documented skip with make-up date) |
| Ongoing | Referral asks at success moments | See [Capture referral](../sops/advocate/capture-referral.md) |
| Quarterly | Refresh / re-touch association segments still in ICP | — |

### Follow-up cadence (no response)

| Touch | Timing | Action |
|------:|--------|--------|
| 1 | Day 0 | First email and/or call + voicemail |
| 2 | Day 3–5 | Second channel (if email first → call, or reverse) |
| 3 | Day 10–14 | Final short bump; offer demo access or “not now is fine” |
| — | After touch 3 | Move to **nurture**: next activity **60–90 days** out, or mark closed-not-now with reason |

Honor “do not contact” immediately. Do not burn chiefs with weekly pings.

---

## Named assets

| Asset | Status | Notes |
|-------|--------|-------|
| South Plains Police Chiefs Association / list | In Pipedrive as **Leads** | Work from Leads inbox; convert to Org/Person/Deal per rules above |
| First-touch language | [Template](../templates/first-touch-outreach.md) | Email, voicemail, field, referral variants |
| Customer reference / referral roster | Informal | Formalize via Advocate SOPs |
| Field-day stop list template | [Template](../templates/field-day-stop-list.md) | Use before each territory day |
| Two-week sales plan | [Template](../templates/sales-plan-two-week.md) | Blank plan + illustrative example for Acquire |

Do not commit full mailing dumps into GitBook.

---

## Court selling handoff

**Suggestion (adopt until replaced):**

| Phase | When | Who sells Court |
|-------|------|-----------------|
| **Now** | Until Court demo kit is Acquire-ready | **Keslin** leads Court conversations; Fugate may join for LE context on combined deals |
| **Shadow** | Next 2–3 Court demos | Fugate attends; Keslin facilitates |
| **Combined path** | Court + RMS/CAD on one deal | Acquire (Fugate) owns commercial path; founder joins Court segment of the live conversation until kit ready |
| **Acquire-owned** | After kit + successful shadow | Acquire runs Court on standard path; founder by exception (custom, multi-judge, product-risk) |

Standalone Court (no LE path) remains founder-gated per ICP packaging.

---

## What “enough pipeline” means

Aligned with [Annual operating plan — 2026 H2](annual-operating-plan-2026-h2.md): enter 2027 with a healthy qualified pipeline while closing named 2026 opportunities.

**Leading indicator (starting):** each month, Acquire aims for **≥ 4 demos scheduled** and **≥ 8 new Orgs/People touched** in Priority 1 with origin set and a next activity — refine after 60 days of clean data.
---

## Out of scope for this page

- Demo, proposal, and contract procedures — see [Acquire SOPs](../sops/acquire/README.md) and [Acquire authority](../policies/acquire-authority.md).  
- Implementation and training delivery.  
- Individual performance assessments — this document defines company focus and channels only.

---

## Related

- [Customer value stream](../customer-value-engine/customer-value-stream.md)  
- [Cold leads](../customer-value-engine/acquire/cold-leads.md) · [Awareness](../customer-value-engine/acquire/awareness.md) · [Referral](../customer-value-engine/advocate/referral.md)  
- [SOP index](../sops/README.md)
