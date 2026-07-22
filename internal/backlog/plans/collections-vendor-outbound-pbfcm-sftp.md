---
backlog: "TBD · Court / Accounting · Collections vendor outbound files (PBFCM / Perdue Brandon SFTP)"
status: done
created: 2026-07-22
updated: 2026-07-22
---

# Plan: Collections vendor outbound files (PBFCM SFTP)

## Goal

Send Perdue Brandon Fulton Collins & Mott LLP (PBFCM) pipe-delimited `.TXT` files over SFTP for (1) new placements, (2) payments/adjustments taken at the court (not at PBFCM), and (3) closed/recalled cases — using the layouts in their UNT templates.

## Implementation progress

- **Phase A (done):** pipe formatters, export service, date-window queries, API download endpoints, Collections UI page, unit tests.
- **Phase B (done):** per-agency SFTP settings, SFTP client, export batch audit table, nightly `CVO` scheduler job, Generate & send API/UI. Upload skipped until host/credentials exist.
- **Phase C (done):** last-run status UI/API, empty-file upload policy (skip header-only by default; `CollectionsVendor:UploadEmptyFiles` override), runbook + sample `.TXT` files under `Docs/Court/PurdueBrandon/`.

## Ops references

- Runbook: product-repo `Docs/Court/PurdueBrandon/PBFCM-VENDOR-OUTBOUND-RUNBOOK.md`
- Samples: `sample_NEW_PLACEMENTS.txt`, `sample_PAYMENT_ADJUSTMENT.txt`, `sample_CLOSED_CASE.txt`

## Remaining after PBFCM call

- Confirm layout defaults (IDs, Transaction Type, dates, PII, empty-day behavior).
- Enter SFTP host/path/credentials on the agency.
- Optional filename-pattern tweaks if they require a specific convention.
