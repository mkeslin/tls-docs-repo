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

> Replace every bracketed field and have the agency CJISO / authorized official approve the result. This template does not replace agency counsel, DPS, or CJIS Security Office direction.

**Standard Thin Line access model:** Cloud administration (Azure Government) **and** agency-attended endpoint support (ScreenConnect). On-premises TLETS connector administration is **out of scope** — the Thin Line TLETS interface connector is hosted in Microsoft Azure Government.

## Purpose

This policy defines how **[AGENCY NAME]** authorizes, enables, monitors, and terminates remote access associated with **Thin Line Software LLC** and Thin Line RMS/CAD. Access must have an approved business purpose, use unique identities and AA/MFA, use encrypted transport, follow least privilege, and be auditable.

## Thin Line access methods

### Cloud administration

Thin Line does **not** remotely connect to the agency’s internal network or control agency endpoints under cloud administration alone. Authorized Thin Line personnel administer Thin Line–managed Microsoft Azure Government resources through separately authenticated management interfaces using Microsoft single sign-on with MFA. Agency users access Thin Line RMS/CAD over HTTPS.

Any screen-sharing or agency-endpoint session requires separately approved attended endpoint support.

### Agency-attended remote support

Thin Line may view or control an agency endpoint only after case-specific agency authorization. An authorized agency employee initiates or approves the session, can observe and terminate it, and confirms closure. Unattended access is prohibited unless separately documented and approved.

**Approved tool / version:** ScreenConnect by ConnectWise, version **26.4.3.9662** (and later Thin Line–deployed versions)  
**Approver roles:** Agency LASO / IT coordinator / supervisor (or other role designated by the agency) who authorizes the support ticket before the session begins  
**Observer / escort rule:** An authorized agency employee must remain present for the duration of the session (physical presence at the endpoint or active observation of the ScreenConnect session), may revoke consent or disconnect at any time, and confirms session closure. Thin Line shall not leave an unattended remote-control session on an agency endpoint.

**How the session is established**

1. Agency opens or approves a support ticket identifying the endpoint, purpose, Thin Line technician, and expected duration.
2. Agency staff start or accept a **ScreenConnect** support session and grant consent for remote view or control.
3. The named Thin Line technician authenticates to ScreenConnect with a unique identity and MFA before joining.
4. The agency escort remains able to observe and terminate the session at any time.
5. When work is complete, Thin Line disconnects; the agency confirms closure and ends the session.

**Encryption (CJI in transit on this path):** ScreenConnect encrypts session traffic using **AES-256** and **RSA** via the Microsoft RSA/Schannel Cryptographic Provider. ConnectWise documents this as **FIPS-compliant algorithm use on Windows**, not as a FIPS-certified ScreenConnect product. Attach current ConnectWise/ScreenConnect CJIS and FIPS evidence (see [ConnectWise ScreenConnect CJIS documentation](https://docs.connectwise.com/ScreenConnect_Documentation/On-premises/Advanced_setup/Criminal_Justice_Information_Services_(CJIS)_Security_Policy)).

### Out of scope — on-premises TLETS connector administration

The Thin Line TLETS interface connector is hosted in Microsoft Azure Government. This policy does **not** authorize Thin Line to administer an on-premises agency TLETS connector or use an agency VPN/bastion path to a connector host.

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

**Thin Line application users:** Agency users authenticate through **Descope or an approved federated identity provider**, with MFA enforced by the approved tenant configuration. Approved factors: one-time code via SMS, one-time code via email, and magic link via email.

**Attended remote support:** Unique identity, AA/MFA, explicit authorization, and agency-controlled revocation.

**Remote-tool MFA:** ScreenConnect MFA using a one-time email code for Thin Line host accounts used for attended sessions.  
**Emergency access:** None. Thin Line does not maintain a separate break-glass remote-access account or MFA-bypass path. Recovery of a Thin Line Microsoft identity follows Microsoft’s account-recovery process. ScreenConnect host access remains gated by ScreenConnect one-time email MFA. Agency-endpoint support still requires a normally authorized attended session.

## CJI in transit and FIPS evidence

CJI transmitted between agency endpoints and Thin Line–managed Microsoft Azure Government application tiers uses **TLS 1.2 or higher**. Thin Line relies on FIPS 140-validated cryptographic modules operated by Microsoft for applicable Azure Government computing elements. Thin Line does **not** represent Thin Line RMS/CAD or Azure Government as a whole as a FIPS-validated cryptographic module.

Do not invent a certificate number for the cloud service or rely only on the phrase “FIPS compliant.”

| Path / component | Product / crypto module | Protocol | FIPS certificate # | Evidence | Owner |
|------------------|-------------------------|----------|--------------------|----------|-------|
| Agency browser → Thin Line UI/API | Microsoft Azure Government App Service / TLS termination; underlying Windows OS crypto modules | TLS 1.2+ (HTTPS) | SEE ATTACHED MICROSOFT MODULE MATRIX | [Azure FIPS 140](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-fips-140-2); [Windows FIPS validation](https://learn.microsoft.com/en-us/windows/security/security-foundations/certification/fips-140-validation); Azure Gov TLS screenshots | Thin Line |
| Thin Line interface → DPS/TLETS | Thin Line–operated TLETS interface connector in Microsoft Azure Government | Approved DPS path over TLS 1.2+ (message format, typically XDAC/OFML, pending TLETS Ops confirmation) | SEE ATTACHED MICROSOFT MODULE MATRIX | Architecture diagram; Interface Questionnaire; TLS/cipher export when available | Thin Line |
| Agency remote-support path | ScreenConnect by ConnectWise; AES-256 / RSA via Microsoft RSA/Schannel Cryptographic Provider | Encrypted ScreenConnect session | See Microsoft FIPS 140 module evidence for Schannel/RSA; ScreenConnect is not itself FIPS-certified | [ConnectWise ScreenConnect CJIS docs](https://docs.connectwise.com/ScreenConnect_Documentation/On-premises/Advanced_setup/Criminal_Justice_Information_Services_(CJIS)_Security_Policy); Thin Line MFA evidence | Thin Line + Agency |

## Step-by-step authorization

### Request and validate

1. Open a support/change ticket with purpose, systems, requested access, and duration.
2. Identify whether CJI may be visible and whether cloud administration, attended support, or both apply.
3. Identify the named Thin Line person performing the work.
4. Agency verifies that person is approved and satisfies applicable screening/training.
5. Agency confirms the requested system, privilege, tool, and duration are the minimum necessary.

### Authorize and enable

6. Authorized agency approver records approval in **[SYSTEM]** before access.
7. Approval records approver, Thin Line user, assets, access method, start/expiration, purpose, and observer requirements.
8. Agency enables only the approved account or remote-support session.
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

**Emergency documentation deadline:** 24 hours

## Logging and review

Retain the request, authorization, participants, authentication/connection logs, systems accessed, changes, start/end time, exceptions, and closure validation under agency records-retention and CJIS policies.

**Review frequency:** At least monthly, or more frequently if required by agency policy  
**Authorized-personnel review:** At least quarterly, and whenever personnel or screening/training status changes

Access is revoked upon role change, termination, screening/training lapse, contract termination, or agency direction. Exceptions require written approval, compensating controls, and an expiration.

## Agency approval

By signing, the agency adopts the procedures in this document after resolving placeholders.

**Access methods covered:** Cloud administration (Azure Government) and agency-attended endpoint support (ScreenConnect). On-premises TLETS connector administration is out of scope.

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
- [ ] ConnectWise ScreenConnect CJIS / security documentation

## Related

- [Interface Approval Packet answers](interface-approval-packet.md)
- [TLETS application home](README.md)
- Canonical packet export template: `ThinLineSoftware/Docs/TLETS/attestation-kit/06-agency-inserts/AGENCY-REMOTE-ACCESS-POLICY-TEMPLATE.md`
