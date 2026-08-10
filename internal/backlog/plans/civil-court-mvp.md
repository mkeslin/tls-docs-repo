---
backlog: "Court – Civil MVP · CVC"
status: done
created: 2026-08-10
---

# Plan: Court – Civil MVP

## Goal

Bare-bones Court – Civil (`CVC`) MVP: one civil case root with agency-entered cause number, StatusCode lifecycle, case-type lookup, parties child, scalar next hearing + light disposition, thin add → details shell, and full NEW-RMS-MODULE checklist (grid print, detail PDF, chat, record groups, recent).

## Context

- Foundation stub already existed (`CourtCivilCase`, claims, agency flag, placeholder UI).
- Mirror: Civil Process (`CVP`) for MVP shell/checklist; agency-entered cause like Fleet unit number (not RecordNumbers).
- Checklist: product-repo `Docs/NEW-RMS-MODULE.md`.

## Locked decisions

| Topic | Choice |
|-------|--------|
| Identity | Agency-entered `CauseNumber` (authoritative); no system process number |
| Lifecycle | **StatusCode** (`_CVCS`), header ToList menu |
| Case types | Codes `_CVCT`: SMCL / DEBT / EVCT / REPR / OTHR |
| Parties | Child collection + role codes `_CVCR` (PLA/PET/DEF/RES) |
| Hearings | Scalar `NextHearingDateTime` |
| Disposition | `DispositionCode` (`_CVCD`), `DispositionDateTime`, optional `JudgmentAmount` |
| Cross-module | None (record-grouper chrome only) |

## Status transitions

| From | Allowed to |
|------|------------|
| OPEN | PEND, HEAR, DISM, CLSD |
| PEND | HEAR, DISP, DISM, CLSD |
| HEAR | PEND, DISP, DISM, CLSD |
| DISP | CLSD |
| DISM | CLSD |
| CLSD | — (terminal) |

## Delivered

**API** (migration `20260810111407_CourtCivilMvp`, applied to ThinLineRMS):

- Deepened `CourtCivilCase` + `CourtCivilCaseParties` + codes + unique agency/cause index
- Status via domain action; nested parties; CLSD field-edit lock
- Search FilterMode Active/Closed/All; gridPrint; detail full-pdf
- Master-merge remaps for party person/org snapshots; moduleRecordGroups on VM

**UI:**

- Thin add (cause #, type, filed) → details by cause number
- Search + print; details General / Parties / Attachments / History
- Chat|task, favorites, report-lister, module-record-grouper, `useModuleBase('CVC')`
- Soft-launch: `ADMIN_MODULES_SHOW_COURT_CIVIL = true`

## Verification

- [x] Migration applied; codes seeded
- [x] `dotnet build` + CourtCivil unit tests (32+)
- [x] UI `npm run build`
- [ ] Manual smoke: create → parties → status → prints / groups / recent

## Out of scope (unchanged)

Civil Process integration, writs, e-filing, fee accounting, case-type-specific engines, advanced docket.
