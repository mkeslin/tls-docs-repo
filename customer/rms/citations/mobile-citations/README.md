# Mobile citations

**Mobile Citations** is Thin Line’s officer-facing ticket product: write and **Issue** a citation from Dashboard or patrol, sync it to RMS, then (when needed) finish **Mobile Citation Import** so masters and court handoff are clean.

This is a different path from desktop [Add a citation](../add.md). Mobile drafts live on the device/browser until Issue succeeds; RMS then receives a **SYNCED** (or fully issued) citation for records follow-up.

![Mobile Citations list — In-Progress and Printed/Issued](../images/mobile-citations-list.png)

## Who uses which part

| Role | Work | Guide |
|------|------|-------|
| **Officer** | Create drafts, complete the ticket, **Issue**, print/download, **Sync Now** if needed | [Write and issue](write-and-issue.md) · [List, sync, and offline](list-sync-and-offline.md) |
| **Records / supervisor** | Clear **SYNCED** import backlog; print from RMS | [Import SYNCED into RMS](import-synced.md) |
| **Trainer** | End-to-end stop → Issue → import → court | [Citations workshop](../../../training/citations-workshop.md) |

## What you need

- **Citation Modify** (`Rms.Citation.Modify`)
- Agency setting **mobile citations enabled** (`citationMobileEnabled`)
- User is an **officer** (or full support) — non-officers see a message that they cannot write mobile citations and should use the Citations module instead
- Correct **agency** in the header

## End-to-end flow

```mermaid
flowchart LR
  A[Dashboard / Patrol] --> B[Mobile draft<br/>local TEMP-#]
  B --> C[Issue]
  C --> D[RMS citation<br/>SYNCED]
  D --> E[Mobile Citation Import]
  E --> F[Normal RMS citation<br/>DRAFT / ISSUED]
  F --> G[Court handoff]
```

1. Open **Dashboard → Mobile Citations** (or patrol **Citations** / Traffic Stop shortcuts).  
2. **Add** a draft — number is temporary (**TEMP-…**) until Issue assigns the real number.  
3. Complete the ticket sections and **Issue** (see [Write and issue](write-and-issue.md)).  
4. On success, the ticket appears under **Printed/Issued**; use **Go to Citation** for the RMS record.  
5. Records staff complete [Import SYNCED](import-synced.md) when the RMS status is **SYNCED**.  
6. Continue [Draft to Issued](../draft-to-issued.md) / [Citation to court](../citation-to-court.md) per agency rules.

## Topics in this guide

| Topic | When to use it |
|-------|----------------|
| [Write and issue](write-and-issue.md) | Officer create, fields, validation, Preview, Issue |
| [List, sync, and offline](list-sync-and-offline.md) | In-Progress / Printed-Issued, Sync Now, storage, failures |
| [Import SYNCED into RMS](import-synced.md) | Records import stepper after mobile sync |

## Related

- [Citations overview](../README.md)
- [Dashboard](../../../getting-started/dashboard.md)
- [Racial profiling](../racial-profiling.md) (Stop Information on mobile)
- [Print and attachments](../print-and-attachments.md)
