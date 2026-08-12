---
title: "2026 H2 monthly product releases"
status: draft
created: 2026-08-09
updated: 2026-08-09
---

# 2026 H2 — Monthly product releases

**Period:** August–December 2026  
**Cadence:** One product release per month  
**Goal:** Allocate **every** 2027 sales feature equally across five releases (ship all before 2027). Months may be packed; balance of count matters more than keeping each month light. Each month also carries **two equal platform packages** (kebab-case + Razor/Dink → QuestPDF).

**Related:** [Annual operating plan — 2026 H2](annual-operating-plan-2026-h2.md), [Strategic roadmap 2026–2029](strategic-roadmap-2026-2029.md), backlog [prioritized.md](../backlog/prioritized.md); product monorepo `Docs/ROUTE-NAMING.md`, `RouteNamingConvention_Tests`, `ThinLine.UI/src/components/sandbox/sandboxReportCatalog.ts`

## Rules of the road

- **Target ship week:** last week of each month (adjust ±1 week for holidays / DPS waits).
- **Equal allocation first:** every listed theme appears in exactly one release; load is spread as evenly as count allows (**4 or 5 themes per month**).
- **Platform tracks:** every release includes **both** platform packages below (kebab + QuestPDF) — same intent size each month; do not skip or pile into December.
- **Done means:** demoable, tested, and releasable — not endless polish.
- **Customer-happy assumption:** prefer new capability over rework of satisfied current workflows.
- Outside this list (OCA PDF polish, grid prints, Hub, etc.) stays **parked** unless a live customer forces it.

## Inventory (22 themes)

| # | Feature |
|---|---------|
| 1 | TLETS |
| 2 | Criminal trespass |
| 3 | Merge tools |
| 4 | Asset / Fleet |
| 5 | Finish bonds (logic + batch/export) |
| 6 | Finish collections |
| 7 | Refund batches |
| 8 | Finish eSign |
| 9 | Clerk / judge flows |
| 10 | Juvenile → adult |
| 11 | Youth diversion |
| 12 | Court dashboards |
| 13 | Civil court module |
| 14 | Violator portal |
| 15 | Patrol dashboard |
| 16 | Improved incident workflow |
| 17 | K-9 module |
| 18 | DA access |
| 19 | AVL / mapping → CAD |
| 20 | Improved booking flow |
| 21 | Custody episode changes |
| 22 | Visitation logs |

**Split:** 4 + 4 + 5 + 5 + 4 = **22** (as even as five months allow).

## Release calendar

| Release | Target | Product theme | Themes | Platform — kebab | Platform — QuestPDF |
|---------|--------|---------------|-------:|------------------|---------------------|
| **26.08** | Late Aug 2026 | Access & masters | 4 | Masters | Masters + notepad + user list (~12) |
| **26.09** | Late Sep 2026 | Court money | 4 | Court | Citations (~5) |
| **26.10** | Late Oct 2026 | Court process & civil | 5 | LE A (incidents + citations) | Incidents (~9) |
| **26.11** | Late Nov 2026 | Portal, patrol & K-9 | 5 | LE B + **BL-026** | Warrant + CE + evidence + images (~9) |
| **26.12** | Late Dec 2026 | CAD & jail | 4 | CAD/Jail/CE/EMS + **BL-008** | CAD/close patrol + RPR + retire Razor (~7 + closure) |

---

## Platform tracks (equal allocation)

Long-running hygiene alongside product themes. **Two packages per month** (kebab + QuestPDF) — do not defer either program to year-end.

### Track A — kebab-case URLs (snapshot 2026-08-09)

| Done | Remaining |
|------|-----------|
| Vue Router SPA paths (kebab; migration redirects removed) | — |
| Accounting API roots + UI `src/api` (on `RouteNamingConvention_Tests`) | — |
| Selected LE/court controllers already on the test allowlist (~32 controllers) | **~175 controllers** not yet enrolled in `RouteNamingConvention_Tests` |
| Most `tlsapi/...` **resource roots** already lowercase/kebab | **Report action segments** still snake_case / camelCase / merged words + matching ThinLine.UI `src/api` callers |

**Kebab done-when:** rename routes + sync UI API clients + enroll those controllers in `RouteNamingConvention_Tests` + update `Docs/ROUTE-NAMING.md` changelog.

### Track B — Razor/Dink → QuestPDF (snapshot 2026-08-09)

**Source of truth:** product-repo `ThinLine.UI/src/components/sandbox/sandboxReportCatalog.ts` (sandbox Dink vs Quest comparison table).

| Status in catalog | Meaning | Count (approx.) |
|-------------------|---------|----------------:|
| `DONE` | Quest is production path (e.g. CE notice letter) | 1 |
| `PARITY_REVIEW` | Quest endpoint + composer exist; need visual parity, UI cutover, then retire Dink | **~41** |
| `DINK_ONLY` | Special cases (HTML blotter; CNT controller commented out) | 2 |

**Grid prints** already on QuestPDF (`CreateGridReportAsync` → Quest) — out of this track.

**Court legal docs** already authored as QuestPDF (plea / FTA / OCA / SQR / etc.) — out of this catalog; not in the Razor migration set.

**Each QuestPDF package’s done-when (per variant family):**

1. Sandbox visual parity → set catalog `status: 'DONE'`.
2. Point production UI (`reportApi` / callers) at the Quest route (or make Quest the only route).
3. Remove or stop calling the Dink/Razor endpoint for that family; delete unused `.cshtml` when nothing else shares it.
4. Prefer collapsing `_questpdf` suffix into the canonical kebab route when cutting over (coordinate with that month’s kebab package).

### Other platform streams

| Stream | Backlog | Where allocated |
|--------|---------|-----------------|
| Multi-value GET query params | **BL-026** | **26.11** (kebab LE B) |
| Device fingerprinting | **BL-008** | **26.12** (kebab closure) |
| Layout primitives (`tls-flex` → named `tls-*`) | UI architecture | Opportunistic on touched files |
| Web Awesome / `TlsPageWa` production | Follow-on to **BL-021** | **Parked for 2027** unless a month finishes early |

---

### 26.08 — Access & masters (late August) — 4 + platform

**Sales story:** “TLETS in motion; masters and fleet ready for go-lives.”

| # | Feature | Backlog / notes |
|---|---------|-----------------|
| 1 | **TLETS** — packet submitted; interface readiness as far as DPS allows | Propose BL-029; `Docs/TLETS/` |
| 2 | **Criminal trespass** — finish module / person surface | **BL-014** |
| 3 | **Merge tools** — search coalesce + scored duplicates | **BL-024**, **BL-025** |
| 4 | **Asset / Fleet** — gap-close to sales-ready | [`equipment-fleet-modules.md`](../backlog/plans/equipment-fleet-modules.md) |

**Platform — Kebab: Masters**

- Normalize Master* report routes → kebab; sync UI; enroll Masters controllers in `RouteNamingConvention_Tests`.

**Platform — QuestPDF: Masters + notepad + user list (~12 variants)**

| Module | Variants |
|--------|----------|
| MPI / MLI / MRI / MVI / MOI | Full + Public detail each (10) |
| FCS | Notepad full (1) |
| USR | User list (1) |

All are `PARITY_REVIEW` today (Quest composers wired). Finish parity → UI cutover → retire Dink templates for these modules.

---

### 26.09 — Court money (late September) — 4 + platform

**Sales story:** “Bonds, collections, refunds, and eSign close the money + paperless loop.”

| # | Feature | Backlog / notes |
|---|---------|-----------------|
| 1 | **Finish bonds** — logic + batch/export | **BL-005**, **BL-004** |
| 2 | **Finish collections** — supplemental item-level referrals | **BL-023** (**BL-027** done) |
| 3 | **Refund batches** | **BL-009** |
| 4 | **Finish eSign** | Propose BL-037 |

**Platform — Kebab: Court**

- Remaining Court report/action segments; sync UI; enroll Court controllers (Accounting already done).

**Platform — QuestPDF: Citations (~5 variants)**

| Module | Variants |
|--------|----------|
| CIT | Full, Public, Court copy, Offender copy, TX criminal complaint |

TX complaint needs careful layout review. Cut over UI citation prints; retire CIT Razor templates when unused.

---

### 26.10 — Court process & civil (late October) — 5 + platform

**Sales story:** “Full court operating surface — clerk/judge, diversion, juvenile, dashboards, civil.”

| # | Feature | Backlog / notes |
|---|---------|-----------------|
| 1 | **Clerk / judge flows** | Propose BL-035 |
| 2 | **Juvenile → adult** | Propose BL-033 |
| 3 | **Youth diversion** | Propose BL-034 |
| 4 | **Court dashboards** | Propose BL-036 |
| 5 | **Civil court module** | Propose BL-042 (new module — MVP “sales ready”) |

**Platform — Kebab: Law Enforcement A (Incidents + Citations)**

- Incident + citation report action segments → kebab; sync UI; enroll controllers.

**Platform — QuestPDF: Incidents (~9 variants)**

| Module | Variants |
|--------|----------|
| INC | Detail Full / Public / Basic; Activity; Synopsis; Police blotter PDF; Arrest affidavit; DA cover sheet PDF; Juvenile referral |

**Leave on Razor (by design):** Police blotter **HTML** (press kit) — Quest is PDF-only. DA cover sheet **HTML** twin stays Razor. Mark those `DINK_ONLY` / keep explicitly; do not block the month on them.

---

### 26.11 — Portal, patrol & K-9 (late November) — 5 + platform

**Sales story:** “Public portal + officer LE modules for 2027 demos.”

| # | Feature | Backlog / notes |
|---|---------|-----------------|
| 1 | **Violator portal** | Propose BL-038 (public / payments) |
| 2 | **Patrol dashboard** | **BL-030** (assigned); [`levelland-patrol-cad-2026-roadmap.md`](../backlog/design/levelland-patrol-cad-2026-roadmap.md); [`patrol-officer-command-center.md`](../backlog/design/patrol-officer-command-center.md) |
| 3 | **Improved incident workflow** | Propose BL-032 |
| 4 | **K-9 module** | Propose BL-043 |
| 5 | **DA access** | Propose BL-039 |

**Platform — Kebab: Law Enforcement B + BL-026**

- Warrant, Notepad, Close Patrol, other LE segments → kebab; enroll tests.
- **BL-026** — multi-value GET query params ([plan](../backlog/plans/BL-026-align-multivalue-get-query-params.md)).

**Platform — QuestPDF: Warrant + code enforcement + evidence + images (~9 variants)**

| Module | Variants |
|--------|----------|
| WAR | Full + Public |
| CEN | Detail Full + Public (letter already `DONE`) |
| EVC | In custody, for incident, chain of custody, inventory audit |
| ATT | Module image print |

---

### 26.12 — CAD & jail (late December) — 4 + platform

**Sales story:** “Map-aware CAD + finished jail custody story.”

| # | Feature | Backlog / notes |
|---|---------|-----------------|
| 1 | **AVL / mapping → CAD** | Propose BL-031; with **BL-022** as needed |
| 2 | **Improved booking flow** | **BL-002** |
| 3 | **Custody episode changes** | Propose BL-040 |
| 4 | **Visitation logs** | Propose BL-041 (or clear done-when on **BL-003**) |

**Platform — Kebab: CAD / Jail / CE / EMS + closure + fingerprinting**

- CAD / CE / EMS / Jail / Common leftovers → kebab; near-full `RouteNamingConvention_Tests`.
- **BL-008** — device fingerprinting.

**Platform — QuestPDF: CAD + close patrol + racial profiling + retire Razor (~7 + closure)**

| Module | Variants |
|--------|----------|
| CLL | Call sheet Full / Public / Dispatcher notes |
| CPT | Detail + batch |
| RPR | Racial profiling summary (TX-2020) |
| CNT | Contact tracing — wire `_questpdf` when/if EMS controller reactivated (`DINK_ONLY` today) |

**Closure (same month):**

- Confirm catalog has no remaining `PARITY_REVIEW` (except documented HTML keepers).
- Delete orphaned `ReportTemplates/**/*.cshtml` and unused SharedResources partials.
- Remove Dink/HtmlToPdf path from production print entry points where nothing remains.
- Sandbox catalog: all PDF families `DONE` or explicitly `DINK_ONLY` with a note.

---

## Week-level rhythm (repeat each month)

| Week | Focus |
|------|--------|
| **W1** | Scope “done when,” spike risks, start heaviest **product** theme; park platform for W3–W4 / DPS-wait gaps |
| **W2** | Primary product theme deep work |
| **W3** | Next product themes + **kebab package** (pairs with report renames) |
| **W4** | **QuestPDF package** (parity + cutover); polish; tests; release notes; ship |

When DPS wait opens earlier, pull QuestPDF parity forward (often sandbox-only) without delaying product.

## Dependency reminders

```text
TLETS (26.08) ──► DPS wait (fill with other 26.08 items)
Court money (26.09) ──► Court process + Civil (26.10) ──► Portal (26.11)
Patrol + incident + K-9 (26.11) ──► stronger with TLETS live path
CAD remediation ──► AVL (26.12)
Jail booking / custody / visitation (26.12) — mostly independent of court
Civil (26.10) — new module; keep MVP boundary explicit in W1
```

## Tracking

- Check off themes here as each monthly release ships.
- Durable implementation detail stays in `internal/backlog/plans/` per `BL-###`.
- Release notes: product-repo `ReleaseNotes/` + docs-repo `release-notes/` per finalize-release process.
