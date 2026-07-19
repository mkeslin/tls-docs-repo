# Gap analysis: Jail (Intake, Command Center, JMS) P0



**Document type:** Reference (behavior-contract step 3)  

**Status:** Snapshot — update as scenarios are locked  

**Convention:** [Behavior contract flywheel](../behavior-contract-flywheel.md)  

**Backlog:** [BL-002](../../backlog/plans/BL-002-jail-booking-verify.md) (finish booking), [BL-003](../../backlog/plans/BL-003-jcc-verify.md) (finish command center)  

**Court counterpart:** [Gap analysis: Court / Accounting / Collections](gap-analysis-court-accounting-collections.md)



Inventory of **P0 jail journeys** vs automated locks and GitBook. Legend:



| Cell | Meaning |

|------|---------|

| **YES** | Exists and reasonably locks the journey |

| **PARTIAL** | Related coverage; not scenario-aligned or not the full path |

| **NO** | Missing |



Focus: happy path + critical fail paths for **Jail Intake** and **Jail Command Center** (JLM/JMS). Out of scope here: deep Visitor Log productization, JLM Settings chrome, SignalR scale-out as a separate initiative, and agency-specific print branding polish (covered by BL-002/003 manual checklists).



---



## Priority summary



| Priority | Gap | Why |

|----------|-----|-----|

| **P0** | ~~Any Jail / JLM / JMS HTTP integration~~ | **In progress** — scaffold + `jail-accept-into-custody` + `jail-housing-move` HTTP under `IntegrationTests/Jail/` |

| **P0** | ~~`jail-accept-into-custody` HTTP~~ | **YES** — HTTP IT + existing unit |

| **P0** | ~~`jail-housing-move` unit + HTTP~~ | **YES** — `JlmService_MoveEpisode_Tests` + HTTP IT |

| **P1** | `jail-create-booking` unit + HTTP | Thin create-booking coverage; BL-002 entry point |

| **P1** | `jail-release-from-custody` / `jail-observation-cell-check` HTTP | Strong units; still no HTTP IT |

| **P1** | Flywheel pilot (accept or create→accept) | Same shape as [court PRE-PLEA pilot](court-preplea-pilot.md); no jail scenario map yet |

| **P2** | Playwright Cancel-only on JCC / intake | After API locks; canary non-destructive |

| — | Live SignalR board refresh | Manual / BL-003 checklist; do not replace with brittle e2e |



**Already in good shape:** Customer GitBook for the full intake→floor→release path; **unit** depth on intake steps, accept, release, observation passes, and medication administration; docs-screenshot **surfaces** (command center, intake search/add, locations); BL-002/BL-003 manual QA checklists.



**Headline vs court:** Court already had a deep HTTP state-machine suite before the flywheel; jail’s remaining hole is **breadth** of HTTP IT (create/release/observation), not zero integration coverage.



---



## Jail Intake



| Scenario id | Journey | API unit | API IT | Playwright | Screenshots | Customer docs | Internal scenario map | Notes |

|-------------|---------|----------|--------|------------|-------------|---------------|----------------------|-------|

| `jail-create-booking` | Add Booking wizard → booking created | **PARTIAL** (arrest free-text / start edge only) | **NO** | NO | YES (intake add) | YES — [start-a-booking](../../../customer/jail/start-a-booking.md) | NO | BL-002 entry; thin create coverage |

| `jail-complete-intake-steps` | Mark Complete / defer required steps | YES (per-step services) | **NO** | NO | PARTIAL | YES — [intake-steps](../../../customer/jail/intake-steps.md) | NO | Strongest unit area in jail |

| `jail-accept-into-custody` | Accept → custody episode on board | YES | **YES** | NO | PARTIAL | YES — [accept-into-custody](../../../customer/jail/accept-into-custody.md) | NO | HTTP: `JailIntake_Accept_HttpTests`; facility agency 3 |

| `jail-booking-search` | Find / open bookings in Intake | PARTIAL | **NO** | NO | YES (intake search) | YES — [getting-around](../../../customer/jail/getting-around.md) | NO | Read-mostly |

| `jail-void-delete-draft` | Delete draft before accept | PARTIAL | **NO** | NO | NO | YES (start-a-booking) | NO | Docs warn: don’t delete after accept |



---



## Jail Command Center (JLM) + floor ops



| Scenario id | Journey | API unit | API IT | Playwright | Screenshots | Customer docs | Internal scenario map | Notes |

|-------------|---------|----------|--------|------------|-------------|---------------|----------------------|-------|

| `jail-command-center-board` | Open board / roster vs layout / heartbeat | PARTIAL (reports/flags/tasks) | **NO** | NO | YES | YES — [command-center](../../../customer/jail/command-center.md) | NO | Hub UX; SignalR live updates = manual |

| `jail-housing-move` | Assign / move location (incl. Unassigned) | **YES** (`MoveEpisodeAsync`) | **YES** | NO | YES (JCC surface) | YES — [housing-and-moves](../../../customer/jail/housing-and-moves.md) | NO | Unit + HTTP: assignment persist; inactive → 422 |

| `jail-observation-cell-check` | Start / complete CELL CHECK or SUICIDE CHECK | YES (JMS + JLM pass/cadence) | **NO** | NO | YES (surface) | YES — [observation](../../../customer/jail/observation-and-cell-checks.md) | NO | Strong unit; needs HTTP |

| `jail-log-medication` | Add schedule / log administration | YES (JMS MedicalLog + intake normalize) | **NO** | NO | YES (surface) | YES — [flags-alerts-medication](../../../customer/jail/flags-alerts-medication.md) | NO | |

| `jail-release-from-custody` | Release from Custody wizard | YES | **NO** | NO | YES (surface) | YES — [release](../../../customer/jail/release.md) | NO | Strong unit; HTTP next after accept/move |

| `jail-offsite-transfer` | Transfer out / offsite packet | PARTIAL (draft/complete + report) | **NO** | NO | YES (surface) | YES — [offsite-transfer](../../../customer/jail/offsite-transfer.md) | NO | |

| `jail-manage-locations` | Configure cells / Include in cell checks | PARTIAL (create location) | **NO** | NO | YES | YES — [manage-locations](../../../customer/jail/manage-locations.md) | NO | Admin/setup; prerequisite for floor ops |

| `jail-reports-roster` | Print roster / transfer log / booking PDFs | PARTIAL–YES (report factories) | **NO** | NO | PARTIAL | YES — [reports](../../../customer/jail/reports.md) | NO | Reference; BL-002/003 print rubric |



---



## Layer verdicts



| Layer | Jail Intake | Command Center / JLM | JMS (obs / meds) |

|-------|-------------|----------------------|------------------|

| Customer GitBook | Strong | Strong | Strong |

| API unit | Strong steps/accept/release; thin create | **MoveEpisode** locked; partial board helpers | Strong observation + medication |

| API integration | **Accept HTTP YES** | **Housing-move HTTP YES** | **None** |

| Playwright e2e | None | None | None |

| Docs screenshots | Intake search/add | Command center | Surfaces only (via JCC) |

| Internal scenario maps | None | None | None |

| Manual QA plans | BL-002 checklist | BL-003 checklist | Overlap in both |



---



## How to run existing locks



| Scope | Command |

|-------|---------|

| Jail Intake units | `dotnet test ThinLine.API/ThinLine.API.UnitTests/... --filter "FullyQualifiedName~ThinLine.API.UnitTests.JailIntake"` |

| JLM units | `… --filter "FullyQualifiedName~ThinLine.API.UnitTests.Jlm"` |

| JMS units | `… --filter "FullyQualifiedName~ThinLine.API.UnitTests.Jms"` |

| MoveEpisode units | `… --filter "FullyQualifiedName~JlmService_MoveEpisode"` |

| Jail HTTP IT | `npm run api:test:itest:jail` (Docker) or LocalDB: `--settings ThinLine.API/IntegrationTests.LocalDb.runsettings` + Jail filter |



Policy: **unit = mocks/InMemory**; **new integration = Docker SQL** (LocalDB escape hatch only). See product-repo `ThinLine.API/ThinLine.API.IntegrationTests/README.md` and [behavior-contract-flywheel.md](../behavior-contract-flywheel.md).



---



## Suggested order of work



1. ~~**Scaffold jail `MsSqlIntegration`**~~ — done (`Jail_TestData`, `Jail_SqlProbe`, `Jail_HttpTestBase`, auth profile `JailIntakeReaderAndModify`, agency 3).  

2. ~~**Lock `jail-accept-into-custody` HTTP**~~ — done.  

3. ~~**Lock `jail-housing-move`**~~ — done (unit + HTTP).  

4. **`jail-create-booking` HTTP** (+ thicken create unit) — BL-002 entry; keeps Accept tests from depending on ambient data.  

5. **Flywheel pilot** — pick accept (or create→accept) for scenario ids on customer docs + Traits (court PRE-PLEA template).  

6. **Release + observation HTTP** as capacity allows.  

7. Playwright only for Cancel-only shell journeys after API locks — keep canary non-destructive. Do **not** use Playwright as the primary board-move lock.



---



## Related product paths



| Area | Typical roots |

|------|----------------|

| Jail Intake API / UI | `ThinLine.API/.../JailIntake/`, `ThinLine.UI/.../jailIntake/`, `api/jailIntakeApi.ts` |

| JLM board | `ThinLine.API/.../Jlm/`, `ThinLine.UI/.../jlm/JlmBoardContainer.vue`, `api/jlmApi.ts` |

| JMS observation / meds | `ThinLine.API/.../Jms/`, observation + medical-log controllers |

| Unit tests | `ThinLine.API.UnitTests/JailIntake/`, `Jlm/`, `Jms/` |

| Integration tests | `ThinLine.API.IntegrationTests/Jail/` |

| Docs screenshots | `ThinLine.UI/tests/docs-screenshots/captures/jail-masters-admin.spec.ts` |

| Customer | `customer/jail/` |

| Manual verify | `internal/backlog/plans/BL-002-jail-booking-verify.md`, `BL-003-jcc-verify.md` |


