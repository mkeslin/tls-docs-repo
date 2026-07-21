# TLETS application (internal)

**Status:** Working draft — <mark style="color:red;">**internal only until nailed down**</mark>  
**Last revised:** 2026-07-20

Playbook for Thin Line staff applying to run **NCIC / TLETS queries from within Thin Line RMS/CAD**, with Thin Line Software LLC as the **interface vendor**.

---

## Start here

| Document | Purpose |
|----------|---------|
| [Word forms (download)](forms/README.md) | DPS `.docx` working copies |
| [Interface Questionnaire answers](interface-questionnaire.md) | **Pickable answer versions** for the TLETS Interface Questionnaire |
| [Interface Approval Packet answers](interface-approval-packet.md) | **Pickable answer versions** for the CJIS Security Office Interface Approval Packet |
| [Agency remote access policy template](agency-remote-access-policy-template.md) | Use when the agency needs a complete policy |
| [Thin Line remote access addendum](thin-line-remote-access-addendum-template.md) | Use when the agency already has a policy and needs Thin Line-specific language |
| [Agency network diagram template](agency-network-diagram-template.md) | Use when the agency needs a complete proposed CJIS/TLETS diagram |
| [Thin Line network diagram insert](thin-line-network-diagram-insert.md) | Use when the agency already has a diagram and needs the Thin Line/Azure portion |
| [Agency boundary equipment worksheet](agency-boundary-equipment-worksheet.md) | Inventory make/model, installed and latest versions, updates, support dates, and diagram IDs |
| [Direct-interface scope](direct-interface-scope.md) | Working scope statement for the packet |
| [Open decisions](open-decisions.md) | Blockers before locking Word-form answers |
| [Agency guide (planned)](agency-guide-planned.md) | Future **customer** section — not published yet |

### Word form downloads

- [TLETS Interface Questionnaire (.docx)](forms/tlets-interface-questionnaire.docx)
- [CJIS Security Office Interface Approval Packet (.docx)](forms/cjis-security-office-interface-approval-packet.docx)
- [Agency remote access policy (.docx)](forms/agency-remote-access-policy-template.docx)
- [Thin Line remote access addendum (.docx)](forms/thin-line-remote-access-addendum-template.docx)
- [Agency boundary equipment worksheet (.csv)](forms/agency-boundary-equipment-worksheet.csv)

**Monorepo packet sources (PDF export, evidence, agencies):**  
`ThinLineSoftware` → `Docs/TLETS/` (phase-1, attestation-kit, application, evidence, agencies)

---

## Application checklist (Thin Line)

### Decisions before filling forms

- [ ] Sponsoring **agency + ORI** for this submission copy (one agency per form unless DPS confirms multi-ORI host)
- [ ] **Access level:** Inquiry only (YNN without CCH) vs Full Access (YYY with CCH)
- [ ] **Message format:** XDAC / OFML vs DAC — confirm with TLETS Ops / engineering
- [ ] **Connector topology:** where the interface terminates (agency network vs Azure Gov) and path to DPS
- [ ] **Device count** for *this* agency (not a multi-tenant range)
- [ ] **DL images** in v1 scope? (Yes/No)
- [ ] **Test connection** needed vs already proven in DPS TEST

### Packet pieces

- [ ] Complete **TLETS Interface Questionnaire** ([fill guide](interface-questionnaire.md))
- [ ] Complete / coordinate **CJIS Security Office Interface Approval Questionnaire**
- [ ] Architecture diagrams showing **TLETS query path** (UI → Thin Line interface → DPS); use the [complete agency template](agency-network-diagram-template.md) or [Thin Line insert](thin-line-network-diagram-insert.md)
- [ ] Direct-interface scope ([direct-interface-scope.md](direct-interface-scope.md)) — CPSO pass before export
- [ ] Agency attestation / addendum / fingerprint evidence
- [ ] Agency network diagram update: Thin Line query UI + interface connector + ORI

### Engineering honesty (2026-07)

| Item | Status |
|------|--------|
| Monorepo `LetsQuery` module | RMS **recordkeeping** — **not** a TLETS wire client |
| XDAC / OFML / DMPP connector | <mark style="color:red;">**Not implemented**</mark> in ThinLineSoftware as of this writing |
| In-app Help CJIS copy | Update when product ships queries |

---

## Contacts

| Role | Person |
|------|--------|
| Facilitates approval process | Matthew Keslin |
| Primary CPSO / package follow-up | Eric Gibson |

---

## Related

- [Compliance home](../README.md)
- [Integrations and hardware SOP](../../sops/deliver/integrations-and-hardware.md)
- [Agency guide (planned — customer)](agency-guide-planned.md)
