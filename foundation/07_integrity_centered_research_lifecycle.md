# Research Mechanism Architecture

## Integrity-Centered Research Lifecycle v0.1

**Status:** Working meta-architecture reference  
**Repository authority:** Integrity Nexus  
**Author:** Kai Stefan Dietrich  
**Date:** 2026-08-06

---

## 1. Purpose

This document defines the relationship between the principal mechanisms currently used across the TIG-E research ecosystem.

It is a meta-architecture document.

It does not replace the detailed source documents for:

- search-space compression;
- intuition;
- emergence;
- crystallization;
- validation and audit;
- canonical documentation.

Its function is to show how these mechanisms form one governed research lifecycle.

The lifecycle is domain-neutral at the architectural level. Domain-specific evidence standards, mathematical objects, ontologies, and validation procedures remain the responsibility of the applicable Domain Pack and research repository.

---

## 2. Core Research Mechanism

The principal lifecycle is:

```text
State Reconstruction
        ↓
Problem Analysis
        ↓
Target Analysis
        ↓
Bottleneck and Constraint Extraction
        ↓
Search-Space Compression
        ↓
Intuitive Candidate Formation
        ↓
Open Structural Hypothesis
        ↓
Evidence Search and Formal Reconstruction
        ↓
Constraint and Dependency Testing
        ↓
Emergence Candidate
        ↓
Crystallization
        ↓
Validation and Audit
        ↓
Canonical Documentation
        ↓
Repository Preservation and Reuse
```

This sequence is a governed research architecture.

It is not a claim that every discovery follows one psychologically or physically identical process.

---

## 3. Stage 0 — State Reconstruction

### Function

Reconstruct the current system state before proposing changes or new research objects.

### Required questions

- Which repositories, documents, registries, and prior decisions already exist?
- Which source is authoritative for each object?
- Which work has already been completed?
- Which conflicts, gaps, duplicates, and unresolved dependencies are present?
- What is observation, candidate, validated result, canon, or historical record?

### Output

A sufficiently explicit current-state model.

### Governing rule

> No new object should be created merely because an existing object has not yet been rediscovered.

State reconstruction protects the lifecycle against duplicate work, false novelty, and accidental authority conflicts.

---

## 4. Stage 1 — Problem Analysis

### Function

Define the actual problem rather than beginning from an assumed solution.

### Required questions

- What exactly is failing, missing, inconsistent, unknown, or underdetermined?
- What is inside and outside the active scope?
- Which terms require definition?
- Which levels, domains, or object classes must remain separate?
- Which apparent problem may only be a symptom of another bottleneck?

### Output

A bounded problem statement with explicit scope and unresolved components.

---

## 5. Stage 2 — Target Analysis

### Function

Define what would count as useful progress or successful resolution.

### Required questions

- What target state is sought?
- Which success criteria apply?
- Which non-goals and forbidden shortcuts apply?
- Which evidence or validation would be required?
- Which uncertainty may remain open?

### Output

A target description, success criteria, non-goals, and admissible stopping conditions.

### Governing rule

A target is not a preferred answer. It is a controlled description of the result conditions.

---

## 6. Stage 3 — Bottleneck and Constraint Extraction

### Function

Identify the dominant dependency and the conditions that bound admissible work.

### Bottleneck analysis

The bottleneck is the unresolved object, dependency, ambiguity, or contradiction whose resolution would most strongly change the effective problem space.

### Constraint extraction

Constraints may include:

- definitions;
- invariants;
- dependency order;
- repository authority;
- mathematical consistency;
- empirical requirements;
- claim boundaries;
- status rules;
- non-circularity requirements;
- resource or implementation limits.

### Output

A bottleneck statement and an explicit constraint set.

### Intuition sensor note

Intuition may act at this early stage as a weak sensor for a possible bottleneck, contradiction, or neglected relation.

Such a signal has low authority. It must be preserved as an observation and reconstructed before it changes the governed research state.

---

## 7. Stage 4 — Search-Space Compression

### Function

Reduce an initially unbounded or weakly structured problem space into a smaller, governed, auditable set of candidate paths.

Compression may use:

- candidate classification;
- dependency mapping;
- generator/projection separation;
- level control;
- contradiction detection;
- circularity checks;
- evidence thresholds;
- scope control;
- rejection and parking decisions.

### Output

A structured residual search space with visible dependencies, exclusions, candidate classes, and review requirements.

### Governing rule

> Compression removes or marks inadmissible routes without silently selecting a final answer.

Canonical source inside Integrity Nexus:

```text
foundation/03_search_space_compression.md
```

---

## 8. Stage 5 — Intuitive Candidate Formation

### Function

Identify a potentially relevant relation, bottleneck, constraint, or higher-order integration before complete formal reconstruction is available.

High-value intuitive synthesis occurs after initial search-space compression, when the remaining candidate space is constrained enough for implicit pattern recognition to become methodically useful.

### Two roles

```text
Intuition as Sensor
→ early low-authority orientation

Intuition as Synthesis
→ candidate formation inside a compressed search space
```

### Output

An Intuition Event or a candidate relation requiring reconstruction.

### Governing rule

> Intuition may prioritize where rigorous work begins. It may not determine where rigorous work ends.

Detailed source authority in the TIG-E repository:

```text
docs/research/intuition/
TIG-E_Intuition_Operationalization_Framework_v0.1.md
```

---

## 9. Stage 6 — Open Structural Hypothesis

### Function

Convert a surviving intuitive signal or structural observation into an explicit, auditable research object.

An Open Structural Hypothesis preserves a potentially important relation without treating it as:

- evidence;
- derivation;
- validation;
- proof;
- an established result;
- or a canonical claim.

### Output

A named structural hypothesis with:

- scope;
- originating observation;
- relevant dependencies;
- current constraints;
- expected explanatory or compression value;
- possible counterevidence;
- next tests.

---

## 10. Stage 7 — Evidence Search and Formal Reconstruction

### Function

Make the implicit candidate explicit and seek independent material capable of supporting, constraining, differentiating, or falsifying it.

### Evidence Search

Evidence Search identifies:

- canonical sources;
- independent observations;
- relevant literature;
- mathematical constraints;
- prior counterexamples;
- competing hypotheses;
- empirical or computational tests.

### Formal Reconstruction

Formal reconstruction translates the candidate into an explicit:

- proposition;
- relation;
- model;
- dependency structure;
- algorithm;
- mathematical object;
- or testable work hypothesis.

### Output

A reviewable candidate no longer dependent solely on the subjective force of its originating intuition.

---

## 11. Stage 8 — Constraint and Dependency Testing

### Function

Test whether the reconstructed candidate remains admissible under known formal, semantic, empirical, repository, and domain-specific constraints.

### Required outcomes

```text
RETAIN
REVISE
REJECT
PARK
SPLIT
ESCALATE
```

### Output

A classified candidate and an explicit test record.

A candidate that fails this stage does not proceed by rhetorical reformulation or silent status promotion.

---

## 12. Stage 9 — Emergence Candidate

### Function

Identify the appearance of a previously undocumented higher-order structure from an already organized, constrained, and internally related system.

An emergence candidate may integrate multiple surviving elements and reveal a structure that was not explicitly designed as an independent object.

### Required boundary

Emergence is not:

- proof;
- automatic truth;
- unexplained novelty;
- intuition itself;
- uncontrolled invention;
- or canonical status.

### Output

A reviewable emergent structure candidate.

Canonical and supporting sources:

```text
Integrity Nexus:
foundation/04_emergence_protocol.md

TIG-E repository:
docs/research/EMERGENCE_ARCHITECTURE.md
docs/research/TIG-E_Emergence_Operationalization_Framework_v0.1.md
docs/research/Working_Paper_0_Methodological_Foundations_EN.md
```

---

## 13. Stage 10 — Crystallization

### Function

Determine whether an emergent or otherwise developed structure remains stable under continued constraint pressure, reconstruction, comparison, and review.

The lifecycle distinguishes three uses of crystallization:

1. **Conceptual crystallization** — stabilization and persistence of an emergent structure;
2. **Governance crystallization** — controlled preservation of an audited research state;
3. **Applied crystallization** — a concrete scope-specific checkpoint.

### Output

A stable, explicitly bounded structure or checkpoint suitable for validation and controlled preservation.

### Governing boundaries

- Emergence creates or reveals a candidate structure.
- Crystallization tests and records persistence.
- Crystallization does not itself prove physical truth.
- Open and unresolved states may be crystallized if their boundaries are preserved accurately.

Detailed authority map in the TIG-E repository:

```text
docs/research/crystallization/README.md
```

Normative crystallization process:

```text
docs/governance/CRYSTALLIZATION_PROTOCOL.md
```

---

## 14. Stage 11 — Validation and Audit

### Function

Evaluate the crystallized structure against the evidence, derivation, dependency, consistency, reproducibility, domain, and governance standards required for its claimed status.

Validation and audit must distinguish:

- formal validity;
- semantic consistency;
- mathematical correctness;
- empirical support;
- domain compatibility;
- repository authority;
- claim status;
- unresolved dependencies.

### Output

A traceable verdict, correction requirement, status decision, or open-question record.

### Governing rule

> Compatibility is not derivation. Formal admissibility is not physical validation. Audit passage is not proof unless proof is the specific audited object and all proof obligations are satisfied.

---

## 15. Stage 12 — Canonical Documentation

### Function

Translate the validated or accurately bounded research state into a stable repository artifact.

Canonical documentation must preserve:

- what has been established;
- how it was established;
- what remains assumed;
- what remains open;
- which dependencies remain unresolved;
- which claims are expressly not made;
- which source has authority;
- which future work is permitted.

### Output

A governed repository artifact with explicit status, scope, dependencies, authority, and traceability.

### Governing rule

> History records the path. Canon records the currently authorized state.

---

## 16. Stage 13 — Repository Preservation and Reuse

### Function

Preserve the canonical artifact as institutional memory and make it reusable without detaching it from its status and evidence boundaries.

```text
Validated or Bounded Structure
        ↓
Canonical Documentation
        ↓
Repository Preservation
        ↓
Reusable Asset
        ↓
Institutional Memory
```

Repository preservation is not merely storage. It externalizes the governed research state so that future work does not depend exclusively on individual memory or access to the original conversation.

---

## 17. Non-Linearity and Feedback Loops

The lifecycle is ordered but not strictly one-directional.

Permitted feedback loops include:

```text
Evidence Search
→ revised Problem Analysis

Constraint Testing
→ additional Search-Space Compression

Audit
→ revised Formal Reconstruction

Crystallization
→ newly visible Constraints

Canonical Documentation
→ new Open Questions
```

Feedback must be explicit and traceable. A loop may revise an earlier stage but may not silently bypass a later gate.

---

## 18. Object and Status Separation

The lifecycle distinguishes process stage from epistemic status.

Examples:

```text
Intuition Event
= process object
≠ evidence

Open Structural Hypothesis
= governed research object
≠ established hypothesis confirmation

Emergence Candidate
= higher-order candidate structure
≠ validated result

Crystallized Checkpoint
= stabilized research state
≠ proof or physical truth

Canonical Documentation
= authorized repository representation
≠ guarantee that every contained open question is solved
```

---

## 19. Cross-Repository Authority Model

Integrity Nexus owns the meta-level lifecycle and relationship architecture.

It does not replace local authority for detailed mechanisms or domain content.

```text
Integrity Nexus
→ lifecycle map, cross-repository relationships, shared governance boundaries

TIG-E
→ detailed method operationalization, Runtime design, event schemas, Domain Packs

Scientific repositories
→ domain objects, mathematics, evidence, derivations, experiments, validation
```

A meta-level reference may point to a local source. It may not silently rewrite the local source or promote its status.

---

## 20. Relationship to the Discovery Engine Architecture

The existing Discovery Engine Architecture describes the structural system components through which governed discovery work is processed:

```text
Free Input
→ Structuring
→ Filters
→ Registry
→ Compression
→ Emergence
→ Review
→ Repository Integration
```

This document complements that component architecture by defining the **research-state lifecycle** and the roles of intuition, Open Structural Hypotheses, Evidence Search, crystallization, validation, and canonicalization.

Therefore:

```text
Discovery Engine Architecture
= system-component view

Integrity-Centered Research Lifecycle
= research-process and state-transition view
```

Neither document replaces the other.

Canonical component source:

```text
foundation/06_discovery_engine_architecture.md
```

---

## 21. Runtime Translation

The lifecycle provides the future Runtime with candidate governed objects and transitions.

Possible machine-readable objects include:

- State Reconstruction Record;
- Problem Definition;
- Target Definition;
- Bottleneck Record;
- Constraint Set;
- Compression Record;
- Intuition Event;
- Open Structural Hypothesis;
- Evidence Search Record;
- Emergence Event;
- Crystallization Checkpoint;
- Validation Record;
- Audit Finding;
- Canonicalization Decision.

A future Runtime may support these transitions. It may not infer authority merely from sequence completion.

---

## 22. Current Scientific and Governance Status

- **Lifecycle architecture:** working meta-architecture;
- **Stage ordering:** current controlled model;
- **Intuition sensor/synthesis distinction:** working methodological candidate;
- **Open Structural Hypothesis:** working governed process object;
- **Emergence mechanism:** operationally described; general theory open;
- **Crystallization mechanism:** multiple meanings separated; universal theory open;
- **Cross-domain reproducibility:** unverified;
- **Formal mathematical model:** open;
- **Physical interpretation:** not claimed;
- **Open-question closure:** not authorized by this document.

---

## 23. Governing Statement

> Reconstruct the state, define the problem and target, expose the bottleneck and constraints, compress the search space, preserve intuition as a testable route signal, permit emergence only as a candidate, crystallize only what remains stable, validate explicitly, and canonize only the currently authorized state.
