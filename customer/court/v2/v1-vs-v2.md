# Court V1 vs Court V2

Use this page to explain what changes when a court turns on Court V2. Court V1 is the original way of working cases, described in the [Court](../README.md) pages. Court V2 is the outcome-based workflow described in this section.

## The main differences

| | **Court V1** | **Court V2** |
|---|--------------|--------------|
| **Guides** | [Court](../README.md): case states, queues, payments, programs, FTA and documents | [Court V2](README.md) and [Court V2 training](training/README.md) |
| **How work starts** | The clerk moves the case from state to state with case actions | The violator or clerk picks an outcome, and Thin Line puts together the steps that outcome needs |
| **Who decides** | The clerk records pleas, judgments and programs | The judge approves, rejects or returns each request (**Approve**, **Reject** or **Needs Info**) and signs every judgment and dismissal |
| **Signatures** | As described in the Court pages | Always the violator's own signature: online, on the counter tablet, or on printed paper. Never a name typed by the clerk. |
| **Queues** | Work queues by case state | The Clerk Queue, Judge Queue and Prosecutor Queue, plus the same work queues |
| **Dismissals** | Recorded on the case | Always a request that the judge signs. The clerk uses **Request dismissal**; there's no direct dismiss for clerks. |
| **Online** | Online payment | The Court V2 online portal: outcomes, not guilty pleas, notices and requests, with some outcomes kept for the counter |
| **Issuance** | Citations and court import as described in [RMS citations](../../rms/citations/README.md) | Adds the officer's probable cause record, which the clerk and judge read in court |
| **Compliance dismissal** | [Court programs](../court-programs.md) | A request that follows the TMCEC chart. The fee is collected at the counter, and the judge signs the order. |

## Turning on Court V2

An administrator turns on Court V2 at **Admin > Agency > General** with **Turn on Court V2 for this agency**. It's admin-only, off by default, and one-way: once a court is on Court V2, it stays on. The work queues, calendar and reports work the same either way.

You may run Court V1 and Court V2 side by side in a local demo environment to compare them. That isn't a production setup, so don't promise a cutover date or a migration plan.

## Which guide to give someone

| Audience | Start here |
|----------|------------|
| Clerk at a court that hasn't turned on Court V2 | [Court (V1)](../README.md) and [How-tos](../how-tos/README.md) |
| Clerk, judge or prosecutor at a Court V2 court | [Court V2 training](training/README.md) |
| Sales or solutions showing Court V2 | [Demoable now](demoable-now.md), then [Path walk](path-walk.md) |

## Details that differ

| Topic | Court V1 | Court V2 |
|-------|----------|----------|
| Waiting for the judge | Work queues and case states | A submitted request waits in the Judge Queue until the judge acts |
| Hardship evidence | See [Court programs](../court-programs.md) and [Payment plans](../payment-plans.md) | Evidence is required to submit online or on the tablet |
| When community service starts | See [Court programs](../court-programs.md) | Only when the judge approves the request |
| Counter tablet | Not used | The clerk pairs a counter tablet from the workspace so the violator can review and sign |

## Related

- [Court V2](README.md)
- [Court (V1)](../README.md)
