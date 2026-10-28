# Scenario: Dismissals

> **Not yet approved for demos.** This page describes the current Court V2 build, which is newer than the version approved for demos. Use it for training and planning. Check [Demoable now](../../demoable-now.md) before showing these screens to a customer.

## When to use

The case should be dismissed: the violator fixed a compliance problem, the prosecutor moves to dismiss, or the judge orders a dismissal.

## The rule

**The judge signs every order of dismissal.** Clerks don't dismiss cases. Checking proof and collecting a fee never dismiss a case on their own. A prosecutor signs the motion, never the order.

## Compliance dismissal

For offenses the law lets the court dismiss once the problem is fixed, such as an expired registration or license, defective equipment, an inspection, or insurance in effect on the offense date.

### At the counter

1. Open the case. Select **Compliance dismissal** in **Pre-plea**. The card appears only when the offense qualifies.
2. Record what was fixed and when.

   ![Compliance dismissal facts](../../images/court-v2-cd-facts.png)

   *The clerk records the remedy, with the legal basis alongside.*

3. Pair the tablet so the violator can answer and sign, or switch to paper.
4. Collect the dismissal fee. It's *Up to $20.00 on the TMCEC chart (optional). A change from the maximum is logged with your name and the time.*
5. Submit for the judge.

### On paper

1. Select **Print all (one PDF)** or print each form. The violator hand-signs.
2. Confirm the hand signature, and check **Proof verified by clerk**. Attaching a scan is optional and evidence only; the signed paper goes in the physical packet.
3. Select **Submit for judge (paper)**.

   ![Paper packet ready to submit](../../images/court-v2-cd-paper-ready.png)

   *Printed, hand-signed, proof checked, ready to submit.*

### Judge

The judge reviews and signs the order of dismissal. **Needs Info** keeps the fee paid.

### If it's denied or cancelled

The fee stays posted and is flagged for the court administrator, and a follow-up appears in **Clerk Queue > Fee / follow-up**. There's no automatic refund.

A judge can also dismiss a compliance case directly, without a clerk request.

## Prosecutor motion to dismiss (CCP 32.02)

1. **Clerk:** select **Request dismissal**, choose **Prosecutor motion to dismiss (CCP 32.02)**, enter the State's reasons, and send it. It waits in the Prosecutor Queue.
2. **Prosecutor:** select **Approve and sign**, or **Decline** with a note. A prosecutor can also file a motion from the case with **Sign and file motion**.
3. **Judge:** select **Sign order and dismiss**, **Return for correction** or **Deny motion**.
4. If the prosecutor declines or the judge denies, the clerk follows up from **Clerk Queue > Fee / follow-up**.

## Paper motion already signed

When the prosecutor signed a paper motion:

1. Select **Request dismissal** and choose **Prosecutor already signed a paper motion**.
2. Record it. It goes straight to the Judge Queue and doesn't appear in the Prosecutor Queue.
3. Attaching a scan is optional. The signed paper goes in the physical packet. **Not yet approved for demos:** recording a paper motion without a scan isn't available in the current build yet.

## Judge-ordered dismissal

1. Select **Request dismissal** (or **Submit for dismissal** from the case action menu) and choose **Judge-ordered dismissal**.
2. Pick the reason: **Judicial Discretion**, **Clerical Error**, **Other**, or **Parent nonattendance (CCP 45A.403)**, and enter the reasons.
3. The judge signs the order.

## Signing the order

The judge selects **Approve**, draws a signature, selects **Sign order and dismiss**, and confirms: *Sign the order of dismissal? The case is dismissed and closed when you sign.* The signed order is kept with the case.

## Can't or blocked

- *This case already has an open request. Finish or cancel it before requesting a dismissal.*
- A compliance dismissal is blocked once a payment has been entered as a plea and judgment.
- Dismissals can't be batch-approved.

## Related

- [Clerk guide](../clerk-guide.md#8-request-a-dismissal)
- [Prosecutor guide](../prosecutor-guide.md)
- [Judge guide](../judge-guide.md#4-sign-an-order-of-dismissal)
