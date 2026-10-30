# Direct LETS — operations and enforcement (internal)

Product behavior shipped on the **release/6.5.0** line for **direct LETS** queries, device authorization, and agency controls. Customer-facing steps: [Direct LETS queries](../../customer/cad/direct-lets-queries.md).

## Agency switch

| Control | Who can change it | Notes |
|---------|-------------------|--------|
| **Enable Direct LETS Queries** (`EnableDirectLetsQueries` on agency) | **ThinLine.Full.Support** only | UI in **Admin → Agency → Law Enforcement Details**; readonly for agency admins. PUT `tlsapi/agencies/{id}` rejects a changed value from non-staff. CAD agency mapper never maps this field. |
| **AgencyTletsSettings** row | Staff for verification window + IP allowlist | Missing row = defaults. `TletsEnabled` column removed — direct LETS uses the single agency switch above. |

Staff helper copy lives in `adminTletsAgencySettings.ts` (support-only messaging).

## Gateway configuration

`appsettings.json` / Production token replacement:

```json
"LetsGateway": {
  "BaseUrl": "",
  "ApiKey": "",
  "TimeoutSeconds": 20
}
```

Unresolved or placeholder **BaseUrl** is treated as **not configured** (no call to a placeholder host). Gateway failures return a reason surfaced in the UI stored-response **error** field.

## Device authorization model

- **Enroll / verify** through method-specific `IDeviceVerifier` implementations.
- **DevTestDeviceVerifier** — registered when `TletsDevice:EnableDevTestVerifier` is true, including Production. Leave the flag off in Production unless a controlled test verifier is intended. The API starts with the flag off.
- **DeviceVerifications** keyed by **TletsSessionKey** (`sr:{sub}|{rexp}` — Descope `sub` + refresh expiry; plain `nvarchar(200)`).
- Verification window from **AgencyTletsSettings** (default **12** hours, allowed **1–24**).
- **POST** `tlsapi/lets-queries/direct` runs `TletsDeviceAuthorizationFilter` (fail-closed: switch, user claims, active verification, device status/claims, verifier).
- Every attempt writes a **LetsQueries** audit row (`Outcome`, `DenyReason`, `DeviceId`, `DeviceVerificationId`, `SessionId`, `ClientIp`, `CorrelationId`, `CompletedAt`).

### Claims and support users

- Claim keys: `Lets.Tlets.Query`, `Lets.Tlets.Chri`, `Lets.Tlets.DevicesApprove` (seeded).
- **HasClaim** semantics: **ThinLine.Full.Support** passes user-claim checks for all TLETS claims; device verification and device claims still apply.

### Admin APIs and UI

| Surface | Route / location |
|---------|------------------|
| Device admin | `TletsDeviceAdminController` — list/approve/suspend/reactivate/revoke, claim grant/remove (agency-scoped, `DevicesApprove`) |
| My devices | `GET tlsapi/tlets/devices/mine` — assigned devices + shared terminals this user enrolled |
| User authorization display | `GET tlsapi/tlets/authorization/mine` |
| Admin UI | **Admin → TLETS** — Devices and Operators (`AdminTlets`) |
| Approve dialog | Confirms row permission checkboxes; API always grants TLETS query on approve; **CHRI** follows row checkbox state |

DevTest enrollment: server-generated device ID (`TLETS-TEST-DEVICE-` + 12 chars), generated label `{USER NAME}-{TYPE}` with numeric suffix on collision.

### SecurityLog events (filter names)

Event IDs **9140–9231** (device lifecycle, agency enable/disable/settings, claim grant/remove) plus **9241** **TLETS Device Verification Failure**. Names are exposed on **Admin → Security Events** action filter (`AdminSecurityEventSearchOptions.vue`).

## LETS Query UI (sandbox module)

- **LETS Query** page: tabs **Query**, **Devices**, **History**.
- **TletsAuthorizationCards** — user + device state on Query tab.
- **TEST VERIFIER** badge and **Register this device** — DevTest only (`SandboxTletsDevice`, `SandboxTletsStepUpDialog`).
- History: expandable row via `letsQueryHistoryDetails.ts`; columns include TLETS outcome and device id (internal troubleshooting).
- Query validation: `LetsDirectQueryRules` is the source of truth and ignores a client-chosen key. The form’s **DRIVER** / **VEHICLE** control only decides which fields are posted. Blank state is the agency state. Texas driver is **CPL**. Another state’s driver is **DQ**. Texas registration is **REG** with no registration type. The 2026 form requires **RGT** and does not print the code. The switch rejected **EC**, so the type stays off until an accepted code is known. Another state’s registration is **RQ**. One identifier per inquiry. An out-of-state name search requires date of birth and sex. **Requesting Officer** stays optional. The gateway user id is the stored DPS user id, not the internal user id.
- A single **DQ** record can request **KQ** through `requestDriverHistory`. The same fields without that flag stay **DQ**. Texas or a vehicle plus the flag is refused. The slideout shows **Driver History** on that one record and on an expanded row in the last 24 hours.
- Test reason code migration: `_QRC` test code (`AddTestLetsQueryReasonCode`).
- **Plate Type** is sent on an out-of-state plate search and uses NCIC license plate type codes (`AddLicensePlateTypeCodes`). Texas **REG** does not send it. Plate year is sent when entered and is required for an out-of-state plate.

The same Query / Devices / History workspace also opens from the right-edge **TLETS** button (`TletsRailButton` → `TletsQueryDrawer`) when `directLetsQueriesEnabled` and `canModifyLetsQueries` are both true. The drawer follows the agency direct-query switch on its own. Ready authorization collapses to labeled header buttons. The current switch response stays under the form and is separate from the last 24 hours of saved queries. Unverified device attempts are omitted from that recent list. A direct query requires a stored DPS user id for the signed-in user at this agency.

## CAD query monitor

`CadTletsQueryDrawer` is the notes-area button on CAD. It opens a bottom sheet titled **TLETS** / **Last 24 hours**.

`CadTletsQueryMonitor.IsEnabled` is true only when the **system** `EnableDirectLetsQueries` setting is on and at least one agency allows direct queries. The button also requires `canAccessLetsQueries`. The list is the signed-in agency’s queries from every user, newest first, and it drops device-not-verified audit rows.

## Admin TLETS

**Admin → TLETS** has **Devices** and **Operators**. Operators stores the **DPS user id** per user for the current agency (`AuthUserTletsOperators`). A query sends that id; an empty value removes it.

**Admin → TLETS Mailbox** (`canManageTletsMailbox`) lists messages the switch delivered to this agency’s terminal. Dismiss and restore keep the row. Search results stay on the query. **Operates the TLETS Terminal** and **Terminal Device** are full-support agency settings.

Claim `Lets.Tlets.Mailbox`: can read and dismiss messages delivered to the agency TLETS terminal.

## IP allowlist and reasons

Staff **IP allowlist** and verification window endpoints trim and uppercase stored values. Device action reasons use `TrimUpperOrNull` for status/revoke reasons and SecurityLog **Reason**.

## Gateway service (tls-lets)

Thin Line API calls the separate **tls-lets** host (`LetsGateway` settings). Gateway auth, FoxTalk sessions, query store, and deploy topology are documented in:

- [tls-lets gateway service](tls-lets-gateway.md)
- [End-to-end direct query round trip](end-to-end-direct-query.md)
- [Azure hosting and agency inventory](azure-hosting-and-agency-inventory.md)

## Related

- [TLETS application home](README.md)
- [Direct-interface scope](direct-interface-scope.md)
- [Open decisions](open-decisions.md)
