---
backlog: "BL-001 · Court Violations · OCA Report — verify February data"
status: draft
created: 2026-03-30
---

# Plan: BL-001 — OCA February data verification

## Goal

Confirm **February 2026** OCA municipal XML is **correct in Thin Line**, **accepted by the Texas OCA portal** (CARD), and explain or resolve the **upload failure** you hit.

---

## What failed (from your screenshot)

Failure is in the **Office of Court Administration (OCA) Electronic File Submission** app (**CARD**), not in Thin Line RMS:

- **Exception:** `System.NullReferenceException` at  
`OCA.CARD.BusinessLogic.JusticeAndMunicipal.Categories.Import(..., BaseReport previousMonthReport)` — **line 109** in `Categories.cs`.
- **Call chain:** `MunicipalReport.Import` → `BaseSection.Import` → `Categories.Import`.

**Implication:** Fixing this requires **CARD / OCA** server code or **operational data** on their side (e.g. prior-month report record). The Thin Line repo does **not** contain `C:\CARD\CARD.Web\...`.

### Leading hypothesis (portal-side)

The method takes **`previousMonthReport`**. For a **February** upload, the importer typically loads **January** as the prior month. If **no accepted January report exists** in CARD for court `721520500`, that object can be **null** and cause an NRE if the code does not guard it.

**Check first:** In OCA/CARD, confirm whether **January 2026** was **submitted and accepted** for the same **court identifier** (`721520500`) before retrying February.

### Wrong file uploaded as “January” (August XML)

If court staff (or a judge) **intended** to file **January 2026** but uploaded a file whose **XML header is still August 2025** (`REPORTINGMONTH` 08 / `REPORTINGYEAR` 2025), CARD will index that submission as **August 2025**, not January 2026. **January 2026** can therefore remain **missing**. When **February 2026** is uploaded, the importer still looks for **January 2026** as `previousMonthReport` → **null** → same **`NullReferenceException`** pattern.

So a mistaken August-for-January upload **does not** satisfy the prior-month slot February needs; it only adds confusion. **Remediation:** ensure a **correct January 2026** XML is submitted and **accepted**, then retry February.

---

## Files you provided


| File                                              | Actual period (from XML header)                                     | Notes                                                                                                                                                               |
| ------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OCA_Report_2026-2(February)_2_1774008649230.xml` | **February 2026** (`REPORTINGMONTH` 02, `REPORTINGYEAR` 2026)       | Matches upload scenario. `COURTIDENTIFIER` **721520500**.                                                                                                           |
| `OCAReport1_31_20266_27 AM (4) (1).xml`           | **August 2025** (`REPORTINGMONTH` **08**, `REPORTINGYEAR` **2025**) | **Not** January 2026 — filename/metadata is misleading for a “January vs February” diff. Use a **January 2026** export for a true month-over-month compare in CARD. |


Same court ID on both samples: **721520500**.

---

## Structural differences (February 2026 vs August 2025 sample)

These are **different reporting months and schema eras**; treat as **illustrative**, not a strict January-vs-February diff.

- **`LINENUMBER`:** August sample uses **1001, 1002, 1003…**; February 2026 uses small integers (**1**, **1**, **1** for lines 1a / 1b / rollup line 1). CARD may key logic on line + description; both can be valid if generated consistently.
- **`desc` text:** Wording differs (e.g. “New Cases Filed **During Month**” vs “New Cases Filed”; “Total Cases **on** Docket” vs “Total Cases **On** Docket”). OCA has renamed labels over time; your **February** file follows **current-style** labels consistent with a newer generator.
- **Column completeness:** In the August sample, at least one **8a**-style category is **incomplete** (only `Traffic_NonParking` present). A **current** export should emit **all** measure columns for each category where required by schema. The **February** file shows full six columns for the lines sampled.

---

## Thin Line RMS (this repo)

- OCA XML is produced by **`OcaXmlGenerator`** (`ThinLine.Business.Objects/Court/Oca/OcaXmlGenerator.cs`): `CriminalCategory` uses `Desc`, `Line`, `LineNumber`, and the six count columns from `IOcaRecord` data.
- **BL-001** can include:
  - **Data validation:** Reconcile February **criminal** (and other sections) counts against RMS / OCA detail screens and health checks.
  - **Export validation:** Confirm generated XML is **well-formed**, matches **agency court identifier**, and matches **expected line list** for the reporting month (`OcaCriminalReportLabels` and related mapping).
  - **Portal:** If CARD still NREs after **January 2026** is confirmed accepted, escalate to **OCA** with the stack trace and both XML attachments.

---

## Checklist (verification)

### OCA portal / process

- Confirm **January 2026** report status for **721520500** (submitted / accepted / missing).
- Ask whether an **August 2025** (or other wrong-month) file was ever submitted in place of January — if so, **January 2026** may still be absent; correct January must be on file.
- Retry **February** upload after January is accepted; capture any new error text.
- If failure persists with January on file, open **OCA/CARD support** with screenshot + stack trace + both XML files.

### Data / Thin Line (optional but aligned with BL-001)

- Spot-check February **OCA** numbers in RMS against source queries / OCA tab on sample violations.
- Regenerate February XML from RMS and compare to the file you uploaded (hash or diff) to ensure the file tested is what RMS emits.

### Reference XML

- Obtain **January 2026** XML export (same court) for a proper **month-over-month** structural diff; replace the August 2025 sample for that purpose.

---

## Changelog


| Date       | Notes                                                                           |
| ---------- | ------------------------------------------------------------------------------- |
| 2026-03-30 | Initial scope: CARD NRE + XML comparison + Thin Line `OcaXmlGenerator` pointer. |
| 2026-03-30 | Noted: wrong-month upload (e.g. August XML as “January”) leaves Jan 2026 missing → Feb upload NRE risk. |


