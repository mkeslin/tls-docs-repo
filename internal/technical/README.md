# Technical

Internal technical runbooks and references for environments, releases, and infrastructure.

## Purpose

Document how Thin Line builds, deploys, and operates the platform — for staff, not customers.

## Contents

<mark style="color:red;">**TODO:**</mark> Add runbooks for:

- Azure environments and tenant provisioning (Bicep)
- Azure DevOps pipelines and release process
- Database / SQL operational notes (non-destructive)
- Access and secrets handling (no secrets in this repo)

<mark style="color:red;">**Decision needed:**</mark> What stays in the `ThinLineSoftware` monorepo vs. this docs repo. Prefer linking to authoritative engineering docs rather than duplicating them.

## Related

- [Product](../product/README.md)
- [Operate — product updates](../customer-value-engine/operate/product-updates.md)
- [Deliver — Infrastructure](../customer-value-engine/deliver/infrastructure.md)

## Safety

Do not commit connection strings, API keys, or customer data. Prefer `<mark style="color:red;">**TODO:**</mark>` pointers to secure stores.
