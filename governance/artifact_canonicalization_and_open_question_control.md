# Artifact Canonicalization and Open-Question Control

**Repository:** Integrity_Nexus  
**Control ID:** INX-CAN-OQ-001  
**Version:** v1.0  
**Date:** 2026-09-26  
**Artifact Status:** Canonical Artifact  
**Scientific Status Applicability:** NOT APPLICABLE  
**Scope:** Cross-repository governance control for Artifact Status `Canonical Artifact` and the effect of open scientific/research questions on canonicalization  
**Status Vocabulary Authority:** `governance/claim_status_taxonomy.md`  
**Global Synchronization Authority:** `registry/repository_status.md`

---

## 1. Purpose

This control defines when an artifact may be assigned Artifact Status `Canonical Artifact` while scientific, empirical, downstream, or research questions remain open.

It operationalizes the existing axis separation in `governance/claim_status_taxonomy.md`.

It does not create scientific evidence, close a question, resolve science, promote a Claim Status, or authorize public release.

---

## 2. Protected Non-Identities

```text
Artifact Status Canonical Artifact != scientific truth
Artifact Status Canonical Artifact != Claim Status Proven
Artifact Status Canonical Artifact != Claim Status Validated
Artifact Status Canonical Artifact != Scientific Status Resolved
Artifact Status Canonical Artifact != Question State CLOSED

Question State OPEN != Artifact Status Non-Canonical Input
Scientific Status Scientifically Open != Artifact Status Non-Canonical Input
open research question != automatic canonicalization blocker

question closure != artifact canonicalization
artifact canonicalization != question closure
```

A canonical artifact is the authoritative, identity-, version-, scope-, provenance-, and status-bound representation of what is currently asserted, not asserted, qualified, or left open within its declared object scope.

Canonicalization therefore does not require scientific completeness.

---

## 3. Canonicalization Impact Is Relation-Specific

An open question does not possess one global canonicality effect.

Its impact is assessed **per relation between the question and an affected artifact**.

Required control field:

```text
Canonicality Impact:
BLOCKING
NON_BLOCKING
NOT_APPLICABLE
UNASSESSED
```

Meanings:

### BLOCKING

The open question prevents canonicalization of the affected artifact because the unresolved matter leaves the artifact itself insufficiently determined, contradictory, non-auditable, or structurally incomplete in a load-bearing way.

Typical cases:

- object identity or owner remains ambiguous;
- scope is not determinable;
- a load-bearing definition is unresolved;
- a load-bearing type or relation is unresolved;
- a circular or contradictory derivation remains open;
- a required upstream dependency is missing or ambiguous;
- two incompatible authoritative formulations remain unreconciled;
- the artifact cannot state its own bounded content without deciding the question.

### NON_BLOCKING

The question remains scientifically relevant but does not prevent the affected artifact from being an authoritative bounded representation.

Typical cases:

- empirical validation remains open;
- broader generalization remains open;
- domain-specific operationalization is downstream;
- alternative model classes remain to be tested;
- replication remains open;
- additional predictions remain open;
- a downstream bridge or experiment remains open;
- a later stronger Claim Status remains open;
- the question lies outside the artifact's declared scope.

### NOT_APPLICABLE

The question does not affect canonicalization of that artifact.

### UNASSESSED

The relation has been registered but canonicality impact has not yet been classified.

`UNASSESSED` is a workflow state for the relation only. It is not a Question State, Scientific Status, Claim Status, or Artifact Status.

An artifact canonicalization gate may not complete while a linked question that is declared relevant to that artifact remains `UNASSESSED`.

---

## 4. Canonicalization Gate

An artifact may be assigned Artifact Status `Canonical Artifact` when all required controls for its declared scope are satisfied:

```text
object identity bound
owner / authority bound
version and provenance bound
scope bound
object/type discipline consistent
load-bearing logic internally consistent
required upstream dependencies sufficiently bound
claim/status axes correctly typed
open-question references registered
canonicality impact assessed for relevant question-artifact relations
Canonicality Impact BLOCKING count = 0
required audit / approval gate satisfied
```

The following are **not** required merely for canonicalization:

```text
all research questions CLOSED
all Scientific Status values Resolved
all claims Proven
all claims Validated
all downstream experiments completed
all possible generalizations completed
```

---

## 5. Question-State Rule

Question State remains controlled independently:

```text
OPEN
CLOSED
```

A question may remain `OPEN` while one or many related artifacts are `Canonical Artifact`.

A question becomes `CLOSED` only under its governing closure rule and registry action.

Canonicalization of an artifact must never silently close a question.

---

## 6. Required Question-to-Artifact Record

For every question-artifact relation used during canonicalization, record at least:

```text
Question ID
Affected Artifact ID
Relation Type
Canonicality Impact
Impact Reason
Load-Bearing Area, if any
Owner
Evidence / source pointer
Assessment version
```

One question may be:

```text
BLOCKING for Artifact A
NON_BLOCKING for Artifact B
NOT_APPLICABLE for Artifact C
```

This is valid and expected.

---

## 7. Scaling Rule

Open questions are registered once as question identities and referenced by affected artifacts.

```text
one question identity
→ many question-to-artifact relations
```

Do not duplicate the same semantic research question merely because it appears in multiple documents.

Documents should store question references, not independently owned duplicate question records, unless a governing native registry requires preservation of the source identity.

---

## 8. Downstream and Successor Rule

Canonical does not mean immutable forever.

A later result may require:

- a successor artifact;
- a narrowed scope;
- a stronger or weaker Claim Status;
- reopening or reclassification of an affected question;
- a new canonical version.

Historical canonical artifacts remain provenance records and are not retroactively rewritten as if the later knowledge had always existed.

---

## 9. Mandatory Cross-Axis Guardrails

```text
Canonicality Impact != Question State
Canonicality Impact != Scientific Status
Canonicality Impact != Claim Status
Canonicality Impact != Operational Status

BLOCKING != scientifically false
NON_BLOCKING != scientifically resolved
UNASSESSED != OPEN question
CLOSED question != automatic Canonical Artifact
```

---

## 10. Adoption Rule

Repositories importing this control must:

1. preserve the META-defined semantics;
2. use a relation-specific question-to-artifact impact record;
3. prevent open questions from becoming automatic canonicalization blockers;
4. prevent non-blocking classification from silently closing or resolving questions;
5. route duplicate semantic questions to one controlled question identity where the local/native authority permits.

This file is a governance control. It does not supersede scientific owners or question registries.
