# Configuration discovery workbook

**Audience:** Customer project team · Thin Line implementation  
**Purpose:** Collect and approve the customer-specific decisions needed to configure Thin Line products.  

This workbook **replaces the configuration portions** of older all-in-one onboarding questionnaires. It is modular: complete only the sections for products and options you purchased. Mark other sections **Not applicable**.

---

## How to use this workbook

1. Thin Line proposes **recommended defaults**. Change a default only when you have an operational reason.  
2. If legacy data is migrated, **prefer importing valid existing values** over typing lists by hand.  
3. Do **not** try to list every code or option here. Capture **exceptions** and intentional choices.  
4. Separate **facts** (agency name, ORI, addresses) from **policy decisions** (who may approve, what must be validated).  
5. Note when a choice needs **executive, CJIS, records, court, jail**, or other specialized approval.  
6. Flag items that affect **integrations, migration, reporting, or training**.  
7. Finish with **customer configuration approval** before treating configuration as ready for training / go-live.  

### Status values (for rows below)

| Status | Meaning |
|--------|---------|
| Not started | Not discussed |
| Proposed | Thin Line recommendation; awaiting customer decision |
| Decided | Customer decision recorded |
| Deferred | Explicitly postponed with owner |
| N/A | Not in scope |

### Standard decision columns

Each configuration table uses:

| Column | Meaning |
|--------|---------|
| **Configuration item** | What is being set |
| **Recommended default** | Thin Line starting point |
| **Customer decision** | What the agency chooses (or “Use default”) |
| **Source or rationale** | Why—operational need, legacy import, statute, preference |
| **Decision owner** | Named person (and approval type if specialized) |
| **Status** | From the list above |
| **Verified in system** | ☐ when confirmed in the configured environment |
| **Notes** | Impacts (migration / integration / reporting / training), constraints |

---

## Change control

Configuration can change after this workbook is approved. Later changes are normal—but they may affect **timeline, testing, training materials, or go-live readiness**. Material changes should be recorded as new decisions (who approved, when) rather than silent edits.

---

## Products in scope for this engagement

Check only what applies. Leave other product sections marked N/A.

- [ ] RMS  
- [ ] CAD  
- [ ] Mobile citations  
- [ ] Evidence / property  
- [ ] Jail  
- [ ] Court  
- [ ] Code enforcement  
- [ ] Other: _______________  

**Engagement name / agency:** _______________  
**Thin Line implementation lead:** _______________  
**Customer project lead:** _______________  

---

## 1. Organization and agency identity

**Facts** (confirm accuracy) and **decisions** (how the agency appears and is typed in the system).

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Agency display name | As provided at kickoff | | | | | ☐ | |
| Agency abbreviation / short name | Derived from display name | | | | | ☐ | |
| Agency type (e.g. law enforcement) | Per purchase / kickoff | | | | | ☐ | May affect available settings |
| Physical address | Customer-provided | | | | | ☐ | Defaults report header unless overridden |
| Mailing address (if different) | Same as physical | | | | | ☐ | |
| State | Per agency location | | | | | ☐ | |
| County | Per agency location | | | | | ☐ | |
| Agency latitude / longitude | Optional; set if maps/location features used | | | | | ☐ | |
| Agency theme / branding colors | Thin Line standard palette | | | | | ☐ | Cosmetic; training screenshots |
| Agency logo / image | None until customer provides file | | | | | ☐ | File required |
| Agency seal / signature images | None until provided | | | | | ☐ | Often court/CE documents |

**Specialized approval if needed:** Executive (official name), CJIS (if identity rules interact with compliance policy).

---

## 2. Report headers and contact information

How your agency appears on **reports** and **formal documents**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Report agency name (line 1) | Agency display name | | | | | ☐ | Reporting |
| Report agency name (line 2) | Blank | | | | | ☐ | |
| Report address lines | Customer-provided mailing/physical | | | | | ☐ | |
| Report city / state / ZIP | Customer-provided | | | | | ☐ | |
| Report phone / fax / email | Customer-provided | | | | | ☐ | |
| Document / letterhead agency name | Same as report unless told otherwise | | | | | ☐ | |
| Document physical address | Customer-provided | | | | | ☐ | |
| Document mailing address | Same as physical unless different | | | | | ☐ | |
| Document phone / fax / email / website | Customer-provided | | | | | ☐ | |
| City designation (documents) | Per customer practice | | | | | ☐ | |

**Specialized approval:** Records / admin for public-facing contact info.

---

## 3. Agency relationships and record sharing

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Multi-agency / shared records needed? | No (single agency) | | | | | ☐ | Integration / training |
| Agencies that may read our records | None | | | | | ☐ | CJIS / executive as required |
| Agencies that may write / contribute | None | | | | | ☐ | |
| Default court facility (if LE) | Set when court relationship known | | | | | ☐ | Citations / court |
| Related court or LE partners (names) | List partners; configure later | | | | | ☐ | |

Mark section **N/A** if you are a standalone agency with no sharing.

---

## 4. Users, roles, supervisors, and approvers

Separate **project contacts** from **application users**. Capture policy for access and approval—not every password.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Who may create user accounts | Thin Line + designated agency admin | | | | | ☐ | Security |
| Role model (officer / clerk / supervisor / admin, etc.) | Thin Line standard roles | | | | | ☐ | Training |
| Report approvers / review chain | Per agency rank practice | | | | | ☐ | Records / command |
| Who may approve NIBRS / IBRS submissions | Designated supervisor or records | | | | | ☐ | Reporting |
| Initial go-live user cohort | Named list attached (roster) | | | | | ☐ | Training |
| Officers / personnel records approach | Create for go-live cohort; expand later | | | | | ☐ | Migration may import |

**Attach:** Roster of initial users by role (separate file). Do not paste large directories into this workbook.

**Specialized approval:** CJIS / security contact for access policy; command for approval chains.

---

## 5. Numbering and identifiers

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| ORI (if law enforcement) | Customer-provided ORI | | | | | ☐ | Migration / reporting |
| Incident / case number pattern | Thin Line proposes pattern + sample | | | | | ☐ | Prefer legacy if migrating |
| Citation number — paper / manual | Thin Line / state practice | | | | | ☐ | Distinct from mobile if both used |
| Citation number — mobile | Same as paper unless court requires otherwise | | | | | ☐ | Mobile citations |
| Citation number — non-printed (if used) | Thin Line standard or N/A | | | | | ☐ | Often N/A |
| Warrant number pattern | Thin Line standard; “judge-assigned” OK | | | | | ☐ | |
| Close patrols number pattern | Thin Line standard or N/A | | | | | ☐ | Only if module purchased |
| Call / CAD number pattern | Thin Line standard | | | | | ☐ | CAD |
| Code enforcement number pattern | Thin Line standard or N/A | | | | | ☐ | CE |
| Lost and found number pattern | Thin Line standard or N/A | | | | | ☐ | |
| Field contacts number pattern | Thin Line standard or N/A | | | | | ☐ | If licensed |
| Notes / notepad number pattern | Thin Line standard or N/A | | | | | ☐ | If licensed |
| Evidence / property number pattern | Thin Line standard | | | | | ☐ | Evidence |
| Starting “next numbers” | Continue from legacy if migrating; else start fresh | | | | | ☐ | Migration |

**Rule of thumb:** Complete rows only for modules in purchase. Thin Line shows a **sample number** (not raw tokens like `YY-XXXX`); confirm it “looks like ours.” If history is migrating, align patterns with imported numbers unless you intentionally renumber.

---

## 6. RMS configuration

*Complete only if RMS is purchased.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Incident / offense modules enabled | Per purchase | | | | | ☐ | |
| Field contact / notepad (as licensed) | Per purchase | | | | | ☐ | |
| Report approval required before finalize | On (recommended) | | | | | ☐ | Training |
| NIBRS / State IBRS versions & start date | Per state / go-live plan | | | | | ☐ | Reporting; specialized |
| Validate IBRS on submit | **On** (recommended) | | | | | ☐ | Discuss officer workload |
| Validate IBRS on approve | **On** (recommended) | | | | | ☐ | Discuss approver workload |
| Warrant / trespass / other RMS modules | Per purchase | | | | | ☐ | Exceptions only |

**Exceptions / must-change from defaults**

-

---

## 7. CAD configuration

*Complete only if CAD is purchased.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| CAD / call module enabled | Per purchase | | | | | ☐ | |
| Dispatch agencies linked | This agency only | | | | | ☐ | Multi-agency CAD |
| Call types approach | Thin Line defaults + import/adjust exceptions | | | | | ☐ | Prefer import if migrating |
| Self-dispatch vs full CAD posture | Per purchase / kickoff | | | | | ☐ | Training |
| CAD partner webhooks / integrations | Off until integration phase | | | | | ☐ | Integrations |

**Call types and statuses:** Do not list every code here. Decide approach (defaults / import / customize) and attach exception lists if needed.

---

## 8. Mobile citation configuration

*Complete only if mobile / electronic citations are in scope.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Mobile citations enabled | Per purchase | | | | | ☐ | Hardware |
| Paper / handwritten citations until mobile ready | Allowed; plan training for both if needed | | | | | ☐ | Go-live constraint |
| Default court for citations | Named court facility | | | | | ☐ | Court |
| Municipal court — judge, address, hours/text | Customer-provided | | | | | ☐ | Printed on citation |
| JP court — judge, address, hours/text | Same as municipal if identical; else separate | | | | | ☐ | Avoid duplicate entry |
| Appearance day / time rules | Thin Line / court practice | | | | | ☐ | Court approval |
| Violator statement text | Thin Line / state standard text | | | | | ☐ | Legal/policy review if changed |
| Online payment for violations | Off until payments configured | | | | | ☐ | Integrations |
| QR code on mobile citation | Off unless online payment on | | | | | ☐ | |

---

## 9. Evidence and property configuration

*Complete only if Evidence is purchased.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Evidence module enabled | Per purchase | | | | | ☐ | |
| Property room / storage locations | Customer list (start small) | | | | | ☐ | Prefer import if migrating |
| Custody / checkout practices | Thin Line standard workflow | | | | | ☐ | Training |
| Label / barcode printing | Per hardware plan | | | | | ☐ | Hardware / integrations |

---

## 10. Jail configuration

*Complete only if Jail is purchased.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Jail intake module enabled | Per purchase | | | | | ☐ | |
| Booking number pattern | Thin Line standard or legacy | | | | | ☐ | Migration |
| Manual add / delete permissions | Per Thin Line security defaults | | | | | ☐ | Jail / security approval |
| Housing / status practices | Thin Line standard + exceptions | | | | | ☐ | Jail lead |
| Medical / classification notes approach | Per product capability & agency policy | | | | | ☐ | Specialized approval |

---

## 11. Court configuration

*Complete only if Court is purchased.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Court violation / court modules enabled | Per purchase | | | | | ☐ | |
| OCA / DPS identifiers (if used) | Customer-provided | | | | | ☐ | Reporting |
| Program default due-date days | Thin Line defaults for programs you use | | | | | ☐ | Court lead |
| In-person / online payment posture | Off until payment setup complete | | | | | ☐ | Integrations |
| Collections / third-party referral | Off unless purchased & configured | | | | | ☐ | |
| Citation import warning behavior | Thin Line defaults | | | | | ☐ | |
| VPTA / filing options (if used) | Per court practice | | | | | ☐ | Court approval |

---

## 12. Code enforcement configuration

*Complete only if Code Enforcement is purchased.* Otherwise **N/A**.

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Code enforcement module enabled | Per purchase | | | | | ☐ | |
| Letterhead / CE image | Customer-provided | | | | | ☐ | |
| Ordinances / violation approach | Import or attach list; not full codebook in this sheet | | | | | ☐ | CE lead |
| Mobile CE (if licensed) | Per purchase | | | | | ☐ | Hardware |

---

## 13. Notifications and communications

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Dashboard / task notifications | Thin Line defaults for enabled modules | | | | | ☐ | Training |
| Email for complaints / compliments (if used) | Customer-provided address | | | | | ☐ | |
| Other outbound email needs | Per kickoff | | | | | ☐ | Integrations |

List **notification exceptions** only (turn off noise, add critical alerts)—not every toggle.

---

## 14. Security and access

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Authentication approach | Thin Line standard for your deployment | | | | | ☐ | IT / CJIS |
| Who may grant elevated access | Named agency admins | | | | | ☐ | Executive / CJIS |
| CJIS compliance contact | Named | | | | | ☐ | |
| Session / access expectations for users | Per Thin Line + agency policy | | | | | ☐ | Training |

Do not record passwords or secrets in this workbook.

---

## 15. Reference codes and lookup values

**Do not paste full code tables here.**

| Configuration item | Recommended default | Customer decision | Source or rationale | Decision owner | Status | Verified in system | Notes |
|--------------------|---------------------|-------------------|---------------------|----------------|--------|--------------------|-------|
| Overall codes approach | Use Thin Line defaults; import legacy where valid; customize exceptions | | | | | ☐ | Migration |
| Call types (CAD) | Defaults + import/exceptions | | | | | ☐ | |
| Offense / charge lists | Import or state source as applicable | | | | | ☐ | Reporting |
| Property / evidence types | Defaults + exceptions | | | | | ☐ | |
| Other critical lookups | Named lists attached separately | | | | | ☐ | |

**Attached exception / import files** (names only)

| File / list name | Module | Owner | Status |
|------------------|--------|-------|--------|
| | | | |

---

## 16. Configuration decisions and approvals

### Impact checklist

Call out decisions that need extra care:

| Decision (short name) | Affects migration | Affects integrations | Affects reporting | Affects training | Specialized approver |
|-----------------------|:-----------------:|:--------------------:|:-----------------:|:----------------:|----------------------|
| | ☐ | ☐ | ☐ | ☐ | |
| | ☐ | ☐ | ☐ | ☐ | |

### Customer configuration approval

By approving, the named authority confirms that:

- Decisions recorded above (and attachments) are the intended configuration for go-live scope  
- Deferred items are listed with owners and are accepted as not blocking the next phase—or are explicitly blocking with agreement  
- Thin Line may configure the system accordingly  

| Field | Value |
|-------|--------|
| Agency | |
| Approval date | |
| Approved by (name / title) | |
| Role *(final acceptance / records / executive / other)* | |
| Thin Line implementation lead acknowledgment | |

**Deferred items still open**

| Item | Owner | Target date | Blocks training or go-live? |
|------|-------|-------------|------------------------------|
| | | | Yes / No |

### Signature / acknowledgment

Customer approval: _______________________________ Date: ________  

Thin Line acknowledgment: _________________________ Date: ________  

---

## Related

- [Customer implementation workbook](customer-implementation-workbook.md) — when to collect what  
- [Getting started](../getting-started/README.md) · [Training](../training/README.md)  

*Thin Line Software · Configuration discovery workbook · Customer-facing · Reusable*
