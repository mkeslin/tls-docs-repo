# Court documents and forms

Court Violations generates Texas municipal-court style PDFs from the case. Templates can vary by agency letterhead, seal, and judge signature images.

State filings (OCA, DPS conviction, State Quarterly) are separate — see [Reports](reports.md).

**How to read the grid**

| Column | Meaning |
|--------|---------|
| **Used?** | Whether clerks use it in a live workflow (**Yes**), it is created automatically, it is Support-only, or it is **not** offered. |
| **How** | What happens: clerk print, batch print, auto-attach, kiosk signing, electronic warrant issuance, or retired. |
| **Where** | The screen or queue. **Documents** = case utility drawer → Documents grid (age rules may hide a row). **Sample court forms** = Thin Line Support only (same court forms, sample data; citation copies are not on that page). |

Many work-queue print actions stay disabled until every row on the page has a show-cause date.

---

## Catalog

| Form | Used? | How | Where |
|------|-------|-----|-------|
| **Court violation summary** (Overview) | Yes | Clerk prints a case statement / cover sheet (not OCA). | Case **Print Overview**. Also on Sample court forms. |
| **Citation Details (Full)** | Yes | Clerk prints the full citation packet from the linked citation. Often auto-attached at intake when a citation PDF can be generated. | Case **Print Citation**; **New Case Review** → Batch Print → Citation Details (Full); Attachments tab when auto-saved. Needs a live citation — **not** on Sample court forms. |
| **Citation Details (Public)** | Yes | Clerk prints the public citation copy. | Case **Print Citation**. Needs a live citation — **not** on Sample court forms. |
| **Citation Details (Court copy)** | Yes | Clerk prints the court-copy citation. | Case **Print Citation**. Needs a live citation — **not** on Sample court forms. |
| **Envelope** | Yes | Clerk prints a mailing envelope for the defendant. | Documents; **New Case Review** → Batch Print → Envelopes; Sample court forms. |
| **FTA / missed-appearance address labels** | Yes | Batch-prints Avery-style address labels for mailing notices. Not a single-case Documents item. | **FTA — Missed Appearance**, **Program Failures — Show Cause Required**, **Compliance — Missed Deadline**, and **Compliance — Missed Payment** → Batch Print → Address labels (sheet). **Not** on Documents. |
| **Complaint** | Yes | Clerk can print a filled complaint. The **electronically sworn** layout is auto-attached when the court violation is created from a citation with an officer certification date. After officer sign, complaint text is **locked**. Cases already past **New** that still need a court jurat appear on **Complaint Jurat Needed** — use **Execute Complaint Jurat** (batch) to store the final court-signed PDF without changing case state. Empty / filled / e-signed layouts exist. | Documents (filled); Attachments tab (e-signed auto-attach at intake); **Complaint Jurat Needed** work queue; Sample court forms (including e-signed reprint). No auto-attach until the citing officer certified the citation. |
| **Complaint (blank / empty body)** | Support / special | Empty-body complaint (header/footer from the case) for manual completion. | Sample court forms → complaint **Empty**. Not a separate Documents title. |
| **Initial Court Setting Notice** | Yes | Clerk prints the first-appearance / setting letter. | Documents; Sample court forms. |
| **Pre-Trial Setting Notice** | Yes | Clerk prints the pre-trial setting letter after a not-guilty / pre-trial path. | Documents; Sample court forms. |
| **Summons for Defendant** | Yes | Clerk prints a defendant summons. | Documents; Sample court forms. |
| **Jury Summons** | Yes | Clerk prints a jury summons. | Documents; Sample court forms. |
| **School/Work Excuse** | Yes | Clerk prints an excuse letter for school or work from a court setting. | Documents; Sample court forms. |
| **FTA 10 Day Notice** | Yes | Clerk prints a ten-day FTA notice (separate from the FTA show-cause letter used in the missed-appearance queue). | Documents; Sample court forms. |
| **Late Notice Letter** | Yes | Clerk prints a late / missed-payment notice; also batched for the missed-payment queue. | Documents; **Compliance — Missed Payment** → Batch Print → Late Notice Letter; Sample court forms. |
| **Notice Following Plea by Mail** | Yes | Clerk prints the follow-up notice after a mailed plea. | Documents; Sample court forms. |
| **Plea Form (By Mail)** | Yes | Clerk prints the mail plea form; can be included in a kiosk signing packet. | Documents; kiosk document signing (from the case); Sample court forms. |
| **Plea Form (In Person)** | Yes | Clerk prints the in-person plea form; batch-prints for new cases; kiosk: defendant chooses plea, signs, and the signed PDF attaches to the case. | Documents; **New Case Review** → Batch Print → Plea - In Person; kiosk document signing; Sample court forms. |
| **Plea / no contest at payment** | Yes (automatic) | System attaches the plea PDF when payment records a no-contest (or equivalent) plea. Clerks do not pick this from Documents. | Attachments tab after online or window payment on that path. **Not** on Documents. |
| **Judgment** | Yes | Clerk prints the judgment; also batched for new-case review. | Documents; **New Case Review** → Batch Print → Judgments; Sample court forms. |
| **Judgment Not Guilty (Adult and Juvenile)** | Yes | Clerk prints the not-guilty / acquittal judgment. | Documents; Sample court forms. |
| **Judgment/Jury Waived Guilty** | Yes | Clerk prints the jury-waived guilty judgment. | Documents; Sample court forms. |
| **Judgment/Jury Verdict (Juvenile)** | Yes | Clerk prints the juvenile jury-verdict judgment. Hidden unless age at offense is under 17. | Documents (juvenile-at-offense only); Sample court forms. |
| **Judgment — Alcohol by Minor** | Yes | Clerk prints the alcohol-by-minor judgment. Hidden unless age at offense is under 21. | Documents (under 21 at offense); Sample court forms. |
| **Motion and Order to Dismiss** | Yes | Clerk prints the motion and order to dismiss. | Documents; Sample court forms. |
| **Dismissal: Compliance Dismissal** | Yes | Clerk prints the compliance-dismissal order (for example after program completion). | Documents; Sample court forms. |
| **Jail Credit Addendum** | Yes | Clerk prints jail-credit language. Hidden if under 17 at offense. | Documents (adult only); Sample court forms. |
| **Order of Commitment** | Yes | Clerk prints an order of commitment. Hidden if under 17 at offense. | Documents (adult only); Sample court forms. |
| **Chemically Dependent Person Order** | Yes | Clerk prints that order when the court uses it. | Documents; Sample court forms. |
| **Juvenile Continuing Obligation** | Yes | Clerk prints juvenile continuing-obligation language. | Documents; Sample court forms. |
| **DPS Correction Form** | Yes | Clerk prints a DPS correction form. | Documents; Sample court forms. |
| **Deferred Disposition Order** | Yes | Clerk prints the standard deferred-disposition order when granting that program. | Documents; Sample court forms. See [Court programs](court-programs.md). |
| **Deferred Disposition Order (Under 25)** | Yes | Clerk prints the under-25 deferred order. Hidden unless age at offense is under 25. | Documents (under 25 at offense); Sample court forms. |
| **Deferred Disposition: Extension** | Yes | Clerk prints a deferral extension. | Documents; Sample court forms. |
| **Deferred Disposition Show Cause** | Yes | Clerk prints the deferred show-cause letter. Also produced when **Missed Deadline Show Cause** resolves to a deferred condition. | Documents; also via **Program Failures — Show Cause Required** → Batch Print → Missed Deadline Show Cause (when the unmet condition is deferred); Sample court forms. |
| **Court Program Show Cause** | Yes | Clerk prints the generic (non-deferred / non-DSC) program show-cause letter. Also produced when **Missed Deadline Show Cause** resolves to a generic program condition. | Documents; also via **Program Failures — Show Cause Required** → Batch Print → Missed Deadline Show Cause (when the unmet condition is a generic program); Sample court forms. |
| **Missed Deadline Show Cause** | Yes | Clerk or batch print; the system picks **Deferred**, **DSC**, or **Court Program** show-cause text from the case’s past-due program conditions. | Documents; **Program Failures — Show Cause Required** → Batch Print → Missed Deadline Show Cause; Sample court forms. |
| **DSC Request Packet** | Yes | Clerk prints the driver safety course request packet. | Documents; Sample court forms. |
| **DSC Show Cause** | Yes | Clerk prints DSC show cause. Also produced when **Missed Deadline Show Cause** resolves to a DSC condition. | Documents; also via **Program Failures — Show Cause Required** batch (when the unmet condition is DSC); Sample court forms. |
| **DSC Final Judgment** | Yes | Clerk prints the DSC final judgment. | Documents; Sample court forms. |
| **DSC Court Order** | No (not in clerk list) | Factory exists internally; clerks do not see it on Documents. Use DSC Request Packet, DSC Show Cause, and DSC Final Judgment instead. | Not on Documents. |
| **Teen Court Request** | Yes | Clerk prints the teen-court request. | Documents; Sample court forms. |
| **Teen Court Order** | Yes | Clerk prints the teen-court order. | Documents; Sample court forms. |
| **Teen Court Jury Instructions** | Yes | Clerk prints teen-court jury instructions. | Documents; Sample court forms. |
| **Teen Court Community Service Referral** | Yes | Clerk prints the teen-court community-service referral. | Documents; Sample court forms. |
| **Application for Time Payment, Extension, Community Service, or Waiver** | Yes | Clerk prints the time-payment / extension / community-service / waiver application. | Documents; Sample court forms. See [Payment plans](payment-plans.md). |
| **Installment Agreement Order** | Yes | Clerk prints the installment-plan order. | Documents; Sample court forms. |
| **Community Service Order** | Yes | Clerk prints a community-service order. | Documents; Sample court forms. |
| **Show Cause** | Yes | Clerk prints the FTA / general show-cause notice; also batched as the FTA missed-appearance notice and as the violator letter on the surety queue. | Documents; **FTA — Missed Appearance** → Batch Print → Show Cause Notice; **Surety Bond — Show Cause** → Batch Print → Violator Show Cause; Sample court forms. See [FTA, warrants, and bonds](fta-warrants-bonds.md). |
| **Show Cause Capias Pro Fine** | Yes | Clerk prints the CPF show-cause notice; also batched on compliance queues. Hidden if under 17 at offense. | Documents (adult only); **Compliance — Missed Deadline** and **Compliance — Missed Payment** → Batch Print → Show Cause Capias Pro Fine; Sample court forms. |
| **Bond Company Show Cause** | Yes | Clerk prints the surety / bond-company show-cause letter; also batched on the surety queue. | Documents; **Surety Bond — Show Cause** → Batch Print → Bond Company Show Cause; Sample court forms. |
| **Arrest Warrant** | Yes | Clerk can print from the case (adult). **Issuance** is electronic: Issue Warrants attaches an **e-signed** PDF to the **warrant** (not batch-printed as blank paper). Empty / filled / e-signed layouts exist. Hidden if under 17 at offense. | Documents (adult only); **FTA — Missed Show Cause** → **Issue Warrants** (e-signed PDF on the warrant); Sample court forms. |
| **Warrant: Capias Pro Fine** | Yes | Same pattern as arrest warrant, for post-judgment CPF. Hidden if under 17 at offense. | Documents (adult only); **Compliance — Missed Show Cause** → **Issue Warrants** (e-signed PDF on the warrant); Sample court forms. |
| **Affidavit for Probable Cause for Failure to Appear** | Yes | Clerk prints the court FTA probable-cause affidavit. | Documents; Sample court forms. |
| **Affidavit for Probable Cause for Failure to Appear (Citation)** | Yes | Clerk prints the citation-based FTA probable-cause affidavit. | Documents; Sample court forms. |
| **Clerk’s Affidavit for Capias Pro Fine** | Yes | Clerk prints the clerk CPF affidavit. Hidden if under 17 at offense. | Documents (adult only); Sample court forms. |
| **Violation of Promise to Appear** | Yes | Clerk prints the violation-of-promise-to-appear form. | Documents; Sample court forms. |
| **Warrant: Capias** (Chapter 23) | No | Retired. FTA uses **Arrest Warrant**. | Not offered in the clerk UI. |
| **Affidavit for Probable Cause** (generic) | No | Not offered. Use the FTA affidavits above. | Not offered in the clerk UI. |
| **Deferred Disposition Final Judgment** | Yes | Clerk prints the deferred-disposition final judgment. | Documents; Sample court forms. See [Court programs](court-programs.md). |

---

## Tips

- Print from the **case** when you need one form; use **work-queue batch print** when you are mailing a queue of notices or labels.
- **Issue Warrants** is the issuance path — it creates the electronic warrant PDF. FTA / CPF show-cause queues do not batch-print warrant paper.
- If a form is missing from Documents, it is usually an age-at-offense rule (adult-only warrants/CPF, juvenile jury verdict, under-21 alcohol judgment, under-25 deferred).
- Online payment URL and related fields may appear on defendant-facing notices when configured.

## Related

- [Reports](reports.md)
- [Work queues](work-queues.md)
- [Getting around](getting-around.md)
- [Pleas and judgment](pleas-and-judgment.md)
- [Court programs](court-programs.md)
- [FTA, warrants, and bonds](fta-warrants-bonds.md)
- [Payment plans](payment-plans.md)
- [Court overview](README.md)
