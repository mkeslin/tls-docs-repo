# Thin Line Software — Documentation

Durable documentation for Thin Line Software and the Thin Line Platform.

This repository is organized around how Thin Line creates and delivers customer value — not as a general company wiki.

## Two areas

| Area | Path | Audience | Purpose |
|------|------|----------|---------|
| **Internal** | [`internal/`](internal/) | Staff only | Company strategy, policies, operating procedures, implementation and customer-success playbooks, product backlog and design docs |
| **Customer** | [`customer/`](customer/) | Customers and partners | Training and support resources for Thin Line products |

Product **work items**, **plans**, and **design documents** (CAD, Jail, Court, and all modules): [`internal/backlog/`](internal/backlog/README.md).

## Application-consumed content (do not reorganize without a product release)

These paths are loaded by Thin Line RMS in-app Help. Leave them alone unless a coordinated UI change is planned:

| Path | Purpose |
|------|---------|
| [`guide/`](guide/) | In-app user guide (`guide.json` + topic folders) |
| [`release-notes/`](release-notes/) | In-app release notes (`release-notes.json` + version folders) |

## Navigation

GitBook spaces sync **folder roots**, not the whole-repo TOC:

| Space | Sync root | TOC file |
|-------|-----------|----------|
| Documentation (customer) | [`customer/`](customer/) | [`customer/SUMMARY.md`](customer/SUMMARY.md) |
| Internal Docs | [`internal/`](internal/) | [`internal/SUMMARY.md`](internal/SUMMARY.md) |

Root [`SUMMARY.md`](SUMMARY.md) is a combined index for local browsing; it does **not** drive the customer GitBook space.

## Documentation standards

- Prefer clear, direct language. No corporate filler.
- Do not invent product behavior, legal requirements, customer commitments, or internal procedures.
- When information is unknown, use a clearly labeled `<mark style="color:red;">**TODO:**</mark>` or `<mark style="color:red;">**Decision needed:**</mark>` note.
- Distinguish document types: **Policy**, **SOP**, **Guide**, **Checklist**, **Template**, **Reference**.
- Use relative Markdown links and keep [`SUMMARY.md`](SUMMARY.md) updated when pages are added, removed, or moved.
- Do not expose internal-only information in `customer/`.

Meta documentation for this repository: [`internal/documentation/`](internal/documentation/).
