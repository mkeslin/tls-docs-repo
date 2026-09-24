# Court V1 vs Court V2 (demo walks)

Use this page when you need to explain **two parallel stories** in the same local environment: classic **Court Violations (V1)** guides vs the **V2 packet overlay**.

| | **Court V1** | **Court V2 (packet path)** |
|---|--------------|---------------------------|
| **Customer docs** | [Court guides](../README.md) — procedural states, queues, payments, programs, FTA, documents | [Court V2](README.md) — typed packets, issuance read path, limited portal ack, Phase 4 packets |
| **Primary mental model** | Case **procedural state** and clerk **actions** on the violation | **Packets** on a shared spine: defendant submit → judge **Approve / Reject / NeedsInfo** |
| **Defendant online** | V1 portal flows as documented in legacy court topics | Limited portal ack + Phase 1 and Phase 4 packet surfaces on the V2 spine |
| **Judge work** | Pleas, judgment, programs, warrants per V1 pages | Packet queue outcomes; warrant slices as in [Path walk](path-walk.md); CS clock **only on Approve** |
| **Issuance / PC** | Citations and court import per [RMS citations](../../rms/citations/README.md) | Phase 2 **issuance quality** + **package read** on the V2 walk |
| **Compliance dismissal** | V1 [court programs](../court-programs.md) and related flows | Phase 1 **ComplianceDismissal packet** on V2 — **locked**; do not reopen CD hard-cut or rule-pack changes in customer docs |
| **Production cutover** | Live product documentation today | **No** Phase 5 cutover date or customer feature-flag setting documented here |

## Local dual-path (Soft OK — not go-live)

On a **local** or **dev** build at the [current demo ceiling](demoable-now.md), teams may run **V1 procedural court** and **V2 packet** flows **side by side** to compare behavior. That dual-path mode is **Soft OK for demos only** — it is **not** Phase 5 production cutover and **not** a promise that every agency will operate both paths in production.

Do **not** invent:

- A customer-visible **feature flag** name or admin toggle for V2 cutover.
- A **cutover date** or “automatic migration” story.

<mark style="color:red;">**Decision needed:**</mark> When Phase 5 cutover is ready for customer-facing language, this page should gain an implementation-linked section — until then, keep cutover out of pitches.

## Which guide to hand someone

| Audience | Start here |
|----------|------------|
| Clerk learning daily court work | [Court (V1)](../README.md) and [How-tos](../how-tos/README.md) |
| Sales / solutions demoing the packet overlay | [Demoable now](demoable-now.md) → [Path walk](path-walk.md) |
| BA or engineering alignment | Phase specs and BA PASS scores (not duplicated in this customer set) |

## Locked differences to keep straight

| Topic | V1 docs | V2 packet path |
|-------|---------|----------------|
| Pending work | Queues and procedural states | Active packet status; “pending judge” = submitted packet awaiting staff |
| Hardship evidence | <mark style="color:red;">**TODO:**</mark> map to V1 finance/program pages if a separate V1 story exists | **Mandatory on Submit** for hardship packet |
| Community service clock | <mark style="color:red;">**TODO:**</mark> confirm any legacy V1 CS program wording stays separate | Starts **only** on judge **Approve** |
| Handshake / counter tablet | <mark style="color:red;">**TODO:**</mark> document in V1 only when pitch-safe | **Off pitch** until two-browser verify — see [Demoable now](demoable-now.md) |

## Related

- [Court V2 index](README.md)
- [Court (V1)](../README.md)
