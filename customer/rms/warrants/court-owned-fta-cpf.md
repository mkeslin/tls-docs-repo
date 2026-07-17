# Court-owned FTA and CPF

How Court Violations create and update warrants, and how LE records service.

## Two systems, one warrant

| Side | Typical actions |
|------|-----------------|
| **Court** | Issue FTA warrant, Issue CPF warrant(s), Recall warrant, Mark warrant executed |
| **Warrants (WAR)** | View court-owned warrant, add **Service Attempts**, print/attach; limited edit when COURT OWNED |

See also [Court — FTA, warrants, and bonds](../../court/fta-warrants-bonds.md).

## FTA (failure to appear)

Typical court path:

1. Defendant misses appearance → court marks FTA (and sets show cause as required).
2. Clerk/judge uses **Issue FTA warrant** (or equivalent) on the court violation.
3. Thin Line creates a linked warrant (often type **AR** / arrest warrant style) and advances the court case toward an FTA warrant state.
4. LE locates/serves and records service in WAR; court may **Mark warrant executed** or sync from completed service rules.
5. **Recall FTA warrant** returns the court case toward the FTA / show-cause track and updates warrant status (for example **REC**).

## CPF (capias pro fine)

Post-judgment non-compliance may use **Issue CPF warrant(s)** (single or batch). CPF warrants are court-owned enforcement tools; LE still records service attempts in WAR when serving them.

## PD responsibilities

- Search and open the warrant (including court-generated indicators).
- Add diligent **service attempts**.
- Complete service / attestation when policy and the UI require it for court-owned returns.
- Coordinate with court before assuming a recall or clear — do not “fix” court warrants by adding a second local warrant.

## Status language (common)

| Code / idea | Meaning |
|-------------|---------|
| **ACT** (Active) | Serviceable |
| **CLR** (Cleared) | No longer active — often after execute / completion |
| **REC** (Recalled) | Recalled by court / process |

Exact descriptions are ALL CAPS code descriptions in your agency lists.

## Related

- [Service attempts](service-attempts.md)
- [Search warrants](search.md)
- [Court — work queues](../../court/work-queues.md)
