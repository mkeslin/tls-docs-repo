# Court V2 (packet path)

These pages describe the **Court V2** path: defendant-initiated **typed disposition packets** on a shared packet spine, running **in parallel** with the existing [Court](../README.md) guides (V1 procedural workflows). They are **customer Guide** pages for demos and orientation — not internal SOPs or phase spec copies.

V2 does not replace the V1 topic pages. Clerks and judges still use V1 guides for day-to-day procedural states, queues, payments, and documents unless you are explicitly walking the V2 packet overlay.

## Pages in this set

| Page | Use when |
|------|----------|
| [Demoable now](demoable-now.md) | Sales demo ceiling — what is on-pitch vs off-pitch |
| [Path walk](path-walk.md) | Ordered customer-facing walk of the current V2 demo path |
| [V1 vs V2](v1-vs-v2.md) | Side-by-side for local dual-path demo walks |

## Demo and verification gate

Playwright end-to-end tests are **paused**. Demo unlock for the V2 ceiling is **unit/API green + Court BA PASS** on the claimed tip — not Playwright green.

**Demo tip ceiling (ops):** `64c4bd40a0` (parent `b8a7ffcd48`; local unit green-up). Details and pitch boundaries are in [Demoable now](demoable-now.md).

## Related

- [Court (V1)](../README.md)
- [Court clerk workshop](../../training/court-clerk-workshop.md)
