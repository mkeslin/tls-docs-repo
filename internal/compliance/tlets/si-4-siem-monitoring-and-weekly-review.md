# SIEM monitoring and weekly review (SI-4)

**Status:** Internal working template — Thin Line completes the monitoring narrative; the agency documents its own weekly review where the agency owns the tool.
**Purpose:** Pairs the exported SIEM report with evidence that security signals are reviewed at least weekly, as expected for SI-4 in CJIS Security Policy discussions.
**Download:** [Editable Word template](forms/si-4-siem-monitoring-and-weekly-review.docx) · [Weekly review log (.csv)](forms/si-4-weekly-review-log.csv)
**Handling:** Mark the completed attachment **FOR OFFICIAL USE ONLY (FOUO)** or with the agency/DPS-required handling label.

This document does not replace the SIEM report itself. Submit both: the exported consolidated report **and** the weekly review record below.

## What this requirement needs

The packet item asks for a SIEM monitoring tool **and** consolidated reports reviewed by the agency weekly. That is two artifacts:

| Artifact | Source | Who produces it |
|---|---|---|
| Consolidated SIEM report (with visible date range) | Exported/printed from the SIEM tool | Whoever operates the SIEM (Thin Line for Thin Line-managed Azure/Sentinel; agency for agency-owned SIEM) |
| Weekly review record (reviewer, date, findings, escalations) | The log in this template | The reviewing party (agency for agency-owned signals; Thin Line for Thin Line-hosted signals) |

Do not submit only the tool output. The review record is what demonstrates the weekly cadence.

## Ownership

| Scope | Monitoring owner | Weekly review owner |
|---|---|---|
| Thin Line-hosted RMS/CAD in Microsoft Azure Government | Thin Line | Thin Line |
| Agency network, endpoints, and agency-owned security devices | Agency | Agency |
| Agency-operated SIEM, if any | Agency | Agency |
| Proposed TLETS interface connector signals | Confirm after topology/implementation approval | Confirm after topology/implementation approval |

## 1. Submission information

| Field | Entry |
|---|---|
| Agency | `[AGENCY NAME]` |
| ORI | `[ORI]` |
| Environment/tenant | `[TENANT KEY / ENVIRONMENT]` |
| SIEM tool(s) | `[MICROSOFT SENTINEL / AGENCY SIEM / OTHER]` |
| Report cadence | Weekly (state day/frequency: `[DAY]`) |
| Effective date | `[YYYY-MM-DD]` |
| Prepared by | `[NAME / TITLE]` |
| Agency reviewer | `[NAME / TITLE]` |

## 2. Monitoring narrative (SI-4)

> Security-relevant events for the Thin Line-hosted RMS/CAD environment in Microsoft Azure Government are collected into `[MICROSOFT SENTINEL / LOG ANALYTICS WORKSPACE]`. Monitored sources include `[APP SERVICE / API LOGS]`, `[AZURE SQL AUDIT / DEFENDER]`, `[AZURE PLATFORM DIAGNOSTICS]`, `[IDENTITY / DESCOPE SIGN-IN EVENTS]`, and `[ADDITIONAL SOURCES]`. Analytics rules and scheduled reports generate alerts and a consolidated report that is reviewed at least weekly. Findings are triaged, escalated, and tracked under Thin Line incident-response procedures. Agency-owned network, endpoint, and security-device monitoring, and any agency-operated SIEM, remain the agency's responsibility and are reviewed under agency procedures.

Adjust the bracketed sources to match the deployment. Do not claim a monitored source that is not actually forwarded to the SIEM.

## 3. Monitored source inventory

| Source | Data captured | SIEM/sink | Alerting | Retention | Review owner | Evidence date |
|---|---|---|---|---|---|---|
| `[API / APP SERVICE]` | `[ACCESS / ERRORS / DIAGNOSTICS]` | `[SENTINEL / LAW]` | `[RULES / NONE]` | `[DURATION]` | `[THIN LINE / AGENCY]` | `[YYYY-MM-DD]` |
| `[AZURE SQL]` | `[AUDIT / DEFENDER ALERTS]` | `[SINK]` | `[RULES]` | `[DURATION]` | `[OWNER]` | `[YYYY-MM-DD]` |
| `[IDENTITY / MFA]` | `[SIGN-IN / MFA / LOCKOUT]` | `[SINK]` | `[RULES]` | `[DURATION]` | `[OWNER]` | `[YYYY-MM-DD]` |
| `[AZURE PLATFORM]` | `[ACTIVITY / NSG / DEFENDER]` | `[SINK]` | `[RULES]` | `[DURATION]` | `[OWNER]` | `[YYYY-MM-DD]` |
|  |  |  |  |  |  |  |

## 4. Weekly review process

1. Generate/export the consolidated SIEM report for the review period from `[SENTINEL WORKBOOK / SCHEDULED REPORT]`.
2. Confirm the export shows the covered date range.
3. Reviewer examines alerts, incidents, and notable signals.
4. Record findings or an explicit "no findings" notation.
5. Open tickets/incidents for anything requiring action and reference them in the log.
6. Store the export and the review-log entry under records retention.
7. Escalate under incident-response procedures when warranted.

## 5. Weekly review log

Use the [CSV log](forms/si-4-weekly-review-log.csv) for an ongoing record. Each row is one weekly review.

| Review date | Period covered (start–end) | SIEM/report | Reviewer | Alerts/incidents reviewed | Findings or "no findings" | Tickets/escalations | Report evidence reference |
|---|---|---|---|---|---|---|---|
| `[YYYY-MM-DD]` | `[YYYY-MM-DD – YYYY-MM-DD]` | `[TOOL / REPORT]` | `[NAME]` | `[COUNT / SUMMARY]` | `[NO FINDINGS / SUMMARY]` | `[TICKET IDs / NONE]` | `[FILENAME / LOCATION]` |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

## 6. Evidence checklist

- [ ] Exported consolidated SIEM report(s) with visible date range for the submission period
- [ ] Completed monitored-source inventory reflecting current forwarding
- [ ] Weekly review log covering recent consecutive weeks
- [ ] Reference from each log entry to its stored report export
- [ ] Analytics-rule or scheduled-report configuration evidence, if requested
- [ ] Retention settings for the SIEM workspace
- [ ] Clear split between Thin Line-owned and agency-owned monitoring/review

## 7. Approval

| Role | Name/title | Signature or approval record | Date |
|---|---|---|---|
| Thin Line reviewer |  |  |  |
| Agency reviewer / LASO |  |  |  |

## Known Thin Line baseline — verify per agency

- Thin Line operates **Microsoft Sentinel** in Azure Government for hosted RMS environments.
- Exact monitored sources, analytics rules, retention, and scheduled-report configuration must be confirmed from the current workspace before submission.
- Where the agency operates its own SIEM or owns network/endpoint monitoring, the agency documents and performs that weekly review.
- The TLETS connector's monitored signals cannot be finalized until the topology and implementation are approved.

## Related

- [Interface Approval Packet answers](interface-approval-packet.md)
- [Cloud data storage disclosure](cloud-data-storage-disclosure-template.md)
- [Direct-interface scope](direct-interface-scope.md)
