# Mobile citations

Issuing citations on mobile / patrol and importing them into RMS.

## Mobile issue (patrol)

Officers with mobile citation access can create and issue citations from the patrol / mobile citation workspace (often reached from Dashboard or patrol tools). Those records sync to RMS.

Exact mobile screens vary by deployment; training for your agency’s device build should cover field entry. This page focuses on what records staff see in RMS afterward.

## SYNCED status

When a mobile citation arrives in RMS awaiting master-data verification, workflow status is commonly **SYNCED**.

On detail, normal tabs are replaced by the **Mobile Citation Import** stepper, for example:

1. Verify General  
2. Location  
3. Person  
4. Vehicle  

Match or create the correct master person and vehicle, confirm location and header data, then complete import so the citation becomes a normal RMS record (draft/issued path per your rules).

## Find SYNCED work

Use [Citation Search](search.md) with workflow **SYNCED** (and source **Mobile**) to clear the import backlog.

## Print

After import / issue, use [Print and attachments](print-and-attachments.md). **Print Mobile Citation** may be available when configured.

## Tips

- Do not leave large SYNCED backlogs — court handoff and reporting expect cleaned masters.
- If import cannot match a person, resolve masters carefully to avoid duplicates.
- Support-only tools (Analyze / Import OCR, sync debug) are not part of everyday officer workflow.

## Related

- [Draft to Issued](draft-to-issued.md)
- [Person, vehicle, and location](person-vehicle-location.md)
- [Citation to court](citation-to-court.md)
