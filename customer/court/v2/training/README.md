# Court V2 training

> **Not yet approved for demos.** This page describes the current Court V2 build, which is newer than the version approved for demos. Use it for training and planning. Check [Demoable now](../demoable-now.md) before showing these screens to a customer.

This section trains clerks, judges, prosecutors and other court staff on a court that has turned on Court V2. Start with the guide for your role, then work through the scenarios that match your court's caseload.

## What changes on a Court V2 court

On a Court V2 court, staff **request** outcomes and the **judge rules** on them. The violator, or the clerk on the violator's behalf, picks an outcome such as pay in full, a driving safety course or a payment plan. Thin Line builds the steps and documents that outcome needs from the case as it stands, and the finished request goes to the judge.

- Clerks don't dismiss cases, grant court programs or enter judge orders. They send requests to the judge.
- Every dismissal is signed by the judge. Checking proof and collecting a fee never dismiss a case on their own.
- The prosecutor's work is limited to motions to dismiss and Youth Diversion objections.
- Paper and the counter tablet are both supported at the counter. On paper, the clerk checks the signed form instead of uploading it.

## Who does what

| Job | Clerk | Judge | Prosecutor | Read-only user | Court supervisor | Payments user |
|-----|:-----:|:-----:|:----------:|:--------------:|:----------------:|:-------------:|
| Clerk Queue, case workspace, outcomes at the counter | ✓ | ✓ | | | | |
| Request dismissal | ✓ | ✓ | Files their own motion instead | | | |
| Judge Queue: Approve, Needs info, Reject; sign orders | | ✓ | | View only | | |
| Prosecutor Queue: sign or decline motions, object to Youth Diversion | | | ✓ | | | |
| Reports, analytics and audits | | | | | ✓ | |
| Post payments | With the payments role | | | | | ✓ |

The judge role includes clerk permission, so a judge can do everything in the clerk guide as well.

## The three queues

The **Clerk Queue**, **Judge Queue** and **Prosecutor Queue** appear in the court menu only on Court V2 courts, and only to users whose role allows them.

| Queue | Who works it | What's in it |
|-------|--------------|--------------|
| **Clerk Queue** | Clerks and judges | Requests the judge returned with Needs Info, fee and follow-up items, and violator portal requests and contact updates |
| **Judge Queue** | Judges (read-only users can view) | Submitted requests waiting for a ruling |
| **Prosecutor Queue** | Prosecutors | Motions to dismiss and Youth Diversion requests open for objection |

The existing work queues (new case review, FTA, show cause, deferred, missed payment and the rest) work the same as before. See [Work queues](../../work-queues.md).

## Rules every role should know

1. **One open request per case.** A case can have only one open request at a time. A second request can start after the judge decides the first, or after it's revoked or cancelled.
2. **Submitting isn't approval.** Nothing changes on the case until the judge acts.
3. **Only the judge rules** on program, relief and dismissal requests: Approve, Needs Info or Reject.
4. **The judge signs every order of dismissal.** A prosecutor or clerk never signs one.
5. **Youth Diversion is in person only,** at the counter or on paper.

## Pick your guide

| Guide | For |
|-------|-----|
| [Clerk guide](clerk-guide.md) | Clerks and cashiers who run the counter, the Clerk Queue and the case workspace. Judges use it for clerk work too. |
| [Judge guide](judge-guide.md) | Judges who rule in the Judge Queue and sign orders |
| [Prosecutor guide](prosecutor-guide.md) | Prosecutors and court attorneys who sign motions to dismiss and object to Youth Diversion |
| [Other roles](other-roles.md) | Read-only users, court supervisors and payments users |
| [Role setup](appendix-role-setup.md) | Administrators who assign court roles |

## Scenarios

Each scenario walks one kind of case from start to finish for every role involved. See the [scenario list](scenarios/README.md):

- [Plea and pay](scenarios/plea-and-pay.md)
- [Not guilty](scenarios/not-guilty.md)
- [Deferred disposition](scenarios/deferred-disposition.md)
- [Driving safety course](scenarios/driving-safety-course.md)
- [Hardship and ability to pay](scenarios/hardship-ability-to-pay.md)
- [Extension (request for more time)](scenarios/extension.md)
- [Community service](scenarios/community-service.md)
- [FTA and failure to pay](scenarios/fta-cpf.md)
- [Youth and juvenile cases](scenarios/youth-juvenile.md)
- [Portal requests](scenarios/portal-requests.md)
- [Dismissals](scenarios/dismissals.md)

## Turning on Court V2

An agency administrator turns on Court V2 at **Admin > Agency > General** with the switch **Turn on Court V2 for this agency**. It's off by default. Once a court turns it on, it stays on, so plan training before the switch is turned on. See [Court V2](../README.md).

## Related

- [Court V2](../README.md)
- [Clerk workspace](../resolution-workspace-and-controls.md)
- [Court programs and eligibility](../court-programs-eligibility.md)
- [Demoable now](../demoable-now.md)
