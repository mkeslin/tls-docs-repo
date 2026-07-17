# Standard operating procedures (SOPs)

Repeatable procedures organized by [Customer Value Engine](../customer-value-engine/README.md) phase.

SOPs are part of **Thin Line OS**: they document how work is done today, expose gaps, and drive maturity so the company becomes less founder-dependent over time.

**Before major Deliver work:** complete the relevant [Assessment](../assessments/README.md) (decision document). Example: [Legacy System Migration Assessment](../assessments/legacy-system-migration-assessment.md) → Approved Conversion Plan, then execute via the SOP.

**Model SOP:** [Legacy System Migration](deliver/legacy-system-migration.md)

---

## Thin Line OS SOP standard

Every SOP should follow this structure. Do not invent undocumented process detail — use `<mark style="color:red;">**TODO:**</mark>` or `<mark style="color:red;">**Decision needed:**</mark>` markers.

### Front matter

1. **Title, phase, status, next review date**
2. **Executive Summary** — objective, typical duration, owner (role), stakeholders, success criteria, related SOPs (readable in under a minute)
3. **Responsibility swimlane** — who does what (Customer vs Thin Line, or more lanes if needed)

### Core procedure

4. Purpose  
5. Scope  
6. Owner (role + current incumbent if useful)  
7. Trigger  
8. Preconditions  
9. Inputs  
10. Outputs  
11. Tools  
12. **Current state** — how the work is performed today  
13. **Target state** — the scalable standard  
14. **Gap analysis** — current → target  
15. **Common risks**  
16. **Decision trees** — at least one diagram for major forks  
17. **Time expectations** — per phase (starting estimates OK if marked TODO to refine)  
18. **Automation score** — 1–5 by major process step  
19. Procedure (numbered phases / steps)  
20. Verification  
21. Failure and escalation  
22. KPIs  
23. Related documents  

### Continuous improvement system (required ending)

Every SOP ends with this loop:

24. **Weaknesses**  
25. **Automation opportunities**  
26. **Product impact** — how Thin Line Platform (or internal tooling) could reduce or eliminate work in this SOP  
27. **Process maturity** — current level (1–5), description, next milestone, future goal  
28. **Next review date** — owner + review questions  
29. **Change history**

```text
Current state
    ↓
Weaknesses
    ↓
Target state
    ↓
Automation opportunities
    ↓
Product impact
    ↓
Process maturity
    ↓
Next review date
```

### Maturity scale (shared with Customer Value Engine)

| Score | Meaning |
|------:|---------|
| 1 | Founder-driven |
| 2 | Documented |
| 3 | Standardized |
| 4 | Automated |
| 5 | Scalable |

---

## By phase

| Phase | Folder |
|-------|--------|
| Acquire | [acquire/](acquire.md) |
| Deliver | [deliver/](deliver.md) |
| Operate | [operate/](operate.md) |
| Expand | [expand/](expand.md) |
| Advocate | [advocate/](advocate.md) |

## Priority for first SOPs

| Priority | SOP | Status |
|----------|-----|--------|
| 1 | [Deliver — Legacy System Migration](deliver/legacy-system-migration.md) | v1 model SOP |
| 2 | [Deliver — Bootstrap Environment](deliver/bootstrap-environment.md) | v1 — Infrastructure PowerShell (`bootstrap-client.ps1`) |
| 3 | [Deliver — Customer Onboarding](deliver/customer-onboarding.md) | <mark style="color:red;">Placeholder</mark> *(start of Implementation domain)* |
| 4 | Deliver — go-live / training | Not started |
| 5 | Acquire — demo | Not started |
| 6 | Acquire — proposal / contract | Not started |
| 7 | Operate — support triage | Not started |

**Migration domain (standards):** Philosophy, Architecture, Decision Matrix, Package Standards, Configuration, Validation, Metrics, and per-vendor guides are under [deliver/](deliver/README.md).

**Bootstrap / environment domain (standards):** Bootstrap Standard, Inventory, Lifecycle, Classification, Baseline DB, Bootstrap vs Configuration, Hub draft, and [Environment Health Checklist](../checklists/environment-health-checklist.md) — treat as complete enough to move primary effort to **Implementation** (configuration after bootstrap).

Interview owners and document what is done today, then improve.
