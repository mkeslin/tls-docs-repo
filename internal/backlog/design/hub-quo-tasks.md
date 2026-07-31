---
title: "Hub Quo tasks overlay"
status: accepted
created: 2026-07-30
updated: 2026-07-30
modules: [Hub]
backlog: []
---

# Design: Hub Quo tasks overlay

## Goal

Show Quo (OpenPhone) tasks for the signed-in Hub user as an overlay on the Board (visible 14-day window) and Today — beside Outlook chips and notecards. Do not auto-create `BoardTask` rows. Allow edit / due-date move / complete via Quo write APIs (Hub holds the workspace key).

## Decisions

1. **Quo Public API** `GET https://api.quo.com/v1/tasks` (+ `/v1/users` for email → Quo user id). Writes: `PUT /v1/tasks/{id}`, `POST .../change-due-date`, `POST .../complete`.
2. **Auth:** workspace **API key** in Hub server config (`Quo:ApiKey`). Never expose to the browser. Header is the raw key (`Authorization: <key>`), not Bearer.
3. **Whose tasks** — match Hub login emails (JWT claims → Descope user → HubUsers) to Quo user `email`, then filter assigned-to-me **or** unassigned-but-created-by-me. Independent of board “Show for”.
4. **When** — non-deleted tasks whose **due date** falls in the Board window or Today (open + completed). Tasks without a due date are omitted. Board/Today **Show completed** hides completed Quo chips the same way as notecards.
5. **UI** — phone-styled chips (draggable across Board days; strikethrough when completed) + dialog (edit title/description, mark completed). Toggle `hub-board-show-quo`.
6. **Writes** — Hub verifies the task is still “mine” before calling Quo. Due-date drag preserves local time-of-day (else noon in board TZ). Completing hides the chip unless Show completed is on.

Related: [Hub notecard board](hub-notecard-board.md), [Hub Outlook calendar](hub-outlook-calendar.md).

## Hub API

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/tlsapi/board/quo-tasks?start=&end=` | List overlay tasks |
| PUT | `/tlsapi/board/quo-tasks/{taskId}` | Title + description |
| PUT | `/tlsapi/board/quo-tasks/{taskId}/due-date` | Body `{ dueDate: yyyy-MM-dd }` |
| POST | `/tlsapi/board/quo-tasks/{taskId}/complete` | Mark completed |

## Admin setup

1. Quo → Workspace settings → **API** → generate a key (owner/admin).
2. Set Hub API config (user secrets / env preferred over committed appsettings):

| Key | Purpose |
|-----|---------|
| `Quo:ApiKey` | Workspace API key |
| `Quo:ApiBaseUrl` | Default `https://api.quo.com` |

3. Ensure HubUsers / Descope login emails match Quo user emails.

## Out of scope

Auto-creating notecards from Quo, undated task piles, Quo web deep-links (until a stable URL pattern is confirmed), reopen / delete / reassign from Hub.
