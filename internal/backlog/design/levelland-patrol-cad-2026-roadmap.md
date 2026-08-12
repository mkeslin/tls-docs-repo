---
title: "Levelland fit — Patrol + CAD 2026 roadmap"
status: accepted
created: 2026-08-11
modules: [Patrol, CAD, AVL, Citations]
backlog: ["BL-030", "BL-022", "BL-029"]
---

# Design: Levelland fit — Patrol + CAD 2026 roadmap

> **Source of truth:** Internal Docs (GitBook). Companion interactive canvas may exist in Cursor; this document is canonical for the team.

**Thin Line RMS · Make Patrol the field experience; make CAD + Patrol share one operational reality**

Roadmap derived from Levelland-style operational-fit scoring against **master** (CAD desk/map/arrangement + Patrol Command Center). Discipline: make the existing product **truthful and dependable** before adding impressive functionality.

**Status:** Accepted product posture (2026) — **P0.0 confirmed** as initiative goal  
**Related design:** [Patrol officer command center](patrol-officer-command-center.md), [CAD desk arrangements & map panel](cad-desk-arrangements.md)  
**Related backlog:** [**BL-030**](../prioritized.md) (this initiative); [BL-022](../plans/BL-022-cad-large-agency-remediation.md); [BL-029](../plans/BL-029-cad-map-dispatch-location-intel.md)

---

## Goal

**P0.0 (confirmed):** Patrol is the field experience Thin Line sells and implements for **25–50 officer agencies.**

Officers perform common vehicle workflows with CAD, records, mapping, and documentation in one cockpit—not by retreating to classic Mobile CAD as the primary go-live path (classic remains an escape hatch / legacy surface).

**Done means:** A 25–50 officer agency can perform the field and dispatch jobs Levelland described **without workarounds, duplicate effort, or promised future development**—using Patrol as the sold field experience and a CAD desk that stays synchronized with the officer. P0.1–P0.8 exist only to make this goal true; P0.8 acceptance proves it.

---

## Product commitment (P0.0) — confirmed

| | |
|--|--|
| **Decision** | **Confirmed** — Commit to Patrol as the field experience for 25–50 officer agencies. |
| **Kind** | Product goal / gate — not a development ticket and not optional. |
| **Why** | Patrol is the architectural answer to vehicle workflows with CAD, mobile, records, and mapping working together. Levelland-class buyers asked for that integration; finishing Patrol is the path. |
| **Not** | Selling classic Mobile CAD + Citations as the primary field story for this segment. |

All following P0 work (CadHub, queries, tray, citation, agency config, server session, AVL, E2E acceptance) exists to make this commitment **operationally true**.

---

## Three outcomes (roadmap shape)

| Horizon | Outcome | Meaning |
|---------|---------|---------|
| **P0** | **Patrol is real** | An officer can perform Levelland field workflows end-to-end using production data and services. |
| **P0** | **Dispatch and Patrol share reality** | Calls, units, AVL, assignments, notes, lookups, records, and dispositions stay synchronized. |
| **P1** | **It holds under operational pressure** | Multiple calls, keyboard workflows, filters, multiple monitors, interruptions, handoffs, and unusual encounters do not make the experience fall apart. |
| **P2** | **Make it exceptional** | Nearest-unit intelligence, map assignment, incident replay, advanced situational awareness—**after** P0/P1. |

Do not confuse P2 “wow” features with resolving Levelland’s objection. If dispatch can clearly see which units are available and where they are, nearest-unit recommend is optional.

---

## P0 — Make Patrol true (officer viability order)

| Order | Kind | Work item | Closes scenarios (scorecard) |
|-------|------|-----------|------------------------------|
| **P0.0** | **Confirmed goal** | Patrol is the sold field experience for 25–50 officer agencies | 9–22, 26 |
| **P0.1** | Build | CadHub (live sync) on `/patrol` | 9, 18, 22 |
| **P0.2** | Build | Real field query path — person / DL / plate / vehicle from Patrol | 11, 12, 13 |
| **P0.3** | Build | Lookup → encounter context / tray → downstream prefill | 12, 13, 14 |
| **P0.4** | Build | Real citation workflow; eliminate mock fallback | 14, 20, 26 |
| **P0.5** | Build | Agency-managed Patrol configuration | 15, 21, 26 |
| **P0.6** | Build | Server-backed encounter / session state | 16, 22, 24 |
| **P0.7** | Investigate + build | Operationally dependable unit location (AVL) | 7, 1, 8 |
| **P0.8** | Acceptance | End-to-end scenario validation (no mocks, no manual fixes) | 9–22, 26 |

### P0.2 — Field queries (acceptance)

**Requirement:** Officer can perform required field queries from Patrol **without dispatcher assistance or unnecessary workflow switching**.

Underneath that acceptance test, define and implement:

- What Thin Line can return **today** (e.g. local master, LETS request logging)
- What requires **external / hot-file** integration

Do not describe this as “gate query reality.” Ship a real query path until the acceptance test passes.

### P0.3 — Encounter context (one-system proof)

| Bad integration | Thin Line integration |
|-----------------|------------------------|
| Run DL → get results → open citation → type person again | Run DL → select person → person enters encounter/tray → citation already knows the person |

Lookup and intel must feed the same encounter context used by citations and other stop artifacts.

### P0.7 — AVL (requirement first)

**Requirement:** Dispatch can depend on unit location **operationally**.

1. Ship **stale / unavailable** presentation on CAD and Patrol maps (never present dead GPS as current).
2. **Investigate** whether browser/device GPS is operationally reliable for target agencies. If not, elevate vendor/modem (or equivalent) AVL into P0/P1 infrastructure—do **not** default “reliable real-time unit location” to hopeful P2.

The requirement is not “integrate a modem.” Let the technical solution follow from operational dependability.

### P0.8 — Acceptance scenarios

Complete only when **both** run on production paths—no mocks, no manually fixing data, no “normally this would…”

**Scenario A — Dispatch-led**

Dispatcher creates call → assigns officer → officer receives it in Patrol → officer runs person/DL/plate → information enters encounter context → officer takes action → creates citation/record → CAD receives appropriate updates → officer clears → dispatcher sees clearance → resulting records remain linked.

**Scenario B — Officer-initiated**

Officer initiates traffic stop → CAD becomes aware → AVL remains visible → plate/DL query → person/vehicle follows into citation → citation issued → disposition → clear.

If either breaks, P0 is not done.

---

## P1 — Hold under operational pressure

Promote dual-monitor / pop-out hardening early—Levelland specifically complained about dispatch layout flexibility; the architecture exists; make sure it survives real use.

| Order | Work item | Notes / backlog |
|-------|-----------|-----------------|
| **P1.1** | Harden dual-monitor / pop-out CAD desks | Detach/reattach, crash reopen, selection sync, training presets |
| **P1.2** | Re-enable location intelligence on the live CAD desk | **BL-029** |
| **P1.3** | CAD keyboard navigation + command line under load | **BL-022** |
| **P1.4** | Board filtering + bulk clear | **BL-022** |
| **P1.5** | Thin handoffs: arrest → booking, tow → impound | Prefill from tray/call; not inlined booking/inventory UIs |
| **P1.6** | Harden evidence attach + durable SA / Lost & Found notes | Real CAD notes; fix module keys |
| **P1.7** | Classic mobile citation ↔ CAD link when Patrol unused | Escape-hatch path still leaves linked records |

---

## P2 — Make it exceptional

| Work item | Why later |
|-----------|-----------|
| Nearest / best-available unit recommendation | Wow feature; not required if availability + location are already clear (**BL-022** class) |
| Map assign gestures, multi-sheet, presence, written-warning document | Operational polish / optional agency asks |
| Incident replay, advanced situational awareness, predictive layers | Explicitly after P0/P1 outcomes are true |

**Do not** let map drag-and-drop or nearest-unit steal time while encounter state still lives in localStorage.

---

## Scoring posture (how we judge “done”)

Score what a dispatcher or officer can **actually accomplish** through the currently implemented UX.

- Do **not** award points for architecture that *could* support a scenario.
- Do **not** credit planned functionality, TODOs, commented code, mocks, or work that requires development before an agency could use it.
- Prefer full end-to-end scenarios (P0.8) over ticket checklists.

Related scorecard dimensions (0–4) used in the Levelland operational-fit review: Not supported → Design only → Partial/workaround → Needs polish → Production-ready for a 25–50 officer agency.

---

## Decisions

1. **P0.0 confirmed (2026-08-11)** — **Patrol is the sold field cockpit** for 25–50 officer agencies. Finish it rather than retreating to classic Mobile CAD as the primary story. This is the initiative goal for **BL-030**.
2. **P0 ordering follows end-to-end officer viability** — sync, queries, tray prefill, real citation, agency config, server session, dependable AVL, then acceptance.
3. **Lookup → tray is P0** — duplicate re-entry of query results into citations is a Levelland-class failure.
4. **Nearest-unit recommend stays P2** — situational clarity on the desk is the baseline; recommendation is exceptional.
5. **AVL classification is requirement-driven** — stale UI now; vendor/modem only if browser GPS cannot meet operational dependability.

### Alternatives considered

- **Sell classic Mobile CAD + Citations as the field path** — Safer short-term for CadHub/maturity, but abandons the integrated vehicle cockpit Levelland asked for. **Rejected** as primary go-live story; kept as escape hatch only.
- **Keep query work as “document the gap”** — Insufficient; Levelland rejection language is about performing queries from the vehicle.

### Consequences

- Engineering focus through P0 is Patrol productionization + shared reality with CAD—not map toys.
- Soft-launch / claims for Patrol may still be needed for rollout control; the **product goal** is not in question.
- BL-022 / BL-029 continue as P1 pressure and map/intel depth, subordinate to P0 acceptance of the Patrol field goal.

---

## Scope

### In scope

- Delivering on **P0.0**: Patrol Command Center as the production field experience
- Patrol productionization (session, config, queries, tray, citation, sync)
- CAD desk reliability under multi-monitor and peak load (P1)
- AVL operational dependability (presentation + reliability investigation)
- End-to-end acceptance scenarios above

### Out of scope (until P2)

- Nearest-unit / predictive recommend
- Incident replay and advanced GIS “wow” layers
- Full in-stop Jail booking or tow inventory UIs (handoffs only in P1)

---

## Open questions

- Exact hot-file / external query partner and return UX for P0.2 (agency-dependent).
- Outcome of P0.7 AVL reliability investigation for target hardware (MDT browser GPS vs modem).
- Soft-launch claim/flag shape for Patrol rollout (**how** we roll out—not **whether** Patrol is the field goal).

---

## Related

- Living Patrol UX decisions: [patrol-officer-command-center.md](patrol-officer-command-center.md)
- CAD desk / map: [cad-desk-arrangements.md](cad-desk-arrangements.md)
- Product monorepo: `ThinLine.UI/src/components/dashboard/officer/`, `ThinLine.UI/src/components/cad/`
