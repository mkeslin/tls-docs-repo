# Thin Line Software LLC — Information Security and Compliance Manual

> Moved from TLS-App `Docs/TLETS/attestation-kit/01-vendor-security-program.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Attestation kit:** Volume 01 — Vendor security program (full manual)  
**Phase 1 export:** Use [`../phase-1/01-security-program-summary.md`](../phase-1/01-security-program-summary.md) for first submission; provide this full document on DPS kickback.  
**Document status:** Working CJIS 5.9.5 revision for TLETS attestation kit (agency vetting starting point per DPS Feb 2026)  
**Supersedes / updates:** `ThinLineSoftware_InformationSecurityAndComplianceManual.docx`, updated September 2020  
**Prepared date:** 2026-05-14  
**Policy owner:** Information Security and Compliance Officer (ISCO)  
**Primary compliance scope:** Thin Line Software LLC hosted RMS, Microsoft Azure Government, CJIS Security Policy 5.9.5  
**Review cadence:** At least annually, and after material changes to the hosted RMS architecture, CJIS Security Policy, agency requirements, or incident response procedures.

## 1. Overview

Thin Line Software LLC (Thin Line) contracts with local government agencies to provide software solutions for law enforcement, fire departments, EMS, and emergency management. Due to the nature of these services, Thin Line may process, store, transmit, display, or support access to Criminal Justice Information (CJI), Criminal History Record Information (CHRI), Protected Health Information (PHI), personally identifiable information (PII), and other sensitive agency data.

This manual documents Thin Line's information security and compliance policies for the hosted Thin Line RMS service and related support operations. It is intended to support CJIS Security Policy 5.9.5, agency TLETS/CJIS readiness packets, and customer security review.

Thin Line RMS is a cloud-hosted records management system. For Slaton PD and similarly hosted deployments, Thin Line RMS is hosted in Microsoft Azure Government and accessed by agency users over HTTPS through a browser or approved progressive web app (PWA) workflow. Thin Line RMS may contain CJI/CHRI entered or maintained by agency users, but Thin Line RMS is not represented as the agency's direct TLETS, NCIC, or III wire-transaction interface unless separately documented and approved by the agency and DPS/CPSO.

Agency-owned TLETS terminals, ORI/TLETS identifiers, CJIS workstations, local networks, local facility controls, agency identity policies, and agency CJIS authority decisions remain agency responsibilities unless specifically assigned to Thin Line by contract or written DPS/CPSO direction.

## 2. Roles and Responsibilities

### 2.1 Information Security and Compliance Officer

Thin Line has designated **Eric Gibson** as the Information Security and Compliance Officer (ISCO).

The ISCO is responsible for:

- Maintaining this manual and related CJIS/TLETS compliance procedures.
- Coordinating security and compliance communications with agency representatives, Agency Coordinators, LASOs, TACs, and DPS/CPSO contacts as needed.
- Maintaining Thin Line CJIS-scope personnel records, including roster, training status, and fingerprint/background check evidence status.
- Coordinating evidence collection for audits and agency packet submissions.
- Coordinating incident response, evidence preservation, escalation, and post-incident review for Thin Line-hosted systems.
- Tracking policy exceptions, corrective actions, and annual review activity.

### 2.2 Agency Coordinator Contact List

The ISCO maintains an Agency Coordinator Contact List containing the names and contact information for agency representatives responsible for CJIS, TLETS, security, technical, and contract communications.

The list is reviewed at least annually and updated when an agency changes primary contacts or when Thin Line receives notice of a new TAC, LASO, Agency Coordinator, or operational contact.

### 2.3 Shared Responsibility

Thin Line is responsible for the security controls it operates for the hosted RMS application, Thin Line support operations, and Thin Line-managed Azure Government resources.

Customer agencies remain responsible for:

- ORI/TLETS identifiers and agency CJIS authority.
- Agency users and user authorization decisions.
- Agency workstations, mobile devices, peripherals, and local browser/device hardening.
- Agency TLETS terminals, CJIS inquiry systems, CAD/OpenFox or similar controlled interfaces.
- Agency local networking, firewall, Wi-Fi, VPN, physical security, evidence rooms, and wiring closets.
- Agency policy, sanctions, local training records, and agency personnel rosters.

Where a control is shared, Thin Line documents the hosted RMS portion and the agency documents the agency-owned portion.

## 3. Personnel Security Policy

### 3.1 CJIS-Scope Personnel Roster

Thin Line maintains a personnel access list for owners, employees, contractors, and vendors who may access CJI, CHRI, PHI, or systems containing such data as part of their job duties.

The roster includes, as applicable:

- Full name.
- Role or job function.
- Whether the person may access CJI/CHRI or PHI.
- Training status.
- Fingerprint/background check status or source record.
- Authorization date and review date.
- Access removal date, if applicable.

The current CJIS-scope roster for the Slaton PD / Thin Line packet is tracked separately in the TLETS evidence folder.

### 3.2 Personnel Access Changes

The ISCO updates the personnel access list within five business days after relevant personnel changes, including hiring, termination, transfer, role change, or access-scope change.

When a person no longer requires access to CJI/CHRI or hosted RMS administrative functions, Thin Line removes or disables access to applicable systems, directories, cloud resources, support tools, and privileged roles according to the access control procedure in this manual.

### 3.3 Security Awareness and Role-Based Training

Thin Line personnel with access to CJI/CHRI or systems supporting CJI/CHRI must complete CJIS security awareness training appropriate to their role before access is granted and on the schedule required by CJIS Security Policy or agency direction.

The ISCO maintains training records, including completion date, training source, role or module, and expiration/renewal date. Training evidence is retained for at least three years unless a longer retention period is required by contract, agency policy, or DPS/CPSO direction.

### 3.4 Fingerprint and Background Check Evidence

Thin Line maintains evidence status for fingerprint-based background checks for CJIS-scope personnel. Thin Line does not store raw fingerprint records, full SSNs, driver's license numbers, or similarly sensitive identity records in this repository or in general-purpose compliance packets.

Original records must be stored in the secure legal/compliance location and provided only through the channel requested by the agency, DPS, or CPSO.

### 3.5 Personnel Sanctions

Thin Line personnel are subject to sanctions for violating this manual, CJIS Security Policy requirements, customer data handling requirements, or other applicable security policies.

Sanctions may include counseling, retraining, access suspension, removal from CJIS-scope duties, contract action, termination, or referral to legal or law enforcement authorities as appropriate.

The ISCO documents sanctions or corrective actions related to security policy violations and ensures lessons learned are incorporated into future training or policy updates where appropriate.

## 4. Access Control Policy

### 4.1 General Access Principles

Access to CJI, CHRI, PHI, hosted RMS systems, and production support tools is granted according to least privilege, business need, and role assignment.

Access decisions may consider:

- Job assignment or support function.
- Agency authorization.
- Physical location.
- Logical location.
- Network path.
- Time-of-day or day-of-week restrictions.
- MFA and identity assurance.
- Whether the person has completed required training and personnel screening.

### 4.2 RMS User Authentication

Thin Line RMS uses Descope or an approved customer federation path for hosted RMS authentication. Thin Line validates authenticated sessions through token-based application controls. MFA is enforced according to the Descope tenant configuration or the upstream identity provider configuration approved for the deployment.

Agency workstation logons, agency Google/Microsoft identity policies, TLETS terminal authentication, and direct CJIS inquiry identity policies remain agency-owned unless otherwise documented.

### 4.3 Privileged and Support Access

Privileged access to production RMS systems, cloud resources, databases, logs, and support functions is limited to authorized Thin Line personnel with a documented support or operational need.

Privileged access must be:

- Approved through an internal support, operational, or emergency process.
- Time-limited where practical.
- Protected by MFA.
- Logged through the relevant identity, application, cloud, or SIEM system.
- Reviewed during routine audit or support access review.

Thin Line support access to customer data must be tied to a customer support need, production incident, approved maintenance activity, or compliance request.

### 4.4 Break-Glass and Recovery Access

Break-glass access is reserved for incidents or outages where normal administrative access is unavailable and immediate action is required to protect confidentiality, integrity, availability, or customer operations.

Break-glass use must be documented with:

- Person using the access.
- Date and time.
- Business reason.
- Systems accessed.
- Actions taken.
- Customer notification, if applicable.
- Post-use review and access reset/rotation, if applicable.

### 4.5 Account Review and Removal

The ISCO or designated system owner reviews CJIS-scope and privileged access at least annually and after personnel changes. Access that is no longer required must be removed promptly.

For terminated or transferred personnel, Thin Line disables applicable accounts, tokens, group memberships, privileged roles, and support access according to the account removal process.

## 5. Physical and System Access Policy

### 5.1 Thin Line Devices

Thin Line personnel agree that computers and devices that contain or access CJI, CHRI, PHI, or production support systems must:

- Remain locked with a password, PIN, biometric, or other approved local authentication when not in use.
- Automatically lock after no more than 30 minutes of inactivity.
- Use full-disk encryption when storing sensitive data.
- Use updated firewall and malware protection where applicable.
- Remain current with critical security patches.
- Be configured to reduce shoulder-surfing risk when CJI/CHRI or PHI is displayed.
- Avoid storing CJI/CHRI in consumer cloud sync services, including personal OneDrive, Google Drive, Dropbox, iCloud, or similar services.

### 5.2 Physical Areas Controlled by Thin Line

Thin Line does not require a Thin Line-owned RMS server or appliance at the customer police department for standard hosted RMS use.

Any Thin Line-controlled physical area containing systems or media with CJI/CHRI or PHI must:

- Remain locked when authorized personnel are not present.
- Restrict access to authorized personnel.
- Require visitor sign-in and escort.
- Protect printed or electronic media from unauthorized viewing or removal.
- Maintain access records appropriate to the area and risk.

Azure Government data center physical controls are operated by Microsoft. Thin Line relies on Microsoft compliance documentation for Azure Government physical security controls and provides Microsoft/Azure evidence where requested by the agency or assessor.

## 6. Mobile Device and Remote Work Policy

### 6.1 Mobile Access

Thin Line personnel must not use cellular devices or devices running limited-feature operating systems to process, store, or transmit CJI/CHRI or PHI unless the device, workflow, and agency authorization have been reviewed and approved.

For hosted RMS agency users, mobile or PWA access is subject to agency policy, agency device management, and DPS/CPSO direction. Thin Line documents RMS as a browser/PWA-accessible application; the agency remains responsible for MDM, endpoint encryption, screenshots, local cache controls, hotspot/tethering policy, and CJIS mobile policy applicability.

### 6.2 Thin Line Laptops and Mobile Workstations

Thin Line laptops or mobile workstations used for support or administrative access must:

- Use local authentication.
- Use MFA for cloud and production access.
- Use full-disk encryption.
- Use host firewall or equivalent endpoint controls.
- Use malware protection where applicable.
- Apply critical patches in a timely manner.
- Avoid local storage of CJI/CHRI unless specifically required and approved.

### 6.3 Personal Firewall

A personal firewall or equivalent endpoint protection control must be employed on devices that are mobile by design and used for Thin Line support or administrative duties.

At a minimum, the control should:

- Manage program access to the Internet.
- Block unsolicited inbound connections.
- Filter incoming traffic by IP address, protocol, or port.
- Maintain logs where supported.

## 7. Encryption and FIPS 140 Policy

### 7.1 Encryption Requirements

CJI, CHRI, PHI, and other sensitive customer data must be protected by encryption when transmitted outside a physically secure location or stored electronically outside a physically secure location.

Encryption must use AES-128 or stronger, or another agency-approved cryptographic mechanism, unless a stricter requirement applies by contract, law, CJIS Security Policy, or DPS/CPSO direction.

### 7.2 Microsoft Azure Government FIPS 140 Language

Thin Line RMS is hosted in Microsoft Azure Government. Microsoft states that FIPS 140 validation applies to cryptographic modules, not to a cloud service as a whole. Microsoft further states that cloud service providers can obtain and operate FIPS 140 validated cryptographic modules for the computing elements that comprise their cloud services, and that Azure services use FIPS 140 approved algorithms for data security.

For Azure SQL Database transparent data encryption (TDE), Microsoft states that TDE relies on FIPS 140 validated encryption through the underlying operating-system cryptographic modules.

Thin Line therefore documents the Azure Government services, TLS configuration, Azure SQL TDE status, and any customer-managed key or HSM configuration in use for the deployment, rather than representing Thin Line RMS itself as a FIPS-validated product.

### 7.3 FIPS Mode and Validation Claims

Thin Line does not represent the Thin Line RMS application or Azure cloud service itself as FIPS 140 validated. FIPS evidence must be tied to the relevant cryptographic module, Azure Government service configuration, TLS/certificate settings, Azure SQL TDE, and any Azure Key Vault or Managed HSM configuration used by the deployment.

Any statement that a system is operated in a FIPS-approved mode requires configuration evidence for the relevant module and service.

### 7.4 TLS and Certificates

Thin Line must maintain evidence for hosted RMS TLS settings, including:

- Public hostnames and endpoints.
- Minimum TLS protocol version.
- Certificate binding/status.
- Any front-end gateway, WAF, App Service, or equivalent TLS policy.
- Date of screenshot/export.

Weak or deprecated protocols must be disabled where administratively available in the hosted environment.

## 8. Media Protection and Data Handling Policy

### 8.1 Media Handling

Thin Line personnel must protect CJI/CHRI and PHI on both electronic and physical media until the data is securely deleted, sanitized, destroyed, returned, or transferred according to an approved process.

Examples of media include paper, hard drives, SSDs, CDs, DVDs, tapes, USB drives, backup exports, database exports, support artifacts, screenshots, logs, and removable storage.

### 8.2 Electronic Media Sanitization

Electronic media containing CJI/CHRI or PHI must be sanitized before reuse, redeployment, sale, return, or disposal.

Acceptable methods include:

- Cryptographic erase where encryption is in place and key destruction is appropriate.
- Secure wipe using tooling aligned to NIST SP 800-88 style sanitization.
- Physical destruction when wipe or reuse is not appropriate.
- Vendor-provided destruction with certificate of destruction where a third party is used.

The ISCO or designee maintains records of sanitization or destruction, including media identifier, date, method, person performing or witnessing the action, and destination or disposal method.

### 8.3 Physical Media Disposal

Physical media containing sensitive information must be destroyed when no longer required. Paper media must be shredded or incinerated. Optical discs, removable media, and drives must be shredded, drilled, crushed, degaussed, incinerated, or otherwise destroyed using an approved method that renders the data unrecoverable.

### 8.4 Cloud Data and Tenant Offboarding

For hosted RMS data, Thin Line uses controlled cloud and database processes for backups, retention, export, purge, and tenant offboarding. Thin Line does not routinely ship unencrypted database media from Thin Line premises to agency sites.

Offboarding or purge activities must be approved, documented, and performed according to the contract, agency instruction, and applicable retention requirements.

Microsoft is responsible for physical disposal and sanitization of Azure Government data center hardware under Microsoft's cloud service controls. Thin Line provides Microsoft compliance collateral where requested.

## 9. Audit Logging and SIEM Review Policy

### 9.1 RMS and Cloud Logging

Thin Line maintains audit and operational logging for hosted RMS and supporting cloud services as configured for the deployment.

Logs may include:

- RMS application audit events.
- User authentication and session events.
- Privileged support actions.
- API and application service telemetry.
- Database auditing or monitoring events.
- Azure platform diagnostic logs.
- Security alerts and incidents from Microsoft Sentinel or equivalent monitoring.

When Thin Line operates an approved **TLETS interface**, query/response logging for those transactions is documented as part of the interface design and agency packet. Other official TLETS/NCIC logging outside Thin Line’s interface path remains agency-owned unless otherwise agreed.

### 9.2 Weekly Review

Security-relevant logs, SIEM alerts, or consolidated monitoring reports must be reviewed at least weekly for hosted RMS production environments where CJI/CHRI may be present.

The review should document:

- Date range reviewed.
- Reviewer.
- Tool/report reviewed.
- Findings or "no findings" notation.
- Escalations or tickets opened.
- Corrective actions and closure status.

### 9.3 Log Protection and Retention

Audit logs must be protected from unauthorized modification or deletion through role-based access, cloud permissions, and monitoring controls.

Retention periods must be documented for RMS application logs, Azure/Sentinel logs, database audit logs, and backup records. Where the agency requires a longer retention period by contract or CJIS packet, Thin Line must document the applicable configuration or exception.

## 10. Security Alerts and Advisories Policy

The ISCO or designee monitors external security alerts, advisories, and directives relevant to Thin Line RMS and supporting services.

Sources may include:

- Microsoft Security Response Center and Azure service health/security notices.
- CISA.
- MS-ISAC.
- US-CERT / CISA alerts.
- Texas DIR and DPS CJIS Security Office notices where applicable.
- Vendor advisories for application, framework, database, identity, and cloud services used by Thin Line.

When relevant alerts are received, the ISCO or designee evaluates the impact to Thin Line RMS, notifies appropriate personnel, opens tracking work where needed, and documents actions taken.

## 11. Incident Response Policy

### 11.1 Purpose

This incident response policy prepares Thin Line to detect, analyze, contain, eradicate, recover from, and report physical or electronic security incidents affecting Thin Line systems, hosted RMS, CJI/CHRI, PHI, or customer data.

### 11.2 Scope

This policy applies to Thin Line personnel, support systems, cloud-hosted RMS resources, production infrastructure, security monitoring, and any Thin Line-managed systems or data that may contain or support CJI/CHRI or PHI.

Agency-owned facilities, TLETS terminals, CJIS workstations, local networks, and agency incident response procedures remain agency-owned. Thin Line coordinates with the agency when an incident affects hosted RMS or customer data.

### 11.3 Definitions

An **event** is an exception to normal system, infrastructure, or service operation. Not all events are incidents.

An **incident** is an event that violates or threatens to violate security policy, acceptable use, confidentiality, integrity, or availability of Thin Line systems, customer data, CJI/CHRI, or PHI.

### 11.4 Incident Severity

Thin Line categorizes incidents using four levels:

| Level | Name | Description |
|---|---|---|
| 0 | Low | Minimal impact, such as spam or isolated malware detection with no data exposure. |
| 1 | Medium | Significant but limited operational impact or suspected security issue requiring investigation. |
| 2 | High | Severe impact, service disruption, confirmed compromise, or suspected exposure of customer confidential data. |
| 3 | Extreme | Catastrophic impact, widespread outage, confirmed public exposure, ransomware, or major compromise affecting multiple clients or CJIS/PHI data. |

### 11.5 Evidence Preservation

Incident response must balance rapid containment with preservation of evidence. Thin Line preserves relevant logs, alerts, screenshots, configuration state, tickets, and communication records in a manner consistent with legal, administrative, and customer requirements.

### 11.6 Preparation

Thin Line prepares for incidents through:

- Security awareness training.
- Malware and endpoint protection.
- Firewalls, cloud security controls, and boundary monitoring.
- Personnel screening and access control.
- Physical security controls where Thin Line controls the area.
- Event logging and weekly security review.
- Patching and vulnerability management.
- Backup and recovery procedures.

### 11.7 Detection and Analysis

Detection may occur through:

- Personnel review of event data.
- Automated alerts from cloud monitoring or SIEM.
- Intrusion detection/prevention or firewall alerting.
- Customer report.
- Vendor alert.
- Suspicious physical or electronic activity.

Analysis determines the attack method, affected systems, data impact, severity, scope, and immediate containment options.

### 11.8 Containment, Eradication, and Recovery

The ISCO or designated incident lead coordinates containment, eradication, and recovery.

Containment may include disabling accounts, revoking tokens, blocking network paths, isolating systems, stopping services, preserving affected resources, or changing credentials.

Eradication may include removing malware, disabling malicious accounts, patching exploited vulnerabilities, correcting misconfiguration, and confirming no other systems were affected.

Recovery may include restoring from backup, rebuilding systems, validating application integrity, rotating secrets, increasing monitoring, and confirming customer service restoration.

### 11.9 Incident Reporting

If an incident involves or is suspected of involving CJI, Thin Line coordinates with the affected agency and follows the reporting path directed by the agency, DPS, or CPSO. The Texas DPS Information Security Officer incident reporting process must be followed when applicable.

### 11.10 Post-Incident Activity

After containment, eradication, and recovery, Thin Line conducts a post-incident review. The review should document:

- What happened and when.
- How the incident was detected.
- What systems/data were affected.
- Actions taken.
- Communication and notification.
- Evidence preserved.
- Lessons learned.
- Corrective actions.
- Policy or training updates needed.

## 12. Change Management and Release Policy

### 12.1 Change Control

Thin Line controls changes to hosted RMS source code, infrastructure, configuration, and production releases through documented change practices.

Production-impacting changes must be reviewed, approved, tested as appropriate, and traceable to a request, issue, pull request, release branch, deployment record, or emergency change record.

### 12.2 Production Release Review

Production release changes must be reviewed and merged by authorized personnel. For current release-branch practice, Matthew Keslin reviews and merges changes pushed to release branches that feed production pipelines.

Evidence may include:

- Pull request records.
- Release branch history.
- Pipeline run records.
- Test/build output.
- Deployment approvals.
- Change tickets or release notes.

### 12.3 Emergency Changes

Emergency changes are permitted when needed to restore service, remediate a critical vulnerability, contain an incident, or protect customer data.

Emergency changes must be documented after implementation, including reason, approver or incident lead, systems affected, testing performed, customer impact, rollback plan if applicable, and post-change review.

### 12.4 Baselines and Configuration Settings

Thin Line maintains baseline documentation for hosted RMS components, including:

- Azure Government resources.
- App Service/API/UI endpoints.
- Database resources.
- Identity/authentication configuration.
- TLS/certificate settings.
- Logging/monitoring configuration.
- External partner/service dependencies.

Deviations from baseline must be documented and approved when they materially affect security posture.

## 13. Vulnerability and Patch Management Policy

### 13.1 Vulnerability Intake

Thin Line identifies vulnerabilities through vendor advisories, Microsoft/Azure notices, dependency alerts, code review, scanning tools, incident findings, customer reports, and public security channels.

### 13.2 Scanning and Monitoring

Thin Line should perform vulnerability monitoring and scanning for hosted applications, dependencies, cloud resources, and externally exposed services at least monthly and when significant new vulnerabilities are identified.

Scanning tools and definitions/plugins should be updated before scans or when new vulnerabilities are reported.

### 13.3 Remediation Timelines

Thin Line prioritizes remediation using severity and exploitability. Unless a stricter contract or agency requirement applies, target remediation timelines are:

| Severity | Target remediation |
|---|---|
| Critical | 15 days |
| High | 30 days |
| Medium | 60 days |
| Low | 90 days |

Risk acceptance, compensating controls, or delayed remediation must be documented and approved.

### 13.4 Tracking and Closure

Vulnerabilities must be tracked to closure through tickets, pull requests, change records, or security work items. Closure evidence should include fix description, deployment date, verification, and any residual risk.

### 13.5 Vulnerability Reporting Channel

Thin Line maintains customer support and compliance contact paths for reporting security concerns. Thin Line should maintain a public or customer-visible vulnerability reporting process if required by CJIS audit, customer contract, or risk assessment.

## 14. System and Services Acquisition Policy

Thin Line documents external service providers and subprocessors that support hosted RMS functions, including identity, hosting, monitoring, telemetry, payments if used, AI services if enabled, and other tenant-specific integrations.

For each material service, Thin Line should document:

- Service name.
- Purpose.
- Data type or sensitivity.
- Region or hosting boundary where known.
- Logging or diagnostic owner.
- Review cadence.
- Contract/security review status.

Thin Line uses CJIS Security Addendum, contract language, vendor due diligence, and audit evidence as applicable to support external service oversight.

Unsupported system components must be replaced, upgraded, or supported through an approved compensating arrangement before they create unacceptable risk to hosted RMS.

## 15. Risk Assessment Policy

Thin Line maintains risk assessment practices for hosted RMS and supporting cloud services.

The risk assessment should:

- Categorize the hosted RMS and the information it processes.
- Identify threats, vulnerabilities, likelihood, and impact.
- Document risk ratings.
- Track mitigations and residual risk.
- Be reviewed at planned intervals and after significant changes.
- Inform security planning, control selection, and prioritization.

Risk assessment evidence may include a risk register, security plan, vulnerability reports, architecture diagrams, change records, and management review notes.

## 16. Maintenance Policy

Thin Line performs maintenance for hosted RMS application code, cloud configuration, dependencies, databases, and support tooling through remote administrative processes.

Maintenance activities must be:

- Performed by authorized personnel.
- Logged or otherwise traceable.
- Protected by MFA and least privilege.
- Tested or validated as appropriate.
- Communicated to customers when customer-visible.

Microsoft is responsible for Azure Government data center hardware maintenance and physical hardware replacement. Thin Line relies on Microsoft compliance documentation for Microsoft-operated infrastructure.

On-premises Thin Line maintenance at customer sites occurs only under a contracted statement of work or other approved arrangement.

## 17. Exceptions and Corrective Action

Exceptions to this manual must be documented, risk-reviewed, approved by the ISCO or appropriate leadership, and assigned an expiration or review date.

Corrective actions from audits, incidents, vulnerabilities, or policy exceptions must be tracked to closure.

## 18. Annual Review and Approval

The ISCO reviews this manual at least annually and after material changes. Review evidence should include:

- Review date.
- Reviewer.
- Summary of changes.
- Approval or acceptance.
- Next review date.

## Appendix A — Primary Audit Evidence Mapping

| Audit area | Manual section(s) |
|---|---|
| PA2 Awareness and training | Sections 3.3, 11.6 |
| PA3 Incident response | Section 11 |
| PA4 Auditing and accountability | Section 9 |
| PA5 Access control | Sections 4, 5, 6 |
| PA6 Identification and authentication | Sections 4.2, 4.3, 4.4 |
| PA7 Configuration management | Section 12 |
| PA8 Media protection | Section 8 |
| PA9 Physical protection | Section 5.2 |
| PA10 Systems and communications protection | Sections 7, 9, 12 |
| PA12 Personnel security | Section 3 |
| PA14 System and services acquisition | Section 14 |
| PA15 System and information integrity | Sections 10, 13 |
| PA16 Maintenance | Section 16 |
| PA19 Risk assessment | Section 15 |

## Appendix B — Source Links

- Microsoft Azure Government compliance: https://learn.microsoft.com/en-us/azure/azure-government/documentation-government-plan-compliance
- Microsoft Azure FIPS 140 compliance: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-fips-140-2
- Microsoft FIPS 140-2 compliance: https://learn.microsoft.com/en-us/compliance/regulatory/offering-fips-140-2
