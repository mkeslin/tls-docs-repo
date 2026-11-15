# CentralSquare (Asyst) JE import — ThinLine export

This folder holds the **CentralSquare / Asyst** JE import specification and example workbook:

- `Reference Documents\Court\CentralSquare\JE Import File Specifications.docx` (OneDrive; PDF copy alongside)
- `Reference Documents\Court\CentralSquare\JE Import Example 1.xlsx` (OneDrive)

## RMS implementation

Court revenue allocation exports can be downloaded from the accounting UI (**Export journal entries** → **CentralSquare Asyst**) as a **comma-delimited** plain-text **`.txt`** file (**ASCII** comma-delimited JE rows per spec—doc may say “ACHII”; **no header row**):

- **Same credit aggregation** as the Tyler ERP (“city GL”) export: posted allocation transaction lines with `CreditAmount > 0`, rolled up by account code (combined deposit + RA exports aggregate and net wash accounts first).
- **Source / Type:** `AR` + `CR` (cash receipts) for deposit, settlement, and revenue-allocation exports; `AP` + `CD` (cash disbursements) for refund, collections, and state remittance exports.
- **Pending bundle export:** when multiple queue items are combined, Trans Number is renumbered sequentially (`1`, `2`, `3`, …) per balanced journal entry so merged files do not reuse the same Trans Number across batches.
- **Balancing cash debit:** resolved from the chart row for `OPERATING_BANK_ACCOUNT` (`AccountingAccounts.AccountNumber`, punctuation stripped for Asyst — e.g. `10.102` → `10102`). No account-code substitution at export time.
- **Revenue / payable lines:** account numbers from the chart of accounts: `AccountNumber` with `-`, `.`, and `,` removed; export fails if any line’s account code lacks `AccountNumber`.
- **Numeric amounts:** padded `000000000.00` (9-digit integer portion per spec examples); **not quoted**.
- **Numeric identifiers** (Trans Number, Vendor Number, Check Number, Fiscal Period, Project Number): fixed width per spec; **not quoted**.
- **Text columns:** comma-delimited with **every text field wrapped in double quotes**; unneeded text fields use a **single blank space** (`" "`).

Prefer importing that **`.txt`** file **without opening it first in Excel** (leading zeros can be damaged per vendor notes in the specification).
