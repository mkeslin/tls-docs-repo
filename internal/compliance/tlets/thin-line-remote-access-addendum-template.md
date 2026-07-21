# Thin Line remote access addendum to agency policy

**Use when:** The agency already has an approved remote-access policy and needs a Thin Line–specific supplement for its CJIS Interface Approval Packet.

**Agency:** [AGENCY NAME]  
**ORI:** [ORI]  
**Agency policy supplemented:** [POLICY TITLE / NUMBER / VERSION / DATE]  
**Effective date:** [DATE]  
**Approved by:** [APPROVING AUTHORITY]

> Replace every bracketed field, select the applicable access model, delete unused alternatives, and obtain agency approval. The existing agency policy remains controlling; the more restrictive requirement applies if documents conflict.

## Thin Line system and support boundary

Thin Line RMS/CAD is hosted in **Microsoft Azure Government**. Agency users access the application over encrypted HTTPS connections.

Thin Line support may include:

- administration of Thin Line–managed Azure Government resources;
- review of Thin Line application configuration, logs, and tenant data when authorized and necessary;
- agency-attended support of an agency endpoint; or
- administration of a specifically approved TLETS interface connector if deployed in the agency’s secure environment.

This addendum does not grant Thin Line unrestricted access to the agency network.

## Select the applicable access model

### ☐ Model A — Cloud administration only (recommended where accurate)

Thin Line does **not** remotely connect to the agency’s internal network or control agency endpoints. Authorized Thin Line personnel administer Thin Line–managed Azure Government resources through separately authenticated management interfaces. Any screen-sharing or agency-endpoint session requires Model B approval.

### ☐ Model B — Agency-attended endpoint support

Thin Line may view or control an agency endpoint only after case-specific agency authorization. An agency employee initiates or approves the session, can observe and terminate it, and confirms closure. Unattended access is prohibited unless separately documented and approved.

**Tool / version:** [TOOL]  
**Approver roles:** [ROLES]  
**Observer / escort rule:** [RULE]

### ☐ Model C — On-premises TLETS interface connector

Thin Line may administer the identified TLETS connector only through the managed path on the CJIS network diagram. This does not authorize general agency-network access.

**Connector / asset:** [HOSTNAME / ASSET ID]  
**Managed path:** [VPN / BASTION / OTHER]  
**Approval mechanism:** [PROCESS]

## Authorized personnel

Only named Thin Line personnel satisfying applicable fingerprint-based screening, CJIS Security Awareness Training, and agency authorization may receive access. Shared or anonymous support accounts are prohibited.

**Approved personnel source:** [ATTACHMENT / SYSTEM]

## Authentication and AA/MFA

- **Thin Line cloud administration:** Microsoft single sign-on with MFA for Thin Line–managed Microsoft Azure Government administration.
- **Agency application users:** Descope or an approved federated identity provider, with MFA enforced by the approved tenant configuration.
- **Agency-controlled paths:** Unique named identity, AA/MFA, explicit authorization, and agency-controlled revocation.

**Agency AA/MFA:** [METHOD]  
**Remote-tool MFA:** [METHOD]  
**Emergency access:** [METHOD OR NONE]

## CJI in transit and FIPS evidence

CJI transmitted between agency endpoints and Thin Line–managed Azure Government application tiers uses **TLS 1.2 or higher**. Thin Line relies on FIPS 140-validated cryptographic modules operated by Microsoft for applicable Azure Government computing elements.

Thin Line does **not** represent Thin Line RMS/CAD or Azure Government as a whole as a FIPS-validated cryptographic module.

| Path / component | Product / module | Protocol | FIPS certificate # | Evidence | Owner |
|------------------|------------------|----------|--------------------|----------|-------|
| Agency browser → Thin Line UI/API | Azure Government deployed module | TLS 1.2+ | [# OR “SEE ATTACHED MICROSOFT MODULE MATRIX”] | [EVIDENCE] | Thin Line |
| Thin Line interface → DPS/TLETS | [CONNECTOR / MODULE] | [PROTOCOL] | [#] | [EVIDENCE] | [OWNER] |
| Attended remote support | [TOOL / MODULE] | [PROTOCOL] | [#] | [EVIDENCE] | Agency |
| VPN/bastion → connector | [PRODUCT / MODULE] | [PROTOCOL] | [#] | [EVIDENCE] | Agency |

Do not enter a certificate number for Thin Line RMS or Azure Government as a whole. Attach evidence for the applicable validated module and approved configuration.

## Thin Line authorization procedure

1. Open a support/change ticket with purpose, affected systems, access requested, and duration.
2. Identify possible CJI exposure, access model, and named Thin Line support person.
3. Agency verifies the person’s approval, screening, and training.
4. Agency confirms least-privilege scope and required tool.
5. Agency approver records authorization before access, including start/expiration and observer requirements.
6. Agency enables only the approved account, VPN, bastion, invitation, or connector path.
7. User authenticates with unique identity and AA/MFA.
8. Agency observer remains present for Model B when required.
9. Thin Line performs only approved work and records material changes.
10. Unexpected CJI exposure or suspicious activity is reported immediately.
11. Thin Line ends the session and confirms completion.
12. Agency disables temporary access and verifies disconnection.
13. Thin Line records work, systems, changes, and validation.
14. Agency reviews and closes or escalates the ticket.

**Emergency documentation deadline:** [TIME PERIOD]

## Restrictions and records

Thin Line shall not copy CJI to local devices, consumer cloud storage, removable media, chat, or email; capture CJI screenshots/recordings without authorization; or install persistent remote-control software without express approval.

Retain request, authorization, participants, logs, systems accessed, changes, session times, exceptions, and closure validation under agency records-retention and CJIS policies.

**Activity review frequency:** [FREQUENCY]  
**Personnel review frequency:** [QUARTERLY / ANNUALLY]

## Approval

The agency incorporates this addendum into **[AGENCY POLICY]** for Thin Line support and administration.

**Models:** ☐ A — Cloud only · ☐ B — Attended support · ☐ C — On-prem connector  

**Agency approving official:** ______________________________  
**Title:** _________________________________________________  
**Signature / date:** ______________________________________  

**Agency CJISO / security reviewer:** _______________________  
**Signature / date:** ______________________________________  

**Thin Line representative:** _______________________________  
**Title:** _________________________________________________  
**Signature / date:** ______________________________________

## Attachments

- [ ] Existing agency remote-access policy
- [ ] Approved CJIS network diagram
- [ ] Thin Line authorized personnel list
- [ ] Cryptographic-module / FIPS evidence
- [ ] AA/MFA evidence
- [ ] Sample authorization / support ticket

## Related

- [Full agency policy template](agency-remote-access-policy-template.md)
- [Interface Approval Packet answers](interface-approval-packet.md)
- [TLETS application home](README.md)
- Canonical packet template: `ThinLineSoftware/Docs/TLETS/attestation-kit/06-agency-inserts/THIN-LINE-REMOTE-ACCESS-ADDENDUM-TEMPLATE.md`

