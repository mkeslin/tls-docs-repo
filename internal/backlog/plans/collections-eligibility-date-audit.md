---
title: Texas municipal court collections eligibility — implementation audit
status: audit
created: 2026-08-06
related:
  - court-violation-third-party-collections.md
  - BL-022-collections-supplemental-item-referrals.md (BL-023)
  - collections-module.md
statute: Tex. Code Crim. Proc. Art. 103.0031
---

# Collections eligibility date audit

Audit of existing Thin Line RMS Texas municipal court collections logic versus desired Art. 103.0031-aligned eligibility rules. **No production code was changed** for this audit.

Legend used below:

| Label | Meaning |
| ----- | ------- |
| **Confirmed** | Observed in live eligibility / referral code paths |
| **Inferred** | Reasonable reading of related code that is not on the live path |
| **Desired** | Behavior supplied in the audit request (maps closely to Art. 103.0031(f)) |
| **Legal/product** | Repository does not establish the correct treatment |

---

## 1. Executive summary

**Confirmed:** Live collections referral eligibility does **not** use appearance dates, judgment dates, payment-plan due dates, or a court-determined “paid in full” date. It uses a single case-level clock: the UTC calendar date of the **latest timeline transition into `CPF_WARRANT`**, then requires **strictly more than** N days to have elapsed (default N = 60). On referral, TPC (capped at 30%) is assessed against the **entire outstanding non-TPC principal**. Post-referral fee increases get their **own** 60-day clocks via `CourtViolationCollectionsReferralItems` (`INCREASE` / `ClockStartOn`) and CV\|15 / `ReferAdditionalAsync`.

**Desired:** Eligibility must follow Art. 103.0031(f)-style bases:

- Unadjudicated FTA → required appearance date + 60 days
- Adjudicated debt → date the balance must be paid in full + 60 days (judgment / court deadline / accelerated plan / final installment)

**Primary gap (Critical):** The product plan for collections originally called for Art. 103.0031(f) trigger dates; the shipped implementation substituted **CPF warrant state entry**. **Product decision (2026-08-06):** realign to statute — unadjudicated from `AppearanceDateTime`; adjudicated from `ComplianceDueDateTime` (judgment + 5 business days default, synced to plans/CS); amount-level aging; no warrant gate for eligibility.

**Secondary gaps:** Today’s `ComplianceDueDateTime` defaults (~30 calendar days, never overwrite) and lack of plan/CS sync; no pre-referral amount-level clocks; health still CPF-only for active referrals; CV\|13 vs `CollectionsAutoReferDays` inconsistency.

**Violation health (in scope):** Health rule `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` currently hard-requires an active referral to sit in `CPF_WARRANT`, via `CollectionsReferralEligibilityRules.IsActiveCollectionsReferralProceduralStateValid`. Supporting rules (`CPF_WARRANT_WITHOUT_JUDGMENT_DATE`, `FTA_WARRANT_WITH_JUDGMENT_DATE`, `PRE_PLEA_NO_NEXT_PROCEDURAL_DATE`, `CONVICTED_MISSING_COMPLIANCE_DUE_DATE`) protect dates the new eligibility tree needs, but **no health rule** flags missing paid-in-full due dates, overdue-but-not-referred collections candidates, or eligibility-basis data gaps. Any statutory eligibility rewrite **must** update health rules, candidate fields, UI issue-code list, and detector tests in the same change set.

**Off-by-one:** **Resolved (§12):** follow statute — unpaid on the **61st day after** the source date. Example: source `2026-06-01` → first eligible **`2026-08-01`** (matches current strict `>` 60 helper). The original prompt’s Jul 31 example is `+60` arithmetic, not the statutory flip day.

---

## 2. Existing implementation

### 2.1 Core domain (confirmed)

| Area | Location |
| ---- | -------- |
| Statutory helpers | `ThinLine.API/ThinLine.API/Court/CourtViolations/CollectionsReferralEligibilityRules.cs` |
| Service contract (cites Art. 103.0031(f)) | `ThinLine.API/ThinLine.API/Court/CourtViolations/ICourtViolationCollectionsService.cs` (lines 9–21) |
| Live eligibility + refer | `ThinLine.API/ThinLine.Business.Objects/Court/CourtViolations/CourtViolationCollectionsService.cs` (`IsEligibleForReferralAsync` ~165–253; `ReferToCollectionsAsync` ~259+) |
| Item math | `ThinLine.API/ThinLine.API/Court/CourtViolations/CollectionsReferralItemMath.cs` |
| Post-referral fee → INCREASE | `.../CollectionsReferralFeeAssessmentHook.cs` |
| Promote ELIGIBLE / DECREASE / TPC trim | `.../CollectionsReferralLifecycleHook.cs` |
| CPF warrant clock source | `.../CourtViolationTimelineEventDataStore.cs` `GetLatestCpfWarrantStateEnteredDateTimeAsync` (~146–174) |
| Work queues CV\|13 / CV\|15 | `.../CourtViolationDataStore.cs` (~2912–2981) |
| Search column | `vw_CourtViolationSearch.CpfWarrantStateEnteredDateTime` (migration `UseCpfWarrantStateTransitionForCollectionsEligibility`) |
| Referral header | `CourtViolationCollectionsReferral` |
| Referral lines | `CourtViolationCollectionsReferralItem` (`ClockStartOn` for INCREASE) |
| Agency knobs | `Agency.CollectionVendorName`, `CollectionsAutoReferDays`, `CollectionsEnabled`, vendor SFTP fields |
| REST | `CourtViolationCollectionsController` |
| UI card / COL module | `ThinLine.UI/.../courtViolation/collections/`, `components/modules/collections/` |
| Violation health detector | `ThinLine.API/.../Health/CourtViolationHealthIssueDetector.cs` |
| Health candidate / rebuild | `CourtViolationHealthCandidate.cs`, `CourtViolationHealthService.cs` |
| Health issue code catalog (UI) | `ThinLine.UI/src/models/courtViolation/courtViolationHealthIssueCodes.ts` |
| Health detector tests | `ThinLine.API.UnitTests/Court/CourtViolationHealthIssueDetector_Tests.cs` |

### 2.1a Violation health — collections coupling (confirmed)

Materialized health issues are rebuilt by `CourtViolationHealthService` → `CourtViolationHealthIssueDetector.Detect`. Collections-related surface today:

| Issue code | Severity / category | Current rule | Coupling to collections model |
| ---------- | ------------------- | ------------ | ----------------------------- |
| `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` | High / Financial | Active `REFERRED` referral while procedural state ≠ `CPF_WARRANT` | Uses `IsActiveCollectionsReferralProceduralStateValid` / constant `ActiveCollectionsReferralExpectedProceduralState = "CPF_WARRANT"` |
| `CPF_WARRANT_WITHOUT_JUDGMENT_DATE` | High / StateMachine | In `CPF_WARRANT` without `JudgmentDateTime` | Assumes CPF warrant is always post-judgment |
| `FTA_WARRANT_WITH_JUDGMENT_DATE` | High / StateMachine | `FTA_WARRANT` with judgment date set | Separates pre- vs post-judgment warrant posture |
| `PRE_PLEA_NO_NEXT_PROCEDURAL_DATE` | High / StateMachine | `PRE_PLEA` with null `AppearanceDateTime` | Protects the date desired unadjudicated eligibility needs |
| `CONVICTED_MISSING_COMPLIANCE_DUE_DATE` | Medium / ProgramPlan | Disposed/convicted cases missing expected `ComplianceDueDateTime` | Closest existing “paid/compliance due” hygiene; **not** wired as collections source date |
| `PAYMENT_PLAN_EXISTS_OUTSIDE_POST_JUDGMENT` | Medium / Financial | Plan outside allowed states | Plans ignored by collections clock today |

Candidate flag (confirmed):

```78:79:ThinLine.API/ThinLine.Business.Objects/Court/CourtViolations/Health/CourtViolationHealthCandidate.cs
	/// <summary>True when a non-satisfied active (REFERRED) <see cref="CourtViolationCollectionsReferral"/> exists; excludes SATISFIED and RECALLED.</summary>
	public bool HasActiveCollectionsReferral { get; set; }
```

Detector rule (confirmed):

```495:502:ThinLine.API/ThinLine.Business.Objects/Court/CourtViolations/Health/CourtViolationHealthIssueDetector.cs
		// 8c. COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE — non-satisfied active (REFERRED) vendor referral only valid in CPF_WARRANT.
		if (c.HasActiveCollectionsReferral
			&& !CollectionsReferralEligibilityRules.IsActiveCollectionsReferralProceduralStateValid(state))
		{
			issues.Add(MakeIssue(c, "COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE", "High", "Financial",
				$"Active (non-satisfied) collections referral while procedural state is {state}; expected CPF WARRANT (post-judgment warrant).",
				"Recall from collections, correct procedural state, or re-refer when the violation is in CPF warrant.",
```

**Confirmed absent today:** health rules for “statutory-eligible but not referred,” “missing required appearance for collections,” “missing paid-in-full due date for adjudicated collections,” or “eligibility basis / source date inconsistent with referral snapshot.”

**Product interaction:** Remittance posting already blocks `FTA_WARRANT` (`GetCollectionsRemittanceBlockReason`). Health flags the same class of bad referral posture for clerks via Violation Health rebuild.

### 2.2 Which date is used today (confirmed)

```137:143:ThinLine.API/ThinLine.API/Court/CourtViolations/CollectionsReferralEligibilityRules.cs
	/// <summary>
	/// Collections eligibility trigger is when the violation most recently entered <c>CPF_WARRANT</c>.
	/// </summary>
	public static DateTime? DetermineCollectionsEligibilityTriggerDate(DateTime? cpfWarrantStateEnteredDateTime)
	{
		return cpfWarrantStateEnteredDateTime;
	}
```

`IsEligibleForReferralAsync` loads that date from timeline events and rejects if null:

```194:228:ThinLine.API/ThinLine.Business.Objects/Court/CourtViolations/CourtViolationCollectionsService.cs
		var cpfWarrantStateEnteredDate = await _unitOfWork.CourtViolationTimelineEventDataStore
			.GetLatestCpfWarrantStateEnteredDateTimeAsync(pCourtViolationId)
			.ConfigureAwait(false);
		if (!cpfWarrantStateEnteredDate.HasValue)
		{
			return CollectionsReferralEligibility.Ineligible("Violation has not entered CPF warrant state.");
		}
		// ...
		var eligibleDays = CollectionsReferralEligibilityRules.ResolveEligibleDaysAfterCpfWarrantStateEntered(
			agency.CollectionsAutoReferDays);
		if (!CollectionsReferralEligibilityRules.IsMoreThanEligibleDaysAfterCpfWarrantStateEntered(
				cpfWarrantStateEnteredDate.Value,
				eligibleDays))
```

**Not used for the live clock:** `AppearanceDateTime`, `JudgmentDateTime`, `ComplianceDueDateTime`, `FinalDispositionDateTime`, payment-plan installment `DueDate`, disposition-plan condition dues (except as helpers that are unused).

### 2.3 Day arithmetic (confirmed)

```176:197:ThinLine.API/ThinLine.API/Court/CourtViolations/CollectionsReferralEligibilityRules.cs
	public static DateTime GetEligibleStrictCutoffDateUtc(int eligibleDaysAfterIssue, DateTime? asOfUtc = null)
	{
		return (asOfUtc ?? DateTime.UtcNow).Date.AddDays(-eligibleDaysAfterIssue);
	}
	// ...
	public static bool IsMoreThanEligibleDaysAfterCpfWarrantStateEntered(...)
	{
		return cpfWarrantStateEnteredDateUtc.Date < GetEligibleStrictCutoffDateUtc(...);
	}
```

- Compares **UTC `.Date`** values (calendar days, not wall-clock duration).
- Eligibility requires trigger date **strictly before** `asOf.Date.AddDays(-N)` ⇒ **more than N days** elapsed.
- For N=60: exactly 60 days ago → **not** eligible; 61+ days ago → eligible.
- Unit proof: `CollectionsReferralEligibilityRules_Tests.IsMoreThanEligibleDaysAfterCpfWarrantStateEntered_RequiresStrictlyGreaterThanThreshold`.

**Versus requested example**

| Convention | Source date `2026-06-01` | First eligible calendar day |
| ---------- | ------------------------ | --------------------------- |
| Desired prompt (`+ 60`, `current >= eligibilityDate`) | | **2026-07-31** |
| Current code (`>` 60 elapsed) | | **2026-08-01** |
| Literal Art. 103.0031(f) (“unpaid on the **61st day after**”) | day-after counting | typically **2026-08-01** |

**Legal/product:** Confirm whether to keep current/statutory “61st day after” (Aug 1) or adopt the prompt’s July 31 example.

### 2.4 Case-level vs amount-level (confirmed)

| Layer | Behavior |
| ----- | -------- |
| Initial referral | **Case-level.** One active `REFERRED` header. Principal = sum of all non-TPC fee balances. One TPC assessment on that total. |
| Post-referral fees | **Amount/line-level.** Each fee assessment creates `INCREASE` PENDING with `ClockStartOn = UtcNow`; after >60 days → ELIGIBLE; `ReferAdditionalAsync` assesses incremental TPC on eligible sum only. |
| Pre-referral later-added fees | No separate aging. Once case is eligible, **all** current non-TPC principal is referred together. |

### 2.5 Eligibility storage vs dynamic (confirmed)

- **Computed dynamically** at check / queue / refer time (no stored `CollectionsEligibilityDate`).
- **Stored on referral:** `ReferredOn`, `ReferralAmount`, `TpcAmount`, `TpcRate`, status, indigency flag; item lines store `ClockStartOn` / `ReferredOn`.
- **No manual eligibility override** field. Referral is clerk-initiated after eligibility passes; cannot refer while already REFERRED without recall.

### 2.6 Dead / unused helpers (confirmed)

`HasEnforceableCourtDebt` (judgment / disposition / procedural-state heuristics) is defined and unit-tested but **never called** from `IsEligibleForReferralAsync` or CV\|13 (repo-wide call sites are only the rules class + its tests). Live path only requires CPF warrant entry + balance + vendor + TPC fee config.

### 2.7 Payment plans (confirmed)

`AccountingPaymentPlan` / `AccountingPaymentPlanInstallment.DueDate` drive missed-payment workflows (e.g. CV\|4), not collections clocks. No acceleration → collections hook found.

### 2.8 Historical product intent (confirmed docs)

Original plan (`court-violation-third-party-collections.md`) said eligibility should use Art. 103.0031(f) trigger dates. Migration `20260527232331_UseCpfWarrantStateTransitionForCollectionsEligibility` later locked search/queue to CPF warrant state entry. Interface comments still cite subsection (f) “per item type,” but implementation does not.

---

## 3. Current decision flow

```mermaid
flowchart TD
  A[Refer / IsEligible / CV|13] --> B{Vendor configured?}
  B -->|no| X[Ineligible]
  B -->|yes| C{Warning?}
  C -->|yes| X
  C -->|no| D{Latest CPF_WARRANT timeline entry?}
  D -->|null| X
  D -->|date| E{Non-TPC principal > 0?}
  E -->|no| X
  E -->|yes| F{Already REFERRED?}
  F -->|yes| X
  F -->|no| G{trigger.Date < asOf.Date - N days?}
  G -->|no| X
  G -->|yes| H{TPC fee configured?}
  H -->|no| X
  H -->|yes| I[Eligible]
  I --> J[Refer: snapshot header + INITIAL item]
  J --> K{Indigent?}
  K -->|yes| L[TPC = 0]
  K -->|no| M[Assess TPC = round2 principal × rate ≤ 30%]
  N[Post-referral AddFee] --> O[INCREASE PENDING ClockStartOn=now]
  O --> P[After >60 days → ELIGIBLE / CV|15]
  P --> Q[Refer additional → incremental TPC]
```

**Notes**

- N defaults to 60; service may use `CollectionsAutoReferDays` if > 0 (including values **&lt; 60** — tests allow 45). CV\|13 **hardcodes** statutory 60 via `GetStatutoryPastDueStrictCutoffDateUtc()`.
- Unadjudicated vs adjudicated is **not** branched; both require CPF warrant state.
- FTA warrant (`FTA_WARRANT`) blocks remittance posting only; it does not start the referral clock.

---

## 4. Gap analysis

| Area | Current behavior | Desired behavior | Gap | Severity | Recommended change |
| ---- | ---------------- | ---------------- | --- | -------- | ------------------ |
| Unresolved FTA (no judgment) | Clock = CPF warrant state entry; no appearance-based path | Clock = required appearance (promise / notice / summons / order) + 60 days | Wrong trigger; many FTAs wait for warrant before eligibility | **Critical** | Resolve controlling appearance date; branch unadjudicated path |
| Judgments due immediately | Same CPF warrant clock | Clock = paid-in-full due date (often judgment date) + 60 | Wrong / delayed trigger | **Critical** | Model paid-in-full due date; use for adjudicated path |
| Judgments with future payment deadline | CPF warrant only | Clock from court-ordered paid-in-full deadline | Missing field + logic | **Critical** | Persist court-ordered due date; drive eligibility |
| Installment plan, no acceleration | Plans ignored for collections | Eligibility from **final** scheduled installment due date | No link | **Critical** | Integrate final installment due date when plan is controlling |
| Installment plan with acceleration | No acceleration flag/event → collections | Full balance due date = default/acceleration date | Missing domain concept | **Critical** | Legal/product: define acceleration representation; wire to due date |
| Missed installments | CV\|4 missed payment; collections only after CPF warrant | May accelerate or still wait for final due date | Ambiguous + unimplemented | **High** | Explicit acceleration vs non-acceleration policy |
| Later-added fees (pre-referral) | Folded into case principal at refer | Possibly separate aging per assessment | Case-level only pre-referral | **High** / **Legal** | Decide amount-level aging; if yes, fee due dates + item clocks before first refer |
| Later-added fees (post-referral) | INCREASE + own 60-day clock + Refer additional | Aligns with per-item aging after referral | Partial match | Medium | Keep; extend model if pre-referral also per-item |
| Partial payments | Reduce principal; referral snapshot fixed; pro-rata TPC on cash; DECREASE on non-cash satisfaction | Unchanged statutory allocation concerns | Largely implemented; proportional (e) still flagged historically | Medium | Retain; legal review of (e) allocation |
| Reopened / vacated judgments | No eligibility recompute from judgment vacation | Should drop adjudicated basis / recalculate | No event hook | **High** | Recalc on vacation/reopen |
| Withdrawn pleas | No collections-specific handling | Likely revert to unadjudicated appearance basis | Unimplemented | **High** / **Legal** | Product rules + event handlers |
| Dismissed cases | Not explicitly blocked if CPF warrant + balance exist | Not collectible / fee does not apply (statute (b)) | Gap vs statute | **Critical** | Hard gate: dismissed → ineligible (confirm compliance-dismissal exceptions) |
| Payment-plan modifications | No eligibility impact | Recalculate controlling due date | Missing | **High** | Recalc on plan create/modify/cancel |
| Court-ordered date changes | Appearance/judgment edits do not affect clock | Recalculate from new controlling date | Missing | **High** | Recalc hooks on date edits |
| Recalled warrants | Clock uses **latest** CPF warrant entry; recall of warrant without state clear may leave stale date | Should stop or reset clock when warrant recalled / state leaves CPF_WARRANT | Partially inferred | **High** | Recalc when leaving CPF_WARRANT; clarify product if warrant required at all under new rules |
| Already referred | Ineligible for initial refer; supplemental path exists | Keep historical referral; don’t use appearance for adjudicated re-check blindly | Mostly OK | Low | Snapshot eligibility basis at referral for audit |
| Balances reduced after referral | Lifecycle DECREASE / satisfaction / TPC trim | Same | Implemented | Low | Keep |
| Timezone / calendar dates | UTC `.Date` | Legal rule is calendar-date oriented; agency local day may differ near midnight | Possible off-by-one at TZ boundaries | Medium | Prefer agency calendar date or date-only type for eligibility |
| Day count convention | Strict `>` 60 → eligible day 61 after trigger | Prompt example uses `+60` / July 31 | Off-by-one vs prompt | **High** / **Legal** | Confirm; encode one helper + tests |
| `HasEnforceableCourtDebt` | Unused | Desired tree needs adjudicated vs not | Dead code | Medium | Wire into decision tree or remove |
| Agency `CollectionsAutoReferDays` | Service uses override; CV\|13 fixed 60; admin help says min 60 but code allows &lt;60 | Statute floor is 60 for fee; longer wait OK | Inconsistency / compliance risk if &lt;60 | **High** | Clamp ≥ 60; align queue filter with agency setting |
| Manual override | None | Prompt suggests possible `ManualCourtDetermination` | Missing | Medium | Optional override with reason + audit |
| Auto-refer | Queue + manual refer (auto-refer setting is day count, not auto job) | Out of scope unless product wants auto | Docs vs setting naming | Low | Clarify admin copy |
| Health: active referral state gate | `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` requires `CPF_WARRANT` | If referrals allowed outside CPF warrant under new rules, rule is wrong; if warrant remains operational gate, rule stays | Depends on warrant-gate product call | **Critical** (coupled) | Rewrite allowed-state set + messaging with eligibility change |
| Health: eligibility data quality | No rule for missing appearance / paid-in-full due / basis | Desired model needs auditable source dates | Missing rules | **High** | Add health issues for missing collections source dates when balance/vendor configured |
| Health: overdue not referred | No “eligible but not referred” health issue (CV\|13 queue only) | Optional clerk data-quality signal | Gap vs ops visibility | Medium / optional | New issue or keep queue-only |
| Health: candidate fields | Only `HasActiveCollectionsReferral` | May need source date, basis, eligibility date, plan acceleration flags | Insufficient for new rules | **High** | Extend `CourtViolationHealthCandidate` + loader in `CourtViolationHealthService` |
| Health: UI issue catalog | `courtViolationHealthIssueCodes.ts` lists current code | New codes must stay in sync (sync tests) | Process gap if forgotten | Medium | Update catalog + detector remarks + tests together |

---

## 5. Data-model findings

### 5.1 What exists today

| Concept | Present? | Notes |
| ------- | -------- | ----- |
| Required appearance | Partial | `CourtViolation.AppearanceDateTime` — used broadly as appearance/court date; not proven to distinguish promise vs summons vs order |
| Judgment date | Yes | `JudgmentDateTime` |
| Paid-in-full due date | **No** dedicated field | Closest: `ComplianceDueDateTime`, plan installment dues, disposition condition `DueOn` |
| Collections eligibility date | **No** stored | Dynamic |
| Collections referral date | Yes | `ReferredOn` |
| Collections status | Yes | Referral `StatusCode` + item statuses |
| Payment plan final due | Derivable | Max/`OrderBy` installment `DueDate` |
| Payment plan default / acceleration | **No** | |
| Amount-level pre-referral clock | **No** | Post-referral only via `ClockStartOn` |
| Eligibility basis / source date | **No** | |

### 5.2 Smallest clean auditable model (recommended)

Prefer **computed eligibility with an optional snapshot at referral**, rather than many redundant date columns on `CourtViolation`.

**On referral header (or a thin eligibility snapshot table):**

```text
CollectionsEligibilityDate          -- calendar date used at referral
CollectionsEligibilityBasis         -- enum/code
CollectionsEligibilitySourceDate    -- the controlling “day 0” date
```

**Basis codes (aligned with prompt + statute):**

```text
RequiredAppearance
JudgmentDueImmediately
CourtOrderedDueDate
PaymentPlanFinalDueDate
PaymentPlanAcceleration
ManualCourtDetermination
```

**Optional supporting fields (only if not already reconstructible):**

- `CourtOrderedPaidInFullDueDate` on the violation (or judgment/order record) when the court sets a future deadline distinct from judgment date.
- `PaymentPlanAcceleratesOnDefault` (bool) + `AcceleratedDueOn` (date) on the payment plan — **Legal/product** whether contracts always accelerate.

**Avoid** storing a free-floating `CollectionsEligibilityDate` that never updates without also storing basis + source date and defining recalc events.

**Dynamic vs stored**

| Approach | Pros | Cons |
| -------- | ---- | ---- |
| Fully dynamic | Always reflects latest case facts | Harder audit of “why referred then”; vendor disputes |
| Snapshot at referral only | Auditable; matches current header pattern | Pre-referral queue still needs live calc |
| Hybrid (recommended) | Live calc for queue/eligibility; snapshot basis/source/eligibility date on refer | Slight duplication |

Post-referral INCREASE lines already snapshot `ClockStartOn` — keep that pattern.

### 5.3 Amount-level aging

**Confirmed:** Initial refer does **not** age amounts separately. **Legal/product:** Art. 103.0031 speaks of each **item** more than 60 days past due. AG opinion GA-0313 discusses fees assessed later having their own clocks. Requiring per-fee clocks **before** first referral would be a larger model change (ledger lines need due dates). Flag as policy; BL-023 partially addressed post-referral only.

---

## 6. Edge cases and remaining open items

Resolved product answers are in **§12**. Remaining design risks after those decisions:

1. **`ComplianceDueDateTime` overload** — Today defaults to ~30 **calendar** days from agency-now and **never overwrites**. Using it as Art. 103.0031(f)(1) paid-in-full requires changing default to **judgment + 5 business days** and **syncing** on plan/CS create/modify/cancel (see §12 Q7).
2. **CONVICTED `ModifyComplianceDueDate` Compute quirk** — existing Compute may clobber clerk-entered dates; must fix when making this field the collections clock.
3. **Acceleration still needs a concrete default** — §12 Q5: recommend plans **accelerate on first missed installment by default** (update `ComplianceDueDateTime` to that missed due date) so the clock becomes earliest lawful after default; allow opt-out later if agreements do not accelerate.
4. **Amount-level aging** — case `ComplianceDueDateTime` ages judgment/dismissal principal; later-assessed fees need per-item clocks from each item’s own due/assessment date (extend referral-item model pre-referral).
5. **Multi-violation payment plans** — syncing one plan’s final due onto each violation’s `ComplianceDueDateTime` needs an explicit rule (same date on all linked CVs vs per-violation share).
6. **Vacated judgment / withdrawn plea** — clear or recompute `ComplianceDueDateTime`; unadjudicated path falls back to appearance.
7. **(a)(3) false-alarm items** — out of municipal CV scope unless later required.

---

## 7. Recommended decision tree

Updated for resolved §12 decisions (`ComplianceDueDateTime` as adjudicated source; statute day-count; no CPF warrant gate for eligibility):

```text
If warning OR no collectible non-TPC principal:
    not eligible

If already REFERRED:
    use supplemental / amount-level INCREASE path only (existing + pre-referral item aging)

# --- Amount-level: each unreferred principal item has its own source date ---
For each unreferred non-TPC balance item:
    If item is unadjudicated FTA path (Art. 103.0031(a)(2)):
        sourceDate = ResolveRequiredAppearanceDate(violation)
        basis = RequiredAppearance
    Else:  # adjudicated / dismissal-fee / deferred money (a)(1)
        sourceDate = ComplianceDueDateTime   # court-determined paid-in-full date
        basis = CourtOrderedDueDate (or JudgmentDueImmediately when still at judgment+5BD default)
        # If ComplianceDueDateTime null → ineligible / health data-quality (not CV|13)
    eligibilityDate = sourceDate + 60 calendar days
    item eligible when asOfDate is on/after the 61st day after sourceDate
        # Convention B / statute: unpaid on the 61st day after → first eligible = sourceDate + 61
        # Keep shared helper consistent with current strict >60 tests

Case is referable when any item is eligible (or when referring, refer all currently eligible items + assess TPC only on those).
```

**`ComplianceDueDateTime` maintenance (adjudicated path):**

```text
On judgment entry (CONVICTED) with balance / compliance obligation:
    if ComplianceDueDateTime is null OR still at system default:
        ComplianceDueDateTime = JudgmentDateTime + 5 business days (agency TZ)

On dismissal with money due:
    ComplianceDueDateTime = dismissal compliance due (existing path; align default similarly)

On payment plan create / modify:
    ComplianceDueDateTime = final installment DueDate
    # On first missed installment (recommended default acceleration):
    #   ComplianceDueDateTime = that missed installment DueDate (earliest lawful after default)

On payment plan cancel without full pay:
    ComplianceDueDateTime = JudgmentDateTime + 5 business days (or remaining court-ordered date)

On community service / disposition-plan condition create/modify:
    ComplianceDueDateTime = max(current ComplianceDueDateTime intent, latest relevant condition DueOn)
    # Product: CS completion due extends paid-in-full determination

On clerk ModifyComplianceDueDate / ExtendComplianceDueDate:
    store clerk value (fix CONVICTED Compute overwrite bug)
```

**Required appearance resolver (unadjudicated) — specific mapping:**

| Priority | Field | When it applies |
| -------- | ----- | --------------- |
| 1 | `CourtViolation.AppearanceDateTime` | Primary. Seeded from `Citation.InitialAppearanceDate` at CV create (promise / written notice to appear). Updated by `ModifyAppearanceDate` (PRE_PLEA), clear-FTA / recall-warrant appearance computes. |
| 2 | If null after FTA show-cause reset | Use `ShowCauseDateTime` only when product treats the show-cause setting as the new ordered appearance (confirm in implementation; otherwise keep AppearanceDateTime required). |
| Do not use | `Citation.CourtDate` | Column exists; **not** mapped into CV. |
| Do not use | `HearingDateTime` / `TrialDateTime` / `PreTrialDateTime` | Post-appearance procedural settings; not the (f)(2) “promised/notified/summoned/ordered” citation appearance unless case never had `AppearanceDateTime` and court ordered a later first appearance (rare — prefer copying into `AppearanceDateTime`). |

TLS does **not** currently store separate “promise vs summons vs order” codes. Treat `AppearanceDateTime` as the single statutory (f)(2) date unless conversion later splits them.

**Active referral health allow-list (from state machine):**

Allow `REFERRED` without `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` in:

- `CONVICTED` — primary post-judgment debt home
- `CPF_FTC` — normal intermediate after warrant recall/execution / noncompliance
- `CPF_WARRANT` — still valid enforcement posture; **not required** to refer

Exclude: `FTA_WARRANT` / `FTA` (pre-judgment; remittance already blocks `FTA_WARRANT`), `DISMISSED` with active referral (prefer recall on dismiss), `APPEALED`, `TRANSFERRED`, `VOIDED`, `WARNING`, pre-plea/trial track.

Optional later: `DEFERRED_DISPOSITION` if deferred balances are intentionally referred.

---

## 8. Recommended code changes

Suggested sequencing (product decisions in §12 are now locked unless revisited):

1. **Introduce eligibility context DTO**  
   `CollectionsEligibilityEvaluation { IsEligible, Basis, SourceDate, EligibilityDate, Reason, ProspectivePrincipal, ProspectiveTpc, EligibleItems }`  

2. **Rewrite eligibility trigger**  
   Unadjudicated → `AppearanceDateTime`; adjudicated/dismissal money → `ComplianceDueDateTime`. **Remove CPF warrant requirement** from statutory eligibility.

3. **Date math helper**  
   Statute convention: eligible when unpaid on the **61st day after** source date (keep current strict `>` 60 / first eligible = source + 61 calendar days). Shared by CV\|13, refer, and item promotion.

4. **`ComplianceDueDateTime` as paid-in-full clock**  
   - Default on judgment: **`JudgmentDateTime` + 5 business days** (reuse `ComputeFunctions.AddBusinessDays`).  
   - Replace “30 calendar days / never overwrite” behavior for this purpose.  
   - Sync on payment-plan and CS/disposition-plan lifecycle (see §7).  
   - Fix CONVICTED `ModifyComplianceDueDate` so clerk values persist.

5. **Amount-level aging**  
   Extend referral-item / fee-due clocks **before** first refer: each assessment gets a source date; TPC only on items past the statutory window when referred.

6. **Required appearance resolver**  
   Implement §7 mapping; health-flag missing `AppearanceDateTime` when unadjudicated balance + collections enabled.

7. **Dismissed path**  
   Collectible dismissal fees age from `ComplianceDueDateTime` (due when dismissed). Do **not** block referral solely because state is DISMISSED if money remains due under normal compliance logic; still suppress TPC where statute (b) forbids fee on dismissed **cases** — **Legal nuance:** statute says collection fee does not apply to a case that has been dismissed; product Q7 chose compliance-due aging for dismissal obligations. Implement as: referral of remaining compliance amounts allowed; **TPC assessment** on dismissed cases requires a final legal read of (b) vs residual fees. Default engineering stance until counsel says otherwise: allow referral of residual balances; **do not assess TPC** while procedural state is DISMISSED if (b) is read literally as case-level.

8. **Event recalculation** for ComplianceDueDate + item clocks; snapshot basis at refer.

9. **Align CV\|13**; clamp `CollectionsAutoReferDays` ≥ 60.

10. **UI / admin copy** — basis-aware; show ComplianceDueDate / appearance as source.

11. **Violation health (same release)**  
    - Allow-list active referral in `CONVICTED` | `CPF_FTC` | `CPF_WARRANT`.  
    - Data-quality: missing appearance (unadjudicated) / missing ComplianceDueDate (adjudicated with balance).  
    - **Do not** add eligible-but-not-referred health issues (CV\|13 owns that).  
    - Sync `courtViolationHealthIssueCodes.ts` + rebuild.

12. **Tests** — §10 matrix including ComplianceDueDate sync and amount-level aging.

---

## 9. Recommended migration or backfill strategy

1. **Schema (EF scaffold only):** add optional snapshot columns on `CourtViolationCollectionsReferrals` (basis, source date, eligibility date); optional `CourtOrderedPaidInFullDueDate` / plan acceleration fields if product confirms.
2. **Do not backfill historical referrals’ clocks** into new statutory bases without review — preserve `ReferredOn` / amounts; optionally **annotate** basis as `LegacyCpfWarrant` for rows referred under old rules.
3. **Search view / queue:** replace or supplement `CpfWarrantStateEnteredDateTime` filter with computed eligibility (may need persisted projection table if SQL cannot express the tree efficiently).
4. **Portfolio already REFERRED:** leave alone; supplemental INCREASE clocks unchanged.
5. **Open CV\|13 candidates:** will reshuffle heavily (earlier eligibility for appearance/judgment-due cases; some warrant-only edge cases may drop). Provide clerk communication + report of delta before cutover.
6. **Feature flag:** `CollectionsEligibilityMode = LegacyCpfWarrant | StatutoryArt1030031` for staged rollout.
7. **Health rebuild:** After rule code changes, run Violation Health rebuild per agency so `CourtViolationHealthIssues` reflects the new detector (stale `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` rows otherwise persist until next rebuild).

---

## 10. Test plan

### 10.1 Existing coverage (confirmed)

| Suite | What it covers |
| ----- | -------------- |
| `CollectionsReferralEligibilityRules_Tests` | Strict >60, enforceable-debt helper, remittance FTA block, TPC math |
| `CourtViolationCollectionsService_Tests` | CPF warrant eligibility gates, refer/indigency, remittance |
| `CollectionsReferralItemMath_Tests` | Item rollups / TPC cap |
| Integration `Court/Collections/*` | Remittance / financial pipeline / closure |
| UI `courtDashboardWorkAreaNavigation.spec.ts` | CV\|13 / CV\|15 routing |
| `CourtViolationHealthIssueDetector_Tests` | `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` only valid in non-`CPF_WARRANT`; CPF warrant OK |

**Missing:** appearance-based and paid-in-full-due-date eligibility; plan acceleration; dismissal gate; agency TZ calendar; July 31 vs August 1 convention tests for **statutory source dates** (current tests only cover CPF warrant); health rules for missing collections source dates / revised referral-state gate.

### 10.2 Proposed matrix (minimum)

Assume legal confirms either Convention A (`eligible on source+60`, prompt example) or Convention B (`eligible on source+61` / current “more than 60”).

**Convention A examples**

| Source date | Eligibility date |
| ----------- | ---------------- |
| 2026-06-01 | **2026-07-31** |
| 2024-02-01 (leap) | 2024-04-01 |
| 2026-01-31 | 2026-04-01 |

**Convention B examples (current code behavior)**

| Source date | First eligible asOf |
| ----------- | ------------------- |
| 2026-06-01 | **2026-08-01** |
| 2026-03-22 with asOf 2026-05-22 | eligible (existing unit test pattern) |

**Scenario tests**

| # | Setup | Expect |
| - | ----- | ------ |
| 1 | Unadjudicated; appearance 2026-06-01; no judgment | Eligible per chosen convention; basis=`RequiredAppearance` |
| 2 | Judgment 2026-06-01; due immediately; no plan | Basis=`JudgmentDueImmediately`; same offset |
| 3 | Judgment; court ordered paid-in-full 2026-08-15 | Clock from 2026-08-15, not appearance |
| 4 | Plan final installment 2026-12-01; no acceleration | Clock from 2026-12-01 |
| 5 | Plan accelerates on miss; missed 2026-07-01 | Clock from acceleration date |
| 6 | Plan does not accelerate; missed middle installment | Still final due date (if policy confirms) |
| 7 | Warrant fee assessed after judgment; amount-level policy ON | Separate eligibility for that fee |
| 8 | Same; policy OFF | Included only when case eligible |
| 9 | Partial payment before refer | Principal reduced; still same source date |
| 10 | Vacated judgment | Lose adjudicated basis; fall back or ineligible |
| 11 | Null appearance and null judgment | Ineligible with clear reason |
| 12 | Dismissed | Ineligible (pending policy) |
| 13 | Already REFERRED | Initial ineligible; INCREASE path unchanged |
| 14 | DST spring/fall around agency midnight | Agency calendar date, not UTC shift |
| 15 | Legacy referred under CPF warrant | Snapshot `LegacyCpfWarrant`; no TPC reassess |

**Health detector matrix**

| # | Setup | Expect |
| - | ----- | ------ |
| H1 | Active referral + `CPF_WARRANT` | No invalid-state issue (legacy / if CPF still allowed) |
| H2 | Active referral + `FTA_WARRANT` | Issue **only if** product still forbids FTA referrals; else no issue / different code |
| H3 | Active referral + `CONVICTED` (if newly allowed) | Matches updated allowed-state set |
| H4 | Unadjudicated balance, collections enabled, null appearance | New missing-appearance collections health issue |
| H5 | Adjudicated balance, null judgment and null paid-in-full due | New missing-due-date collections health issue |
| H6 | Satisfied/recalled referral + non-CPF state | No `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` (unchanged: only active REFERRED) |
| H7 | UI issue-code catalog includes every new detector code | Sync test / catalog update |

Use **date-only** values in tests unless wiring forces `DateTime`; avoid `DateTime.Now` nondeterminism (`asOf` / `evaluatedAtUtc` parameters already exist — extend them).

---

## 11. Files likely requiring modification

**API / domain**

- `CollectionsReferralEligibilityRules.cs`
- `CourtViolationCollectionsService.cs` / `ICourtViolationCollectionsService.cs`
- `CourtViolationDataStore.cs` (CV\|13 filter)
- `CourtViolationTimelineEventDataStore.cs` (may become secondary)
- `CollectionsReferralLifecycleHook.cs` / `CollectionsReferralFeeAssessmentHook.cs`
- Possibly new: `CollectionsEligibilityEvaluator.cs`, payment-plan due-date resolver
- `Agency` validation for `CollectionsAutoReferDays`
- EF migration for snapshot / due-date fields (scaffold only)
- `vw_CourtViolationSearch` / search object if projection changes

**UI**

- `CourtViolationCollectionsCard.vue`
- `adminCourtAgencyFieldHelp.ts` / `AdminAgencyGeneral.vue`
- `useCourtViolationActionDate.ts`
- Work-queue info cards / dashboard copy
- `ICourtViolationCollections.ts` / API client types
- `courtViolationHealthIssueCodes.ts` (keep in sync with detector)

**Violation health**

- `Health/CourtViolationHealthIssueDetector.cs` (remarks + rules)
- `Health/CourtViolationHealthCandidate.cs`
- `Health/CourtViolationHealthService.cs` (candidate load / joins for plan dues, eligibility inputs)
- `CollectionsReferralEligibilityRules.IsActiveCollectionsReferralProceduralStateValid` (shared with health + remittance posture)
- `CourtViolationHealthIssueDetector_Tests.cs`
- Optional: health suggestion resolver if new issues get fix suggestions

**Tests**

- `CollectionsReferralEligibilityRules_Tests.cs`
- `CourtViolationCollectionsService_Tests.cs`
- New evaluator tests; integration probes for queue membership
- Health detector / catalog sync tests

**Docs**

- Customer `tls-docs-repo/customer/collections/*`
- Internal plans / release notes when shipping
- Any Violation Health operator docs that list issue codes

---

## 12. Questions requiring legal or product confirmation — **resolved 2026-08-06**

| # | Question | Decision |
| - | -------- | -------- |
| 1 | Day-count / Jul 31 vs Aug 1 | **Statute.** Eligible when unpaid on the **61st day after** the source date (align with current strict `>` 60 implementation; source `2026-06-01` → first eligible **`2026-08-01`**). Prompt example Jul 31 was illustrative of `+60` math, not the statutory flip day. |
| 2 | Require CPF warrant to refer? | **No.** Align to statute; warrant is not the eligibility trigger. |
| 3 | Amount-level aging | **Implement** (pre- and post-referral). |
| 4 | Paid-in-full when judgment silent | **Statute (f)(1)** = date court determines paid in full. **Default = judgment date + 5 business days** stored on **`ComplianceDueDateTime`**. CS orders and payment plans **should update** that date to the end of the order/plan (see Q7). |
| 5 | Acceleration | Uncertain. **Engineering recommendation for “earliest lawful”:** default municipal plans to **accelerate on first missed installment** and set `ComplianceDueDateTime` to that installment’s due date; without a miss, plan creation extends due to **final installment**. Opt-out flag can come later if agreements never accelerate. |
| 6 | Required appearance mapping | **Specific:** use `CourtViolation.AppearanceDateTime` (from `Citation.InitialAppearanceDate` + clerk/FTA updates). See §7 table. No separate promise/summons/order fields today. |
| 7 | Dismissed cases | Follow normal compliance logic; residual money uses **`ComplianceDueDateTime`** (due when dismissed). See §8 item 7 for TPC-on-dismissed nuance under (b). |
| 7+ | ComplianceDueDate as sole adjudicated clock? | **Yes — recommended.** See narrative below. |
| 8 | Deferred disposition | Treat deferred balances with money due like (a)(1): age from `ComplianceDueDateTime` / controlling disposition condition due synced onto compliance due. |
| 9 | Recalc after referral | **Snapshot fixed** for referred amounts/TPC; new/unreferred amounts get new clocks. Do not rewrite historical referral basis when later dates change. |
| 10 | `CollectionsAutoReferDays` | **≥ 60** for TPC eligibility (statute floor). Longer waits allowed; shorter not for fee assessment. |
| 11 | Health allowed states for active REFERRED | From state machine: **`CONVICTED`, `CPF_FTC`, `CPF_WARRANT`**. Exclude `FTA_WARRANT` / pre-judgment. |
| 12 | Eligible-but-not-referred health? | **No.** CV\|13 / work area owns that procedure. |

### Would using `ComplianceDueDateTime` work?

**Yes**, with required behavior changes — it is the best existing case-level field and CV\|4 already treats past compliance due as failure to pay in full.

| Today (confirmed) | Needed for collections |
| ----------------- | ---------------------- |
| Default ~30 **calendar** days from agency-now | Default **judgment + 5 business days** |
| Never overwrites once set | **Must sync** when plans/CS create, modify, cancel, miss (if accelerate) |
| Collections ignores it | Adjudicated eligibility **keys off it** |
| CONVICTED modify may clobber clerk date | Fix Compute overwrite |

**Tradeoff vs new `PaidInFullDueDate` column:** reusing `ComplianceDueDateTime` avoids a parallel clerk-facing date and keeps CV\|4 / health / collections aligned. Cost is broadening its meaning to “court-determined paid-in-full date” and implementing sync. That matches your intent.

**Amount-level still needed:** `ComplianceDueDateTime` ages the adjudicated (or dismissal) principal bundle; fees assessed later (warrant, FTA, time-payment, etc.) keep **per-item** clocks from their own assessment/due dates so TPC is not applied early to new lines.

**Open micro-decision:** On payment-plan create, always move compliance due to **final installment** (extends clock). On first miss, if we adopt recommended acceleration, move it **earlier** to the missed due date. Confirm that acceleration default when you are ready to implement; until then the audit records it as the recommended default for “as early as statute allows.”

---

## Prioritized implementation plan

### Critical correctness fixes

1. Stop using **only** CPF warrant state as the Art. 103.0031(f) past-due trigger; implement appearance vs **`ComplianceDueDateTime`** decision tree (no warrant gate).
2. Encode statute **61st-day-after** convention; align CV\|13.
3. Retarget **`ComplianceDueDateTime`** default to judgment + **5 business days**; sync with payment plans / CS; fix CONVICTED modify overwrite.
4. Implement **amount-level aging** (extend item clocks pre-referral).
5. Clamp **`CollectionsAutoReferDays` ≥ 60**; snapshot basis at referral.
6. **Violation health:** allow-list `CONVICTED` \| `CPF_FTC` \| `CPF_WARRANT`; missing source-date data-quality only; **no** eligible-not-referred health; rebuild.

### Recommended structural improvements

1. Payment-plan **acceleration-on-miss** default (or explicit flag) driving `ComplianceDueDateTime`.
2. Event-driven ComplianceDueDate + item-clock recalculation.
3. Feature-flagged cutover + **legacy** CPF-warrant basis for existing referrals.
4. UI surfaces for source date / eligibility date / item eligibility.
5. Resolve TPC-on-**DISMISSED** vs Art. 103.0031(b) with counsel if residual fees are referred.

### Optional future enhancements

1. Split promise/summons/order appearance types if conversion needs them.
2. Auto-refer job (still queue + manual by default).
3. Manual court determination override with reason codes.
4. Agency-local date-only type end-to-end.
5. Vendor export eligibility basis fields.
6. ~~Eligible-but-not-referred health~~ — **rejected** (work area owns it).

---

## Appendix A — Event → recalc matrix

| Event | Recalculate eligibility? | Notes |
| ----- | ------------------------ | ----- |
| Citation / case creation | Yes | May lack appearance yet |
| Appearance-date change | Yes | Unadjudicated basis |
| FTA recorded | Yes | Still appearance-based until judgment |
| Judgment entry | Yes | Switch to adjudicated basis |
| Judgment vacation | Yes | Fall back / ineligible |
| Payment deadline entry | Yes | Court-ordered due date |
| Payment-plan create/modify/cancel | Yes | Final due / acceleration |
| Installment default | Yes if acceleration | Else maybe no |
| Fee assessment / removal | Yes for principal; new clocks if amount-level | Post-referral already hooks INCREASE |
| Payment / reversal | Principal only unless paid in full / satisfaction | Referral snapshot fixed |
| Dismissal | Yes → not eligible | |
| Case reopen | Yes | |
| Enter/leave CPF_WARRANT | Only if warrant remains operational gate | Not statutory basis under desired rules; health allowed-state set must stay consistent |
| Referral | Snapshot basis; stop initial eligibility | Supplemental clocks continue; health uses `HasActiveCollectionsReferral` |
| Health rebuild | Re-evaluate all detector rules | Required after rule/code changes so materialization matches detector |

**After referral:** Keep historical eligibility snapshot fixed for the INITIAL placement. Recalculate only for **unreferred** supplemental amounts and satisfaction/DECREASE handling (current design).

---

## Appendix B — Relationship to backlog

- **BL-023** (plan file still named `BL-022-collections-supplemental-item-referrals.md`): post-referral item clocks — **partially implemented** (`CourtViolationCollectionsReferralItems`, CV\|15). This audit’s critical gap is **pre-referral statutory trigger dates**, which BL-023 does not fully solve.
- Original collections plan Phase 1 text already expected Art. 103.0031(f) triggers; implementation drifted to CPF warrant.
- **Violation health** is a hard dependency of the eligibility rewrite because `COLLECTIONS_REFERRAL_INVALID_PROCEDURAL_STATE` currently encodes the CPF-warrant-only referral posture. Do not ship eligibility changes without a coordinated health detector + catalog + rebuild plan.

---

*End of audit. No production code modified.*
