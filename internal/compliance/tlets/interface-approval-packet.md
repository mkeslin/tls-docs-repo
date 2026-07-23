# CJIS Security Office Interface Approval Packet — answers (pick a version)

**Form:** Texas DPS CJIS Security Office — *Criminal Justice Agency Interface Approval Packet*  
**Last revised:** 2026-07-20  
**Status:** <mark style="color:red;">Internal draft — choose one option where variants exist; agency must complete agency-owned fields</mark>

### Download the Word form

- **[CJIS Security Office Interface Approval Packet (.docx)](forms/cjis-security-office-interface-approval-packet.docx)** — working copy in this docs repo  
- Also listed under [Word forms](forms/README.md)  
- OneDrive original: `Reference Documents\TLETS\CJIS Security Office Interface Approval Packet.docx`

**Companion:** [Interface Questionnaire answers](interface-questionnaire.md) · [Scope](direct-interface-scope.md) · [Open decisions](open-decisions.md) · [TLETS application home](README.md)

**Ownership:** Many Yes/No rows are **agency**. Thin Line drafts are marked **TL**. Do not submit agency attestations Thin Line cannot truthfully make.

**Placeholders:** `[Agency]` · `[ORI]` · `[Agency POC fields]` · `[N]`

---

## Agency contact block — **Agency**

| Field | Options |
|-------|---------|
| Agency Name | `[Agency]` (e.g. Slaton Police Department) |
| ORI | `[ORI]` |
| Agency POC Name / Title / Phone / Alt / Email | Agency supplies |

---

## Vendor contact block — **TL**

| Field | Option A (recommended) | Option B |
|-------|------------------------|----------|
| Vendor Name | Thin Line Software LLC | Same |
| Vendor Solution | **Thin Line RMS** | **Thin Line RMS / CAD** (add **JMS** if jail queries/UI in scope) |
| Vendor POC Name | Matthew Keslin | Same |
| Vendor POC Title | Co-Founder | Same |
| Vendor POC Phone | 806-535-4455 | Same |
| Vendor POC Email | matthew.keslin@thinlinesoftware.com | Same |
| Alt Phone | _(blank)_ | _(blank)_ |
| Subcontractor POC | _(blank — no separate subcontractor)_ | Fill only if a named subcontractor has CJI access |

**Cover memo (optional):** Primary CPSO follow-up: Eric Gibson (ISCO).

---

## Will the proposed solution interface with CAD / RMS / JMS / Livescan / MBIS?

**Overall:** Yes (for modules in scope).

### Per-row choices

| Use | Option A — in scope (recommended if licensed) | Option B — not in this packet |
|-----|-----------------------------------------------|-------------------------------|
| **CAD** | Yes · Government Cloud · Enrollment: N/A *(or attach Azure enrollment if DPS requires)* · FIPS: *FIPS 140-validated cryptographic modules utilized by Microsoft Azure Government* | Leave blank / N/A if CAD not in this agency’s purchase |
| **RMS** | Same as CAD | — |
| **JMS** | Same as CAD if jail module in scope | **N/A / Choose N/A** if no JMS |
| **Livescan / Mobile ID** | — | **N/A** (recommended unless Livescan is in scope) |
| **MBIS / ULW** | — | **N/A** (recommended unless in scope) |

**FIPS note — pick wording:**

| Option | Paste this |
|--------|------------|
| **A — Recommended** | FIPS 140-validated cryptographic modules utilized by Microsoft Azure Government (Thin Line does not claim the RMS application itself is FIPS-certified). |
| **B — Explicit 140-2/140-3** | Microsoft Azure Government services rely on FIPS 140-2 / FIPS 140-3 validated cryptographic modules for applicable computing elements; see Microsoft Azure FIPS guidance. Thin Line RMS is not itself a FIPS-validated product. |
| **C — Avoid** | ~~Inventing a Thin Line or Azure “FIPS cert #” for the whole SaaS~~ |

---

## 5.1.1.5 Security Addendum

| Question | Option A | Option B |
|----------|----------|----------|
| Security Addendum for all vendors/CSP personnel with CJI support or secure-location access? | **Yes** — attach fully executed 8-page Addendum + FBI cert pages | **No** — do not submit until executed |
| Third party involved in hosting? | **Yes** — Microsoft Azure Government (CSP) | **No** — only if truly no CSP (not Thin Line’s model) |

---

## 5.12.1 Personnel screening — **Agency**

| Question | Option A | Option B |
|----------|----------|----------|
| Have all vendor personnel who access CJIS data been fingerprint-based background checked **by the agency** before access? | **Yes** — sponsoring LEA completed checks for Thin Line roster (Matthew Keslin, Eric Gibson, Eric Fugate) + AT | **No** — stop; complete fingerprints before DPS submit |

Thin Line cannot truthfully check **Yes** for the agency.

---

## Message switch location

| Option | When to use | Answer |
|--------|-------------|--------|
| **A — Recommended (cloud path)** | Connector / switch not on agency LAN | **No** |
| **B — On-prem connector** | Message switch/appliance inside agency secure location | **Yes** |
| **C — Hybrid** | Agency edge device + Azure | Answer **Yes** only if the *message switch* itself is in the secure location; otherwise **No** and show hybrid on diagram |

---

## AC-17 Remote access — **Agency** (Yes / No / N/A matrix)

Agency completes each row. Thin Line does **not** invent agency policy answers.

| Requirement | If agency has formal remote-access policy covering support | If not yet documented |
|-------------|--------------------------------------------------------------|------------------------|
| Usage restrictions / config / guidance for each remote access type | **Yes** | **No** (remediate before submit) |
| Each type explicitly authorized before use | **Yes** | **No** |
| Controls apply to MBIS/LiveScan/ULW devices | **Yes** / **N/A** if those devices out of scope | **N/A** or **No** |

**Attachment:** Agency remote access policy + step-by-step process + MFA/AA + encryption for remote CJI paths. Thin Line may attach a **vendor support remote-access SOP** as a supplement.

**Ready-to-adopt starting point:** [Agency remote access policy template](agency-remote-access-policy-template.md). The agency completes placeholders and the FIPS evidence register for the standard Thin Line access methods (Azure Government cloud administration + attended ScreenConnect support), and signs the approval section. On-premises connector administration is out of scope for the standard topology.

**Agency already has a remote-access policy:** use the narrower [Thin Line remote access addendum](thin-line-remote-access-addendum-template.md) instead.

---

## CM-2 Network diagram — **Agency** (+ TL may draft)

The agency owns and approves the final diagram because it must represent the agency's actual network and controls. This is a **joint artifact**, however: Thin Line should provide and verify the Thin Line/Azure Government/interface portion rather than asking the agency to infer it.

**Ready-to-adopt starting point:** [Agency network diagram template](agency-network-diagram-template.md). Use when the agency does not have a suitable current diagram; the agency replaces placeholders, removes unused alternatives, verifies its environment, and approves the result.

**Agency already has a diagram:** provide the narrower [Thin Line network diagram insert](thin-line-network-diagram-insert.md) for the agency to incorporate.

Required diagram content:

1. Paths from agency systems through interconnection to endpoints  
2. Logical location of firewalls, routers, switches, servers, encryption, clients (counts OK)  
3. FOUO marking  
4. Cloud components + FIPS/encryption for paths outside secure network; hosting links if multi-agency  
5. Agency name + revision date  

**Topology callouts to match Interface Questionnaire Q9:**

| Option | Show on diagram |
|--------|-----------------|
| **A — Azure connector** | Agency browsers → Thin Line Azure Gov UI/API/SQL → TLETS interface in Azure Gov → DPS |
| **B — Agency connector** | Agency browsers → Thin Line Azure Gov UI/API → on-prem Thin Line/agency connector → DPS |
| **C — Hybrid** | Both paths labeled |

---

## Cloud data storage details — **TL draft; Agency reviews**

Thin Line should prepare this attachment because Thin Line controls the cloud deployment and third-party service relationships. The agency reviews it and includes the approved, agency-specific copy in its submission.

**Ready-to-complete attachment:** [Cloud data storage and third-party vendor disclosure](cloud-data-storage-disclosure-template.md).

Row-level **Cloud Storage Inventory** and **Third-Party Vendor Register** tables live in the companion TLETS equipment and cloud worksheet workbook (Excel) and are **incorporated by reference** into the Word disclosure (the columns do not fit Word).

At minimum, the completed disclosure + workbook must identify:

1. Each production database, attachment/file store, backup/replica, and log/telemetry store
2. Exact Azure Government region for each resource and any backup/replication location
3. Data categories, encryption, retention, deletion, and access ownership
4. Microsoft as the primary CSP and every other third party that stores or may retain agency-related data (including always-on Descope, Maps, SendGrid, Twilio; and Stripe / Azure AI only if enabled)
5. Current evidence for configured resources—not merely capabilities available from Azure

Do not finalize the attachment until the agency's file storage, log retention, identity-provider residency, enabled integrations, and proposed TLETS connector storage/logging have been verified.

---

## SC-7 Boundary protection

### Checkbox rows — **Agency** for agency network; **TL** supports Azure narrative

| Requirement | Typical for this architecture |
|-------------|------------------------------|
| Control access to networks processing CJI | Agency: **Yes** (agency LAN) |
| Monitor/control at external and key internal interfaces | Agency: **Yes**; Azure side described by TL |
| Separate public subnets from internal | Agency: **Yes** / **N/A** per their design |
| External connections only through managed boundary devices | **Yes** |

### Narrative — pick one (**TL**)

| Option | Paste this |
|--------|------------|
| **A — Recommended** | The Thin Line solution is hosted in Microsoft Azure Government. Agency users access the application over encrypted HTTPS (TLS 1.2 or higher). Azure Government provides network boundary protection through managed platform controls (for example network security groups / firewall posture and monitored ingress/egress). Communications between agency devices and Thin Line occur through secure managed interfaces. Agency-owned firewalls, IDS/IPS, and on-prem boundary devices remain agency-controlled and are shown on the agency network diagram and equipment list. |
| **B — Shorter** | Thin Line RMS/CAD is hosted in Microsoft Azure Government and reached only over TLS 1.2+ HTTPS. Azure Government managed networking provides cloud boundary controls; agency boundary devices protect the agency network and are documented on the agency diagram/equipment list. |

Agency must still attach make/model/OS/firmware/EoS equipment list for **agency** devices.

**Ready-to-complete attachment:** [Agency boundary equipment and software worksheet](agency-boundary-equipment-worksheet.md) · [Download CSV](forms/agency-boundary-equipment-worksheet.csv). Each row uses a Diagram ID so the inventory can be reconciled to the network diagram.

---

## SC-13 Cryptographic protection (in transit) — **TL draft; agency confirms endpoint policies**

**⚠ Fix Word draft:** do not paste at-rest text here.

### Checkboxes

| Requirement | Option A | Option B |
|-------------|----------|----------|
| FIPS 140-2/140-3 modules for CJI in transit outside secure locations | **Yes** (Azure modules) | **N/A** only if DPS directs otherwise |
| AES ≥ 128-bit | **Yes** | — |
| Encryption policies for laptops/flash/mobile/external storage | **Agency Yes** if policy exists | **Agency No** until policy updated |
| TLS 1.2 or greater | **Yes** | — |

### Explanation — pick one

| Option | Paste this |
|--------|------------|
| **A — Recommended** | CJI in transit between agency endpoints and Thin Line Azure Government application tiers is protected using TLS 1.2 or higher. Cryptographic protection relies on FIPS 140-validated modules operated by Microsoft Azure Government for the computing elements that provide TLS termination and related services. Thin Line does not represent the RMS application itself as a FIPS-validated product. Encryption of agency laptops, removable media, and mobile devices is governed by agency policy. |
| **B — With screenshot evidence** | Same as A, plus: Minimum TLS and certificate bindings for Thin Line App Service endpoints are documented in attached Azure TLS configuration screenshots. |
| **C — Wrong (do not use)** | ~~At-rest Azure SQL TDE paragraph under SC-13~~ |

---

## SC-28 Protection of information at rest — **TL draft; agency confirms media policies**

### Checkboxes

| Requirement | Option A | Option B |
|-------------|----------|----------|
| FIPS modules for CJI at rest outside secure locations | **Yes** (Azure) | — |
| AES-256 | **Yes** | — |
| Laptop/flash/mobile/external encryption policies | **Agency Yes** | **Agency No** until fixed |
| Digital media encrypted outside secure rooms | **Agency Yes** | **Agency No** / **N/A** |

### Explanation — pick one

| Option | Paste this |
|--------|------------|
| **A — Recommended** | Criminal Justice Information stored within the Thin Line platform in Microsoft Azure Government is encrypted at rest using Azure service encryption / Transparent Data Encryption (for example Azure SQL), using AES-256 and relying on FIPS 140-validated cryptographic modules as described by Microsoft for Azure Government. Access to encrypted storage is restricted through authentication and role-based access controls. Agency endpoint and removable-media encryption remain agency-owned controls. |
| **B — Shorter** | CJI at rest in Thin Line’s Azure Government data stores is protected with AES-256 service encryption/TDE using FIPS 140-validated modules provided by Microsoft Azure Government. Agency device/media encryption is per agency policy. |

---

## 5.13 Mobile devices — **Agency** (+ TL product fact)

| Question | Option A | Option B | Option C |
|----------|----------|----------|----------|
| Will this solution include mobile devices? | **Yes** — browsers/PWA/MDTs/phones/tablets authorized | **No** — workstations only | **Yes** — MDTs/laptops only (no smartphones) |

Per device type (MDT/MDC, laptops, tablets, smartphones): agency marks **Yes / No / N/A** to match Q1 on the Interface Questionnaire.

| Policy acknowledgment | Option A | Option B |
|----------------------|----------|----------|
| Policy updated; MFA; MDM outside secure location | Agency checks “I have read and will comply” | Do not submit until policy/MDM path exists |

---

## Attestation & purpose — **TL purpose; Agency assessment Yes/No**

### Purpose narrative — pick one

| Option | When | Paste this |
|--------|------|------------|
| **A — Recommended** | Single-agency first submit | The purpose of the proposed interface is to allow authorized personnel of `[Agency]` (ORI `[ORI]`) using Thin Line RMS/CAD to securely submit TCIC/NCIC (TLETS) queries and receive responses through the Thin Line application. Thin Line Software LLC is the interface vendor. Access is authenticated, authorized, audited, and limited to personnel of the sponsoring criminal justice agency. The solution is hosted in Microsoft Azure Government. |
| **B — Multi-module** | RMS+CAD+JMS | Same as A, naming Thin Line RMS, CAD, and JMS as applicable licensed modules. |
| **C — Multi-agency host** | Only if Q8 = Yes on Interface Questionnaire | The purpose of the proposed interface is to allow authorized law enforcement agencies using the Thin Line platform to securely query and receive TCIC/NCIC (TLETS) data through the Thin Line application, each under its own ORI as listed in the TLETS Interface Questionnaire. Thin Line Software LLC is the interface vendor. Access is authenticated, logged, and restricted to authorized personnel of participating criminal justice agencies. Hosting is Microsoft Azure Government. |
| **D — Inquiry-only emphasis** | Matches Interface Questionnaire Q5 = Inquiry only | Same as A, adding: Initial access requested is TCIC Inquiry only (YNN without CCH), subject to DPS approval. |

### Agency assessment question — **Agency only**

| Option | Answer |
|--------|--------|
| **A — Ready to submit** | **Yes** — agency completed CA-style assessment vs current CJIS Security Policy |
| **B — Not ready** | **No** — do not send packet |

### Dates / Assessor(s)

| Field | Who |
|-------|-----|
| Date of Submission | Set on send |
| Date of Approval / Assessor(s) | **Leave blank** (DPS) |

---

## Final checklist (attachments)

| Item | Option A (include) | Option B |
|------|--------------------|----------|
| Fully executed Addendum + FBI pages | Required | — |
| Updated FOUO network diagram | Required | — |
| Cloud storage / CSP details | Completed [cloud storage and third-party disclosure](cloud-data-storage-disclosure-template.md) with current evidence | — |
| SIEM + weekly review samples | Exported SIEM report **plus** the completed [SI-4 monitoring and weekly review](si-4-siem-monitoring-and-weekly-review.md) log | <mark style="color:red;">Report alone (no review record) = expect kickback</mark> |
| Remote access policy + vendor remote procedure | Agency policy + Thin Line support SOP | — |
| This packet + Interface Questionnaire | Both | — |

---

## Suggested consistent bundles

| Bundle | Message switch | Mobile | Purpose | Matches Interface Questionnaire |
|--------|----------------|--------|---------|----------------------------------|
| **Safe first** | A (No) | A or C | A or D | Safe first bundle |
| **On-prem connector** | B (Yes) | as authorized | A | Q9 option C |
| **Multi-ORI host** | A | A | C | Q8 option B |

---

## Related

- [Download Word form](forms/cjis-security-office-interface-approval-packet.docx)
- [All Word forms](forms/README.md)
- [Interface Questionnaire answers](interface-questionnaire.md)
- [Open decisions](open-decisions.md)
- [Direct-interface scope](direct-interface-scope.md)
- [TLETS application home](README.md)
