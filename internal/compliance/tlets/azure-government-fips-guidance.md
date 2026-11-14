# Microsoft Azure Government — FIPS 140 guidance notes

> Moved from TLS-App `Docs/TLETS/evidence/2026-05-14-microsoft-azure-government-fips-guidance.md` on 2026-11-14. Links into the old TLS-App attestation kit or application packet no longer resolve.

**Prepared for:** Thin Line Software LLC / Slaton PD TLETS-CJIS readiness  
**Prepared date:** 2026-05-14  
**Source:** Microsoft Learn, Azure compliance / Azure Government compliance pages.

## Microsoft guidance to use in packet wording

Microsoft describes FIPS 140 as a U.S. government standard for **cryptographic modules**, not for whole applications or cloud services.

Microsoft's Azure FIPS 140 offering states that the current CMVP implementation guidance **precludes a FIPS 140 validation for a cloud service**, but cloud service providers can **obtain and operate FIPS 140 validated cryptographic modules for the computing elements that comprise their cloud services**.

For Azure, Microsoft states that Azure is built from hardware, commercially available operating systems, and Azure-specific Windows versions that leverage FIPS 140 validated implementations. Microsoft also states that, through the Microsoft Security Development Lifecycle, Azure services use **FIPS 140 approved algorithms** for data security.

Microsoft's Azure FIPS 140 documentation specifically notes that Azure Storage service encryption uses the Windows cryptographic primitives library to provide **AES-256 data encryption at rest that is enabled by default**, and that the same is true for **Azure SQL Database transparent data encryption (TDE)** and encryption in other Azure services. The documentation also explains that Azure Storage or Azure SQL Database cannot themselves be packaged and submitted to NIST labs for FIPS validation; instead, those services rely on FIPS 140 validated encryption through the underlying operating-system cryptographic modules.

Microsoft further distinguishes **FIPS 140 validated** from **FIPS 140 compliant**:

- **FIPS 140 validated** means the cryptographic module, or product embedding the module, has been validated by CMVP.
- **FIPS 140 compliant** is an industry term for products that rely on FIPS 140 validated products for cryptographic functionality.

Microsoft states that FIPS 140-2 has been superseded by FIPS 140-3. CMVP guidance allows FIPS 140-2 modules to remain active for five years after validation or until **2026-09-21**, when FIPS 140-2 validations move to the historical list. Microsoft notes that a certificate moving to the historical list does **not** mean the certificate was revoked, but agencies are advised not to include those modules in new procurements and should make their own risk determination.

## Thin Line packet wording

Use the following language for Thin Line RMS hosted in Azure Government:

> Thin Line RMS is hosted in Microsoft Azure Government. Microsoft states that FIPS 140 validation applies to cryptographic modules, not to a cloud service as a whole. Microsoft further states that cloud service providers can obtain and operate FIPS 140 validated cryptographic modules for the computing elements that comprise their cloud services, and that Azure services use FIPS 140 approved algorithms for data security. For Azure SQL Database transparent data encryption (TDE), Microsoft states that TDE relies on FIPS 140 validated encryption through the underlying operating-system cryptographic modules. Thin Line therefore documents the Azure Government services, TLS configuration, Azure SQL TDE status, and any customer-managed key or HSM configuration in use for the deployment, rather than representing Thin Line RMS itself as a FIPS-validated product.

Use the following caution where the audit asks about FIPS mode or FIPS validation:

> Thin Line does not represent the Thin Line RMS application or Azure cloud service itself as FIPS 140 validated. FIPS evidence should be tied to the cryptographic modules, Azure Government service configuration, TLS/certificate settings, Azure SQL TDE, and any Azure Key Vault or Managed HSM configuration used by the deployment. Any statement that a system is operated in a FIPS-approved mode requires configuration evidence for the relevant module and service.

## Source links

- Microsoft Learn — Azure Government compliance: https://learn.microsoft.com/en-us/azure/azure-government/documentation-government-plan-compliance
- Microsoft Learn — Federal Information Processing Standard (FIPS) 140, Azure Compliance: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-fips-140-2
- Microsoft Learn — Federal Information Processing Standard (FIPS) Publication 140-2, Microsoft Compliance: https://learn.microsoft.com/en-us/compliance/regulatory/offering-fips-140-2
