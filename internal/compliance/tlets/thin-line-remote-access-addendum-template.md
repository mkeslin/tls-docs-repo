# Thin Line remote access addendum to agency policy

**Use when:** The agency already has an approved remote-access policy and needs a Thin Line–specific supplement for its CJIS Interface Approval Packet.

**Agency:** [AGENCY NAME]  
**ORI:** [ORI]  
**Agency policy supplemented:** [POLICY TITLE / NUMBER / VERSION / DATE]  
**Effective date:** [DATE]  
**Approved by:** [APPROVING AUTHORITY]

### Download Word

- **[Thin Line remote access addendum (.docx)](forms/thin-line-remote-access-addendum-template.docx)**
- Also listed under [Word forms](forms/README.md)

> Replace every bracketed field and obtain agency approval. The existing agency policy remains controlling; the more restrictive requirement applies if documents conflict.

**Standard Thin Line access model:** Cloud administration (Azure Government) **and** agency-attended endpoint support (ScreenConnect). On-premises TLETS connector administration is **out of scope** — the Thin Line TLETS interface connector is hosted in Microsoft Azure Government.

## Thin Line system and support boundary

Thin Line RMS/CAD is hosted in **Microsoft Azure Government**. Agency users access the application over encrypted HTTPS (TLS 1.2 or higher).

Thin Line support includes:

- administration of Thin Line–managed Azure Government resources;
- review of Thin Line application configuration, logs, and tenant data when authorized and necessary; and
- agency-attended support of an agency endpoint using the approved remote-support tool.

The Thin Line TLETS interface connector is hosted in Microsoft Azure Government. This addendum does **not** authorize Thin Line to administer an on-premises agency TLETS connector or grant unrestricted access to the agency network.

## Thin Line access methods

### Cloud administration

Authorized Thin Line personnel administer Thin Line–managed Azure Government resources through separately authenticated management interfaces. Thin Line does not remotely connect to the agency’s internal network or control agency endpoints under cloud administration alone. Any screen-sharing or agency-endpoint session requires separately approved attended endpoint support.

### Agency-attended endpoint support

Thin Line may view or control an agency endpoint only after case-specific agency authorization. An agency employee initiates or approves the session, can observe and terminate it, and confirms closure. Unattended access is prohibited unless separately documented and approved.

**Tool / version:** ScreenConnect by ConnectWise, version **26.4.3.9662** (and later Thin Line–deployed versions)  
**Approver roles:** Agency LASO / IT coordinator / supervisor (or other role designated by the agency) who authorizes the support ticket before the session begins  
**Observer / escort rule:** An authorized agency employee must remain present for the duration of the session (physical presence at the endpoint or active observation of the ScreenConnect session), may revoke consent or disconnect at any time, and confirms session closure. Thin Line shall not leave an unattended remote-control session on an agency endpoint.

**How the session is established**

1. Agency opens or approves a support ticket identifying the endpoint, purpose, Thin Line technician, and expected duration.
2. Agency staff start or accept a **ScreenConnect** support session and grant consent for remote view or control.
3. The named Thin Line technician authenticates to ScreenConnect with a unique identity and MFA before joining.
4. The agency escort remains able to observe and terminate the session at any time.
5. When work is complete, Thin Line disconnects; the agency confirms closure and ends the session.

**Encryption (CJI in transit on this path):** ScreenConnect encrypts session traffic using **AES-256** and **RSA** via the Microsoft RSA/Schannel Cryptographic Provider. ConnectWise documents this as **FIPS-compliant algorithm use on Windows**, not as a FIPS-certified ScreenConnect product. Attach current ConnectWise/ScreenConnect CJIS and FIPS evidence (see [ConnectWise ScreenConnect CJIS documentation](https://docs.connectwise.com/ScreenConnect_Documentation/On-premises/Advanced_setup/Criminal_Justice_Information_Services_(CJIS)_Security_Policy)).

## Authorized personnel

Only named Thin Line personnel satisfying applicable fingerprint-based screening, CJIS Security Awareness Training, and agency authorization may receive access. Shared or anonymous support accounts are prohibited.

**Approved personnel source:** Thin Line CJIS-scope personnel access list and fingerprint/training attachments in the agency packet (do not hardcode names in this addendum).

## Authentication and AA/MFA

- **Thin Line cloud administration:** Microsoft single sign-on with MFA for Thin Line–managed Microsoft Azure Government administration.
- **Agency application users:** Descope or an approved federated identity provider, with MFA enforced by the approved tenant configuration. Approved factors: one-time code via SMS, one-time code via email, and magic link via email.
- **Attended endpoint support:** Unique named identity, AA/MFA, explicit authorization, and agency-controlled revocation.

**Remote-tool MFA:** ScreenConnect MFA using a one-time email code for Thin Line host accounts used for attended sessions.  
**Emergency access:** None. Thin Line does not maintain a separate break-glass remote-access account or MFA-bypass path. Recovery of a Thin Line Microsoft identity follows Microsoft’s account-recovery process. ScreenConnect host access remains gated by ScreenConnect one-time email MFA. Agency-endpoint support still requires a normally authorized attended session.

## CJI in transit and FIPS evidence

CJI transmitted between agency endpoints and Thin Line–managed Azure Government application tiers uses **TLS 1.2 or higher**. Thin Line relies on FIPS 140-validated cryptographic modules operated by Microsoft for applicable Azure Government computing elements.

Thin Line does **not** represent Thin Line RMS/CAD or Azure Government as a whole as a FIPS-validated cryptographic module.

| Path / component | Product / module | Protocol | FIPS certificate # | Evidence | Owner |
|------------------|------------------|----------|--------------------|----------|-------|
| Agency browser → Thin Line UI/API | Microsoft Azure Government App Service / TLS termination; underlying Windows OS crypto modules | TLS 1.2+ (HTTPS) | SEE ATTACHED MICROSOFT MODULE MATRIX | [Azure FIPS 140](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-fips-140-2); [Windows FIPS validation](https://learn.microsoft.com/en-us/windows/security/security-foundations/certification/fips-140-validation); Azure Gov TLS screenshots | Thin Line |
| Thin Line interface → DPS/TLETS | Thin Line–operated TLETS interface connector in Microsoft Azure Government | Approved DPS path over TLS 1.2+ (message format, typically XDAC/OFML, pending TLETS Ops confirmation) | SEE ATTACHED MICROSOFT MODULE MATRIX | Architecture diagram; Interface Questionnaire; TLS/cipher export when available | Thin Line |
| Attended remote support | ScreenConnect by ConnectWise; AES-256 / RSA via Microsoft RSA/Schannel Cryptographic Provider | Encrypted ScreenConnect session | See Microsoft FIPS 140 module evidence for Schannel/RSA; ScreenConnect is not itself FIPS-certified | [ConnectWise ScreenConnect CJIS docs](https://docs.connectwise.com/ScreenConnect_Documentation/On-premises/Advanced_setup/Criminal_Justice_Information_Services_(CJIS)_Security_Policy); Thin Line MFA evidence | Thin Line + Agency |

## Thin Line authorization procedure

1. Open a support/change ticket with purpose, affected systems, access requested, and duration.
2. Identify possible CJI exposure and the named Thin Line support person.
3. Agency verifies the person’s approval, screening, and training.
4. Agency confirms least-privilege scope and required tool.
5. Agency approver records authorization before access, including start/expiration and observer requirements for attended support.
6. Agency enables only the approved account or remote-support session.
7. User authenticates with unique identity and AA/MFA.
8. Agency observer remains present for attended endpoint support when required.
9. Thin Line performs only approved work and records material changes.
10. Unexpected CJI exposure or suspicious activity is reported immediately.
11. Thin Line ends the session and confirms completion.
12. Agency disables temporary access and verifies disconnection.
13. Thin Line records work, systems, changes, and validation.
14. Agency reviews and closes or escalates the ticket.

**Emergency documentation deadline:** 24 hours

## Restrictions and records

Thin Line shall not copy CJI to local devices, consumer cloud storage, removable media, chat, or email; capture CJI screenshots/recordings without authorization; or install persistent remote-control software without express approval.

Retain request, authorization, participants, logs, systems accessed, changes, session times, exceptions, and closure validation under agency records-retention and CJIS policies.

**Activity review frequency:** At least monthly, or more frequently if required by agency policy  
**Personnel review frequency:** At least quarterly, and whenever personnel or screening/training status changes

## Approval

The agency incorporates this addendum into **[AGENCY POLICY]** for Thin Line support and administration.

**Access methods covered:** Cloud administration (Azure Government) and agency-attended endpoint support (ScreenConnect). On-premises TLETS connector administration is out of scope.

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
- [ ] ConnectWise ScreenConnect CJIS / security documentation

## Related

- [Full agency policy template](agency-remote-access-policy-template.md)
- [Interface Approval Packet answers](interface-approval-packet.md)
- [TLETS application home](README.md)
- Canonical packet template: `ThinLineSoftware/Docs/TLETS/attestation-kit/06-agency-inserts/THIN-LINE-REMOTE-ACCESS-ADDENDUM-TEMPLATE.md`
