# PBFCM / Perdue Brandon — vendor outbound file runbook

Operational guide for Thin Line RMS outbound collections files (pipe-delimited `.TXT`) sent to Perdue Brandon Fulton Collins & Mott LLP (PBFCM).

Vendor layout templates (reference):

- `Reference Documents\Court\PurdueBrandon\UNT_NEW_PLACEMENTS.xlsx` (OneDrive)
- `Reference Documents\Court\PurdueBrandon\UNT_PaymentAdjustment_layout.xlsx` (OneDrive)
- `Reference Documents\Court\PurdueBrandon\UNT_ClosedCase_layout.xlsx` (OneDrive)

Sample files: `sample_NEW_PLACEMENTS.txt`, `sample_PAYMENT_ADJUSTMENT.txt`, `sample_CLOSED_CASE.txt`.

## What ships from Thin Line

Filename pattern (confirmed): `{AgencyName}_{yyyyMMdd}_{kind}.txt` where `kind` is `placements`, `adjustments`, or `closed`.

| File | Contents |
|---|---|
| `*_placements.txt` | **INITIAL** refers only (Account/Case required; citation & participant optional) |
| `*_adjustments.txt` | Court-side `PAYMENT` (**negative** amounts); supplemental **INCREASE** as positive `ADJUSTMENT`; court reductions / time served as negative `ADJUSTMENT`. Excludes CLR remittances |
| `*_closed.txt` | **Recalled / retracted** referrals only (not paid-in-full / SATISFIED) |

Confirmed format:

- Pipe-delimited (`|`), UTF-8, **header row included**
- Dates: `MM/dd/yyyy`
- Amounts: two decimal places; payments negative; increase adjustments positive; decrease/time-served adjustments negative
- PII: include SSN and DL when on file
- Empty files: **skip** (do not upload header-only)

## Clerk workflow

1. Open **Collections → Vendor File Export**.
2. Choose a **Period** and click **Generate files** (creates an export run; pipe `.TXT` bodies are archived on the run).
3. **Generate test** creates a realistic synthetic sample (`SampleMunicipalCourt_yyyyMMdd_*.txt`) with fictitious people and several scenarios. Marked `(test)`; excluded from the export watermark even if later transmitted.
4. On the run row: **Download** menu serves archived bytes as ZIP or each `.TXT`; **Transmit** uploads those same archived bytes via SFTP when configured.
5. **Export runs** lists recent batches. Monthly `CVO` writes to the same table (`IsScheduledRun`).

## Admin setup (SFTP)

1. **Admin → Agency → Third-Party Collections**
2. Set vendor name/contact as today.
3. Enable **Collections Vendor SFTP Export**.
4. Enter Host (IP from PBFCM), Port **22**, Username, Password, Upload Directory when provided.
5. Until host/credentials exist, generate/transmit still archives files; upload status = `SKIPPED` (not a failure).

## Cadence

- PBFCM prefers **batch** uploads (not near-real-time); most of their clients are **monthly**.
- Thin Line supports clerk-triggered generate/transmit and a monthly `CVO` job (5th of each month for the prior calendar month).

## Return / confirmation

- No return/ack file is sent to Thin Line / the vendor integration.
- PBFCM sends a confirmation to the **client** after data is entered in their system.
- A successful SFTP put is sufficient on our side; track status on **Export runs**.

## Automated monthly job

- Scheduler job type **`CVO`** (`COLLECTIONS VENDOR OUTBOUND`).
- Cron: `0 0 2 5 * ?` (02:00 UTC on the **5th** of every month), schedule mode `CRN`.
- Period: **previous calendar month** (1st through last day, UTC).
- Runs for agencies with Collections enabled **and** Collections Vendor SFTP Export enabled.
- Empty-file policy: **do not upload** header-only files.

## Status codes (`CollectionsVendorExportBatches`)

| Status | Meaning |
|---|---|
| `GENERATED` | Files built; upload not requested |
| `SENT` | At least one non-empty file uploaded |
| `SKIPPED` | SFTP not configured, or all files empty under default policy |
| `FAILED` | Generate or SFTP error (see `ErrorMessage`) |

## Vendor Q&A (answered 2026-07)

| Topic | Answer | Thin Line behavior |
|---|---|---|
| Identifiers | Account/Case mandatory; citation & participant optional | Still send citation / participant when present |
| Amounts | Payments negative; additional court charges positive; time served negative adjustment | Implemented |
| Format | Header, UTF-8, `MM/dd/yyyy` | Confirmed |
| PII | Include SSN/DL when on file | Confirmed |
| Increases | Positive adjustment (not placements) | Implemented |
| Closed | Recalled/retracted only | Implemented |
| Empty files | Skip | Confirmed |
| SFTP | Port 22; host/creds forthcoming; `ClientName_yyyymmdd_{placements\|closed\|adjustments}.txt` | Filename implemented; host/creds pending |
| Cadence | Batch preferred; most clients monthly | Clerk + monthly job on the 5th |
| Confirmation | No vendor return file; client gets confirmation after entry | No inbound ack job |

## UAT checklist with PBFCM

- [x] Header / UTF-8 / date format
- [x] Amount signs and INCREASE → adjustments
- [x] Closed = recalled only
- [x] Empty-file skip
- [x] Filename pattern
- [ ] Receive SFTP host IP + credentials
- [ ] Round-trip: Thin Line generate → their load → client confirmation path understood
- [ ] Confirm agency display name used as `ClientName` stem (sanitized)

## Related product paths

- UI: `/module/collections/vendor-export`
- API: `GET/POST …/tlsapi/court-violations/collections/vendor-export/*`
- Plan: `tls-docs-repo/internal/backlog/plans/collections-vendor-outbound-pbfcm-sftp.md`
