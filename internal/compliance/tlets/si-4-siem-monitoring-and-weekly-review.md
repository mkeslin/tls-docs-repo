# Thin Line SIEM monitoring and weekly review addendum (SI-4)

**Status:** Internal working template — Thin Line completes the Azure/Sentinel portion; the agency retains its own SIEM/monitoring for agency network and boundary systems.  
**Purpose:** Supplements the agency’s SI-4 / SIEM program with Thin Line’s monitoring of Thin Line–managed **Microsoft Azure Government** resources for Thin Line **RMS/CAD/JMS**.  
**Download:** [Editable Word template](forms/si-4-siem-monitoring-and-weekly-review.docx) · [Weekly review log (.csv)](forms/si-4-weekly-review-log.csv)  
**Handling:** Mark the completed attachment **FOR OFFICIAL USE ONLY (FOUO)** or with the agency/DPS-required handling label.

> **Use this as an addendum to the agency’s existing SIEM / monitoring process.** The agency remains responsible for monitoring and weekly review of agency-owned networks, endpoints, firewalls, and any agency-operated SIEM. This document covers only Thin Line–hosted Azure Government application and platform signals.

This document does not replace the SIEM report itself. Submit: (1) an exported consolidated report with a visible date range, (2) the weekly review record (log), and (3) this addendum.

---

## 1. Submission information

| Field | Entry |
|---|---|
| Agency | `[AGENCY NAME]` |
| ORI | `[ORI]` |
| Thin Line tenant key / environment | `[TENANT KEY / ENVIRONMENT]` |
| Products in scope | RMS / CAD / JMS *(delete products not purchased)* |
| Agency SIEM / monitoring policy supplemented | `[AGENCY POLICY / TOOL NAME / N/A]` |
| Thin Line SIEM tool | Microsoft Sentinel (Azure Government) |
| Report cadence | At least weekly |
| Effective date | `[YYYY-MM-DD]` |
| Thin Line preparer | `[NAME / TITLE]` |
| Agency reviewer | `[NAME / TITLE]` |
| Weekly review log filename / location | `[e.g. si-4-weekly-review-log.csv — PATH / REVISION]` |

---

## 2. Relationship to agency monitoring

This addendum supplements **`[AGENCY SIEM / MONITORING POLICY]`** for security monitoring associated with **Thin Line Software LLC** and Thin Line RMS/CAD/JMS.

| Scope | Monitoring owner | Weekly review owner |
|---|---|---|
| Thin Line–hosted RMS/CAD/JMS and Thin Line–managed Microsoft Azure Government resources | Thin Line | Thin Line |
| Agency network, endpoints, firewalls, and other agency-owned security devices | Agency | Agency |
| Agency-operated SIEM (if any) | Agency | Agency |
| Proposed TLETS interface connector signals | Confirm after topology/implementation approval | Confirm after topology/implementation approval |

If this addendum conflicts with the agency’s SIEM policy, the more restrictive requirement applies unless the agency CJISO / authorized official documents an approved exception.

---

## 3. Thin Line monitoring narrative (SI-4)

Security-relevant events for Thin Line–hosted **RMS/CAD/JMS** in **Microsoft Azure Government** are collected into **Microsoft Sentinel** (backed by an Azure Monitor Log Analytics workspace in Azure Government).

**Target coverage:** Thin Line’s standard posture is to monitor **Thin Line–managed Azure Government resources** used for the tenant—application tiers, data stores, identity/admin paths in Azure, platform security alerts, and related Azure Monitor / diagnostic telemetry—so that security-relevant Azure signals for the hosted solution are available in Sentinel for alerting and weekly review. Exact data connectors, diagnostic settings, and tables must be confirmed from the **current** Sentinel / Log Analytics workspace before each agency submission (attach workspace evidence).

**Typical Thin Line–managed Azure sources intended for Sentinel (verify enabled for the tenant):**

| Source category | Examples of data captured | Review owner |
|---|---|---|
| Subscription / control plane | Azure Activity Log, resource changes, privileged Azure operations | Thin Line |
| Microsoft Defender for Cloud | Security alerts and recommendations for in-scope Azure resources | Thin Line |
| App Service (UI / API) | HTTP/platform diagnostics, app service logs, availability/failures | Thin Line |
| Azure SQL Database | SQL auditing / Defender for SQL signals as configured | Thin Line |
| Azure Storage / file shares | Storage diagnostic and security-relevant access signals as configured | Thin Line |
| Azure Monitor / Application Insights | Application and dependency telemetry used for security/ops review | Thin Line |
| Thin Line Azure administration identity | Microsoft Entra ID / Microsoft SSO sign-in and MFA signals for Thin Line cloud administration | Thin Line |

**Outside Azure (disclose separately if reviewed with this packet):** Application end-user authentication via **Descope** is not an Azure resource. Descope sign-in/MFA signals are reviewed under Thin Line identity operations and are not claimed as “Azure Sentinel coverage” unless a specific forwarder into Sentinel is configured and evidenced.

Analytics rules, workbooks, and/or scheduled queries generate alerts and a consolidated view that is reviewed **at least weekly** by **Thin Line personnel authorized for CJIS-scope duties** (applicable fingerprint-based screening and CJIS Security Awareness Training current). Findings are triaged, escalated, and tracked under Thin Line incident-response procedures. No shared or anonymous reviewer accounts are used.

Agency-owned network, endpoint, and security-device monitoring remain the agency’s responsibility under the agency’s SIEM/monitoring program.

---

## 4. Weekly review process (Thin Line–hosted scope)

1. Generate/export a consolidated Microsoft Sentinel report for the review period (Sentinel workbook, incident/alert summary, or scheduled analytics / KQL export) as **PDF or CSV**, with the **covered date range visible** on the export.  
2. Confirm the export matches the intended period.  
3. A CJIS-authorized Thin Line reviewer examines alerts, incidents, and notable signals for Thin Line–managed Azure resources.  
4. Record findings or an explicit **“no findings”** notation in the weekly review log.  
5. Open tickets/incidents for anything requiring action and reference them in the log.  
6. Store the export and the log entry under records retention.  
7. Escalate under Thin Line incident-response procedures when warranted.

**Cadence:** At least weekly.  
**Reviewer qualification:** Thin Line personnel authorized for CJIS-scope duties (fingerprint-based screening and CJIS Security Awareness Training current). Do not list individual names in this addendum; names appear only in the weekly review log and personnel attachments as needed.

---

## 5. Weekly review log — by reference

The authoritative weekly review record is the Thin Line SI-4 weekly review log named in section 1 (CSV or equivalent). That log is **incorporated by reference** and is not duplicated in full in this Word addendum.

Each log entry should include at least: review date, period covered, SIEM/report identifier, reviewer, alerts/incidents reviewed, findings or “no findings,” tickets/escalations, and a reference to the stored report export.

A starter CSV is available: [si-4-weekly-review-log.csv](forms/si-4-weekly-review-log.csv).

---

## 6. Retention (Thin Line standard)

| Control | Thin Line standard |
|---|---|
| Sentinel / Log Analytics security log retention | **365 days** (1 year) for the Thin Line Azure Government workspace used for SIEM, unless a longer period is required by agency contract |
| Weekly report exports + review log entries | Retained at least **1 year**, or longer if required by agency records policy / contract |
| Agency SIEM retention | Per agency policy (out of scope of this addendum) |

A capability available in Azure is not evidence that it is enabled. Confirm the workspace retention setting on the evidence date and attach a screenshot or export if requested.

---

## 7. Evidence checklist

- [ ] This Thin Line SI-4 addendum completed for the agency tenant  
- [ ] Exported consolidated Microsoft Sentinel report(s) with visible date range for the submission period  
- [ ] Weekly review log covering recent consecutive weeks (by reference)  
- [ ] Reference from each log entry to its stored report export  
- [ ] Current Sentinel / Log Analytics evidence of in-scope Azure data connectors / diagnostic forwarding (do not claim unconnected sources)  
- [ ] Workspace retention setting evidence (Thin Line standard: 365 days)  
- [ ] Clear split between Thin Line–owned Azure monitoring and agency-owned network/boundary SIEM  
- [ ] TLETS connector monitoring documented after topology/implementation approval (or marked pending)  
- [ ] Thin Line and agency approval/signoff  

---

## 8. Approval

By signing, the agency acknowledges this addendum as the Thin Line Azure/Sentinel portion of SI-4 monitoring for Thin Line RMS/CAD/JMS, supplementing the agency’s own SIEM/monitoring program.

| Role | Name/title | Signature or approval record | Date |
|---|---|---|---|
| Thin Line reviewer |  |  |  |
| Agency reviewer / LASO |  |  |  |

---

## Related

- [Interface Approval Packet answers](interface-approval-packet.md)
- [Cloud data storage disclosure](cloud-data-storage-disclosure-template.md)
- [Thin Line remote access addendum](thin-line-remote-access-addendum-template.md)
- [Direct-interface scope](direct-interface-scope.md)
- Canonical packet copy (product repo): `ThinLineSoftware/Docs/TLETS/application/si-4-siem-monitoring-and-weekly-review.md`
