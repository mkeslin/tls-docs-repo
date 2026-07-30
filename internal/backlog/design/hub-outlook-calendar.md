---
title: "Hub Outlook / Teams calendar overlay"
status: accepted
created: 2026-07-30
modules: [Hub]
backlog: []
---

# Design: Hub Outlook / Teams calendar overlay

## Goal

Show the signed-in user’s Microsoft Outlook/Teams meetings as a **read-only overlay** on the Board (visible 14-day window) and Today — without turning invites into notecards.

## Decisions

1. **Microsoft Graph** `GET /me/calendarView` (Teams meetings appear as Outlook calendar events).
2. **Delegated `Calendars.Read`** only — no app-only mailbox access.
3. **Descope Outbound Apps** store and refresh Graph tokens; Hub never persists Microsoft refresh tokens in SQL.
4. **Whose calendar** — always the logged-in user’s mailbox (personal context), independent of board “Show for”.
5. **When** — events intersecting the Board’s visible date range or Today’s date only.

Related: [Hub notecard board](hub-notecard-board.md).

## Admin setup (one-time)

### 1. Entra ID app (tenant `thinlinesoftware.com`)

1. App registration → **Authentication** → add redirect URI used by Descope outbound OAuth (from Descope console when creating the outbound app).
2. **API permissions** (delegated): `Calendars.Read`, plus `openid` / `offline_access` if Descope requires them.
3. Grant admin consent for the org if your tenant requires it for these scopes.
4. Create a client secret (or certificate) and note **Application (client) ID** + secret for Descope.

### 2. Descope Outbound App

1. Descope Console → **Outbound Apps** → create / select **Microsoft** (Graph) app.
2. Set app id to a stable id Hub will call (recommended: `microsoft-graph`).
3. Wire Entra client id, secret, and tenant.
4. Allowed scopes: `https://graph.microsoft.com/Calendars.Read` (and offline/openid as needed).
5. Set redirect URL(s) for Hub UI, e.g. `http://localhost:6015/home` and production Hub origin.

### 3. Hub configuration

| Key | Purpose |
|-----|---------|
| `Identity:ProjectId` | Existing Descope project |
| `Identity:ManagementKey` | Existing — used server-side to fetch outbound tokens (`Bearer {ProjectId}:{ManagementKey}`) |
| `Identity:ApiUrl` | Descope API base (e.g. `https://api.descope.com`) |
| `Identity:OutboundMicrosoftGraphAppId` | Outbound app id (default `microsoft-graph`) |

Never expose the management key to the browser.

## Runtime flow

1. User clicks **Connect Outlook** in Board settings → Descope SDK `outbound.connect(appId, { redirectUrl, scopes })` → Microsoft consent → tokens stored in Descope.
2. Board/Today call `GET /tlsapi/board/calendar-events?start=&end=`.
3. Hub resolves Descope `sub` from the session JWT → `POST …/v1/mgmt/outbound/app/user/token/latest` → Graph access token.
4. Hub calls Graph `calendarView` for the requested window → returns DTOs.
5. UI renders read-only chips; click opens `webLink` in a new tab.

If the user has never connected (Descope 404), API returns `{ connected: false, events: [] }` without failing the board.

## UI

- Board settings → **Connect Outlook** (Descope outbound consent) / **Show meetings** toggle (`hub-board-show-outlook`).
- Board day columns and Today agenda render read-only chips (time + subject; click opens `webLink`).
- Env: `VITE_OUTBOUND_MICROSOFT_GRAPH_APP_ID` (default `microsoft-graph`).

## Out of scope

Writing meetings, auto-creating cards, other users’ calendars, Quo ingest, app-only Graph.
