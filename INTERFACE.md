# Repository Interface

## Purpose

This document defines the interface boundary of the Integrity Nexus repository.

Integrity Nexus acts as a meta-governance and architecture repository for the Integrity Nexus research architecture.
It maps connected repositories without replacing their local source-of-truth files.

---

## Source-of-Truth Boundary

Integrity Nexus may define:

- cross-repository governance structure,
- repository role boundaries,
- shared interface expectations,
- import and export conventions,
- claim-boundary standards,
- and LM-export readiness criteria.

Integrity Nexus must not silently override:

- domain-specific proofs,
- repository-local canonical status files,
- repository-local registries,
- repository-local paper status,
- or repository-local scientific limitations.

If a conflict exists, the repository-local canonical file remains authoritative for its own domain unless an explicit cross-repository governance update is registered.

---

## Import Boundary

Imported material from connected repositories is treated as referenced input.

Imported material is not automatically canonical inside Integrity Nexus unless it is:

1. explicitly listed in an import manifest,
2. tied to a source repository and path,
3. assigned an import status,
4. and reviewed against claim-boundary rules.

---

## Export Boundary

Exports from Integrity Nexus are governance or architecture exports.

Exports must not be presented as scientific derivations unless the source repository provides the relevant derivation status.

---

## Interface Rule

```text
Repository interface mapping is not theory creation.
Cross-repository consistency is not proof.
Claim-boundary control is not claim promotion.
```

---

## Audit Status

Status:

```text
STRUCTURAL INTERFACE FILE — ACTIVE
```
