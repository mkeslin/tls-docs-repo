# Behavior contract flywheel

**Document type:** Reference (engineering + docs convention)  
**Status:** Adopted for new work; apply opportunistically to existing pages/tests  
**Audience:** Internal — engineers, docs authors, Cursor agents

This page defines how **product code**, **automated tests**, and **GitBook** (customer + internal) stay aligned. It is the agreement only — not a tooling project.

## Three rules

1. **Code is runtime truth.** What the shipped API and UI do is authoritative. When docs, tests, and code disagree, trust the running product, then fix the lagging artifact (or change the code if the doc was an intentional product decision).
2. **Shared scenario ids.** Name a behavior once and reuse that id across test titles/annotations, customer doc sections, docs-screenshot shot ids, and (when useful) internal notes. Prefer kebab-case: `court-preplea-enter-plea-cancel`.
3. **Put assertions in the right layer** (testing diamond — fat middle, thin e2e tip):

| Layer | Asserts | Lives in | Persistence |
|-------|---------|----------|-------------|
| API unit | Pure rules, mappers, serializers, edge cases | `ThinLine.API.UnitTests` | **Mocks and/or EF InMemory** |
| API integration | Persist / enforce / contract through API + DB | `ThinLine.API.IntegrationTests` | **Real SQL via Docker/Testcontainers** |
| UI unit (Vitest) | Component/composable logic without a full browser | `ThinLine.UI` Vitest | N/A |
| Playwright e2e | Journeys: shell, navigation, dialogs open/Cancel | `ThinLine.UI/tests/e2e` | Canary (non-destructive) |
| Docs screenshots | Visual match for customer Help (not business rules) | `ThinLine.UI/tests/docs-screenshots` | Seeded demo data |
| Customer GitBook | Human-facing happy path | `tls-docs-repo/customer/` | N/A |
| Internal GitBook | Seeds, agency setup, ops edges, “why” | `tls-docs-repo/internal/` | N/A |

Do **not** re-prove fee math or state-machine tables in Playwright. Do **not** use customer Help as the only lock on a rule — add a test.

### Persistence split (API)

- **Unit:** mocks / EF InMemory — keep the PR gate fast; never treat InMemory as SQL Server truth.
- **Integration (`MsSqlIntegration`):** Docker/Testcontainers SQL Server — the fat middle of the diamond. Do not add InMemory hosts for new HTTP integration facts. LocalDB is an optional Windows escape hatch only.
- **Scoped runnable recipes** (repo root): `npm run api:test:itest:court`, `api:test:itest:court-accounting`, `api:test:itest:collections`, or `api:test:itest:scoped`. Details: product-repo `ThinLine.API/ThinLine.API.IntegrationTests/README.md`.

## Flywheel

```text
Code (runtime) ──validates──► Tests (must stay true)
       ▲                            │
       │                            │ same scenario language
       │                            ▼
       └──────── gaps / intent ◄── Docs (what humans are told)
```

- **New work:** intent may start in a backlog plan or doc; ship code + tests; update customer/internal docs in the same release train when user-facing.
- **After ship:** code wins; docs and tests catch up, or code changes if product intent changed.

## Scenario id conventions

| Place | How to use the id |
|-------|-------------------|
| Playwright test | `test('court-preplea-enter-plea-cancel: …')` or `test.info().annotations` `{ type: 'scenario', description: '…' }` |
| Docs screenshot | Shot id in `manifest.ts` / capture file matches or prefixes the scenario |
| Customer markdown | Heading or HTML comment near the section: `<!-- scenario: court-preplea-enter-plea-cancel -->` |
| Internal note | Same id in a short “Scenarios” list (seeds, agency, Cancel-only caveats) |
| API test | Method or trait/category name includes the id when it locks the same behavior |

One scenario can map to **multiple** test layers (e.g. API integration for persist + Playwright for dialog Cancel). That is expected.

## Audience split

| Space | Include | Exclude |
|-------|---------|---------|
| **Customer** (`customer/`) | Steps a clerk/officer follows; screenshots; field labels users see | Seeds, Descope, canary, test ids, internal agency ids |
| **Internal** (`internal/`) | DOCSCV seeds, agency **10003**, Cancel-only on canary, support edges | Copy-paste of entire customer tutorials |

## Canary vs local (UI e2e)

- **Canary Playwright (default):** non-destructive journeys (open menus/dialogs → **Cancel**, no Save that mutates shared data).
- **Local / writable fixture:** future home for mutation e2e; until then, prefer **API integration** for commits that change persisted state.

See product-repo `ThinLine.UI/tests/e2e/README.md` and `tests/docs-screenshots/README.md`.

## When behavior changes

| Change | Update |
|--------|--------|
| API/UI behavior | Tests in the same PR (per product-repo `AGENTS.md`); customer/internal docs when user-facing or support-facing |
| Doc-only clarification | No code; add a test only if the doc asserted something never locked in |
| Screenshot drift | Re-run docs screenshots; review PII before committing assets |

Release notes and GitBook gates for a cut still follow product-repo `Docs/RELEASE-FINALIZATION.md`.

## What this is not

- Not a requirement to backfill every existing page with scenario ids in one pass.
- Not permission to grow a large Playwright suite that duplicates API tests.
- Not a generator that writes Help from code automatically (optional later).

## Related

- Product monorepo quickstart / test commands: `Thin Line Software` → `AGENTS.md`
- UI e2e: `ThinLine.UI/tests/e2e/README.md`
- Docs screenshots: `ThinLine.UI/tests/docs-screenshots/README.md`
- Finalize release (docs + tests): product monorepo `Docs/RELEASE-FINALIZATION.md`
- **Pilot (court PRE-PLEA):** [scenarios/court-preplea-pilot.md](scenarios/court-preplea-pilot.md) — scenario map across customer docs, API tests, and Playwright
- **Gap analysis (Court / Accounting / Collections P0):** [scenarios/gap-analysis-court-accounting-collections.md](scenarios/gap-analysis-court-accounting-collections.md)
