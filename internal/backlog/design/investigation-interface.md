# Investigation Interface Design — Case Intelligence Cockpit

> **Source of truth:** Internal Docs (GitBook). Paths under `ThinLine.UI/` and `ThinLine.API/` refer to the product monorepo.


**Thin Line Platform — Investigator Command Center**

This document describes the layout, user experience, interaction design, and demo flow for the Investigation interface. It follows the same three-column command center pattern as the Patrol Command Center but is adapted for detectives and investigators: case-centric, depth-focused, and tightly connected to Court, Jail, and RMS.

---

## Design Goals

| Priority | Question | Design Response |
|----------|----------|-----------------|
| 1 | "What do I work next?" | Case control via My Active Cases + My Tasks queues |
| 2 | "What am I missing?" | Pattern visibility in Connections, Case Health, Suggested Next Steps |
| 3 | "What's pending and what's blocked?" | Evidence workflow, task blockers, lab status |
| 4 | "Can I hand this to the DA?" | DA Packet tab with readiness checklist |
| 5 | Speed to context | Under 3 seconds via search, click-through, and context panel |
| 6 | Professional tone | Neutral palette, restrained color, analytical feel |

---

## Screen Structure — Three-Column Layout

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TOP BAR (full width)                                                             │
├──────────────┬────────────────────────────────────────────┬──────────────────────┤
│ LEFT         │ CENTER                                     │ RIGHT                │
│ Queues &     │ Case Workspace                             │ Context & Action     │
│ Workload     │ (tabs: Overview | Timeline | Connections  │ Panel (dynamic)      │
│              │  | Evidence | DA Packet)                   │                      │
│ My Active    │                                            │ Updates when user    │
│ My Tasks     │ Primary workspace for case work            │ selects case,       │
│ Pending      │                                            │ person, address,     │
│ Evidence/Lab │                                            │ vehicle, evidence    │
│ Court/Jail   │                                            │                      │
│ Watch        │                                            │                      │
└──────────────┴────────────────────────────────────────────┴──────────────────────┘
```

- **Responsive**: On smaller screens, columns stack vertically. Left and Right collapse into drawers or accordions; Center remains primary.
- **Clean**: Generous whitespace between sections. No form-like density. Feels like a workspace, not a data entry screen.

---

## Top Bar Design (Investigation)

### Contents (left to right)

1. **Global Search**
   - Placeholder: "Search person, case, address, vehicle, evidence…"
   - Command-palette feel: fast, keyboard-first. Suggest Ctrl+K or Cmd+K shortcut.
   - Results preview appears below input as user types.

2. **"My Cases" Filter Controls**
   - Status: Open | Pending Lab | Pending Review | Submitted | Cleared
   - Priority: High | Medium | Low
   - Assigned To: Me | Unit | [dropdown]
   - Date Range: Last 7 days | Last 30 days | Custom
   - Filters appear as compact chips or a collapsible "Filters" dropdown. Visible but not overwhelming—default to "My Cases" view with minimal chrome.

3. **Quick Toggle**
   - "Show My Work" vs "Unit View"
   - Single toggle or segmented control. "My Work" = investigator's own cases/tasks. "Unit View" = unit-wide workload (for supervisors).

4. **Demo Mode Toggle**
   - Checkbox or switch: "Demo"
   - When on: richer narratives, Demo Insight badges, Suggested Next Steps.

5. **Quick Actions**
   - New Case
   - Add Supplement
   - Add Evidence
   - Request Warrant Review
   - Export DA Packet
   - Primary action (e.g., New Case) slightly more prominent; others secondary.

6. **Status Summary (right side)**
   - Active case count
   - Overdue tasks count (if any)
   - Next court date (if within 7 days)

### Search Result Previews

- **Case**: Case #, title, status chip, days open. Example: `24-1032 | Burglary — 123 Maple St | Open | 12 days`
- **Person**: Name, DOB, role in case(s). Example: `John Doe | DOB 1985 | Suspect in 24-1032`
- **Address**: Street, city, case count. Example: `123 Maple St | 2 cases`
- **Vehicle**: Plate, make/model, owner. Example: `TX ABC123 | 2019 Honda Civic | John Doe`
- **Evidence**: Item ID, case, status. Example: `E-4421 | Case 24-1032 | At Lab`

Results grouped by type. Clicking a result loads it into Center (if case) or Center + Right Context (if person/address/vehicle/evidence).

### Keyboard Shortcut Feel

- Search opens with shortcut; focus goes to input immediately.
- Arrow keys navigate results; Enter selects.
- Escape closes search.
- No lag—feels instant.

---

## Left Column — Queues & Investigator Workload

Stacked sections (cards) with clear counts and urgency. Each section scrolls independently if needed.

### Visual Style

- Card: subtle border, rounded corners, section header with count badge.
- Urgency: use color sparingly. Red only for critical (e.g., court tomorrow, overdue task). Amber for "attention soon." Slate/neutral for normal.
- Avoid constant red; investigation is analytical, not alarm-driven like patrol.

---

### 1) My Active Cases

**Header**: "My Active Cases" with count badge (e.g., `12`).

**Content**:
- Sorted by priority, then days open.
- Each row: Case #, short title, status chip, days open, last activity.
- Status chips: Open | Pending Lab | Pending Review | Submitted | Cleared
- Truncate long titles; full title on hover or in Center.

**Placeholder examples**:
| Case | Title | Status | Days | Last Activity |
|------|-------|--------|------|---------------|
| 24-1032 | Burglary — 123 Maple St | Pending Lab | 12 | Feb 24 |
| 24-0987 | Agg Assault — Doe | Open | 18 | Feb 22 |
| 24-0912 | Theft — Retail | Pending Review | 5 | Feb 25 |

**Click behavior**: Loads case into Center Workspace (Case Overview tab). Right Context Panel shows case summary, quick facts, and case-specific actions.

---

### 2) My Tasks

**Header**: "My Tasks" with count badge.

**Content**:
- Task type: Interview to schedule, evidence to submit, subpoena to send, supplement due, lab follow-up.
- Each task: due date, case link, blocker reason (if any).
- "Quick complete" affordance: small checkmark or "Done" on hover.

**Placeholder examples**:
- `Schedule interview — Witness M. Jones | Due Feb 28 | Case 24-1032`
- `Submit evidence E-4421 | Due Feb 27 | Blocked: Lab pending`
- `Send subpoena — Pawn records | Due Mar 5 | Case 24-0987`

**Click behavior**: Opens task in Center (or focuses case + scrolls to task). Right panel shows task details and "Complete" / "Reschedule" actions.

---

### 3) Pending Evidence / Lab

**Header**: "Pending Evidence / Lab" with count.

**Content**:
- Evidence items with state: Collected | Submitted | At Lab | Returned
- Emphasize items blocking closure or DA packet (e.g., bold or amber chip).

**Placeholder examples**:
- `E-4421 | Tool — At Lab | Case 24-1032 | Blocking DA packet`
- `E-4402 | Phone — Returned | Case 24-0987`
- `E-4398 | Clothing — Submitted | Case 24-0912`

**Click behavior**: Loads evidence item into Right Context Panel. Center can switch to Evidence tab of linked case.

---

### 4) Court & Jail Watch

**Header**: "Court & Jail Watch" with count.

**Content**:
- Upcoming court dates tied to investigator's cases.
- Custody status changes: Booked | Released | Bonded
- Conditions of release (placeholder) that matter for investigation (e.g., "No contact with victim").

**Placeholder examples**:
- `Court: 24-1032 | Mar 3 | Prelim | Doe, J.`
- `Custody: Doe, J. — Bonded Feb 25 | Conditions: No contact, surrender passport`
- `Court: 24-0987 | Mar 10 | Arraignment`

**Click behavior**: Clicking court date opens case in Center, scrolls to Timeline, highlights court event. Clicking custody item opens person in Right Context Panel.

---

## Center Panel — Case Workspace (Primary)

Tabbed interface. Tabs: **Case Overview** | **Timeline** | **Connections** | **Evidence** | **DA Packet**.

Selecting a case, person, address, vehicle, or evidence in Center updates the Right Context Panel.

---

### Tab A: Case Overview (default)

**Case header**:
- Case #, title, priority badge, status chip, assigned investigator(s)
- Large, clear typography for case title.

**Case Health indicators** (simple, horizontal row of chips or icons):
- Missing statements
- Pending lab
- No suspect
- No disposition
- Next court date
- Green check = resolved; amber = needs attention; gray = N/A

**Key entities**:
- Victim(s) | Suspect(s) | Witness(es) | Primary location(s) | Associated vehicle(s)
- Each as a clickable chip or row. Click → Right panel shows full context.

**Recent activity feed** (last 10 actions):
- Chronological list: "Feb 25 — Supplement added", "Feb 24 — Evidence E-4421 submitted to lab", "Feb 23 — Interview with M. Jones"
- Click activity → may jump to Timeline tab.

---

### Tab B: Timeline

**Layout**: Clean chronological timeline. Vertical line with nodes.

**Event types** (visually distinct):
- **Incident Events**: Original offense, 911 call, etc. (e.g., filled circle)
- **Investigative Actions**: Interviews, supplements, evidence logged (e.g., square)
- **Court/Jail Events**: Arraignment, bond, custody change (e.g., diamond)

**Quick add** (floating or inline):
- "Add Interview Note"
- "Add Supplement"
- "Add Evidence Entry"
- No implementation details—just affordances.

---

### Tab C: Connections (Link/Relationship View)

**Concept**: Simple relationship canvas. Nodes = people, addresses, vehicles, cases. Edges = relationships.

**Placeholder example**:
```
[John Doe] ←→ [123 Maple St] ←→ [Vehicle TX ABC123] ←→ [Case 24-1032 Burglary]
     ↓
[Case 24-0987 Agg Assault]
```

**Interaction**: Clicking a node updates Right Context Panel with that entity. Double-click could expand or open detail.

**Not fancy**: No heavy graph library. Clean, readable diagram. Optional "Demo Insight" badge: "Same address links suspect to prior case."

---

### Tab D: Evidence

**Content**:
- Evidence list with status chips and dates.
- "Blocking" labels: e.g., "Awaiting lab results", "Chain incomplete".
- Attachments placeholder: photos, documents, body cam references.
- Quick actions: "Generate Chain Summary", "Request Lab Update" (placeholders).

**Visual**: Table or card list. Blocking items highlighted (amber border or chip).

---

### Tab E: DA Packet (Court Packet)

**Readiness checklist**:
- Statements complete?
- Evidence logged?
- Charges drafted?
- Warrants attached?
- Timeline verified?

**Confidence indicator**: Ready | Almost Ready | Not Ready — with reasons listed.

**Actions**:
- "Export Packet" button
- "Last exported" timestamp placeholder

**Tone**: Checklist feel. Clear what's missing. No guesswork.

---

## Right Column — Context & Action Panel (Dynamic)

Updates when user selects: Case | Person | Address | Vehicle | Evidence item.

---

### 1) Primary Context Header

- **Big title**: e.g., "John Doe" or "Case 24-1032"
- **Subheader**: DOB/age (placeholder), address, case status, role (Suspect | Witness | Victim)

---

### 2) Risk / Caution Signals

- Smaller than patrol. Use "Caution" vs "Danger" tone.
- Examples: "Violence history", "Weapons noted", "Known flight risk", "Protective order"
- Professional, not alarmist. Slate/amber for caution; red only when critical.

---

### 3) Smart Summary Box

- Investigation narrative style.
- **Placeholder**: "Primary suspect linked via shared address and vehicle. Two prior contacts at location. Awaiting lab on recovered tool."
- Demo Mode: Add "Demo Insight" badge and richer narrative.

---

### 4) Quick Facts (chips)

- Outstanding warrants? Probation/parole? Custody status? Next court date?
- Conditions of release (placeholder)

---

### 5) Related Items

- Related cases
- Associates
- Known addresses
- Known vehicles

---

### 6) Investigator Quick Actions (context-specific)

**When viewing a person**:
- Add as Suspect / Witness / Victim to case
- Start Interview Note
- Generate Photo Lineup (placeholder)
- Request Warrant Draft (placeholder)

**When viewing a case**:
- Add Supplement
- Add Evidence
- Assign Task
- Request Supervisor Review
- Export DA Packet

**When viewing an evidence item**:
- Mark submitted
- Attach lab result (placeholder)
- Add chain note

**Button hierarchy**: One primary action (filled, prominent). Others secondary (outline or muted). "Fast, decisive" feel—no hunting for actions.

---

## Demo Mode Enhancements

When Demo Mode is enabled:

- **Demo Insight badges** on summaries and connection nodes.
- **Richer placeholder narratives** (e.g., "Custody status updated 2 hours ago", "Court date scheduled", "Bond conditions apply").
- **Suggested Next Steps** box:
  - "Suggested: re-interview witness, check pawn records, verify alibi" (placeholders)
- **Unity advantage highlights**:
  - "Custody status updated 2 hours ago"
  - "Court date scheduled"
  - "Bond conditions apply"

No technical details—only the experience.

---

## Visual Design Principles (Investigation)

### Palette

- **More neutral than patrol**: Slate, charcoal, soft grays. Avoid bright accent overload.
- **Color sparingly**: Red for critical deadlines/blockers. Amber for attention. Green for ready/complete. Blue for links or secondary emphasis.
- **Professional**: Feels like a law enforcement workspace, not a consumer app.

### Typography

- **Big case title**: 1.25–1.5rem, semibold.
- **Clean subheaders**: Uppercase, tracked, muted.
- **Tight metadata**: Small, readable. Dates, IDs, status chips.

### Density & Whitespace

- Dense information, but structured. Clear sections. Whitespace between cards and blocks.
- Avoid form-like appearance. Workspace, not data entry.

### Urgency

- Red: court tomorrow, overdue task, critical blocker.
- Amber: due soon, pending lab, needs attention.
- Neutral: normal status.

---

## Demo Flow Walkthrough — Win the Room

**Goal**: Position Thin Line Platform as "from street to court, one system."

### Step 1: Start on Investigation Home

- Show My Active Cases with 3–5 placeholder cases.
- Point out status chips, days open, last activity.
- "This is your workload at a glance."

### Step 2: Open a Compelling Case

- Click "24-1032 | Burglary — 123 Maple St".
- Center loads Case Overview. Right shows case context.
- "One click. Full context."

### Step 3: Timeline Tells the Story

- Switch to Timeline tab.
- Show incident events, investigative actions, court/jail events.
- "Chronological. No digging. The story is right here."

### Step 4: Connections — Click Suspect Node

- Switch to Connections tab.
- Click "John Doe" node.
- Right panel updates: person context, custody status, next court date, conditions of release.
- "Same system. Jail. Court. RMS. No switching."

### Step 5: Unity Advantage — Jail + Court Signals

- Highlight custody status, next court date, bond conditions in Right panel.
- "Custody updated 2 hours ago. Court date scheduled. Conditions of release visible. All in one place."

### Step 6: Evidence Tab — Blocking Clarity

- Switch to Evidence tab.
- Point to "Awaiting lab results" blocking label.
- "You see what's blocking. No surprises."

### Step 7: DA Packet — Readiness + Export

- Switch to DA Packet tab.
- Show checklist: Statements ✓, Evidence logged ✓, Lab pending ✗, etc.
- "Ready or not. Clear reasons. One-click export when ready."

### Step 8: Closing Line

- "From street to court. One system. Thin Line Platform."

---

## Placeholder Data Summary

| Section | Example Placeholders |
|---------|----------------------|
| My Active Cases | 24-1032 Burglary, 24-0987 Agg Assault, 24-0912 Theft |
| My Tasks | Schedule interview (M. Jones), Submit evidence E-4421, Send subpoena |
| Pending Evidence | E-4421 At Lab, E-4402 Returned, E-4398 Submitted |
| Court & Jail | Court Mar 3 (24-1032), Doe bonded Feb 25, Conditions: No contact |
| Connections | John Doe ↔ 123 Maple St ↔ TX ABC123 ↔ Case 24-1032 |
| Smart Summary | "Primary suspect linked via shared address and vehicle…" |
| Suggested Next Steps | Re-interview witness, check pawn records, verify alibi |

---

*Document version: 1.0 — Investigation Interface Design*
