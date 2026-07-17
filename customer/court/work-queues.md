# Work queues

Exception-driven lists of court violations that need clerk or judge attention.

## Why use queues

Search is for finding a known case. **Work queues** answer: “What should we work next?” Counts on the dashboard help you prioritize the day.

In navigation you may see **Work Queues** (older builds may have said Court Proceedings).

## Common queues

Names in your environment may vary slightly; these are the usual work areas:

| Queue (typical) | What it usually means | Typical next step |
|-----------------|----------------------|-------------------|
| **New case review** | Newly created cases not yet activated | Set appearance; activate to Pre-plea; transfer/void if needed |
| **FTA — missed appearance / show cause** | Failure to appear work | Set show cause; warrant/bond path; record appearance |
| **Program / compliance — missed deadline** | Court program or compliance date missed | Notice, show cause, fail/revoke program, or extend per court order |
| **Program — show cause** | Program FTC show-cause set | Record appearance or next enforcement step |
| **Surety bond — show cause** | Bond-related show cause | Bond hearing / resolve bond actions |
| **Program — ready to close** | Program appears complete | Verify conditions; complete program / dismiss |
| **Follow-up — past due** | Follow-up date passed | Contact, reschedule, or clear follow-up |
| **Compliance — missed payment** | Installment or payment compliance missed | Notice; failed to comply / show cause; accept payments |
| **Payment plan — fee eligible** | Time-payment fee assessment candidate | Assess fee per policy |
| **Collections — eligible** | Candidate for collections referral | Refer per agency process |
| **Payment — accept new** | Payments awaiting court acceptance | Accept (or correct) pending payments |

## How to work a queue

1. Open **Work queues** from Court Violations.
2. Select a queue and review the list.
3. Open a case, take the appropriate action, and confirm it leaves the queue (or moves to the correct next queue).
4. Use batch actions only when you understand the effect (for example batch activate or batch show-cause date). Spot-check results.

## Tips

- Clear **payment acceptance** daily so receipts and deposits stay current.
- Do not ignore **ready to close** and **health** signals — they prevent stuck balances and open plans on disposed cases.
- If a case will not leave a queue after you act, the action may have been dialog-only (edit without state change) or a guard blocked the transition.

## Related

- [Getting around](getting-around.md)
- [Create and import cases](create-and-import.md)
- [Payments](payments.md)
- [FTA, warrants, and bonds](fta-warrants-bonds.md)
