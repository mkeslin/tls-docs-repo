# Court programs and eligibility

> **Past demo ceiling:** This page describes behavior at pushed tip `6234e081ca`, which is **past** the official demo ceiling `64c4bd40a0`. It is **not** approved for demos until Court BA scores that tip PASS and the tls-* Playwright suite is re-run. See [Demoable now](demoable-now.md).

Court V2 **court program** packets (driving safety course, deferred disposition, youth diversion, and related clerk/tablet flows) share one spine: defendant or clerk **submits**; a judge **Approve**, **Reject**, or **NeedsInfo** enrolls or denies the program.

## Statutory clocks (read-only in V2 UI)

| Program | Default period shown in V2 |
|---------|----------------------------|
| **Driving safety course (DSC)** | **90** days |
| **Deferred disposition** | **180** days (default/cap; over-max dates clamp server-side) |

Copy appears on clerk program flows, portal program request, and online judge-packet stubs. Agency default day fields in admin are capped to the same statutory limits in the current Court V2 build.

## Tier 1 eligibility (DSC and deferred)

The resolution hub and portal gate **Driving safety course** and **Deferred disposition** using shared statutory rules. Examples reflected in product behavior and demo fixtures:

| Situation | Typical hub/portal result |
|-----------|---------------------------|
| **CDL** (citation driver license class) | DSC denied; deferred denied on moving violations |
| **Workers present** on citation | DSC and deferred denied |
| **Offense type missing** (blank OCA) | DSC not available — *Offense type missing* |
| **Date of birth missing** on moving deferred | Blocked — *Date of birth required for Deferred on a moving violation* |
| **Under 25** on a moving violation | Deferred may proceed; a **DSC condition** is added on the same plan (judge queue shows informational statutory notes) |
| **School bus** offense (TC **545.066**) | DSC **hard deny**; deferred may remain available with discretionary notes |
| **Leave scene** offenses (TC **550.022** / **550.023**) | DSC **hard deny**; deferred may remain available with discretionary notes |

Judge queue cards for court programs can show a blue **Statutory notes (informational)** box, optional forced-DSC line, and *Approve re-checks these rules against current case facts.*

## DSC request details (portal and clerk)

Beyond tier-1 gates, DSC packets can collect:

- **Military status** (required on requests).
- **License state**, **last DSC completed** (clerk-oriented fields when shown).
- **Document uploads** (insurance and other coded document types).

Submit is blocked when required DSC answers or documents are missing (portal shows the validation message from the rules).

## DSC good-cause extension

While a driving safety course is **active**, defendants or staff can use **Ask for more time** (CCP **45A.355**):

- Portal: **Need more time to finish the driving safety course? You can ask the judge for more time.**
- Counter: **Dsc more time** panel on the violation status area; judge sets a new DSC due date.

## Youth diversion (ages 10–16, non-traffic)

Youth diversion targets eligible minors (product rules: age **10–16**, **non-traffic**, offense type present). UI and server checks include:

| Area | Product behavior |
|------|------------------|
| **Parent/guardian** | **Parent or guardian name** and **Parent or guardian signed name** on tablet; paper path confirms parent hand signature. Tablet intro: *A parent or guardian must sign youth diversion next to the child.* |
| **Youth condition** | Clerk/paper selects among conditions such as **COMMUNITY SERVICE**, **TOBACCO AWARENESS**, **CLASS ALCOHOL**. |
| **Prosecutor objection** | Clerk fields can record prosecutor objection (hard deny when entered). |
| **Other-court prior diversion** | Optional prior start date and outcome fields feed server eligibility. |
| **Judge referral and orders** | Judge-only signed orders, dismissal, and ready-to-close paths on the disposition plan (**Youth diversion court** panel). |
| **Confidentiality** | Public portal lookup and payment paths block confidential youth-diversion records; staff with access can work the case. |

**Youth diversion agreement** replaces the shared deferred form for youth packets.

DSC pre-judgment plans are **not** applied to youth diversion plans (statutory separation in code).

## Other status panels (V1/V2 shared case record)

These panels appear on the court violation **Status** area when rules apply:

| Panel | Purpose |
|-------|---------|
| **Minor plea — parent or guardian present** | CCP **45.0215** — minor plea requires parent present; online/mail deny when required. |
| **Parent nonattendance dismissal** | CCP **45A.403** parent contributing-to-nonattendance dismissal packet. |
| **Ability to pay inquiry** | CCP **45A.252** / **45A.253** — judge records ability-to-pay answer before judgment. |
| **Community service completed** | CCP **45A.254** — record completion hours and credit. |
| **Chemical dependency deferral** | CCP **45A.402** — pre-judgment chemical dependency deferral on eligible cases. |

## Related

- [Portal and online options](portal-and-online-options.md)
- [Compliance gaps (not full Texas statutory coverage)](compliance-gaps.md)
- [Path walk](path-walk.md)
