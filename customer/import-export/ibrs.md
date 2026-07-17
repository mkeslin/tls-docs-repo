# IBRS

Create, validate, download, and complete a monthly IBRS / NIBRS transmission.

## Create a transmission

1. Open **Import/Export** → **IBRS**.
2. **Create IBRS Transmission** — confirm agency, **Report Year**, **Report Month** (defaults often to the previous month).
3. Choose **Create**.
4. Open the new transmission.

## Validate and fix errors

1. Review tabs **Details** and **Errors/Warnings**.
2. If errors exist, open the listed incidents and fix data quality ([Incidents](../rms/incidents/README.md), [Data quality checklist](data-quality-checklist.md)).
3. Return to the transmission → **Rebuild & Validate**.
4. Repeat until errors are clear (warnings may remain per your state process).

You generally cannot finish a clean download while blocking errors remain.

## Download and submit

1. When validation is clean, **Download IBRS File**.
2. Submit the file through your state process (for example Texas DPS portal — use the login link your screen provides).
3. When you receive an EDS / result file, **Upload EDS result file** on the transmission.
4. Use **View History** for prior months.

Exclude selected incidents from a transmission only when your agency process allows it.

## Tips

- Assign one primary submitter per period so two people do not overlap months.
- Fix incidents at the source — rebuild does not invent missing NIBRS data.
- Support-only debug downloads are not part of agency training.

## Related

- [Data quality checklist](data-quality-checklist.md)
- [Incidents — Print, attachments, history, and IBRS](../rms/incidents/print-attachments-history-ibrs.md)
