# Case lifecycle

![Judgment / convicted case](images/court-judgment.png)

How a court violation moves from intake through disposition and compliance.

## Two ways to think about status

| Concept | What it means |
|---------|----------------|
| **Procedural state** | Where the case is in court process (for example Pre-plea, Court program, Convicted, FTA warrant) |
| **Workflow status** | Broader work bucket used for queues and filtering (New, Active, Inactive, Closed, Compliance) |

Clerks mostly work from **actions** on the case. Choosing an action (Enter plea, Mark failure to appear, Enter judgment, and so on) moves the procedural state when the action is allowed.

## Common procedural states

| State | Plain-language meaning |
|-------|------------------------|
| **New** | Created; not yet activated into active court flow |
| **Pre-plea** | Awaiting plea / first appearance work |
| **Post-plea, pre-judgment** | Plea recorded; judgment or court program not yet final |
| **Pre-trial / Trial / Verdict returned** | Not-guilty track through trial |
| **Court program** (deferred disposition) | Diversion-style program with conditions |
| **Court program — failed to comply** | Program failure; show-cause path |
| **Convicted** | Judgment entered; fines/compliance/payment work |
| **FTA / FTA warrant** | Failure to appear; may include warrant |
| **CPF warrant / CPF failed to comply** | Capias pro fine / post-judgment enforcement track |
| **Dismissed / Transferred / Voided / Warning / Appealed** | Closing or exit paths |

Exact labels in your environment follow the product UI. Some actions are available in many states (for example bond enter/modify/resolve, or enter follow-up date).

## How to move a case

1. Open the court violation.
2. Review the current state on the Status area.
3. Choose an **enabled** action from the action menu.
4. Complete any required dialog (plea, dates, notes, plan details).
5. Confirm the new state and that calendar / queue expectations match the outcome.

If an action is missing or disabled, a **guard** is usually blocking it (active bond rules, payment plan rules, missing show-cause date, juvenile rules, and similar). Fix the underlying condition rather than forcing a different path.

## Typical happy paths (overview)

**Guilty / no contest**

New → Pre-plea → Enter plea → Post-plea pre-judgment → Enter judgment → Convicted → pay / payment plan / close

**Court program**

… → Post-plea pre-judgment → Grant court program → complete program (often dismiss) **or** fail / revoke paths

**Not guilty**

Pre-plea → Enter plea (not guilty) → Pre-trial → Trial → Verdict → Judgment or acquittal/dismissal

**Missed appearance**

From an appearance state → Mark failure to appear → FTA track → warrant / bond / return paths as applicable

## Related

- [Pleas and judgment](pleas-and-judgment.md)
- [Court programs](court-programs.md)
- [FTA, warrants, and bonds](fta-warrants-bonds.md)
- [Work queues](work-queues.md)
