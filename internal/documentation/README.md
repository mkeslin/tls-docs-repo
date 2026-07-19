# Documentation meta

How this repository is organized and maintained.

## Contents

| Document | Purpose |
|----------|---------|
| [Behavior contract flywheel](behavior-contract-flywheel.md) | Code / tests / GitBook alignment — scenario ids, assertion layers |
| [Pilot: Court PRE-PLEA scenarios](scenarios/court-preplea-pilot.md) | First vertical mapped end-to-end (docs + API + Playwright) |
| [Gap analysis: Court / Accounting / Collections](scenarios/gap-analysis-court-accounting-collections.md) | P0 journey inventory — what docs/tests lock vs missing |
| [Repository alignment plan](repository-alignment-plan.md) | Audit findings, information architecture, migration plan |
| [Content inventory](content-inventory.md) | Inventory of existing pages and recommended actions |

## Near-term scope

- Build and maintain **`internal/`** (company, policies, procedures).
- Build and maintain **`customer/`** (training and support).
- Do **not** reorganize [`release-notes/`](../../release-notes/) (application-consumed).
- Do **not** reorganize [`guide/`](../../guide/) until a later migration is approved.

## Finalize a release

When preparing a product release, the Cursor rule [`.cursor/rules/finalize-release.mdc`](../../.cursor/rules/finalize-release.mdc) applies. Customer release notes (`release-notes/` + `release-notes.json`) and relevant `customer/` / `internal/` updates are **required gates**. Full checklist (tests, version bump): product monorepo `Docs/RELEASE-FINALIZATION.md`.

## Document types

| Type | Meaning |
|------|---------|
| Policy | A governing rule |
| SOP | A repeatable procedure |
| Guide | Explanatory instructions with judgment involved |
| Checklist | Verification steps |
| Template | Reusable starting material |
| Reference | Factual supporting information |

## Outstanding items (red text)

Mark incomplete work so it is visible in GitBook. Use `color:red` (real CSS). Do **not** use `color:$danger` — Git Sync does not resolve that editor token.

```html
<mark style="color:red;">**TODO:**</mark>
<mark style="color:red;">**Decision needed:**</mark>
<mark style="color:red;">**TODO / Decision needed:**</mark>
<mark style="color:red;">Placeholder</mark>
<mark style="color:red;">Draft</mark>
<mark style="color:red;">TBD</mark>
```

Color **only** the marker keyword, not the rest of the sentence or table cell (wrapping trailing text breaks Markdown tables).

Helper script (re-runnable): [`_tools/mark_outstanding.py`](../../_tools/mark_outstanding.py).  
Cursor rule (applies to `*.md`): [`.cursor/rules/outstanding-markers.mdc`](../../.cursor/rules/outstanding-markers.mdc).

## Improvement framework

Evaluate every process in this order:

1. Simplify
2. Standardize
3. Automate
4. Delegate
5. Scale
