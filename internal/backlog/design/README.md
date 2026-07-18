# Design documents

Longer-lived **product and technical design** for Thin Line Platform. Use this folder when the artifact is more than a single backlog implementation checklist.

## When to use design vs plans

| Use | Folder |
|-----|--------|
| Sprint-ready implementation steps for a **`BL-###`** | [plans/](../plans/README.md) |
| Cross-cutting design, schema/product rules, multi-phase architecture, ADRs | **design/** (here) |

A design doc may spawn several backlog items and plans. Link them both ways.

## Modules in scope

Design docs may cover **any** product area — CAD, Jail, Court, Accounting, RMS, Masters, Security, UI shell, integrations, and shared platform concerns.

## How to add a design doc

1. Copy [design-doc-template.md](design-doc-template.md) to `design/<kebab-case-short-title>.md`.
2. Fill goal, context, decisions, and open questions. Mark unknowns with `<mark style="color:red;">**TODO:**</mark>` or `<mark style="color:red;">**Decision needed:**</mark>`.
3. Link related **`BL-###`** rows in [prioritized.md](../prioritized.md) and any [plans](../plans/README.md).
4. Add the page under **Design documents** in [internal/SUMMARY.md](../../SUMMARY.md).

## Related engineering docs in the product monorepo

Deep technical audits and module architecture often still live in the product repo (e.g. `Docs/CAD-Architectural-Audit.md`, `ThinLine.API/docs/`, `ThinLine.UI/docs/`). Prefer linking those from a short design doc here when the decision needs an internal GitBook home; do not duplicate large audits unless you are deliberately migrating them.
