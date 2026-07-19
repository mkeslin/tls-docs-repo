# Supervisor Command Center — Design Document

> **Source of truth:** Internal Docs (GitBook). Paths under `ThinLine.UI/` and `ThinLine.API/` refer to the product monorepo.


**Thin Line Platform · Oversight Cockpit for Sergeants & Lieutenants**

This document describes layout, user experience, interaction design, visual hierarchy, and demo impact. No technical implementation details.

---

## Screen Structure Overview

Three-column command center layout matching the Patrol Command Center pattern:

| Column | Purpose |
|--------|---------|
| **Left** | Attention & Queues — triage, approvals, overdue, staffing |
| **Center** | Live Operations & Workload — primary workspace |
| **Right** | Context & Supervisor Actions — dynamic detail and decisions |

**Top Bar** spans full width with search, scope, time window, demo mode, and quick actions.

Responsive: on smaller screens, columns stack vertically. Left and Right panels collapse or become drawers when space is limited. Center remains primary.

---

## Top Bar Design (Supervisor)

### Contents

1. **Global Search**
   - Placeholder: "Search officer, call, address, person, case, report…"
   - Search preview results appear below input as user types (after 2+ characters)
   - Results grouped by type: Officers, Calls, Reports, Cases, Addresses, Persons
   - Example preview items:
     - "Officer J. Martinez | Unit 12 | On Scene 24-001"
     - "Call 24-001 | Domestic — 1200 Oak St | 18 min"
     - "Report R-2024-0892 | Pending approval | 2 days"
     - "Case 24-1032 | Burglary — Open | Det. Smith"
   - Clicking a result loads it into Center and Right panels

2. **View Scope Selector**
   - Options: **My Shift** | **My Team** | **All Units**
   - Default: My Shift
   - Controls which officers, calls, and queues appear across the screen
   - Prevents overwhelm by limiting scope; supervisors can expand when needed

3. **Time Window Selector**
   - Options: **Now** | **Last 24h** | **Last 7d**
   - Default: Now
   - Affects: overdue counts, aging items, trend data, approval queue age
   - "Now" = live state; "Last 24h/7d" = historical context for trends and backlog

4. **Demo Mode Toggle**
   - Checkbox or toggle: "Demo"
   - When on: enables Demo Insight badges, richer narratives, suggested actions, Unity advantage callouts

5. **Quick Actions** (compact buttons)
   - **Broadcast Message** — send to shift/team
   - **Create BOLO** — quick BOLO entry
   - **Assign Follow-Up** — assign task to officer
   - **Review Queue** — jump to Approvals Review tab
   - **Export Shift Summary** — export summary for shift handoff

### Top Bar Feel

- **Fast**: Search responds instantly; scope and time selectors are single-click
- **Calm**: No flashing alerts; status is conveyed via subtle indicators
- **Controlled**: Scope + time window prevent information overload — supervisor chooses what to see

---

## Left Column — Attention & Queues (Triage)

Stacked sections with bold counts and urgency. Highest priority at top. Each section uses a consistent card style: dark background, subtle border, left accent for severity.

### Severity System

| Level | Use | Visual |
|-------|-----|--------|
| **Info** | Normal status, no urgency | Neutral gray, no accent |
| **Caution** | Needs attention soon | Amber left border, amber text for counts |
| **Critical** | Immediate action required | Red left border, red sparingly for true urgency |

### 1) Attention Required (highest priority)

**Section header**: "Attention Required" with total count badge.

**Placeholder examples**:
- "2 High-Risk Calls Active (No backup within 5 min) — **Critical**
- "3 Calls Pending Dispatch > 8 min" — **Caution**
- "1 Officer Emergency Alert" — **Critical**
- "4 Use-of-Force reports not started (policy window)" — **Caution**

**Card style**: Each item is a clickable card. Critical items have red left border (2–3px). Caution items have amber left border. Text: primary line bold, secondary line smaller and muted.

**Click behavior**: Loads the item into Center panel (e.g., call list with that call highlighted, or UoF queue) and Right panel (context, risk signals, supervisor actions).

---

### 2) Approvals Queue

**Section header**: "Approvals Queue" with count badge.

**Placeholder examples**:
- "7 Reports pending approval · Oldest: 2 days"
- "3 Supplements pending review"
- "2 Evidence submissions requiring sign-off"
- "1 Policy exception (placeholder)"

**Display**: Count + oldest waiting time in subheader. Example: "7 items · Oldest: 2d 4h"

**Quick filters**: Pills or tabs — "Overdue" | "High Priority" | "New"

**Card style**: Each item shows report/case number, type, officer, age. Overdue items have amber accent.

**Click behavior**: Switches Center panel to **Approvals Review** tab and loads that report into the review workspace. Right panel shows report context, checklist, and approval actions.

---

### 3) Overdue & Aging

**Section header**: "Overdue & Aging" — "Bottleneck radar" feel.

**Placeholder examples**:
- "5 Reports overdue"
- "3 Cases with no activity 14+ days"
- "2 Cases with no activity 30+ days"
- "1 Warrant needing follow-up"
- "2 Court packets not ready (placeholder)"

**Card style**: Grouped by type. Each row: count + description. Aging tiers (14/30/60 days) use progressively stronger amber.

**Click behavior**: Jumps Center to relevant view (e.g., Team Workload filtered to overdue, or a case list). Right panel shows selected item with "Assign Follow-Up" action.

---

### 4) Resource & Staffing

**Section header**: "Resource & Staffing"

**Placeholder examples**:
- "8 Units available · 12 committed"
- "2 Break/lunch coverage gaps"
- "Investigator workload imbalance: Smith 12, Jones 4 (placeholder)"

**Card style**: Summary cards. Availability vs committed as a simple ratio. Gaps highlighted with amber.

**Click behavior**: Jumps Center to Live Operations (unit status) or Team Workload (investigator view). Right panel can show staffing summary.

---

## Center Panel — Live Operations & Workload (Primary)

Tabbed interface. Tabs: **Live Operations** | **Team Workload** | **Approvals Review** | **Trends**

### A) Live Operations (default tab)

**Active Calls List**
- Call number, type, location, priority, elapsed time
- Sort by priority, then elapsed time
- Selecting a call highlights it and updates Right panel
- Involved units shown inline or as badges

**Units Status Grid**
- Officers/units in a compact grid or list
- Status: Available | En Route | On Scene | Busy | Out
- Color-coded status (e.g., green available, amber en route/on scene, gray out)
- Click unit to load officer context in Right panel

**Coverage Gaps Mini Panel**
- "Areas with no nearby units" — e.g., "North sector — 0 units within 5 min"
- Compact list; clicking could highlight on map (placeholder)

**Escalation Suggestions** (placeholder)
- "Recommend adding backup" — for high-risk call with solo unit
- "Recommend supervisor response" — for call type or duration threshold
- Shown as subtle cards, not alarming

**Quick Supervisor Actions** (when call selected)
- Assign Backup (primary)
- Reassign Unit
- Add Supervisor Note
- Placeholders for: Create BOLO from call, Mark for After-Action Review

---

### B) Team Workload

**Workload Table/Tiles by Officer**
- Columns or tiles: Officer name, Active calls, Pending reports, Open cases, Overdues
- Visual "heat" indicators: green (light load), amber (moderate), red (overloaded)
- Sort by overdues, active calls, or name

**Drill-down**: Click officer to see their queue (reports, cases, tasks) in expanded view.

**Click behavior**: Loads officer profile + workload into Right panel. Actions: View workload, Reassign reports/cases, Message officer (placeholder), Flag for commendation / counseling note (placeholder, neutral).

---

### C) Approvals Review

**Clean Review Workspace**
- Report/supplement/evidence displayed in a focused, readable layout
- Side-by-side or stacked: document content + checklist

**Checklist Style**
- Required fields present
- Narrative quality flags (placeholder)
- Attachments present
- Policy compliance (placeholder)

**Diff/Changes Indicator** (placeholder)
- "New since last review" badge on changed sections

**Review Experience**
- Calm, standardized, no clutter
- One-click **Return for correction** with reason templates
- **Approve** and **Request supplement** as primary actions

**Reason Template Microcopy** (placeholders):
- "Please clarify probable cause…"
- "Add witness statement attachment…"
- "Update offense code to match narrative…"
- "Supplement needed for [section]…"

---

### D) Trends (Shift + Recent)

**Shift Snapshot**
- Response times (avg, p95)
- Arrests, citations, UoF count
- Pursuits (placeholder)
- Calls by type (breakdown)

**Trend Indicators**
- Simple up/down vs previous period (e.g., "↑ 12% vs last shift")
- Placeholders for comparison periods

**Tone**: Leadership glance, not analytics-heavy. A few key numbers, not dashboards.

---

## Right Column — Context & Supervisor Action Panel (Dynamic)

Updates based on selection: call, officer, report, or bottleneck item.

### 1) Primary Context Header

- **Title**: Call #, Officer Name, or Report #
- **Subheader**: Priority, elapsed time, status, location (as relevant)

Example: "Call 24-001" / "Domestic · 18 min · High · 1200 Oak St"

---

### 2) Risk & Liability Signals

**Only show signals that matter for supervisor decisions.** Not noisy.

**Placeholder examples**:
- "Solo unit on high-risk call"
- "History of weapons at address"
- "Use-of-force requires review within X hours (placeholder)"
- "Pursuit flagged (placeholder)"

**Visual**: Compact list, red only for critical. Amber for caution. Neutral for informational.

---

### 3) Smart Summary Box (Supervisor Phrasing)

**Placeholder example**:
> "Call has been active 18 min. One unit on scene. Prior violent incidents at location. Recommend adding backup."

Written for decision-making: what’s happening, what’s at risk, what to do.

---

### 4) Quick Supervisor Actions (Context-Specific)

**When viewing a call**:
- Assign Backup (primary)
- Reassign Unit
- Add Supervisor Note
- Create BOLO from call
- Mark for After-Action Review (placeholder)

**When viewing an officer**:
- View workload
- Reassign reports/cases
- Message officer (placeholder)
- Flag for commendation / counseling note (placeholder, neutral)

**When viewing a report for approval**:
- Approve
- Return for correction
- Request supplement
- Request evidence clarification

**Reason templates** (placeholders):
- "Please clarify probable cause…"
- "Add witness statement attachment…"
- "Update offense code to match narrative…"

---

### 5) Audit/Traceability Panel

**High trust, defensibility.** Subtle but visible.

- "Last touched by: [Officer] · [Date]"
- "Last updated: [Date/Time]"
- "Pending approvals: [Count]"
- "Policy flags: [Any]"

Compact, muted text. Supervisors value clear chain of custody and accountability.

---

## Demo Mode Enhancements

When Demo Mode is enabled:

1. **Demo Insight badges** on risk recommendations and bottleneck explanations
   - Small badge: "Demo Insight" — indicates enhanced narrative

2. **Richer placeholder narratives**
   - "This call resembles previous disturbance pattern at this address…"
   - "Similar incident 3 weeks ago — weapons recovered."

3. **Suggested Actions box**
   - 1–3 recommended steps (placeholders)
   - Example: "1. Assign backup. 2. Notify next shift. 3. Flag for AAR."

4. **Unity advantage callouts**
   - "Custody status changed 30 min ago"
   - "Court date scheduled"
   - "Bond conditions in effect"

No technical details — experience only.

---

## Visual Design Principles (Supervisor)

### Calm, Authoritative Feel

- Control tower, not form reviewer
- Decisive, not flashy
- Structured density: lots of info, grouped into decision-ready chunks

### Color Usage

- **Red**: Only for true critical risk (officer emergency, imminent danger)
- **Amber**: Caution — overdue, attention needed, policy window
- **Neutral (slate/gray)**: Most items, normal status
- **Green**: Available, approved, on track

### Typography

- **Big counts**: Section badges and key numbers stand out
- **Readable elapsed time**: Monospace or clear font for timers
- **Strong section headers**: Uppercase, tracking, muted color

### Layout

- Grouped chunks: each section is a clear block
- Avoid clutter: whitespace between sections
- Left column scrolls if needed; Center and Right adapt

---

## Placeholder Data Examples

### Attention Required
```
2 High-Risk Calls Active (No backup within 5 min)
3 Calls Pending Dispatch > 8 min
1 Officer Emergency Alert
4 Use-of-Force reports not started (policy window)
```

### Approvals Queue
```
R-2024-0892 · Report · Martinez · 2d 4h
R-2024-0889 · Supplement · Johnson · 1d
E-4421 · Evidence sign-off · Smith · 3d
```

### Overdue & Aging
```
5 Reports overdue
3 Cases — no activity 14+ days
2 Cases — no activity 30+ days
1 Warrant — follow-up needed
```

### Smart Summary (Call)
```
Call has been active 18 min. One unit on scene. Prior violent incidents at location. Recommend adding backup.
```

### Reason Templates (Return for Correction)
```
Please clarify probable cause…
Add witness statement attachment…
Update offense code to match narrative…
Supplement needed for [section]…
```

---

## Demo Flow Walkthrough (Win the Room)

**Goal**: Show chiefs and supervisors an oversight cockpit that keeps officers safe, keeps calls moving, ensures report quality, and spots risk before it becomes liability.

### Step 1: Start on Supervisor Command Center

- Land on the main view with **Attention Required** at top of left column
- Point out: "What needs me right now?" — triage at a glance
- Highlight scope: "My Shift" — only my people, my queues

### Step 2: Click a High-Risk Call

- Click "2 High-Risk Calls Active (No backup within 5 min)"
- Center shows call; Right shows:
  - Elapsed time: 18 min
  - Solo unit on scene
  - Risk history at location
- **One-click Assign Backup** — demonstrate immediate action
- Emphasize: "Officer safety first. No digging through screens."

### Step 3: Jump to Approvals Queue

- Click "7 Reports pending approval"
- Center switches to **Approvals Review** tab
- Show oldest report with checklist: required fields, attachments, narrative
- **Return for Correction** with reason template: "Please clarify probable cause…"
- Emphasize: "Quality control without the paperwork chase."

### Step 4: Show Overdue & Aging

- Click "5 Reports overdue" or "3 Cases — no activity 14+ days"
- Show bottleneck radar: what’s going stale
- **Assign Follow-Up** — one click to push work to the right person
- Emphasize: "Nothing falls through the cracks."

### Step 5: Show Team Workload

- Switch to **Team Workload** tab
- Show workload heat by officer: who’s overloaded, who has capacity
- Reassign an item (placeholder) — "Balance the board."
- Emphasize: "Fair distribution. No surprises at shift change."

### Step 6: Close with Defensibility

- Point to **Audit/Traceability** panel on Right
- "Last touched by, last updated, pending approvals, policy flags"
- Emphasize: "This prevents liability and keeps shifts running smoothly. One place. One view. Decisions, not data entry."

---

## Summary

The Supervisor Command Center is a **demo-winning oversight cockpit** that:

1. **Triages attention** — "What needs me right now?"
2. **Surfaces officer safety and risk** — before it becomes liability
3. **Streamlines approvals** — checklist-based, reason templates, one-click actions
4. **Balances workload** — heat by officer, reassign in one place
5. **Tracks timeliness** — overdue, aging, bottlenecks
6. **Provides a performance snapshot** — shift and trends at a glance

It feels **decisive, calm, and authoritative** — a control tower for sergeants and lieutenants, not a flashy or cluttered dashboard.
