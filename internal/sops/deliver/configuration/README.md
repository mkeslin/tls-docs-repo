# Configuration

**Lifecycle step:** 4 · Configuration  
**Milestone outcome:** Configuration Complete  
**Document type:** Phase overview  
**Status:** v1  

Engagement status: ☐ Not started · ☐ In progress · ☐ Complete

CVE stage: [Configuration](../../../customer-value-engine/deliver/configuration.md)

---

## Purpose

Finish agency **business setup** so the customer can work in Thin Line: Admin → **Agency & Module Settings**, officers, users, codes, and related Admin areas. Distinct from Infrastructure ([Bootstrap vs Configuration](../infrastructure/bootstrap-vs-configuration.md)).

This phase ends when in-scope configuration is done (or deferred with owners)—not when integrations are live or training is finished.

---

## Inputs

| Input | Source |
|-------|--------|
| Infrastructure | [Infrastructure](../infrastructure/README.md) |
| Data Migration (or N/A) | [Data Migration](../data-migration/README.md) |
| Agency preferences / worksheets | Kickoff / customer |
| Module / license scope | Contract / Kickoff |
| Baseline codes already in bacpac | Seed DB |
| Migration Overrides (if migrated) | Number patterns / code maps |

---

## Activities

1. Complete [Agency & Module Settings](agency-settings.md) for the agency type and licensed modules (General, Modules, Notifications & Workflow, Reports, Documents; Record Sharing if multi-agency).  
2. Configure related Admin areas: officers, users/roles, codes, CAD dispatch agencies, evidence locations as in scope.  
3. Align record number patterns with migration Overrides when historical data was imported.  
4. Work customer decisions with the [Configuration discovery workbook](../../../../customer/implementation/configuration-discovery-workbook.md); keep internal verification on the [Agency configuration checklist](../../../checklists/agency-configuration-checklist.md).  
5. Smoke core workflows in the configured tenant (create/open a record in each enabled module family).  
6. Hand off open items (payments live verify, partner webhooks, devices) to [Integrations and hardware](../integrations-and-hardware.md) when needed.  

---

## Outputs

| Output | Notes |
|--------|--------|
| Configured agency settings | Identity, modules, headers, workflow toggles |
| People / codes ready for go-live cohort | Officers, users, required codes |
| Completed (or N/A) configuration checklist | Required |
| Config debt list | Deferred items with owners |

---

## Exit criteria

Milestone **Configuration Complete** when:

- [ ] [Agency Configuration Checklist](../../../checklists/agency-configuration-checklist.md) complete for go-live scope (or items deferred with owners)  
- [ ] Agency & Module Settings match [Agency & Module Settings](agency-settings.md) exit criteria for in-scope cards  
- [ ] Customer (or Implementation) can perform core workflows in a configured tenant (smoke)  
- [ ] Platform health remains green — not re-run as configuration; see [Environment Health Checklist](../../../checklists/environment-health-checklist.md) if infra changed  

---

## Referenced SOPs / standards / checklists

| Doc | Type |
|-----|------|
| [Agency & Module Settings](agency-settings.md) | Reference |
| [Configuration discovery workbook](../../../../customer/implementation/configuration-discovery-workbook.md) | Customer-facing decisions |
| [Agency configuration checklist](../../../checklists/agency-configuration-checklist.md) | Internal verification |
| [Bootstrap vs Configuration](../infrastructure/bootstrap-vs-configuration.md) | Boundary |
| [Implementation overview](../implementation-overview.md) | Parent |
| [Legacy onboarding questionnaire mapping](../legacy-onboarding-questionnaire-mapping.md) | Source→destination crosswalk |

**Previous:** [Data Migration](../data-migration/README.md) or [Infrastructure](../infrastructure/README.md)  
**Next:** [Integrations and Hardware](../integrations-and-hardware.md) or [Training](../training.md)
