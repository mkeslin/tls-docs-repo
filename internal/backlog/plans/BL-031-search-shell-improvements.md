---
backlog: "BL-031 · UI · Search shell improvements"
status: draft
created: 2026-08-13
---

# Plan: BL-031 — Search shell improvements

## Goal

Give standard RMS search screens a **shared shell** so users can hide/show columns, rearrange columns, use multi-select on most coded filters, and keep a consistent last-opened row highlight. **Grid print** (and a later CSV/Excel export) should represent the **grid as shown**, not a hardcoded full-column dump.

**Done** means the shared contract exists, a **pilot search** uses it end-to-end (columns + highlight + print-follows-grid), and remaining `search-container` screens can adopt it incrementally. CSV/Excel is a last phase, not a blocker for the rest.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) — **BL-031** (P3 — Later). Platform epic; implement when prioritized, not as drive-by module work.
- **Related:**
  - **[BL-015](BL-015-accounting-grid-prints.md)** — Accounting-only *coverage* of PDF grid prints. Keep that item about “does this screen print?” BL-031 is “does print match the visible grid?”
  - **[BL-026](BL-026-align-multivalue-get-query-params.md)** — Prerequisite for turning most filters into multi-select without truncating GET query values.
  - **[BL-021](BL-021-tls-page-shell-classic-layout.md)** — Page chrome (`TlsPage`). Not this work.
- **H2 monthly releases:** Grid-print / search-shell polish stays **parked** unless a live customer forces it (`internal/strategy/2026-h2-monthly-product-releases.md`).
- **Risk / lane:** Feature / UI platform. Touches public search GET shapes when filters become arrays (coordinate with BL-026). Not auth, billing, or EF migrations unless a later persistence choice requires a user-pref table.
- **Product today:**
  - Shell: product-repo `ThinLine.UI/src/components/shared/SearchContainer.vue` (title, record count, print, reset, search, options + results slots).
  - State: product-repo `ThinLine.UI/src/stores/_useSearchBase.ts` (criteria/options in `localStorage`; print is `GET` criteria + sort, not column layout).
  - Columns: per-screen hardcoded `headers` arrays (e.g. `CitationSearchResults.vue`).
  - Print: per-module `*GridModel` + `AddColumn` lists (e.g. `AccountingPaymentReconciliationSearchGridModel`) — independent of the UI headers.
  - Row highlight: local only (court violation work queues / search “last opened”; Call Sheet Search on master). Not a shared control.

## Approach

Do **not** rewrite every search in one pass. Land a shared contract, prove it on a **pilot**, then enroll screens.

**Recommended pilot:** Court Violation search / work-queue grid (already has last-opened highlight and high clerk traffic). Alternate: Citation search if court-violation files are too specialized.

### Phase 0 — Inventory and column contract

1. Inventory `search-container` screens: headers source, filter types (single vs already multi), print wired (`hide-print` / `printSearchResultsAsync`), existing highlight.
2. Define a **column descriptor** shared by UI grid + print + export: stable `key`, title, default visibility, default order, `required` (cannot hide), format hint (date, money, code).
3. Decide persistence for column prefs: start with **`localStorage` keyed like `useSearchBase`** (`${searchKey}-columns`). Agency/user server prefs only if product later wants roam-across-devices.

### Phase 1 — Hide / show columns

1. Column picker in the search chrome (SearchContainer action or results toolbar).
2. Apply visibility to the results table without mutating the canonical header list.
3. Persist per search key. Reset Options restores default visibility (confirm whether Reset also clears filters — today it resets search options; keep that behavior unless product says otherwise).
4. Required columns stay on (identity / primary number at minimum).

### Phase 2 — Arrange columns

1. Reorder via picker list (drag or up/down). Same persisted layout object as Phase 1 (`keys` + `hidden`).
2. Frozen leading column(s) if the grid already pins an identity column — do not invent a second freeze model.
3. **Tradeoff:** picker-only reorder is simpler and keyboard-friendlier than drag-on-header; header drag is nicer for power users but easier to break on dense/responsive tables. Prefer picker first; header drag is optional follow-on.

### Phase 3 — Multi-select filters (depends on BL-026)

1. Default: coded / enum-like filters become multi-select (`tls-code-select` / select `multiple`). Keep **single-value** for dates, free text, record numbers, and true radio/exclusive states.
2. Align API criteria to `List<T>` / repeated query keys per BL-026 before flipping UI filters. Do not add more comma-CSV + `.Split` contracts.
3. Print and search must use the same criteria object (already true today).
4. Option labels stay **ALL UPPERCASE** (code-descriptions rule).

### Phase 4 — Shared row highlight

1. Extract the court-violation / Call Sheet “last opened” pattern into a small composable (id + row class + clear on new search/page/sort).
2. Opt-in per grid (`row-id` getter). Do not force highlight on admin/tool grids.
3. Highlight is **session UI only** — not printed, not exported.

### Phase 5 — Grid print follows the visible grid

1. Print request sends **visible column keys in display order** (plus existing criteria + sort).
2. Reporting `*GridModel` builds columns from that list (or a shared descriptor), not a hardcoded `BuildColumns()` dump.
3. Hidden columns omitted; order matches the UI. Sort and filters stay as executed by search (current BL-015 rule).
4. **Still represent the grid:** same titles/formatters as the table where practical (dates via agency-local report helpers). Do not try to print row chrome (menus, chips-as-widgets, highlight).
5. Pagination: keep today’s meaning — print is the **search result set** (with the usual print-size warning), not only the current page, unless product later wants “what I see on this page.”
6. BL-015 screens that already print keep working; enroll them in the new payload when those modules adopt the column contract.

### Phase 6 — CSV / Excel export (after print-follows-grid)

1. Same column layout + criteria + sort as print. Add an export affordance next to Print in SearchContainer (do not replace PDF).
2. Prefer **CSV first** (no new library; matches existing GL/remittance CSV downloads). Excel (`.xlsx`) only if a customer needs formatted workbooks.
3. Same print-size warning / cap thinking as PDF so huge result sets do not silently dump.

## Files / areas (expected)

- `ThinLine.UI/src/components/shared/SearchContainer.vue` — chrome for columns / export
- `ThinLine.UI/src/stores/_useSearchBase.ts` — optional column-layout persistence hook
- New shared helpers (names TBD): column layout store/composable; row-highlight composable
- Pilot search results + options (likely court violation or citation)
- `ThinLine.UI/src/api/*` print/export methods — pass column keys
- `ThinLine.API` search `gridPrint` (and later export) actions — accept column list
- `ThinLine.Reporting.Engine` `*GridModel` / `ReportGridModel` — dynamic columns
- Docs: product-repo `ThinLine.UI/docs/UI-ARCHITECTURE.md` (search shell); `Docs/NEW-RMS-MODULE.md` §6 when print-follows-grid ships

## Verification

Per slice, from product-repo `AGENTS.md`:

- [ ] UI: `npm run lint` and `npm run build` in `ThinLine.UI`
- [ ] Vitest for column layout (hide/show/order/reset) and highlight clear-on-search
- [ ] When print/export or filter query shapes change: `dotnet build ThinLine.API/ThinLine.Server.slnx` and `dotnet test` on `ThinLine.API.UnitTests` (print model + criteria binding)
- [ ] Manual pilot: hide two columns, reorder one, search, print — PDF matches visible columns/order; reset restores defaults
- [ ] Manual multi-select (Phase 3): two code values + print; no truncated IDs (BL-026)

## Open questions

- **Pilot screen** — Court Violation search vs Citation vs a quieter accounting search?
- **Reset** — does Reset Options also restore column layout, or only filters/paging?
- **Required columns** — which keys are locked per module vs a global “first identity column”?
- **Print scope** — all matching rows (today) vs current page only?
- **Column prefs** — `localStorage` only, or roam via user/agency settings (likely a migration)?
- **Excel** — CSV sufficient for v1, or does a named customer need `.xlsx`?
- **Enrollment** — opt-in per search vs a hard cutover once the contract exists?

## Notes

- Treat this as **one BL with phases**, not five module tickets — otherwise print, export, and headers will drift again.
- Do not expand BL-015 into this epic. New accounting prints can still ship the old full-column PDF until that screen enrolls.
- Action columns / row menus are never printable or exportable.
- Alternative if time is tight: ship Phase 1–2 + 4 on the pilot only, and leave print/export on the current full-column models until a customer asks. Cheaper, but the “PDF looks like my grid” gap stays.