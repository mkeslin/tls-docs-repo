# Business Systems Architecture

**Phase:** Company Operating System  
**Document Type:** Architecture  
**Status:** Living Document  
**Owner:** Matthew Keslin

---

## Purpose

This document defines the purpose of each major business system used by Thin Line Software, establishes the **system of record** for each type of information, and provides the long-term roadmap for evolving Thin Line Hub into the company's operational platform.

The objective is **not** to consolidate everything into a single application.

Instead, the objective is to ensure every piece of information has **one canonical home**, while allowing systems to integrate and evolve over time.

This document should guide future process improvements, delegation, automation efforts, and product development.

---

## Guiding Principles

### One Source of Truth

Every type of information should have exactly one authoritative home.

Other systems may display or synchronize the information, but ownership belongs to only one system.

---

### Document Before Automating

A process should first be:

1. Understood
2. Documented
3. Standardized

Only then should it be automated or replaced.

---

### Buy Before Build

Thin Line should leverage mature third-party platforms whenever they already solve the problem well.

Internal development should focus on workflows that are unique to Thin Line Software or create strategic competitive advantages.

---

### Operational Data vs. Knowledge

Not all information is the same.

Knowledge explains **how** work is performed.

Operational data describes **what is currently happening.**

Artifacts provide evidence that work was completed.

Understanding this distinction is critical when deciding where information belongs.

---

## Systems of Record

| System | Owns | Purpose |
|----------|------|---------|
| GitBook | Knowledge | SOPs, policies, guides, templates, company operating system |
| Pipedrive | Revenue & Pipeline | Leads, opportunities, implementations, projects |
| Thin Line Hub | Operations | Customers, environments, deployments, operational dashboards |
| OneDrive / SharePoint | Project Artifacts | Contracts, assessments, exports, reports, deliverables |
| Git Repositories | Source Code | Product code, migration tools, infrastructure, automation |
| Xero | Accounting | Invoices, bookkeeping, financial reporting |
| Stripe | Billing | Payment processing and subscriptions |
| Gusto | Payroll | Employees and payroll |

---

## Information Categories

### Knowledge

Knowledge answers:

> "How do we perform this work?"

Examples:

- SOPs
- Guides
- Policies
- Checklists
- Templates
- Architecture

**System of Record**

GitBook

---

### Operational Data

Operational data answers:

> "What is happening right now?"

Examples:

- Current implementation phase
- Deployment status
- Customer health
- Environment status
- Outstanding issues

**System of Record**

Thin Line Hub

---

### Project Artifacts

Artifacts answer:

> "What evidence exists that work was completed?"

Examples:

- Contracts
- Migration assessments
- Customer exports
- Validation reports
- Customer approvals
- Training recordings
- Signed documents

**System of Record**

OneDrive / SharePoint

---

### Source Code

Examples:

- Application source
- SQL scripts
- Migration scripts
- Infrastructure code
- Bicep
- PowerShell
- APIs

**System of Record**

Git

---

### Financial Records

Examples:

- Invoices
- Payments
- Journal entries
- Payroll
- Taxes

**Systems of Record**

Xero

Stripe

Gusto

---

## Current Operating Model

### GitBook

GitBook is the company's knowledge base.

Its purpose is to document:

- Company Operating System
- Strategy
- SOPs
- Policies
- Technical documentation
- Implementation guides
- Customer documentation
- Templates

GitBook answers:

> "How do we do this?"

GitBook is **not** responsible for tracking live work.

---

### Pipedrive

Pipedrive currently manages:

- Sales pipeline
- Opportunities
- Implementations
- Customer onboarding

Pipedrive answers:

> "Where is this customer in our pipeline?"

Although implementation tracking will eventually move into Thin Line Hub, Pipedrive remains the implementation system until Hub provides equivalent functionality.

---

### Thin Line Hub

Thin Line Hub is the operational platform.

Its purpose is to provide visibility into live operations.

Examples include:

- Customers
- Environments
- Deployments
- Health
- Dashboards
- Operational status

Hub answers:

> "What is happening?"

Hub should not become another documentation platform.

---

### OneDrive / SharePoint

OneDrive stores project artifacts.

Examples:

```
Customers/

    Levelland/

        Contracts/

        Assessments/

        Data/

        Reports/

        Deliverables/
```

OneDrive is intentionally simple.

It stores files.

It does not own processes.

---

### Git

Git stores executable assets.

Examples:

- SQL
- C#
- PowerShell
- Infrastructure
- Migration scripts
- Mapping definitions

Migration tooling currently lives in the **product monorepo** under `Utilities/Migration Tools/` (may become its own repository later).

Canonical layout (see [Migration Package Standards](../sops/deliver/data-migration/vendor-packages/migration-package-standards.md)):

```
Utilities/Migration Tools/

    PROCESS.md                 ← agent-led engagement procedure

    CrimeStar/
    CopSync/                   ← COPsync / Kologik
    IncodeCourt/               ← Tyler / INCODE + Common V14 court
    Xpediter/

    <each Vendor>/
        VERSION
        AgencyChecklist.md
        ConvertedAgencies.md
        StagingImporter/       ← when applicable
        SqlPackage/
            Pipeline/ or Common/
            Overrides/*.TEMPLATE.sql
```

Agency-specific filled scripts and checklist answers live under `Clients/<Client>/Conversion/` (and/or Team Drive)—not in the shared vendor Pipeline.

---

## What Belongs Where?

| Question | System |
|-----------|---------|
| How do we perform a migration? | GitBook |
| What stage is Levelland currently in? | Thin Line Hub |
| Where is the signed SaaS agreement? | OneDrive |
| What SQL converts a CopSync / CrimeStar / Xpediter agency? | Product Git — Migration Tools + client Conversion folder |
| Has the invoice been paid? | Xero / Stripe |
| What is our payroll expense? | Gusto |

---

## Legacy System Migration Example

### GitBook

Contains:

- Legacy Migration SOP
- Assessment Guide
- Validation Guide
- Vendor Guides

---

### OneDrive

Contains:

- Completed Assessment
- Customer Export
- Validation Reports
- Deliverables

---

### Git

Contains:

- Conversion scripts
- SQL
- Mapping logic

---

### Thin Line Hub

Displays:

Customer

↓

Migration Status

↓

Current Phase

↓

Assigned Owner

↓

Timeline

↓

Related SOP

↓

Artifacts

↓

Environment

---

## Long-Term Vision

The current implementation process spans multiple disconnected systems.

Future implementations should be orchestrated through Thin Line Hub.

The Hub should become the execution layer while GitBook remains the knowledge layer.

Example workflow:

```
Start Implementation

↓

Generate Assessment

↓

Complete Checklist

↓

Provision Environment

↓

Run Migration

↓

Validate

↓

Schedule Training

↓

Go Live

↓

Transition to Support
```

Each stage references the appropriate SOP while tracking live operational progress.

---

## What Thin Line Hub Should Own

Future operational capabilities include:

- Customer implementations
- Migration assessments
- Implementation timelines
- Operational dashboards
- Environment management
- Customer health
- Deployment tracking
- Customer success
- Internal workspaces

These are operational workflows rather than documentation.

---

## What Thin Line Hub Should NOT Replace

The following systems already perform their responsibilities well:

### GitBook

Continue using GitBook for documentation.

---

### Git

Continue using Git for source control.

---

### Xero

Continue using Xero for accounting.

---

### Stripe

Continue using Stripe for payments.

---

### Gusto

Continue using Gusto for payroll.

---

### OneDrive / SharePoint

Continue using OneDrive for project artifacts and customer files.

Hub should reference these artifacts rather than duplicating storage.

---

## Evolution Roadmap

### Phase 1 — Document

Capture company knowledge.

- Write SOPs
- Document processes
- Standardize terminology
- Create templates

Primary Platform:

GitBook

---

### Phase 2 — Standardize

Reduce inconsistency.

- Standard folder structures
- Standard assessments
- Standard implementation process
- Standard artifacts

Primary Platforms:

GitBook

OneDrive

---

### Phase 3 — Integrate

Connect systems together.

Examples:

- Hub links to GitBook SOPs
- Hub references customer artifacts
- Hub displays implementation status
- Hub references environments

Avoid duplicating information.

---

### Phase 4 — Replace

Only replace third-party tools when Thin Line provides significantly greater value.

Examples:

- Replace implementation tracking in Pipedrive
- Replace Word-based assessments
- Replace spreadsheets
- Replace manual implementation dashboards

Do **not** replace mature commodity platforms unless they become strategic constraints.

---

## Decision Framework

Before building a new capability inside Thin Line Hub, ask:

### Does a mature platform already solve this problem?

If yes:

Integrate.

Do not rebuild.

---

### Is this workflow unique to Thin Line?

If yes:

Build it.

---

### Will this improve scalability?

If no:

Do not build it.

---

### Will this reduce founder dependency?

If yes:

Prioritize it.

---

### Does this create a competitive advantage?

If yes:

Strong candidate for Hub.

---

## Future Workspaces

Long-term, Thin Line Hub should become the operational home for specialized workspaces.

Examples:

- Implementation Workspace
- Sales Workspace
- Customer Success Workspace
- Development Workspace
- Executive Workspace

Each workspace should combine:

- Live operational data
- Related SOPs
- Checklists
- Dashboards
- Artifacts
- Reports

The workspace executes the process.

GitBook explains the process.

---

## Architecture Summary

The operating model can be summarized by three questions.

### GitBook

**How do we perform the work?**

Knowledge.

---

### Thin Line Hub

**What is happening right now?**

Operations.

---

### OneDrive

**Where is the evidence?**

Artifacts.

---

These three systems work together rather than competing with one another.

---

## Open Decisions

- Should customer assessments remain documents or become structured records in Thin Line Hub?
- When should implementation management migrate from Pipedrive into Thin Line Hub?
- What integrations should be built between Hub and GitBook?
- Should migration tooling become its own repository?
- Should customer artifacts remain in OneDrive long term or eventually migrate into Hub?

---

## Review Schedule

Review this document quarterly as Thin Line's internal operating systems evolve.

Update whenever:

- A new business platform is adopted
- A system of record changes
- A major workflow moves into Thin Line Hub
- Significant automation or integration work is completed

---

## Vision

The goal is **not** to replace every business application.

The goal is to create a cohesive operating system where:

- Knowledge is documented.
- Work is visible.
- Artifacts are organized.
- Financial records remain authoritative.
- Commodity tools are leveraged.
- Thin Line Hub becomes the operational layer that connects the entire business.

By documenting first, standardizing second, integrating third, and replacing only where it creates meaningful strategic value, Thin Line Software can scale without creating unnecessary complexity or rebuilding tools that already solve the problem well.
