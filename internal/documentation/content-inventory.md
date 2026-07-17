# Content inventory

**Repository:** `tls-docs-repo`  
**Phase:** 1 — Audit only  
**Date:** 2026-07-16 (note added 2026-07-17)  
**Related:** [repository-alignment-plan.md](repository-alignment-plan.md)

## Near-term scope note (2026-07-17)

- **`release-notes/`** — Do not move, rename, or reorganize (application-consumed). Inventory rows below remain for reference only.
- **`guide/`** — Do not reorganize yet. New external training/support content is authored under `customer/`.
- **`internal/`** and **`customer/`** — Foundational skeletons added; fill with real process and training content over time.

## Legend

| Field | Meaning |
|-------|---------|
| **Type** | Policy, SOP, Guide, Checklist, Template, Reference, Config, Meta |
| **Audience** | `customer` (end users), `customer-admin`, `internal`, `public` |
| **Action** | Keep, Revise, Merge, Archive, Remove |
| **Future location** | Target path after Phase 2 reorganization |

---

## Configuration and navigation manifests

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/guide.json` | Config | customer | `customer/guide.json` (or keep at legacy path during transition) | Revise | Authoritative in-app Help nav. Must stay compatible with `ThinLine.UI` `versionHelper.ts` until UI is updated. Several children point to empty pages. |
| `release-notes/release-notes.json` | Config | customer | `customer/release-notes/release-notes.json` | Revise | Same runtime dependency as guide.json. Structure is sound. |

---

## GitBook (`gitbook/`)

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `gitbook/README.md` | Meta | public | Root `README.md` or `customer/README.md` | Remove | GitBook onboarding template ("Developer Platform", sample API, Discord). Not Thin Line content. Replace entirely. |
| `gitbook/SUMMARY.md` | Config | public | Root `SUMMARY.md` | Remove | Single entry to template README. Replace with full IA from alignment plan. |
| `gitbook/.gitbook/assets/*.jpg` | Reference | — | Archive or delete | Remove | Stock GitBook template images (no-code, hosted, api-reference). |

---

## User guide (`guide/`)

Folder convention: `guide/<label>/<label>.md` + co-located images. Loaded by label from `guide.json`.

### Welcome and general system

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/getstarted/getstarted.md` | Guide | customer | `customer/getting-started/getstarted.md` | Revise | Useful: contact info, ScreenConnect remote assistance, login/logout, YouTube walkthrough. Typos (*inforamtion*, *quaracters*, *instal*). Verify contacts and hours still accurate. |
| `guide/navigating_application/navigating_application.md` | Guide | customer | `customer/getting-started/navigating-application.md` | Revise | Strong module map and shell overview. Heading typo `# ## Application Shells`. Long; consider splitting master-record section to `customer/rms/master-records/`. |
| `guide/navigating_browser/navigating_browser.md` | Guide | customer | `customer/getting-started/managing-browser.md` | Keep | Browser bookmarks, tabs, desktop shortcuts. Good support-adjacent content. |
| `guide/system_reporting/system_reporting.md` | Guide | customer | `customer/rms/reporting.md` | Revise | Solid reporting guide (detail, grid, batch). Typos (*seperatley*, *deatil*, *recomended*). Cross-module — link from CAD and RMS indexes. |
| `guide/faq/faq.md` | Guide | customer | `customer/getting-started/faq.md` | Revise | 4 Q&As; footer says more coming. Claims report history retention (3 years) and role names — verify before publishing updates. |
| `guide/troubleshooting/troubleshooting.md` | Guide | customer | `customer/getting-started/troubleshooting.md` | Keep | Login and spinner issues; clock sync requirement. Short and practical. |

### CAD

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/cad_overview/cad_overview.md` | Guide | customer | `customer/cad/overview.md` | Keep | Video + layout diagram. |
| `guide/cad_units/cad_units.md` | Guide | customer | `customer/cad/units.md` | Keep | Unit status, offline, maintenance. |
| `guide/cad_calls/cad_calls.md` | Guide | customer | `customer/cad/calls-for-service.md` | Revise | Core dispatcher workflow. Shares 9 images with self-dispatch folder. |
| `guide/cad_searchinglogs/cad_searchinglogs.md` | Guide | customer | `customer/cad/searching-logs.md` | Keep | Call search, unit logs, batch print. |
| `guide/cad_selfdispatch/cad_selfdispatch.md` | Guide | customer | `customer/cad/self-dispatch.md` | Merge | Overlaps `cad_calls` procedures. Consider merge with cross-links or shared partial; dedupe images on migration. |

### Administration

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/admin_overview/admin_overview.md` | Guide | customer-admin | `customer/rms/administration/overview.md` | Keep | Entry point to admin cog and sections. |
| `guide/admin_agency/admin_agency.md` | Guide | customer-admin | `customer/rms/administration/agency-settings.md` | Keep | Agency details, modules, locations, security. Duplicates images used in audit history. |
| `guide/admin_codes/admin_codes.md` | Guide | customer-admin | `customer/rms/administration/codes.md` | Keep | Code table management. |
| `guide/admin_offenses/admin_offenses.md` | Guide | customer-admin | `customer/rms/administration/offenses.md` | Keep | Offense table management. |
| `guide/admin_users/admin_users.md` | Guide | customer-admin | `customer/rms/administration/users.md` | Keep | Users, roles, claims, password reset. |
| `guide/admin_officers/admin_officers.md` | Guide | customer-admin | `customer/rms/administration/officers.md` | Keep | Officer records and photos. |
| `guide/admin_cad/admin_cad.md` | Guide | customer-admin | `customer/rms/administration/cad.md` | Keep | CAD agencies and units admin. |
| `guide/admin_audit_history/admin_audit_history.md` | Guide | customer-admin | `customer/rms/administration/audit-history.md` | Merge | Likely overlaps agency admin screenshots. Review scope vs. `admin_agency`; merge or clarify distinction. |

### Master records

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/master_overview/master_overview.md` | Guide | customer | `customer/rms/master-records/overview.md` | Revise | Partial. Vehicles, property, locations marked *coming soon*. Overlaps navigating_application master section. |
| `guide/master_persons/master_persons.md` | Guide | customer | `customer/rms/master-records/persons.md` | Revise | **Broken:** same image repeated 14 times; test anchor header at bottom. High priority fix or hide in guide.json. |
| `guide/master_organizations/master_organizations.md` | Guide | customer | `customer/rms/master-records/organizations.md` | Revise | **Stub:** three lines, no procedures or images. Hide or author before customer sees it. |

### Incidents

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/incidents_overview/incidents_overview.md` | Guide | customer | `customer/rms/incidents/overview.md` | Revise | Placeholder `***Comming Soon***`. Hide or author. |
| `guide/incidents_workflow/incidents_workflow.md` | Guide | customer | `customer/rms/incidents/workflow.md` | Revise | Placeholder. |
| `guide/incidents_propertyandevidence/incidents_propertyandevidence.md` | Guide | customer | `customer/rms/incidents/property-and-evidence.md` | Revise | Placeholder. |
| `guide/incidents_cadintegration/incidents_cadintegration.md` | Guide | customer | `customer/rms/incidents/cad-integration.md` | Revise | Placeholder. |
| `guide/incidents_pcaffidavit/incidents_pcaffidavit.md` | Guide | customer | `customer/rms/incidents/pc-affidavit.md` | Keep | Only substantive incidents page. Arrest affidavit workflow with screenshots. |

### Citations

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/citations_overview/citations_overview.md` | Guide | customer | `customer/rms/citations/overview.md` | Revise | Placeholder. Entire citations section empty in Help. |
| `guide/citations_workflow/citations_workflow.md` | Guide | customer | `customer/rms/citations/workflow.md` | Revise | Placeholder. |
| `guide/citations_racialprofiling/citations_racialprofiling.md` | Guide | customer | `customer/rms/citations/racial-profiling.md` | Revise | Placeholder. |
| `guide/citations_mobile/citations_mobile.md` | Guide | customer | `customer/rms/citations/mobile.md` | Revise | Placeholder. Release notes have mobile citation imagery elsewhere. |
| `guide/citations_towarrant/citations_towarrant.md` | Guide | customer | `customer/rms/citations/to-warrant.md` | Revise | Placeholder. |
| `guide/citations_toincident/citations_toincident.md` | Guide | customer | `customer/rms/citations/to-incident.md` | Revise | Placeholder. |

### Notepads

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/notepads_overview/notepads_overview.md` | Guide | customer | `customer/rms/notepads/overview.md` | Keep | Field contact, lost and found, note types. |
| `guide/notepads_workflow/notepads_workflow.md` | Guide | customer | `customer/rms/notepads/workflow.md` | Revise | Draft/completed states. Typos (*if* → *is*). |
| `guide/notepads_searchviewaddedit/notepads_searchviewaddedit.md` | Guide | customer | `customer/rms/notepads/search-view-add-edit.md` | Keep | Operational how-to. |
| `guide/notepads_connections/notepads_connections.md` | Guide | customer | `customer/rms/notepads/connections.md` | Keep | Master record connections. |

### Close patrols

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/closepatrols_overview/closepatrols_overview.md` | Guide | customer | `customer/rms/close-patrols/overview.md` | Keep | Overview video. |
| `guide/closepatrols_searchviewaddedit/closepatrols_searchviewaddedit.md` | Guide | customer | `customer/rms/close-patrols/search-view-add-edit.md` | Keep | Full search and edit workflow. |

### Warrants

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/warrants_overview/warrants_overview.md` | Guide | customer | `customer/rms/warrants/overview.md` | Keep | Module intro and menu access. |
| `guide/warrants_searchviewaddedit/warrants_searchviewaddedit.md` | Guide | customer | `customer/rms/warrants/search-view-add-edit.md` | Keep | Search, add, edit workflow. |

### Evidence

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/evidence_overview/evidence_overview.md` | Guide | customer | `customer/rms/evidence/overview.md` | Revise | Placeholder. |
| `guide/evidence_chainofcustody/evidence_chainofcustody.md` | Guide | customer | `customer/rms/evidence/chain-of-custody.md` | Revise | Placeholder. |

### IBRS

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `guide/ibrs_errors/ibrs_errors.md` | Reference | customer | `customer/rms/ibrs/errors-and-warnings.md` | Keep | Large NIBRS v2019.2.1 error/warning tables with TLS-specific notes on select codes. High value; maintain when NIBRS rules change. **Decision needed:** customer vs. internal-only sections. |

---

## Release notes (`release-notes/`)

### Manifest

| Current path | Type | Audience | Future location | Action | Notes and risks |
|--------------|------|----------|-----------------|--------|-----------------|
| `release-notes/release-notes.json` | Config | customer | `customer/release-notes/release-notes.json` | Keep | Groups versions 0.x through 6.x. Some intermediate versions exist on disk but not in JSON (see below). |

### Version pages (67 folders)

Each version follows: `release-notes/<label>/<label>.md` + optional images.

| Action | Notes and risks |
|--------|-----------------|
| **Keep** (bulk) | Historical customer-facing changelog. Do not delete without archival policy. |
| **Revise** (ongoing) | New releases should follow established markdown format. Recent files (v6.x) include jail, court, and incident content not covered in user guides. |
| **Future location** | `customer/release-notes/<label>/<label>.md` |

#### Versions on disk

| Label | In `release-notes.json` | Action | Notes |
|-------|-------------------------|--------|-------|
| `v_0_001_01` – `v_0_007_01` | Partial (not all early versions listed) | Keep | Early history; low traffic |
| `v_1_010_01` – `v_1_012_01` | Partial | Keep | |
| `v_2_0_0` – `v_2_16_0` | Partial | Keep | |
| `v_3_0_0` – `v_3_14_0` | Partial | Keep | |
| `v_4_0_0` – `v_4_4_0` | Yes (v4.x group) | Keep | |
| `v_5_0_0` – `v_5_8_0` | Yes (v5.x group) | Keep | |
| `v_6_0_0` – `v_6_4_0` | Yes (v6.x group) | Keep | `v_6_4_0` documents 6.4.0 and 6.4.1; aligns with `versionHelper.currentVersion` `6.4.3` — **verify latest release note exists** |

#### Versions present on disk but not in navigation JSON

These folders exist; confirm whether they should be added to `release-notes.json` or archived:

`v_0_001_01`, `v_0_001_02`, `v_0_002_01`, `v_0_004_01`, `v_0_006_01`, `v_0_007_01`, and other early versions not listed under JSON children — **Decision needed:** expose full history in UI or keep JSON curated.

#### Duplicate images across release-note versions

`CallSheetReport.png`, `EditNote1.png`, `EditNote2.png`, `UnitStandby.png`, `NewIcons.png`, `ShowPassword.png`, `CitationMobileSample.png` appear in multiple version folders. **Keep** for historical accuracy unless storage or publish size becomes an issue.

---

## Missing pages (no source file today)

These are required by the target IA but have no equivalent in the repository.

| Proposed path | Type | Audience | Action | Notes |
|---------------|------|----------|--------|-------|
| `README.md` (root) | Meta | internal + customer | Create | Repo landing page |
| `SUMMARY.md` (root) | Config | — | Create | GitBook navigation |
| `internal/strategy/*` | Policy / Reference | internal | Create | Seed from approved brief |
| `internal/operating-system/**` | Guide / Reference | internal | Create | Value stream stages |
| `internal/sops/**` | SOP | internal | Create | All stages |
| `internal/implementation/**` | Guide | internal | Create | |
| `internal/customer-success/**` | Guide | internal | Create | |
| `internal/product/**` | Reference | internal | Create | Link to monorepo docs |
| `internal/technical/**` | Reference | internal | Create | Azure, DevOps, Bicep |
| `internal/policies/**` | Policy | internal | Create | |
| `internal/checklists/**` | Checklist | internal | Create | |
| `internal/templates/**` | Template | internal | Create | |
| `customer/README.md` | Meta | customer | Create | |
| `customer/court/**` | Guide | customer | Create | No court guides exist |
| `customer/jail/**` | Guide | customer | Create | JLM content only in release notes |

---

## Summary statistics

| Category | Count | Keep | Revise | Merge | Remove | Create |
|----------|------:|-----:|-------:|------:|-------:|-------:|
| Guide pages | 44 | 22 | 20 | 2 | 0 | 0 |
| Release note pages | 67 | 67 | ongoing | 0 | 0 | 0 |
| Config / JSON | 2 | 0 | 2 | 0 | 0 | 0 |
| GitBook template | 2 + assets | 0 | 0 | 0 | 2+ | 0 |
| Internal (target) | 0 | 0 | 0 | 0 | 0 | 40+ |
| Customer gaps (court, jail) | 0 | 0 | 0 | 0 | 0 | 2+ modules |

### Highest-risk items

1. **`guide/master_persons/master_persons.md`** — broken content visible to customers.
2. **Twelve placeholder guide pages** — navigation promises missing content.
3. **Legacy path dependency** — `ThinLine.UI` hardcodes `guide/` and `release-notes/` paths.
4. **GitBook template** — public-facing sync may show non-TLS boilerplate if published as-is.
5. **No internal documentation** — delivery and sales processes exist only as tribal knowledge.

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-16 | Phase 1 initial inventory |
