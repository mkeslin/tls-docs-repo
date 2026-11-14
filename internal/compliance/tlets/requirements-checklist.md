# TLETS requirements — traceability hub

> Moved from TLS-App `Docs/TLETS/requirements-checklist.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

Rolling index for the **Thin Line TLETS Attestation Kit**. Detailed tasks live in linked documents; **`Status`** here is coarse.

**Process (Feb 2026):** [`process-dps-2026-02.md`](./process-dps-2026-02.md)

**Direct interface application:** [`application/README.md`](./application/README.md)

**Separate track:** CJIS in-app Help + audit reference → [`Docs/CJIS/`](../CJIS/)

---

## Direct TLETS interface application (in-app queries)

| ID | Topic | Primary document | Status |
|----|--------|------------------|--------|
| APP | Application hub | [application/README.md](./application/README.md) | Active |
| APP-SCOPE | Direct-interface scope | [application/DIRECT-INTERFACE-SCOPE.md](./application/DIRECT-INTERFACE-SCOPE.md) | Draft |
| APP-IQ | TLETS Interface Questionnaire fill guide | [application/tlets-interface-questionnaire.md](./application/tlets-interface-questionnaire.md) | Draft |
| APP-DEC | Open decisions (ORI, access, XDAC, topology) | [questions-open.md](./questions-open.md) | Open |

---

## Phase 1 — minimal first submission (default)

| ID | Topic | Primary document |
|----|--------|-------------------|
| P1 | Phase 1 overview | [phase-1/README.md](./phase-1/README.md) |
| P1-ESIGN | E-sign + DPS forward workflow | [phase-1/ESIGN-WORKFLOW.md](./phase-1/ESIGN-WORKFLOW.md) |
| P1-DPS | Agency DPS forward checklist | [phase-1/AGENCY-DPS-FORWARD-CHECKLIST.md](./phase-1/AGENCY-DPS-FORWARD-CHECKLIST.md) |
| P1-ASM | Markdown → PDF export | [phase-1/ASSEMBLY.md](./phase-1/ASSEMBLY.md) |
| P1-01 | Security program **summary** | [phase-1/01-security-program-summary.md](./phase-1/01-security-program-summary.md) |
| P1-SCOPE | Direct-interface scope | [application/DIRECT-INTERFACE-SCOPE.md](./application/DIRECT-INTERFACE-SCOPE.md) |
| P1-05 | Agency attestation (Phase 1) | [phase-1/05-agency-attestation-phase1.md](./phase-1/05-agency-attestation-phase1.md) |
| P2-KB | Kickback → full kit map | [phase-2-kickback/README.md](./phase-2-kickback/README.md) |

---

## Phase 2 — full attestation kit volumes

| Vol | ID | Topic | Primary document |
|-----|-----|--------|------------------|
| 00 | KIT-00 | Cover and agency instructions | [attestation-kit/00-cover-and-instructions.md](./attestation-kit/00-cover-and-instructions.md) |
| 01 | KIT-01 | Vendor security program (**agency starting point**) | [attestation-kit/01-vendor-security-program.md](./attestation-kit/01-vendor-security-program.md) |
| 02 | KIT-02 | Vendor evidence index | [attestation-kit/02-vendor-evidence-index.md](./attestation-kit/02-vendor-evidence-index.md) |
| 03 | KIT-03 | Architecture and data flow | [attestation-kit/03-architecture-and-data-flow.md](./attestation-kit/03-architecture-and-data-flow.md) |
| 04 | KIT-04 | Questionnaires | [attestation-kit/04-questionnaires.md](./attestation-kit/04-questionnaires.md) (+ [application/](./application/) for Interface Questionnaire) |
| 05 | KIT-05 | Agency attestation template | [attestation-kit/05-agency-attestation-template.md](./attestation-kit/05-agency-attestation-template.md) |
| 06 | KIT-06 | Agency inserts | [attestation-kit/06-agency-inserts/README.md](./attestation-kit/06-agency-inserts/README.md) |

---

## Supporting indexes

| ID | Topic | Primary document |
|----|--------|-------------------|
| AGENCIES | **Concurrent rollout** (5 agencies) | [agencies/README.md](./agencies/README.md) |
| PROC | DPS process and deliverable checklist | [process-dps-2026-02.md](./process-dps-2026-02.md) |
| Q-ISSUES | Outstanding questions | [questions-open.md](./questions-open.md) |
| TD-AGCY | Agency checklist (Slaton example) | [checklists/agency-template-sl8n.md](./checklists/agency-template-sl8n.md) |
| TD-VEND | Thin Line internal todos | [checklists/vendor-internal.md](./checklists/vendor-internal.md) |

---

## High-level rollup (Feb 2026 process)

| Bucket | Contents | Priority |
|--------|----------|----------|
| **Phase 1 (TL)** | Summary security program, scope statement, personnel PDFs, tenant inventory | **Blocking — first send** |
| **Phase 1 (agency)** | Phase 1 attestation, Addendum p8, **one** network diagram | **Blocking — first send** |
| **People** | Fingerprints + AT for TL CJIS-scope staff (agency-sponsored) | **Blocking** |
| **Phase 2 / kickback** | Full Vol 01 manual, Vol 03 architecture, questionnaires, SIEM, policies | On DPS request |
| **Internal reference** | CJIS 5.9.5 audit workbooks | Secondary — [`Docs/CJIS/reference/`](../CJIS/reference/) |

---

## Source record (authority)

| Field | Value |
|-------|--------|
| Authority / issuer | DPS CJIS Assessments — Kimberly Allen email 2026-02-20 |
| Document set / revision | Attestation kit v1 (reorganized 2026-07-06) |
