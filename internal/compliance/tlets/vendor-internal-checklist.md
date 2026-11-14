# To-do — vendor (Thin Line Software) — TLETS attestation kit

> Moved from TLS-App `Docs/TLETS/checklists/vendor-internal.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Phase 1 first:** [`../phase-1/ESIGN-WORKFLOW.md`](../phase-1/ESIGN-WORKFLOW.md) · **Phase 2:** [`../phase-2-kickback/README.md`](../phase-2-kickback/README.md) · **Direct interface application:** [`../application/README.md`](../application/README.md)

Internal checklist for Thin Line RMS product, hosting, and security program artifacts.

**Concurrent agencies (Jul 2026):** Slaton · Crosby County SO · Littlefield · Crystal City · Levelland — [`../agencies/README.md`](../agencies/README.md)

**DPS process:** [`../process-dps-2026-02.md`](../process-dps-2026-02.md) — agency vetting + attestation (Feb 2026).

**CJIS audit / in-app work (separate):** [`Docs/CJIS/`](../../CJIS/)

---

## 0. Phase 1 e-sign — blocking (first send)

Follow [`../phase-1/ESIGN-WORKFLOW.md`](../phase-1/ESIGN-WORKFLOW.md).

- [ ] ISCO review [`../phase-1/01-security-program-summary.md`](../phase-1/01-security-program-summary.md) → Word/PDF
- [ ] Build shared PDFs: summary, scope, personnel bundle from [`../evidence/`](../evidence/)
- [ ] Per agency: cover ([`COVER-LETTER-ESIGN.md`](../phase-1/COVER-LETTER-ESIGN.md)), inventory, attestation, DPS checklist → PDFs 01–02
- [ ] Merge PDF 01 (vendor reference + checklist); upload envelope (01 review, 02 sign, optional addendum p8)
- [ ] Send e-sign to agency CJIS signatory; set completion deadline
- [ ] On completion: archive signed PDFs; remind agency to use [`AGENCY-DPS-FORWARD-CHECKLIST.md`](../phase-1/AGENCY-DPS-FORWARD-CHECKLIST.md) for DPS

---

## 1. Phase 2 / full kit — on kickback or coordinator request

### a. Volume 01 — security program

- [ ] Final review and date **Volume 01** ([`attestation-kit/01-vendor-security-program.md`](../attestation-kit/01-vendor-security-program.md))
- [ ] ISCO sign-off for PDF export

### b. Volume 02 — evidence gaps

- [ ] Explicitly capture **2026 sensitivity:** **partner endpoints without logging** — inventory TL surfaces and remediate/document
- [ ] DR process documented in kit narrative
- [ ] Evidence of **immutable** backup posture where claimed (or document Azure LTR/PITR honestly)
- [ ] **Microsoft Azure Government enrollment / agreement** artifact (§6 below)
- [ ] Standalone **remote access / support SOP** export for Vol 02

### c. Encryption in transit / at rest

- Use Microsoft Azure's module-focused FIPS 140 language (see [`../evidence/2026-05-14-microsoft-azure-government-fips-guidance.md`](../evidence/2026-05-14-microsoft-azure-government-fips-guidance.md)).
- [ ] Stack document (libraries, terminating endpoints, KMS/HSM linkage)
- [ ] Vol 03 diagrams reflect external encryption paths after updates
- [ ] Confirm **data and metadata** encryption story for CJIS-scope storage

### d. V5.9.5 portal assessment (secondary — unless CPSO directs)

- [ ] Complete cloud assessment if still required: https://texas.cjisapps.com/security/cjisaudit/index.pl  
- Reference only: [`Docs/CJIS/reference/`](../../CJIS/reference/)

---

## 2. SIEM coordination

| Topic | Decision / owner |
|-------|-------------------|
| Which SIEM (agency vs TL vs shared MSSP)? | TBD |
| Weekly consolidated review rhythm (SI‑4 posture) | TBD |

- [ ] Propose repeatable reporting for agencies without SIEM (Vol 06 insert support)
- [ ] Sample consolidated report for agency weekly review attestation

---

## 3. Security program (Volume 01)

Kimberly Allen (DPS, Feb 2026): agency starts vetting by requesting vendor **documented security program**.

- [x] Draft security program exists — polish for PDF export
- [ ] Map explicit CJISSECPOL CA crosswalk if agency requests

---

## 4. Security Addendum roster — Thin Line personnel

- [ ] Confirm CJIS-scope roster: **Matthew**, **Eric Gibson**, **Eric Fugate**; artifacts in [`../evidence/`](../evidence/)
- [ ] **Security Awareness** certificates current
- [ ] **Fingerprint-based** background confirmation — **agency acceptance pending**

---

## 5. TXRAMP / FedRAMP posture

| Question | Response |
|---------|----------|
| TXRAMP certified? | TBD |
| FedRAMP (any offering)? | TBD |

---

## 6. Microsoft Azure Gov — enrollment

- [ ] Enrollment / agreement artifact for Vol 02 (distribution per CPSO sensitivity rules)

---

## 7. Solution architecture (Volume 03)

Primary source: [`attestation-kit/03-architecture-and-data-flow.md`](../attestation-kit/03-architecture-and-data-flow.md)

| # | Topic | Notes |
|---|-------|-------|
| a | Cloud TLETS access | Direct in-app queries — see §8 and [`../application/`](../application/) |
| b | Dedicated interface server / connector host | Define Azure vs agency placement; match questionnaire Q9 |
| c | Authentication | Descope / SSO; MFA |
| d | MDM | Agency-owned unless PWA/mobile scope expands |
| e | Mobile / query UI | Browser/PWA on approved devices |
| f | TLS / FIPS cipher posture | Production cipher inventory + Azure module language |
| g | Technical stack dossier | Versions, change control, third-party services, scanners |

---

## 8. Direct TLETS interface application

**Hub:** [`../application/README.md`](../application/README.md)  
**Goal:** Approve **in-app NCIC/TLETS queries** with Thin Line as interface vendor.

- [ ] Lock decisions: sponsoring agency/ORI, access level, XDAC vs DAC, connector topology, DL images, device count — [`../questions-open.md`](../questions-open.md)
- [ ] Complete **TLETS Interface Questionnaire** using [`../application/tlets-interface-questionnaire.md`](../application/tlets-interface-questionnaire.md)
- [ ] Coordinate **CJIS Security Office Interface Approval Questionnaire** ([`../attestation-kit/04-questionnaires.md`](../attestation-kit/04-questionnaires.md))
- [ ] Review / export [`../application/DIRECT-INTERFACE-SCOPE.md`](../application/DIRECT-INTERFACE-SCOPE.md) after CPSO pass
- [ ] Update architecture exhibits for TLETS query path
- [ ] Align in-app CJIS Help copy when product ships queries ([`Docs/CJIS/`](../../CJIS/))

---

## Cross-links

- Agency tasks (Slaton example): [`agency-template-sl8n.md`](./agency-template-sl8n.md)  
- DPS process checklist: [`../process-dps-2026-02.md`](../process-dps-2026-02.md)  
- Direct interface application: [`../application/README.md`](../application/README.md)  
- Open Q&A: [`../questions-open.md`](../questions-open.md)  
- Kit assembly: [`../attestation-kit/README.md`](../attestation-kit/README.md)
