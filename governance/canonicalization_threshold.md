# Canonicalization Threshold

## Research Object Readiness Gate

**Status:** Working governance specification  
**Repository authority:** Integrity Nexus  
**Author:** Kai Stefan Dietrich  
**Date:** 2026-08-06

---

## 1. Purpose

This document defines the readiness threshold that a research object must satisfy before it may be considered for canonical documentation within the Integrity Nexus research ecosystem.

It does not define scientific truth, proof, publication acceptance, or universal completion.

It governs whether the current state of a research object is sufficiently explicit, bounded, traceable, reviewed, reconstructable, and authorized to become the currently controlling repository representation.

---

## 2. Core Definition

> **The Canonicalization Threshold is the minimum combined epistemic, documentary, dependency, audit, placement, and authority readiness required before a research object may enter canonical memory.**

Crossing the threshold means:

```text
ready for canonicalization decision
```

It does not mean:

```text
proven
true
complete
published
universally valid
closed to revision
```

---

## 3. Required Distinctions

```text
Canonicalization Threshold ≠ Truth Threshold
Canonicalization Threshold ≠ Proof Threshold
Canonicalization Threshold ≠ Publication Threshold
Canonicalization Threshold ≠ Open-Question Closure
Canonicalization Threshold ≠ Scientific Completion
Canonicalization Threshold ≠ Governance Approval by itself
```

The threshold is a readiness gate. A separate governance decision authorizes or refuses canonicalization.

---

## 4. Canonicalization of Open States

A research object does not need to be scientifically complete to become canonical.

An open question, unresolved candidate, negative result, bounded construction, failed proof attempt, or current audit finding may be canonicalized when:

- its object identity is clear;
- its open or negative status is explicit;
- its support and limitations are accurate;
- its dependencies are visible;
- its non-claims are preserved;
- and it is the authorized current representation of that state.

```text
Canonical open status
≠ closed question
```

---

## 5. Mandatory Readiness Dimensions

### 5.1 Object Identity

The object must be uniquely named and distinguishable from adjacent objects, projections, prior versions, and similarly named concepts.

Required:

- canonical title or identifier;
- object class;
- repository and path;
- version or status marker;
- relation to superseded or competing objects.

### 5.2 Scope Boundary

The object must state:

- what it covers;
- what it does not cover;
- applicable domain;
- scale or level;
- intended use;
- and forbidden interpretations where material.

### 5.3 Provenance

The origin and development path must be reconstructable through:

- source documents;
- observations or data;
- prior decisions;
- relevant commits or records;
- originating candidate or hypothesis;
- and material transformations.

### 5.4 Epistemic Status

The object must distinguish, where applicable:

```text
Definition
Assumption
Observation
Candidate
Open Structural Hypothesis
Formal Construction
Derivation
Proof
Validation
Compatibility
Interpretation
Open Question
```

No document may rely on tone, placement, or filename alone to communicate epistemic status.

### 5.5 Support Record

The support must match the claimed status.

Examples:

- a definition requires explicit scope and consistency;
- a construction requires formal specification;
- a derivation requires traceable premises and steps;
- a proof requires discharged proof obligations;
- a validation claim requires defined criteria and results;
- an empirical claim requires evidence and method;
- an open question requires accurate unresolved status.

### 5.6 Dependency State

The object must list:

- satisfied dependencies;
- unresolved dependencies;
- external dependencies;
- circularity risks;
- and downstream objects affected by its status.

Unresolved dependencies may remain, but they may not be hidden.

### 5.7 Non-Claims

The object must explicitly exclude materially plausible but unsupported interpretations.

Non-claims are mandatory when readers could otherwise infer:

- scientific completion;
- physical interpretation;
- universal applicability;
- causal explanation;
- proof;
- ontology selection;
- or cross-domain identity.

### 5.8 Audit and Conflict State

Known contradictions, audit findings, reviewer objections, and status conflicts must be:

- resolved;
- corrected;
- rejected with reason;
- or explicitly retained as controlled open findings.

A known material conflict may not be silently omitted from the canonical representation.

### 5.9 Reconstructability

A qualified reviewer must be able to understand the object without access to the originating private memory, chat context, or undocumented oral explanation.

The object must contain or reference enough context to reconstruct:

- purpose;
- status;
- logic;
- evidence;
- dependencies;
- and current next actions.

### 5.10 Authority and Placement

The canonical repository, path, approving authority, and relationship to local or meta-level sources must be explicit.

```text
Correct content in the wrong authority location
≠ canonical readiness
```

### 5.11 Preservation Readiness

The object must be prepared for durable reuse through:

- stable naming;
- traceable links;
- version relation;
- readable format;
- status metadata;
- and protection against unmarked duplication or silent supersession.

---

## 6. Threshold Checklist

A candidate object may enter the canonicalization decision only when all mandatory questions can be answered:

```text
[ ] Is the object uniquely identified?
[ ] Is its scope explicit?
[ ] Is provenance reconstructable?
[ ] Is epistemic status explicit?
[ ] Does support match the claimed status?
[ ] Are dependencies visible?
[ ] Are material non-claims stated?
[ ] Are known conflicts controlled?
[ ] Can an independent reviewer reconstruct it?
[ ] Is authority and placement correct?
[ ] Is durable preservation prepared?
```

A missing mandatory item requires return, revision, or explicit exception authorization.

---

## 7. Readiness Outcomes

```text
THRESHOLD_MET
THRESHOLD_NOT_MET
THRESHOLD_MET_WITH_CONTROLLED_OPEN_ITEMS
REQUIRES_AUTHORITY_REVIEW
REQUIRES_DOMAIN_REVIEW
REQUIRES_RECONSTRUCTION
REQUIRES_AUDIT
```

These are readiness outcomes, not final canonicalization decisions.

---

## 8. Governance Decisions

After readiness assessment, authorized governance may decide:

```text
CANONICALIZE
CANONICALIZE_AS_OPEN_STATE
RETURN_FOR_RECONSTRUCTION
RETURN_FOR_VALIDATION
RETURN_FOR_AUDIT
REVISE_STATUS
RELOCATE
PARK
ARCHIVE
REJECT
```

The decision must state its rationale and affected dependencies.

---

## 9. Canonicalization Record

```yaml
canonicalization_record:
  record_id: CAN-YYYY-NNNN
  object_id: ""
  repository: ""
  path: ""
  version: ""
  object_class: ""
  epistemic_status: ""
  readiness_outcome: ""
  open_items: []
  dependencies: []
  non_claims: []
  audits_reviewed: []
  supersedes: []
  canonicalization_decision: ""
  approving_authority: ""
  decision_date: ""
  next_review_trigger: ""
```

This schema is an initial candidate and requires Runtime alignment.

---

## 10. Relationship to Crystallization

Crystallization and canonicalization are distinct.

```text
Crystallization
→ Is the structure stable enough to preserve as a bounded research state?

Canonicalization Threshold
→ Is that state documented and governed well enough to become the current authoritative representation?
```

A structure may be conceptually crystallized but fail the Canonicalization Threshold because provenance, status, dependency mapping, or placement is incomplete.

---

## 11. Relationship to Validation and Audit

Validation evaluates support for the scientific or formal claim.

Audit evaluates consistency, compliance, dependency state, and representation.

The Canonicalization Threshold integrates their relevant outputs but does not replace either.

```text
Validation result
+ Audit result
+ Documentary readiness
+ Authority readiness
→ Canonicalization readiness assessment
```

---

## 12. Relationship to Canonical Memory

Only an authorized object that has met the applicable threshold may enter Canonical Memory as the current controlling representation.

Controlled non-canonical memory may preserve objects that do not meet the threshold, provided their status is explicit.

```text
Preservation may precede canonicalization.
Canonical authority may not precede readiness and approval.
```

---

## 13. Failure Modes

Canonicalization fails when:

- a polished document hides unresolved scientific status;
- repository placement is mistaken for validation;
- an open question is silently presented as closed;
- formal notation creates an appearance of derivation;
- provenance is lost;
- conflicting files remain without authority mapping;
- known audit findings are omitted;
- non-claims are absent;
- the object depends on undocumented conversation context;
- or approval occurs without a traceable decision record.

---

## 14. Exception Handling

An exception may be authorized only when:

- the missing readiness item is explicitly identified;
- the reason for exception is documented;
- the risk is bounded;
- the object is clearly marked;
- and a correction or review trigger is registered.

An exception may not convert missing scientific support into a validated claim.

---

## 15. Current Status

- **Threshold model:** working governance specification;
- **Mandatory dimensions:** normative working requirements;
- **Checklist:** initial operational gate;
- **Machine-readable record:** candidate schema;
- **Cross-domain calibration:** open;
- **Automatic canonicalization:** prohibited;
- **Scientific truth authority:** not claimed.

---

## 16. Governing Statement

> Canonicalize neither the strongest-sounding formulation nor the newest document; canonicalize the most accurate, bounded, traceable, reviewed, reconstructable, and explicitly authorized representation of the current research state.
