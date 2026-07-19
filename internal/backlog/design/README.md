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

## Current design docs

| Document | Topic |
|----------|--------|
| [Patrol officer command center](patrol-officer-command-center.md) | Officer Patrol dashboard and use cases |
| [Investigation interface](investigation-interface.md) | Investigation command center |
| [Supervisor command center](supervisor-command-center.md) | Supervisor command center |
| [Data integrity interface](data-integrity-interface.md) | Data integrity command center |
| [Security command center](security-command-center.md) | CJIS / identity oversight shell |

## How to add a design doc

1. Copy [design-doc-template.md](design-doc-template.md) to `design/<kebab-case-short-title>.md`.
2. Fill goal, context, decisions, and open questions. Mark unknowns with `<mark style="color:red;">**TODO:**</mark>` or `<mark style="color:red;">**Decision needed:**</mark>`.
3. Link related **`BL-###`** rows in [prioritized.md](../prioritized.md) and any [plans](../plans/README.md).
4. Add the page under **Design documents** in root [`SUMMARY.md`](../../../SUMMARY.md) and [`internal/SUMMARY.md`](../../SUMMARY.md).
5. **Do not leave a full duplicate in the product monorepo.** If content was migrated from `Thin Line Software/Docs/Design/`, delete it there (a one-line pointer README is optional).

## No duplication rule

GitBook (this repo) is the **source of truth** for backlog, plans, and durable design. The product monorepo keeps code-adjacent engineering docs (API/UI architecture, CAD audits, release finalization, compliance packets). When you move a design or work-item doc here, **remove the body from the product repo** in the same change set.

## Related engineering docs in the product monorepo

Deep technical audits and module architecture often still live in the product repo (e.g. `Docs/CAD-Architectural-Audit.md`, `ThinLine.API/docs/`, `ThinLine.UI/docs/`). Prefer linking those from a short design doc here when the decision needs an internal GitBook home; do not duplicate large audits unless you are deliberately migrating them.
