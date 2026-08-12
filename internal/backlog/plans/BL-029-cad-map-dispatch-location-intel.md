---
backlog: "BL-029 · CAD · Map-first dispatch + location intelligence"
status: in-progress
created: 2026-08-11
---

# Plan: CAD map-first dispatch + location intelligence

## Goal

Dispatchers can enable **Dispatch from map** in map options so CAD runs as a **map-first desk**: one big map canvas with the call sheet opening on/in the map. **Location intelligence** surfaces **existing** authorized context (prior calls at the master location + location notes) from the open call — available with or without map-first mode. No new premise-alert schema.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-029**.
- **Design:** [cad-desk-arrangements.md](../design/cad-desk-arrangements.md) (M4+ map-first / on-map sheet / intel).
- **Product:** `Docs/CAD-AVL-Integration.md` (dispatcher map UX).
- **Risk / lane:** Feature (CAD UI + thin CAD read API). No EF migrations. CadAccess for intel; do not widen Masters write surfaces.

## Approach

1. Persist `mapDispatchMode` in CAD user prefs; toggle in Map options.
2. When on: full-bleed map desk chrome; **open-call strip across the top**; **units docked left**; calls/notes via drawer FABs; pin/strip click opens on-map call sheet on the **right**.
3. CAD-authorized location-intelligence read DTO from existing notes + CALL records (`vw_MasterLocationRecords`).
4. `CadLocationIntelligencePanel` from call location affordances (sheet + map action bar); not gated on `mapDispatchMode`. CAD desk hosts one drawer.

## Files / areas (expected)

- `ThinLine.UI/src/components/cad/CadMapPanel.vue`, `CadContainer.vue`, `CadCallSheetContainer.vue`, new intel panel
- `ThinLine.UI/src/stores/cadStore.ts` (prefs)
- `ThinLine.API` CAD call controller + BO service for location intelligence
- Docs: this plan, desk arrangements, CAD-AVL pointer

## Verification

- [x] `dotnet build` Business.Objects / WebAPI / UnitTests
- [x] `dotnet test` filter `CallLocationIntelligenceService_Tests` (+ Calls_WebApi_Tests)
- [x] UI: touched CAD files lint clean of errors; `npm run build` in `ThinLine.UI`
- [x] Vitest: `cadStoreUserPreferences` includes `mapDispatchMode`
- [ ] Manual: map-first on → pin → on-map sheet → assign; location intel; mode off restores desk

## Manual smoke checklist

1. Enable AVL; open CAD; Map options → **Dispatch from map** ON → desk is full-bleed map with open-call strip on top and units on the left.
2. Click call pin or a strip card → call sheet docks on the **right**; units list stays on the **left**; assign/status works.
3. FAB Calls/Notes open drawer panels (units are on-map left, not a FAB).
4. With an open call that has a location (map-first **or** classic desk) → **Location intelligence** (sheet or Map action bar) → notes + prior calls; open a prior call.
5. Toggle mode OFF → classic columns restore; pin click opens desk sheet column; location intel still works.

## Open questions

- None locked for MVP (map-first + existing data only).

## Notes

Explicit non-goals: `PremiseAlert` entity; empty-map create-call; board auto-badges; geocode-radius nearby search.
