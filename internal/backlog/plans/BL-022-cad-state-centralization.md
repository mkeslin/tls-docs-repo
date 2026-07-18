---
backlog: "BL-022 · CAD · State centralization (audit item #3)"
status: done
completed: 2026-05-25
---

# Plan: CAD call state centralization — completed

**Status:** Done (May 2026). Audit remediation **#3** closed.

**Remaining follow-on** (tracked under [`BL-022-cad-large-agency-remediation.md`](BL-022-cad-large-agency-remediation.md)): route notes and module associations through `ICadCallMutationNotifier`.

## Delivered

| Milestone | Summary |
|-----------|---------|
| **M1** | Close-call side effects in `CallService`; mapper delegates |
| **M2** | Org/person/vehicle CRUD in `CallService`; snapshot-if-closed; thin `CallController` |
| **M3** | `ICadCallMutationNotifier` — SignalR + webhooks from service/mapper |
| **M4** | `CadCallUnitStatusTransition`; `CreateCallAsync`; webhook ordering in consumer guide §9 |

## Key artifacts

- `CallService` — unit, association, lifecycle mutations
- `ICadCallMutationNotifier` / `CadCallMutationNotifier`
- `CadCallUnitStatusTransition`, `CadWebhookUnitState`, `CadStateChangeType`
- Tests: `CallService_Lifecycle_Tests`, `CallService_Association_Tests`, `CadCallMutationNotifier_Tests`, `CadCallUnitStatusTransition_Tests` (301+ CAD unit tests total)

## Related

- product-repo `Docs/CAD-Architectural-Audit.md` — open items #4–#5
- [`BL-022-cad-large-agency-remediation.md`](BL-022-cad-large-agency-remediation.md) — active remaining work
