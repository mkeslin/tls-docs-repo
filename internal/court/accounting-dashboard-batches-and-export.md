# Accounting manual — Posting batches and exporting transaction data (Dashboard)

**Audience:** Accountants and finance staff using Thin Line RMS **Accounting**.

**Scope:** This document covers only:

1. **Posting batches** from the **Accounting Dashboard**.
2. **Downloading city GL exports** (**Tyler ERP** plain text and/or **CentralSquare** JE CSV) for posted batches from the same dashboard.

Other accounting screens (transaction search, settlement batch search, reconciliation, etc.) are out of scope here.

---

## Before you start

- You need **Accounting** access (claim `Rms.Accounting.Access` in your agency).
- Open the **Accounting** module from the app navigation. The default landing page is the **Accounting Dashboard** (`SimpleDashboard` in the product).

---

## 1. Accounting Dashboard layout

The **Accounting Dashboard** has two tabs:

| Tab | Purpose |
|-----|--------|
| **Processing** | Today’s workflow: status, **cash/check/money order** pending deposit, **credit card** payout batches ready to post, and **batches posted today**. |
| **History** | Choose a **business date** and see **batches posted** on that date (same actions as below for reports and export). |

Use **Processing** for day-to-day posting. Use **History** when you need a **past date** or to re-download an export for a batch that was posted earlier.

---

## 2. Posting batches — cash, check, and money order

These payments accumulate in a **pending** state until you build **deposit** and **revenue allocation** batches and post them.

1. On the **Processing** tab, find the card **Cash, Check & Money Order Payments**.
2. Review the **Deposit Batch** and **Revenue Allocation** summary (amounts by cash, check, money order, and totals).
3. When you are ready to post **selected** transaction sets into new batches and post them in one step:
   - Click **Create & Post Batches** (primary button).
   - In the dialog **Create & Post Batches**, review the list of **pending transaction sets** (transaction number, date, amount, payment method, description).
   - Use the checkboxes to include or exclude rows. By default, all pending rows are selected.
   - Click **Create & Post Batches** to confirm. The system creates the new batches and **posts** them immediately.

**If there is nothing to post:** The card may show **No batches to post** or no pending deposit rows when there are no pending items.

**If you only need a preview:** When the UI offers **Preview Payment Report** (context-dependent), you can use it to review before posting.

---

## 3. Posting batches — credit card (Stripe payout)

Card payments are processed in **settlement / payout** batches. When a batch is ready and your user is allowed to post it:

1. On the **Processing** tab, open the **Credit Card Payments** card.
2. Find a row that shows **Post** (only when the batch is eligible to post).
3. Click **Post** to complete that payout batch.

You can use **Preview Payment Report** on a row when available to review before posting.

---

## 4. Exporting transaction data — city GL (Tyler ERP and CentralSquare)

After batches are **posted**, use the **download** control (document + down-arrow) on each batch row; hover shows **Export journal entries**, and the menu lists **Tyler ERP** and **CentralSquare Asyst**.

### Where to find it

- **Processing** tab — table **Batches Posted Today**: each row includes the combined JE export menu when available.
- **History** tab — pick a **date**, then use **Batches Posted for Selected Date**; the same control appears per batch.

### What you get

**Tyler ERP**

- Content type **text/plain** (comma-separated values in plain text lines; first line balances cash `99`,`1000` with summed credits).

**CentralSquare**

- **Comma-separated** rows suitable for CentralSquare **JE Import** (**no header row**; padded amounts). Download uses **`text/plain`** with a **`.txt`** filename to match **ASCII** plain-text JE import expectations (vendor doc wording may say “ACHII”).

Typical filenames from the dashboard (`GL_Export_{Type}_{Id}_{Date}_{Amount}_{Vendor}.txt`):

| Batch kind | Tyler ERP (`text/plain`) | CentralSquare (`text/plain`, `.txt`) |
|------------|---------------------------|--------------------------------------|
| Deposit (cash/check/money order) | `GL_Export_Deposit_{batchId}_{yyyy-MM-dd}_{amount}_Tyler.txt` | `GL_Export_Deposit_{batchId}_{yyyy-MM-dd}_{amount}_CentralSquare.txt` |
| Card payout (settlement) | `GL_Export_Payout_{batchId}_{yyyy-MM-dd}_{amount}_Tyler.txt` | `GL_Export_Payout_{batchId}_{yyyy-MM-dd}_{amount}_CentralSquare.txt` |

Amount is two decimals. A pending bundle uses `GL_Export_Bundle_{Kind}_{n}items_{date}_{amount}_{Vendor}.txt`.

### Related actions (not the same as the export file)

- **Payment report** (printer + down-arrow): opens a menu with **View PDF** (in-app viewer) and **Download PDF** (saves the file) — useful for audit; not the same as the GL exports.

---

## 5. Quick reference

| Task | Where | Control |
|------|--------|---------|
| Post cash/check/money order from pending | Processing → **Cash, Check & Money Order Payments** | **Create & Post Batches** → confirm in dialog |
| Post credit card payout batch | Processing → **Credit Card Payments** | **Post** on an eligible row |
| Download Tyler ERP / CentralSquare Asyst JE exports | Processing (**Batches Posted Today**) or **History** (date + batch list) | JE export (**Export journal entries**) → **Tyler ERP** / **CentralSquare Asyst** |
| Download **PDF** payment report | Same batch rows | **Payment report** menu → **View PDF** or **Download PDF** |

---

## Changelog

| Date | Notes |
|------|--------|
| 2026-05-19 | Dashboard / accounting batch grids: JE export tooltip **Export journal entries**, menu labels **Tyler ERP** / **CentralSquare Asyst**, aligned toolbar controls; tertiary **payment report** + JE export (**tls-btn**, **View PDF** / **Download PDF**); **`text/plain`** `.txt` CentralSquare JE files (**ASCII**; vendor wording may say “ACHII”). |
| 2026-03-30 | Initial manual from `SimpleDashboard.vue` / `CreateAndPostBatchFromPendingDialog.vue` behavior. |
