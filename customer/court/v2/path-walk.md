# Court V2 path walk

Customer-facing walk of the **current V2 demo ceiling** in demo order. For what Sales may claim in the room, see [Demoable now](demoable-now.md). For how this relates to V1 guides, see [V1 vs V2](v1-vs-v2.md).

This walk assumes an authenticated defendant on the **online portal** or a clerk on **Clerk Assist** for packet assembly, and a judge on the **staff** queue for outcomes. Packet types share one spine: submit captures defendant intent (and payment capture where Phase 1 paid types apply); **Approve / Reject / NeedsInfo** are **judge-only** (staff APIs — not defendant self-service).

## 1. Typed dispositions (Phase 1)

Defendant or clerk assist starts a **typed disposition packet** (for example pay in full, payment plan, compliance dismissal, plea, or court program — per agency configuration and the locked Phase 1 set).

- Dual channel: **portal** and **in-person tablet / Clerk Assist** on the same backend.
- **One active packet** at a time for the spine rules in effect on your build.
- Paid Phase 1 types: capture at submit; refund on reject — per locked Phase 1 money rules. Do not reopen compliance-dismissal hard-cut or rule-pack pitch in customer conversations.

## 2. Issuance PC cite (Phase 2)

On the law-enforcement / issuance side, the citation carries **issuance quality**: oath record, catalog-driven PC narrative, and **court-record attachments** on the violation (PDFs and similar — not a print-queue product story).

Issuing officer corrections use **addendum-only** behavior; clerks and judges **read** the package later in court flow.

At the [current demo ceiling](demoable-now.md), **Issuance PC cite** is on pitch together with **clerk ↔ tablet** counter flow.

## 2b. Clerk ↔ tablet handshake

For in-person counter work, clerk pairs a tablet through **`/public/counter-device`** until the UI shows **Tablet connected**, then continues packet assist on the shared V2 spine (same types as portal Clerk Assist).

**ON pitch** at tip `64c4bd40a0` (parent `b8a7ffcd48`) — Matthew Soft OK two-browser verify. See [Demoable now](demoable-now.md) for the full ceiling.

## 3. Package read

Clerk or judge opens the **PC package** for read/review before relying on it in downstream judicial steps (including warrant work). This is a read surface — not a new procedural state named “pending judge” on the case.

## 4. FTA and CPF warrants (Phase 3)

On the **staff** side, ordered judge-only paths for **FTA** and **CPF** warrant work. The portal does **not** issue warrants and does not bypass notice or rule-of-hearing gates by itself.

## 5. Portal read and acknowledge (Phase 3.3)

On the **limited defendant portal**, for eligible FTA and CPF surfaces:

- Defendant **reads** notice or show-cause content (and linked attachments when present).
- Defendant **acknowledges receipt** with a durable timestamp.
- **No upload** of response documents on this slice.

Acknowledgment does not by itself pass gates, issue warrants, or unlock CPF without the ordered staff path.

## 6. Hardship / ability-to-pay (Phase 4.1)

Defendant or clerk assist drafts a **hardship** packet.

| Step | Behavior |
|------|----------|
| Draft | Narrative and proposed terms as implemented on your build. |
| Submit | **At least one evidence upload is required** — submit without evidence fails closed. |
| Pending judge | Packet awaits staff review (submitted / pending judge alias). |
| Approve | Judge applies approved terms via the packet spine (no auto-grant on submit). |
| Reject / NeedsInfo | Staff-only; reject does not apply approved terms; needs info allows more evidence and resubmit without treating submit as approve. |

**Payment plan combined** host is in scope Soft OK. **Pay in full combined** is a documented gap Soft OK — do not pitch as shipped.

Staff surfaces follow the same dual-channel pattern as other Phase 4 packets (portal + clerk assist + judge queue).

## 7. Extension (Phase 4.2)

Defendant or clerk assist drafts an **extension** packet.

| Topic | Locked behavior |
|-------|-----------------|
| Count cap | **None** — a second extension after an approved one is allowed; each still needs judge **Approve**. |
| Max length | Agency setting **`extension.maxDays`**, default **30** calendar days; over-max proposals fail closed. |
| Evidence | **Not required** on extension (unlike hardship). |
| Submit | Does **not** apply a new due date by itself. |
| Approve | Applies proposed due date through the packet spine when proposed; empty proposed delta is a documented no-op (no auto-grant). |
| Reject / NeedsInfo | Do not apply extension dates; needs info allows edit and resubmit. |

**Payment plan combined** Soft OK. **Extension + hardship** combined is a documented gap Soft OK.

## 8. Community service (Phase 4.3)

Defendant or clerk assist places **community service** in **draft**, then **submits** for judge review.

| Topic | Locked behavior |
|-------|-----------------|
| Clock / order start | Starts **only** on judge **Approve**, stamped with **`orderStartedAtUtc`** and **`orderStartedByUserId`**. |
| Reject | **Never** starts CS obligation. |
| NeedsInfo | Does **not** start the clock. |
| Submit | Does **not** start the clock (submit ≠ approve). |
| Proposed work | `proposedHours` / `proposedAmount` shape on your build (at least one required when present; validation as implemented). |
| Evidence | **Not required** on CS (unlike hardship). |
| Fee | No invented CS fee in this slice (`FeeAmount` null). |
| Completion hours | **Not** tracked in this slice — do not demo completion-hour ledgers. |
| Combined hosts | **Payment plan + CS** Soft OK. **Extension + CS** and **hardship + CS** are documented gaps Soft OK — do not pitch as shipped. |

### Where to open community service

| Role | Route (as implemented) |
|------|-------------------------|
| Defendant portal | `/portal/citations/:citationNumber/community-service` |
| Judge | `/module/court-violation/community-service` |
| Clerk assist | `/module/court-violation/community-service-clerk-assist` |

Judge **Approve**, **Reject**, and **NeedsInfo** are staff-only on the judge queue / panel for this packet type.

## End of current ceiling

Steps above match the **on-pitch** list in [Demoable now](demoable-now.md). Production **V1/V2 cutover** is **not** part of this walk — local dual-path remains Soft OK for demos only.
