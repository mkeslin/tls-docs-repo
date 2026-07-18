---
backlog: "BL-020 · Security · Harden Descope cookie revocation on logout"
status: draft
created: 2026-05-13
---

# Plan: BL-020 — Harden Descope cookie revocation on logout

## Goal

Close a CJIS IA-11 edge case where the 12-hour absolute session cap (item
**B** of the session/re-auth audit) can be silently reset if `sdk.logout()`
fails to revoke the Descope session cookie server-side and a new tab is
opened immediately afterward.

## Context

- **Backlog reference:** [`PRIORITIZED.md`](../prioritized.md) — P2 / Security.
- **Risk / lane:** auth-sensitive; per ``AGENTS.md`` (product repo `AGENTS.md`), small focused PR
  with unit tests; do not change other auth surfaces in the same change.
- **Related work (already merged):**
  - Phase-1 PR — session refresh hardening (single-flight refresh, `_retry`
    guard, CJIS constants, `logOutRedirectAsync` clears user store).
  - Phase-2 PR — CJIS IA-11 absolute 12-hour cap via persisted
    `authenticatedAtUtcIso` and `computeEffectiveExpiry`.

## Failure mode

In `securityServiceDescope.logOutRedirectAsync`:

1. Local user state is cleared (`identityUser`, `systemUser`, `clearAuthenticatedAt`).
2. `sdk.logout()` is called.
3. If `sdk.logout()` throws anything other than 400 (e.g. network outage,
   5xx from Descope, DNS failure), the catch block logs and proceeds.
4. `router.push({ name: 'Logout' })` runs; the user lands at `/login`.

But: the **Descope session cookie may not have been revoked server-side**.
If the user opens a fresh tab immediately, the Descope SDK can restore the
session from cookies. `IdentityAuthorization.vue:setUserAsync` then calls
`markAuthenticatedIfMissing()`, which sees no local record (cleared in
step 1) and stamps a fresh `authenticatedAtUtcIso = now`. The 12-hour cap
effectively restarts from this moment.

This violates CJIS IA-11 / IA-5 o(2)(c) for any user who can reach the
network conditions that trigger the failed `sdk.logout()`.

## Approach (options to consider — pick one in the PR)

### Option A — Cross-check the refresh-token `iat` claim before re-stamping

In `markAuthenticatedIfMissing`, if the Descope refresh token is readable
and decodes to a JWT with an `iat` (issued-at) older than
`EFFECTIVE_SESSION_LIMIT_MINUTES`, force a logout instead of stamping.
With rotation enabled the refresh-token `iat` is the most-recent rotation,
not the original login — so this only catches the case where rotation
hasn't happened recently. Partial fix; deferred to the wider A1
investigation if Descope emits a stable session-start claim.

### Option B — Retry-with-backoff + hard cookie clear on failure

If `sdk.logout()` throws a non-400, retry once with a short timeout. If
still failing, explicitly delete known Descope cookies via
`document.cookie = '<name>=; expires=...; path=/; domain=...'`. This is
brittle (cookie names and domain attributes vary by Descope project
config), but it's the most direct mitigation.

### Option C — Hard reload on the redirect to `/login`

After `sdk.logout()` succeeds or fails, replace the SPA navigation with
`window.location.assign(...)`. A full reload causes the Descope SDK to
re-evaluate cookies from scratch; if they're still valid the SDK will
restore the session and the user lands on the dashboard (which is then
caught by the absolute cap check below). Combined with **Option A** this
gives a defense-in-depth result.

### Option D — Re-check the absolute cap at session restore

In `IdentityAuthorization.vue:setUserAsync`, BEFORE calling
`markAuthenticatedIfMissing`, check whether a stored
`authenticatedAtUtcIso` exists for the **previous** identity user that is
older than `EFFECTIVE_SESSION_LIMIT_MINUTES`. If so, force logout. This
catches the cross-tab attack window even when local state was wiped.

**Likely preferred combination:** **A + D** (no DOM-level cookie hacks;
deterministic; testable).

## Files / areas (expected)

- `ThinLine.UI/src/security/securityServiceDescope.ts`
  - `logOutRedirectAsync` — possibly tighter error handling.
  - New helper: parse `iat` from the refresh-token JWT.
- `ThinLine.UI/src/stores/userStore.ts`
  - Either widen `authenticatedAtUtcIso` semantics or add a sibling
    helper `wasAuthenticatedTooLongAgo()` that returns true if the most
    recent stored timestamp (regardless of user mismatch) is older than
    the cap. Trade-off: cross-user contamination vs cross-tab safety.
- `ThinLine.UI/src/layouts/identity/IdentityAuthorization.vue`
  - `setUserAsync` — call the new pre-check before `markAuthenticatedIfMissing`.
- `ThinLine.UI/tests/unit/security/`
  - New test for the iat-check helper (Option A).
  - New test for the stale-cap pre-check (Option D).

## Verification

- [ ] `npm run lint` clean on touched files.
- [ ] `npm run test:run` — full UI vitest passes; new tests cover the
      stale-cap pre-check (Option D) and the iat parsing (Option A).
- [ ] `npm run build` — production build clean.
- [ ] Manual: simulate failed `sdk.logout()` (e.g. temporarily throw a 500
      from a fetch mock or block the Descope hostname in DevTools); confirm
      that opening a fresh tab immediately afterward does NOT extend the
      12-hour cap and forces a sign-in.

## Open questions

- Does the deployed `@descope/vue-sdk` version emit a stable "session
  start" claim distinct from the per-rotation `iat`? If yes, Option A
  becomes a clean primary fix instead of partial.
- Should we also surface a console.warn / toast when `sdk.logout()` fails
  so support can spot it in production? Today it logs to console but
  there's no user-visible signal.
- Is there a Descope server-side log we can correlate against to confirm
  how often this failure actually occurs in production?

## Notes

This item was identified during the session/re-auth audit on 2026-05-13
when verifying the phase-2 absolute-cap PR. It is **not** a blocker for
that PR — the cap works correctly under normal logout conditions; this
is a defense-in-depth follow-up.
