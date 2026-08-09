---
backlog: "Five module foundation stubs · K9M CVC CVP VCS CAS"
status: done
created: 2026-08-09
---

# Plan: Five-module foundation stubs

## Goal

Ship **one coordinated foundation** that registers and soft-hides five new modules end-to-end (API keys/claims/flags + thin root CRUD shells + UI routes/nav), matching the soft-launch pattern used by Criminal Trespass / Equipment / Fleet. Domain depth comes later, one module at a time.

## Context

- **Backlog reference:** Not yet assigned a `BL-###`; initiative tracked here until prioritized.
- **Risk / lane:** Feature; touches auth claims and EF migrations (product-repo `AGENTS.md` risk boundaries — explicit in scope for foundation).
- **Pattern:** Equipment/Fleet foundation ([`equipment-fleet-modules.md`](equipment-fleet-modules.md)); thin stack from Criminal Trespass ([`BL-014-criminal-trespass.md`](BL-014-criminal-trespass.md)).

## Locked decisions

| Module | Key | Drawer label | Shape | Numbering | Nav |
|--------|-----|--------------|-------|-----------|-----|
| K9 Management | `K9M` | K9 | Root + children (placeholders) | None | After Fleet |
| Court Civil | `CVC` | Court Civil (mirrors Court Violation) | Lighter case container under **Court** (not Law Enforcement) | Agency-entered cause # | After Court Violation |
| Civil Process | `CVP` | Civil Process | Root + children (placeholders) | System + optional originating court/cause | After Warrants |
| Vehicle Custody | `VCS` | Vehicle Custody | Root + thin children | System (shared helper) | Near Evidence |
| Cases | `CAS` | Cases | Lighter Incident shell | System (shared helper) | After Incidents |

- Soft-hide Admin toggles: **yes** — commented rows in `AdminAgencyModules.vue` like CTP/EQP/FLM. Disabled = hidden from nav/use; schema/data retained.
- Do **not** reuse `IMP` (CAD Impound Log). `VCS` is a separate RMS custody-event module.
- Do **not** add separate `SystemModules` for IA / Security Incident / Small Claims / etc. — those are future types under `CAS` / `CVC`.

## Claims / flags

| Module | Claims | Agency flag | CanAccess / CanModify |
|--------|--------|-------------|------------------------|
| K9 | `Rms.K9.Access`, `Rms.K9.Modify` | `K9Enabled` | `canAccessK9` / `canModifyK9` |
| Court Civil | `Rms.CourtCivil.Access`, `Rms.CourtCivil.Modify` | `CourtCivilEnabled` | `canAccessCourtCivil` / `canModifyCourtCivil` |
| Civil Process | `Rms.CivilProcess.Access`, `Rms.CivilProcess.Modify` | `CivilProcessEnabled` | `canAccessCivilProcess` / `canModifyCivilProcess` |
| Vehicle Custody | `Rms.VehicleCustody.Access`, `Rms.VehicleCustody.Modify` | `VehicleCustodyEnabled` | `canAccessVehicleCustody` / `canModifyVehicleCustody` |
| Cases | `Rms.Cases.Access`, `Rms.Cases.Modify` | `CasesEnabled` | `canAccessCases` / `canModifyCases` |

Wire **both** `SecurityValidator` and `AuthorizationService.TestModule*Claim*` for all five.

## Routes (kebab-case)

| Module | Paths |
|--------|-------|
| K9 | `/module/k9`, `/module/k9/add`, `/module/k9/:id/:agencyId` |
| Court Civil | `/module/court-civil`, … |
| Civil Process | `/module/civil-process`, … |
| Vehicle Custody | `/module/vehicle-custody`, … |
| Cases | `/module/cases`, … |

## Approach

1. **PR1 — Foundation:** Shared registration hotspots + thin root CRUD + UI shells + soft-hide for all five. Migrations via `dotnet ef migrations add` only; wrap SQL in `exec()` per migrations rule.
2. **PR2+:** Depth one module at a time.

Do **not** split PR1 into five PRs — shared files would conflict repeatedly.

## Files / areas (expected)

- `ThinLine.API/` — `SystemModules`, `ClaimKeys`, Agency flags, auth/common migrations, entities, DataStore/UoW/DI, services/controllers, ViewModels
- `ThinLine.UI/` — `BaseModuleDetails`, moduleStore/helpers, routes, NavDrawers ×3, module component shells, soft-hide Admin
- `ThinLine.API/docs/API-FEATURE-INDEX.md`

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test ThinLine.API/ThinLine.API.UnitTests` — focused factory/claim/gating tests
- [ ] UI: `npm run lint` / `npm run build`; extend route-naming vitest
- [ ] Manual: agency flag false → nav hidden; flag + claims true → search/add/details shell

## Out of scope (PR1)

K9 training/deployment workflows; Court Civil parties/filings/judgments/fees; Civil Process service attempts/returns; Vehicle Custody tow rotation/notifications/fees/auctions; Cases IA/Security business logic; un-hiding Admin toggles; CAD CallModules linking; reports/grid print.

## Notes

Thinner shapes (Court Civil, Cases) can grow to root + children later without new `SystemModules` keys.
