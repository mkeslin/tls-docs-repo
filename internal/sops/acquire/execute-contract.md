# Execute contract

**Document type:** SOP  
**Phase:** Acquire · Contract  
**Status:** v0.1  
**Next review:** <mark style="color:red;">**TODO:**</mark> set date (owner: Acquire)  
**Audience:** Internal — Acquire  
**Related:** [Contract](../../customer-value-engine/acquire/contract.md) · [Acquire authority](../../policies/acquire-authority.md) · [Prepare proposal](prepare-proposal.md) · [Sales handoff](../deliver/sales-handoff.md) · [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md)

---

## Executive summary

| Field | Value |
|-------|--------|
| **Objective** | Get a standard agreement fully executed via Dropbox Sign and hand off cleanly to Implementation |
| **Typical duration** | Send in **24–48 business hours** after proposal accept; customer signature 1–14 days |
| **Owner (role)** | Acquire |
| **Stakeholders** | Founders (redlines / non-standard), Thin Line signatory, prospect signers, Implementation |
| **Success criteria** | Fully executed packet stored; Pipedrive Won (or equivalent); handoff checklist started |
| **Related** | [Sales handoff](../deliver/sales-handoff.md) |

---

## Responsibility swimlane

| Step | Acquire | Founder / signatory | Prospect | Implementation |
|------|---------|---------------------|----------|----------------|
| Assemble standard packet | Owns | Approves template changes | — | — |
| Send via Dropbox Sign | Owns | Thin Line countersign as designated | Signs | — |
| Customer redlines | Summarizes | Negotiates / approves | Requests | — |
| CJIS / security path | Includes standard exhibits | Unusual requirements | Completes agency side | May support later |
| Handoff packet | Owns | — | — | Accepts |

---

## 1. Purpose

Make contracting a **standard Acquire-owned workflow** (Dropbox Sign + standard paper), with founder involvement reserved for redlines and exceptions.

## 2. Scope

**In scope:** Preparing the signature packet from an accepted proposal; e-sign; tracking; filing; starting sales handoff.

**Out of scope:** Implementation kickoff work; negotiating novel legal frameworks without counsel/founder; invoicing details beyond what contract requires (<mark style="color:red;">TODO</mark> link Invoice stage when documented).

## 3. Owner

**Role:** Acquire  
**Current incumbent:** Fugate  

## 4. Trigger

Prospect accepts proposal (email/verbal/written) or asks for contract, and commercial terms are settled within authority.

## 5. Preconditions

- Accepted proposal (or equivalent agreed terms) in Pipedrive  
- Standard contract templates available in **SharePoint** commercial library  
- Dropbox Sign access for Acquire  
- Thin Line signatory: **Eric Fugate** (Acquire) for SaaS and CJIS Security Addendum  
- CJIS path known if agency will have CJI exposure  

## 6. Inputs

| Input | Source |
|-------|--------|
| Final commercial terms | Proposal / Pipedrive |
| Legal entity / billing info | Prospect |
| Signers (name, email, title) | Prospect |
| Standard SaaS agreement | SharePoint commercial library |
| CJIS / security addendum (when required) | SharePoint commercial library |

## 7. Outputs

- Executed agreement(s)  
- Stored PDF / Dropbox Sign record  
- Pipedrive: Contract out → Won; key dates  
- [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md) started / completed as far as Sales can  

## 8. Tools

| Tool | Use |
|------|-----|
| Dropbox Sign | E-signature |
| Pipedrive | Stage + activities; store/link executed copy on the deal |
| SharePoint | Templates + executed copy in deal / commercial library |

## 9. Current state

Contracts go through Dropbox Sign; cycle 1–14 days often driven by customer procurement. Maturity 3 in CVE, but step-by-step Acquire ownership and CJIS packet rules need documentation.

## 10. Target state

Acquire sends standard packets within 24–48 business hours of accept; redlines escalate fast; every win produces a complete handoff packet without re-discovering the deal.

## 11. Gap analysis

| Gap | Move toward target |
|-----|--------------------|
| SharePoint deep links | Pin exact folder URLs |
| CJIS when/when-not for court-only | Decision tree below |
| Handoff incomplete | Checklist mandatory before “done” |

## 12. Common risks

| Risk | Mitigation |
|------|------------|
| Customer procurement delay | Early ask for signer + process; Pipedrive follow-ups |
| Side-email “agreements” | Only Dropbox Sign / approved paper |
| Scope drift in redlines | Compare to proposal; escalate product promises |
| Missing CJIS path | Gate: if CJI/support access likely, include standard path |

## 13. Decision trees

```text
Proposal accepted?
    │
    ├─ Terms still changing ──► Update proposal first (Prepare proposal)
    │
    ├─ Standard paper OK ──► Build packet → Dropbox Sign → track → countersign → handoff
    │
    └─ Redlines / non-standard ──► Summarize → founder (do not accept silently)
```

```text
CJIS / security exhibits?
    │
    ├─ Agency will use RMS/CAD with CJI or vendor access to CJI ──► Include standard CJIS path
    │
    ├─ Court-only / unclear ──► <mark style="color:red;">TODO / Decision needed:</mark> default include vs ask founder
    │
    └─ Explicitly no CJI ──► Document rationale; standard SaaS only
```

## 14. Time expectations

| Step | Target |
|------|--------|
| Accept → packet sent | **24–48 business hours** |
| Thin Line signs first | Eric proofs and signs in Dropbox Sign **before** agency routing |
| Agency completion | Chase every 3–5 business days until signed or lost |

## 15. Automation score

| Step | Score (1–5) |
|------|------------:|
| Packet prep | 2 |
| E-sign send | 3–4 |
| Redlines | 1 |
| Handoff | 2 |

## 16. Procedure

1. **Confirm terms frozen** — Match accepted proposal; no open pricing fights.  
2. **Collect signer info** — Legal name of agency, signer name/email/title, billing contact.  
3. **Assemble packet** from **SharePoint** templates:
   - Standard SaaS agreement (commercial terms from proposal)  
   - Pricing / order exhibit if used as a separate file  
   - CJIS Security Addendum when required  
4. **Internal check** — Terms within [Acquire authority](../../policies/acquire-authority.md) + pricing card; Eric **proofreads** before sending.  
5. **Send Dropbox Sign — Thin Line first** — **Eric Fugate** signs for Thin Line first (proofread gate), then route to agency signers.  
6. **Agency signers (typical)**  
   - **SaaS agreement:** usually **police chief** and **mayor / superintendent** (or equivalent)  
   - **CJIS Security Addendum:** **police chief** for the agency; Eric for Thin Line  
7. **Pipedrive** — Stage Contract out; activity to follow up; link to signature request.  
8. **Monitor** — Remind per cadence; answer process questions; escalate substance/redlines to founder.  
9. **On full execution** — Store executed docs in **Pipedrive** and **SharePoint**; mark Won; start [Sales handoff](../deliver/sales-handoff.md) + [checklist](../../checklists/sales-handoff-checklist.md).  
10. **Redlines path** — Summarize requested changes; do not verbally accept material changes; wait for founder guidance; re-send only when approved.

### Standard packet inventory

| Document | When | Thin Line signer | Typical agency signer(s) | Location |
|----------|------|------------------|--------------------------|----------|
| SaaS agreement | Always | Eric Fugate | Chief + mayor / superintendent (or equivalent) | SharePoint templates |
| Pricing / order form | When used | (with SaaS packet) | (with SaaS packet) | SharePoint |
| CJIS Security Addendum | When CJI path applies | Eric Fugate | Police chief | SharePoint |
| Executed copies | After completion | — | — | Pipedrive **and** SharePoint |

## 17. Verification

- [ ] Packet matches accepted proposal  
- [ ] Correct signers  
- [ ] Dropbox Sign completed (all parties)  
- [ ] Executed copy stored  
- [ ] Handoff checklist underway  

## 18. Failure and escalation

| Situation | Action |
|-----------|--------|
| Signer wrong / bounced email | Correct and re-send |
| Procurement requires paper/mail | Escalate for exception process |
| Material redline | Founder; pause clock |
| Customer ghost after send | Cadence then closed-lost / nurture reason |

## 19. KPIs

| KPI | Definition |
|-----|------------|
| Time accept → send | Business hours |
| Time send → fully executed | Calendar days |
| % wins with complete handoff checklist | Quality |

## 20. Related documents

- [Prepare proposal](prepare-proposal.md)  
- [Sales handoff](../deliver/sales-handoff.md)  
- [Sales Handoff Checklist](../../checklists/sales-handoff-checklist.md)  
- [Acquire authority](../../policies/acquire-authority.md)  
- Compliance / CJIS materials under `internal/compliance/` as applicable  

---

## Continuous improvement

### Weaknesses

- SharePoint deep links not pinned  
- CJIS default for court-only / unclear still undecided  

### Automation opportunities

- Dropbox Sign templates with merge fields; Pipedrive ↔ Sign integration  

### Product impact

- Faster “time to handoff” improves implementation scheduling  

### Process maturity

| Item | Value |
|------|--------|
| Current | ~3 practice / ~2 documentation |
| Next milestone | Acquire sends standard packet without founder on every deal |
| Future | Self-serve order form + e-sign for in-card deals |

### Change history

| Date | Change |
|------|--------|
| 2026-07-26 | SharePoint kit, Eric signs first, SaaS/CJIS signer pattern, dual storage |
| 2026-07-22 | v0.1 — initial SOP |
