# Codebase size by release

Non-blank lines of code for **ThinLine.API** and **ThinLine.UI** at selected `origin/release/*` branch tips in the Thin Line Software monorepo.

Measured: **2026-07-20** (local clone tip of each remote-tracking branch).

Status: <mark style="color:red;">**Draft**</mark> — major-line releases (`X.0.0`) plus current tip (`6.4.0`). Full `release/**` sweep still deferred.

## Major releases (`X.0.0`)

| Release | Tip date | API | UI | Total (API+UI) |
|---------|----------|-----|----|----------------|
| 2.0.0 | 2020-01-18 | 73,103 | 56,194 | 129,297 |
| 3.0.0 | 2021-02-19 | 112,283 | 77,077 | 189,360 |
| 4.0.0 | 2023-11-29 | 132,486 | 134,878 | 267,364 |
| 5.0.0 | 2024-08-05 | 139,012 | 141,113 | 280,125 |
| 6.0.0 | 2026-03-10 | 235,866 | 188,010 | 423,876 |

### Growth (majors)

| From → to | Total change |
|-----------|--------------|
| 2.0.0 → 3.0.0 | +60,063 (~+46%) |
| 3.0.0 → 4.0.0 | +78,004 (~+41%) |
| 4.0.0 → 5.0.0 | +12,761 (~+5%) |
| 5.0.0 → 6.0.0 | +143,751 (~+51%) |
| 2.0.0 → 6.0.0 | +294,579 (~+228%) |

## Current tip

Most recent major (`6.0.0`) alongside the current tip (`6.4.0`) for in-line comparison.

| Release | Tip date | API | UI | Total (API+UI) |
|---------|----------|-----|----|----------------|
| 6.0.0 | 2026-03-10 | 235,866 | 188,010 | 423,876 |
| 6.4.0 | 2026-07-15 | 437,886 | 320,024 | 757,910 |

| From → to | Total change |
|-----------|--------------|
| 6.0.0 → 6.4.0 | +334,034 (~+79%) |

## Methodology

| Item | Rule |
|------|------|
| Scope | `ThinLine.API` and `ThinLine.UI` only |
| Metric | **Non-blank physical lines** (any line with non-whitespace). Comments are included. |
| API extensions | `.cs`, `.cshtml`, `.razor`, `.sql` |
| UI extensions | `.vue`, `.ts`, `.tsx`, `.js`, `.jsx`, `.css`, `.scss`, `.sass`, `.html` |
| Excluded dirs | `bin`, `obj`, `node_modules`, `dist`, `coverage`, `.vs`, `packages`, `TestResults`, and other common build/cache folders |
| EF migrations | Up/Down migration `.cs` files **are included** in API. `*.Designer.cs` and `*ModelSnapshot.cs` are **excluded** (auto-generated). |
| Tooling | Product monorepo `Scripts/measure-loc-by-release.py` — `git archive` per branch, then a simple line counter |

## Notes

- Branch tips move when a release branch receives commits; re-run the script to refresh.
- Tip dates are the commit date of the branch tip, not necessarily the marketing ship date.
- This is a **volume** metric, not quality or complexity.
- There is no `origin/release/1.0.0` on the remote; majors start at `2.0.0`.

## How to refresh / expand

From the Thin Line Software monorepo:

```bash
git fetch origin "refs/heads/release/*:refs/remotes/origin/release/*"

# Majors + current tip
python Scripts/measure-loc-by-release.py --versions 2.0.0,3.0.0,4.0.0,5.0.0,6.0.0,6.4.0

# All release branches
python Scripts/measure-loc-by-release.py
```

Copy generated Markdown from `Scripts/loc-out/codebase-size-by-release.md` into this page.

## Related

- [Technical](README.md)
- Product monorepo script: `Scripts/measure-loc-by-release.py`
