---
title: "Hub Pipedrive overlay"
status: accepted
created: 2026-07-30
updated: 2026-07-30
modules: [Hub, Acquire, Expand, Advocate, Deliver]
backlog: []
---

# Design: Hub Pipedrive overlay

## Goal

Show the signed-in Hub user’s **Pipedrive activities** and **project tasks** as two separate read/write overlays on the Board (visible 14-day window) and Today — beside Outlook, Quo, and notecards. Do not auto-create `BoardTask` rows. Pipedrive remains the system of record.

## Decisions

1. **Two overlays, two toggles** — Activities (`hub-board-show-pipedrive-activities`) and project tasks (`hub-board-show-pipedrive-project-tasks`) are independent in Board settings. Different chip styles.
2. **APIs** — Activities: `GET/PATCH /api/v2/activities`. Project tasks: `GET/PATCH /api/v2/tasks`. Users for email match: `GET /api/v1/users`. Auth: company **API token** in `x-api-token` (never exposed to the browser).
3. **Whose items** — match Hub login emails → Pipedrive user `email`, then activities with `owner_id` = me; project tasks with `assignee_id` / `assignee_ids` containing me. Independent of board “Show for”.
4. **When** — open (not done) items whose **due date** falls in the Board window or Today. Undated items are omitted from the calendar overlay.
5. **Writes** — Hub verifies the item is still “mine” before PATCH. Supported: edit subject/title + note/description, change due date (day drag), mark done. Completing removes the chip unless “Show completed” is on (in-session).
6. **Config** — `Pipedrive:ApiToken`, `Pipedrive:CompanyDomain` (base `https://{domain}.pipedrive.com`). Prefer user secrets / env over committed appsettings.

Related: [Hub Quo tasks overlay](hub-quo-tasks.md), [Hub Outlook calendar](hub-outlook-calendar.md), [Hub notecard board](hub-notecard-board.md), [Hub Acquire Desk](hub-acquire-desk.md).

## Hub API

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/tlsapi/board/pipedrive-activities?start=&end=` | List activity overlay |
| PUT | `/tlsapi/board/pipedrive-activities/{id}` | Subject + note |
| PUT | `/tlsapi/board/pipedrive-activities/{id}/due-date` | Body `{ dueDate: yyyy-MM-dd }` |
| POST | `/tlsapi/board/pipedrive-activities/{id}/complete` | Mark done |
| GET | `/tlsapi/board/pipedrive-project-tasks?start=&end=` | List project-task overlay |
| PUT | `/tlsapi/board/pipedrive-project-tasks/{id}` | Title + description |
| PUT | `/tlsapi/board/pipedrive-project-tasks/{id}/due-date` | Body `{ dueDate: yyyy-MM-dd }` |
| POST | `/tlsapi/board/pipedrive-project-tasks/{id}/complete` | Mark done |

## Admin setup

1. Pipedrive → Personal preferences → **API** → copy token (or company admin token with activities + projects access).
2. Note company subdomain (e.g. `thinline` → `https://thinline.pipedrive.com`).
3. Set Hub API config:

| Key | Purpose |
|-----|---------|
| `Pipedrive:ApiToken` | API token (`x-api-token`) |
| `Pipedrive:CompanyDomain` | Subdomain only (no `.pipedrive.com`) |

4. Ensure Hub / Descope login emails match Pipedrive user emails.

## Out of scope

Auto-creating notecards from Pipedrive, undated piles, creating new activities/tasks from Hub, deal/org sync, pipeline UI, reopen/delete/reassign from Hub.
