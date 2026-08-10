---
backlog: "K9 Management MVP · K9M"
status: done
created: 2026-08-10
---

# Plan: K9 Management MVP

## Goal

Bare-bones K9 Management (`K9M`): K9 profile root + Training and Deployment children. No cross-module links, certifications, GPS, or advanced training schemas.

## Context

- Foundation stub: entity `K9Unit`, `tlsapi/k9-units`
- Mirror: Fleet dual nested children + Civil Process event-child + CVP/CAS checklist chrome
- Checklist: product-repo `Docs/NEW-RMS-MODULE.md`

## Locked decisions

| Topic | Choice |
|-------|--------|
| Identity | Numeric PK only — no user-facing record number |
| Status | Code `_K9ST` profile dropdown (not transition engine) |
| Sex | `_K9SX` M / F |
| Handler | Optional `PrimaryHandlerOfficerId` |
| Training / Deployment | Nested children + code types |
| Cross-module | None |

## Delivered

**API** (migration `20260810121428_K9Mvp`, applied to ThinLineRMS):

- Deepened `K9Unit` + `K9Trainings` + `K9Deployments` + codes
- Nested trainings/deployments CRUD; search FilterMode; gridPrint; detail full-pdf
- ModuleRecordGroups on VM; soft-delete children

**UI:**

- Thin add (Name + Status) → details by PK
- Search + print; tabs General / Training / Deployments / Attachments / History
- Chat|task, favorites, report-lister, module-record-grouper, `useModuleBase('K9M')`
- Soft-launch Admin flag remains on

## Verification

- [x] Migration applied; codes seeded
- [x] `dotnet build` + 25 K9Unit tests
- [x] UI `npm run build`
- [ ] Manual Rex workflow

## Out of scope (unchanged)

Certifications, group training, odor/hides, GPS, vet, RMS/CAD links, advanced reports.
