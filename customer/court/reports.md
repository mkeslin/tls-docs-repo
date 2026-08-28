# Reports

![Court dashboard](images/court-dashboard.png)

Two different “reports” surfaces in Court:

1. **Operational rosters** — Court Violations → **Reports** (clerk lists you can filter and print)
2. **Regulatory / state packs** — OCA, DPS conviction, and State Quarterly (filed with the state)

**Reporting Status** (Court Violations navigation) shows whether current OCA, DPS, and State Quarterly periods are on track or need attention.

For the full list of case PDFs (notices, judgments, warrants, program letters, labels) and **where each is printed**, see [Documents and forms](documents.md).

## Operational reports (Court Violations → Reports)

Open **Court Violations** → **Reports**. Each card is a preset roster (not a state filing). Bond Search is linked from the same page.

| Report | What it lists | Typical filters |
|--------|---------------|-----------------|
| **Court Programs** | Cases with a disposition plan | Program status (defaults to ACTIVE), plan type, condition type |
| **Disposed** | Cases with a final disposition date in range | Month (or custom range); optional terminal state |
| **Payment Summary** | Cases with **posted** payments in the transaction-date range | Payment transaction dates (not citation date) |
| **New Cases** | Cases **filed** in the selected date range | Filed dates (not citation date) |
| **Payment Plans** | Accounting installment plans | Plan number, defendant, status, balance |
| **Bonds** | Cases with bonds on the violation | Bond type, status, amount, bond dates |
| **Bond Search** (shortcut) | Bonds across cases | Same Bond Search screen as the main nav item |

Each roster (except the Bond Search shortcut) supports **Work** and **Report** display modes: **Work** shows a denser grid for day-to-day clerk follow-up; **Report** favors print layout. Default mode varies by report (for example Payment Summary and Bonds default to **Report**).

Print from the roster grid when you need a paper list. These reports are operational insight — they do not replace OCA / DPS / State Quarterly filings.

## Operational prints (summary)

Clerks print case documents from the **case utility drawer**, **work-queue batch print**, or automatic attachments. Common groups:

- Court violation overview / statement
- Notices (initial setting, pre-trial, show cause, late notice, missed-deadline show cause)
- Deferred disposition / court program, teen court, DSC, and installment agreement documents
- Receipts (final receipts after payment acceptance) — see [Payments](payments.md)
- Citation copies from a court violation (including **batch** citation detail prints from New Case Review)
- FTA / compliance **address labels** from work-queue batch print (not from the case Documents grid)

Use the document your court adopted in training; templates can vary by agency configuration.

## Regulatory / state packs

Thin Line includes Texas-oriented reporting packs for municipal court operations. Availability depends on your agency setup and permissions.

| Report pack | Typical purpose |
|-------------|-----------------|
| **OCA** | Office of Court Administration style monthly court activity reporting |
| **DPS conviction** | Weekly (Sun–Sat) conviction reporting to DPS. Generate on Monday for the prior week; due Tuesday |
| **State quarterly** | Quarterly state accounting / fee reporting |

These reports are for authorized court staff. Many packs are also launched from left-rail [Import/Export](../import-export/README.md) (**DPS Conviction**, **OCA**, **State Quarterly**). Agree one path per filing so staff do not produce conflicting files. Agency identifiers are configured during implementation.

### Preview (without filing)

Court Violations → **Reports** also includes **PREVIEW** cards for OCA, DPS conviction, and State Quarterly. Use preview to inspect matrix / period totals for a selected year and month (or week / quarter) **without creating an official submission**. When a stored preview exists, the card shows last-refreshed time. Filing and download still happen from [Import/Export](../import-export/README.md) (or the official report record after create).

## Analytics

Some environments include **court violation analytics** for volume and workload views. Treat analytics as operational insight, not a substitute for required state filings.

## Tips

- Run a sample period in a non-production or carefully reviewed run before the first live filing deadline after go-live.
- If totals look wrong, verify payment **acceptance**, dismissed/voided cases, and date filters before assuming a report defect.
- Online payment URL and related fields may appear on defendant-facing notices when configured.

## Related

- [Documents and forms](documents.md)
- [Import/Export](../import-export/README.md)
- [Payments](payments.md)
- [Work queues](work-queues.md)
- [Court overview](README.md)
