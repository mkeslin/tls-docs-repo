# Citation to court

How issued citations become **court violations** for clerks.

## Relationship

| LE side | Court side |
|---------|------------|
| **Citation** + offense line(s) | One or more **court violations** |
| Citing officer / issued ticket | Clerk / judge workflow in Court Violations |

Court processing (plea, judgment, payments) happens in [Court](../../court/README.md), not on the Citations Offenses tab.

## How handoff happens

Depending on agency configuration, court violations may be created:

1. **Automatically** when a citation is completed / issued and Court is active for the agency, and/or  
2. Through **Court Citation Import** / import tools used during go-live or catch-up (often support-assisted).

Your implementation team documents which path your agency uses. Day-to-day, officers should **issue** complete citations; clerks work the resulting violations in Court (for example New Case Review).

## What clerks need from the citation

Before handoff, LE side should have:

- Correct person and vehicle
- Offenses (warning vs charge set correctly)
- Court / appearance information when used
- **Issued** status when your court path requires it

## Voiding and corrections

- **Court void / dismiss / transfer** applies to the **court violation**.
- **Reset for Edit** on the citation (when allowed) is an LE correction path — see [Draft to Issued](draft-to-issued.md).
- Coordinate LE and court before changing an issued ticket that already has an active court case.

## Related Court topics

- [Create and import cases](../../court/create-and-import.md)
- [Getting around](../../court/getting-around.md) (Court)
- [Court clerk workshop](../../training/court-clerk-workshop.md)

## Related

- [Offenses and warnings](offenses-and-warnings.md)
- [Draft to Issued](draft-to-issued.md)
