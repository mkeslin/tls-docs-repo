# Clerk workspace

> **Not yet approved for demos.** This page describes the current Court V2 build, which is newer than the version approved for demos. Use it for training and planning. Check [Demoable now](demoable-now.md) before showing these screens to a customer.

Clerks do in-person Court V2 work in the case workspace. This page covers the workspace layout, new-case intake, the tablet and paper channels, not guilty pleas, Needs Info, and how to cancel or revoke a request. For step-by-step training, see the [Clerk guide](training/clerk-guide.md).

## Workspace layout

![Clerk workspace with outcomes, clerk actions and the tablet column](images/court-v2-workspace-outcomes-hub.png)

*Outcomes on the left, clerk actions in the middle, and signature, tablet and contact details on the right.*

| Column | What's there |
|--------|--------------|
| **Outcomes** (left) | The violator's options, grouped as **Pre-plea** (pay in full, **Enter a plea of not guilty**, and compliance dismissal when the offense qualifies), **Diversions** (driving safety course, deferred disposition, Youth Diversion) and **Financial relief** (payment plan, extension, community service, hardship). Each card shows whether it's available for this case. |
| **Clerk actions** (middle) | Date changes (for example **Modify appearance date**), **Enter follow-up date**, **Transfer to another court** and **Void citation**, plus **Case requests and orders** with **Request dismissal**, **Request for more time** and the other case panels the case state allows. Actions that don't apply show **Unavailable**. |
| **Signature and tablet** (right) | The **Violator signature** choice (tablet or **Paper**), **Pair tablet**, the violator's contact details, and **Case at a glance**. |

On narrow screens, the clerk actions collapse into a menu at the top.

## Payment links and the online portal

On a case, expand **Payment Links** in the left navigation:

| Link | Opens |
|------|-------|
| **Online Payment** | The public citation payment page |
| **In-Person Payment** | The desk payment page used at the counter |
| **Court V2 Online Portal** | The violator portal lookup, in a new tab |

Use **Court V2 Online Portal** to see what the violator sees online.

![Online citation payment](images/court-v2-payment-link-online.png)

*The online payment link opens the public citation payment page in a new tab.*

![In-person desk payment](images/court-v2-payment-link-desk.png)

*The in-person payment link opens the desk payment page.*

## New cases: intake before pre-plea

A new case can't take outcomes or pair a tablet until the clerk finishes intake and chooses **Proceed to Pre-Plea**. Online, the portal tells the violator the case is still processing.

| Requirement | What happens |
|-------------|--------------|
| **Date of birth** | Required before **Proceed to Pre-Plea**. If the citation has no date of birth, the person record's date of birth fills in. The message is *Date of birth is required before Proceed to Pre-Plea*. |
| **Actual speed and posted limit** | Required on speeding offenses. Speed comes from the citation and can't be edited in the workspace. If either value is missing, a note says the citation must be corrected before the case can proceed. |

Other new-case actions are intake (offense, appearance date, fees, date of birth), **Transfer to another court**, **Void citation** and **Enter follow-up date**.

![New-case intake panel](images/court-v2-workspace-new-intake.png)

*The intake panel on a new case.*

## Tablet or paper

Every Court V2 signature comes from the violator. The clerk never types the violator's name as a signature.

- **Tablet.** Choose **Pair tablet** and pair the counter tablet. When the workspace shows **Tablet connected**, the violator previews the documents, checks **I have reviewed these documents**, uploads any required proof, signs, and chooses how to pay. Cash or check goes to the clerk; a card is entered on the tablet. The tablet checks the signature itself.
- **Paper.** Turn on **Paper** under **Violator signature**. Print the packet (each document has a **Print** button, plus **Print all (one PDF)**), have the violator hand-sign, and mark it hand-signed. Thin Line records your name and the time, and the judge checks the paper when approving. Uploads are never required on paper; photocopied proof goes in the physical folder for the judge.

![Pair a tablet](images/court-v2-pair-tablet-card.png)

*Pair tablet on the clerk workspace.*

![Tablet connected](images/court-v2-tablet-connected-card.png)

*The workspace after pairing.*

## Not guilty pleas

A not guilty plea isn't a request to the judge. How it's entered depends on the channel:

| Channel | What happens |
|---------|--------------|
| **Tablet** | The violator chooses not guilty and signs on the tablet. The tablet verifies the signature, and the plea is entered. |
| **Paper** | Print the plea form, have the violator hand-sign it, mark it hand-signed, set the **Pre-trial date**, and enter the plea. |
| **Online** | The violator chooses **Enter a plea of not guilty** on the portal. The portal tells them the submission isn't yet an entered plea. The request appears in the Clerk Queue under **Violator portal**. The plea is entered only when a clerk approves it there. |

After the plea, the case moves to pre-trial, and the pre-trial and trial dates drive the calendar. Family-violence not guilty pleas are taken at the counter or on paper only.

There's no separate guilty or no contest request. A guilty or no contest plea is a step inside another outcome, such as pay in full, a payment plan, a driving safety course or deferred disposition.

![Not guilty plea on the tablet](images/court-v2-tablet-ng-plea.png)

*The violator enters a not guilty plea on the counter tablet.*

### Paying in full after a not guilty plea

A violator who has pleaded not guilty can still choose pay in full. Paying in full then counts as a plea of no contest and a waiver of a jury trial, and the violator sees a warning first. This doesn't apply to juveniles or to family-violence cases.

![Pay in full at the counter](images/court-v2-pay-in-full-counter.png)

*Pay in full at the counter on a case in pre-trial.*

## Needs Info

When the judge returns a request with **Needs Info**, it moves to the **Needs info** section of the Clerk Queue with the judge's note. Choose **Review case and documents**, update the request with the violator (on the tablet or on paper), choose **Save edit**, then **Resubmit**. The request goes back to the Judge Queue. A fee that was already paid stays paid.

![Needs Info card with Resubmit](images/court-v2-clerk-needs-info-resubmit-card.png)

*Save edits and resubmit a returned request.*

## Cancel, revoke, then start another

A case has one open request at a time. A second request can start after the judge decides the first, or after it's revoked or cancelled.

| Action | When | What it does |
|--------|------|--------------|
| **Cancel outcome** | The request is still a draft | Confirm with **Cancel outcome** (or **Keep outcome** to stay). The draft is cleared, and the tablet clears too. |
| **Revoke** | The request was submitted or returned with Needs Info, and the judge hasn't approved or rejected it | A clerk or a judge can revoke. Money held for a pay in full request is refunded by check. Revoking doesn't enter a plea and doesn't change the case state. |

After the judge approves or rejects a request, **Revoke** isn't offered.

While a request waits for the judge, the other outcome cards are muted and show **Not available**, with a note such as *Extension is waiting for the judge. Revoke it to choose a different outcome.* After a cancel or revoke, the outcome cards reload so they reflect the case as it stands.

![Outcomes muted while a request waits for the judge](images/court-v2-workspace-pending-revoke.png)

*An extension is waiting for the judge, so the other outcomes are muted until it's decided or revoked.*

## Related

- [Clerk guide](training/clerk-guide.md)
- [Portal and online options](portal-and-online-options.md)
- [Court programs and eligibility](court-programs-eligibility.md)
- [Compliance gaps](compliance-gaps.md)
