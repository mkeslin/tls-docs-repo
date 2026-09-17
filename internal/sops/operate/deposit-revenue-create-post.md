# Create & Post — deposit and revenue allocation twins

**Document type:** SOP  
**Phase:** Operate · Support  
**Status:** v0.1  
**Audience:** Internal — Support, Deliver (hypercare)  
**Related:** Customer [Deposit batches](../../../customer/accounting/deposit-batches.md) · [Revenue allocation](../../../customer/accounting/revenue-allocation.md) · [Troubleshooting](../../../customer/support/troubleshooting.md)

---

## What changed in 6.4.19

Dashboard / Deposit Batch / Revenue Allocation **Create & Post Batches** posts the deposit and its revenue-allocation twin in **one transaction**. If the RA journal fails, the deposit post is rolled back.

That closes the “posted deposit, no allocation” half-post that support has seen after Create & Post (including bond-only days with no eligible trust balances).

## Triage

| Report | Version | What to do |
|--------|---------|------------|
| Create & Post shows an error and **neither** batch is posted | 6.4.19+ | Expected. Read the validation message (often no eligible trust / empty RA). Fix setup or selection and retry. |
| **Posted deposit** exists **without** a paired RA | Any, especially pre-6.4.19 | Do **not** tell the clerk to Create & Post again. Escalate to product with agency, batch id, date, and whether the day was bond-only. There is no support-run remediation script in this SOP. |
| Empty pending | Any | Acceptance / agency / date — not this defect. |

## Do not

- Invent a void + recreate sequence on a live half-post without product
- Promise that older posted-without-RA rows self-heal on upgrade — 6.4.19 prevents **new** half-posts from this path only
