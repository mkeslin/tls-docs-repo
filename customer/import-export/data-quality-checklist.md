# Data quality checklist

Fix source records **before** Create / Rebuild / Download. Exports do not invent missing facts.

## IBRS

- [ ] Incidents for the month are approved / complete per agency NIBRS rules
- [ ] Offenses, victims, offenders, property, and arrest segments required by your state are populated
- [ ] Rebuild & Validate shows no blocking errors ([IBRS](ibrs.md))

## Racial profiling

- [ ] Citations (and related stops) have required RP fields completed
- [ ] Officers trained on [Citations — Racial profiling](../rms/citations/racial-profiling.md)
- [ ] Date range matches the submission period

## DPS Conviction / OCA / State Quarterly

- [ ] Agency identifiers configured (DPS location code / OCA id as required)
- [ ] Dispositions and conviction data for the period are complete on court violations
- [ ] Agreed single submitter and calendar (month vs quarter)

## General

- [ ] Correct **agency** in the header before creating a transmission
- [ ] Training tenant used for rehearsal; production only for real submissions
- [ ] Copies retained per records retention

## Related

- [Opening Import/Export](opening-import-export.md)
- [Support](../support/README.md)
