# Data Integrity Interface Design

> **Source of truth:** Internal Docs (GitBook). Paths under `ThinLine.UI/` and `ThinLine.API/` refer to the product monorepo.


**Thin Line Platform — System Health Cockpit for Data Integrity Officers**

This document describes the layout, user experience, interaction design, and demo flow for the Data Integrity interface. It follows the same three-column command center pattern as Patrol and Investigation Command Centers, tuned for data quality, record health, master record management, and audit readiness.

---

## Screen Structure Overview

The Data Integrity screen uses a three-column layout:

| Left Column | Center Column | Right Column |
|-------------|---------------|--------------|
| Integrity Queues & Alerts | Record Analysis & Comparison Workspace | Context & Corrective Actions |
| ~1fr | ~2fr | ~1fr |

A full-width **Top Bar** spans above all columns. The layout is structured, analytical, and calm — a professional cockpit for records supervisors, RMS admins, and QA roles.

---

## Top Bar Design (Data Integrity)

### Contents

**Global Search**
- Placeholder: "Search Person, Vehicle, Address, Incident, Citation, Case, Evidence, Master Record ID"
- Search preview results show:
  - Record type (e.g., Person, Incident, Citation)
  - Integrity status chip (Healthy / Warning / Critical)
  - Primary identifier (name, ID, plate, etc.)
- Results are clean and scannable; clicking a result loads it into the Center workspace.

**Filters (visible but not overwhelming)**
- **Issue type**: Open Issues | Duplicates | Association Gaps | Validation Errors | All
- **Severity**: Critical | High | Medium | Informational
- **Time**: Last 7 days | Last 30 days | All time

Filters appear as compact pill-style toggles or dropdowns. Active filters show a subtle indicator (e.g., filled background or checkmark). Severity is communicated with small, restrained color chips — red only for Critical, amber for High, slate for Medium/Info. No alarming visuals; precision over drama.

**Demo Mode Toggle**
- Checkbox or switch labeled "Demo"
- When enabled, shows richer placeholder narratives and "Demo Insight" badges throughout the interface.

**Quick Actions**
- **Run Integrity Scan** (placeholder) — triggers a system-wide scan
- **Export Audit Report** — exports current view or full audit trail
- **Create Merge Review** — starts a new merge review workflow
- **Configure Rules** (placeholder) — opens rule configuration (disabled or modal placeholder in demo)

### Visual Hierarchy
- Search is the dominant element (flexible width, max ~400px)
- Filters grouped logically; severity and time filters slightly smaller than issue-type filters
- Quick actions as secondary buttons; primary action (e.g., Run Integrity Scan) slightly emphasized
- Top bar background: neutral slate; no accent except a subtle left border when critical issues exist

---

## Left Column — Integrity Queues & Alerts

Stacked sections with counts and severity indicators. Each section is a collapsible card. Items are clickable and load into the Center workspace.

### 1. Critical Integrity Issues

**Purpose:** Surface records that pose reporting or legal risk.

**Card style:** Dark background, left border in red (restrained — not bright). Section header with count badge.

**Placeholder examples:**
- 3 Incidents with Missing Required Offense Data
- 2 Citations Without Linked Person Master Record
- 1 Arrest With No Booking Disposition
- 4 Evidence Items Missing Chain-of-Custody Entry

**Click behavior:** Clicking an item loads it into the Center workspace, opens the Record Detail tab, and highlights the problematic area. The Right panel shows corrective actions.

**Severity:** Red reserved for true compliance or legal risk only.

---

### 2. Duplicate Master Records

**Purpose:** Help users identify and merge duplicate persons, vehicles, addresses.

**Card style:** Neutral slate; amber accent only for high-confidence matches. Each item shows match confidence and last activity.

**Placeholder examples:**
- 12 Potential Duplicate Persons
- 3 Potential Duplicate Vehicles
- 5 Potential Duplicate Addresses

**Per-item display:**
- Match confidence (e.g., "92% match")
- Last activity date
- Brief identifier (e.g., "John Smith / J. Smith")

**Click behavior:** Opens side-by-side Compare & Merge view in the Center panel.

---

### 3. Association Gaps

**Purpose:** Discovery-oriented — find records that co-occur but are not formally linked.

**Card style:** Informational; blue-grey accent. Less urgent than Critical or Duplicates.

**Placeholder examples:**
- Incidents Without Linked Person
- Citations Without Linked Vehicle
- Cases Without Primary Location
- Persons Frequently Co-Occurring But Not Linked

**Click behavior:** Loads the Associations tab in Center with the relevant pattern highlighted. Suggestion box appears when applicable.

---

### 4. Compliance & Reporting Flags

**Purpose:** NIBRS, statutory, and reporting validation issues.

**Card style:** Similar to Critical but amber/slate for non-critical compliance items.

**Placeholder examples:**
- 6 Records Failing NIBRS Validation
- 2 Reports Missing Statutory Fields
- 3 Arrests Missing Charge Codes

**Click behavior:** Loads validation detail into the Center Validation tab.

---

### 5. System Health Snapshot

**Purpose:** Small summary of overall data health.

**Card style:** Compact, muted. No urgency — informational only.

**Placeholder content:**
- % Records with complete required fields (e.g., "94%")
- Duplicate rate trend (e.g., "↓ 12% vs last month")
- Merge actions this month (e.g., "8 merges")
- Open integrity issues by category (mini breakdown)

**Interaction:** Read-only summary; no click-to-load. Provides at-a-glance confidence.

---

### Left Column — General Behavior

- **Severity system:** Critical (red) | High (amber) | Medium (slate) | Info (muted)
- **Selected state:** Selected item has a left border accent (emerald or slate-400) and slightly darker background
- **Empty states:** "No critical issues" or "No duplicates" with a subtle checkmark or neutral message
- **Scroll:** Left column scrolls independently if content exceeds viewport

---

## Center Panel — Record Analysis & Comparison Workspace

Primary analytical area. Tabbed interface, similar to other command centers.

### Tabs

| Tab | Purpose |
|-----|---------|
| Record Detail | Single record view with integrity signals |
| Compare & Merge | Side-by-side comparison for duplicate resolution |
| Associations | Co-occurrence patterns and suggested links |
| Validation | Structured validation failures and corrections |
| Audit History | Chronological log of edits, merges, corrections |

---

### A) Record Detail Tab

**Layout:**
- Clean record header: **Record Type** + **ID** + **Status**
- **Integrity Status Badge:** Healthy | Warning | Critical (small, restrained)

**Content:**
- Record fields in a structured layout
- **Problematic fields** highlighted with a subtle visual indicator (e.g., light amber background or left border) — not alarming, just noticeable
- **Related Records** list: incidents, citations, cases, evidence linked to this record
- **Integrity Signals** summary box

**Integrity Signals example (placeholder):**
> "Missing primary offense code. No linked vehicle. Possible duplicate person record."

**Interaction:** Clicking a related record loads it. Clicking a problematic field could scroll to it or open a quick-edit context (placeholder).

---

### B) Compare & Merge Tab

**Layout:**
- Side-by-side comparison of two master records
- Left: Record A | Right: Record B
- **Differing fields** highlighted (e.g., name spelling, DOB, DL, address, identifiers)
- **Shared related records** shown in a middle or bottom section (incidents, citations in common)

**Merge Impact Summary:**
- # Incidents affected
- # Citations affected
- # Cases affected

**Primary Record selector:** Radio or dropdown to choose which record survives the merge.

**Safe merge preview (placeholder text):**
> "After merge, 14 incidents and 3 citations will reference Master Record #10231."

**Interaction:**
- Non-destructive preview — user must confirm before merge
- Clear confirmation step (no implementation details — just UX flow)
- Emphasis on traceability: "This action will be logged in Audit History"

---

### C) Associations Tab

**Layout:**
- Analytical view of co-occurrence patterns

**Placeholder examples:**
- "Person A and Person B appear together on 5 incidents."
- "Vehicle TX ABC123 appears in 3 cases with different driver spellings."

**Relationship visualization:** Simple, not flashy — e.g., two nodes with a line, or a list with connecting lines. Concept: clarity over aesthetics.

**Suggestion box:**
> "Suggested Association: Link Person A and Person B as Associates (confidence 78%)."

**Interaction:** User can accept suggestion, ignore, or add a note. Right panel shows corrective actions when a suggestion is selected.

---

### D) Validation Tab

**Layout:**
- Structured list of validation failures
- Each row: Field name | Required/optional | Current value | Suggested correction (placeholder)

**Interaction:**
- Quick jump-to-field behavior (clicking a row scrolls or focuses the field)
- **Mark as Reviewed** option with reason (dropdown: "Intentional", "Pending correction", "Out of scope", etc.)

**Tone:** Methodical, not punitive. Focus on resolution.

---

### E) Audit History Tab

**Layout:**
- Chronological log of:
  - Record edits
  - Merge actions
  - Field corrections
  - User who performed action
  - Timestamp

**Filters:** By user, date range, action type.

**Emphasis:** Defensibility and transparency. Every change is traceable. Clean, scannable list — no clutter.

---

## Right Column — Context & Corrective Action Panel (Dynamic)

Updates based on the selected item in the Center.

### 1. Record Context Header

- Record type + ID
- Created date
- Last modified date
- Created by / Last modified by

**Style:** Compact, muted. Provides provenance at a glance.

---

### 2. Integrity Risk Summary

**Placeholder example:**
> "This record impacts 14 incidents and 3 citations. Missing required NIBRS element. Potential duplicate exists."

**Style:** Brief, scannable. Amber or slate background if risks exist.

---

### 3. Impact Scope

- Count of linked records (incidents, citations, cases, evidence)
- Reporting impact (placeholder, e.g., "2 monthly reports affected")
- Court packet impact (placeholder, e.g., "1 open case packet")

**Style:** Bullet or list format. Small, factual.

---

### 4. Corrective Actions (Context-Specific)

**When viewing validation error:**
- Edit Record (placeholder)
- Mark as Reviewed
- Assign to User
- Add Integrity Note

**When viewing duplicate pair:**
- **Merge** (primary action — slightly emphasized)
- Dismiss Match
- Flag for Further Review
- Assign Merge Review

**When viewing association suggestion:**
- Create Association
- Ignore Suggestion
- Add Note

**Style:** Buttons or links. Primary action (e.g., Merge) more prominent. Secondary actions subdued.

---

### 5. Integrity Notes Panel

- **Add structured note** — text area with optional reason/tag
- **Placeholder examples:**
  - "Confirmed duplicate via matching DL and DOB."
  - "Spelling variation only; records represent same subject."
- **Prior notes** displayed in chronological order

**Style:** Compact list. Notes are read-only once saved; add-new at top.

---

### 6. Audit Warning Banner (Subtle)

When an action is high-impact:
> "This action will affect 27 linked records."

**Style:** Muted banner, not alarming. Appears above corrective actions when relevant.

---

## Demo Mode Enhancements

When Demo Mode is enabled:

- **Demo Insight badges** appear on association suggestions and duplicate matches
- **Richer placeholder narratives:**
  - "High-confidence duplicate based on DOB, SSN fragment, and shared incident history."
- **Trend callouts:**
  - "Duplicate rate decreased 18% since last month."
- **Unity advantage highlight:**
  - "Merged record automatically updated 12 incidents, 3 citations, and 1 open case."

**Tone:** Demonstrates value without technical detail. Focus on outcomes and trust.

---

## Visual Design Principles (Data Integrity)

### Palette
- **Calm, analytical:** Blues, greys, slate tones
- **Red only** for compliance or legal risk (Critical severity)
- **Amber** for High severity and caution
- **Muted accents** for Medium and Informational

### Typography
- Strong record IDs and field labels — easy to scan
- Monospace or distinct font for IDs if helpful
- Clear hierarchy: section headers > labels > values

### Layout
- Structured, grid-based
- Consistent spacing; no clutter
- Precision over density — white space supports focus

### Trust & Defensibility
- Every destructive or high-impact action has a preview and confirmation
- Audit trail is always visible
- No hidden actions; everything is traceable

---

## Placeholder Data Examples

### Critical Integrity Issues
| Issue | Count |
|-------|-------|
| Incidents with Missing Required Offense Data | 3 |
| Citations Without Linked Person Master Record | 2 |
| Arrest With No Booking Disposition | 1 |
| Evidence Items Missing Chain-of-Custody Entry | 4 |

### Duplicate Master Records
| Type | Count | Example |
|------|-------|---------|
| Potential Duplicate Persons | 12 | John Smith / J. Smith — 92% match |
| Potential Duplicate Vehicles | 3 | TX ABC123 / TX ABC 123 — 88% match |
| Potential Duplicate Addresses | 5 | 123 Maple St / 123 Maple Street — 95% match |

### Integrity Signals (Record Detail)
- "Missing primary offense code. No linked vehicle. Possible duplicate person record."
- "Chain of custody gap: 3 days between transfer and receipt."

### Merge Impact Summary
- 14 incidents affected
- 3 citations affected
- 1 open case affected

---

## Demo Flow Walkthrough — Win the Room

### Step 1: Start on Data Integrity Home View
- Show the **Critical Integrity Issues** count (e.g., 10 items)
- Emphasize: *"We surface risks before they become audit findings or reporting failures."*
- Point out the System Health Snapshot: *"94% of records have complete required fields — and we know exactly which 6% need attention."*

### Step 2: Click a Duplicate Master Record
- Select "12 Potential Duplicate Persons" → click a specific pair
- Center loads **Compare & Merge** tab with side-by-side view
- Show **Merge Impact Summary**: "14 incidents, 3 citations will reference the primary record"
- Demonstrate **safe merge preview**: *"You see exactly what will change before you confirm. No surprises."*
- Highlight: *"Every merge is logged. Full audit trail."*

### Step 3: Switch to Associations Tab
- Show co-occurrence insight: "Person A and Person B appear together on 5 incidents"
- Demonstrate **suggested association**: "78% confidence — Link as Associates?"
- Emphasize: *"We help you discover connections that might otherwise be missed."*

### Step 4: Open a Validation Error
- Click "3 Incidents with Missing Required Offense Data"
- Center loads **Validation** tab
- Highlight the missing required field with subtle indicator
- Show **Mark as Reviewed** with reason: *"Sometimes the right answer is 'intentional' — we capture that, too."*

### Step 5: Open Audit History
- Switch to **Audit History** tab
- Show chronological log: merges, corrections, who did what, when
- Emphasize: *"Public records requests, internal audits, court discovery — you have a defensible trail for every change."*

### Step 6: Closing Positioning Statement
> *"Thin Line doesn't just store your data — it protects its integrity across Patrol, Investigations, Jail, and Court. The Data Integrity cockpit gives your records team the visibility and control they need to stay audit-ready and compliant."*

---

## Summary

The Data Integrity interface is a **system health cockpit** for Data Integrity Officers. It:

1. **Surfaces critical risks** first — compliance and legal exposure
2. **Makes merge and correction workflows safe** — preview, confirm, trace
3. **Provides visibility into systemic patterns** — duplicates, associations, trends
4. **Ensures audit traceability** — every action logged and filterable
5. **Prevents accidental destructive actions** — clear previews and confirmations

The design is precise, trustworthy, and methodical — not flashy. It matches the Patrol Command Center pattern while tuning every element for data quality and defensibility.
