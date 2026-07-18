---
backlog: "Collections module · vendor-safe portfolio"
status: implemented
created: 2026-07-13
---

# Plan: Collections Module

## Goal

Ship a first-class **Collections** product module (`COL`) so court staff and collections-agency users can work the Tex. CCP 103.0031 lifecycle under least-privilege claims, without granting `CourtViolationAccess` or full `AccountingAccess` to vendors.

## Context

- Pattern: Equipment/Fleet module wiring ([`equipment-fleet-modules.md`](equipment-fleet-modules.md)).
- Risk: auth claims + EF migrations (``AGENTS.md`` (product repo `AGENTS.md`)).

## Approach (delivered)

1. **Claims:** `Rms.Collections.Access` / `Rms.Collections.Modify`; role `COLLECTIONS_VENDOR` (Access only); seed Continuity onto Accounting + CourtViolation.Modify roles.
2. **Agency module:** `Agencies.CollectionsEnabled` (backfill when `CollectionVendorName` set); Admin → Modules toggle; `canAccessCollections` / `canModifyCollections`.
3. **API auth:** Portfolio/remittance history/reports → Collections Access; remittance post/CSV/disbursement mutators → Collections Modify; refer/recall stay on Court Violation claims.
4. **UI:** `/module/collections` with Referred Portfolio, Payment History, Payment Entry/Import, Disbursement Report/Batches, Activity Report; Accounting nav entries removed (redirects kept).
5. **Stay on CV:** Collections card, eligible queue, batch refer.

## Files / areas

- API: `ClaimKeys`, `SystemModules`, Agency flag, Auth migrations, controller `[Authorize]`, unit tests
- UI: `components/modules/collections/`, nav drawers, `routes.ts`, `AdminAgencyModules.vue`

## Verification

- [x] `dotnet test` filter `Collections` (authorize + factory + existing collections tests)
- [ ] UI: `npm run lint` / `npm run build` on touched files
- [ ] Manual: enable module, assign `COLLECTIONS_VENDOR`, confirm portfolio-only access

## Admin steps (vendor user)

1. Enable **Collections** on the court agency (Modules tab), or rely on vendor-name backfill.
2. Create SystemUser for the collections agency contact; authorize to the court agency id(s).
3. Assign role **`COLLECTIONS_VENDOR`** (or claim `Rms.Collections.Access` only).
4. User sees Collections module: Referred Portfolio + Payment History (+ read reports). No Court Violation / Accounting / remittance posting.

## Notes

Controllers remain under Court/Accounting folders; claim surface is Collections. Optional follow-up: relocate to `Controllers/Collections/` and `/tlsapi/collections/...`.
