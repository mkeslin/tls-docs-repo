---
backlog: "Cases MVP · CAS"
status: done
created: 2026-08-10
---

# Plan: Cases MVP

## Goal

Bare-bones Cases (`CAS`) MVP: standalone case/report root with system Case Number, StatusCode lifecycle (Open / In Progress / Closed), case-type classification, optional location + assigned officer, lightweight involved-people child, thin add → details, and full NEW-RMS-MODULE checklist. No IA/Security-specific logic or cross-module associations.

## Context

- Foundation: [`five-module-foundation-stubs.md`](five-module-foundation-stubs.md)
- Mirror: Civil Process shell + Court Civil party-child pattern
- Checklist: product-repo `Docs/NEW-RMS-MODULE.md`

## Locked decisions

| Topic | Choice |
|-------|--------|
| Identity | System `RecordNumbers` for `CAS` → `CaseNumber` |
| Lifecycle | **StatusCode** (`_CASS`): OPEN / INPR / CLSD |
| Case types | `_CAST`: IA, SEC, ADM, GEN |
| Involved | Child + `_CASR` (SUBJ/WIT/VIC/OTH) |
| Location | Optional `LocationMasterLocationSnapshotId` |
| Assignment | Optional `AssignedOfficerId` |
| Narrative | Root `Narrative` field |
| Cross-module | None (record-grouper chrome only) |

## Status transitions

| From | Allowed to |
|------|------------|
| OPEN | INPR, CLSD |
| INPR | OPEN, CLSD |
| CLSD | — (terminal; stamps `ClosedDateTime`) |

## Delivered

**API** (migration `20260810115904_CasesMvp`, applied to ThinLineRMS):

- Deepened `CaseRecord` + `CaseInvolveds` + codes + RecordNumbers
- Status via domain action; nested involved; CLSD field-edit lock
- Search FilterMode; gridPrint; detail full-pdf; moduleRecordGroups
- Master-merge remaps for location + involved person/org snapshots

**UI:**

- Thin add → details by case number
- Search + print; details General / People / Attachments / History
- Chat|task, favorites, report-lister, module-record-grouper, `useModuleBase('CAS')`
- Soft-launch Admin flag remains on for local

## Verification

- [x] Migration applied; codes + RecordNumbers seeded
- [x] `dotnet build` + CaseRecord unit tests
- [x] UI `npm run build`
- [ ] Manual smoke: create → people → status → prints / recent

## Out of scope (unchanged)

IA allegations/findings, Security client/site, NIBRS, evidence, cross-module links, case-type numbering.
