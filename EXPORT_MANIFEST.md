# Export Manifest

## Purpose

This manifest defines export rules for Integrity Nexus.

Exports from this repository are architecture, governance, registry, or audit exports unless a different status is explicitly registered.

---

## Export Rule

An export must preserve:

- source repository identity,
- source file path,
- object ownership,
- claim status,
- limitations,
- and review status.

Exports must keep candidate, working, reviewed, and canonical statuses distinct.

---

## Required Export Fields

Each registered export should specify:

- EXPORT_ID
- EXPORT_TARGET
- SOURCE_PATHS
- SOURCE_COMMITS_OR_VERSIONS
- OBJECT_TYPES
- CLAIM_BOUNDARY
- LIMITATIONS_INCLUDED
- LM_READY
- REVIEW_STATUS

---

## Export Status Values

Allowed status values:

- draft
- ready-for-review
- approved
- superseded
- blocked
- archived

---

## Boundary Rule

Exported material is not automatically proven material.
LM-ready material is not automatically claim-complete material.
Governance export is not scientific derivation.
Summary is not source of truth.

---

## Initial Registry

No exports are registered in this manifest at creation time.

Future exports must be added explicitly through repository governance.
