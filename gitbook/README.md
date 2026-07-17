# Thin Line Software documentation

This `gitbook/` folder previously held a GitBook onboarding template. Canonical documentation now lives at the **repository root**.

- [Documentation home](../README.md)
- [Table of contents](../SUMMARY.md)
- Internal: [`../internal/`](../internal/documentation/README.md)
- Customer: [`../customer/`](../customer/README.md)

<mark style="color:red;">**Decision needed:**</mark> Point the GitBook space sync root at the repository root (recommended) so `SUMMARY.md` and the `internal/` / `customer/` trees publish correctly. Application-consumed paths `guide/` and `release-notes/` remain at the repo root and should not be reorganized without a product release.
