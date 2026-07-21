# Agency remote access policy — Thin Line approval template

**Status:** Internal working template for agency review and adoption  
**Agency:** [AGENCY NAME]  
**ORI:** [ORI]  
**Effective date:** [DATE]  
**Approved by:** [APPROVING AUTHORITY]  
**Review cycle:** At least annually and after material access or architecture changes

### Download Word

- **[Agency remote access policy template (.docx)](forms/agency-remote-access-policy-template.docx)**
- Also listed under [Word forms](forms/README.md)

> Replace every bracketed field, select the applicable access model, delete unused alternatives, and have the agency CJISO / authorized official approve the result. This template does not replace agency counsel, DPS, or CJIS Security Office direction.

## Purpose

This policy defines how **[AGENCY NAME]** authorizes, enables, monitors, and terminates remote access associated with **Thin Line Software LLC** and Thin Line RMS/CAD. Access must have an approved business purpose, use unique identities and AA/MFA, use encrypted transport, follow least privilege, and be auditable.

## Select the approved access model

### ☐ Model A — Cloud administration only (recommended where accurate)

Thin Line does **not** remotely connect to the agency’s internal network or control agency endpoints. Authorized Thin Line personnel administer Thin Line–managed Microsoft Azure Government resources through separately authenticated management interfaces using Microsoft single sign-on with MFA. Agency users access Thin Line RMS/CAD over HTTPS.

Any screen-sharing or agency-endpoint session requires separately approved Model B access.

### ☐ Model B — Agency-attended remote support

Thin Line may view or control an agency endpoint only after case-specific agency authorization. An authorized agency employee initiates or approves the session, can observe and terminate it, and confirms closure. Unattended access is prohibited unless separately documented and approved.

**Approved tool / version:** [TOOL]  
**Approver roles:** [ROLES]  
**Observer / escort rule:** [RULE]

### ☐ Model C — Approved on-premises interface connector

Thin Line may administer the specifically identified TLETS interface connector inside the agency’s secure environment only through the managed path shown on the approved CJIS network diagram. This does not authorize general access to the agency network.

**Connector / asset:** [HOSTNAME / ASSET ID]  
**Managed path:** [VPN / BASTION / OTHER]  
**Approval mechanism:** [PROCESS]

## Usage restrictions

Remote access shall:

1. be tied to a support ticket, approved maintenance, or incident;
2. use a unique named identity—shared vendor accounts are prohibited;
3. require AA/MFA and encrypted transport;
4. be limited to the minimum systems, privileges, and duration necessary;
5. prohibit copying CJI to local devices, consumer cloud storage, removable media, chat, or email;
6. prohibit persistent remote-control software unless expressly approved;
7. be logged using available agency, identity-provider, remote-tool, application, and cloud records; and
8. end promptly when work is complete or authorization expires.

## Authentication and AA/MFA

**Thin Line cloud administration:** Authorized Thin Line workforce identities use **Microsoft single sign-on with MFA** for Thin Line–managed Microsoft Azure Government administration.

**Thin Line application users:** Agency users authenticate through **Descope or an approved federated identity provider**, with MFA enforced by the approved tenant configuration.

**Agency-controlled remote paths:** Models B and C require a unique identity, AA/MFA, explicit authorization, and agency-controlled revocation.

**Agency AA/MFA method:** [METHOD]  
**Remote-tool MFA:** [METHOD]  
**Emergency access:** [METHOD OR NONE]

## CJI in transit and FIPS evidence

CJI transmitted between agency endpoints and Thin Line–managed Microsoft Azure Government application tiers uses **TLS 1.2 or higher**. Thin Line relies on FIPS 140-validated cryptographic modules operated by Microsoft for applicable Azure Government computing elements. Thin Line does **not** represent Thin Line RMS/CAD or Azure Government as a whole as a FIPS-validated cryptographic module.

The agency and Thin Line must identify validation evidence for every deployed remote-access path. Do not invent a certificate number for the cloud service or rely only on the phrase “FIPS compliant.”

| Path / component | Product / crypto module | Protocol | FIPS certificate # | Evidence | Owner |
|------------------|-------------------------|----------|--------------------|----------|-------|
| Agency browser → Thin Line UI/API | Azure Government deployed service/module | TLS 1.2+ | [# OR “SEE ATTACHED MICROSOFT MODULE MATRIX”] | [EVIDENCE] | Thin Line |
| Thin Line interface → DPS/TLETS | [CONNECTOR / MODULE] | [PROTOCOL] | [#] | [EVIDENCE] | [OWNER] |
| Agency remote-support path | [TOOL / MODULE] | [PROTOCOL] | [#] | [EVIDENCE] | Agency |
| Agency VPN/bastion → connector | [PRODUCT / MODULE] | [PROTOCOL] | [#] | [EVIDENCE] | Agency |

## Step-by-step authorization

### Request and validate

1. Open support/change ticket **[TICKET ID]** with purpose, systems, requested access, and duration.
2. Identify whether CJI may be visible and which access model applies.
3. Identify the named Thin Line person performing the work.
4. Agency verifies that person is approved and satisfies applicable screening/training.
5. Agency confirms the requested system, privilege, tool, and duration are the minimum necessary.

### Authorize and enable

6. Authorized agency approver records approval in **[SYSTEM]** before access.
7. Approval records approver, Thin Line user, assets, model, start/expiration, purpose, and observer requirements.
8. Agency enables only the approved account, VPN, bastion, invitation, or connector access.
9. User authenticates with a unique identity and AA/MFA.
10. Agency observer remains present for attended sessions when required.

### Perform, terminate, and close

11. Thin Line performs only approved work and documents material changes.
12. Available authentication, connection, application, and administrative logs are preserved.
13. Unexpected CJI exposure or suspicious activity is reported under incident-response procedures.
14. Thin Line ends the session and confirms completion.
15. Agency disables temporary access and verifies disconnection.
16. Thin Line records work, affected systems, changes, and validation in the ticket.
17. Agency reviews the record and closes or escalates the ticket.

## Logging and review

Retain the request, authorization, participants, authentication/connection logs, systems accessed, changes, start/end time, exceptions, and closure validation under agency records-retention and CJIS policies.

**Review frequency:** [FREQUENCY]  
**Authorized-personnel review:** [QUARTERLY / ANNUALLY]

Access is revoked upon role change, termination, screening/training lapse, contract termination, or agency direction. Exceptions require written approval, compensating controls, and an expiration.

## Agency approval

By signing, the agency adopts the selected models and procedures after resolving placeholders and deleting unused alternatives.

**Models:** ☐ A — Cloud only · ☐ B — Attended support · ☐ C — On-prem connector  

**Approving official:** ____________________________________  
**Title:** _________________________________________________  
**Signature / date:** ______________________________________  

**CJISO / security reviewer:** ______________________________  
**Signature / date:** ______________________________________  

## Attachments

- [ ] Approved CJIS network diagram
- [ ] Agency remote-access policy, if separate
- [ ] Thin Line authorized personnel list
- [ ] Cryptographic-module / FIPS evidence
- [ ] AA/MFA configuration evidence
- [ ] Sample authorization / support ticket

## Related

- [Interface Approval Packet answers](interface-approval-packet.md)
- [TLETS application home](README.md)
- Canonical packet export template: `ThinLineSoftware/Docs/TLETS/attestation-kit/06-agency-inserts/AGENCY-REMOTE-ACCESS-POLICY-TEMPLATE.md`

