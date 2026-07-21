# Agency boundary equipment and software worksheet

**Status:** Agency-completed working template  
**Purpose:** Accompanies the CJIS/TLETS network diagram and documents equipment and software used to meet boundary-protection requirements.  
**Download:** [Spreadsheet-compatible CSV template](forms/agency-boundary-equipment-worksheet.csv)

The agency owns and verifies this inventory. Thin Line may help identify the Thin Line/Azure Government components, but should not invent agency equipment, versions, update dates, or support dates.

## Submission information

| Field | Agency entry |
|---|---|
| Agency name | `[AGENCY NAME]` |
| ORI | `[ORI]` |
| Diagram title/revision | `[DIAGRAM TITLE / REVISION]` |
| Inventory effective date | `[YYYY-MM-DD]` |
| Prepared by/title | `[NAME / TITLE]` |
| Technical reviewer | `[NAME / TITLE]` |
| LASO/approving authority | `[NAME / TITLE]` |
| Handling marking | `FOR OFFICIAL USE ONLY (FOUO)` or agency/DPS-required marking |

## Instructions

1. Give every relevant object on the network diagram a unique identifier, such as `FW-01`, `RTR-01`, `SW-01`, `VPN-01`, `IDS-01`, `SRV-01`, or `EDR-01`.
2. Use the same identifier in the **Diagram ID** column below.
3. Include equipment and software that protects, routes, monitors, authenticates, remotely accesses, or otherwise supports systems that process, transmit, or store CJI.
4. Include firewalls, routers, switches, VPN/remote-access gateways, IDS/IPS, wireless controllers, proxy/filtering systems, authentication/MFA systems, endpoint security/EDR, relevant servers, and any agency-hosted TLETS connector.
5. Use one row per materially different make/model/version. Identical assets may be grouped only when their installed versions, update dates, and support dates are the same.
6. Obtain **Latest version** and **End-of-support date** from the manufacturer/publisher or the agency's authorized support provider. Record the source in **Evidence/source**.
7. Use ISO dates (`YYYY-MM-DD`). If the vendor has not announced an end-of-support date, enter `NOT ANNOUNCED` and cite the source checked and date checked.
8. Do not include passwords, keys, private IP addresses, or unnecessary serial numbers in the copy sent outside the agency.

## Equipment and software inventory

The downloadable CSV has the same columns and is easier to complete in Excel.

| Diagram ID | Asset type | Boundary/security purpose | Owner | Location/zone | Qty. | Make/publisher | Model/product | Current OS/firmware/version | Latest vendor version | Last updated | End of support | Status | Remediation/action | Evidence/source | Verified by/date | Notes |
|---|---|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| `[FW-01]` | `[Firewall]` | `[Internet boundary; filtering; IDS/IPS]` | `[Agency]` | `[Secure network edge]` | `[1]` | `[MAKE]` | `[MODEL]` | `[CURRENT VERSION]` | `[LATEST VERSION]` | `[YYYY-MM-DD]` | `[YYYY-MM-DD]` | `[CURRENT / UPDATE DUE / EOS]` | `[ACTION AND DUE DATE]` | `[VENDOR URL / SUPPORT RECORD]` | `[NAME / YYYY-MM-DD]` | |
| `[EDR-01]` | `[Endpoint security software]` | `[Malware prevention and monitoring]` | `[Agency]` | `[Managed CJI endpoints]` | `[N]` | `[PUBLISHER]` | `[PRODUCT / TIER]` | `[CURRENT VERSION]` | `[LATEST VERSION]` | `[YYYY-MM-DD]` | `[YYYY-MM-DD or NOT ANNOUNCED]` | `[STATUS]` | `[ACTION]` | `[SOURCE]` | `[NAME / DATE]` | |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Status definitions

| Status | Use when |
|---|---|
| `CURRENT` | Installed version is supported and meets agency update requirements. |
| `UPDATE DUE` | A newer approved version or required security update is pending. |
| `EOS APPROACHING` | Vendor support ends within the agency's planning threshold. |
| `END OF SUPPORT` | Vendor support has ended; document compensating controls and replacement/remediation. |
| `VERIFY` | Version, update date, latest release, or support date has not been validated. Resolve before submission. |
| `N/A` | Field genuinely does not apply; explain why in Notes. |

## Software-only entries

For software without a hardware make/model:

- Put the software publisher in **Make/publisher**.
- Put the product, edition, or service tier in **Model/product**.
- Put the deployed agent/service version in **Current OS/firmware/version**.
- If software is SaaS and the publisher controls releases, enter `VENDOR-MANAGED SAAS` for the current/latest version where appropriate and cite the service lifecycle documentation.
- Record the agency-controlled policy/configuration revision separately if that configuration is what satisfies the boundary requirement.

## Reconciliation checklist

- [ ] Every inventory row maps to a labeled item or grouped device class on the network diagram.
- [ ] Every boundary/security item shown on the diagram appears in this inventory or is clearly identified as Thin Line-, Azure-, carrier-, or DPS-controlled.
- [ ] Current and latest versions were compared using authoritative sources.
- [ ] Last-updated dates are supported by management-console records, change tickets, or maintenance records.
- [ ] End-of-support dates were verified or marked `NOT ANNOUNCED` with a source/date checked.
- [ ] Unsupported or outdated items have a remediation date and documented interim controls.
- [ ] Remote-access equipment/software matches the agency remote-access policy and procedure.
- [ ] The network diagram revision and worksheet revision match.
- [ ] Agency technical staff and the approving authority reviewed the completed attachment.

## Suggested response for the packet

> `[AGENCY NAME]` uses the boundary-protection equipment and software identified in the attached detailed equipment and software inventory. Each item is cross-referenced to the accompanying network diagram by Diagram ID. The inventory identifies the manufacturer or publisher, model or product, currently installed operating system/firmware/software version, latest vendor version, date last updated, and vendor end-of-support date. Agency technical staff reviewed the inventory as of `[YYYY-MM-DD]`. Items requiring updates or replacement are identified with planned remediation and, where necessary, interim controls.

## Related

- [Agency network diagram template](agency-network-diagram-template.md)
- [Thin Line network diagram insert](thin-line-network-diagram-insert.md)
- [Interface Approval Packet answers](interface-approval-packet.md)
