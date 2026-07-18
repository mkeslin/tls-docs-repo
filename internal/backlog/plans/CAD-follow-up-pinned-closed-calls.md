---
backlog: "CAD · Follow-up child calls"
status: implemented
created: 2026-07-10
updated: 2026-07-10
---

# Plan: CAD Follow-up child calls

## Goal

Dispatchers can **Start follow-up** on a call to create a **new open child call** linked via `ParentCallId`, copying type/priority/location. Child appears on the main open board (not a separate expansion). Children cannot have children and cannot associate incidents/citations.

## Product decisions

| Decision | Choice |
|----------|--------|
| Entity | New `Call` with `ParentCallId` |
| Board | Child on **open** list |
| Copy | Call type, priority, location snapshot |
| Nesting | One level only |
| Modules | Blocked on children (API + UI) |
| Pin model | Retired (`FollowUpActiveAt` dropped) |

## Verification

- [ ] Create follow-up → new open call with parent link
- [ ] Child cannot create follow-up
- [ ] Child cannot link/create incident/citation
- [ ] Migration applied on ThinLineRMS
