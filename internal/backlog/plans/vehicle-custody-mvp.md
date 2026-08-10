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

See Cursor plan `vehicle_custody_mvp` — required MVI; optional MLI (retrieved from), MOI (tow), MPI (owner); release requires MPI; OfficerId; free-text StorageLocation; persisted status codes `OPEN`/`RELEASED` with user-facing **ACTIVE**/**RELEASED**; hold is independent of status; block release while hold; generic PUT cannot change lifecycle/hold/release fields.

## Attachment immutability (MVP note)

Released VCS records are read-only for custody fields. The Attachments tab disables upload/delete when the record is released (`can-upload` gated). Broader shared attachment APIs were left unchanged for the MVP (no invasive framework change).

## Module checklist alignment (post-MVP)

Aligned to `Docs/NEW-RMS-MODULE.md` gaps:

- Detail report: `GET vehicle-custody-records/{id}/report/full-pdf` + Details `<report-lister>`
- Module record groups on Details + associable via `ModuleRecordGrouper` (`VCS`)
- Admin soft-launch flag `ADMIN_MODULES_SHOW_VEHICLE_CUSTODY = true` (dev/on for now; set `false` before customer release)

## Approach

1. Reshape entity + EF migration (codes, RecordNumbers, merge remaps). Search uses EF joins on master snapshots (no separate `vw_VehicleCustodySearch` mapping).
2. Root validation + hold/release endpoints
3. UI list/add/details with master cards
4. Unit tests + verify

## Verification

- [x] `dotnet build` / `dotnet test` filter VehicleCustody (+ merge inventory)
- [x] UI lint/build on `vehicleCustody/`
