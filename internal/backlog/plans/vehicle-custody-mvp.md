---
backlog: "Vehicle Custody MVP · VCS"
status: done
created: 2026-08-09
---

# Plan: Vehicle Custody MVP

## Goal

Deliver create → edit → hold → release on the existing `VCS` module shell, with required Master Vehicle and optional Master Location / Organization / Person links. No CAD/RMS/Evidence coupling.

## Context

- Foundation stubs: [`five-module-foundation-stubs.md`](five-module-foundation-stubs.md)
- Pattern: Fleet MVI + master module cards; Equipment RecordNumbers; CodeCommons via `Insert_Code`

## Locked decisions

See Cursor plan `vehicle_custody_mvp` — required MVI; optional MLI (retrieved from), MOI (tow), MPI (owner); release requires MPI; OfficerId; free-text StorageLocation; OPEN/RELEASED; block release while hold.

## Approach

1. Reshape entity + EF migration (codes, RecordNumbers, merge remaps). Search uses EF joins on master snapshots (no separate `vw_VehicleCustodySearch` mapping).
2. Root validation + hold/release endpoints
3. UI list/add/details with master cards
4. Unit tests + verify

## Verification

- [x] `dotnet build` / `dotnet test` filter VehicleCustody (+ merge inventory)
- [x] UI lint/build on `vehicleCustody/`
