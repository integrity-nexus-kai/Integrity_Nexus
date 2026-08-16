# Repository and Governance Specification v0.1

**Repository:** `Riemann_Integrity_Research`  
**Version:** v0.1  
**Date:** 2026-08-16  
**Status:** WORKING GOVERNANCE SPECIFICATION  
**Canonical status:** NOT ESTABLISHED

## 1. Governance objective

The repository must remain reconstructible after months of work and hundreds of sources. Every load-bearing scientific statement must retain provenance, statement type, claim status, scope, dependencies, and review history.

## 2. Separation of axes

The repository uses multiple independent axes. They must never be collapsed.

### 2.1 Statement Type — local mathematical typing

- `DEF` — definition
- `EXT-THEOREM` — theorem established in external literature
- `LEMMA` — internally proved lemma, within stated assumptions
- `CONJECTURE` — conjecture or candidate statement
- `NUM` — numerical/computational observation
- `HEURISTIC` — heuristic or analogy
- `OQ` — open question
- `REFUTED` — refuted statement or failed candidate
- `SOURCE-CLAIM` — statement merely reported by a source and not yet promoted

These are **not** Nexus Claim Status values.

### 2.2 Nexus-compatible Claim Status

Where a claim-bearing object needs a Nexus Claim Status, use only the applicable canonical vocabulary from Integrity Nexus and record the evidence for the assignment. No local Statement Type automatically maps to a Claim Status.

Examples:

- `EXT-THEOREM` does not become `Proven` merely because a source calls it a theorem; the theorem conditions and source status must be checked.
- `NUM` never becomes `Proven` from numerical extent alone.
- `CONJECTURE` may remain without a Claim Status until a specific claim-state decision is justified.

### 2.3 Other independent controls

At minimum, track where relevant:

- Artifact Status
- Scientific Status / applicability
- Definition State
- Operational Status
- Audit Verdict
- Question State
- Provenance State
- Knowledge Class A/B/C

## 3. Source intake protocol

Every new source receives a stable ID `SOURCE-INTAKE-NNNN` before substantive use.

Required fields:

- source ID;
- exact filename/title;
- source class;
- acquisition date;
- original location or bibliographic identifier when available;
- cryptographic hash for stored binary when available;
- storage path;
- parser/extraction status;
- source-claim summary;
- verification state;
- corrections or conflicts;
- downstream objects that use the source.

A source can be useful while remaining `NON-CANONICAL INPUT`.

## 4. Proof hygiene

Every original proof attempt must specify:

1. exact target proposition;
2. domain and notation;
3. premises and imported theorems;
4. dependency graph;
5. each nontrivial inference;
6. hidden regularity/convergence/interchange assumptions;
7. branch, analytic-continuation, and boundary conditions where relevant;
8. proof obligations not yet discharged;
9. known failure modes and counterexamples;
10. independent audit status.

A proof attempt cannot be called a proof while any load-bearing obligation remains open.

## 5. Computational hygiene

Each computational result must be reproducible from:

- code version/commit;
- environment manifest;
- input data and hash;
- precision settings;
- algorithm;
- termination/error criteria;
- output hash;
- interpretation boundary.

Computation can refute a universal claim by a valid counterexample, but finite verification cannot establish a universal statement about infinitely many cases.

## 6. Knowledge-class firewall

- **A — Classical mathematics** must be sourced and reconstructed independently of Nexus/TIG concepts.
- **B — External research programmes** must preserve the claims and limitations of their actual literature.
- **C — Nexus/TIG-origin hypotheses** must be labeled as internal research hypotheses unless and until a formal bridge is established.

No Class C language may be injected into Class A definitions or theorem statements without an explicit bridge object.

## 7. Change control

Never silently overwrite a historical claim or decision. Corrections create a new version or an explicit correction record. `CURRENT_STATE.md` is the navigation pointer; it is not a historical archive.

## 8. Phase gates

### Phase 0 — Domain Reconstruction
Goal: audited baseline of definitions, standard results, known equivalences, proof barriers, computational state, and research programmes.

### Phase 1 — Attack-Surface Mapping
Goal: compare proof strategies, dependencies, known obstructions, and candidate leverage points.

### Phase 2 — Controlled Hypothesis Formation
Goal: formulate new candidate structures with explicit proof obligations.

### Phase 3 — Proof Attempt Activation
Goal: permit work in `05_PROOF_ATTEMPTS/` only after Phase 0 and 1 controls are satisfied.

### Phase 4 — Independent Mathematical Audit
Goal: line-by-line checking, counterexample search, assumption audit, and source verification.

### Phase 5 — Result Stabilization / Publication Readiness
Activated only for bounded results that survive audit. RH proof status remains separate and requires its own exceptional standard of validation.

## 9. Standalone-repository activation gates

Before the staging image is promoted to an active standalone repository:

- repository must exist under exact name `Riemann_Integrity_Research`;
- ownership and author metadata must be confirmed;
- license decision must be explicit;
- Integrity Nexus project-card and repository-map integration must be added;
- source binary transfer must be verified by SHA-256;
- initialization files must be checked against the transfer manifest;
- no staging status may be silently promoted to canonical.