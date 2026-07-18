---
backlog: "BL-021 · ThinLine.UI · TlsPage shell (Classic layout)"
status: done
created: 2026-05-17
---

# Plan: `TlsPage` shell (Classic layout, Vuetify-backed)

## Goal

Introduce a **single app-owned layout primitive**—**`TlsPage`**—that defines the **stable slots/API** for the main content column used by **Classic layout** today. The first implementation is a **thin wrapper around existing Vuetify markup** (`v-main` region content only) so **visual and behavioral parity** is preserved (no user-visible redesign). This creates the seam where **`wa-page` (Web Awesome)** can replace internals later without rewiring every route.

**Out of scope for this plan:** installing Web Awesome, migrating Modern/Experiment layouts, enabling dormant mobile shells, or replacing leaf controls (tables, pickers, etc.).

## Context

- **Active layout:** product-repo `ThinLine.UI/src/layouts/classic/ClassicLayout.vue` composes drawers, product-repo `ThinLine.UI/src/layouts/classic/NavBar.vue`, product-repo `ThinLine.UI/src/layouts/classic/NavDrawer.vue`, dialogs, and a **`v-main`** region containing banners + product-repo `ThinLine.UI/src/router/`.
- **Root shell:** product-repo `ThinLine.UI/src/App.vue` still wraps **`v-app`** and layout selection; only Classic is in use today.
- **Direction (future):** `TlsPage` will eventually delegate to **`wa-page`**; Vuetify may remain for gaps (per dual-stack strategy) until migrated.
- **Risk / lane:** UI structure only—**no API**, **auth**, **billing**, or **migrations**. Keep diffs easy to review; avoid drive-by refactors in `NavBar`/drawers.
- **Backlog:** [`PRIORITIZED.md`](../prioritized.md) — **BL-021**.

## Approach

### 1. Lock the `TlsPage` public API (app-level, not WA-level)

| Slot | Responsibility |
|------|----------------|
| `default` | Primary page content (**`router-view`**). |
| `banners` | Optional stacked alerts/banners above the scrolling content (today: `security-banner`, `system-notification-banner`). |

### 2. Implement `TlsPage.vue` (Vuetify-backed v1)

- **File:** product-repo `ThinLine.UI/src/components/core/TlsPage.vue`
- **Template:** Multi-root fragment (`banners` slot then default) so slot output stays **direct under `v-main`** (Classic parity with Vuetify `v-main` flex/scroll behavior).
- **`ClassicLayout`** keeps **`v-main`** classes and `router-view` bindings unchanged.

### 3. Wire `ClassicLayout.vue` only

- **`v-main` inner block** uses **`<tls-page>`** with `#banners` and default `router-view`.

### 4. Documentation

- product-repo `ThinLine.UI/docs/UI-ARCHITECTURE.md` — Classic shell + `TlsPage` note.

## Verification

- [x] Visual smoke: Classic app loads; **nav + drawers + main content** unchanged at common breakpoints (manual / dev responsibility).
- [x] Scroll behavior: structure unchanged vs pre-`TlsPage` (no extra wrapper `div`).
- [x] `npm run lint` in `ThinLine.UI`
- [x] `npm run build` in `ThinLine.UI`

## Open questions

- **Resolved for v1:** Slot name **`banners`**; **`v-main`** stays on **`ClassicLayout`**; **`TlsPage`** explicitly imported in `ClassicLayout` (matches nearby `core` imports).

## Notes (follow-ons)

- **Phase 2:** Dev route: `TlsPage` + **`wa-page`** inside, map slots.
- **Phase 3:** Modern/Experiment/mobile as **`TlsPage`** variants after migration.
