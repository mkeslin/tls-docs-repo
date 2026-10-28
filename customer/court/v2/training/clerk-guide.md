# Clerk guide

> **Not yet approved for demos.** This page describes the current Court V2 build, which is newer than the version approved for demos. Use it for training and planning. Check [Demoable now](../demoable-now.md) before showing these screens to a customer.

**Who this is for:** staff with the court clerk role (court officer). Most clerks also have the accounting role so they can take payments. Judges have clerk permission too, so they can use this guide for clerk work.

On a Court V2 court, the clerk runs the counter and prepares requests. The judge rules on them. You'll spend most of your day in three places: the **case workspace**, the **Clerk Queue**, and the existing **work queues**.

## 1. Get around

1. Open **Court Violations**. The left menu has **Dashboard**, **Calendar**, **Violations**, **Clerk Queue**, **Judge Queue**, **Citations**, **Reports** and **Reporting Status**. Clerks see the Judge Queue read-only.
2. To find a case, type the number in **Court Violation #** and search, then open the case from the results.
3. The work queues are the same as before: New case review, FTA initial appearance, FTA show cause, Surety bond show cause, Deferred missed deadline, Deferred FTC show cause, Deferred ready to close, Missed payment, Collections eligible, Compliance missed deadline, Compliance show cause and Follow-up past due. See [Work your queues](../../how-tos/work-your-queues.md).
4. The **Dashboard** can switch between **Clerk** and **Judge** modes when your role has both.

## 2. Work the Clerk Queue

Open **Clerk Queue**. It has three sections.

| Section | What's in it | What you do |
|---------|--------------|-------------|
| **Needs info** | Requests the judge returned with Needs Info, with the judge's note | Select **Review case and documents**, fix what the judge asked for, select **Save edit**, then **Resubmit**. The request goes back to the Judge Queue. |
| **Fee / follow-up** | Compliance dismissal fee follow-ups, requests the judge rejected or denied, and **Prosecutor declined dismissal request** | Follow up with the violator or the court administrator as your court requires, then select **Mark followed up**. |
| **Violator portal** | **Portal requests and contact updates** from violators | Select **Review request**, then **Approve** or **Needs info** (or **Deny** where it's offered). See [Violator portal requests](#violator-portal-requests). |

![A request returned with Needs Info](../images/court-v2-clerk-needs-info-resubmit-card.png)

*A request the judge returned. Add a note, save your edit, and resubmit.*

### Violator portal requests

Online requests and contact updates show the **Source** of each request. For each one:

1. Select **Review case and documents** to check the case.
2. Select **Review request**.
3. Choose **Approve**, **Needs info** or, where declining is allowed, **Deny**. **Deny** appears only for compliance dismissals that can be declined.

An online not guilty plea becomes an entered plea only when you approve it here. See [Not guilty](scenarios/not-guilty.md).

## 3. The case workspace

Open a case to see the workspace.

![The clerk workspace](../images/court-v2-workspace-outcomes-hub.png)

*The workspace: outcomes on the left, clerk actions and case requests in the middle, signature, tablet and contact details on the right.*

| Area | What it shows |
|------|---------------|
| **Header** | Violation number, offense, violator, procedural state, workflow, balance, and the plea and next setting once they're set |
| **Outcomes** (left) | Outcome cards grouped as **Pre-plea**, **Diversions** and **Financial relief**. Each shows **Available** or the reason it isn't. |
| **Clerk actions** (middle) | Date changes, **Enter follow-up date**, **Transfer to another court**, **Void citation**, and **Case requests and orders** with **Request dismissal** and **Request for more time** |
| **Right column** | **Violator signature** (switch on **Paper (print and hand-sign)** for paper), **Pair tablet**, **Violator contact**, **Case at a glance**, and **Legal basis** while an outcome is open |

**Outcome groups:**

- **Pre-plea:** Pay in full, **Enter a plea of not guilty**, and **Compliance dismissal** when the offense qualifies.
- **Diversions:** Driving safety course, Deferred disposition, and Youth Diversion for eligible juvenile cases.
- **Financial relief:** Payment plan, Extension, Community service and Hardship.

Thin Line works out the steps for each outcome from the case's current state. For example, a plea step is included only when no plea has been entered yet. You don't walk through case states by hand.

### New cases

A new case shows **Intake checks** instead of outcomes. Each check shows **Passed**, **Needs attention** or **N/A**. When the checks pass, select **Proceed to Pre-Plea**. While a case is new, you can also **Transfer to another court**, **Void citation** or **Enter follow-up date**.

## 4. Run an outcome with the counter tablet

1. Select the outcome card. The outcome opens with numbered steps, for example **Plea and jury waiver**, **Violator answers on the tablet**, **Clerk review and submit** and **Judge review**.
2. On **Pair tablet**, start pairing. The violator opens the counter device and enters the code, or scans it.

   ![Pair tablet card](../images/court-v2-pair-tablet-card.png)

   *The Pair tablet card while waiting for the tablet.*

   ![Counter device landing](../images/court-v2-counter-device-landing.png)

   *The counter device waiting for a code.*

3. When the tablet connects, the card shows it.

   ![Tablet connected](../images/court-v2-tablet-connected-card.png)

   *The clerk sees that the tablet is connected.*

4. Watch **Violator answers on the tablet** fill in. It's read-only for you and updates as the violator saves. The violator reviews the documents, ticks **I have reviewed these documents**, and signs.
5. Fill in the clerk fields the outcome needs, such as the remedy date for a compliance dismissal or the documents for a driving safety course. Add an internal note if needed; it isn't shown to the violator.
6. Take any fee or payment the outcome needs (this needs the payments role).
7. Select **Submit for judge review**. The workspace shows the request waiting for the judge.

To stop an outcome before you submit it, select **Cancel outcome**, then confirm **Cancel outcome** (or choose **Keep outcome**). To step away from an open outcome without cancelling it, select **Leave outcome**.

## 5. Run an outcome on paper

1. In **Violator signature**, switch on **Paper (print and hand-sign)**.
2. Open the outcome. Select **Print all (one PDF)** or print each form. You can reprint at any time, including when the judge asks for more information.
3. Have the violator hand-sign. Mark the form as hand-signed in Thin Line.
4. Tick the paper checks, such as **Proof verified by clerk** or the parent's name for a minor. Paper proof is a clerk check, not an upload.
5. Take any fee or payment, then select **Submit for judge (paper)**. The judge checks the hand-signed paper when approving. Keep the signed paper in the physical packet.

![Compliance dismissal paper packet](../images/court-v2-cd-paper-ready.png)

*A paper packet ready to submit: printed, hand-signed, proof checked.*

## 6. Revoke a request that's waiting

Use **Revoke** when a submitted request, or one returned with Needs Info, should be withdrawn, for example because the violator wants a different outcome.

1. Open the case. The pending request shows on the workspace, and the other outcome cards are muted.

   ![Outcomes muted while a request waits](../images/court-v2-workspace-pending-revoke.png)

   *An extension waits for the judge; the other outcomes are muted.*

2. Select **Revoke** and confirm.
3. The request is cancelled. Revoking enters no plea and doesn't change the case state. Money held for a pay in full request is refunded by check.
4. A second request can start after the judge decides the first, or after it's revoked or cancelled. You can now start the outcome the violator wants.

A clerk or a judge can revoke. Once the judge approves or rejects a request, **Revoke** isn't offered.

## 7. Take a not guilty plea

1. Select **Enter a plea of not guilty**.
2. **Tablet:** the violator types their name, certifies the plea is their own choice, signs, and selects **Sign not guilty plea**.

   ![Not guilty plea on the tablet](../images/court-v2-tablet-ng-plea.png)

   *The violator signs a not guilty plea on the tablet.*

3. **Paper:** print the form, have it hand-signed, and mark it hand-signed.
4. There's no judge request for a not guilty plea. The plea is entered, the case moves to pre-trial, and the header shows the plea and next setting. From here, pre-trial and trial dates drive the calendar.

A family-violence not guilty plea is taken at the counter or on paper only. See [Not guilty](scenarios/not-guilty.md).

## 8. Request a dismissal

Clerks don't dismiss cases. Every dismissal goes to the judge.

1. In **Case requests and orders**, select **Request dismissal**. From the case action menu, the same entry is **Submit for dismissal**.
2. Choose one:
   - **Prosecutor motion to dismiss (CCP 32.02).** Enter the State's reasons and send it. The panel shows: *Waiting for the prosecutor in the Prosecutor Queue. It goes to the judge only when the prosecutor approves and signs it.*
   - **Prosecutor already signed a paper motion.** Record the signed paper motion. It goes to the Judge Queue. Attaching a scan is optional, and the signed paper goes in the physical packet. **Not yet approved for demos:** recording a paper motion without a scan isn't available in the current build yet.
   - **Judge-ordered dismissal.** Choose **Judicial Discretion**, **Clerical Error**, **Other**, or **Parent nonattendance (CCP 45A.403)**, and enter the reasons. It goes to the Judge Queue.
3. If the case already has an open request, you'll see: *This case already has an open request. Finish or cancel it before requesting a dismissal.*
4. If the prosecutor declines, the case appears in **Clerk Queue > Fee / follow-up** as **Prosecutor declined dismissal request**.

For compliance dismissals, see [Dismissals](scenarios/dismissals.md).

## 9. Record paper rulings and other records

| Task | How |
|------|-----|
| **Judge's paper ruling** on an extension or a driving safety course more-time request | Select **Record judge's paper ruling**. Enter the judge who ruled, the ruling, the dates, the new due date and any reasons. |
| **Youth Diversion paper objection** | Tick the prosecutor's paper objection on the Youth Diversion request. |
| **Commitment discharge** | Record it in the **Commitment discharge** panel. |
| **Parent presence before plea** | Record the parent or guardian present before a minor's plea (CCP 45.0215). |

## 10. What clerks can't do

These are judge actions. Send a request to the judge instead.

- Dismiss a case directly, grant a new trial, or vacate a judgment.
- Grant a court program. The screen says: *Only a judge can grant a court program (CCP 45A.307). Submit it to the judge.*
- Approve, return or reject requests in the Judge Queue.
- The ability-to-pay inquiry, fine or cost waivers, commitment terms, community service order terms, and the driving safety course after-failure ruling.
- FTA warrant one-step, CPF warrant one-step, and the CPF ROH.

## Practice checklist

- [ ] Find a case, open the workspace, and name the three outcome groups.
- [ ] Run one outcome with the counter tablet and one on paper, through **Submit for judge review**.
- [ ] Resubmit a request from **Needs info**.
- [ ] Revoke a pending request, then start a different outcome.
- [ ] Send a judge-ordered dismissal request and a prosecutor motion request.
- [ ] Approve a violator portal request.

## Related

- [Clerk workspace](../resolution-workspace-and-controls.md)
- [Judge guide](judge-guide.md)
- [Scenarios](scenarios/README.md)
