# LM Export Manifest

## Purpose

This manifest defines readiness criteria for language-model-facing exports of Integrity Nexus material.

It is a governance file.
It does not create theory, validate derivations, or promote claims.

---

## LM Export Readiness Criteria

An LM export is ready only if it preserves:

- repository source identity,
- object ownership,
- canonical versus non-canonical status,
- candidate versus reviewed status,
- limitations,
- unresolved gates,
- and claim-boundary constraints.

---

## Required LM Export Fields

Each LM export should specify:

- LM_EXPORT_ID
- EXPORT_SCOPE
- SOURCE_REPOSITORIES
- SOURCE_PATHS
- SOURCE_COMMITS_OR_VERSIONS
- INCLUDED_LIMITATIONS
- INCLUDED_OPEN_GATES
- CLAIM_BOUNDARY_LEVEL
- REVIEW_STATUS

---

## Disallowed LM Export Behavior

LM exports must not:

- remove limitations,
- present candidates as completed derivations,
- present working assumptions as proofs,
- merge repository ownership boundaries,
- or treat summaries as source-of-truth files.

---

## Initial Registry

No LM exports are registered in this manifest at creation time.
