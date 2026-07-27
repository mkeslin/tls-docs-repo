# Triage support request

**Document type:** SOP  
**Phase:** Operate · Support  
**Status:** v0.1  
**Next review:** 2026-10-01 (owner: Support)  
**Audience:** Internal — Support, founders, Deliver (hypercare)  
**Related:** [Support](../../customer-value-engine/operate/support.md) · [Operate authority](../../policies/operate-authority.md) · [Hypercare and transition](../deliver/hypercare-and-transition.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Intake, classify, resolve or escalate customer issues without losing them in personal lists |
| **Typical duration** | Acknowledge ASAP; many resolve same day; P1 continuous until stable |
| **Owner (role)** | Support (steady state) · Deliver/Acquire training owner during hypercare |
| **Current incumbents** | **Gibson** (steady state); **Fugate** during onboarding/training/hypercare |
| **Success criteria** | Severity set; owner clear; customer heard from; outcome logged in shared place |
| **Related** | [Operate authority](../../policies/operate-authority.md) |

---

## Responsibility swimlane

| Step | Support (Gibson) | Fugate (hypercare / training) | Product (Keslin) | Customer |
|------|------------------|-------------------------------|------------------|----------|
| Intake (email / Quo) | Owns steady state | Owns during hypercare | — | Reports issue |
| Severity + first response | Owns | Owns in hypercare | — | — |
| Remote session (ScreenConnect) | Owns | Owns in hypercare | — | Authorizes / attends |
| Bug / change needed | Logs + stays customer-facing | Same | Prioritizes / fixes | Confirms |
| Close / confirm | Owns | Owns in hypercare | — | Confirms |

---

## 1. Purpose

Make support **visible and repeatable**: preferred channels, severity, ownership handoff from hypercare → steady state, and escalation when almost every real defect needs product.

## 2. Scope

**In scope:** Live-customer issues via email/Quo; triage; remote assisted sessions; logging; escalation to product.

**Out of scope:** Pre-sales; unlimited custom work; agency IT and third-party vendors ([Operate authority](../../policies/operate-authority.md)).

## 3. Owner

**Steady state:** Support — Gibson  
**Onboarding / training / hypercare:** Fugate (transitions to Gibson after hypercare exit)

## 4. Trigger

Customer contacts Thin Line about a live (or hypercare) environment issue or question.

## 5. Preconditions

- Know whether the agency is in **hypercare** or **steady-state Operate**  
- Access to email + Quo  
- ScreenConnect available for attended endpoint support  
- Shared log location available (see Tools — improve over personal lists)

## 6. Inputs

| Input | Source |
|-------|--------|
| Customer message | Email or Quo (preferred) |
| Agency / environment | Org knowledge / Hub / notes |
| Hypercare flag | Deliver engagement |

## 7. Outputs

- Severity (P1–P3)  
- Response to customer  
- Shared log entry (minimum)  
- Product item when defect/change needed  
- Closed confirmation or open next action  

## 8. Tools

| Tool | Use |
|------|-----|
| **Email** | Preferred written channel |
| **Quo** | Preferred phone/SMS channel |
| ScreenConnect | Attended remote support |
| Shared support log | <mark style="color:red;">**Target:**</mark> Microsoft List or Azure Boards — **today:** personal lists + telling each other (must improve) |
| Azure DevOps | Engineering work when product involved |

## 9. Current state

Phone/email/SMS; Gibson handles most steady-state; Fugate covers onboarding/training then transitions. No strong ticket system — coordination is verbal and personal lists. Usually answer if available; otherwise ASAP. Remote via ScreenConnect. Almost every confirmed product issue escalates to engineering/product. Maturity 1.

## 10. Target state

Same human ownership model, but every request has **severity**, **owner**, **next action**, and a **shared log**. Customers know email/Quo are preferred. P1 has a clear emergency path. Hypercare → Operate handoff is explicit. Product gets a clean bug report, not a vague ping.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| Personal lists only | Stand up shared Microsoft List (or ADO) with Agency, Severity, Owner, Status, Summary |
| No severity language | Use P1–P3 below on every intake |
| “Tell each other” | Post P1/P2 in Teams support channel + assign owner |
| Unclear hypercare vs Operate | 14-day default hypercare then Gibson owns new tickets |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Issue lost | Shared log + next action date |
| Wrong owner (still in hypercare) | Check go-live date / hypercare flag first |
| Promised ship date | Never — escalate priority only |
| Scope creep (agency IT) | Redirect per authority matrix |

## 13. Decision trees

```text
Who owns this request?
    │
    ├─ Agency in hypercare / active onboarding training ──► Fugate primary
    │
    └─ Steady-state live customer ──► Gibson primary
```

```text
Severity?
    │
    ├─ P1 Emergency ──► Stabilize now; notify founders; continuous until workaround or fix path
    │
    ├─ P2 Major ──► Same-day working response; escalate product if blocked
    │
    └─ P3 Normal ──► Same day or next business day; queue if needed
```

```text
Need product / eng?
    │
    ├─ How-to / training / config in product ──► Support resolves
    │
    ├─ Suspected bug or data issue ──► Reproduce → log → escalate to Keslin (almost always for real defects)
    │
    └─ Out of scope ──► Redirect (agency IT / vendor / Acquire / billing)
```

## 14. Time expectations

| Severity | First response target | Resolution intent |
|----------|----------------------|-------------------|
| **P1** | Immediate / as soon as seen (nights/weekends: respond if reachable; otherwise ASAP) | Continuous effort until stable or safe workaround |
| **P2** | Same day | Days, not weeks, for workaround or fix path |
| **P3** | Same day if possible; else next business day | Scheduled with other work |

Aligns with contract spirit (emergency ~1 hour effort when reachable; standard ~1 business day) — document honesty: today is “answer if we can.”

## 15. Automation score

| Step | Today (1–5) | Target |
|------|------------:|-------:|
| Intake | 1 | 3 (shared queue) |
| Severity | 1 | 3 |
| Remote session | 2 | 3 |
| Eng handoff | 1 | 3 |
| Closeout | 1 | 3 |

## 16. Procedure

### A. Intake

1. Prefer **email** or **Quo**; if customer calls another path, still log it.  
2. Capture: agency, who contacted, environment (prod), symptom, when started, urgency in their words.  
3. Determine **hypercare vs Operate** ownership ([Operate authority](../../policies/operate-authority.md)).

### B. Classify severity

| Severity | Meaning | Examples |
|----------|---------|----------|
| **P1 — Emergency** | Core operations materially blocked or security incident | App down for agency; cannot dispatch/book if that module is live; suspected CJI exposure / breach |
| **P2 — Major** | Important workflow broken; no good workaround | Cannot complete report/citation path used daily; login failure for multiple users |
| **P3 — Normal** | Question, minor bug, enhancement, single-user annoyance | How-to; cosmetic; “nice to have”; one user needs password help |

When unsure between P1 and P2, treat as **P1** until proven otherwise.

### C. Respond and act

1. Acknowledge the customer (especially P1/P2).  
2. Reproduce or gather screenshots / tenant / user.  
3. If endpoint help needed: attended **ScreenConnect** with agency authorization (see CJIS remote-access practices).  
4. Resolve if how-to/config.  
5. If defect/change: open/notify **product item** for Keslin; keep customer updated; do **not** invent ship dates.  
6. Log in the **shared** place (target List): severity, owner, status, next action.

### D. Close

1. Confirm with customer that they are unblocked (or that the item is tracked and they accept the workaround).  
2. Mark closed in shared log.  
3. If knowledge is reusable, note candidate for Help / FAQ later.

## 17. Verification

- [ ] Severity assigned  
- [ ] Owner matches hypercare vs Operate  
- [ ] Customer received a response  
- [ ] Shared log updated (not only a personal note)  
- [ ] Product escalated when needed  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| P1 and primary unreachable | Other founder/Support picks up; do not wait on formality |
| Customer demands custom feature | Decline as Support commitment; route to product/Acquire |
| Repeated same question | Resolve + flag for Help article / training gap |
| Blame / contract dispute | Founder |

## 19. KPIs (starting)

| KPI | Definition |
|-----|------------|
| % requests logged in shared list | Target → 100% within 60 days of List existing |
| P1 count / month | Trend |
| Time to first response (P2/P3) | Sample weekly |
| Reopened issues | Quality signal |

## 20. Related documents

- [Operate authority](../../policies/operate-authority.md)  
- [Support (CVE)](../../customer-value-engine/operate/support.md)  
- [Hypercare and transition](../deliver/hypercare-and-transition.md)  
- [Publish product update](publish-product-update.md)  

---

## Continuous improvement

### Weaknesses

- No durable ticket system yet  
- Severity not used in customer language yet  
- Knowledge stays in people’s heads  

### Automation opportunities

- Shared Microsoft List → later Helpdesk/ADO  
- Email alias → List  
- Canned Quo/email acknowledgements by severity  

### Product impact

- In-app Help for top repeated questions  
- Better error messages reduce P3 noise  

### Process maturity

| Item | Value |
|------|--------|
| Current level | 1 |
| Next milestone | Shared List + P1–P3 on every request for 30 days |
| Future goal | Tiered support without founder dependency on routine P3 |

### Next review date

2026-10-01  
