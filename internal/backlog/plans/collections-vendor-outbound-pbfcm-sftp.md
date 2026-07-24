---
backlog: "TBD · Court / Accounting · Collections vendor outbound files (PBFCM / Perdue Brandon SFTP)"
status: done
created: 2026-07-22
updated: 2026-07-24
---

# Plan: Collections vendor outbound files (PBFCM SFTP)

## Goal

Send Perdue Brandon Fulton Collins & Mott LLP (PBFCM) pipe-delimited `.TXT` files over SFTP for (1) new placements, (2) payments/adjustments taken at the court (not at PBFCM), and (3) closed/recalled cases — using the layouts in their UNT templates.

## Implementation progress

- **Phase A (done):** pipe formatters, export service, date-window queries, API download endpoints, Collections UI page, unit tests.
- **Phase B (done):** per-agency SFTP settings, SFTP client, export batch audit table, monthly `CVO` scheduler job (5th for prior month), Generate & send API/UI. Upload skipped until host/credentials exist.
- **Phase C (done):** last-run status UI/API, empty-file upload policy (skip header-only by default; `CollectionsVendor:UploadEmptyFiles` override), runbook + sample `.TXT` files under `Docs/Court/PurdueBrandon/`.

## Ops references

- Runbook: product-repo `Docs/Court/PurdueBrandon/PBFCM-VENDOR-OUTBOUND-RUNBOOK.md`
- Samples: `sample_NEW_PLACEMENTS.txt`, `sample_PAYMENT_ADJUSTMENT.txt`, `sample_CLOSED_CASE.txt`

## Implementation notes (post Phase C + vendor Q&A)

- Export runs archive the three pipe `.TXT` bodies on `CollectionsVendorExportBatches`; download/transmit use archived bytes.
- Filenames: `{AgencyName}_{yyyyMMdd}_{placements|adjustments|closed}.txt`.
- Payments negative; INCREASE → positive ADJUSTMENT; DECREASE/time-served → negative ADJUSTMENT; closed = recalled only.
- **Generate test** / `IsTestRun` excluded from the export watermark.
- Monthly `CVO` (cron `0 0 2 5 * ?`, previous calendar month) uses the same runs table (`IsScheduledRun`).

## Remaining

- Enter SFTP host IP + credentials when PBFCM provides them (port 22).
- Confirm sanitized agency `Name` is acceptable as `ClientName` stem (or add a dedicated field).

Canonical runbook: product-repo `Docs/Court/PurdueBrandon/PBFCM-VENDOR-OUTBOUND-RUNBOOK.md`.
