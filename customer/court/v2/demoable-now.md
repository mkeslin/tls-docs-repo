# Demoable now (Court V2 ceiling)

Sales-facing boundary for what you may **pitch** on the Court V2 packet path. This reflects the **current V2 demo ceiling**, not a go-live or Phase 5 cutover promise.

**Ops note — demo tip ceiling:** `64c4bd40a0` (parent `b8a7ffcd48`; local unit green-up). **E2E is paused.** Demo unlock = **unit/API green + Court BA PASS** on that tip. Do **not** claim Playwright green as the demo gate while e2e is paused.

## ON pitch (V2 path)

You may demonstrate this ordered story on a local/dev build at the tip above:

| Slice | What to show |
|-------|----------------|
| **Phase 1 typed dispositions** | Defendant-initiated packet types on the shared spine (portal + clerk assist + judge queue). Compliance dismissal stays on the **locked Phase 1** packet model — do not reopen CD hard-cut or rule-pack pitch. |
| **Issuance PC cite** | Officer/clerk issuance quality: oath, PC narrative, catalog, court-record attachments on the citation/violation (not a separate print-out workflow). |
| **Package read** | Clerk/judge read of the PC package before downstream judicial work. |
| **FTA / CPF warrants** | Judge-only ordered warrant paths for FTA and CPF (not portal-issued warrants). |
| **Portal read + ack** | Limited defendant portal: read FTA notice and CPF show-cause; **timestamped acknowledge**; **no upload**. |
| **Hardship / ability-to-pay (ATP)** | Standalone hardship packet; **Payment Plan combined** Soft OK. Evidence **mandatory on Submit**. Judge **Approve / Reject / NeedsInfo** only. |
| **Extension** | Standalone extension packet; **no extension count cap**; agency max length default **30 days** (`extension.maxDays`); each extension still needs judge **Approve**. Payment Plan combined Soft OK. |
| **Community service (CS)** | Standalone CS: **Draft / Submit** OK; obligation clock and order start **only on judge Approve** (`orderStartedAtUtc` + `orderStartedByUserId`). **Reject** never starts CS. **NeedsInfo** does not start CS. No auto-grant. **Evidence not required** on CS. No invented CS fee. No completion-hour tracking in this slice. Payment Plan combined Soft OK. |

### Shared rules (all Phase 4-style packets)

- **One active packet** per case spine rules (creating a second active packet conflicts).
- **Judge-only** **Approve**, **Reject**, and **NeedsInfo** — defendants cannot self-approve on the portal public API.
- **Submit ≠ Approve** — submitting puts the packet in pending judge review; outcomes apply only on staff action.

### Documented gaps (Soft OK — do not pitch as shipped)

| Combination | Status |
|-------------|--------|
| Extension + community service | Not shipped — gap Soft OK |
| Hardship + community service | Not shipped — gap Soft OK |
| Hardship + Pay in full combined | Pay in full combined optional — **not shipped** (gap Soft OK) |
| Extension + hardship | Not shipped — gap Soft OK |

## OFF pitch (not demo-safe yet)

| Topic | Why |
|-------|-----|
| **Clerk ↔ tablet handshake** | Pairing flow through `/public/counter-device` until **Tablet connected** — needs Matthew **two-browser** verify. Do **not** call handshake pitch-safe. |

## Not a product story

| Topic | Guidance |
|-------|----------|
| **Local dual-path V1 + V2** | Running V1 procedural court and V2 packet overlay side-by-side is **local Soft OK** for demo walks — **not** Phase 5 production cutover. Do not invent a customer feature flag, cutover date, or “every agency gets both paths in prod” claim. |

## Reviewers

- **Court BA** — product truth and locked defaults on this page.
- **Sales** — demoable-now boundaries and on/off pitch before customer-facing demos.
