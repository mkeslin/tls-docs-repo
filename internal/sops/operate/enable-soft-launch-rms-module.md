# Enable soft-launch RMS module (pilot)

**Document type:** SOP  
**Phase:** Operate · Product updates / Support pilots  
**Status:** v0.1  
**Audience:** Internal — product, engineering, Support  
**Related:** [Publish product update](publish-product-update.md) · product `Docs/NEW-RMS-MODULE.md` · `ThinLine.UI/src/config/adminModuleFeatureFlags.ts`

---

## Purpose

Soft-launch RMS modules ship in the product build but stay **hidden from Admin → Modules** and **off for agencies** until a deliberate pilot. This SOP is the checklist to turn one on for a named agency without treating it as GA.

## Modules in this posture (as of 6.4.9)

| Module | Admin flag | Agency flag (typical) |
|--------|------------|------------------------|
| Criminal Trespass | `ADMIN_MODULES_SHOW_CRIMINAL_TRESPASS` | `CriminalTrespassEnabled` |
| Equipment / Fleet | `ADMIN_MODULES_SHOW_EQUIPMENT_FLEET` | Equipment / Fleet enabled bits |
| Vehicle Custody (`VCS`) | `ADMIN_MODULES_SHOW_VEHICLE_CUSTODY` | `VehicleCustodyEnabled` |
| Civil Process (`CVP`) | `ADMIN_MODULES_SHOW_CIVIL_PROCESS` | `CivilProcessEnabled` |
| Court Civil (`CVC`) | `ADMIN_MODULES_SHOW_COURT_CIVIL` | `CourtCivilEnabled` |
| Cases (`CAS`) | `ADMIN_MODULES_SHOW_CASES` | `CasesEnabled` |
| K9 (`K9M`) | `ADMIN_MODULES_SHOW_K9` | `K9Enabled` |

Default for customer builds: **Admin flags `false`**, agency enabled **`false`**.

## Preconditions

1. Product owner names the **pilot agency**, module, and success criteria.
2. Target environment has applied the module foundation migrations (Auth claims, Common agency flags, ThinLine MVP tables/views).
3. Pilot users have (or will get) the correct **Access/Modify** claims for that module (LE vs court roles as designed).
4. Customer-facing docs for the module are either ready or explicitly waived for the pilot.

## Enablement steps

1. **Build flag (UI):** Set the matching `ADMIN_MODULES_SHOW_*` to `true` in a build destined for that environment (or use an internal/dev build that already has it on). Rebuild UI.
2. **Admin → Modules:** For the pilot agency, enable the module and set numbering if required.
3. **Claims:** Confirm pilot roles include module Access (and Modify if they will edit).
4. **Smoke:** Search → Add → Details → print/report path for that module; attach a file; confirm master Records tab when the module has snapshot FKs.
5. **Support note:** Record agency, module, build/version, and who approved the pilot.

## Do not

- Flip Admin soft-launch flags for **all** customer tenants without product approval.
- Market soft-launch modules as GA in release email or training until product signs off.
- Enable without migrations / claims — nav and saves will fail confusingly.

## Disable / rollback

1. Turn agency module **Enabled** off.
2. Optionally set Admin flag back to `false` on the next build so the Modules row disappears again.
3. Leave data in place unless a separate data-cleanup plan is approved.
