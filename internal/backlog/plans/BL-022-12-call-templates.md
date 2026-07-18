---
backlog: "BL-022-12 · CAD · Call templates and quick actions"
status: implemented
created: 2026-06-02
---

# Plan: Call templates and quick actions

## Goal

Agency-configured call templates let dispatchers and officers create calls with preset call-sheet fields. Quick actions are templates flagged for the unit menu and self-dispatch; applying from a unit context assigns that unit as primary.

## Context

- **Backlog reference:** product-repo `Docs/CAD-Architectural-Audit.md` — BL-022-12
- **Product decisions:** Single `CadCallTemplate` entity; `ShowOnUnitMenu` drives quick actions; optional prompts for note/plate/location; busy-unit guard on apply; agency-scoped templates

## Approach (implemented)

1. **Data:** `CadCallTemplate` entity + EF migration `AddCadCallTemplate`
2. **API:** CRUD at `tlsapi/call-templates`; apply at `POST call-templates/{id}/apply` via `CallService.CreateFromTemplateAsync`
3. **Admin UI:** Third tab on product-repo `ThinLine.UI/src/components/admin/AdminCad.vue` and in-CAD product-repo `ThinLine.UI/src/components/cad/CadUnitDialog.vue`
4. **Dispatcher UI:** Split Add Call on product-repo `ThinLine.UI/src/components/cad/CadCallContainer.vue`
5. **Unit / self-dispatch:** Quick templates on product-repo `ThinLine.UI/src/components/cad/CadUnitMenuCard.vue` and product-repo `ThinLine.UI/src/components/mobile/MobileCadUnitCalls.vue`

## Files / areas

- `ThinLine.Data.Model/CAD/Entities/CadCallTemplate.cs`
- `ThinLine.Business.Objects/CAD/CallTemplates/`
- `ThinLine.Business.Objects/CAD/Calls/CallService.cs` — `CreateFromTemplateAsync`
- `ThinLine.RMS.WebAPI/Controllers/CAD/CallTemplateController.cs`
- `ThinLine.UI/src/components/cad/CadCallTemplateAdmin.vue`
- `ThinLine.UI/src/components/cad/CadAddCallSplitButton.vue`

## Verification

- [x] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [x] `dotnet test … --filter "FullyQualifiedName~CallTemplate|FullyQualifiedName~CreateFromTemplate"`
- [x] `npm run build` in `ThinLine.UI`

## Follow-ups

- Wire sandbox `createTrafficStop` command to template apply
- Module tag hints on templates
- `OfficerActionGrid` integration
