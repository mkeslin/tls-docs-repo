# Product updates

**Phase:** Operate  
**Desired outcome:** Deliver improvements customers can understand

## Inputs

Roadmap, bugs, feedback, support fires

## Outputs

Production release; benefit-led in-app New features; optional customer email; Support brief

## Owner

**Keslin** (priority and customer message) · Engineering (deploy) · Support (follow-up questions)

## Current process

Regular releases; often fire-driven; organized loosely by module. In-app New features points at dry release notes. Little customer email.

## Target process

[Publish product update](../../sops/operate/publish-product-update.md) — ship when ready with weekly heartbeat; email only when it earns attention; rewrite New features in benefit language.

## Tooling

Azure DevOps · In-app New features · Email ([template](../../templates/customer-release-email.md))

## Capacity (today)

Weekly when active

## Cycle time

1–2 days typical ship

## Maturity

**1 / 5 — Founder-driven** → next milestone: email yes/no + benefit-led in-app notes on every user-visible ship

## What would break first?

Release coordination; Support surprised by changes

## Continuous improvement (10x ideas)

| Lens | Idea |
|------|------|
| Reduce / Simplify | Manual note writing |
| Standardize | Release comms checklist |
| Automate | CI/CD, draft notes from work items |
| Delegate | Engineering owns deploy; product owns message |
| Scale | Continuous delivery + digest email |

## Product responsibility

**Keslin** — what ships and what customers are told. Engineering — how it ships safely.

## Related documents

- SOP: [Publish product update](../../sops/operate/publish-product-update.md)
- Template: [Customer release email](../../templates/customer-release-email.md)
- Policy: [Operate authority](../../policies/operate-authority.md)
- Sibling: [Triage support request](../../sops/operate/triage-support-request.md)
