# Mental Health intake: notification rules from section helper text (canonical plan)

**Use this file as the single implementation spec.** It replaces the separate Cursor plan stub for the same feature—everything needed to build and verify is below.

## Goal

Wire **completion validation (API)** and **required-field UX (Vue)** so they match the **instructional text** under each Mental Health step section: pre-screening, suicide risk 1a–1d, questions 2–12, and staff observations 13–16. Users must document the appropriate notifications before **Mark Complete**; the server must reject incomplete notification documentation on `CompleteStepAsync` for `MENTAL_HEALTH`.

## Current gap (why this work exists)

- Captions for **2–12** and **13–16** require supervisor/magistrate (and MH when warranted), but **Q3–Q12** and **Q13–Q15** are largely **not** in `IsSuicideRiskIndicated`, so those “Yes” answers do not trigger existing suicide-risk notification rules.
- **Pre-screening** and **Suicide 1a–1d** copy is not fully reflected in a single place in the plan doc history; this file merges that with the 2–16 work.
- **Signature / Acknowledgment** and other step rules stay as today unless this plan explicitly changes them.

## Source of rules

Validation is driven by the **small text** under each section plus the **fields in that section** (not a separate external spec).

### Section helper text (verbatim from UI)

Source: [`JailIntakeBookingStepMentalHealth.vue`](ThinLine.UI/src/components/modules/jailIntake/details/steps/JailIntakeBookingStepMentalHealth.vue)

**Physical / Medical Pre-Screening**

- *“\* If yes, Notify Medical or Supervisor Immediately”* (under the section title; same line appears beside traumatic brain injury when that answer is Yes.)

**Suicide Risk (1a–1d)**

- *“Place inmate on suicide watch if Yes to 1a-1d or at any time jailer/supervisor believe it is warranted.”*
- *“IF YES TO 1a, 1b, 1c, or 1d BELOW, NOTIFY SUPERVISOR, MAGISTRATE, and MENTAL HEALTH IMMEDIATELY.”*

**Mental Health History (Questions 2–12)**

- *“IF YES to 2-12 BELOW, NOTIFY SUPERVISOR AND MAGISTRATE. Notify Mental Health when warranted.”*

**Staff Observations (13–16)**

- *“IF YES to 13-16 BELOW, NOTIFY SUPERVISOR AND MAGISTRATE. Notify Mental Health when warranted.”*

### How each block maps to implementation

| Block | Intent of the small text | Existing / proposed wiring |
|-------|---------------------------|------------------------------|
| **Pre-Screening** | Any **Yes** → notify **medical or supervisor** immediately (not the same wording as magistrate). | Add predicate `AnyPreScreeningYes` over the pre-screen booleans. When true, require **medical/supervisor follow-up documentation** (e.g. non-empty `MedicalMedicalNotifyEntity` and/or `MedicalSupervisorNotified` + `MedicalSupervisorNotifiedAt`; confirm if a **medical notification datetime** exists or must be added). **Do not** reuse only the 2–16 supervisor/magistrate rule without product sign-off. |
| **Suicide Risk 1a–1d** | **Yes** on 1a–1d → **supervisor, magistrate, mental health immediately**; aligns with suicide watch text. | Covered by [`IsSuicideRiskIndicated`](ThinLine.API/ThinLine.Business.Objects/JailIntake/JailIntakeService.cs) + `GetMentalHealthStepCompletionErrors` suicide branch + conditional UI (`hasSuicideRisk`). Align UI and API (including **1c** `_YNR` **YES** / **REFUSED**, **1a** officer belief). Audit whether **Mental Health notified** must be required whenever the bold text applies. |
| **2–12 and 13–16** | **Yes** → **supervisor and magistrate**; MH when warranted. | `AnyScreeningYes_Questions2Through16` + **notifications-only** branch when **not** already in full suicide-risk workflow (see below). |

## Field inventory (Yes = `true` on booking, except 1c)

| Range | Form fields (booking / API names) |
|-------|-----------------------------------|
| **Pre-Screening** | `medicalSeriousInjury90Days`, `medicalCurrentlyTakingPrescriptionMeds`, `medicalDisabilityChronicIllness`, `medicalAppearsUnderInfluence`, `medicalDrugAlcoholAbuseHistory`, `medicalWithdrawalSymptomsExpected`, `medicalTraumaticBrainInjury` |
| **Suicide 1a–1d** | `medicalOfficerBeliefSuicideRisk` (1a), `medicalExpressedDesireToDie` (1b), `medicalPriorSuicideAttemptCode` (1c — **YES** / **REFUSED** count as risk in API), `medicalFeelingHopeless` (1d) |
| Q2–Q12 | `medicalHearingVoicesPsychosis`, `medicalBeliefMindControl`, `medicalDepressedPriorToArrest`, `medicalPtsdFlashbacks`, `medicalWorriedSomeoneHurt`, `medicalWorriedLoseJobSpouse`, `medicalMentalHealthServicesEver`, `medicalMentalHealthHospitalLastYear`, `medicalKnowDiagnosis`, `medicalDifficultyLearningSchool`, `medicalWeightChange` |
| Q13–Q16 | `medicalSignsOfDepression`, `medicalUnusualBehavior`, `medicalIncoherentDisoriented`, `medicalVisibleSelfHarmMarks` |

## Overlap with existing suicide-risk workflow

[`IsSuicideRiskIndicated`](ThinLine.API/ThinLine.Business.Objects/JailIntake/JailIntakeService.cs) already includes some **2–16**-related flags (e.g. `MedicalHearingVoicesPsychosis`, `MedicalVisibleSelfHarmMarks`) plus many flags **outside** the 2–16 list.

**Important:** Most of **Q3–Q12** and **Q13–Q15** are **not** in `IsSuicideRiskIndicated` today. Those “Yes” answers still need the **supervisor/magistrate** notification path from the section text **without** forcing the full suicide-risk **risk level / actions / notes** workflow unless product adds those flags to `IsSuicideRiskIndicated`.

## Proposed validation shape (API + Vue)

1. **Pre-Screening:** Define `AnyPreScreeningYes`. When true, require medical/supervisor documentation per pre-screen caption (see table). Add `GetMentalHealthStepCompletionErrors` branch + Vue `isFieldRequired` / `fieldClass` parity.
2. **Suicide 1a–1d:** Keep `IsSuicideRiskIndicated` + existing suicide completion rules; audit alignment with `hasSuicideRisk` and optional **MH notified** requirement.
3. **Define** `AnyScreeningYes_Questions2Through16` = logical OR of all **boolean** fields for Q2–Q16 in the inventory table.
4. **`GetMentalHealthStepCompletionErrors`** (after acknowledgment checks):
   - If **`IsSuicideRiskIndicated`** → keep existing suicide-risk rules.
   - Else if **`AnyScreeningYes_Questions2Through16`** → require **supervisor/magistrate** documentation only (same field rules as the suicide branch’s notification checks: `MedicalSupervisorNotified`, `MedicalSupervisorNotifiedAt`, `MedicalMagistrateNotified`, `MedicalMagistrateNotifiedAt`).
   - Optional: “Notify Mental Health when warranted” → `MedicalMentalHealthNotified` + timestamp/entity (product; default non-blocking unless decided).
5. **Vue** ([`JailIntakeBookingStepMentalHealth.vue`](ThinLine.UI/src/components/modules/jailIntake/details/steps/JailIntakeBookingStepMentalHealth.vue)): Mirror predicates; when suicide risk is **false** but `AnyScreeningYes_Questions2Through16` is **true**, show supervisor/magistrate controls in the **Notifications** area (reuse `form` fields; avoid duplicate controls when suicide sub-block is visible).
6. **Tests:** Extend [`JailIntakeService_MentalHealthStep_Tests.cs`](ThinLine.API/ThinLine.API.UnitTests/JailIntake/JailIntakeService_MentalHealthStep_Tests.cs) — pre-screen Yes without documentation; Q3 or Q13 Yes without supervisor/magistrate; positive paths.

## Files to touch

| Area | File |
|------|------|
| API validation | [`JailIntakeService.cs`](ThinLine.API/ThinLine.Business.Objects/JailIntake/JailIntakeService.cs) — `GetMentalHealthStepCompletionErrors`, helpers (`IsSuicideRiskIndicated`, new predicates) |
| UI + client validation | [`JailIntakeBookingStepMentalHealth.vue`](ThinLine.UI/src/components/modules/jailIntake/details/steps/JailIntakeBookingStepMentalHealth.vue) — computeds, `isFieldRequired`, `MENTAL_HEALTH_POTENTIAL_REQUIRED_FIELDS`, conditional Notifications UI |
| Unit tests | [`JailIntakeService_MentalHealthStep_Tests.cs`](ThinLine.API/ThinLine.API.UnitTests/JailIntake/JailIntakeService_MentalHealthStep_Tests.cs) |

## Implementation checklist

- [ ] API: `AnyPreScreeningYes` + completion errors + messages for medical/supervisor documentation.
- [ ] API: `AnyScreeningYes_Questions2Through16` + `else if` branch when not `IsSuicideRiskIndicated`.
- [ ] API: Audit `IsSuicideRiskIndicated` vs 1a–1d and MH notification requirement vs bold text.
- [ ] Vue: `hasSuicideRisk` / computeds aligned with API; `isFieldRequired` / `canCompleteMentalHealth` / `fieldClass`.
- [ ] Vue: Notifications area shows supervisor/magistrate when needed without duplicate controls.
- [ ] Tests: new cases for pre-screen and 2–16 notification branches.
- [ ] Verify: `dotnet test` on `ThinLine.API.UnitTests`; `npm run lint` / `npm run build` on touched UI per [AGENTS.md](AGENTS.md).

## Tradeoffs

- **Pre-screening** names **Medical or Supervisor**, not **Magistrate**—do not reuse only the 2–16 magistrate rule without product approval.
- **One OR over 2–16** matches both section captions; split later if product wants finer rules.
- **Q2 / Q16 Yes** may hit `IsSuicideRiskIndicated` first → full suicide workflow (heavier than notifications-only).
- Stricter **MH notified** on suicide path may block more bookings—confirm with stakeholders.

## Verification commands

```bash
dotnet test ThinLine.API/ThinLine.API.UnitTests/ThinLine.API.UnitTests.csproj --filter "FullyQualifiedName~JailIntakeService_MentalHealthStep"
```

```bash
cd ThinLine.UI && npm run lint && npm run build
```

(Adjust filter if test class name changes; full mental health tests or full suite per team practice.)
