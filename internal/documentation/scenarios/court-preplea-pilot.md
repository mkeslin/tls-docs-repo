# Pilot: Court PRE-PLEA scenarios

**Document type:** Reference (behavior-contract pilot)  
**Status:** Active pilot  
**Convention:** [Behavior contract flywheel](../behavior-contract-flywheel.md)

Maps one vertical — **PRE-PLEA** court actions — across code, tests, and GitBook using shared **scenario ids**. Prefer extending this table over inventing parallel names.

## Environment notes (internal)

| Item | Value |
|------|--------|
| Canary agency | **THIN LINE MUNICIPAL COURT** (`agencyId` **10003**) |
| Demo seed | Product-repo `Scripts/docs-screenshots/CourtDocsDemoSeed.sql` (`DOCSCV*`) |
| Plea demo case | `DOCSCV05-01` (typical PRE-PLEA / plea dialog captures) |
| UI e2e on canary | **Cancel only** — open dialogs, do not Save |
| Mutations | API integration tests (owned seeds) or future local/writable e2e |

## Scenario map

| Scenario id | Intended behavior | Customer doc | API lock | UI e2e (Cancel) | Screenshot |
|-------------|-------------------|--------------|----------|-----------------|------------|
| `court-preplea-menu` | From PRE-PLEA, action menu includes **Enter plea**, **Modify appearance date**, **Dismiss case** | [Pleas and judgment](../../../customer/court/pleas-and-judgment.md) | Integration: `GetAvailableTransitions_PrePlea_IncludesEnterPlea` | `courtViolation.stateTransitions.spec.ts` | Soft captures under docs-screenshots court packs (optional) |
| `court-preplea-enter-plea-cancel` | Enter plea dialog opens; Cancel leaves case unchanged | [Record a plea…](../../../customer/court/how-tos/record-a-plea-and-judgment.md) (abandon path) | — (no persist) | Playwright | — |
| `court-preplea-enter-plea-nco` | Enter plea **No contest** → `POST_PLEA_PRE_JUDGMENT` | [Pleas and judgment — Enter a plea](../../../customer/court/pleas-and-judgment.md) | Integration: `ExecuteTransition_EnterPlea_NoContest_FromPrePlea_MovesToPostPleaPreJudgment` | — | `court-pleas-judgment.png` (illustrative) |
| `court-preplea-modify-appearance-cancel` | Modify appearance date dialog opens; Cancel | [Calendar and appearances](../../../customer/court/calendar-and-appearances.md) (related) | — | Playwright | — |
| `court-preplea-modify-appearance` | Modify appearance date stays `PRE_PLEA` | Calendar / appearances | Integration: `ExecuteTransition_ModifyAppearanceDate_FromPrePlea_StaysInPrePlea` | — | — |
| `court-preplea-dismiss-case-cancel` | Dismiss case dialog opens; Cancel | [Pleas and judgment — Dismiss](../../../customer/court/pleas-and-judgment.md) | — | Playwright | — |
| `court-preplea-dismiss-case` | Dismiss case from PRE-PLEA → `DISMISSED` | Pleas and judgment — Dismiss | Integration: `ExecuteTransition_DismissCase_FromPrePlea_MovesToDismissed` | — | — |

Unit tests under `CourtViolationStateExecution_Tests` (EnterPlea / DismissCase transition shape) support the same rules; they use Trait `Scenario` where tagged.

## How to open the menu (UI)

On **Court Violations → Violations** search, each result row shows a procedural-state button (e.g. **PRE-PLEA**). Click it for the action menu. Customer Help may say “Pre-plea”; the button label in the product is typically **PRE-PLEA**.

## Product-repo pointers

| Artifact | Path |
|----------|------|
| Playwright | `ThinLine.UI/tests/e2e/courtViolation.stateTransitions.spec.ts` |
| Shared e2e helpers | `ThinLine.UI/tests/e2e/helpers/courtViolationStateTransitions.ts` |
| Integration (UAT core) | `ThinLine.API/.../CourtViolationStateMachine_UatCore_HttpTests.cs` |
| Integration (workflow) | `ThinLine.API/.../CourtViolationStateMachine_Workflow_HttpTests.cs` |
| Unit (transition defs) | `ThinLine.API/.../CourtViolationStateExecution_Tests.cs` |
| Docs demo seed | `Scripts/docs-screenshots/CourtDocsDemoSeed.sql` |

## Gaps (intentional for this pilot)

- No dedicated customer how-to for **Cancel** — covered as a one-line note on the plea how-to.
- No new screenshot required for Cancel journeys.
- Judgment / deferred disposition scenarios are out of scope for this pilot (separate ids later).
