# How we capture work

Use this section to maintain a single **prioritized Markdown backlog**, durable **plans**, and **design docs** for humans and Cursor.

## Layout

| Path | Purpose |
|------|---------|
| [prioritized.md](prioritized.md) | **Canonical sorted/prioritized backlog** — each item has a stable **`BL-###`** id |
| [plans/](plans/README.md) | **Implementation plans** — one Markdown file per item when you want a durable plan before coding |
| [design/](design/README.md) | **Design documents** — broader product/technical design that is not only an implementation checklist |
| [feedback/](feedback/README.md) | Field and site-visit feedback |
| [templates/plan-template.md](templates/plan-template.md) | Starter outline for a new plan |
| [templates/backlog-import-template.csv](templates/backlog-import-template.csv) | Suggested columns for Excel / Google Sheets exports |
| Product repo `Backlog/raw/` | **Drop new CSV files** before processing |
| Product repo `Backlog/archive/` | **Preserved copies** of each processed dump (timestamped) |

## Backlog IDs (`BL-###`)

- Assigned in [prioritized.md](prioritized.md): **`BL-001`**, **`BL-002`**, … (zero-padded).
- **Stable:** do not renumber when priority or wording changes; new imports get the next free number.
- Reference in plans (`backlog: "BL-015"`), commits, and PRs.
- Covers **all modules** (CAD, Jail, Court, Accounting, RMS, Security, UI, General, etc.).

## Workflow: create a plan for a backlog item

1. Ask Cursor to **create a plan** for a specific row in [prioritized.md](prioritized.md) (name the module + work item).
2. The agent should write **`internal/backlog/plans/<BL-###-kebab-case-title>.md`** (e.g. `BL-015-accounting-grid-prints.md`), using [templates/plan-template.md](templates/plan-template.md) as a guide (goal, context, approach, verification per product-repo `AGENTS.md`).
3. **Optional:** Add a link under **Active plans** in [prioritized.md](prioritized.md), or a Plan link next to that item.
4. Update plan **`status`** in frontmatter when you move from draft → ready → in-progress → done.

Plans are **not** a substitute for PR review; they are a parking lot for agreed steps and verification.

## Workflow: design document

When the work needs a durable design (multi-module, schema choices, product rules) before or alongside a `BL-###` plan:

1. Copy [design/design-doc-template.md](design/design-doc-template.md) to `design/<kebab-case-title>.md`.
2. Link related backlog IDs and implementation plans.
3. Add the page to [internal/SUMMARY.md](../SUMMARY.md) under **Design documents**.

## CSV format (recommended columns)

Export as **UTF-8 CSV**. Minimum useful columns:

- **Title** — one line per task (required).
- **Notes** — optional context.
- **Area** — e.g. `API`, `UI`, `DB`, `Scripts`, `Clients`, `Infra`, `Docs`.
- **Lane** — e.g. `feature`, `bug`, `cleanup`, `tests`, `data`.
- **Priority** — your rough hint: `P0`, `P1`, `P2`, or blank for the agent to infer.

Extra columns are fine; they will be folded into Notes or preserved in the Markdown table.

## Workflow: process a new dump

1. Save or copy your CSV into the product monorepo **`Backlog/raw/`** (any `*.csv` name).
2. In Cursor, ask to **process the backlog dump** (or `@Backlog/raw/yourfile.csv`).
3. The agent should:
   - **Copy** the file to product-repo `Backlog/archive/` with a name like `YYYY-MM-DD-HHmmss-originalfilename.csv`.
   - **Read** the CSV, dedupe obvious duplicates, merge with context from [prioritized.md](prioritized.md) if you want continuity (user may say “replace” vs “merge”).
   - **Write** [prioritized.md](prioritized.md) with:
     - Sections by priority (**P0 / P1 / P2** or **Now / Next / Later**).
     - Grouping by **Module**, **Area**, and/or **Lane** where helpful.
     - **Blocked / waiting** and **Needs clarification** sections when applicable.
     - A short **Changelog** footer with date and source filename.

Respect product-repo **`AGENTS.md` risk boundaries** when prioritizing (e.g. do not treat `Clients/` conversion work as low-risk cleanup).

## Workflow: “what should I work on?”

Ask in chat. The agent should read [prioritized.md](prioritized.md), respect P0 first, and call out **dependencies** and **verification** (build/test commands from product-repo `AGENTS.md`).

## Product monorepo boundary

The Thin Line Software monorepo keeps **CSV intake only** (`Backlog/raw/`, `Backlog/archive/`). Plans, design docs, and the prioritized backlog are **not** duplicated there. Edit content in this docs repo only. When migrating a document from the monorepo into GitBook, delete the full body from the product repo in the same change.
