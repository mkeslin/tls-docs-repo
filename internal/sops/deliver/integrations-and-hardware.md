# Integrations and hardware

**Lifecycle step:** 5 · Integrations and hardware  
**Milestone outcome:** Integrations and hardware verified (or N/A)  
**Document type:** Phase overview  
**Status:** <mark style="color:red;">Placeholder</mark>  

Engagement status: ☐ Not started · ☐ In progress · ☐ Complete · ☐ N/A

CVE stage: [Integrations and hardware](../../customer-value-engine/deliver/integrations-and-hardware.md)

---

## Purpose

Connect and prove customer-required **integrations** (TLETS, payments, partners, exports, CAD webhooks, etc.) and confirm **hardware** (mobile printers, scanners, workstations) so go-live is not blocked by unknown interface or device failures.

---

## Inputs

| Input | Source |
|-------|--------|
| Configuration Complete (or parallel agreement) | [Configuration](configuration/README.md) |
| Integration list from kickoff / contract | Handoff / Kickoff |
| Hardware list from kickoff / quote | Kickoff / Sales |
| Vendor credentials / endpoints | Customer |
| Agency settings that enable integrations | [Agency & Module Settings](configuration/agency-settings.md) (Stripe, OmniBase, CAD webhooks, etc.) |

---

## Activities

### Integrations

1. Confirm in-scope integrations from Kickoff discovery.  
2. Configure each integration (product Admin + vendor side as required).  
3. Test end-to-end with the customer.  
4. Document failovers / known limits for Operate.  

### Hardware

1. Confirm devices ordered / received ([Hardware Readiness Checklist](../../checklists/hardware-readiness-checklist.md)).  
2. Install drivers / pair devices in the target environment.  
3. Print / scan / mobile smoke tests for go-live roles.  

<mark style="color:red;">**TODO:**</mark> Integrations SOP and per-integration checklists (TLETS, Stripe, OmniBase, CAD partners, exports).

---

## Outputs

- Verified integration matrix (pass / fail / deferred)  
- Hardware readiness completed or N/A  
- Runbooks or notes for Operate  

---

## Exit criteria

- [ ] Each in-scope integration tested or explicitly deferred with risk acceptance  
- [ ] [Hardware Readiness Checklist](../../checklists/hardware-readiness-checklist.md) complete or N/A  
- [ ] No unknown blockers for Go Live  

If no integrations **and** no hardware in scope: mark **N/A**.

---

## Referenced SOPs / standards / checklists

| Doc | Type |
|-----|------|
| [Hardware Readiness Checklist](../../checklists/hardware-readiness-checklist.md) | Checklist |
| [Agency Configuration Checklist](../../checklists/agency-configuration-checklist.md) | Related (settings that enable integrations) |
| <mark style="color:red;">**TODO:**</mark> Integrations SOP | Procedure |
| [Implementation overview](implementation-overview.md) | Parent |

**Previous:** [Configuration](configuration/README.md)  
**Next:** [Training](training.md)
