---
backlog: "BL-014 · Person · Criminal trespass"
status: in-progress
created: 2026-05-12
updated: 2026-05-12
---

> **Implementation status (2026-05-12):** Backend module landed end-to-end —
> entity (`CriminalTrespass`), search object, EF context registration, data
> store + UoW wiring, business object (`CriminalTrespassRoot`) with revoke
> command + auto-numbering via `ModuleNumberHelper`, service, ViewModels +
> mappers + factories, controller (claims `Rms.CriminalTrespass.Access` /
> `.Modify`), DI registration. Constants:
> `SystemModules.CriminalTrespass = "CTP"`, `ClaimKeys.CriminalTrespass*`,
> `CriminalTrespassConstants` (codes + signature dispositions),
> `CriminalTrespassAttachmentLinkedTypeCodes` (mobile + full PDF). UI:
> `MasterTagger.vue` now merges `TRS` notes with `CTP` records under one
> TRESPASSED chip and populates `ACTIVE WARRANT` popover items from
> `MasterPersonCardViewModel.Records` (and now also surfaces the WAR chip
> when only the records prop carries it, so full person-card callers don't
> rely on the legacy `Tags` flag); `PersonCard.vue`, `PersonEmbedCard.vue`,
> and `CadCallSheetPersonCard.vue` pass `records` through. SQL companions
> live under `Scripts/CriminalTrespass/` (view recreate, search view, code
> seeds with extended `_CTPR` revoke list, per-agency `RecordNumbers` row).
> EF migration `20260512184009_CriminalTrespassesAdd` was scaffolded with
> the snapshot updates and embeds every SQL companion (CTP UNION on
> `vw_MasterPersonRecords`, `vw_CriminalTrespassSearch`, code seeds, per-
> agency `RecordNumbers` insert) so a single `dotnet ef database update`
> brings an environment current. Companion auth migration
> `20260512191350_AddCriminalTrespassAuthClaims` (ThinLineAuthorization
> context) inserts `Rms.CriminalTrespass.Access` / `.Modify` into
> `AuthClaims` and grants them to the same roles that already receive
> `Rms.Warrant.Access` / `.Modify` (`LE_OFFICER` + `CE_OFFICER` get both;
> `LE_READONLY` + `CE_READONLY` get Access only — verified against the
> live ThinLineRMS DB on 2026-05-12; court roles intentionally excluded).
> `SecurityValidator` switch cases for `SystemModules.CriminalTrespass`
> were added to both `ValidateModuleAccessClaim` and
> `ValidateModuleModifyClaim` so any generic module-claim path resolves
> the new claims.
>
> Master merge plumbing extended: `MasterPersonDataStore`,
> `MasterLocationDataStore`, and `MasterOrganizationDataStore`
> `UpdateReferencesForMergeAsync` each re-point the matching
> `CriminalTrespass` snapshot FK (`MasterPersonSnapshotId`,
> `MasterLocationSnapshotId`, `ComplainantMasterOrganizationSnapshotId`)
> so CT records survive duplicate-merge operations on subject, premises,
> and complainant org. Three new in-memory merge tests pin each path
> (`MasterMerge_UpdateReferencesForMerge_Tests`).
>
> Full UI module shipped: `criminalTrespassApi`, models
> (`ICriminalTrespass`, `ICriminalTrespassSearch`, `criminalTrespassTabs`),
> stores (`useCriminalTrespassStore`, `useCriminalTrespassSearchStore`),
> nav drawer + nav drawer list, search/options/results, add view, details
> shell + header (with status chip + Revoke action) + tabs (General /
> Attachments / History) + dedicated `CriminalTrespassRevokeDialog`.
> `CriminalTrespassModuleDetails` registered in `BaseModuleDetails`,
> `moduleStore`, and `moduleHelper`; router entries added under
> `/module/criminalTrespass` (kebab alias `/module/criminal-trespass`)
> claim-gated to `Rms.CriminalTrespass.Access` / `.Modify`. Nav launchers
> updated in `modern`, `classic`, `experiment` drawers and `FullscreenNav`,
> all gated on `systemUser.canAccessCriminalTrespass`. Search VM aligned
> with `SearchResultsViewModel<C, R>` so the generic `useSearchBase` works
> without an adapter.
>
> Per-agency feature flag landed (mirrors `WarrantEnabled` /
> `NotepadEnabled`): `Agency.CriminalTrespassEnabled` (default `false` at
> the entity layer + new-agency commit + ThinLineCommon migration
> `20260512194148_AgencyCriminalTrespassEnabled`); plumbed through
> `IAgency`, `AgencyRoot`, `AgencyViewModel` / Mapper / Factory; surfaced
> in `AdminAgencyModules.vue` as a "Criminal Trespass" toggle that also
> owns the per-agency `CTP` `RecordNumbers` row (so admins enable + define
> the prefix in one place). `SystemUserViewModelFactory` now AND-gates
> `CanAccessCriminalTrespass` / `CanModifyCriminalTrespass` on the agency
> flag + the matching claim, so existing agencies stay opt-in even when
> users already hold the claim. `IAgency.ts` mirrors the new field.
>
> Reports landed (server-rendered QuestPDF, no client-side PDF library):
> `CriminalTrespassReportModel` (flattened, code-resolved fields) +
> `CriminalTrespassDetailReportModel` (composite with subject Person,
> premises Location, optional complainant Org, header). Two QuestPDF
> document factories — `CriminalTrespassDetailQuestPdfDocumentFactory`
> (Letter, full layout: Issuance / Premises / Texas-specific notice /
> Complainant / Revocation) and `CriminalTrespassMobileQuestPdfDocumentFactory`
> (4"x6" thermal-friendly receipt: subject, premises, issuance, Texas
> notice, warning text, signature line). Controller
> `CriminalTrespassReportController` (`tlsapi/criminal-trespasses`) exposes
> `GET .../{id}/report/full-pdf` (claim: Access) and
> `GET .../{id}/report/mobile-pdf` (claim: Modify). The mobile endpoint
> persists the rendered PDF via `IAttachmentService.AddAttachmentAsync`
> with linked type `CriminalTrespassAttachmentLinkedTypeCodes.CriminalTrespassMobilePdf`,
> idempotently replacing any prior mobile PDF for the same CT so the
> attachments tab only ever holds the most recent issued copy. Both
> endpoints log to report history via `IReportService.CreateDetailQuestPdfAsync`.
> DI wired in `DIHelper`. UI: `reportApi.getAvailableReports()` registers
> both report keys (`CriminalTrespass_Details_Full`,
> `CriminalTrespass_Mobile_Pdf`) under `moduleId: 'CTP'` /
> `screenId: 'CriminalTrespassDetails'`; `CriminalTrespassDetailsHeader.vue`
> drops in the shared `<report-lister>` and filters the mobile entry out
> for view-only users (since that endpoint also writes an attachment).
>
> Tests: `CriminalTrespass_BusinessObject_Tests` (14 tests, all passing);
> full API unit suite green (2,497 / 2,497); `vitest run` green
> (166 / 166); UI lint clean on touched files; full slnx build clean; UI
> production `vite build` clean.
>
> Live-DB verification (2026-05-13): all three migrations applied
> successfully against ThinLineRMS — `CriminalTrespassesAdd` initially
> failed on two stale references that surfaced only at view-creation time
> and were corrected in place (no follow-up migration needed because the
> migration had not been recorded; EF rolled the txn back cleanly):
> (1) `vw_CriminalTrespassSearch` was using
> `mls.AddressDescription` which doesn't exist on `MasterLocationSnapshots`
> — replaced with `dbo.fn_LocationDescription(mls.Address1, mls.Address2,
> mls.CityCode, mls.StateCode, mls.ZipCode)`; (2) the `JLI` UNION in the
> `vw_MasterPersonRecords` rebuild had an outdated join that referenced
> `b.MasterPersonId` (removed in
> `20260309214602_RemoveMasterPersonIdFromJailEntities`) — replaced with
> the corrected snapshot-routed join from
> `20260309221630_FixVwMasterPersonRecordsBinding`. Post-apply DB checks
> show: 5 `_CTPS` codes, 5 `_CTPN` codes, 16 `_CTPR` codes, one `CTP`
> `RecordNumbers` row per agency (16 / 16), `vw_CriminalTrespassSearch`
> queryable (0 rows, no CT records yet), `vw_MasterPersonRecords`
> queryable (577 rows, including 18 booking rows via the corrected JLI
> join).
>
> **Remaining follow-ups:** vitest helper that pins the merged TRESPASSED
> computation (extract `getPersonTags` from `MasterTagger.vue` into a pure
> helper); QuestPDF golden-snapshot tests for the two new layouts (the
> reporting engine doesn't have a snapshot harness today, so this is a
> separate scope alongside other report templates).

# Plan: Criminal trespass module

## Goal

Provide **criminal trespass** support at two depths: (**1**) **existing person notes** — code type **`_PNT`** / **`TRS`** (`TRESPASSED`), including agencies that rely on notes **only**, with no structured module—and (**2**) optional **full RMS module** (citation/notepad-class) when an agency adopts it **with full-page + 4-inch mobile** prints.  

**Master person cards** (`master-tagger` on person slides, embeds, search grids): **both** trespass pathways must surface **one** **TRESPASSED** cue using **`tlsIconTrespassed`** (see product-repo `ThinLine.UI/src/components/masters/shared/MasterTagger.vue`), merging **current `TRS` notes** and **active criminal trespass module-derived lines**, with popover **`items`** showing **a few key facts**, not only note text (**[Master person card](#master-person-card-one-trespassed-chip-dual-source)** and **[Companion UX](#companion-ux-actionable-chip-detail-warrants--trespass)**).

The **ACTIVE WARRANT** chip should follow **the same popover richness** (**warrant number**, dates, succinct offense/context from linked records)—see **MasterTagger** / **`Records`** wiring under [Companion UX](#companion-ux-actionable-chip-detail-warrants--trespass).

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-014** (P2); full import description: “Figure out best way to get criminal trespass information on person.”
- **Risk / lane:** New feature touching **data model and API** — plan migrations and review with the team per ``AGENTS.md`` (product repo `AGENTS.md`). Not in the “do not touch” list if migrations are explicitly approved for this work. UI already has a trespass affordance (`tlsIconTrespassed` / `MasterTagger`) that should align with whatever we persist.
- **Legal note (Texas):** Trespass enforcement under Penal Code §30.05 hinges on **notice** (oral, written, signage, etc.). The module should support documenting **how** and **when** notice was given and **which premises** are covered—not only free text.
- **NCIC / protective orders:** Routine criminal trespass warnings are typically **agency-local RMS** records, not CJIS protective-order entries. Treat external interfaces as optional follow-on unless product explicitly requires export to a regional system.
- **Dual-path product:** **`TRS` person notes** remain the lightweight, perpetual option; the **full module** is optional per agency/process. Never require the module for officers to capture trespass—the notes path stays first-class.

## Resolved product decisions

Stakeholder answers below replace prior open questions.

| Topic | Decision |
|-------|-----------|
| **Jurisdiction / fields** | Model **generic** RMS fields usable in any jurisdiction **and** optional **Texas-specific** fields or sections (e.g. PC §30.05–oriented wording/placeholders/help where distinct). UX may hide Texas-only inputs when product rules allow—or show with clear labeling. |
| **Expiration date** | Include an **`ExpirationDate`** (or equivalent **`DateOnly`/`DateTime?`**) on the trespass entity. **`null`/`empty` by default** at create; officers/agencies fill when applicable. Optionally still use agency **`CriminalTrespassExpirationDays`** (if present in schema later) **only as a UI hint/suggested date**, not overwriting explicit null unless product defines that helper. |
| **NCIC / external interfaces** | **Out of scope** for BL-014. |
| **Revocation** | Any principal with **`Rms.CriminalTrespass.Modify`** (or final claim name) may **revoke** an active trespass module record. Persist **revoke reason**: support a **`RevokeReasonCode`** (controlled list, **ALL CAPS** descriptions per code-description rules) plus optional **free-text revoke reason note**. |
| **Agency visibility / sharing** | Match **`MasterPersonRecordObjects` / agency sharing semantics for active warrants**: same filtering and cross-agency display rules officers already see when the **ACTIVE WARRANT** cue is warranted (parity with **`PersonRecordsAsync`** and existing module-record propagation). |
| **Mobile PDF attachment** | After generating **4-inch mobile PDF**, persist as an **attachment** on the trespass record with a **dedicated attachment linked-type constant** analogous to citations’ **`MobileCitationPdf`** (`CitationAttachmentLinkedTypeCodes` — follow that pattern under a trespass-specific name, e.g. **`CriminalTrespassMobilePdf`**). |
| **Module record numbering** | Criminal trespass is a net-new **`SystemModules`** key — register **agency-scoped numbering** following existing LE modules (**`ModuleNumberHelper`** + whatever **seed/config row per agency** the solution uses today for citation/warrant/notepad sequences). Ensure **every agency using the module** has the correct **`ModuleRecordNumbers`** / sequence configuration so prefixes and next-values apply (same operational checklist as onboarding a new module type). |

## Companion UX: actionable chip detail (warrants + trespass)

### Same BL-014 plan vs separate backlog row

| Option | When to use |
|--------|----------------|
| **Keep in BL-014** | The team tackles **popover detail** alongside trespass (**one `MasterTagger` + caller pass** — warrants are the natural first consumer because VM data already exists). |
| **Split backlog ID** | Warrant UX must ship **before** trespass exists, needs its own QA sign-off, or you want KPIs/reporting tracked separately—in that case carve **BL-### “Master chip — warrant popover detail”** and **reference BL-014** only for trespass wording. Either way **match the UX pattern** warrants establish. |

### Today’s behaviour (why this is small on the slide card API)

product-repo `ThinLine.UI/src/components/masters/shared/MasterTagger.vue` sets **`items: []`** for **`WAR`** — an **empty menu body** beside **ACTIVE WARRANT**. **TRESPASSED** chips already populate **`items`** from **`TRS`** note lines.

product-repo `ThinLine.API/ThinLine.RMS.WebAPI/ViewModels/Masters/MasterPerson/MasterPersonCardViewModel.cs` **already exposes** **`Records`** (`List<PersonCardRecordViewModel>` with **`RecordNumber`**, **`Description`**, **`Type`**, **`RecordDate`**, **`ModuleKeyCode`**, **`RecordId`**) populated in product-repo `ThinLine.API/ThinLine.RMS.WebAPI/ViewModels/Masters/MasterPerson/MasterPersonCardViewModelFactory.cs`. product-repo `ThinLine.UI/src/components/masters/person/slideoutCard/PersonCard.vue` does **not** pass **`records`** into **`MasterTagger`** yet.

### Desired outcome

Both **ACTIVE WARRANT** and **TRESPASSED** menus show **several deterministic lines each** (`warrant number`, **issued/date**, shorthand offense/jurisdiction **where available** — matching field choice for trespass summaries). Optionally **deeplink**/open record from chip (reuse **`RecordId`** and **`ModuleKeyCode`**).

### Search grids / lean DTOs

product-repo `ThinLine.UI/src/components/masters/person/PersonCommonSearchResultGrid.vue` binds **`notes` + `tags` only`** — omit detail lines, enrich search rows, or lazy-load summaries on chip open (**product/engineering choice** documented in Approach).

## Master person card: one TRESPASSED chip (dual source)

- **Preserve** product-repo `ThinLine.UI/src/components/masters/shared/MasterTagger.vue` behavior for **`TRS`** (**`tlsIconTrespassed`**, label **TRESPASSED**).
- **Extend** person card plumbing (see product-repo `ThinLine.UI/src/components/masters/person/slideoutCard/PersonCard.vue` — today **`notes`** + **`tags`** only): **also pass **`records`** from product-repo `ThinLine.API/ThinLine.RMS.WebAPI/ViewModels/Masters/MasterPerson/MasterPersonCardViewModel.cs`** (already populated server-side—see **[Companion UX](#companion-ux-actionable-chip-detail-warrants--trespass)**); filter trespass **`SystemModules`** key when implemented. Embed/grid/CAD callers of **`MasterTagger`** adopt the **same enriched props** incrementally.
- **Merge rule:** **`getPersonTags()`** treats **notes + module-derived lines** as **one** trespass badge: show the icon once; **`count`** reflects total distinct cues; popover **`items`** list both **manual/migrated `TRS` note lines** and **module summaries** (e.g. module number + primary location / expiry)—no **second trespass-shaped icon**, no warrant-style **`Tags` string** for trespass unless product later insists.
- **Deduping:** if an agency optionally **mirrors** module state into **`TRS`** notes AND passes module summaries, omit duplicate lines in UI (prefer module line + note-only when no module row).

Tradeoff: merging in the **UI only** avoids duplicate `TRS` rows for badge purposes; optionally still **mirror** summary rows into **`MasterNote`** for **Notes tab parity** — product choice (**[remaining open questions](#open-questions-remaining)**).

## RMS module pattern (conformance with citation / notepad / etc.)

Align implementation with existing LE modules end-to-end—not a one-off screen.

- **`SystemModules`** — add a short module key (e.g. beside `Citation` / `Notepad` / `Warrant`) in product-repo `ThinLine.API/ThinLine.RMS.Common/Constants/SystemModules.cs` and any `Description` map used for labels.
- **Claims** — add **`Rms.CriminalTrespass.Access` / `.Modify`** (or final names) alongside product-repo `ThinLine.API/ThinLine.RMS.Common/Constants/ClaimKeys.cs` patterns for citation/notepad. **Modify** entitlement includes **revoke** (**[Resolved product decisions](#resolved-product-decisions)**).

- **Record numbering — required for each adopting agency:** add trespass **`SystemModules`** **`ModuleRecordNumber`** (or equivalent) configuration **per agency** that uses criminal trespass, same operational pattern as other RMS modules (**`ModuleNumberHelper.GetModuleNumberAsync`**, seeded rows in the project’s module-number tables). Verification: agencies without config cannot receive valid issued numbers—or implement explicit onboarding default.
- **Person association** — trespass rows must appear on the person’s **module record timeline** the way citations and warrants do (backed by **`MasterPersonRecordObjects`** / `MasterPersonDataStore.GetRecordsAsync`). Follow whatever registration path other modules use today when a record is created, updated, superseded, or closed.
- **Data model** — `DbSet`s on `ThinLineContext`, `Register*` in `OnModelCreating`, soft delete + audit + **`IUserEditable`** consistency with product-repo `ThinLine.API/ThinLine.Data.Model/LawEnforcement/Entities/Warrant/Warrant.cs`-style entities.
- **API + UI** — `ThinLine.API` contracts and DTOs, `ThinLine.Business.Objects` service, thin controller + ViewModel factory in `ThinLine.RMS.WebAPI`; UI under **`ThinLine.UI`** `api/`, `models/`, `stores` or composables, router entries consistent with other RMS modules (see product-repo `ThinLine.UI/docs/UI-ARCHITECTURE.md`).

## Reports: full-size agency copy + 4-inch mobile (subject copy)

- **Full-size** — department/records copy: printable report (grid print and/or dedicated PDF—match whatever combination **citation** / other LE modules already use for archival copies).
- **4-inch mobile** — **handout for the trespassed individual**; layout and typography must read clearly on narrow mobile printers. Reuse the **citations mobile PDF** precedent where practical: HTML fragments and/or dedicated mobile template pipeline (see e.g. **`MobileCitationPdf`** in product-repo `ThinLine.API/ThinLine.RMS.Common/Constants/CitationAttachmentLinkedTypeCodes.cs` and related citation mobile request/report code). After generation, **store the PDF as an attachment** with a **new trespass-specific linked-type code** (**[Resolved product decisions](#resolved-product-decisions)**).
 If agency settings gate **print format** (**Print4Inch**/mobile citation parity), mirror that pattern where applicable.

**Product choice to lock in implementation:** one shared report engine with two layouts (full + mobile) vs two separate report definitions; either is fine if output quality and attachment linking are consistent.

## Person note integration (how this relates to “active warrants”)

Research in-repo behavior (important for planning copy and implementation):

| Concern | Active warrants (today) | Person “trespassed” cue (today) |
|--------|-------------------------|----------------------------------|
| **Person record list** | Yes — included in `PersonRecordsAsync` / `MasterPersonRecordObjects` for the module key **`WAR`**. | Criminal trespass module should register the same way once it exists. |
| **Header / tag chip** | **`MasterPerson.Tags`** includes **`WAR`** when an active warrant exists; sync is driven from person records in product-repo `ThinLine.API/ThinLine.Business.Objects/Masters/MasterPersons/MasterPersonTagService.cs`. | product-repo `ThinLine.UI/src/components/masters/shared/MasterTagger.vue` shows **TRESPASSED** from **`MasterNote`** rows with **`masterNoteTypeCode === 'TRS'`** and **`isCurrent`**, not from `Tags`. Code type **`_PNT`** / **`TRS`** is seeded as **TRESPASSED** (`Scripts/2025-01-17 Migrations/20241021133201_MasterNoteTypes.cs`). |

**Recommendation (adjusted for dual-path agencies):**

1. **Two valid modes:** (**a**) **Notes-only** — users maintain **`TRS`** / **`IsCurrent`** on product-repo `ThinLine.API/ThinLine.Data.Model/Masters/Entities/Shared/MasterNote.cs` as today; (**b**) **Full module** — structured records + person-record timeline where enabled.
2. **Person card cue** uses **merged display** (**one** **`tlsIconTrespassed`** chip), not two independent indicators—implement in **`MasterTagger`** + richer person/card payload (**Approach**, below).
3. **Person module timeline** (`MasterPersonRecordObjects`) — trespass rows where an agency adopts the module, same visibility pattern as citations/warrants/notepads.

**Deprecated for this backlog:** implying that every deployment must synchronize automated **`TRS` rows** whenever the module exists. **Optional mirror** (`MasterNote`) remains valid for agencies who want trespass summarized on the Notes tab; others rely on merged tagger logic only.

**Contrast with warrants:** trespass avoids **`MasterPerson.Tags`**; keep **TRESPASSED** keyed off **notes + structured module summaries** surfaced through **`MasterTagger`**, unified under **`TRS`**’s established icon/name.

## Research — information to capture (baseline)

Grouped for schema and UI planning; tighten with agency SOPs.

### Subject (warned party)

- Link to **`MasterPerson` / snapshot** (required for BL-014—avoid orphan tables that cannot tie to a person). Data model accommodates **generic** fields plus **Texas-specific** supplemental fields (**[Resolved product decisions](#resolved-product-decisions)**).

- Acknowledgement / **signature disposition** (signed, refused, not applicable)—many forms record whether the subject signed.

### Premises and scope

- Support **one or many locations** (each as structured address or `MasterLocationSnapshot`); narrative or labels for ambiguous boundaries (“entire plaza,” suite list) when needed.
- Distinguish **officer-issued warning** contexts from **affidavit + posted signage** programs where the department documents owner authorization separately.

### Authority and issuance

- **Issued date/time** and **recording officer**.
- **Complainant / owner / agent:** identity, role, contact; optional **`MasterOrganization`** when the complainant is a business.
- **Notice type:** oral warning, written warning, affidavit/posted-premises program participant, etc. (controlled codes; visible labels per product **uppercase description** rule for code-backed text).
- **Witnesses** (names or narrative) when SOPs require them.

### Lifecycle, linkage, attachments

- **Expiration:** optional **`ExpirationDate`** / **`ExpiresAt`** (**null by default** on new records per product decision). Agencies may optionally use **`CriminalTrespassExpirationDays`** as a **hint** only unless later product rules automate suggestions.
- **Status:** ACTIVE, EXPIRED, REVOKED, SUPERSEDED, VOID—or equivalent code list (**revoked** transitions require **`RevokeReasonCode`** (+ optional revoke note); **modify** claim authorizes revocation — **[Resolved product decisions](#resolved-product-decisions)**).
- **Links:** related **incident / report** number, optional future tie to **citation or arrest**.
- **Narrative** (circumstances, multi-site explanation if one record covers several locations).
- **Attachments:** scanned affidavit, signed warning, signage photos.
- **Officer safety / visibility:** surface active trespass on **person profile** and in aggregations where officers expect **warrants/citations-style** context (e.g. jail intake person records).

### Policy-style documentation (optional fields if your forms require them)

Some departments also track: **officer / owner / subject signatures** (or “refused”); **distribution of copies** (records, owner, subject); **type of notice** in form language matching GOs. Model only what product and legal review require—do not over-build on day one.

## Tradeoffs (storage / UX)

| Approach | Pros | Cons |
|----------|------|------|
| **Dedicated trespass module** | Queryable, expiry/status, multi-location, audit, attachments, reporting | Migrations, API, UI effort |
| **Person notes only (`TRS`)** | No module cost; satisfies many agencies today | Thin structure, weaker print workflow from RMS |
| **Both** module + **`TRS`** (your direction) | Agencies pick depth; unified icon on cards | Requires **explicit merge logic** + optional agency policy for mirroring notes |

**Recommendation:** ship **merged `MasterTagger`** + **`TRS`** forever-supported path; ship **full module** for agencies who need it—not mandatory for **`TRESPASSED`** visibility.

## Repo parallels (patterns to mimic)

- **Warrants:** agency, dates, person snapshot, status/workflow, audit — product-repo `ThinLine.API/ThinLine.Data.Model/LawEnforcement/Entities/Warrant/Warrant.cs`.
- **Close patrol:** requester + **MasterLocationSnapshot** + notes — product-repo `ThinLine.API/ThinLine.Data.Model/LawEnforcement/Entities/ClosePatrols/ClosePatrol.cs`.
- **Person records aggregation (jail intake):** how incidents/citations/warrants are assembled — product-repo `ThinLine.API/ThinLine.RMS.WebAPI/ViewModels/JailIntake/Booking/JailIntakeViewModelFactory.cs` (`GetRecordsByPersonAsync` pattern).
- **Warrant → person tag:** product-repo `ThinLine.API/ThinLine.Business.Objects/Masters/MasterPersons/MasterPersonTagService.cs` — adds/removes **`WAR`** on **`MasterPerson.Tags`** based on active warrant **person records**.
- **UI trespass cue:** product-repo `ThinLine.UI/src/components/masters/shared/MasterTagger.vue`; person cards pass **`notes`** (+ future module summaries). Icon **`tlsIconTrespassed`** in product-repo `ThinLine.UI/src/plugins/vuetify.ts`.

## Approach

1. **Product decision — adoption:** Agencies may use (**a**) **`TRS` notes alone**, (**b**) **full trespass module**, or (**c**) both when the module is enabled. Claims / menu visibility can hide the module where not licensed while **`TRS`** stays available under master person Notes.
2. **Field sketch:** Apply **[Research baseline](#research--information-to-capture-baseline)** bound by **[Resolved product decisions](#resolved-product-decisions)** — generic + TX fields, nullable expiration, revocation reason code + note; add **`ModuleRecordNumbers`** onboarding for each agency adopting the module.
3. **Chip detail parity — warrants + trespass:** Extend **`MasterTagger`**/`getPersonTags` (+ props from product-repo `ThinLine.UI/src/components/masters/person/slideoutCard/PersonCard.vue`, embeds/CAD): (**a**) **ACTIVE WARRANT** badge — populate **`items`** from **`MasterPersonCardViewModel.Records`** (**`PersonCardRecordViewModel`**; warrant module key matches product-repo `ThinLine.API/ThinLine.RMS.Common/Constants/SystemModules.cs`); (**b**) **TRESPASSED** badge — merged **`TRS` notes + trespass-module-derived lines** (**[Master person card](#master-person-card-one-trespassed-chip-dual-source)**).
4. **Person records:** Criminal trespass module registers **`MasterPersonRecordObjects`** on save/lifecycle.

5. **`TRS` mirror (OPTIONAL sync):** If product wants automated Notes-tab parity from the module, upsert **`MasterNote`** rows with **`MasterNoteTypeCode = 'TRS'`** when module state changes — **not required** once **`MasterTagger`** merges module summaries directly; syncing can duplicate **`TRS`** rows if users also edit notes manually unless constrained.

6. **Printing:** (**module path only**) Full + 4-inch mobile; **persist mobile PDF** with dedicated attachment linked type (**_product decision_**); notes-only agencies keep manual forms otherwise.
7. **API layering:** Contracts in `ThinLine.API`, implementation in `ThinLine.Business.Objects`, thin WebAPI + ViewModels/factories per product-repo `ThinLine.API/docs/API-ARCHITECTURE.md`.
8. **UI:** List + detail/edit for the trespass module (when enabled); grid print if standard for LE modules.
9. **Testing:** Domain services (module lifecycle); **Merged tagger** behaviour (manual **`TRS`** lines, trespass-module lines, **`PersonCardRecordViewModel`** warrant **`items`**, multiple active warrants, duplicate suppression); PDF/report smoke tests if citations use comparable coverage.

## Files / areas (expected)

- `ThinLine.API/ThinLine.Data.Model` — entity/ies, enums or code constants as needed
- `ThinLine.API/ThinLine.Data.Store` — `ThinLineContext`, EF configuration, **migration** (explicit team approval)
- `ThinLine.API/ThinLine.API` — `I*` contracts, DTOs
- `ThinLine.API/ThinLine.Business.Objects` — service implementation
- `ThinLine.API/ThinLine.RMS.WebAPI` — controller(s), ViewModels, factory/mapping
- `ThinLine.API/ThinLine.RMS.Common` — `SystemModules` / audit keys; **new trespass mobile-PDF attachment linked-type constants** (`CitationAttachmentLinkedTypeCodes`-style trespass analogue); migration seeds **`ModuleRecordNumber`** (or equivalent) **per trespass-using agency**
- `ThinLine.UI` — routes, views, models, stores/composables, person integration; print actions from module detail
- **UI — `MasterTagger` + callers** — **required enhancement** (`PersonCard.vue`, **`PersonEmbedCard`**, **`PersonCommonSearchResultGrid`**, **`MasterModuleBaseCard`**, **`CadCallSheetPersonCard`** as needed): pass **`records`** (or summaries) — **fills warrant popovers** immediately; merges trespass summaries when trespass **`SystemModules`** key exists (**[Companion UX](#companion-ux-actionable-chip-detail-warrants--trespass)**)
- **`ThinLine.API/ThinLine.Reporting.*` / `ThinLine.Reporting.Engine`** — full and **mobile 4-inch** report templates (follow citation mobile patterns).
- Optional: agency-level toggles for default mobile printer / format (mirror citation **Print4Inch**-style settings if present on `Agency`).

## Verification

- [ ] `dotnet build ThinLine.API/ThinLine.Server.slnx`
- [ ] `dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj` (plus new tests for this feature)
- [ ] `npm run lint` and `npm run build` in `ThinLine.UI` for touched UI

## Open questions (remaining)

- **Popover line format:** deterministic labels/order for warrant vs trespass chip lines (e.g. **WARRANT NUMBER**, **ISSUED**, offense line)—keep UX consistent and scannable.
- **Manual `TRS` + module:** When both exist, **popover dedup** rules and whether **automated `TRS` mirroring** from the module is permitted (see Approach step 5).
- **Merged tagger UX:** Lines **grouped by source** (note vs module) vs **single flattened list**.
- **`CriminalTrespassExpirationDays`:** Confirm column exists on **`Agency`** (or sibling); define whether empty expiration triggers **wizard suggestion only** vs no automation.

## Notes

- Crosby conversion docs mentioned source labels like **CTR** in legacy systems and tables **without person FK**; seeded person note type for trespass-style flags in this product is **`TRS`** (`TRESPASSED`, code type **`_PNT`**). New implementation should **always** link the warned party to **`MasterPerson` (snapshot)** for BL-014 to be satisfied.
- Resolved product decisions (**jurisdiction layering, expiry null default, revocation, visibility, attachments, numbering**) are recorded in **[Resolved product decisions](#resolved-product-decisions)** (dated in frontmatter **`updated`**).
