# Claim Status Taxonomy

**Repository:** Integrity_Nexus  
**Scope:** Scientific-core TIG Research Ecosystem with controlled Cube-domain coverage  
**Status:** CANONICAL / LOCKED MODE / AUDIT-CORRECTED  
**Synchronization Base:** `shared/terminology_inventory.md` content SHA `c36eb5aa64cd947905f8b41b7cee867cd971c8a3`; `shared/terminology_drift_matrix.md` content SHA `5318c17681b70d34e6b25321331c1e53b0ec8dd5`  
**Position in Control Chain:** terminology inventory → terminology drift matrix → this taxonomy → claim-boundary matrix → registries → repository-status index  
**Global Synchronization and Completion-Readiness Authority:** `registry/repository_status.md`  
**OQ Status Contribution:** READY FOR COMPLETION AUDIT  
**Related Open Questions:** OQ-030 / OQ-NEXUS-001; OQ-031 / OQ-NEXUS-002  
**Last Updated:** 2026-07-13

---

## 1. Purpose and Authority Boundary

This file defines the canonical vocabulary for evidential claims, scientific questions and blockers, registered-question lifecycles, workflow states, definitions, bridges, maturity, progress, and completion readiness.

It prevents silent upgrades and cross-axis collapse.

It does not:

- solve scientific questions;
- define new physics or mathematics;
- create a bridge, ontology, proof, validation, or empirical result;
- close OQ-030 or OQ-031;
- assign a global synchronization count;
- assign global Completion Readiness;
- treat repository placement, canonicality, registration, maturity, or audit wording as scientific evidence;
- use `NOT APPLICABLE` as a Scientific Status value;
- or invent Claim Status where evidence does not support one.

The sole authority for global current-HEAD synchronization, global Progress Classification, and global Completion Readiness is:

```text
registry/repository_status.md
```

---

## 2. Universal Rule

> No value may be upgraded, replaced, inferred, or reassigned across axes by wording, repository location, scientific-domain placement, canonical placement, maturity, registry admission, operational processing, audit passage, relation name, applicability marker, descriptive metadata, or cross-repository transfer.

A stronger value requires evidence appropriate to that exact transition.

When no canonical Claim Status is directly supported, Claim Status remains unassigned.

A generic mixed-semantics field named `Status` is prohibited where the governing axis is unclear.

---

## 3. Canonical Axes and Control Fields

| Axis or Control Field | Canonical Values or Rule |
|---|---|
| Claim Status | Working Assumption; Candidate; Declared; Partial; Compatible; Admissible; Selected; Derived; Proven; Validated; Physical Candidate; Empirically Supported; Fundamental Candidate |
| Scientific Status Applicability | APPLICABLE; NOT APPLICABLE |
| Scientific Status | Scientifically Open; Resolved |
| Question State | OPEN; CLOSED |
| Registry Status | Registerable; Registered |
| Operational Status | Pending; Addressed; Blocked; Operationally Closed |
| Artifact Status | Raw Note; Non-Canonical Input; Canonical Artifact |
| Maturity Status | Preliminary; M0–M5; explicitly mapped local L-levels |
| Definition State | Defined; Partially Defined; Declared but Not Fully Defined; Named but Undefined; Undefined |
| Bridge State | Not Required; Required; Missing; Candidate Bridge; Partial Bridge; Established Within Scope |
| Progress Classification | PARTIALLY RESOLVED — CORRECTION REQUIRED; READY FOR COMPLETION AUDIT |
| Completion Readiness | NOT ESTABLISHED; READY FOR AUDIT; AUDIT PASSED |
| Required Work | Descriptive work metadata such as Definition, Derivation, Proof, Validation, Review, Bridge Construction, Empirical Test, Completion Audit |
| Object Type | Repository-supported type description; not a status value |
| Scope | Explicit local, model, domain, temporal, or evidential limitation; not a status value |
| Scientific Domain | Governance, process, TIG gravitational, QIC quantum-bridge, SIR mathematical, Cube, or SSC deferred application domain |
| Repository Container | Storage location; not scientific-object identity |
| Relation Class | One exact canonical relation class |
| Relation Target | Separate named related object where applicable |

`Required Work`, `Object Type`, and `Scope` are descriptive controls, not Claim Status values.

---

## 4. Claim Status

### 4.1 Exact Values

Claim Status may use only:

```text
Working Assumption
Candidate
Declared
Partial
Compatible
Admissible
Selected
Derived
Proven
Validated
Physical Candidate
Empirically Supported
Fundamental Candidate
```

No other value is permitted on the Claim Status axis.

### 4.2 Meanings and Boundaries

| Value | Meaning | Does Not Mean |
|---|---|---|
| Working Assumption | Temporarily used assumption under explicit scope | Proof, finality, unrestricted transfer |
| Candidate | Proposed object, relation, equation, representation, or model | Final, established, selected by nature |
| Declared | Introduced claim-bearing structure without full derivation | Derived, Proven, Validated |
| Partial | Some components supported while a declared remainder stays open | Complete; Partially Defined |
| Compatible | Does not violate a target structure under stated conditions | Derived, unique, necessary |
| Admissible | Passes a stated gate or predicate under scope | Truth beyond that gate |
| Selected | Chosen minimum or local working option | Derived necessity, uniqueness, ontology |
| Derived | Obtained from stated premises through documented reasoning | Broader claim than premises support |
| Proven | Mathematically or logically proven under assumptions | Physical or empirical truth without bridge |
| Validated | Successfully checked against declared criteria | Universal completion beyond scope |
| Physical Candidate | Candidate with an explicit physical-interpretation path | Empirical confirmation or final ontology |
| Empirically Supported | Supported by observational or experimental evidence under a declared model | Final unrestricted truth |
| Fundamental Candidate | Candidate for underlying structure or ontology | Established fundamental structure |

### 4.3 Values Forbidden as Claim Status

The following are not Claim Status values:

```text
Scientifically Open
Resolved
Pending
Addressed
Blocked
Operationally Closed
Definition
Derivation
Proof
Validation
Review
Bridge Construction
Empirical Test
Completion Audit
Canonical Artifact
Preliminary
Defined
Partially Defined
Declared but Not Fully Defined
Named but Undefined
Undefined
formal gate
minimum placeholder
scoped condition
candidate lifecycle
evidence anchor
Recognized
not yet formalized
WORKING DERIVATION
```

A descriptive phrase containing a canonical word is not automatically an exact Claim Status value.

Examples:

```text
selected minimum placeholder
→ Claim Status: Selected
→ Scope: minimum placeholder only

preliminary effective stress analysis
→ Maturity Status: Preliminary
→ Scope/Object Context: effective realization

Named but Undefined
→ Definition State only
```

---

## 5. Applicability and Scientific Status

### 5.1 Applicability

```text
Scientific Status Applicability: APPLICABLE
→ Scientific Status may be Scientifically Open or Resolved

Scientific Status Applicability: NOT APPLICABLE
→ no Scientific Status value is assigned
```

Rules:

- `NOT APPLICABLE` is not a Scientific Status value.
- Applicability does not itself assign `Scientifically Open` or `Resolved`.
- Missing or unknown applicable status is not the same as inapplicability.
- Governance-question lifecycle is controlled by Question State.

### 5.2 Scientific Status

| Value | Meaning | Boundary |
|---|---|---|
| Scientifically Open | Further scientific definition, derivation, proof, validation, empirical work, or review is required | Not Question State OPEN and not Claim Status |
| Resolved | The exact scientific question or blocker is closed by accepted scientific evidence | Does not automatically close a registered governance question or dependency |

For OQ-030 and OQ-031:

```text
Scientific Status Applicability: NOT APPLICABLE
Scientific Status: no value assigned
```

---

## 6. Question, Registry, Operational, Progress, and Completion Axes

### 6.1 Question State

| Value | Meaning |
|---|---|
| OPEN | The exact registered question has not been formally closed under its governing rule |
| CLOSED | The governing registry has explicitly applied an accepted closure result to the exact question |

### 6.2 Registry Status

| Value | Meaning |
|---|---|
| Registerable | Eligible for possible registry admission |
| Registered | Entered into a registry, backlog, queue, or index |

### 6.3 Operational Status

| Value | Meaning | Boundary |
|---|---|---|
| Pending | Declared workflow work has not been processed | No scientific inference |
| Addressed | Workflow item was processed within scope | Not Resolved, not CLOSED, not Claim Status |
| Blocked | Work cannot proceed until named dependencies are satisfied | Does not establish impossibility or Question State |
| Operationally Closed | Workflow sequence is closed within process scope | Scientific and registry closure remain separate |

### 6.4 Progress Classification

| Value | Meaning | Boundary |
|---|---|---|
| PARTIALLY RESOLVED — CORRECTION REQUIRED | Material progress exists, but known consistency or synchronization corrections remain in the evaluated scope | Question State remains OPEN; global Completion Readiness cannot exceed NOT ESTABLISHED |
| READY FOR COMPLETION AUDIT | Required corrections are complete in the evaluated scope | Question State remains OPEN; global readiness remains separately controlled |

A local artifact may contribute `READY FOR COMPLETION AUDIT` when no local correction remains.

### 6.5 Completion Readiness

| Value | Meaning | Boundary |
|---|---|---|
| NOT ESTABLISHED | The globally controlled chain is not ready for completion audit | No closure inference |
| READY FOR AUDIT | Global synchronization and known-correction checks are complete; independent audit is next | Not AUDIT PASSED and not CLOSED |
| AUDIT PASSED | Independent audit accepted the globally controlled state | Registry application is still required before CLOSED |

Only `registry/repository_status.md` may authoritatively assign global Completion Readiness.

### 6.6 Governance Closure Sequence

```text
corrections completed
→ repository_status records READY FOR AUDIT
→ independent completion audit passes
→ repository_status records AUDIT PASSED
→ accepted result is explicitly applied in local and master registries
→ Question State becomes CLOSED
```

`AUDIT PASSED` is necessary but not sufficient for Question State `CLOSED`.

---

## 7. Definition and Bridge States

### 7.1 Definition State

```text
Defined
Partially Defined
Declared but Not Fully Defined
Named but Undefined
Undefined
```

Mandatory distinctions:

```text
Partial != Partially Defined
Declared != Declared but Not Fully Defined
Claim Status != Definition State
```

### 7.2 Bridge State

```text
Not Required
Required
Missing
Candidate Bridge
Partial Bridge
Established Within Scope
```

Mandatory distinctions:

```text
bridge name != bridge existence
Candidate != Candidate Bridge
Candidate Bridge != Established Within Scope
bridge requirement != existing bridge
```

Scientifically unresolved definitions and Missing bridges are not governance failures when correctly typed, scoped, bounded, and protected from silent promotion.

---

## 8. Relation Classes

Permitted Relation Class values are exactly:

```text
EXPLICITLY IDENTICAL
EXPLICIT LOCAL PROJECTION
EXPLICITLY RELATED
ANALOGICAL ONLY
GOVERNANCE MAPPING ONLY
COMPATIBLE ONLY
UNDEFINED RELATION
EXPLICITLY NON-EQUIVALENT
INSUFFICIENT REPOSITORY EVIDENCE
```

Relation Target must be separate.

Correct:

```text
Relation Class: EXPLICITLY NON-EQUIVALENT
Relation Target: I_QIC
```

Incorrect:

```text
Relation Class: EXPLICITLY NON-EQUIVALENT to I_QIC
```

Semantic resemblance, notation similarity, repository proximity, or historical origin do not establish identity.

---

## 9. Mandatory Non-Identities

```text
repository container != scientific domain
repository placement != scientific object identity
canonical artifact != scientific truth
mature governance != completed theory
effective realization != fundamental structure
mathematical object != physical object
formal readout != physical measurement
compatibility != derivation
selected != derived necessity
preliminary != validated
registered != true
Registered != Question State CLOSED
Operationally Closed != Question State CLOSED
Question State OPEN != Scientific Status Scientifically Open
Question State CLOSED != Scientific Status Resolved
AUDIT PASSED != automatic Question State CLOSED
Progress Classification != Question State
Completion Readiness != Scientific Status
Missing bridge != failed governance
scientifically open object != incomplete terminology governance
unassigned Claim Status != governance failure
Quantum_Integrity_Core repository != QIC scientific object
QIC != TIG
I_QIC != Iμν
Σ_QIC != TIG spacetime state
Cube state != Σ_QIC without explicit bridge
SIR mathematical structure != physical structure without typed bridge
SSC application projection != scientific-core definition
```

---

## 10. Scientific-Domain Controls

| Scientific Domain | Allowed Role | Boundary |
|---|---|---|
| Integrity_Nexus governance | Status vocabulary, dependencies, registry, audit, transfer and closure rules | May not create scientific objects or evidence |
| TIG-E research architecture | Gates, candidate lifecycle, blockers, preservation and research process | Gate or operational state is not scientific completion |
| TIG gravitational architecture | Scoped gravitational and field-equation candidate structures | Current effective realization is not complete covariant theory |
| QIC quantum-bridge research | State, integrity, readout, measurement and QM-bridge research | Bridge work is not completed quantum theory |
| SIR mathematical recursion | Exploratory recursive, topological, manifold and spectral mathematics | Mathematical structure is not physical without bridge |
| Cube research | Cube foundations, state, scale, constraints and bridge questions | Corpus is not completed ontology |
| SSC deferred application projection | Later application-domain projection | May not define the active scientific core |

SSC scope phrase:

```text
DEFERRED APPLICATION-PROJECTION SCOPE
```

---

## 11. Required Object Controls

### 11.1 Foundational TIG Objects

```text
substrate:
  Scientific Status Applicability: APPLICABLE
  Scientific Status: Scientifically Open
  Definition State: Undefined
  Claim Status: unassigned unless separately supported

Rel_TIG:
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Undefined
  Required Work: Definition

DefectSpace:
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Undefined
  Required Work: Definition

B_TIG:
  Claim Status: Declared
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Declared but Not Fully Defined
  Required Work: non-circular derivation
  Dependency: independently defined Rel_TIG / DefectSpace

Iμν:
  Scientific Domain: TIG gravitational architecture
  Claim Status: Physical Candidate
  Scope: static spherical effective realization
  Relation Class: EXPLICITLY NON-EQUIVALENT
  Relation Target: I_QIC
```

### 11.2 QIC Objects

```text
I_QIC:
  Scientific Status Applicability: APPLICABLE
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Named but Undefined
  Required Work: Definition
  Claim Status: unassigned unless separately supported

Σ_QIC:
  Claim Status: Selected
  Scope: minimum abstract placeholder only
  Definition State: Partially Defined
  Non-Claims: not Hilbert space by default; not physical ontology; not TIG spacetime state; not Cube state

Read_QIC:
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Partially Defined
  Required Work: physical measurement-semantics definition
  Non-Claim: formal readout != physical measurement

Pres_QM:
  Claim Status: Compatible
  Scope: structural compatibility condition
  Non-Claims: not Schrödinger evolution; not unitarity; not Hamiltonian dynamics; not QM derivation

generator / Hamiltonian:
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Undefined
  Required Work: Definition and derivation
  Claim Status: unassigned unless separately supported
```

QIC may not inherit TIG status from repository proximity.

---

## 12. Cube, SIR, and SSC Controls

### 12.1 Cube

```text
Cube research corpus != completed Cube theory
Cube hypothesis / Working Assumption != derived physical ontology
Cube state != Σ_QIC without explicit bridge
Planck-scale manifestation != Cube = Planck length
working Cube scale != derived Cube scale
Cube density framework != physical stress-energy
fractal research question != fractal law
Cube transience question != established Cube transience
transient Cube state != transient Cube object
persistent higher-order pattern != persistent substrate unit
bridge requirement != existing bridge
```

Safe statement:

```text
Der Cube kann persistent sein, während sein Zustand transient ist.
```

`WORKING DERIVATION`, `Recognized`, `not yet formalized`, `Blocked`, and `Scientifically Open` must remain on their correct axes or descriptive fields.

### 12.2 SIR

SIR remains an exploratory mathematical domain.

A mathematical-to-physical transfer requires:

- a typed bridge;
- declared assumptions;
- physical interpretation;
- validation within scope.

SIR mathematics does not automatically become TIG physical admissibility, spacetime topology, physical manifold structure, physical spectrum, QIC generator, Cube law, physical proof, or empirical evidence.

### 12.3 SSC

SSC may not define or justify TIG, QIC, SIR, Cube, the common substrate, `Rel_TIG`, `DefectSpace`, `B_TIG`, `I_QIC`, gravitational objects, quantum objects, or scientific-core Claim Status.

---

## 13. Transition Requirements

| From | To | Required Evidence or Action |
|---|---|---|
| Working Assumption | Candidate | Candidate definition and auditable criteria |
| Candidate | Admissible | Named gate or predicate passed under scope |
| Candidate | Selected | Explicit local selection rule and scope |
| Candidate | Derived | Documented derivation from accepted premises |
| Declared | Derived | Independent non-circular derivation |
| Compatible | Derived | Derivation showing the target follows rather than merely fits |
| Selected | Derived | Derivation showing necessity or origin |
| Preliminary | Validated | Completed validation and explicit cross-axis update |
| Mathematical Object | Physical Candidate | Typed physical bridge and supported Claim Status assignment |
| Physical Candidate | Empirically Supported | Observational or experimental evidence under a declared model |
| Named but Undefined | Defined | Explicit type, definition, scope, and non-circular dependencies |
| Missing | Established Within Scope | Typed interface, assumptions, and validation |
| PARTIALLY RESOLVED — CORRECTION REQUIRED | READY FOR COMPLETION AUDIT | Required corrections complete in the evaluated scope |
| READY FOR AUDIT | AUDIT PASSED | Independent completion audit passes |
| AUDIT PASSED | Question State CLOSED | Governing registries explicitly apply the accepted result |

Forbidden direct transitions include:

```text
Registered → Question State CLOSED
Operationally Closed → Question State CLOSED
Addressed → Resolved
Canonical Artifact → Proven
```

---

## 14. Required Record Template

```text
Repository:
Scientific Domain:
Object Type:
Claim Status:
Scientific Status Applicability:
Scientific Status:
Question State:
Registry Status:
Operational Status:
Artifact Status:
Maturity Status:
Progress Classification:
Completion Readiness:
Scope:
Definition State:
Bridge State:
Required Work:
Dependencies:
Relation Class:
Relation Target:
Allowed Transfer:
Forbidden Transfer:
Evidence Required For Upgrade:
Closure Rule:
```

Rules:

- Use one exact supported Claim Status value or leave it unassigned.
- Never write `Scientific Status: NOT APPLICABLE`.
- When applicability is `NOT APPLICABLE`, state that no Scientific Status value is assigned.
- Keep Relation Class and Relation Target separate.
- Do not infer missing values from names, notation, paths, analogy, or proximity.

---

## 15. OQ-030 / OQ-031 Governance State

Required representation during audit preparation:

```text
Question State: OPEN
Registry Status: Registered
Scientific Status Applicability: NOT APPLICABLE
Scientific Status: no value assigned
Claim Status: no value assigned
Operational Status: Addressed
```

A local file may contribute:

```text
Progress Classification: READY FOR COMPLETION AUDIT
```

That local contribution does not assign global Completion Readiness.

---

## 16. Synchronization Result

This taxonomy is locally reconciled with:

```text
shared/terminology_inventory.md
c36eb5aa64cd947905f8b41b7cee867cd971c8a3

shared/terminology_drift_matrix.md
5318c17681b70d34e6b25321331c1e53b0ec8dd5
```

It preserves:

1. the thirteen-value Claim Status set;
2. unassigned Claim Status where evidence is absent;
3. separation of applicability, scientific, question, registry, operational, artifact, maturity, definition, bridge, progress, completion, and descriptive fields;
4. exact relation classes and separate Relation Targets;
5. the governance closure sequence;
6. TIG/QIC, Cube, SIR, and SSC anti-collapse controls;
7. the corrected distinction between existing Cube scale evidence and the absent Cube scale/Planck-manifestation consistency-audit output;
8. `registry/repository_status.md` as sole global authority.

The substantive status-axis and Claim-Status controls were historically adopted across the then-current downstream chain before the independent audits identified the later temporal, Read_QIC, and Cube evidence-path findings.

This revision records that historical substantive state and locally reconciles the taxonomy to the corrected inventory and drift matrix.

Whether later artifacts are currently reconciled or pending is not asserted by this taxonomy. The actual global state is controlled only by `registry/repository_status.md`.

This taxonomy reports no global synchronization count, no authoritative pending-artifact list, no global Completion Readiness, and no audit passage.

---

## 17. Local Status Contribution

```text
Question State: OPEN
Registry Status: Registered
Scientific Status Applicability: NOT APPLICABLE
Scientific Status: no value assigned
Claim Status: no value assigned
Operational Status: Addressed
Progress Classification: READY FOR COMPLETION AUDIT
```

This is a local contribution only.

---

## 18. Maintenance Rule

Any document introducing or changing a claim-bearing or question-bearing artifact must use this taxonomy or provide an explicit equivalent mapping.

Any stronger value requires the evidence or registry action required for that exact transition.

Any change to the terminology inventory or drift matrix invalidates this taxonomy’s local reconciliation until it is explicitly updated against the new content SHAs.

This taxonomy must never supersede `registry/repository_status.md` as the global synchronization or Completion Readiness authority.

No taxonomy update may create scientific evidence, definition, proof, validation, bridge, ontology, theory, audit passage, or question closure absent from governing sources.
