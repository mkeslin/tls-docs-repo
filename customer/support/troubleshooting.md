# Troubleshooting

Quick checks before escalating to Thin Line. Gather [support request](support-request.md) details if these steps fail.

## Login

### “Username or password is incorrect”

1. Caps Lock off; use **Show password** if available.
2. Confirm username with your administrator.
3. Ask whether the account is locked, inactive, or terminated.
4. Request a temporary password → [first-time login](../getting-started/logging-in.md#first-time-login).

### Login succeeds but the app errors or spins

1. Fix the computer **clock** (wrong time breaks sessions).
2. Prefer a bookmark to `/dashboard` (or your go-live URL), not a stale login-only link.
3. Try another browser / clear site data for the Thin Line host (agency IT policy).
4. Confirm VPN / network if your agency requires it.

## Wrong agency or empty lists

1. Check the **agency name** in the header.
2. Switch agency from the user menu if you have more than one.
3. On Jail Command Center / CAD, empty boards usually mean wrong facility/agency — not “no data forever.”

## Missing module, button, or menu

| Symptom | Check |
|---------|--------|
| No module icon | Claims + license ([Admin](../admin/README.md)) |
| No **Admin** | No admin claims |
| No **Accounting** | Must be court agency + accounting access |
| No **Accept into Custody** | Jail facility agency + ready booking |
| No **Self-Dispatch** | CAD mobile + self-dispatch claims + unit assignment |
| No En Route / Arrived in CAD | Agency may use Clear-only unit status |

## Masters

| Symptom | Check |
|---------|--------|
| Forced into Add | Search criteria too narrow; try fewer fields |
| Merge disabled | Missing Master merge claim; property tied to same-incident evidence |
| Snapshot vs live confusion | [Linking and snapshots](../getting-started/master-records/linking-and-snapshots.md) |

## Citations / incidents / evidence

| Symptom | Check |
|---------|--------|
| Citation stuck Draft | [Draft to Issued](../rms/citations/draft-to-issued.md) + modify rights |
| Cannot take property as evidence | Start from incident property — [Evidence](../rms/evidence/README.md) |
| Approval blocked | Incomplete required fields; wrong workflow status |

## Court / Accounting / Collections

| Symptom | Check |
|---------|--------|
| No final receipt | Accept pending payments |
| Deposit Create & Post empty | Acceptance, agency, date |
| Payout missing | [Sync Stripe Payouts](../accounting/online-payments-and-payouts.md); Support if chronic |
| Remittance won’t post | Collections **Modify**; CSV columns; matched lines |
| Do not use | Payment Cleanup, VerifyAndHeal, transaction reverse — Support / finance lead only |

## CAD

| Symptom | Check |
|---------|--------|
| Cannot open CAD | Full CAD access + `cadFull` enabled |
| Cannot drag unit | Unit Available? Already on a call? Out of vehicle? |
| Create Incident disabled | Agency unit on the call? |
| Closed Call Sheet ≠ disposed | Set Disposition after clearing units |

## Jail

| Symptom | Check |
|---------|--------|
| Accept fails | Required steps; facility agency; banner message |
| Cannot Start Pass | Observation **Modify**; locations include cell checks |
| Med log missing Approve actions | Need jail **Approve** to edit med catalog |
| Delete booking unavailable after accept | Use [Release](../jail/release.md) |

## Import/Export

| Symptom | Check |
|---------|--------|
| Menu item missing | Specific report claim |
| DPS/OCA blocked | Agency configuration |
| IBRS errors | Fix incidents → Rebuild & Validate ([checklist](../import-export/data-quality-checklist.md)) |

## Still stuck?

1. Note exact error text, time, agency, record numbers, and steps.
2. Capture a screenshot if safe.
3. [Contact Thin Line](contact.md) with [What to include](support-request.md).
4. Use [Remote assistance](remote-assistance.md) when scheduled.

## Related

- [FAQ](faq.md)
- [Dashboard](../getting-started/dashboard.md)
- [Training by role](../training/roles/README.md)
