# Vendor Q&A — round 3 (Q21–30)

> Moved from TLS-App `Docs/TLETS/correspondence/vendor-qna-round3-partial.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

Captured from stakeholder responses plus repository CI survey for **Q28**.

---

## Q21 — PWA installs

**Answer:** **PWA installs are allowed for users.**

**⚠ OPS / CPSO pairing:** Allowed ≠ unmanaged—document agency policy for sworn devices (managed browser expectations, screenshot retention, Sentinel signals for rogue installs).

---

## Q22 — CJIS mobile policy **5.13.5** special reporting wording

**Answer:** Respondent **unsure**.

**Interpretation helpers:** Decide whether Thin Line’s packet **references only agency AA** (“SL8N adopts policy 5.13.5 processes; RMS is browser-mediated”) versus producing **vendor-side** attestations — **coordinate with CPSO + SL8N** jointly.

---

## Q23–Q24 — “Dedicated interface server” sentences & TLETS connector workflow

**Answer:** Respondent **unsure** on both.

**Next step:** CPSO-aligned draft text can come from **`Docs/TLETS/attestation-kit/03-architecture-and-data-flow.md`** and **`Docs/TLETS/application/`** (**lawful iteration with ISO**).

---

## Q25 — “TLS policy screenshots” (what it means — plain English)

CPSOs want **Vendor proof HTTPS is configured acceptably**:

1. Browser → **`tls-slatontx-prod-ui`** (often **minimum TLS 1.2** or TLS 1.2+ documented).  
2. UI → **`tls-slatontx-prod-api`**.

Collect **Exports / screenshots**:

- Azure Portal → each **App Service** → **Networking / TLS / SSL Settings** (**minimum TLS**) + inbound certificate binding status.  
- If **Azure Front Door / AGW**: corresponding **cipher policy** blade.

Store redacted screenshots under **`Docs/TLETS/evidence/`**.

---

## Q26 — FIPS / cryptography sentence for packet

**Answer:** Respondent **unsure**.

**Recommendation:** Choose **Tier A wording** (**Microsoft Azure Government + platform crypto responsibility + Thin Line appendix exports TLS**) until counsel approves sharper FIPS 140‑3 claims (**avoid self-certifying OS “FIPS mode”** absent engineering packet).

---

## Q27 — Who reviews / merges prod release changes

**Answer:** **Matthew Keslin** reviews **and merges all changes pushed to **`release`** branches** feeding **production** pipelines.

**(Repo hook:** [`ThinLine.API/ThinLine.App.V5.Release.Build.Pipeline.yml`](../../../ThinLine.API/ThinLine.App.V5.Release.Build.Pipeline.yml) triggers on **`release/**`**. Canary path uses **`ThinLine.API/ThinLine.App.V5.Canary.Pipeline.yml`** on **`master`**.)

---

## Q28 — Automated checks during CI (surveyed YAML + local scripts)

_Source of truth snippets:_ [`ThinLine.API/ThinLine.App.V5.Release.Build.Pipeline.yml`](../../../ThinLine.API/ThinLine.App.V5.Release.Build.Pipeline.yml), [`ThinLine.API/ThinLine.App.V5.Canary.Pipeline.yml`](../../../ThinLine.API/ThinLine.App.V5.Canary.Pipeline.yml). Root orchestration **[`package.json`](../../../package.json)** for optional **`npm run verify`**.

### Azure DevOps (release + canary pipelines)

| Stage / job | Gates observed |
|-------------|----------------|
| **BuildApi** (`windows-2022`) | **`dotnet restore`** → **`dotnet build`** (**Release**) on projects including **`ThinLine.API.UnitTests`**, **`ThinLine.Ibrs.Test`** → **`dotnet test`** on same projects `--no-build --no-restore` → **`dotnet ef migrations script`** (multi-context SQL idempotent scripts, **ThinLine Data Store**) → **`dotnet publish`** (`ThinLine.RMS.WebAPI`, self-contained **`win-x64`**, zipped to artifact **`drop-api`**) |
| **BuildUi** (`windows-2022`, Node **24.14.0**) | **`npm ci`** → **`npm run build`** (**Vite prod build**) → zip **`ThinLine.UI/dist`** (**`drop-ui`**) |

### **Not observed** as hard pipeline gates _(may exist elsewhere)_ 

⚠ Repo-wide search of these **`*.Pipeline.yml`** files found **no** explicit **`eslint`**, **`npm audit`**, **SonarQube/CodeQL**, **credential scan**, **`npm run test` / Vitest**, or **`Playwright`** steps.

### Developer / hygiene scripts (offline / discretionary)

[`package.json`](../../../package.json) delegates **`ui:lint`**, **`ui:typecheck`**, **`ui:test`**, **`ui:build`**; **`verify`** merges API build+tests with UI **`vitest`** + **`vite build`** (**AGENTS.md** notes TypeScript backlog).

**⚠ Recommendation:** CPSO questionnaires prefer **truthful enumeration**—“**PR merge gates**:** dotnet test + prod UI build**. **Supplemental** ESLint / Vitest locally or future pipeline tasks.” Elevate selectively if SLA demands (**document roadmap**).

---

## Q29 — Thin Line facilitation / primary follow-up contacts

**Answer:**  

- **Matthew Keslin** — facilitates **approval process**.  
- **Eric Gibson** — **primary contact** for CPSO/package **follow‑ups**.

---

## Q30 — “What?” (Slaton police diagram signatory)

Plain English: Assessors sometimes require **agency attestation on network diagrams**:

- **`Date last revised`**, **`For Official Use Only`** banner, verifying **topology accuracy** (“Slaton CJIS workstations shown distinct from RMS cloud”).

Thin Line drafts diagrams; **Slaton PD** designates **Chief / CJISO / IT manager** (“**agency signatory name**”).  

**⚠ OPS fill:** Ask Slaton PD: _“Who signs FOUO network exhibits?”_

---

_End of paused batch._
