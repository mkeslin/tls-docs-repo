# Direct TLETS / NCIC interface scope (working draft)

**Audience:** Internal / packet draft  
**Last revised:** 2026-07-20  
**Status:** <mark style="color:red;">**CPSO / TLETS Ops review required**</mark> before export to agency or DPS

---

## Purpose

Thin Line Software LLC is applying for DPS / TLETS approval so authorized agency users can run **TCIC / NCIC (TLETS) queries from within Thin Line RMS/CAD**, with Thin Line as the **interface vendor**.

---

## What this proposes

- In-application query UI in Thin Line RMS and/or CAD for authorized users
- A Thin Line–operated interface path that formats and exchanges TLETS traffic (message format per questionnaire — typically **XDAC / OFML** pending DPS confirmation)
- Queries attributed to the **sponsoring agency’s ORI** (single-agency first submission unless DPS approves multi-ORI hosting)
- RMS/CAD hosted in **Microsoft Azure Government**; interface connector topology documented in architecture exhibits

---

## What this does not claim (until approved and built)

- That the current production release **already** completes NCIC/TLETS wire transactions end-to-end
- That Thin Line holds its **own** ORI or TLETS identifier (agency ORI remains authoritative unless DPS directs otherwise)
- **TCIC Full Access (YYY with CCH)** unless the agency CSO and DPS approve that level
- **Multi-agency ORI traffic** on one interface unless the hosting model is explicitly approved

---

## Shared responsibility (summary)

| Area | Thin Line | Agency |
|------|-----------|--------|
| RMS/CAD and Thin Line–managed Azure Gov resources | ✓ | |
| TLETS interface software / connector Thin Line operates (when approved) | ✓ | |
| ORI / TLETS identifiers and CJIS inquiry authority | | ✓ |
| Authorized users, workstations, mobile policy | | ✓ |
| Agency network path / local controls on CJIS diagrams | Joint | ✓ |
| Fingerprint / AT for Thin Line personnel | Joint | ✓ (sponsoring LEA) |

---

## Product / engineering honesty

As of **2026-07-20**, monorepo **`LetsQuery`** supports RMS recordkeeping related to LETS workflows; it is **not** a complete TLETS wire-protocol client. Questionnaire answers and diagrams must track implementation reality and DPS TEST results.

---

## Related

- [Interface Questionnaire fill guide](interface-questionnaire.md)
- [Open decisions](open-decisions.md)
- Monorepo: `ThinLineSoftware` → `Docs/TLETS/application/DIRECT-INTERFACE-SCOPE.md`
