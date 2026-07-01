# Import Manifest

## Purpose

This manifest defines how external or connected repository material may be imported into Integrity Nexus.

It is a structural governance file only.
It does not validate, derive, or promote scientific claims.

---

## Import Rule

Material imported into Integrity Nexus must retain:

- source repository identity,
- source path,
- source status,
- claim boundary,
- and review status.

No imported object becomes canonical merely by being copied, summarized, referenced, or exported.

---

## Required Import Fields

Each registered import should specify:

```text
IMPORT_ID:
SOURCE_REPOSITORY:
SOURCE_PATH:
SOURCE_COMMIT_OR_VERSION:
OBJECT_TYPE:
LOCAL_TARGET_PATH:
IMPORT_STATUS:
CLAIM_BOUNDARY:
REVIEW_STATUS:
```

---

## Import Status Values

Allowed status values:

```text
referenced
candidate
reviewed
superseded
archived
blocked
```

---

## Boundary Rule

```text
Imported != canonical.
Referenced != derived.
Reviewed != proven.
Mapped != owned.
```

---

## Initial Registry

No imports are registered in this manifest at creation time.

Future imports must be added explicitly through repository governance.
