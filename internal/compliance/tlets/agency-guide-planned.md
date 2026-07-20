# Agency TLETS application guide (planned — customer)

**Status:** <mark style="color:red;">Not published — internal-first</mark>  
**Intended audience (later):** Agency CJISO / coordinator / IT  
**Intended location:** `customer/implementation/tlets-interface-application.md` (and `customer/SUMMARY.md`)

---

## Why this page exists now

Thin Line is nailing down **internal** direct-interface materials first:

- [TLETS application (internal)](README.md)
- [Interface Questionnaire fill guide](interface-questionnaire.md)
- [Open decisions](open-decisions.md)

When decisions and packet wording are stable, convert a **customer-safe** subset into an agency-facing guide: what the agency must supply, sign, and send to DPS — without Thin Line engineering gaps, ORI placeholders, or unapproved access-level claims.

---

## Planned customer outline (draft)

1. What Thin Line is applying for (in-app TCIC/NCIC queries)
2. What stays agency-owned (ORI, users, network diagram, fingerprint sponsorship)
3. Documents the agency will receive from Thin Line
4. Documents the agency must complete or sign
5. How to forward the packet to DPS / coordinator
6. What happens after approval (TEST connection, go-live checklist pointer)

## Explicitly out of customer guide (keep internal)

- Safe-first vs product-vision answer tradeoffs
- Engineering status of XDAC connector / `LetsQuery`
- Unlocked ORI / access-level / multi-host decisions
- Vendor Q&A drafts and CPSO review flags

---

## Publish gate

Do **not** expand the customer page beyond the stub until:

- [ ] [Open decisions](open-decisions.md) D1–D7 resolved (or explicitly deferred with customer-safe TBD language)
- [ ] Fill guide answers match the submitted Word form for the pilot
- [ ] Scope language reviewed for customer tone (no internal red markers)

## Related

- Customer implementation pack (current): [`../../../customer/implementation/README.md`](../../../customer/implementation/README.md)
- Internal TLETS home: [README.md](README.md)
- Customer stub: [`../../../customer/implementation/tlets-interface-application.md`](../../../customer/implementation/tlets-interface-application.md)
