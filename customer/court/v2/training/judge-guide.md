# Judge guide

> **Not yet approved for demos.** This page describes the current Court V2 build, which is newer than the version approved for demos. Use it for training and planning. Check [Demoable now](../demoable-now.md) before showing these screens to a customer.

**Who this is for:** staff with the court judge role. The judge role also includes clerk permission, so a judge can do everything in the [Clerk guide](clerk-guide.md) as well. A Thin Line support user is never treated as the judge.

On a Court V2 court, the judge rules on every program, relief and dismissal request, and signs every order of dismissal. Clerks and the violator prepare requests; nothing changes on the case until you act.

## 1. Open the Judge Queue

1. Select **Judge Queue** in the Court Violations menu, or switch the **Dashboard** to **Judge** mode.
2. Filter by **Source** (Portal, Tablet, Paper or Clerk) and by **Packet type**.
3. Each card shows the case, the request, its state, the balance and any money held for it. Paper cards show **Paper awaiting judge** and remind you: *Check the hand-signed paper before you approve.*

![A Judge Queue card](../images/court-v2-judge-queue-card.png)

*A request waiting in the Judge Queue.*

## 2. Review a request

1. Select **Review case and documents**. You see the case, the documents and the violator's answers, such as the plea, the jury waiver, military status, and the signature.
2. For a paper request, check the hand-signed paper in the physical packet. The clerk has already confirmed it was hand-signed and checked any proof.

## 3. Rule on a request

| Ruling | What you do | What happens next |
|--------|-------------|-------------------|
| **Approve** | Confirm. On a paper request, confirm you checked the hand-signed paper. | The outcome takes effect. See [What approving does](#5-what-approving-does). |
| **Needs Info** | Add a note saying what's missing. | The request goes to **Clerk Queue > Needs info** with your note. The clerk fixes it and resubmits. |
| **Reject** | Add a note with your reasons. | The request is closed and appears in the clerk's follow-up list. Money held for a pay in full request is refunded by check. |

After you approve or reject a request, it can't be revoked. A second request on the case can start after you decide the first, or after it's revoked or cancelled.

### Extensions (request for more time)

When you approve an extension, the **Grant the extension** dialog opens.

![Grant the extension dialog](../images/court-v2-judge-grant-extension.png)

*The requested date is filled in. Change it or leave it empty to keep the request as asked.*

The new due date must be after today. Statutory compliance dismissal deadlines can't be extended.

### Batch approve

1. Tick up to 50 rows.
2. Select **Approve selected**. For paper rows, confirm you checked the hand-signed paper.

Every approval is your judicial ruling. Dismissals need a drawn signature, so they're never batch-approved.

### Read-only view

Users without the judge permission see the queue read-only, with this message: *Approve, Needs info and Reject are judge rulings. Your account does not have the judge (Adjudicate) permission.*

## 4. Sign an order of dismissal

1. On a dismissal request, select **Approve**. The order dialog opens.
2. Draw your signature and add an optional note.
3. Select **Sign order and dismiss**, then confirm: *Sign the order of dismissal? The case is dismissed and closed when you sign.*
4. The signed order of dismissal is kept with the case.

Checking proof and collecting a fee never dismiss a case. Your signed order does.

### Prosecutor motions to dismiss

On a motion the prosecutor signed, choose one:

- **Sign order and dismiss.** The case is dismissed and closed.
- **Return for correction.** The motion goes back to the prosecutor to correct and resubmit.
- **Deny motion.** The motion is closed and goes to the clerk's follow-up list.

A prosecutor never signs the order. The dismissal card says: *A court attorney cannot sign an order of dismissal. The judge signs it.*

## 5. What approving does

| Request | Approving it… |
|---------|----------------|
| **Pay in full** | Enters a no contest plea, the jury waiver and the judgment. A not guilty plea on file is replaced (CCP 27.14(c)). |
| **Payment plan** | Starts the plan. |
| **Driving safety course** | Grants the course. The course is due 90 days after you approve. |
| **Deferred disposition** | Grants deferred disposition with its terms. |
| **Youth Diversion** | Grants Youth Diversion, unless the prosecutor objected (CCP 45A.504(d)). |
| **Extension** | Sets the new due date. |
| **Community service** | Approves the community service request. You can edit the terms. |
| **Hardship** | Records your ruling on the hardship request. The violator's ticks for community service or a later date only tell you what they're asking for. They don't create a community service order or an extension. |
| **Dismissal** (any kind) | Requires your signed order. The case is dismissed and closed. |

**Minors:** a parent or guardian must be present before a minor's plea (CCP 45.0215). The clerk records it before the plea.

## 6. Judge-only actions on the case

These are yours alone. A clerk sends a request instead.

- **Ability-to-pay inquiry** and **fine or cost waivers** after a judgment.
- **Commitment terms** and **community service order terms**.
- The **driving safety course after failure** ruling.
- **Warrants:** FTA warrant one-step, CPF warrant one-step, and the CPF ROH.
- **Grant new trial** (CCP 45A.201) and **vacate judgment**, from the case action menu.
- **Grant a court program** (CCP 45A.307).
- **Dismiss a compliance case directly.** You can dismiss a compliance case without a clerk request.
- **Judge-ordered dismissal:** use **Submit for dismissal** from the case action menu and choose the reason. Starting a dismissal request needs clerk permission, which the judge role includes.

## 7. Youth Diversion decisions

A clerk or a judge records the Youth Diversion decision with **Record youth diversion decision**: declined, or not eligible (CCP 45A.504(b)). It's recorded on the case timeline with no e-signature. If the prosecutor objected, Youth Diversion isn't granted (CCP 45A.504(d)). Hearing orders on a Youth Diversion case are judge-only and need your drawn signature.

## 8. Clerk work

Because the judge role includes clerk permission, you can work the Clerk Queue, run outcomes in the case workspace, and revoke a pending request. See the [Clerk guide](clerk-guide.md).

## Practice checklist

- [ ] Filter the Judge Queue by Source and by Packet type.
- [ ] Approve a tablet request and a paper request.
- [ ] Return a request with Needs Info, then approve it after the clerk resubmits.
- [ ] Reject a request with a note.
- [ ] Grant an extension with a changed date.
- [ ] Sign an order of dismissal.
- [ ] Return a prosecutor motion for correction.

## Related

- [Clerk guide](clerk-guide.md)
- [Prosecutor guide](prosecutor-guide.md)
- [Dismissals](scenarios/dismissals.md)
- [Court programs and eligibility](../court-programs-eligibility.md)
