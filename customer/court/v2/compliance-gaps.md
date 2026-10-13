# Compliance gaps (customer-facing honesty)

> **Past demo ceiling:** This page describes behavior at pushed tip `6234e081ca`, which is **past** the official demo ceiling `64c4bd40a0`. It is **not** approved for demos until Court BA scores that tip PASS and the tls-* Playwright suite is re-run. See [Demoable now](demoable-now.md).

Court V2 in the current Court V2 build adds many statutory checks, but **Thin Line does not claim full Texas Code of Criminal Procedure compliance** for every offense and edge case. Use this page when sales, clerks, or judges ask whether “everything in the statute” is automated.

## Not treated as fully supported in customer materials

The following items are **open in legal/audit review** or intentionally not pitched as complete compliance. Product behavior may partially overlap; do not promise full statutory coverage.

| Topic | Customer guidance |
|-------|-------------------|
| **DSC speed deny** (CCP **45A.352(a)(5)** and related speed thresholds) | Speed facts are collected on NEW intake and health checks exist; **full speed-based DSC deny alignment is not documented as complete** for Texas compliance. |
| **Youth diversion** parent consent, prior diversion, and prosecutor rules | UI collects parent/guardian signatures and clerk objection/prior fields; **full CCP 45.304 consent and prosecution rules are not documented as complete**. |
| **Minors with two or more alcohol priors** | **Not documented as supported** in this release slice. |
| **Playwright e2e on tls-* controls** | End-to-end UI automation has **not** been re-run on the tls-* migration at tip `6234e081ca` (past official ceiling `64c4bd40a0`). |

## What to say about online DSC

State law allows a court to **authorize** online driving safety course requests through the portal. Thin Line implements portal DSC **only when** product eligibility allows the request. Do **not** tell agencies that every defendant can always request DSC online without court configuration and offense-level denies.

## Related

- [Demoable now](demoable-now.md)
- [Court programs and eligibility](court-programs-eligibility.md)
