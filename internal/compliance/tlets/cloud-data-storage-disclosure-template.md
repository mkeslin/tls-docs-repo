# Cloud data storage and third-party vendor disclosure

**Status:** Internal working template — Thin Line completes deployment facts; agency reviews and includes the approved version in its interface packet.  
**Purpose:** Documents where solution data is stored and identifies third parties involved in storage, backup, authentication, telemetry, or other processing that may retain agency or CJI-related data.  
**Download:** [Editable Word template](forms/cloud-data-storage-disclosure-template.docx)  
**Handling:** Mark the completed attachment **FOR OFFICIAL USE ONLY (FOUO)** or with the agency/DPS-required handling label.

Thin Line owns the accuracy of the cloud architecture and vendor details. The agency owns acceptance and submission. Do not submit bracketed placeholders, unverified regions, or a vendor list copied from another agency.

## 1. Submission information

| Field | Entry |
|---|---|
| Agency | `[AGENCY NAME]` |
| ORI | `[ORI]` |
| Thin Line tenant key | `[TENANT KEY]` |
| Production environment | `[ENVIRONMENT NAME]` |
| Effective date | `[YYYY-MM-DD]` |
| Thin Line preparer/reviewer | `[NAME / TITLE]` |
| Agency reviewer | `[NAME / TITLE]` |
| Related network diagram revision | `[TITLE / REVISION / DATE]` |

## 2. Packet-ready summary

Complete the inventories below first, then use this narrative:

> Thin Line Software LLC hosts `[AGENCY NAME]`'s Thin Line `[RMS / CAD / JMS]` production environment in **Microsoft Azure Government**. Primary application data is stored in `[AZURE SQL DATABASE NAME]` in `[PRIMARY AZURE GOVERNMENT REGION]`. File attachments are stored in `[AZURE STORAGE ACCOUNT / FILE SHARE OR N/A]` in `[REGION]`. Backups and recovery copies are maintained through `[AZURE BACKUP / SQL PITR / LTR SERVICES]` in `[REGION OR REDUNDANCY SCOPE]` under the retention settings listed in this attachment. Application and security logs are stored in `[LOG SERVICES]` in `[REGION]` for `[RETENTION]`.
>
> Microsoft Corporation is the primary third-party cloud service provider involved in hosting and storage through Microsoft Azure Government. Additional third parties that store or retain agency-related information are identified in the Third-party vendor register below, including the data involved, purpose, storage location, retention, and contract/security evidence. Data in transit is protected using TLS 1.2 or higher. Data at rest is protected using the Azure encryption controls identified in the storage inventory. Thin Line does not represent the Thin Line application or an Azure service as a FIPS-validated product; applicable evidence is tied to the cryptographic modules and configured Azure Government services.

## 3. Cloud storage inventory

List every service that persistently stores production data, attachments, backups, logs, identity data, exports, queues, or other agency-related records. A processing service that does not retain data should still be disclosed in the vendor register with its verified retention behavior.

| ID | Data/service | Data stored | Provider | Cloud/environment | Resource name | Physical region/data residency | Replication/backup location | Encryption at rest | Key owner | Retention/deletion | Access owner | Evidence date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ST-01` | Azure SQL Database | RMS/CAD structured application data and audit records as configured | Microsoft | Azure Government | `[SERVER / DATABASE]` | `[REGION]` | `[PITR/LTR/GEO DETAILS AND REGION]` | `[TDE / AES DETAILS]` | `[MICROSOFT-MANAGED OR CUSTOMER-MANAGED]` | `[PITR/LTR / OFFBOARDING]` | Thin Line | `[YYYY-MM-DD]` |
| `ST-02` | Azure Storage | Attachments/files | Microsoft | Azure Government | `[ACCOUNT / SHARE / CONTAINER OR N/A]` | `[REGION]` | `[REDUNDANCY / BACKUP / REGION]` | `[SERVICE ENCRYPTION]` | `[KEY OWNER]` | `[RETENTION / DELETION]` | Thin Line | `[YYYY-MM-DD]` |
| `ST-03` | Logs/telemetry | `[APPLICATION / SECURITY / AUDIT / DIAGNOSTIC DATA]` | Microsoft | Azure Government | `[APPLICATION INSIGHTS / LOG ANALYTICS / SENTINEL]` | `[REGION]` | `[IF APPLICABLE]` | `[ENCRYPTION]` | `[KEY OWNER]` | `[DAYS / ARCHIVE]` | `[THIN LINE / SHARED]` | `[YYYY-MM-DD]` |
| `ST-04` | Identity service | User identity, authentication, and MFA metadata | `[DESCOPE / AGENCY IDP / OTHER]` | `[ENVIRONMENT]` | `[PROJECT / TENANT]` | `[VERIFIED REGION / RESIDENCY]` | `[IF APPLICABLE]` | `[VENDOR CONTROL]` | `[KEY OWNER]` | `[RETENTION / DELETION]` | `[AGENCY / THIN LINE / SHARED]` | `[YYYY-MM-DD]` |
|  |  |  |  |  |  |  |  |  |  |  |  |  |

### Storage categories to verify

- Production relational databases
- Attachments, reports, exports, images, and uploaded files
- Database point-in-time restore and long-term retention copies
- Storage snapshots, soft-delete versions, or geo-replicas
- Application, security, access, and audit logs
- Message queues or caches only if they retain agency/CJI data
- Identity/MFA records
- Support exports, troubleshooting copies, or temporary files
- Disaster-recovery replicas
- AI or integration services if submitted content is retained

## 4. Third-party vendor register

Include Microsoft and every other third party that stores or may retain agency-related information. Do not describe a vendor as "processing only" until its contract and current service documentation confirm that behavior.

| Vendor/legal entity | Service | Role | Data involved | Stores/retains data? | Storage environment/location | Retention/deletion | CJI access potential | Agreement/evidence | Thin Line owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Microsoft Corporation | Microsoft Azure Government | Primary CSP: application hosting, database, file, backup, and logging services as listed above | CJI and application data according to enabled services | Yes | Azure Government; exact regions in storage inventory | Per configured service policies and contract | `[YES/NO; EXPLAIN SUPPORT ACCESS MODEL]` | `[CJIS/CONTRACT/COMPLIANCE REFERENCES]` | `[OWNER]` | `REQUIRED` |
| Descope, Inc. | Identity/authentication/MFA | Identity provider for configured Thin Line sign-in flows | Identity and authentication metadata; verify whether CJI is prohibited | `[VERIFY]` | `[VERIFY DATA RESIDENCY]` | `[VERIFY]` | `[VERIFY]` | `[DPA / SECURITY / RESIDENCY EVIDENCE]` | `[OWNER]` | `VERIFY` |
| `[VENDOR]` | `[SERVICE]` | `[ROLE]` | `[DATA]` | `[YES/NO/TRANSIENT — EVIDENCE]` | `[LOCATION]` | `[RETENTION/DELETION]` | `[YES/NO]` | `[AGREEMENT/EVIDENCE]` | `[OWNER]` | `[STATUS]` |

### Vendors/services requiring an explicit include-or-exclude decision

Review the agency's enabled production features. Potential integrations in the Thin Line platform include identity providers, Azure AI services, payment processors, mapping/geocoding, email/SMS, webhooks, error monitoring, and support tooling.

For each:

- **Include** it when agency-related data is sent and the service stores, logs, backs up, or otherwise retains that data.
- **Disclose as processing-only** only when current contractual and technical evidence establishes no retention beyond approved transient processing.
- **Exclude with rationale** when the integration is disabled for the agency or no agency-related data reaches it.
- Do not send CJI to a service that has not been approved for that data.

## 5. Backup, retention, and deletion

| Control | Deployment-specific answer |
|---|---|
| SQL point-in-time restore window | `[DURATION / VERIFIED DATE]` |
| SQL long-term retention | `[WEEKLY / MONTHLY / YEARLY SETTINGS]` |
| File/storage backup and redundancy | `[SETTING / REGION / VERIFIED DATE]` |
| Log retention/archive | `[SERVICE / DURATION]` |
| Immutability | `[ENABLED / DISABLED / NOT USED — DO NOT ASSUME]` |
| Legal hold support | `[PROCESS / N/A]` |
| Tenant offboarding export | `[FORMAT / OWNER / TIMING]` |
| Production deletion | `[PROCESS / APPROVAL / TIMING]` |
| Backup expiration after deletion | `[TIMING / SERVICE BEHAVIOR]` |
| Third-party account/data deletion | `[VENDOR-BY-VENDOR PROCESS]` |

Retention periods must match the agency contract, records requirements, and configured cloud settings. A capability offered by Azure is not evidence that it is enabled.

## 6. Data-flow and location reconciliation

- [ ] Each storage service appears on the network/data-flow diagram or is represented by a labeled storage class.
- [ ] Every region is taken from current production resource inventory, not an infrastructure default.
- [ ] Replicas and backups are included, not only the primary database.
- [ ] Attachment/file storage has been mapped to an actual Azure resource and region.
- [ ] Telemetry/log services have current regions and retention settings.
- [ ] The TLETS connector's storage/logging behavior is documented after topology and implementation are approved.
- [ ] Each third-party endpoint receiving agency data has an include/exclude decision.
- [ ] Vendor contracts and service documentation support residency, retention, deletion, and access statements.
- [ ] No secrets, connection strings, private keys, or unnecessary sensitive identifiers appear in the attachment.

## 7. Evidence checklist

Attach or retain for assessor review:

- [ ] Current Azure Government resource export showing resource type, name, subscription, resource group, and region
- [ ] Azure SQL TDE status
- [ ] SQL PITR and LTR settings, including immutability status
- [ ] Azure Storage encryption, redundancy, backup, soft-delete, and region settings
- [ ] Application Insights/Log Analytics/Sentinel region and retention settings, as applicable
- [ ] Data-flow/network diagram matching the inventory IDs
- [ ] Microsoft Azure Government contract/enrollment and applicable compliance references
- [ ] Third-party DPA, data-residency, retention/deletion, and security documentation
- [ ] Agency-specific enabled-integration review
- [ ] Thin Line and agency approval/signoff

## 8. Approval

| Role | Name/title | Signature or approval record | Date |
|---|---|---|---|
| Thin Line technical reviewer |  |  |  |
| Thin Line security/compliance reviewer |  |  |  |
| Agency technical/LASO reviewer |  |  |  |
| Agency approving authority |  |  |  |

## Known Thin Line baseline — verify per agency

Repository evidence supports the following baseline, but the completed attachment must use current production exports:

- Thin Line production deployment patterns target **Microsoft Azure Government**.
- Agency RMS/CAD application tiers commonly use Azure App Service and Azure SQL Database.
- Current agency inventories place common production application and SQL resources in **US Gov Texas**; some telemetry resources may be in **US Gov Virginia**.
- Azure SQL TDE has been verified for documented agency databases, but each packet needs current per-tenant evidence.
- Attachments use an Azure file-storage pattern, but the actual storage account, region, redundancy, backup, and retention must be mapped and verified before submission.
- Microsoft is the primary hosting/storage third party.
- Descope is used in configured identity flows; its data residency, retention, and CJI scope require a current vendor/configuration review.
- The proposed TLETS connector's persistent storage, logs, and region cannot be finalized until the topology and implementation are approved.

## Related

- [Interface Approval Packet answers](interface-approval-packet.md)
- [Agency network diagram template](agency-network-diagram-template.md)
- [Agency boundary equipment worksheet](agency-boundary-equipment-worksheet.md)
- [Direct-interface scope](direct-interface-scope.md)
