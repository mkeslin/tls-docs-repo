# TLETS Interface Questionnaire — answers (pick a version)

**Form:** Texas DPS / Crime Information Bureau — TLETS Operations  
**Last revised:** 2026-07-20  
**Status:** <mark style="color:red;">Internal draft — choose one option per question; paste into Word</mark>

### Download the Word form

- **[TLETS Interface Questionnaire (.docx)](forms/tlets-interface-questionnaire.docx)** — working copy in this docs repo  
- Also listed under [Word forms](forms/README.md)  
- OneDrive original: `Reference Documents\TLETS\TLETS Interface Questionnaire.docx`

For each question, pick **one** answer version. Do not mix conflicting options across questions (e.g. Full Access + “inquiry only” purpose language).

**Placeholders:** `[Agency]` · `[ORI]` · `[N]` (device/user count) · `[Agency list + ORIs]`

**Related:** [Open decisions](open-decisions.md) · [Interface Approval Packet answers](interface-approval-packet.md) · [Scope](direct-interface-scope.md) · [TLETS application home](README.md)

---

## Q1 — What type of devices will use the new interface?

**Question (paraphrase):** RMS, CAD, JMS, Mobile Devices, or both?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended** | Browser/PWA on agency endpoints; RMS + CAD | Agency workstations and approved mobile devices accessing Thin Line RMS and CAD via browser or progressive web app (PWA), where agency policy allows. |
| **B — Modules named** | Same, but list products explicitly | Desktop computers, laptops, tablets, and mobile devices used to access Thin Line RMS, CAD, and (where licensed) JMS via browser/PWA. |
| **C — Workstations only** | Agency bans mobile/PWA for CJI | Agency desktop and laptop workstations accessing Thin Line RMS/CAD via browser over HTTPS. Mobile devices are not authorized for this interface. |
| **D — Include MDT/MDC** | Patrol MDTs will query | Agency workstations, MDTs/MDCs, laptops, tablets, and (if authorized) smartphones accessing Thin Line RMS/CAD via browser/PWA. |

---

## Q2 — Who is your interface vendor?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Only** | Always | Thin Line Software LLC |

---

## Q3 — Test connection needed, or already tested in TEST?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended** | New interface; no successful DPS TEST yet | Test connection needed. |
| **B — Already tested** | Only after documented successful TEST transactions | Vendor has already successfully tested transactions in the DPS TEST system. (Attach/reference TEST proof if available.) |

---

## Q4 — Message format: DAC vs XDAC (OFML)?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended (pending confirm)** | Expected path; TLETS Ops not yet confirmed | XML for Open Fox Message Language OFML (XDAC). Pending final confirmation with TLETS Operations. |
| **B — XDAC confirmed** | TLETS Ops / engineering locked OFML | XML for Open Fox Message Language OFML (XDAC). |
| **C — DAC (period-delimited)** | Only if DPS/engineering requires DAC | Period-delimited TEXT data streams (DAC). |
| **D — TBD with DPS** | Do not want to lock format yet | Message format to be confirmed with TLETS Operations during TEST connection setup (XDAC/OFML preferred). |

---

## Q5 — TCIC/NCIC access level?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended first ask** | Start with lowest bar | TCIC Inquiry only (YNN without CCH). |
| **B — Less than full with CCH** | Need CCH but not full update rights | TCIC Less Than Full Access (YNY with CCH). |
| **C — Full access** | Agency CSO requires Full / YYY | TCIC Full Access (YYY with CCH). |
| **D — Inquiry first, expand later** | Explicit phased ask | TCIC Inquiry only (YNN without CCH) for initial approval; Full Access to be requested in a later amendment if required. |

---

## Q6 — How many devices behind the new interface?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended** | Single agency; known count | `[N]` devices for `[Agency]` (authorized Thin Line RMS/CAD query users / endpoints). |
| **B — Count + growth** | Known now + planned | `[N]` devices currently; up to `[N2]` planned within 12 months for `[Agency]`. |
| **C — Avoid** | Do not use on first submit | ~~Variable 10–100 depending on deployment~~ |

Replace `[N]` with a real number before sending.

---

## Q7 — Will any devices be used by a federal agency? If yes, how many?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended** | No federal users on this path | No. |
| **B — Federal present** | Federal partner will query through this interface | Yes. `[N_fed]` devices used by `[Federal agency name]`. |

---

## Q8 — Will the new interface run traffic for other agencies? If yes, list names and ORIs.

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended (single ORI)** | First submission / safer hosting posture | No. This interface serves `[Agency]` ORI `[ORI]` only. |
| **B — Multi-agency host** | DPS-aware multi-ORI Thin Line host model | Yes. The interface will support multiple law enforcement agencies using their respective ORIs: `[Agency list + ORIs]`. |
| **C — Pilot then expand** | Honest phased commercial plan | No for this submission — `[Agency]` ORI `[ORI]` only. Additional agencies/ORIs will be requested in separate submissions or an approved hosting amendment. |

---

## Q9 — If agency has other TLETS interfaces, will this use the same server? If yes, existing IP?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended** | New Thin Line path; not reusing agency TLETS server IP | No. This will be a new Thin Line interface path (not using an existing agency TLETS interface server IP). |
| **B — Azure connector named** | Topology known in Azure Gov | No. Traffic terminates on a Thin Line–operated interface connector in Microsoft Azure Government (resource details in architecture diagram), not on an existing on-prem agency interface server IP. |
| **C — Agency-hosted connector** | Connector VM/appliance on agency network | No shared reuse of another product’s interface IP. The Thin Line interface connector will be located at `[agency site / IP or hostname per diagram]`. |
| **D — Reuses existing** | Rare — only if truly same host | Yes. Existing interface server IP: `[IP]`. |

---

## Q10 — Is the new interface capable of receiving DL images?

| Option | When to use | Paste this |
|--------|-------------|------------|
| **A — Recommended (v1)** | DL images not in first release | No. |
| **B — Yes** | Product will receive/display DL images on this path | Yes. |
| **C — Later** | Capability planned but not claimed now | No for initial approval. DL image support may be requested in a later amendment when product capability is ready. |

---

## Suggested consistent bundles

Pick a **bundle** so answers do not contradict each other:

| Bundle | Q3 | Q5 | Q8 | Q10 | Notes |
|--------|----|----|----|-----|--------|
| **Safe first** | A | A | A | A | Best default for first DPS ask |
| **CCH needed** | A | B or C | A | A or C | Only if CSO requires CCH |
| **Multi-tenant host** | A | A or C | B | A or B | Harder approval; confirm with DPS first |
| **TEST already done** | B | (as locked) | (as locked) | (as locked) | Only with proof |

---

## Caution on the existing Word draft

The OneDrive `.docx` may already contain a **product-vision** mix (Full Access, multi-agency ORI, DL Yes, variable device counts). Replace with your chosen options above before submit.

---

## Related

- [Download Word form](forms/tlets-interface-questionnaire.docx)
- [All Word forms](forms/README.md)
- [Interface Approval Packet answers](interface-approval-packet.md)
- [Open decisions](open-decisions.md)
- [Direct-interface scope](direct-interface-scope.md)
- [TLETS application home](README.md)
