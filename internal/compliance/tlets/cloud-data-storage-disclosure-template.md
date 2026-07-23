# Cloud data storage and third-party vendor disclosure

**Status:** Internal working template — Thin Line completes deployment facts; agency reviews and includes the approved version in its interface packet.  
**Purpose:** Documents where Thin Line RMS/CAD/JMS solution data is stored and identifies third parties involved in storage, backup, authentication, messaging, telemetry, or other processing that may retain agency or CJI-related data.  
**Download:** [Editable Word template](forms/cloud-data-storage-disclosure-template.docx)  
**Handling:** Mark the completed attachment **FOR OFFICIAL USE ONLY (FOUO)** or with the agency/DPS-required handling label.

Thin Line owns the accuracy of the cloud architecture and vendor details. The agency owns acceptance and submission. Do not submit unverified regions or a vendor list copied from another agency without a current production check.

**Companion workbook (incorporated by reference):** Detailed **Cloud Storage Inventory** and **Third-Party Vendor Register** tables are maintained in the Thin Line TLETS equipment and cloud worksheet workbook (Excel) submitted with this packet. Those sheets are part of this disclosure and are not duplicated here because the columns do not fit a Word layout.

---

## 1. Submission information

| Field | Entry |
|---|---|
| Agency | `[AGENCY NAME]` |
| ORI | `[ORI]` |
| Thin Line tenant key | `[TENANT KEY]` |
| Products in scope | RMS / CAD / JMS *(delete products not purchased)* |
| Production environment | `[ENVIRONMENT NAME]` |
| Effective date | `[YYYY-MM-DD]` |
| Thin Line preparer/reviewer | `[NAME / TITLE]` |
| Agency reviewer | `[NAME / TITLE]` |
| Related network diagram revision | `[TITLE / REVISION / DATE]` |
| Companion workbook filename / revision | `[e.g. 41 equipment-worksheet.xlsx — REVISION / DATE]` |

---

## 2. Packet-ready summary

> Thin Line Software LLC hosts **`[AGENCY NAME]`**’s Thin Line **RMS/CAD/JMS** production environment in **Microsoft Azure Government**. Primary application data is stored in Azure SQL Database **`tls-[tenant]-prod-rms`** on logical server **`tls-db2`** in **USGov Texas**. File attachments are stored in Azure file storage under share label **`tls-[tenant]-prod-fileshare`** in **USGov Texas** (map to the current storage account ARM object in the companion workbook). Backups and recovery copies are maintained through **Azure SQL point-in-time restore (PITR)** and **long-term retention (LTR: weekly P8W / monthly P1Y / yearly P10Y; time-based immutability Disabled)** within the Azure SQL backup scope for **USGov Texas**. Application and security telemetry are stored in **Azure Application Insights / related Azure Monitor logging** in **USGov Virginia**, subject to the retention shown in the companion workbook.
>
> **Microsoft Corporation** is the primary third-party cloud service provider for hosting and storage through Microsoft Azure Government. **Descope, Inc.** provides user authentication and MFA. **Google Maps Platform**, **SendGrid**, and **Twilio** are used across Thin Line deployments for geocoding/maps, email notifications, and SMS notifications, respectively. **Stripe** and **Azure AI services** (for example Azure AI Language and/or Azure OpenAI) are included **only if enabled and configured** for this tenant; see the companion Third-Party Vendor Register for the include/exclude decision and evidence. Data in transit uses **TLS 1.2 or higher**. Data at rest uses the Azure encryption controls identified in the companion Cloud Storage Inventory (including Azure SQL TDE where applicable). Thin Line does **not** represent the Thin Line application or an Azure service as a FIPS-validated product; applicable evidence is tied to cryptographic modules and configured Azure Government services.

Replace `[AGENCY NAME]` and `[tenant]` with the agency’s legal name and Thin Line tenant key before submission. Confirm PITR window, file-storage ARM mapping, and telemetry retention from a current production export.

---

## 3. Cloud storage inventory — by reference

The authoritative row-level inventory is the **Cloud Storage Inventory** sheet in the companion workbook named in section 1. That sheet lists every service that persistently stores production data, attachments, backups, logs, identity-related records, exports, or other agency-related records for this tenant.

**Thin Line standard storage pattern (verify per tenant before submit):**

| Category | Typical resource pattern | Region | Notes |
|---|---|---|---|
| Production relational database | `tls-[tenant]-prod-rms` on `tls-db2` | USGov Texas | Azure SQL; TDE enabled in current inventories — attach current TDE evidence |
| Attachments / files | Share label `tls-[tenant]-prod-fileshare` | USGov Texas | Map label → storage account in workbook |
| SQL PITR | Azure SQL automatic backups | USGov Texas / Azure SQL backup scope | Record configured PITR window from Portal on the evidence date |
| SQL LTR | Weekly **P8W**, monthly **P1Y**, yearly **P10Y** | USGov Texas / Azure SQL backup scope | Time-based immutability **Disabled** (Thin Line standard) |
| App / security telemetry | Application Insights / Azure Monitor as configured | USGov Virginia | Confirm resource names and retention in workbook |
| Identity / MFA metadata | Descope (Thin Line auth configuration) | Per Descope residency evidence | See vendor register |
| TLETS interface connector storage/logging | Thin Line–operated connector in Azure Government | TBD until topology and implementation are approved | Document in workbook when approved; do not invent rows |

### Storage categories that must appear in the workbook (or be marked N/A with rationale)

- Production relational databases  
- Attachments, reports, exports, images, and uploaded files  
- Database PITR and LTR copies  
- Storage snapshots, soft-delete versions, or geo-replicas (if used)  
- Application, security, access, and audit logs  
- Message queues or caches only if they retain agency/CJI data  
- Identity/MFA records  
- Support exports, troubleshooting copies, or temporary files  
- Disaster-recovery replicas (if used)  
- AI or integration services if submitted content is retained  

---

## 4. Third-party vendor register — by reference

The authoritative vendor rows are the **Third-Party Vendor Register** sheet in the companion workbook. Do not describe a vendor as “processing only” until contract and current service documentation confirm that behavior.

**Always disclose for Thin Line hosted tenants (complete location/retention/evidence in the workbook):**

| Vendor | Service | Role |
|---|---|---|
| Microsoft Corporation | Microsoft Azure Government | Primary CSP: hosting, database, files, backup, telemetry |
| Descope, Inc. | Identity / authentication / MFA | Sign-in and MFA for Thin Line application users |
| Google LLC (Google Maps Platform) | Maps / geocoding | Address geocoding and map display |
| Twilio Inc. (SendGrid) | Email notifications | Transactional / notification email |
| Twilio Inc. | SMS notifications | SMS one-time codes and/or notifications as configured |

**Disclose only if enabled and configured for this tenant (include or exclude with rationale in the workbook):**

| Vendor / service | Typical use |
|---|---|
| Stripe, Inc. | Payments / online payments modules |
| Microsoft Azure AI Language | Incident narrative synopsis / language features |
| Microsoft Azure OpenAI | In-app assistant features |
| Other agency-specific integrations | Webhooks, error monitoring, etc., if agency data is sent |

**CJI rule:** Do not send CJI to a service that has not been approved for that data. Agency policy and Thin Line configuration must limit CJI in AI prompts, email, and SMS to what is authorized.

---

## 5. Backup, retention, and deletion

| Control | Thin Line standard / deployment answer |
|---|---|
| SQL point-in-time restore window | Configured Azure SQL PITR window for `tls-[tenant]-prod-rms` — **verify from Portal and record duration + evidence date in the workbook** |
| SQL long-term retention | Weekly **P8W**; monthly **P1Y**; yearly **P10Y** |
| Immutability | Time-based immutability **Disabled** (Thin Line standard). Do not claim immutable vault semantics unless a future configuration change enables them and evidence is attached. |
| File/storage backup and redundancy | Azure Storage redundancy/backup/soft-delete as configured for the tenant file store in **USGov Texas** — verify and record in the workbook |
| Log retention/archive | Application Insights / Azure Monitor retention as configured in **USGov Virginia** — verify and record in the workbook |
| Legal hold support | Supported through Thin Line + agency written legal-hold request; production deletion and routine purge are suspended for held data until the hold is released in writing |
| Tenant offboarding export | Upon written agency request (or contract offboarding), Thin Line produces a tenant data export from Azure SQL and associated file storage in a mutually agreed machine-readable format. Thin Line owns export generation; the agency owns validation and long-term archival. Target: within **30 calendar days** after Thin Line accepts an authenticated request, unless a different schedule is set in the agency agreement |
| Production deletion | After the agency confirms receipt of the offboarding export (or provides a written waiver), Thin Line disables access and deletes or deprovisions primary production tenant application data from Azure SQL and associated file stores under change control. Target: within **30 calendar days** after export acceptance/waiver |
| Backup expiration after deletion | Primary deletion does **not** instantly erase all historical backups. Remaining copies expire according to the configured PITR window and LTR policies (P8W / P1Y / P10Y) |
| Third-party account/data deletion | Processed vendor-by-vendor under each provider’s DPA/terms and Thin Line’s offboarding checklist (Descope, email/SMS, maps, and any enabled Stripe/AI services) |

Retention periods must match the agency contract, records requirements, and configured cloud settings. A capability offered by Azure is not evidence that it is enabled.

---

## 6. Data-flow and location reconciliation

- [ ] Companion workbook **Cloud Storage Inventory** and **Third-Party Vendor Register** sheets are complete for this tenant and match this disclosure’s effective date  
- [ ] Each storage service appears on the network/data-flow diagram or is represented by a labeled storage class  
- [ ] Every region is taken from current production resource inventory, not an infrastructure default  
- [ ] Replicas and backups are included, not only the primary database  
- [ ] Attachment/file storage is mapped to an actual Azure resource and region  
- [ ] Telemetry/log services have current regions and retention settings  
- [ ] TLETS connector storage/logging is documented after topology and implementation are approved (or explicitly marked pending)  
- [ ] Each third-party endpoint has an include / exclude / processing-only decision with evidence  
- [ ] Vendor contracts and service documentation support residency, retention, deletion, and access statements  
- [ ] No secrets, connection strings, private keys, or unnecessary sensitive identifiers appear in this attachment or the workbook  

---

## 7. Evidence checklist

Attach or retain for assessor review:

- [ ] Companion equipment and cloud worksheet workbook (Cloud Storage Inventory + Third-Party Vendor Register)  
- [ ] Current Azure Government resource export (type, name, subscription, resource group, region)  
- [ ] Azure SQL TDE status  
- [ ] SQL PITR and LTR settings, including immutability status  
- [ ] Azure Storage encryption, redundancy, backup, soft-delete, and region settings  
- [ ] Application Insights / Log Analytics region and retention settings  
- [ ] Data-flow / network diagram matching inventory IDs  
- [ ] Microsoft Azure Government contract/enrollment and applicable compliance references  
- [ ] Third-party DPA, data-residency, retention/deletion, and security documentation  
- [ ] Agency-specific enabled-integration review (especially Stripe and Azure AI)  
- [ ] Thin Line and agency approval/signoff  

---

## 8. Approval

| Role | Name/title | Signature or approval record | Date |
|---|---|---|---|
| Thin Line technical reviewer |  |  |  |
| Thin Line security/compliance reviewer |  |  |  |
| Agency technical/LASO reviewer |  |  |  |
| Agency approving authority |  |  |  |

---

## Related

- [Interface Approval Packet answers](interface-approval-packet.md)
- [Agency boundary equipment worksheet](agency-boundary-equipment-worksheet.md)
- [Agency network diagram template](agency-network-diagram-template.md)
- [Direct-interface scope](direct-interface-scope.md)
- Canonical packet copy (product repo): `ThinLineSoftware/Docs/TLETS/application/cloud-data-storage-disclosure-template.md`
