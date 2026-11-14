# Vendor Q&A — round 2 (paused after Q20)

> Moved from TLS-App `Docs/TLETS/correspondence/vendor-qna-round2-partial.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

Captured from coordinator responses. **⚠ CPSO wording** remains subject to review.

---

## Q10–11 — SIEM / Sentinel / weekly review

**Answers (vendor)**

- Thin Line operates **Microsoft Sentinel** in Azure (SIEM).
- Respondent was unsure what the questionnaire asked for—it is mainly: **evidence someone reviews security signals on a weekly cadence** (often aligned to **SI-4** style expectations in CJIS discussions).

**What to attach for assessors (concrete examples)**

- A **Sentinel** **saved workbook** or **Analytics rule** → **weekly** run + **export** (PDF/CSV) or screenshot with **date range** and **reviewer initials** in your process doc; or  
- **Scheduled report** / **incident queue** triage log showing **weekly** management review of alerts.

Cross-link: **`Docs/TLETS/agencies/slaton-pd/azure-inventory.md`** §Q6 (“partner endpoints” table)—pair Sentinel coverage with egress integration inventory.

---

## Q12 — Partner endpoints / integrations log *(starter table — OPS complete)*

CPSOs often want **hostname → purpose → who logs → who reviews → how often**.

| Destination (endpoint / service) | Purpose (Slaton / prod RMS) | Log/diagnostic sink (e.g., Sentinel LAW, Firewall, Asc) | Evidence owner |
|----------------------------------|-----------------------------|----------------------------------------------------------|----------------|
| **Descope** (`static.descope.com`, etc.) | Agency user auth / MFA flows | ⚠ OPS | OPS |
| **Stripe** (`api.stripe.com`) | Payments (if jurisdiction uses) | ⚠ OPS | OPS |
| **Azure AI Language** `tls-ai-language-service.cognitiveservices.azure.us` | Incident narrative synopsis | ⚠ OPS | OPS |
| **Azure OpenAI** (if enabled for chat / other) | Thin Line assistant / other | ⚠ OPS | OPS |
| **Custom API / UI** `slatontx-api.thinline.app`, `slatontx.thinline.app` | Primary RMS traffic | App Service logs / Sentinel | OPS |
| **SQL** `tls-db2.database.usgovcloudapi.net` | Data plane | SQL Auditing / Defender | OPS |
| **Third-party webhooks** (CAD, etc., if any for Slaton) | Outbound/inbound | ⚠ enumerate per tenant | OPS |

---

## Q13 — Security program / CJIS mapping document

**Answer (vendor):** CJIS requirement mapping already exists **in-product** under **Help → Compliance → CJIS** (Vue implementation under [`ThinLine.UI/src/components/help/HelpComplianceCjis.vue`](../../../ThinLine.UI/src/components/help/HelpComplianceCjis.vue) and related `HelpComplianceCjisTabPolicyArea*.vue`).

**⚠ Thin Line OPS / legal:** Assessors typically want a **standalone, version-controlled PDF/word annex** exported or compiled from this content (update for **direct TLETS interface** posture). Schedule a content review vs **current CJIS Security Policy**.

---

## Q14 — TXRAMP / FedRAMP posture

**Answer (vendor):** **TXRAMP process started—not complete.** Attach **milestones / DIR portal status** when available. **FedRAMP:** ⚠ clarify org-wide (often **non-listing SaaS posture**)—do not imply certification unless DIR/FedRAMP package exists.

---

## Q15 — Microsoft Azure Gov enrollment artifact

**Answer (vendor):** Customer model is **Microsoft pay-as-you-go** (consumption/subscription semantics).

**Packet note:** If CPSO requests **Enrollment / MCA** PDFs from **MCA portal**, OPS pulls sanitized copies from **thinlinesoftware** EA/MCA—not the same wording as CSP partner agreements.

---

## Q16–17 — Personnel (CJIS addendum / FBICJIS‑style roster)

**Roster update (Thin Line CJIS-scope staff — per vendor)**

| Name | Status |
|------|--------|
| Matthew | ⚠ CPSO wording |
| Eric Gibson | ⚠ CPSO wording |
| **Eric Fugate** | **Added** |

**Fingerprints / Security Awareness certificates:** **Collected** — vendor will upload to **`evidence/`** (redacted copies for git if needed; originals per records policy).

---

## Q18–19 — Authentication / MFA

**Answers (vendor)**

- **Agency RMS users:** **Descope-managed** identities (agency-facing login path).
- **Thin Line corporate employees:** **Microsoft SSO** (separate workforce IdP)—not interchangeable with Slaton officer login UX without explicit federation design.
- **MFA:** Enforced/administered through **Descope** for identities that authenticate via Descope to RMS.

**⚠ CPSO clarification:** Separate **agency** SSO story vs **TLS staff** SSO in attachments so assessors don’t confuse “who touches CHRI.”

---

## Q20 — Break-glass / recovery access / bypass accounts

**Repo / architecture note (Thin Line RMS)**

- RMS API authorization supports a **`ThinLineSupportClaim`** **JWT claim** for **Thin Line support** scenarios (multiple controllers gate `ClaimKeys.ThinLineSupportClaim`). That is **not** a second password inside SQL—it is still **token-based** identity (typically issued only to **support** principals your org provisions in **Descope / directory**).
- There is **no separate “RMS local admin password”** documented in code as a standard production break-glass for Slaton; **operational** break-glass is an **org process** question: **Descope lockout procedures**, **Azure AD B2B emergency access** (if any), **customer approval** for support sessions.

**OPS action:** Document **who** can hold support-capable tokens, **time-bound** access, **customer notification**, and **audit log** review—CPSO cares about **accountability**, not stack trivia.

**Pause here** — Q21+ remain for a later round.

_Continuation:_ [`vendor-qna-round3-partial.md`](./vendor-qna-round3-partial.md)

