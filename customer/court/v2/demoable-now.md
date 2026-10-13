# Demoable now (Court V2 ceiling)

Sales-facing boundary for what you may **pitch** on the Court V2 packet path. This reflects the **current V2 demo ceiling**, not a go-live or Phase 5 cutover promise.

**Ops note — demo tip ceiling:** **`6234e081ca`** — current **pushed tip** on branch `mkeslin/court-portal` (prior ceiling `64c4bd40a0`, parent `b8a7ffcd48`). **E2E is paused.** Demo unlock = **unit/API green + Court BA PASS** on that tip. Do **not** claim Playwright green as the demo gate while e2e is paused. **Playwright has not been re-run** on the full **tls-*** form-control migration at tip `6234e081ca`. Matthew **approved for demos** handshake **two-browser verify** on the prior ceiling; treat handshake and issuance as still on pitch unless Court BA moves them — see product pages under [Court V2](README.md) for court-portal behavior added since `64c4bd40a0`.

## ON pitch (V2 path)

You may demonstrate this ordered story on a local/dev build at the tip above:

| Slice | What to show |
|-------|----------------|
| **Phase 1 typed dispositions** | Defendant-initiated packet types on the shared spine (portal + clerk assist + judge queue). Compliance dismissal stays on the **locked Phase 1** packet model — do not reopen CD hard-cut or rule-pack pitch. |
| **Issuance PC cite** | Officer/clerk issuance quality: oath, PC narrative, catalog, court-record attachments on the citation/violation (not a separate print-out workflow). **On pitch** at the demo ceiling unless Court BA narrows it. |
| **Clerk ↔ tablet handshake** | **ON pitch** — counter pairing through `/public/counter-device` until **Tablet connected** (approved for demos — two-browser verify on prior ceiling). In-person packet assist alongside portal. |
| **Court-portal slice (docs)** | Tier-1 DSC/deferred gates, portal outcome cards, **Court V2 Online Portal** link, NEW intake DOB/speed, not-guilty paths, youth diversion, DSC **Ask for more time**, and related panels — documented in [Resolution workspace](resolution-workspace-and-controls.md), [Portal and online options](portal-and-online-options.md), and [Court programs and eligibility](court-programs-eligibility.md). **Not** full Texas statutory compliance — see [Compliance gaps](compliance-gaps.md). |
| **Package read** | Clerk/judge read of the PC package before downstream judicial work. |
| **FTA / CPF warrants** | Judge-only ordered warrant paths for FTA and CPF (not portal-issued warrants). |
| **Portal read + ack** | Limited defendant portal: read FTA notice and CPF show-cause; **timestamped acknowledge**; **no upload**. |
| **Hardship / ability-to-pay (ATP)** | Standalone hardship packet; **Payment Plan combined** approved for demos. Evidence **mandatory on Submit**. Judge **Approve / Reject / NeedsInfo** only. |
| **Extension** | Standalone extension packet; **no extension count cap**; agency max length default **30 days** (`extension.maxDays`); each extension still needs judge **Approve**. Payment Plan combined approved for demos. |
| **Community service (CS)** | Standalone CS: **Draft / Submit** OK; obligation clock and order start **only on judge Approve** (`orderStartedAtUtc` + `orderStartedByUserId`). **Reject** never starts CS. **NeedsInfo** does not start CS. No auto-grant. **Evidence not required** on CS. No invented CS fee. No completion-hour tracking in this slice. Payment Plan combined approved for demos. |

### Shared rules (all Phase 4-style packets)

- **One active packet** per case spine rules (creating a second active packet conflicts).
- **Judge-only** **Approve**, **Reject**, and **NeedsInfo** — defendants cannot self-approve on the portal public API.
- **Submit ≠ Approve** — submitting puts the packet in pending judge review; outcomes apply only on staff action.

### Documented gaps (known gap, not shipped — do not pitch as shipped)

| Combination | Status |
|-------------|--------|
| Extension + community service | Known gap, not shipped |
| Hardship + community service | Known gap, not shipped |
| Hardship + Pay in full combined | Pay in full combined optional — **known gap, not shipped** |
| Extension + hardship | Known gap, not shipped |

## OFF pitch (not live catalog on this tip)

- **OFF pitch — unconfirmed DPS / catalog maps:** Do **not** pitch `3205E`, `LP-1`, or **stash fee codes** / other **unconfirmed DPS fee maps** as live issuance catalog on the demo ceiling. The branch includes **`3667A` for plate-display only** — do not imply stash codes or unconfirmed fee maps are live.

## Not a product story

| Topic | Guidance |
|-------|----------|
| **Local dual-path V1 + V2** | Running V1 procedural court and V2 packet overlay side-by-side is **approved for demos** on local builds — **not** Phase 5 production cutover. Do not invent a customer feature flag, cutover date, or “every agency gets both paths in prod” claim. |

## Reviewers

- **Court BA** — product truth and locked defaults on this page.
- **Sales** — demoable-now boundaries and on/off pitch before customer-facing demos.
