# Citations

Customer guides for the **Citations (CIT)** module — issuing and managing law-enforcement citations in Thin Line RMS, including mobile sync and handoff to Court.

![Citations search — find and open tickets](images/citation-search.png)

## What a citation is

A **citation** is the LE ticket / complaint record: who was cited, where, by which officer, for which offense(s), and whether the stop produced a citation or a warning. Citations are created in RMS (desktop) or on mobile patrol, then typically **issued**. When your agency uses Court, issued citations can become **court violations** for clerk processing.

| Record | Who uses it | Purpose |
|--------|-------------|---------|
| **Citation** (this guide) | Officers, records, supervisors | Create, complete, issue, print the LE citation |
| **Court violation** | Court staff | Plea, judgment, payments, compliance — see [Court](../../court/README.md) |

One citation can produce one or more court violations (for example multiple charging offenses). Warning-only lines usually do **not** create court violations.

## Workflow vocabulary

Labels come from your agency’s `_WFC` workflow codes. In product UI they appear in **ALL CAPS**:

| Status | Meaning |
|--------|---------|
| **DRAFT** | Desktop (or unfinished) citation still being completed |
| **ISSUED** | Citing officer certified / issued the citation |
| **SYNCED** | Mobile citation waiting for RMS **Mobile Citation Import** |
| **MOBILE-DRAFT** / **MOBILE-ISSUED** | Mobile-side statuses before or during sync |

Always prefer these labels in training materials so they match Search results and the Workflow button.

## Who this guide is for

| Role | Typical work |
|------|----------------|
| **Officer** | Add or mobile-issue citations; complete tabs; Mark as Issued; print |
| **Records** | Finish drafts; clear **SYNCED** import backlog; print / attachments |
| **Supervisor** | Review; **Reset for Edit** when allowed; correct without duplicate numbers |
| **Trainer** | Workshop path from Search → Issue → Court handoff |

## What you need before first ticket

- **Citation Access** (`Rms.Citation.Access`) — Search and open detail  
- **Citation Modify** (`Rms.Citation.Modify`) — desktop **Add**, edit, and Dashboard **Mobile Citations** when enabled  
- Correct **agency** selected in the header  
- Agency settings that allow manual add and/or mobile citations (if either path is missing, ask an administrator)

## Happy path (desktop)

1. [Search](search.md) first if a draft may already exist.  
2. [Add a citation](add.md) → detail opens in **DRAFT**.  
3. Complete [General](general-and-notes.md), [Person & Vehicle](person-vehicle-location.md), [Offenses](offenses-and-warnings.md), and [Racial profiling](racial-profiling.md) when required.  
4. [Mark as Issued](draft-to-issued.md).  
5. [Print](print-and-attachments.md) and, when Court is used, confirm [handoff](citation-to-court.md).

## Topics in this guide

| Topic | When to use it |
|-------|----------------|
| [Search citations](search.md) | Find and open existing citations |
| [Add a citation](add.md) | Create a new desktop citation |
| [General and notes](general-and-notes.md) | Header fields, court, appearance, notes |
| [Person, vehicle, and location](person-vehicle-location.md) | Link masters and stop location |
| [Offenses and warnings](offenses-and-warnings.md) | Charges, Is Warning, probable cause |
| [Racial profiling](racial-profiling.md) | Stop demographic / RP data |
| [Draft to Issued](draft-to-issued.md) | Mark as Issued; Reset for Edit |
| [Print and attachments](print-and-attachments.md) | PDFs, files, history |
| [Mobile citations](mobile-citations.md) | Issue on mobile; SYNCED import |
| [Citation to court](citation-to-court.md) | How citations become court violations |

## Detail tabs (after import)

On a normal **DRAFT** / **ISSUED** citation (not **SYNCED**), detail uses these tabs:

![Citation detail tabs](images/citation-tabs.png)

| Tab | Guide |
|-----|-------|
| **General** | [General and notes](general-and-notes.md) |
| **Person & Vehicle** | [Person, vehicle, and location](person-vehicle-location.md) |
| **Offenses** | [Offenses and warnings](offenses-and-warnings.md) |
| **Racial Profiling** | [Racial profiling](racial-profiling.md) |
| **Attachments** / **History** | [Print and attachments](print-and-attachments.md) |

## Related

- [Citations workshop](../../training/citations-workshop.md)
- [Journey: Law enforcement — stop to report](../../getting-started/journeys/law-enforcement-stop-to-report.md)
- [Court](../../court/README.md)
- [Master records](../../getting-started/master-records/README.md)
- [Modules and navigation](../../getting-started/modules-and-navigation.md)
