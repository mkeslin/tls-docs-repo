---
backlog: "BL-026 · API / UI · Align multi-value GET query params"
status: draft
created: 2026-08-06
---

# Plan: Align multi-value GET query params

## Goal

Standardize multi-value GET filters on **repeated query keys** bound to `List<T>` / `T[]`, matching what `jsonToQueryString` emits for arrays. Remove reliance on comma-separated `string` + `.Split(',')` for list-of-IDs / multi-select filters.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-026** (P3 — Later).
- **Trigger:** Evidence in/out of custody print truncated selections after `queryStringHelper` began serializing arrays as repeated keys (`1021789fc`, 2026-05-22). Bugfix: UI joins `evidenceIds`; API `EvidenceCriteria` accepts both CSV and repeated keys.
- **Preferred pattern (examples already correct):** master merge (`jsonArrayToQueryString` → `[FromQuery] List<long>`), pinned court violations (`CourtViolationIds` / `CourtViolationNumbers` as `List<>`).
- **Risk / lane:** cleanup / API contract — coordinate any public query-shape changes; not auth/billing.

## Inventory (comma-CSV / string + Split)

### Active UI → API (join or CSV contract)

| Area | UI | API | Notes |
|------|----|-----|--------|
| Evidence in/out of custody print | `ThinLine.UI/src/api/reportApi.ts` — `getEvidenceInCustodyAsync` joins `evidenceIds` | `EvidenceCriteria` in `IncidentReportController.cs` — `string[]` + `ParsedEvidenceIds` still splits commas | **Bug fixed**; still hybrid. Align by dropping UI join and binding `long[]` (or keep dual parse until all callers migrate). |
| Court violation timeline | `courtViolationApi.getTimelineAsync` joins `types` / `subtypes` | `CourtViolationController.GetTimelineAsync` — `[FromQuery] string types/subtypes` + `.Split(',')` | Active; safe today because UI joins. |

### API accepts CSV; UI sends single value today (latent)

| Area | API | Notes |
|------|-----|--------|
| Court violation health search/print | `CourtViolationHealthController` `severity`/`category` → `CourtViolationHealthIssueDataStore` `.Split(',')` | Multi-select without join would truncate. |
| Jail intake booking health | Same shape → `BookingHealthIssueDataStore` | Same. |

### Similar CSV in non-API / out of scope unless desired

| Area | Location | Notes |
|------|----------|--------|
| Court violation calendar schedule types | `CourtViolationCalendar.vue` router query `types=a,b,c` | SPA route, not ThinLine API binder. |
| Stripe webhook IP allowlist | Config CSV | Not a client list-of-IDs GET. |

## Approach

1. For each inventory row: change API to `List`/`T[]` (or keep dual-parse temporarily), update UI to pass arrays through `jsonToQueryString` / `jsonArrayToQueryString` (no `.join(',')`).
2. Add/adjust unit tests for binding/parsing (see `EvidenceCriteria_Tests`).
3. Optional guardrail: comment or lint note on `queryStringHelper` — arrays against `string` FromQuery are unsafe.
4. Do **not** change Stripe config or unrelated domain CSV storage.

## Files / areas (expected)

- `ThinLine.UI/src/api/reportApi.ts`, `courtViolationApi.ts`, health filter criteria if multi-select is added
- `ThinLine.API/.../IncidentReportController.cs` (`EvidenceCriteria`)
- `ThinLine.API/.../CourtViolationController.cs` (timeline)
- `CourtViolationHealthController` / `BookingHealthController` + related data stores
- `ThinLine.API.UnitTests` for criteria parsing

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj` (criteria + related)
- [ ] Manual: evidence multi-select print; timeline type filters; health filters if touched

## Open questions

- Migrate evidence to `long[]` only and remove UI join in the same change, or leave dual-parse until timeline/health land?
- Include calendar router `types` CSV in scope, or leave as SPA-only?

## Notes

- Target pattern: `?ids=1&ids=2` → `[FromQuery] List<long> ids` (or `long[]`).
- Avoid new comma-join call sites when adding multi-select GET filters.
