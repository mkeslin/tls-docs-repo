---
backlog: "Civil Process MVP · CVP"
status: done
created: 2026-08-10
---

# Plan: Civil Process (Civil Service) MVP

## Goal

Bare-bones Civil Process (`CVP`) MVP: one process-for-service root, StatusCode lifecycle, service-attempt child, thin add → details shell. No court integration or writs.

## Context

- Foundation: [`five-module-foundation-stubs.md`](five-module-foundation-stubs.md)
- Pattern: Vehicle Custody thin-add + ClosePatrol/Warrant service-attempt child
- Checklist: product-repo `Docs/NEW-RMS-MODULE.md` (MVP must include §§6, 9–11)

## Locked decisions

- Lifecycle: **StatusCode** (`_CVPS`), not BasicWorkflow Draft/Completed — domain statuses with header ToList menu (workflow UX pattern).
- Masters: optional plaintiff/defendant person snapshots + service location snapshot; court/cause remain free text.
- Numbering: system `RecordNumbers` for `CVP`.
- No cross-module associations (record groups chrome is still shipped for future linking).

## Status codes

| Code | Description |
|------|-------------|
| RCVD | RECEIVED |
| ASGN | ASSIGNED |
| ATTM | ATTEMPTING SERVICE |
| SRVD | SERVED |
| UNSV | UNABLE TO SERVE |
| RETN | RETURNED / CLOSED |

## Status transition map

| From | Allowed to |
|------|------------|
| RCVD | ASGN, ATTM, RETN |
| ASGN | ATTM, RETN |
| ATTM | SRVD, UNSV, RETN |
| SRVD | RETN |
| UNSV | ATTM, RETN |
| RETN | — (terminal) |

A service attempt recorded with result `SVD` also moves the parent record to `SRVD`.

## Delivered

**API** (migration `20260810101548_CivilProcessMvp`, applied to ThinLineRMS):

- Entity + `CivilProcessServiceAttempts` + codes `_CVPS` / `_CVPT` / `_CVPR` + `RecordNumbers` for `CVP`
- `CivilProcessRecordRoot` — create defaults `RCVD`; status via domain action; nested attempts; RETN field-edit lock
- Search with FilterMode Active / Returned / All
- Controllers: CRUD/status/attempts + `gridPrint` + detail `full-pdf`
- Master-merge remaps for person/location snapshots; VM includes `ModuleRecordGroups`

**UI (NEW-RMS-MODULE checklist):**

- Thin add → details by process number
- Search/list grid + **search grid print**
- Details shell: status chip + Status menu; tabs General / Attempts / Attachments / History
- Chat|task, favorites, **report-lister**, **module-record-grouper**, `useModuleBase('CVP')` recent/pinned
- Soft-launch: `ADMIN_MODULES_SHOW_CIVIL_PROCESS = true`

## Verification

- [x] Migration applied (`CivilProcessMvp`)
- [x] Codes + RecordNumbers seeded in ThinLineRMS
- [x] `dotnet build` + CivilProcess unit tests
- [x] Search grid print / detail PDF / record groups wired per checklist
- [ ] Manual smoke: create → status → attempt → served/returned; print search + detail PDF; groups/recent

## Out of scope (unchanged)

Court integration, writs, fees/mileage, maps/GPS, mobile, return-of-service forms, e-filing, notifications.
