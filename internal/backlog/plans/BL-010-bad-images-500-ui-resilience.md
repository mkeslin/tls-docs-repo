---
backlog: "BL-010 · Data · Bad images causing 500 (ShallowaterPD)"
status: draft
created: 2026-08-19
client: ShallowaterPD
---

# Plan: BL-010 — Bad attachment images must not 500 the UI

## Goal

When ShallowaterPD users open records with **corrupt, missing, mis-typed, or unreadable** attachment images, the UI must **degrade gracefully** (placeholder / skip thumbnail) instead of surfacing an HTTP **500** or breaking the screen. API thumbnail/data endpoints should prefer **controlled responses** over unhandled exceptions where practical.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — P2 / priority 5, client **ShallowaterPD**.
- **CSV note:** “Need to handle 500 error when processing image instead of throwing in UI.”
- **Related:** [BL-019 Shallowater go-live](BL-019-shallowater-municipal-court-golive.md) — image-heavy UAT; keep BL-010 closed before or during go-live if still reproducing.
- **Risk / lane:** Bug fix / resilience — **not** auth, billing, migrations, or public API contract breaks.

## Current state (repo inventory)

### API (partial hardening exists)

- `AttachmentController.GetImageThumbnailDataAsync` — returns **404** for non-`IMG` types; otherwise calls `GetThumbnailStreamAsync`.
- `AttachmentRoot.GetThumbnailStreamAsync` — broken-image fallback, Magick decode failure handling, unit tests in `AttachmentRoot_BadImage_Tests.cs`.
- **Gap:** read retry loop can still **rethrow** after 5 failures (`AttachmentRoot.cs`); `GetImageDataAsync` has less explicit corrupt-file handling than thumbnails.

### UI (inconsistent)

| Component | Pattern |
|-----------|---------|
| `JailIntakeBookingStepPerson.vue` | try/catch thumb → full image → null |
| `PersonEmbedCard.vue` | try/catch → null placeholder |
| `CodeEnforcementTimeline.vue` | try/catch per thumbnail, console.warn |
| `AttachmentLister.vue` | **no catch** on `getImageThumbnailBase64` |
| `ImageGallery.vue` | **no catch** on `getImageBase64` |
| Master embed cards (location, vehicle, property, org) | mostly **no catch** |

`attachmentsApi.getImageThumbnailBase64` / `getImageBase64` propagate API errors via `api.getAsync`.

## Approach

1. **Centralize resilience** in `ThinLine.UI/src/api/attachmentsApi.ts` — safe wrappers that catch HTTP/errors and return `null` (or optional broken-image placeholder data URI if product wants visible “broken” tile).
2. **Adopt safe helpers** in `AttachmentLister.vue`, `ImageGallery.vue`, and master embed cards still missing try/catch; align with `CodeEnforcementTimeline` / jail intake patterns.
3. **API hardening (narrow):** ensure `GetImageThumbnailDataAsync` and `GetImageDataAsync` do not leak 500 for known bad-image paths — return broken-image bytes or **404** with logging; extend `Attachment_WebApi_Tests` and `AttachmentRoot_BadImage_Tests`.
4. **Do not** broaden scope to PDF thumbnails, report pipelines, or attachment upload rewrite.

## Files / areas (expected)

- `ThinLine.API/ThinLine.RMS.WebAPI/Controllers/Common/AttachmentController.cs`
- `ThinLine.API/ThinLine.Business.Objects/Common/Attachments/AttachmentRoot.cs` (only if 500 still escapes)
- `ThinLine.API/ThinLine.API.UnitTests/Common/Attachments/AttachmentRoot_BadImage_Tests.cs`
- `ThinLine.API/ThinLine.API.UnitTests/Attachment/Attachment_WebApi_Tests.cs`
- `ThinLine.UI/src/api/attachmentsApi.ts`
- `ThinLine.UI/src/components/shared/AttachmentLister.vue`
- `ThinLine.UI/src/components/shared/ImageGallery.vue`
- `ThinLine.UI/src/components/masters/*/*EmbedCard.vue` (avatar thumbnail callers)

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj --filter "FullyQualifiedName~Attachment"`
- [ ] `cd ThinLine.UI && npm run lint && npm run build`
- [ ] Manual: open attachment list / image gallery on a record with a known-bad image — page stays usable, placeholder shown

## Open questions

- Should UI show a **generic broken-image icon** vs empty slot? (Default: empty/placeholder consistent with `PersonEmbedCard`.)
- Any Shallowater-specific attachment IDs still reproducing 500 in prod? (Optional: capture one ID for regression test fixture.)

## Notes

- Code Enforcement timeline already filters non-`IMG` timeline attachments to avoid thumbnail API 500s — keep that filter; fix is broader resilience, not CE-only.
