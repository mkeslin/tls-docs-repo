---
backlog: "BL-### · Module · Work item name"
status: draft
created: YYYY-MM-DD
---

# Plan: [Short title]

## Goal

One or two sentences: what “done” means for this backlog item.

## Context

- **Backlog reference:** [prioritized.md](../prioritized.md) (section / row).
- **Risk / lane:** e.g. feature vs cleanup; note product-repo `AGENTS.md` boundaries if relevant.

## Approach

1. …
2. …

## Files / areas (expected)

- `ThinLine.API/…` (product monorepo)
- `ThinLine.UI/…` (product monorepo)

*(Adjust paths when the plan is written.)*

## Verification

- [ ] `dotnet build …` / `dotnet test …` (per product-repo `AGENTS.md`)
- [ ] UI: `npm run lint` / `npm run build` in `ThinLine.UI` if applicable

## Open questions

- …

## Notes

Optional follow-ups, dependencies, or links to issues/PRs.
