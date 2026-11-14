# DPS process — agency vetting and attestation (Feb 2026)

> Moved from TLS-App `Docs/TLETS/process-dps-2026-02.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Source:** Kimberly Allen, CJIS Technical Compliance Analyst — email to M'Kayla Villarreal (Slaton PD), **2026-02-20**, re: new TLETS vendor process.

**Contact:** kimberly.allen@dps.texas.gov · 512.424.7186

---

## What changed

The agency is **responsible for vetting** the vendor solution and vendor employees according to **CJISSECPOL CA** (Contractor Assessment).

The **CJIS Security Addendum** requires the vendor to maintain a **documented security program** detailing how the solution meets **CJISSECPOL**. **Requesting this documentation from the vendor should be the agency’s starting point** for conducting its own assessments.

DPS will request an **attestation** confirming the agency thoroughly vetted the vendor and vendor personnel and found the vendor solution and employees compliant with **CJISSECPOL**, **TCIC Access Chart**, and other **State of Texas enhancements**.

---

## Agency obligations (summary)

1. **Vet vendor solution** using vendor security program + supporting evidence.
2. **Fingerprint-based background checks** (by the law enforcement agency) for all personnel with **any potential to access unencrypted CJI** — including **CSP personnel** (cloud provider staff in scope as proposed).
3. **Awareness & Training (AT)** for those personnel.
4. **Attest** to DPS that vetting was thorough and findings are compliant.

---

## Supporting documentation (may include)

Thin Line prepares most **vendor-owned** items in [`attestation-kit/`](./attestation-kit/). **Agency-owned** items use templates in [`attestation-kit/06-agency-inserts/`](./attestation-kit/06-agency-inserts/).

| Item | Owner | Kit volume / location |
|------|--------|------------------------|
| CJIS Security Addendum — fully executed (incl. CSP personnel if cloud) | Joint | Vol 02 + agency signatory (page 8) |
| Proposed diagram — agency’s entire CJIS network | Agency | Vol 06 insert |
| Agency network diagram — before / after / proposed changes | Agency | Vol 06 insert |
| Cloud data storage — location, enrollment, information exchange agreements | Thin Line draft; agency validates | Vol 02 / Vol 03 |
| Relevant **agency security policies** updated for proposed solution | Agency | Vol 06 insert |
| **SIEM** — consolidated reports reviewed **weekly** (SI-4) | Agency reviews; TL may supply reports | Vol 06 insert |
| **Remote access procedures** — product support personnel | Thin Line | Vol 02 |
| **TLETS Interface Questionnaire** | Joint | Vol 04 + [`application/tlets-interface-questionnaire.md`](./application/tlets-interface-questionnaire.md) (**required for direct in-app query track**) |
| **CJIS Security Office Interface Approval Questionnaire** | Joint | Vol 04 |
| Agency **self-attestation** — vetting + fingerprint investigations | Agency signs | Vol 05 |

---

## Deliverable checklist (status tracking)

Legend: **TL** = Thin Line, **AG** = agency, **JT** = joint.

### Network diagrams

| Element | Detail | Status |
|--------|--------|--------|
| Agency identity | Name and identifying information on diagrams | AG — Pending |
| Marking | “For Official Use Only” | AG — Pending |
| Revision | Date last revised | AG — Pending |
| Terminals | CJIS terminal count and connections | AG — Pending |
| Infrastructure | On-prem CJIS servers, firewalls, switches (per-device appendix fields) | AG — Pending |
| External / crypto | FIPS numbers / encryption outside secure agency network | JT — Pending |
| Cloud | Cloud CJIS components vs controlled interfaces | TL draft in Vol 03 — Pending export |

Per-device appendix fields: physical location, make/model, OS/firmware, last update date, EoS/EoL.

### Security Addendum

| Requirement | Status |
|-------------|--------|
| All **eight pages** (Texas version) | JT — Partial (Slaton evidence in `evidence/`) |
| Page 7 — employee detail | TL pages drafted |
| Page 8 — Texas signatory | AG — Pending per agency |
| Per-employee FBI certification | TL personnel signed; AG retains |

### Questionnaires

| Item | Status |
|------|--------|
| TLETS Interface Questionnaire | Vol 04 — **Fill guide drafted** ([`application/`](./application/)); Word form answers pending decision lock |
| CJIS Security Office Interface Approval Questionnaire | Vol 04 — In progress |

### SIEM (SI-4)

| Item | Status |
|------|--------|
| Tool identified | TBD |
| Weekly agency review documented | AG — Pending |
| Sample consolidated report | TL/AG — Pending |

---

## Deprioritized for critical path (unless CPSO directs)

Texas **V5.9.5 on-prem/cloud portal assessment** remains useful internal reference — see [`Docs/CJIS/reference/`](../CJIS/reference/) — but Kimberly’s Feb 2026 email centers **agency vetting + attestation**, not vendor-completed audit portal submission as the primary gate.
