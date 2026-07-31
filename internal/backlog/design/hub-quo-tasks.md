---
title: "Hub Quo tasks overlay"
status: accepted
created: 2026-07-30
modules: [Hub]
backlog: []
---

# Design: Hub Quo tasks overlay

## Goal

Show Quo (OpenPhone) tasks assigned to the signed-in Hub user as a **read-only overlay** on the Board (visible 14-day window) and Today — beside Outlook chips and notecards. Do not auto-create `BoardTask` rows.

## Decisions

1. **Quo Public API** `GET https://api.quo.com/v1/tasks` (+ `/v1/users` for email → Quo user id).
2. **Auth:** workspace **API key** in Hub server config (`Quo:ApiKey`). Never expose to the browser. Header is the raw key (`Authorization: <key>`), not Bearer.
3. **Whose tasks** — match Hub login emails (JWT claims) to Quo user `email`, then filter `assignedTo`. Independent of board “Show for”.
4. **When** — open (not completed / not deleted) tasks whose **due date** falls in the Board window or Today. Tasks without a due date are omitted from the calendar overlay.
5. **UI** — phone-styled chips + dialog (title, due, description, conversation id). Toggle `hub-board-show-quo`.

Related: [Hub notecard board](hub-notecard-board.md), [Hub Outlook calendar](hub-outlook-calendar.md).

## Admin setup

1. Quo → Workspace settings → **API** → generate a key (owner/admin).
2. Set Hub API config (user secrets / env preferred over committed appsettings):

| Key | Purpose |
|-----|---------|
| `Quo:ApiKey` | Workspace API key |
| `Quo:ApiBaseUrl` | Default `https://api.quo.com` |

3. Ensure HubUsers / Descope login emails match Quo user emails.

## Out of scope (v1)

Writing/completing Quo tasks from Hub, auto-creating notecards, unassigned / undated task piles, Quo web deep-links (until a stable URL pattern is confirmed).
