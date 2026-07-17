# Permissions

Who can see and change evidence.

## Common claims (plain language)

| Capability | Typical meaning |
|------------|-----------------|
| **Evidence — Access** | Open Search, Inventory, Inventory Audit; view history |
| **Evidence — Modify** | Take property into custody; add history (IN / OUT / TR) |
| **Evidence — Admin** | Edit existing history rows and other elevated evidence actions |

Exact claim names vary; your administrator assigns them. Incident modify rights are also required to work from incident Property / Evidence tabs.

## Admin utilities

**Admin → Evidence** may show a placeholder (“utilities coming soon”) depending on build. Day-to-day room work does not depend on that screen — see [Admin — Audit, security, and jobs](../../admin/audit-security-jobs.md).

## Tips

- If **Add Evidence** or **Add History** is missing, check both Evidence modify and incident modify.
- Restrict history **edit** to supervisors — changing past custody rows affects legal defensibility.
- DA or limited roles may see incidents without evidence modify — that is expected.

## Related

- [Chain of custody](chain-of-custody.md)
- [Support — FAQ](../../support/faq.md) (missing modules)
