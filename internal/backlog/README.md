# Backlog & design

Canonical home for **product work items**, **implementation plans**, and **design documents** across Thin Line Platform — CAD, Jail, Court, Accounting, RMS, Security, UI, and everything else.

This section is internal-only. It is the durable place to capture what we will build, how we plan to build it, and longer-lived design decisions.

## What lives here

| Area | Purpose |
|------|---------|
| [Prioritized backlog](prioritized.md) | Stable **`BL-###`** work items, ordered by priority |
| [Plans](plans/README.md) | Implementation plans tied to backlog items (or named epics) |
| [Design documents](design/README.md) | Broader design / ADR-style docs that outlive a single sprint |
| [Feedback](feedback/README.md) | Field / site-visit feedback organized for product follow-up |
| [How we capture work](how-we-capture-work.md) | CSV dumps, IDs, plan workflow, agent conventions |
| [Templates](templates/plan-template.md) | Starters for plans and CSV imports |

## Quick start

1. **Pick work** — Read [prioritized.md](prioritized.md); respect P0 first.
2. **Plan before coding** — Create a plan under [plans/](plans/README.md) (or ask Cursor to create one for a `BL-###`).
3. **Design when the shape is large** — Use [design/](design/README.md) for cross-cutting or multi-phase designs that are not a single implementation checklist.
4. **CSV dumps** — Drop files in the product monorepo `Backlog/raw/`, then process into [prioritized.md](prioritized.md) (see [how we capture work](how-we-capture-work.md)).

## Source of truth (no duplication)

| Lives here (GitBook / this repo) | Stays in product monorepo |
|----------------------------------|---------------------------|
| Prioritized backlog, plans, design docs, feedback notes | `Backlog/raw/` and `Backlog/archive/` (CSV intake only) |
| Customer training and implementation templates under `customer/` | `AGENTS.md`, API/UI architecture, CAD engineering audits, release finalization, compliance packets, migration tool `PROCESS.md` |

When migrating content from the product monorepo into this repo: **delete the full document from the product repo in the same change**. Do not leave parallel full copies or “stub farms” that rot. Optional: one short pointer README in the old folder.

## Related

- Product monorepo agent guide: `AGENTS.md` (Thin Line Software repo)
- Product / module ownership notes: [Product](../product/README.md)
- Customer-facing product guides: [`../../customer/`](../../customer/README.md)
