# Object Ownership Manifest

## Purpose

This manifest defines ownership boundaries for objects referenced, mapped, imported, or exported by Integrity Nexus.

Object ownership is structural ownership only.
It does not imply scientific completion or proof status.

---

## Ownership Rule

Each object must have exactly one primary source-of-truth location.

Integrity Nexus may reference or map external objects, but it does not automatically become the owner of those objects.

---

## Ownership Categories

Allowed ownership categories:

- local-governance-object
- local-registry-object
- local-audit-object
- imported-reference-object
- exported-package-object
- cross-repository-interface-object

---

## Required Ownership Fields

Each registered object should specify:

- OBJECT_ID
- OBJECT_NAME
- OBJECT_TYPE
- PRIMARY_OWNER_REPOSITORY
- PRIMARY_OWNER_PATH
- LOCAL_REFERENCE_PATH
- OWNERSHIP_CATEGORY
- CLAIM_BOUNDARY
- REVIEW_STATUS

---

## Boundary Rule

Mapped objects remain owned by their declared source repositories.
Imported references remain references unless explicitly promoted by governance.
Export packages remain derived packaging layers, not primary source-of-truth objects.

---

## Initial Registry

No object entries are registered in this manifest at creation time.
