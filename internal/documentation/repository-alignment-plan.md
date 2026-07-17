# Repository alignment plan

**Repository:** `tls-docs-repo` (`c:\TLS2\tls-docs-repo`)  
**Phase:** 1 — Audit and plan (no content moves in this phase)  
**Date:** 2026-07-16  
**Status:** Draft for founder review

## Executive summary

`tls-docs-repo` today functions primarily as **in-application customer help** (user guides and release notes) consumed by Thin Line RMS via `VITE_APP_DOCSURL`. It does **not** yet serve as the durable source of truth for company strategy, operating procedures, implementation playbooks, or internal technical documentation described in the target model.

The highest-value near-term work is to:

1. **Preserve and reorganize existing customer content** without breaking the RMS in-app Help experience.
2. **Stand up the `internal/` tree** around the customer value stream and SOP framework.
3. **Replace the GitBook onboarding template** in `gitbook/` with a real repository entry point and navigation.
4. **Close product documentation gaps** (court, jail/corrections, citations, incidents, evidence) where pages are placeholders or missing.

---

## 1. Current repository structure

```
tls-docs-repo/
├── .git/
├── gitbook/                    # GitBook sync folder (template only)
│   ├── .gitbook/assets/        # 3 stock images
│   ├── README.md               # GitBook "Developer Platform" template
│   └── SUMMARY.md              # Single entry; not wired to repo content
├── guide/                      # In-app user guide (44 topic folders)
│   ├── guide.json              # Navigation manifest for RMS Help UI
│   └── <topic>/                # One folder per topic; <topic>.md + images
├── release-notes/              # In-app release notes (67 version folders)
│   ├── release-notes.json      # Navigation manifest for RMS Help UI
│   └── v_<major>_<minor>_<patch>/
│       └── v_<major>_<minor>_<patch>.md (+ images)
└── internal/                   # NEW (this plan only)
    └── documentation/
        ├── repository-alignment-plan.md
        └── content-inventory.md
```

### Scale (approximate)

| Asset type | Count |
|------------|------:|
| Markdown pages | 113 |
| Guide topic folders | 44 |
| Release-note version folders | 67 |
| Image files (png/jpg) | 429 |
| Duplicate image filenames across folders | 20 groups |

### No root-level files today

There is no repository `README.md`, no root `SUMMARY.md`, and no `.gitignore` visible at the repository root. Navigation for customer content lives in JSON manifests, not GitBook.

### Runtime integration (critical dependency)

Thin Line RMS loads documentation from GitHub raw content:

| Consumer | Path | Config |
|----------|------|--------|
| `ThinLine.UI/src/helpers/versionHelper.ts` | `guide/guide.json` → `guide/<label>/<label>.md` | `VITE_APP_DOCSURL` in `.env` |
| Same | `release-notes/release-notes.json` → `release-notes/<version>/<version>.md` | Same |

Current URL: `https://raw.githubusercontent.com/mkeslin/tls-docs-repo/main`

**Any move of `guide/` or `release-notes/` without a compatibility layer or coordinated UI change will break in-app Help.**

Alternate production host referenced in UI env comments: Azure blob (`tlsdocs.blob.core.usgovcloudapi.net`). **Decision needed:** whether GitBook, GitHub raw, blob storage, or multiple targets are authoritative for customer-facing docs.

---

## 2. Existing useful content

### Customer-facing user guide (`guide/`)

Substantive, screenshot-backed end-user documentation exists for:

| Area | Topics with real content |
|------|--------------------------|
| **Onboarding** | Getting started (login, password, support contact, remote assistance) |
| **General system** | Application navigation, browser management, reporting |
| **CAD** | Overview, units, calls, log search, self-dispatch |
| **Administration** | Overview, agency settings, codes, offenses, users, officers, CAD admin |
| **Master records** | Overview (partial), persons (broken — see risks), organizations (stub) |
| **Incidents** | PC affidavit only |
| **Notepads** | Overview, workflow, search/view/add/edit, connections |
| **Close patrols** | Overview (video), search/view/add/edit |
| **Warrants** | Overview, search/view/add/edit |
| **IBRS** | Comprehensive NIBRS error and warning reference |
| **Support** | FAQ (4 Q&As), troubleshooting (login and loading issues) |

`guide/guide.json` provides a stable navigation tree already aligned with product modules (CAD, Admin, Incidents, Citations, etc.).

### Release notes (`release-notes/`)

67 versioned markdown files from `v_0_001_01` through `v_6_4_0`, with `release-notes.json` grouping by major version. Recent notes (e.g. v6.4.x) document jail (JLM), intake, incidents, and court-related changes — useful customer-facing change history even where user guides are missing.

### GitBook folder (`gitbook/`)

Only the default GitBook onboarding template. The title, copy, external links, and sample API code are **not Thin Line content**. `SUMMARY.md` does not reference `guide/` or `release-notes/`.

### Internal content

**None** prior to this Phase 1 audit. Strategy, value stream, SOPs, implementation guides, and internal technical docs must be created.

---

## 3. Duplicate or conflicting content

### Structural duplication (images)

Twenty image filenames appear in more than one folder. Most significant:

| Pattern | Folders | Risk |
|---------|---------|------|
| CAD call screenshots | `cad_calls/`, `cad_selfdispatch/` | Intentional copy for self-contained folders; increases repo size and drift risk if one is updated |
| Admin tab screenshots | `admin_agency/`, `admin_audit_history/` | Same images duplicated; audit history page may overlap agency content |
| Release-note images | Multiple `release-notes/v_*` folders | Historical duplication across versions |

**Recommendation:** During customer-content migration, centralize shared assets under `customer/_assets/` (or per-module asset folders) and reference relatively. Do not deduplicate release-note historical images unless a separate archival policy is adopted.

### Content duplication and overlap

| Issue | Details |
|-------|---------|
| **Master overview vs. navigating application** | `master_overview.md` repeats navigation concepts covered in `navigating_application.md` |
| **CAD calls vs. self-dispatch** | Substantial procedural overlap; self-dispatch reuses call-editing imagery and steps |
| **Admin audit history** | Appears related to agency admin screens; scope boundary unclear |

### Placeholder vs. published pages

Twelve guide pages are `***Comming Soon***` placeholders but remain **visible** in `guide.json`. Users can open empty pages from in-app Help:

- All **Citations** guides (6 pages) except none have content
- All **Incidents** guides (4 of 5) except PC affidavit
- Both **Evidence** guides
- **Master overview** partial (vehicles, property, locations marked *coming soon*)

**Conflict:** Navigation promises content that does not exist. Either hide via `"visible": false` in `guide.json` or prioritize authoring.

### Broken or low-quality pages

| Page | Issue |
|------|-------|
| `guide/master_persons/master_persons.md` | Same image repeated 14 times; appears to be accidental paste, not documentation |
| `guide/master_organizations/master_organizations.md` | Three-line stub; no screenshots or procedures |
| `guide/navigating_application/navigating_application.md` | Stray `# ## Application Shells` heading typo |
| Multiple pages | Spelling/grammar inconsistencies (*Comming*, *inforamtion*, *quaracters*) |

### Dual navigation systems (conflicting IA)

| System | Location | Audience | State |
|--------|----------|----------|-------|
| `guide.json` + `release-notes.json` | `guide/`, `release-notes/` | RMS in-app Help | Active, authoritative for customers |
| `SUMMARY.md` | `gitbook/` | GitBook site | Template only; disconnected |

These must be unified under a single information architecture with clear rules for what appears in GitBook vs. in-app Help vs. internal-only.

### Product coverage gaps (not duplicate — missing)

No customer guide content found for:

- **Court** module
- **Jail / corrections (JLM)** — mentioned in release notes only
- **Mobile** workflows beyond citations placeholder
- **Accounting / payments** (may be intentional if customer-admin-only)

---

## 4. Missing foundational documents

### Strategy and operating system (`internal/strategy/`, `internal/operating-system/`)

| Document | Status |
|----------|--------|
| Vision and principles | Provided in planning brief; not yet in repo |
| Strategic roadmap 2026–2029 | Provided in planning brief; not yet in repo |
| Annual operating plan 2026 H2 | Missing |
| Quarterly scorecard template | Missing |
| Customer value stream overview | Provided in planning brief; not yet in repo |
| Per-stage value stream pages (Acquire → Advocate) | Missing (16 substages) |

### Standard operating procedures (`internal/sops/`)

No SOPs exist. Every value-stream stage needs at minimum a stage overview plus SOPs for repeatable work (data conversion, tenant provisioning, demo, contract, support triage, release communication, etc.).

### Implementation and customer success (`internal/implementation/`, `internal/customer-success/`)

No playbooks for:

- Data conversion methodology
- Bootstrap / tenant provisioning
- Training delivery
- Go-live and configuration
- Customer success check-ins and expansion

### Product and technical (`internal/product/`, `internal/technical/`)

No internal product architecture docs, module ownership matrix, release process documentation, or environment/infrastructure runbooks in this repo. (Some technical content may live in `ThinLineSoftware` monorepo — **Decision needed:** boundary between code-repo docs and docs-repo docs.)

### Policies, checklists, templates (`internal/policies/`, `checklists/`, `templates/`)

None present. Expected examples:

- Security and access policy
- Customer communication standards
- Demo checklist
- Go-live checklist
- Data conversion sign-off checklist
- Proposal / SOW templates

### Customer documentation (`customer/`)

Proposed Phase 2 tree does not exist. Existing content lives at legacy paths (`guide/`, `release-notes/`).

### Repository metadata

| Item | Status |
|------|--------|
| Root `README.md` | Missing |
| Root `SUMMARY.md` (GitBook) | Missing (only template in `gitbook/`) |
| Contribution / documentation standards | Missing (brief provides rules; not yet committed as policy) |
| Audience and confidentiality classification | Missing |

---

## 5. Recommended information architecture

Organize around **how Thin Line creates and delivers customer value**, with a hard separation between **internal** and **customer** content.

```
/
├── README.md                         # Repo purpose, audiences, how to contribute
├── SUMMARY.md                        # GitBook navigation (internal + customer top-level)
│
├── internal/                         # Staff-only (GitBook private space / access-controlled)
│   ├── strategy/
│   ├── operating-system/
│   │   ├── customer-value-stream.md
│   │   ├── acquire/ … advocate/     # Stage pages + links to SOPs
│   ├── sops/
│   ├── implementation/
│   ├── customer-success/
│   ├── product/
│   ├── technical/
│   ├── policies/
│   ├── checklists/
│   ├── templates/
│   └── documentation/                # Meta: standards, inventory, alignment
│
├── customer/                         # Customer-safe content
│   ├── README.md
│   ├── getting-started/
│   ├── rms/                          # Incidents, citations, warrants, master, IBRS, etc.
│   ├── cad/
│   ├── court/                        # TODO: new content
│   ├── jail/                         # TODO: new content
│   └── release-notes/
│
├── guide/                            # LEGACY — retain during transition (in-app Help)
└── release-notes/                    # LEGACY — retain during transition
```

### Principles for the target IA

1. **Value stream first for internal docs.** Every internal process document links upward to a value-stream stage (Acquire, Deliver, Operate, Expand, Advocate).
2. **One authoritative page per topic.** Stage overviews link to SOPs; SOPs link to checklists and templates — no copy-paste duplication.
3. **Customer content by product area**, not by legacy folder naming (`incidents_workflow` → `customer/rms/incidents/workflow.md`).
4. **Document type is explicit** in filename prefix or folder: `sop-`, `guide-`, `checklist-`, `template-`, `policy-`, `reference-`.
5. **Legacy paths remain until RMS Help is updated** or a redirect/compatibility layer is verified in production.

### GitBook vs. in-app Help

| Channel | Content | Navigation |
|---------|---------|------------|
| **GitBook (public or customer portal)** | `customer/**` | Root `SUMMARY.md` |
| **GitBook (private)** | `internal/**` | Root `SUMMARY.md` (restricted sections) or separate GitBook space |
| **RMS in-app Help** | Subset of `customer/**` (or legacy `guide/`) | `guide.json` until UI migrates |
| **RMS release notes panel** | `customer/release-notes/` | `release-notes.json` until UI migrates |

**Decision needed:** One GitBook space with visibility rules, or separate spaces for internal vs. customer.

---

## 6. Recommended migration and reorganization steps

### Step 0 — Governance (before moving files)

1. Approve this alignment plan and resolve decisions in Section 9.
2. Add root `README.md` documenting audiences, legacy paths, and contribution rules.
3. Add documentation policy to `internal/documentation/` (adapt rules from planning brief).
4. Define confidentiality labels: `internal-only`, `customer`, `customer-admin`.

### Step 1 — Stand up internal skeleton (Phase 2)

Create `internal/` tree with TODO skeleton pages. No customer content moves. Seed strategy and value-stream pages from the approved planning brief (not invented process detail).

### Step 2 — Fix critical customer content quality (no path changes)

Priority repairs at **existing paths** to avoid breaking RMS Help:

1. Fix `master_persons.md` (remove duplicate images; author real content or hide page).
2. Set `"visible": false` on placeholder guide pages **or** add minimal honest stubs ("Documentation in progress").
3. Expand `master_organizations.md` or hide until ready.
4. Typos and heading fixes on high-traffic pages (`getstarted`, `navigating_application`, `faq`).

### Step 3 — Introduce `customer/` tree (copy-then-cut)

1. Map each `guide/<label>/` folder to `customer/<area>/<topic>/` (see content inventory).
2. **Copy** content to new paths; verify markdown and image links.
3. Add `customer/README.md` as customer doc home.
4. Do **not** delete `guide/` until Step 5.

### Step 4 — GitBook entry point

1. Replace `gitbook/README.md` template with Thin Line customer doc home **or** promote root `README.md` as GitBook root and repoint GitBook sync to repository root.
2. Author root `SUMMARY.md` with Internal and Customer sections.
3. Remove or archive GitBook template assets and boilerplate.

### Step 5 — RMS Help integration update (coordinated release)

Update `ThinLine.UI` `versionHelper.ts` (and any blob publish pipeline) to load from new paths:

- `customer/guide.json` or path-mapper layer
- `customer/release-notes/release-notes.json`

Options:

| Option | Pros | Cons |
|--------|------|------|
| **A. Update UI paths** | Clean URLs | Requires app release + blob sync |
| **B. Keep `guide/` as symlink/publish copy** | No app change | Dual maintenance unless automated |
| **C. Redirect JSON at old paths** | Transitional | Old paths still exist |

**Recommendation:** Option A with a single release; use CI to publish `customer/` to blob and GitHub.

### Step 6 — Retire legacy paths

After verification in dev and production:

1. Remove `guide/` and top-level `release-notes/` **or** replace with thin redirect readmes pointing to `customer/`.
2. Update `release-notes.json` version labels if folder naming changes (e.g. `v_6_4_0` → `6.4.0` — only if worth the churn).

### Step 7 — Author missing product docs

Prioritize by sales and delivery pipeline:

1. Court
2. Jail / corrections (JLM)
3. Citations (replace placeholders)
4. Incidents and evidence workflows

### Step 8 — Internal SOP rollout

By value-stream stage, in priority order (see Section 8):

1. **Deliver** — data conversion, bootstrap, training, go-live
2. **Acquire** — demo, proposal, contract
3. **Operate** — support, product updates
4. **Expand** — customer success
5. **Advocate** — reference, referral

---

## 7. Proposed SUMMARY.md navigation

GitBook root `SUMMARY.md` — two top-level parts. Pages marked *(skeleton)* are Phase 2 placeholders.

```markdown
# Table of contents

## Internal

* [Documentation home](internal/documentation/README.md)
* [Vision and principles](internal/strategy/vision-and-principles.md)
* [Strategic roadmap 2026–2029](internal/strategy/strategic-roadmap-2026-2029.md)
* [Annual operating plan 2026 H2](internal/strategy/annual-operating-plan-2026-h2.md)
* [Quarterly scorecard](internal/strategy/quarterly-scorecard.md)

### Operating system

* [Overview](internal/operating-system/overview.md)
* [Customer value stream](internal/operating-system/customer-value-stream.md)

#### Acquire
* [Stage overview](internal/operating-system/acquire/README.md)
* [Awareness](internal/operating-system/acquire/awareness.md)
* [Cold leads](internal/operating-system/acquire/cold-leads.md)
* [Warm leads](internal/operating-system/acquire/warm-leads.md)
* [Hot leads](internal/operating-system/acquire/hot-leads.md)
* [Demo](internal/operating-system/acquire/demo.md)
* [Proposal](internal/operating-system/acquire/proposal.md)
* [Contract](internal/operating-system/acquire/contract.md)
* [Invoice](internal/operating-system/acquire/invoice.md)

#### Deliver
* [Stage overview](internal/operating-system/deliver/README.md)
* [Data conversion](internal/operating-system/deliver/data-conversion.md)
* [Bootstrap environment](internal/operating-system/deliver/bootstrap-environment.md)
* [Training](internal/operating-system/deliver/training.md)
* [Go-live / configuration](internal/operating-system/deliver/go-live-configuration.md)

#### Operate
* [Stage overview](internal/operating-system/operate/README.md)
* [Support](internal/operating-system/operate/support.md)
* [Product updates](internal/operating-system/operate/product-updates.md)

#### Expand
* [Stage overview](internal/operating-system/expand/README.md)
* [Customer success](internal/operating-system/expand/customer-success.md)
* [Expansion](internal/operating-system/expand/expansion.md)

#### Advocate
* [Stage overview](internal/operating-system/advocate/README.md)
* [Reference](internal/operating-system/advocate/reference.md)
* [Referral](internal/operating-system/advocate/referral.md)
* [Community](internal/operating-system/advocate/community.md)

### SOPs
* [SOP index](internal/sops/README.md)
* Acquire … Advocate subfolders mirror operating-system stages

### Implementation & customer success
* [Implementation index](internal/implementation/README.md) *(skeleton)*
* [Customer success index](internal/customer-success/README.md) *(skeleton)*

### Product & technical
* [Product index](internal/product/README.md) *(skeleton)*
* [Technical index](internal/technical/README.md) *(skeleton)*

### Policies, checklists, templates
* [Policies](internal/policies/README.md) *(skeleton)*
* [Checklists](internal/checklists/README.md) *(skeleton)*
* [Templates](internal/templates/README.md) *(skeleton)*

## Customer

* [Customer documentation home](customer/README.md)
* [Getting started](customer/getting-started/README.md)
* [Release notes](customer/release-notes/README.md)

### RMS
* [Overview](customer/rms/README.md)
* Incidents, citations, warrants, master records, IBRS, evidence, notepads, close patrols, administration

### CAD
* [Overview](customer/cad/README.md)

### Court
* [Overview](customer/court/README.md) *(TODO: new content)*

### Jail
* [Overview](customer/jail/README.md) *(TODO: new content)*
```

During transition, add a **Legacy** section pointing to `guide/` paths until retired.

---

## 8. Prioritized implementation sequence

| Priority | Work item | Owner (suggested) | Depends on |
|----------|-----------|-------------------|------------|
| **P0** | Founder review of this plan + decisions (Section 9) | Matthew, Eric F | — |
| **P0** | Root `README.md` and documentation standards policy | Matthew | P0 decisions |
| **P1** | Phase 2 internal skeleton (`internal/strategy`, `operating-system`, `sops` indexes) | Matthew | Plan approval |
| **P1** | Replace GitBook template; publish root `SUMMARY.md` | Matthew / Annie | GitBook space decision |
| **P1** | Fix broken `master_persons.md`; hide or stub placeholder guide pages | Eric Gibson / Annie | — |
| **P2** | Author **Deliver** stage SOPs (data conversion, bootstrap, go-live) | Matthew + Annie | Interviews with founders |
| **P2** | Author **Acquire** stage SOPs (demo, proposal, contract) | Eric Fugate | Pipedrive / process audit |
| **P2** | Create `customer/` tree; copy guide content | Annie | Path mapping approved |
| **P3** | Court and jail customer guides (new) | Eric Gibson + product | Product readiness |
| **P3** | Citations and incidents guide authoring | Eric Gibson | Screen captures |
| **P3** | RMS Help UI path migration (`versionHelper.ts`) | Matthew | `customer/` stable |
| **P4** | **Operate** SOPs (support, releases) | Eric Gibson + Matthew | Tooling decisions |
| **P4** | **Expand** and **Advocate** playbooks | Eric Fugate + Annie | CRM data |
| **P5** | Deduplicate shared images; editorial pass on legacy typos | Annie | Low risk anytime |
| **P5** | Retire `guide/` and top-level `release-notes/` legacy paths | Matthew | UI + blob verified |

---

## 9. Questions and decisions needed from founders

### Strategy and scope

1. **Is `tls-docs-repo` the single documentation source of truth**, or do `ThinLineSoftware` repo docs (`AGENTS.md`, `API-ARCHITECTURE.md`, etc.) remain authoritative for technical content with this repo linking to them?
2. **Confirm product name for customer-facing docs:** Thin Line Unity vs. Thin Line RMS/CAD (both appear in existing content).
3. **Geographic and module scope for customer docs:** Texas-only assumptions? Which modules are in scope for 2026 H2 (court, jail, mobile)?

### Publishing and access

4. **GitBook structure:** One space (internal + customer with permissions) or two spaces?
5. **GitBook sync root:** Repository root vs. `gitbook/` subfolder?
6. **Authoritative customer doc host:** GitHub raw, Azure blob, GitBook CDN, or combination?
7. **Who may access internal GitBook sections?** Full team vs. role-based.

### RMS in-app Help

8. **Timeline to migrate** `guide/` and `release-notes/` under `customer/` and update `ThinLine.UI`?
9. **Hide placeholder pages** in `guide.json` now, or show "in progress" stubs?
10. **Should in-app Help mirror GitBook customer content exactly**, or a subset?

### Operating model

11. **Confirm or correct ownership** per value-stream stage (Matthew, Eric Fugate, Eric Gibson, Annie).
12. **Annie's role boundaries:** implementation PM, marketing, customer success — which docs does she own first?
13. **Eric Fugate vs. Matthew on strategic sales:** where does strategic sales end and product/architecture begin in documentation?

### Process detail (do not invent — need input)

14. **Data conversion:** standard methodology, tools, sign-off criteria, typical cycle time?
15. **Tenant bootstrap:** manual steps today (Azure, Bicep, SQL scripts) — what is documented vs. tribal knowledge?
16. **Demo environment:** golden tenant? refresh cadence?
17. **Contract and billing:** Dropbox Sign + Stripe + Xero workflow — what is the canonical procedure?
18. **Support tiers:** hours, escalation paths, after-hours policy (getstarted mentions after-hours message — is that still accurate)?
19. **Release communication:** who writes release notes, review cycle, customer notification channel?

### Content quality

20. **`master_persons.md`:** repair from source material or rewrite from scratch?
21. **IBRS errors page:** customer-facing, internal reference, or both?
22. **Release notes versioning:** keep `v_6_4_0` folder convention or adopt semver folders?

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-16 | Phase 1 initial audit and plan |
