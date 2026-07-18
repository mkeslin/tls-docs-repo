# Assign and clear units

![Call sheet / units](images/cad-call-sheet.png)

Put units on a call and move them through response statuses.

## Assign a unit to a call

Requires full CAD modify. Typical methods:

1. **Drag** an available unit from the Units panel onto the call’s unit strip.
2. **Double-click** a unit card while that call’s sheet is open.
3. Unit menu → **Assign to Call:** → choose the call number.

Units generally cannot be dragged when they are **Inactive**, already on a call, or **out of vehicle**.

On a **closed** call sheet, **Add Unit** can attach a cleared unit when your process needs late assignment.

### Primary unit

On the call’s unit activity, use **Set Primary** / **Is Primary** (star) so one unit is marked primary for the call.

## Response statuses (on a call)

After assign, the unit is typically **Dispatched**. Then:

| Action | Meaning |
|--------|---------|
| **En Route** | Unit is responding |
| **Arrived** | Unit is on scene |
| **Clear** / **Cleared** | Unit leaves the call |

**Agency option:** Some agencies enable En Route / Arrived controls; others show **Clear** only. Train to the buttons your tenant shows — both are valid Thin Line configurations.

Clear from:

- The call card unit strip (**Clear** or status menu → **CLEARED**)
- The unit card on the call sheet (**Clear**)
- [Self-dispatch](self-dispatch.md): **Clear From Call #…** for your own unit

## Free-unit status vs on-call status

Changing **Available / Inactive / Meal** (and similar) is covered in [Unit status](unit-status.md). Those free-unit statuses are different from En Route / Arrived / Cleared on a specific call.

## Tips

- Clear units before you expect **Disposition** to appear — see [Dispose and close a call](dispose-and-close-a-call.md).
- Do not clear another agency’s unit unless your policy and permissions allow it — see [Multi-agency CAD](multi-agency-and-related-records.md).
- If drag-assign fails, check the unit is Available (or otherwise assignable) and not already on a call.

## Related

- [Unit status](unit-status.md)
- [Create and update a call](create-and-update-a-call.md)
- [Self-dispatch](self-dispatch.md)
