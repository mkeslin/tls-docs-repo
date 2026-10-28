# Court V2 demo ceiling (internal)

Internal reference for the Court V2 demo boundary, build tips, verification gate and test references. Customer pages don't show hashes or test names; they link to [Demoable now](../../../customer/court/v2/demoable-now.md) and use the "Not yet approved for demos" banner for anything past the ceiling.

Last updated 2026-10-28 by Court Doc Bot from the BA answers (2026-10-28) and Dev answers (HEAD `c9600367c3`).

## Ceiling

| Item | Value |
|------|-------|
| **Official demo ceiling** | `64c4bd40a0` (parent `b8a7ffcd48`). Matthew's rule: the ceiling stays here until he moves it. |
| **Demo unlock gate** | Unit and API tests green, plus Court BA PASS, on the claimed tip. Playwright end-to-end is **paused** and isn't the gate. Don't claim Playwright green. |
| **Approved for demos at the ceiling** | Handshake two-browser verify (approved by Matthew). Sales unlocked the Issuance PC cite and the clerk ↔ tablet flow. The customer list is in Demoable now. |

## Build tips (as of 2026-10-28)

| Tip | Status | Notes |
|-----|--------|-------|
| `6234e081ca` (Oct 13) | Pushed | Older docs described this tip. 273 commits to HEAD. |
| `2713f990f2` (Oct 19) | Pushed ancestor | 148 commits to HEAD. |
| `88532e2aa5` (Oct 28, 6:08 AM CT) | Local, unpushed | Test-only commit ("harness-session-race r3"). Recent commits are bug fixes and tests, not new customer features. |
| `c9600367c3` | Dev HEAD | Test-only on top of `88532e2aa5`; changes only `t3.outcomeWalks.local.spec.ts`. Dev answers cite this tip. |

The tips are nested: `64c4bd40a0` → `6234e081ca` → `2713f990f2` → `88532e2aa5` → `c9600367c3`. From the ceiling to `88532e2aa5` is 928 commits, which include merged-in jail, TLETS, Crosby and Nuxt work that isn't court documentation.

## Key commits referenced in the docs

| Commit | Date (CT) | What it changed |
|--------|-----------|-----------------|
| `d320ff4883` | Oct 27, 2026, 5:22 PM | Revoke on pending requests (ux-b1b2c). Applies to all existing V2 requests. |
| `3b97020180` | Oct 19, 2026, 7:34 PM | DSC more-time counter panel gated on Deferred disposition state (eligibility stays the server's active-DSC check). |
| `ac51f8e39c` | after Oct 19 | Batch approve of paper packets in the Judge Queue. |

## BA scoring

| Score | Tip | Notes |
|-------|-----|-------|
| **B4 PASS** (known-gap rows) | `c9600367c3` | Keep the four combination rows "Known gap, not shipped". Hardship checkbox wording rule. One open request per case. |
| **B6** (revoke) | `c9600367c3` | Revoke (Submitted or NeedsInfo) or Cancel outcome (Draft) moves the request to Cancelled, which frees the case. The one-open-request rule counts only Draft, Submitted and NeedsInfo. Online Pay in full revoke isn't built; not documented. |

What BA walked live vs in code only: the prosecutor workspace, the motion to dismiss routes (paper and portal to judge) and the prosecutor Youth Diversion objection are **in code** (the objection is unit tested) and were not walked live by BA.

## Test references

| Area | Reference |
|------|-----------|
| Outcome walks (local) | `t3.outcomeWalks.local.spec.ts` (only file changed in `c9600367c3`) |
| Revoke blocked state | Workspace hub test id `active-packet-revoke-blocked`; Cancel outcome stays available |
| Prosecutor Youth Diversion objection | Unit tested (BA 2026-10-28) |
| Acceptance criteria | `Docs/Court/V2-Disposition-Engine/` phase review folders (`AC.md`, `AC-CHECKLIST.md`, phases 2.1–4.3) |
| UAT scenarios | `API/docs/COURT_VIOLATION_STATE_MACHINE_UAT_SCENARIOS.md` |

## Internal gaps (not in customer docs)

| Gap | Owner | Detail |
|-----|-------|--------|
| **D9 portal one-time code** | Court Developer Bot | The UI asks for the one-time code on every action except paying online and exploring options. The server enforces it only for a payment plan with a plea; V2 cards rely on the UI. |
| **D4 hardship evidence** | Court Developer Bot | The portal records only evidence file-name metadata, not the file. Customer docs say evidence is required, never that it's stored. |
| **D13 leftover stubs** | Court Developer Bot | The portal judge-packet stub still shows Guilty / No contest options; the server refuses them. No standalone guilty or no contest request is documented. |
| **D15, D16** | Court Developer Bot | Open. Not documented. |

## Offense catalog codes

DPS and catalog codes such as `3205E`, `LP-1` and `3667A` are internal only. Customer pages say to show only offense catalog entries the agency has confirmed.

## Related

- [Court V2 decisions log](decisions-log.md)
- [Customer: Demoable now](../../../customer/court/v2/demoable-now.md)
