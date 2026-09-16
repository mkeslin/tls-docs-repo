# Master Merge — Exact Duplicates

**Document type:** SOP  
**Phase:** Operate · Support / post-conversion cleanup  
**Status:** v0.1  
**Audience:** Internal — Thin Line Support and Implementation  
**Related:** [Post-conversion utilities](../deliver/data-migration/post-conversion-utilities.md) · customer [Duplicates and merge](../../../customer/getting-started/master-records/duplicates-and-merge.md)

---

## Purpose

Merge master records that share the same **canonical identity key** (exact duplicates) from Thin Line Admin, without asking agency staff to use **Admin → Master Merge**.

Agency day-to-day merge stays on Masters search → **Merge**.

---

## When to use

- Post-conversion cleanup when many people / vehicles / locations share a plate, DL, address, or other exact key
- Support tickets where scored duplicates are too noisy and the identity key is already trusted
- After a large import when Implementation agrees the key is safe to merge

Do **not** use Exact Duplicates for “looks similar” clusters — that is the **Scored** tab (see backlog **BL-025**).

---

## Preconditions

1. Target environment has applied:
   - `20260915212120_MergeExactDuplicateProcedures`
   - `20260916103630_ExactDuplicateExclusionsAndEligibility`
2. Operator has Thin Line Support access to **Admin → Master Merge**.
3. Product owner / Implementation has approved bulk merge for that agency and master type.

---

## Current state (product UI)

1. Open **Admin → Master Merge**.
2. Choose the **Exact Duplicates** tab and the master type (person, location, organization, property, vehicle).
3. Review groups. Sort as needed. Confirm the key is truly the same real-world entity.
4. **Merge** a group (or selected groups). The API runs `dbo.MergeExactDuplicate*` once per group and returns survivor / merged counts.
5. If a group is **not** the same entity (shared “UNKNOWN” name, shared placeholder plate, etc.), **Exclude** it. It leaves the list until someone removes the exclusion.
6. Open **Exact Duplicate Exclusions** to review or restore an excluded key.

Unknown-name person and organization groups are gated in the procedure so they do not merge as if they were one identity.

---

## Do not

- Hand the Admin Master Merge screen to agency administrators as a training path.
- Merge a key you have not sampled (open two members and compare attachments / records first).
- Edit `Sql/MergeExactDuplicate*.sql` without a **new** EF migration — already-migrated databases do not re-run the procedure deploy.

---

## Follow-up

- Spot-check the survivor on Masters search and a recent incident / citation / court case.
- Large person runs: use the simulation script under `Scripts/` before production if volume is high.
- <mark style="color:red;">**TODO:**</mark> Record default owner and a review date after the first production use of exclusions.

---

## Related backlog

- **BL-024** Master search coalesce + faster person merge
- **BL-025** Finish scored duplicates
