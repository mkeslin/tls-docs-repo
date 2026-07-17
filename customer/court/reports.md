# Reports

Court reporting and operational prints commonly used with Court Violations.

## Operational reports and documents

From a case or module reports area, clerks commonly generate:

- Court violation overview / statement style reports
- Notices (for example pre-trial setting, show cause, late notice)
- Deferred disposition / court program and installment agreement documents
- Receipts (final receipts after payment acceptance)
- Citation prints from a court violation when needed
- Label outputs used for FTA address mailings (when configured)

Use the document your court adopted in training; templates can vary by agency configuration.

## Regulatory / state packs

Thin Line includes Texas-oriented reporting packs for municipal court operations. Availability depends on your agency setup and permissions.

| Report pack | Typical purpose |
|-------------|-----------------|
| **OCA** | Office of Court Administration style monthly court activity reporting |
| **DPS conviction** | Conviction reporting to DPS |
| **State quarterly** | Quarterly state accounting / fee reporting |

These reports are for authorized court staff. Many packs are also launched from left-rail [Import/Export](../import-export/README.md) (**DPS Conviction**, **OCA**, **State Quarterly**). Agree one path per filing so staff do not produce conflicting files. Agency identifiers are configured during implementation.

## Analytics

Some environments include **court violation analytics** for volume and workload views. Treat analytics as operational insight, not a substitute for required state filings.

## Tips

- Run a sample period in a non-production or carefully reviewed run before the first live filing deadline after go-live.
- If totals look wrong, verify payment **acceptance**, dismissed/voided cases, and date filters before assuming a report defect.
- Online payment URL and related fields may appear on defendant-facing notices when configured.

## Related

- [Import/Export](../import-export/README.md)
- [Payments](payments.md)
- [Work queues](work-queues.md)
- [Court overview](README.md)
