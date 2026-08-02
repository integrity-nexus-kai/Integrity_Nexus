# Claim Boundary Standard

This document defines the claim-boundary standard for Integrity Nexus.

---

# Rule

A relationship between repositories must not be presented as a proof unless a repository-specific formal result supports that claim.

---

# Historical Statement Grades

The labels C0-C4 below are retained only as historical descriptive grades for statement strength. They are not Claim Status values and are not permitted Relation Class values.

Every current cross-repository record must instead assign exactly one Relation Class from `claim_status_taxonomy.md` and `cross_repository_claim_boundary_matrix.md`. No C0-C4 grade maps automatically to a Relation Class.

## C0 — Navigation Statement

A statement about where information is located.

## C1 — Conceptual Relationship

A structural analogy or shared vocabulary across repositories.

## C2 — Dependency Relationship

A documented dependency between repositories or concepts.

## C3 — Evidence-Supported Relationship

A relationship supported by registered evidence.

## C4 — Formal Relationship

A relationship supported by a formal result.

Historical C0-C4 records require case-specific reclassification. Until that review occurs, their Relation Class is:

```text
INSUFFICIENT REPOSITORY EVIDENCE
```

This prevents a descriptive grade from silently becoming identity, derivation, compatibility, or proof.

---

# Boundary Principle

Integrity Nexus may say:

```text
TIG and SSC share a structural pattern of admissible bounded transition.
```

Integrity Nexus may not say:

```text
TIG proves SSC.
```

unless such a proof is explicitly registered in the relevant repository.

---

# Purpose

This standard preserves credibility and prevents cross-domain claim inflation.
