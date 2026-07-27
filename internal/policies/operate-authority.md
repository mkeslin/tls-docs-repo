# Operate authority matrix

**Document type:** Policy (operating)  
**Status:** v0.1 — <mark style="color:red;">Draft</mark>  
**Audience:** Internal — Support, founders, Deliver (hypercare)  
**Related:** [Triage support request](../sops/operate/triage-support-request.md) · [Publish product update](../sops/operate/publish-product-update.md) · [SaaS pricing and discount guardrails](saas-pricing-and-discount-guardrails.md)

---

## Purpose

Define who owns steady-state support vs onboarding-period support, what Support may promise, and when to escalate — so Operate is not only “tell each other and hope.”

---

## Ownership (current → target)

| Situation | Primary owner today | Target |
|-----------|---------------------|--------|
| **Hypercare / early go-live** (onboarding & training window) | **Fugate** (with founders as needed) | Same — Deliver owns until hypercare exit |
| **Steady-state Operate** (after hypercare) | **Gibson** | Gibson primary; Fugate for training refresh / onboarding-adjacent asks |
| **Product defect / change required** | Whoever caught it → **Keslin** (product/priority) | Logged item + Keslin prioritizes; Support stays customer-facing until resolved or workaround accepted |
| **Billing / contract** | Keslin | Keslin |
| **Release notes / customer update email** | Ad hoc | Keslin approves content; designated sender publishes ([Publish product update](../sops/operate/publish-product-update.md)) |

**Transition rule:** After [hypercare exit](../sops/deliver/hypercare-and-transition.md), new issues are **Operate / Gibson** unless clearly training refresh or a still-open Deliver defect.

---

## Authority matrix

| Decision | Support (Gibson) owns alone | Escalate |
|----------|----------------------------|----------|
| Answer how-to / config within product | Yes | — |
| Attended remote support (ScreenConnect) | Yes — with agency authorization | Unusual CJIS / security asks |
| Classify severity P1–P3 | Yes | Disagreement on P1 → founder |
| Promise a **fix date** or custom build | **Never** | Product / founder |
| Confirm bug and open engineering item | Yes (log + notify) | Priority / release commitment → Keslin |
| Credit / fee waiver / SLA change | No | Founder / finance |
| Tell customer “we will build X” | No | Product roadmap owner (Keslin) |
| Emergency / security / widespread outage | Stabilize + notify | Founders immediately |

---

## Out of support scope (redirect)

| Topic | Redirect |
|-------|----------|
| Agency IT (PCs, network, printers, AD) | Agency IT / vendor |
| Third-party hardware / vendor apps Thin Line does not sell | That vendor |
| Custom reports / one-off development | Product / commercial path — not free Support |
| Billing disputes | Finance (Keslin) |
| Pre-sales / new modules | Acquire |

Be polite and clear: Support solves Thin Line product usage and defects; it is not unlimited professional services.

---

## Related

- [Triage support request](../sops/operate/triage-support-request.md)  
- [Publish product update](../sops/operate/publish-product-update.md)  
- [Hypercare and transition](../sops/deliver/hypercare-and-transition.md)  
