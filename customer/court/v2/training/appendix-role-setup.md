# Role setup

> **Not yet approved for demos.** This page describes the current Court V2 build, which is newer than the version approved for demos. Use it for training and planning. Check [Demoable now](../demoable-now.md) before showing these screens to a customer.

**Who this is for:** administrators who set up users at a Court V2 court.

Admin user screens show each role and permission by its id, with a short note. This page lists the ids you'll see and what they mean in plain English.

> **Known gap.** The admin screens don't use the queue names from this training (Clerk Queue, Judge Queue, Prosecutor Queue). Use the tables below to match each role id to the job it covers.

## Court permissions

| Permission id | Plain meaning |
|---------------|---------------|
| `Rms.CourtViolation.Access` | Read court cases |
| `Rms.CourtViolation.Modify` | Do clerk work: run outcomes, work the Clerk Queue, request dismissals |
| `Rms.CourtViolation.Report` | Run court reports |
| `Rms.CourtViolation.Adjudicate` | Make judge rulings in the Judge Queue and sign orders |
| `Rms.CourtViolation.Prosecute` | Sign and file motions to dismiss (CCP 32.02) and object to Youth Diversion (CCP 45A.504(d)). It never changes a case's state, money or pleas. |

## Court roles

| Role id | Plain meaning | Includes | Queues |
|---------|---------------|----------|--------|
| `CRT_OFFICER` | Court clerk | Read and clerk work | Clerk Queue; Judge Queue read-only |
| `CRT_JUDGE` | Judge | Judge rulings, plus read and clerk work | Judge Queue and Clerk Queue |
| `CRT_PROSECUTOR` | Prosecutor or court attorney | Read and prosecute only, with no clerk, judge or accounting permissions | Prosecutor Queue |
| `CRT_READONLY` | Read-only court user | Read only | Judge Queue read-only |
| `CRT_SUPERVISOR` | Court supervisor | Reports, analytics and audits | None |

There's no separate "court clerk" role id. A clerk uses `CRT_OFFICER`.

## Common setups

| Person | Assign |
|--------|--------|
| Clerk who also takes payments | `CRT_OFFICER` plus the accounting role `ACCT_OFFICER`. The court clerk role has no accounting permissions on its own. |
| Clerk who doesn't take payments | `CRT_OFFICER` |
| Judge | `CRT_JUDGE` |
| Prosecutor or court attorney | `CRT_PROSECUTOR` only. Don't add clerk or judge roles. |
| Cashier or finance user | `ACCT_OFFICER` plus `CRT_READONLY` |
| Court administrator | `CRT_SUPERVISOR`, plus `CRT_OFFICER` if they also handle cases |

## Rules to keep in mind

- **Assign each role for the right court agency.** Permissions apply per agency. A prosecutor or judge for one court can't act on another court's cases.
- **Keep prosecutors narrow.** A prosecutor who also has clerk permission still can't record a Youth Diversion decision.
- **Thin Line support users are never treated as the judge,** whatever roles they hold.
- **Turning on Court V2** is a separate agency setting. An administrator with permission to change agency settings uses **Admin > Agency > General** and the switch **Turn on Court V2 for this agency**. It's off by default and can't be turned off once it's on.

## Check a user's setup

1. Ask the user to open **Court Violations**.
2. Confirm the menu shows the queues in the table above for their role.
3. A judge should see **Approve**, **Needs Info** and **Reject** in the Judge Queue. Anyone else sees the read-only message.

## Related

- [Court V2 training](README.md)
- [Other roles](other-roles.md)
