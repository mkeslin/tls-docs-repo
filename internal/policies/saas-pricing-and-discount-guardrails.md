# SaaS pricing and discount guardrails

**Document type:** Policy  
**Status:** v0.2 — <mark style="color:red;">Draft</mark> (working commercial guidance; refine module splits as needed)  
**Audience:** Internal — Acquire, founders (do **not** publish to customers)  
**Related:** [Acquire authority matrix](acquire-authority.md) · [Prepare proposal](../sops/acquire/prepare-proposal.md) · [Migration Pricing Policy](migration-pricing.md) · [Go-to-market](../strategy/go-to-market.md)

---

## Purpose

Give Acquire a **pricing card** so standard proposals can go out without a fire drill, while protecting margin and scope.

This policy covers **recurring SaaS** and common one-time fees. Detailed migration tiers also live in [Migration Pricing Policy](migration-pricing.md) — keep the two consistent.

---

## Sizing anchor (law enforcement)

| Rule | Guidance |
|------|----------|
| **Primary anchor** | About **$1,000 per officer per year** for a typical LE platform deal |
| **Not seat-based** | Do **not** bill per named user/seat; officer count is a **sizing** input for the annual total |
| **Smaller agencies** | Effective rate is usually **closest** to the full ~$1,000/officer anchor |
| **Larger agencies** | Total may grow with size while **effective $/officer** can land lower (example direction: Levelland-scale ~**$50,000**/year for their officer count) |
| **Sanity check** | Compute `officers × ~$1,000`, then adjust for modules included, term, and strategic fit — document the math in Pipedrive |

---

## Modules / packages

Sell **whatever modules the agency needs** (à la carte). Packaging still must follow [Go-to-market](../strategy/go-to-market.md) (Court/Jail with RMS/CAD path; no standalone court outbound for now).

| Package / module | How to price (working) | Notes |
|------------------|------------------------|-------|
| **RMS + CAD** (typical LE) | Size to ~**$1,000/officer/year** for the combined LE stack | Default LE proposal shape |
| **RMS only** or **CAD only** | About **55–70%** of the full LE stack total for that agency size — **not** a second full $1,000/officer on top when both are sold | Avoid double-counting the anchor |
| **Court** (1 clerk / 1 judge ICP) | Include in the overall annual total; keep the deal coherent with the LE anchor when sold together | <mark style="color:red;">**TODO / Decision needed:**</mark> set a clearer Court-only add-on band (e.g. flat annual range) once agreed |
| **Jail** (~15-bed ICP) | Include in the overall annual total when sold with RMS/CAD path | <mark style="color:red;">**TODO / Decision needed:**</mark> set a clearer Jail add-on band once agreed |
| **Bundle** | No fixed SKU bundle — compose from modules needed | — |

Until Court/Jail add-on bands are set, Acquire should propose a total using the LE anchor + modest add-on, and **escalate to founder** if Court/Jail is a large share of the deal or the total feels outside recent comps.

---

## One-time fees

| Fee | Guidance | Acquire may quote alone? |
|-----|----------|---------------------------|
| **Virtual training** | **Free** | Yes |
| **In-person training** | Bill **Thin Line’s cost** (travel/lodging/etc. as applicable) | Yes — itemize cost basis in proposal/Pipedrive |
| **Data conversion / migration** | Working commercial range **$2,000–$5,000** by size/complexity; still follow assessment gate in [Migration Pricing Policy](migration-pricing.md) | Yes **within** $2k–$5k after assessment supports it; outside range or $0 waiver → founder |
| **Hardware** | Pass-through / case-by-case | Usually escalate / ops |

<mark style="color:red;">**TODO:**</mark> Reconcile Migration Pricing Policy tier dollar amounts with this **$2,000–$5,000** working range so both docs match.

---

## Discount authority (recommended bands)

| Discount from guidance total | Authority |
|------------------------------|-----------|
| **0% to 10%** | Acquire alone |
| **Above 10% up to 25%** | Founder approval (document in Pipedrive) |
| **Above 25%**, fee waiver, free modules, or $0 migration | Founder only |

Use discounts primarily to win **longer terms** or strategic Priority 1 logos — not to paper over custom product work.

---

## Term

| Term | Guidance |
|------|----------|
| **Preference** | **Longer is better** — prefer **multi-year** (target **3 years** when the agency will accept it) |
| **1-year** | Allowed; price at guidance (do not stack an extra “short-term penalty” unless founder directs) |
| **Multi-year incentive** | Acquire may apply the **full 0–10%** band to secure 3+ years without founder approval |
| **Beyond 10% for term** | Founder approval |

Proposal validity: **90 days** (see [Prepare proposal](../sops/acquire/prepare-proposal.md)).

---

## Commercial file locations

| Artifact | Location |
|----------|----------|
| Master proposal template | **SharePoint** (Thin Line commercial library) |
| Deal folders / sent proposals | **SharePoint** |
| Contract / CJIS templates | **SharePoint** |
| Executed agreements | **Pipedrive** (deal) **and** **SharePoint** |

<mark style="color:red;">**TODO:**</mark> Add exact SharePoint folder URLs/names when stabilized so Acquire does not rely on memory.

---

## Rules

1. Start from the **officer-count anchor**, then adjust for modules and term — do not invent unrelated round numbers.  
2. **Custom product work is not a discount lever** — see [Acquire authority](acquire-authority.md) and GTM disqualifiers.  
3. **Migration:** prefer assessment first; quote **$2,000–$5,000** only when complexity fits; else escalate. Proposal may say “migration priced after assessment” when not ready.  
4. **Court / Jail packaging** must match [Go-to-market](../strategy/go-to-market.md).  
5. Document the pricing math (officers, modules, term, discount %) in **Pipedrive** on every proposal.

---

## Proposal checklist (pricing)

Before sending a proposal:

- [ ] Officer count (or sizing basis) noted  
- [ ] Modules match discovery notes  
- [ ] Total coherent with ~$1,000/officer anchor **or** founder approval logged  
- [ ] Discount ≤ 10% **or** founder approval logged  
- [ ] Term stated (prefer multi-year)  
- [ ] Training: virtual free / in-person at cost if applicable  
- [ ] Migration called out correctly (N/A, TBD after assessment, or $2k–$5k / approved exception)  
- [ ] Validity **90 days**  
- [ ] No promised custom features  

---

## Change history

| Date | Change |
|------|--------|
| 2026-07-26 | v0.2 — officer anchor, training/migration fees, discount bands, term preference, SharePoint locations |
| 2026-07-22 | v0.1 — structure + authority bands; prices TODO |
