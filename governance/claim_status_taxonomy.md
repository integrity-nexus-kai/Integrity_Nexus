# Claim Status Taxonomy

**Repository:** Integrity_Nexus  
**Scope:** Scientific-core TIG Research Ecosystem with controlled Cube-domain coverage  
**Status:** CANONICAL / LOCKED MODE / AUDIT-CORRECTED  
**Synchronization Base:** `shared/terminology_inventory.md` content SHA `61c983e7d40792d6d93b67f5e1b2351b1e098203`; `shared/terminology_drift_matrix.md` content SHA `349bf02c81ad471f16adf2518676673957036822`  
**Position in Control Chain:** terminology inventory → terminology drift matrix → this taxonomy → claim-boundary matrix → registries → repository-status index  
**Global Synchronization and Completion-Readiness Authority:** `registry/repository_status.md`  
**OQ Status Contribution:** READY FOR COMPLETION AUDIT  
**Related Open Questions:** OQ-030 / OQ-NEXUS-001; OQ-031 / OQ-NEXUS-002  
**Last Updated:** 2026-07-13

---

## 1. Purpose

This file defines the permitted vocabulary for claims, scientific questions and blockers, registered-question lifecycles, workflow states, control artifacts, definitions, bridges, progress, and completion readiness inside the scientific-core TIG Research Ecosystem.

It exists to prevent silent upgrades or axis collapses such as:

- Candidate becoming final,
- Selected becoming necessary or Derived,
- Compatible becoming Derived,
- Declared becoming established,
- Preliminary becoming Validated,
- Addressed becoming Resolved,
- Operationally Closed becoming Question State `CLOSED`,
- Registered becoming Question State `CLOSED`,
- `AUDIT PASSED` becoming automatic registry closure,
- `NOT APPLICABLE` becoming a Scientific Status value,
- applicability becoming status assignment,
- Scientific Status becoming Claim Status,
- Operational Status becoming Claim Status,
- Required Work becoming Claim Status,
- Object Type, Scope, Artifact Status, Maturity Status, or Definition State becoming Claim Status,
- descriptive phrases being inserted into Claim Status,
- effective becoming fundamental,
- mathematical becoming physical,
- canonical artifact becoming completed theory,
- Cube hypothesis becoming Cube ontology,
- QIC bridge work becoming completed quantum theory,
- and SSC application terminology becoming a scientific-core definition.

This file is a governance artifact.

It does not:

- solve scientific open questions,
- close registered questions,
- define new theory,
- create physical interpretation,
- establish ontology,
- define a common substrate,
- define `Rel_TIG`, `DefectSpace`, `B_TIG`, or `I_QIC`,
- establish QIC as identical to TIG,
- establish Cube theory,
- assign the global synchronization count,
- assign global Completion Readiness,
- use `NOT APPLICABLE` as a Scientific Status value,
- assign a noncanonical value to Claim Status,
- invent Claim Status where source evidence does not support one,
- or resolve OQ-030 or OQ-031 by file existence alone.

The sole authority for global current-HEAD synchronization and global Completion Readiness is:

```text
registry/repository_status.md
```

---

## 2. Universal Rule

A claim-bearing or question-bearing statement must carry the exact values applicable to each independent axis and must record applicability before assigning a Scientific Status.

The protected rule is:

> No status may be upgraded, replaced, or reassigned across axes by wording, repository location, scientific-domain placement, registry admission, canonical placement, maturity label, audit passage, relation name, applicability marker, descriptive metadata, or cross-repository transfer.

Claim Status may use only the canonical Claim Status values defined in this file.

Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State must remain on their own axes or control fields.

When source evidence does not support a canonical Claim Status, the Claim Status field remains unassigned.

A stronger status requires evidence appropriate to that exact upgrade.

Depending on the target status, this may require:

- an explicit definition,
- an independent derivation,
- a mathematical proof,
- a completed validation protocol,
- empirical evidence,
- a typed bridge,
- dependency closure,
- a passing completion audit,
- registry application of an accepted audit result,
- or explicit human scientific acceptance.

---

## 3. Canonical Axes and Control Fields

The following axes and control fields are distinct and must not be compressed into one generic `Status` field.

| Axis or Control Field | Question Answered | Canonical Values or Markers |
|---|---|---|
| Claim Status | What evidential strength or claim role does the statement have? | Working Assumption, Candidate, Declared, Partial, Compatible, Admissible, Selected, Derived, Proven, Validated, Physical Candidate, Empirically Supported, Fundamental Candidate |
| Scientific Status Applicability | Does the Scientific Status axis apply to this object or registered question? | APPLICABLE, NOT APPLICABLE |
| Scientific Status | Is the exact scientific question or scientific blocker open or resolved? | Scientifically Open, Resolved |
| Question State | Is the exact registered question formally open or closed under its governing registry rule? | OPEN, CLOSED |
| Registry Status | Has the object or question been admitted to a registry? | Registerable, Registered |
| Operational Status | What happened in the workflow? | Pending, Addressed, Blocked, Operationally Closed |
| Artifact Status | What is the repository acceptance status of the file or input? | Raw Note, Non-Canonical Input, Canonical Artifact |
| Maturity Status | How developed is the artifact, analysis, track, or repository? | Preliminary, M0–M5, explicitly mapped local L-levels |
| Definition State | Is the object explicitly defined? | Defined, Partially Defined, Declared but Not Fully Defined, Named but Undefined, Undefined |
| Bridge State | Is the cross-domain interface established? | Not Required, Required, Missing, Candidate Bridge, Partial Bridge, Established Within Scope |
| Progress Classification | How far has a governed question progressed without changing Question State? | PARTIALLY RESOLVED — CORRECTION REQUIRED, READY FOR COMPLETION AUDIT |
| Completion Readiness | Is the globally controlled artifact chain ready for or through completion audit? | NOT ESTABLISHED, READY FOR AUDIT, AUDIT PASSED |
| Required Work | What work remains without assigning lifecycle or evidential strength? | Definition, Derivation, Proof, Validation, Review, Bridge Construction, Empirical Test, Completion Audit, or another explicitly descriptive work item |
| Object Type | What kind of object is being described? | Explicit repository-supported type description; not a status value |
| Scope | Under what limits does the record apply? | Explicit local, model, domain, temporal, or evidential limitation; not a status value |
| Scientific Domain | In which scientific or governance domain does the claim operate? | Integrity_Nexus governance, TIG-E research architecture, TIG gravitational architecture, QIC quantum-bridge research, SIR mathematical recursion, Cube research, SSC deferred application projection |
| Repository Container | In which repository is the artifact stored? | Integrity_Nexus, TIG-E, Quantum_Integrity_Core, Structural_Integrity_Recursion, Structural_State_Controller |

`Scientific Status Applicability` is an applicability control field. It is not a Scientific Status value and does not itself assign any status.

`Required Work`, `Object Type`, and `Scope` are descriptive control fields. They are not Claim Status values.

### 3.1 Exact-Spelling and Axis Rule

```text
Partial != Partially Defined
Candidate != Candidate Bridge
Operationally Closed != Closed Operationally
Established Within Scope != Established
Preliminary != Validated
Scientific Status Applicability NOT APPLICABLE != Scientific Status value
Scientific Status Applicability APPLICABLE != Scientifically Open
Scientific Status Applicability APPLICABLE != Resolved
Question State OPEN != Scientific Status Scientifically Open
Question State CLOSED != Scientific Status Resolved
Registry Status Registered != Question State CLOSED
Completion Readiness AUDIT PASSED != Question State CLOSED
Progress Classification != Question State
Completion Readiness != Scientific Status
Claim Status != Scientific Status
Claim Status != Operational Status
Claim Status != Required Work
Claim Status != Object Type
Claim Status != Scope
Claim Status != Artifact Status
Claim Status != Maturity Status
Claim Status != Definition State
```

### 3.2 Applicability Rule

```text
Scientific Status Applicability: APPLICABLE
→ Scientific Status may be assigned as Scientifically Open or Resolved

Scientific Status Applicability: NOT APPLICABLE
→ no Scientific Status value is assigned
```

Rules:

- `NOT APPLICABLE` is not a Scientific Status value.
- Applicability does not determine whether an applicable scientific question is open or resolved.
- Missing or unknown scientific status is not the same as inapplicability.
- Governance-question lifecycle is controlled by Question State, not Scientific Status.

### 3.3 Claim-Status Assignment Rule

Canonical Claim Status values are exclusively:

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
```

Rules:

- Scientific Status values remain on Scientific Status.
- Workflow values remain on Operational Status.
- Work descriptions remain under Required Work.
- Repository acceptance remains under Artifact Status.
- Development level remains under Maturity Status.
- Object-definition completeness remains under Definition State.
- Object Type and Scope remain descriptive controls.
- A phrase containing a canonical word does not become a canonical Claim Status unless the exact value is assigned on that axis and supported by evidence.
- Unsupported Claim Status remains unassigned.

### 3.4 Multi-Axis Examples

A registered scientific question may simultaneously be:

```text
Question State: OPEN
Registry Status: Registered
Scientific Status Applicability: APPLICABLE
Scientific Status: Scientifically Open
Claim Status: Candidate
Operational Status: Blocked
Artifact Status: Canonical Artifact
Maturity Status: Preliminary
Definition State: Partially Defined
Bridge State: Missing
Required Work: Definition and Bridge Construction
Scope: Explicitly declared local scope
```

None of these values cancels, replaces, or upgrades another.

A registered governance question may instead be:

```text
Question State: OPEN
Registry Status: Registered
Scientific Status Applicability: NOT APPLICABLE
Scientific Status: no value assigned
Progress Classification: READY FOR COMPLETION AUDIT
Completion Readiness: controlled globally by registry/repository_status.md
```

A named scientific object may correctly have no assigned Claim Status:

```text
Object Type: Named scientific object
Scientific Status Applicability: APPLICABLE
Scientific Status: Scientifically Open
Operational Status: Blocked
Definition State: Undefined
Required Work: Definition
Claim Status: unassigned because no canonical value is supported
```

---

## 4. Scientific-Domain Model

Repository container and scientific domain must be recorded separately.

| Scientific Domain | Role | Default Boundary |
|---|---|---|
| Integrity_Nexus governance | Meta-governance, registry, dependency, maturity, terminology, and claim control | May define governance; may not define physics, mathematics, or ontology |
| TIG-E research architecture | Gates, candidate lifecycle, preservation, blocker, and research-process control | Operational and formal status do not imply scientific completion |
| TIG gravitational architecture | Gravitational and field-equation candidate structures associated with TIG | Scoped architecture is not complete covariant theory |
| QIC quantum-bridge research | QIC state, integrity, readout, measurement, and QM-bridge questions | QIC bridge work is not completed quantum theory |
| SIR mathematical recursion | Recursive, topological, manifold, spectral, and admissibility mathematics | Mathematical structure is not physical structure without bridge |
| Cube research | Cube foundations, state, scale, recursive constraints, and bridge questions | Cube corpus is not completed Cube ontology |
| SSC deferred application projection | Later application-domain projection into control architecture | May not define the scientific core at the present stage |

Mandatory non-identities include:

```text
Quantum_Integrity_Core repository != QIC scientific object
QIC != TIG
I_QIC != Iμν
Σ_QIC != TIG spacetime state
Cube state != Σ_QIC without bridge
SSC application projection != core scientific definition
```

---

## 5. Canonical Vocabulary by Axis

### 5.1 Claim Status

| Value | Meaning | Does Not Mean |
|---|---|---|
| Working Assumption | Temporarily used assumption under explicit scope | Proof, finality, unrestricted transfer |
| Candidate | Proposed object, relation, equation, representation, gate, or model | Final, established, selected by nature |
| Declared | Named or introduced claim-bearing structure without full derivation | Proven, Derived, Validated |
| Partial | Some components of a claim are supported while a declared remainder stays open | Complete; Partially Defined |
| Compatible | Does not violate a target structure under stated conditions | Derived, unique, necessary, physically selected |
| Admissible | Passes a stated gate, predicate, or constraint under declared scope | Truth beyond the gate |
| Selected | Chosen as a minimum, working option, or local implementation | Derived necessity, uniqueness, ontology |
| Derived | Obtained from stated premises through documented reasoning | Broader status than premises support |
| Proven | Mathematically or logically proven under explicit assumptions | Physical or empirical truth without bridge |
| Validated | Checked successfully against declared criteria or evidence class | Universal completion beyond validation scope |
| Physical Candidate | Candidate with an explicit physical interpretation path | Empirical confirmation or final ontology |
| Empirically Supported | Supported by observational or experimental evidence under a declared model | Unrestricted truth or final theory |
| Fundamental Candidate | Candidate for underlying structure or ontology | Fundamental structure or truth |

No other value is permitted on the Claim Status axis.

A missing Claim Status must remain unassigned rather than being filled with another axis value or descriptive phrase.

### 5.2 Scientific Status Applicability

| Marker | Meaning | Boundary |
|---|---|---|
| APPLICABLE | The Scientific Status axis applies to the exact object, scientific question, or scientific blocker | Does not assign Scientifically Open or Resolved |
| NOT APPLICABLE | The Scientific Status axis does not apply to the exact object or governance question | No Scientific Status value may be assigned |

### 5.3 Scientific Status

| Value | Meaning | Boundary |
|---|---|---|
| Scientifically Open | Further definition, derivation, proof, validation, empirical work, or scientific review is required | Does not imply failed terminology governance, Question State `OPEN`, or a Claim Status value by itself |
| Resolved | The exact scientific question or blocker is closed by explicit accepted scientific evidence | Does not close a governance question, dependency, neighboring question, or assign Claim Status automatically |

### 5.4 Question State

| Value | Meaning | Boundary |
|---|---|---|
| OPEN | The exact registered question has not been formally closed under its governing registry rule | May coexist with substantial progress, Operationally Closed work, or AUDIT PASSED pending registry application |
| CLOSED | The governing registry has applied an accepted closure result to the exact question | Does not mean scientific truth, Scientific Status Resolved, or closure of dependencies |

Mandatory closure sequence for governance questions:

```text
corrections completed
→ repository_status records READY FOR AUDIT
→ independent completion audit passes
→ repository_status records AUDIT PASSED
→ governing registry applies the accepted result
→ Question State becomes CLOSED
```

`AUDIT PASSED` is necessary but not sufficient for Question State `CLOSED`.

### 5.5 Registry Status

| Value | Meaning | Boundary |
|---|---|---|
| Registerable | Meets stated conditions for possible registry admission | Not yet Registered; not scientifically accepted; not CLOSED |
| Registered | Entered into a registry, backlog, queue, or index | Not true, scientifically resolved, or Question State CLOSED |

`OPEN` and `CLOSED` are not Registry Status values. They belong only to Question State.

### 5.6 Operational Status

| Value | Meaning | Boundary |
|---|---|---|
| Pending | Declared workflow work has not yet been processed | No scientific inference; not Claim Status |
| Addressed | Declared workflow item was processed within stated operational scope | Not Resolved, not CLOSED, and not Claim Status |
| Blocked | Work cannot proceed until named dependencies are satisfied | Does not establish impossibility, alter Question State, or assign Claim Status |
| Operationally Closed | Workflow or gate sequence is closed within declared process scope | Scientific dependencies and Question State remain separate; not Claim Status |

`Operational` is the axis name, not a status value.

### 5.7 Artifact Status

| Value | Meaning | Boundary |
|---|---|---|
| Raw Note | Unprocessed note, idea, or fragment | No canonical scientific claim |
| Non-Canonical Input | Preserved material not accepted as current canonical claim-bearing output | Must not be cited as current canonical result |
| Canonical Artifact | Repository-recognized file or governance object | Not automatically true, Proven, Validated, Resolved, completed theory, or Claim Status |

### 5.8 Maturity Status

| Value | Meaning | Boundary |
|---|---|---|
| Preliminary | Analysis, result, or artifact exists but remains incomplete, provisional, or not fully validated | Not Claim Status Validated and not a Claim Status value |
| M0–M5 | Repository or artifact maturity under `governance/maturity_model.md` | Maturity is not scientific truth or Claim Status |
| Explicit Local L-Level | Repository-local maturity label when explicitly defined and mapped | Local level must not be generalized without mapping |

### 5.9 Definition State

| Value | Meaning |
|---|---|
| Defined | Object has an explicit local definition and type under scope |
| Partially Defined | Some defining structure is explicit; essential elements remain open |
| Declared but Not Fully Defined | Object is introduced and partially described, but definition or typing is incomplete |
| Named but Undefined | Recognized object with no sufficient definition |
| Undefined | No accepted definition exists |

Claim Status `Declared` and Definition State `Declared but Not Fully Defined` remain distinct.

No Definition State value is a Claim Status value.

### 5.10 Bridge State

| Value | Meaning |
|---|---|
| Not Required | No cross-domain transfer is being claimed |
| Required | Transfer cannot be accepted without an explicit bridge |
| Missing | A required bridge is absent |
| Candidate Bridge | A proposed bridge structure exists but is not established |
| Partial Bridge | Some interface components exist; completion remains open |
| Established Within Scope | A typed and accepted interface exists under explicit limits |

```text
bridge name != bridge existence
Candidate != Candidate Bridge
Candidate Bridge != Established Within Scope
```

### 5.11 Progress Classification

| Value | Meaning | Boundary |
|---|---|---|
| PARTIALLY RESOLVED — CORRECTION REQUIRED | Material progress is repository-supported, but known consistency or synchronization corrections remain in the evaluated scope | Question State remains OPEN; global Completion Readiness cannot exceed NOT ESTABLISHED |
| READY FOR COMPLETION AUDIT | Required corrections are complete in the evaluated scope and the controlled chain may support completion audit once globally reconciled | Question State remains OPEN; does not itself assign global Completion Readiness |

A local artifact may contribute `READY FOR COMPLETION AUDIT` when no correction remains in that artifact. Only `registry/repository_status.md` may authoritatively assign the global Progress Classification and Completion Readiness after evaluating the complete chain.

Progress Classification is not Scientific Status, Question State, Claim Status, or Completion Readiness.

### 5.12 Completion Readiness

| Value | Meaning | Boundary |
|---|---|---|
| NOT ESTABLISHED | The globally controlled chain is not yet ready for completion audit | No closure inference |
| READY FOR AUDIT | Global current-HEAD synchronization and known-correction checks are complete; independent audit is the next step | Does not mean AUDIT PASSED or Question State CLOSED |
| AUDIT PASSED | Independent completion audit accepted the globally controlled state | Governing registry must still apply the result before Question State CLOSED |

Only `registry/repository_status.md` may authoritatively assign these global values.

---

## 6. Composite Status Phrases

Composite phrases are permitted only when every component can be decomposed into canonical axes and applicability controls.

A composite phrase must never be copied verbatim into Claim Status unless it is exactly one canonical Claim Status value.

### Scoped Canonical Field-Equation Architecture

```text
Artifact Status: Canonical Artifact
Claim Status: Physical Candidate or Declared, as locally evidenced
Scope: Explicitly scoped
Scientific Status Applicability: APPLICABLE
Scientific Status: Scientifically Open where dependencies remain
```

It does not mean complete theory.

### Selected Minimum Placeholder

```text
Claim Status: Selected
Definition State: Defined or Partially Defined, as locally evidenced
Scope: Minimum placeholder only
```

`Selected minimum placeholder` is not itself a Claim Status value.

### Preliminary Effective Stress Analysis

```text
Maturity Status: Preliminary
Object Context: Effective realization
Scientific Status Applicability: APPLICABLE
Scientific Status: Scientifically Open where interpretation remains unresolved
```

`Preliminary` is not Claim Status and the phrase does not mean independently Validated physical stress-energy.

### PARTIALLY RESOLVED — CORRECTION REQUIRED

```text
Axis: Progress Classification
Question State: unchanged
Scientific Status Applicability: unchanged
Scientific Status: unchanged where applicable
Claim Status: unchanged or unassigned according to evidence
Global Completion Readiness: NOT ESTABLISHED
```

### READY FOR COMPLETION AUDIT

```text
Axis: Progress Classification
Question State: OPEN
Scientific Status Applicability: unchanged
Scientific Status: unchanged where applicable
Claim Status: unchanged or unassigned according to evidence
Global Completion Readiness: assigned only by registry/repository_status.md
```

---

## 7. Status Upgrade and Transition Requirements

| From | To | Required Evidence or Action |
|---|---|---|
| Raw Note | Non-Canonical Input | Preservation decision and source context |
| Non-Canonical Input | Canonical Artifact | Explicit repository acceptance or canonical placement |
| Working Assumption | Candidate | Candidate definition and testable or auditable criteria |
| Candidate | Admissible | Named gate or predicate passed under declared scope |
| Candidate | Selected | Explicit local selection rule and scope |
| Candidate | Derived | Documented derivation from accepted premises |
| Declared | Derived | Independent derivation without circular premise |
| Compatible | Derived | Derivation showing that the target follows, not merely fits |
| Selected | Derived | Derivation showing necessity or origin |
| Preliminary | Validated | Completed validation against declared criteria; explicit cross-axis update, not a direct same-axis transition |
| Addressed | Resolved | Scientific closure evidence and Scientific Status Applicability `APPLICABLE`; operational processing alone is insufficient and no Claim Status follows automatically |
| Operationally Closed | Resolved | Exact scientific closure criteria and dependencies satisfied; Scientific Status Applicability must be `APPLICABLE`; no Claim Status follows automatically |
| Registerable | Registered | Registry admission under registry rules |
| Registered | Canonical Artifact | Separate artifact-acceptance action |
| Registered | Question State CLOSED | Forbidden direct transition; closure rule and accepted result required |
| Canonical Artifact | Proven | Explicit proof and explicit Claim Status assignment; artifact acceptance alone is insufficient |
| Validated | Resolved | Validation addresses the exact scientific question and dependencies; cross-axis update must be explicit |
| Mathematical Object | Physical Candidate | Explicit physical interpretation bridge and supported Claim Status assignment |
| Effective Description | Fundamental Candidate | Explicit argument beyond effective scope and supported Claim Status assignment |
| Physical Candidate | Empirically Supported | Observational or experimental evidence under a declared model |
| Required or Missing | Established Within Scope | Typed interface, assumptions, and validation of transfer |
| Named but Undefined | Defined | Explicit definition, type, scope, and non-circular dependencies; Definition State change does not itself assign Claim Status |
| Scientific Status Applicability NOT APPLICABLE | APPLICABLE | Explicit reclassification showing that the object is now an exact scientific question or blocker; no Scientific Status or Claim Status follows automatically |
| PARTIALLY RESOLVED — CORRECTION REQUIRED | READY FOR COMPLETION AUDIT | Required corrections complete in the evaluated scope |
| Completion Readiness READY FOR AUDIT | AUDIT PASSED | Independent completion audit passes |
| Completion Readiness AUDIT PASSED | Question State CLOSED | Governing registry explicitly applies the accepted audit result to the exact question |

---

## 8. Forbidden Status Collapses

```text
Candidate = Final
Selected = Derived
Compatible = Derived
Declared = Established
Partial = Complete
Partial = Partially Defined
Preliminary = Validated
Addressed = Resolved
Addressed = Question State CLOSED
Blocked = Question State OPEN
Operationally Closed = Resolved
Operationally Closed = Question State CLOSED
Registerable = Registered
Registered = true
Registered = Question State CLOSED
Canonical Artifact = Completed Theory
Effective = Fundamental
Mathematical = Physical
Local Validation = Global Validation
Foundational = Fundamental
Fundamental Candidate = Fundamental Structure
Audit Passage = Proof
Formal Readout = Physical Measurement
Shared Term = Identical Definition
Repository Container = Scientific Domain Identity
Cube Corpus = Completed Cube Theory
Cube Hypothesis = Cube Ontology
Planck Manifestation = Cube Identity
QIC Compatibility = QM Derivation
TIG Field-Equation Architecture = QIC Theory
SSC Application Projection = Core Scientific Definition
Scientifically Open = Failed Governance
Scientific Status NOT APPLICABLE
Scientific Status Applicability NOT APPLICABLE = Scientific Status value
Scientific Status Applicability APPLICABLE = Scientifically Open
Scientific Status Applicability APPLICABLE = Resolved
Question State OPEN = Scientific Status Scientifically Open
Question State CLOSED = Scientific Status Resolved
Question State CLOSED = scientific truth
Question State CLOSED = closure of dependencies
Completion Readiness AUDIT PASSED = automatic Question State CLOSED
Progress Classification = Question State
Claim Status Scientifically Open
Claim Status Resolved
Claim Status Pending
Claim Status Addressed
Claim Status Blocked
Claim Status Operationally Closed
Claim Status Definition
Claim Status Derivation
Claim Status Proof
Claim Status Validation
Claim Status Review
Claim Status Bridge Construction
Claim Status Empirical Test
Claim Status Completion Audit
Claim Status Canonical Artifact
Claim Status Preliminary
Claim Status Defined
Claim Status Partially Defined
Claim Status Declared but Not Fully Defined
Claim Status Named but Undefined
Claim Status Undefined
Claim Status formal gate
Claim Status minimum placeholder
Claim Status scoped condition
Claim Status candidate lifecycle
Claim Status evidence anchor
local synchronization statement = global synchronization authority
```

---

## 9. Required Claim and Question Header Template

New or materially revised claim-bearing or question-bearing documents should include:

```text
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
Repository:
Scientific Domain:
Object Type:
Scope:
Definition State:
Bridge State:
Required Work:
Dependencies:
Allowed Claims:
Non-Claims:
Evidence Required For Upgrade:
Closure Rule:
```

Applicability and Claim Status rules:

- When `Scientific Status Applicability: APPLICABLE`, assign `Scientifically Open` or `Resolved` where known.
- When `Scientific Status Applicability: NOT APPLICABLE`, leave Scientific Status unassigned and state explicitly that no value is assigned.
- Never write `Scientific Status: NOT APPLICABLE`.
- A missing or unknown applicable Scientific Status must not be disguised as inapplicability.
- Claim Status may use only one canonical Claim Status value supported by evidence.
- Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State must not be written as Claim Status.
- When no canonical Claim Status is supported, leave Claim Status unassigned and state that no value is assigned where ambiguity would otherwise arise.

For fields other than Scientific Status or Claim Status, a field-specific `NOT APPLICABLE` marker may be used only where the governing schema explicitly permits it and no canonical value is being replaced.

For cross-repository or cross-domain material, also include:

```text
Source Repository:
Target Repository:
Source Scientific Domain:
Target Scientific Domain:
Relation Class:
Relation Target:
Allowed Transfer:
Forbidden Transfer:
```

`Claim Type` and `Required Work` are descriptive metadata, not status axes.

Permitted `Required Work` examples include:

- Definition
- Derivation
- Proof
- Validation
- Review
- Bridge Construction
- Empirical Test
- Completion Audit

They must never be placed in a generic `Status` field or in Claim Status.

---

## 10. Scientific-Domain Status Controls

### 10.1 Integrity_Nexus Governance

Governance may define process, registry, dependencies, roles, status vocabulary, maturity vocabulary, review obligations, transfer rules, applicability, Question State, and closure rules.

It may not define physics, mathematical proof, scientific ontology, or empirical truth.

Governance questions normally use:

```text
Scientific Status Applicability: NOT APPLICABLE
Scientific Status: no value assigned
```

A governance question does not receive Claim Status merely because it has progress, registry, operational, or artifact metadata.

### 10.2 TIG-E Research Architecture

TIG-E may define gates, candidate lifecycle, registry admission, blocker states, audit procedures, preservation conditions, and operational workflow.

It may not convert gate passage into truth, compatibility into derivation, registration into physical selection, Operationally Closed into Question State CLOSED, or workflow descriptions into Claim Status.

### 10.3 TIG Gravitational Architecture

TIG physical-candidate claims require explicit model scope, mathematical structure, physical interpretation, declared dependencies, and validation path.

The current scoped architecture must not be promoted to complete covariant theory, completed dynamics, independent fundamental tensor theory, or empirical confirmation.

### 10.4 QIC Quantum-Bridge Research

```text
Σ_QIC:
  Claim Status: Selected
  Scope: minimum abstract placeholder only

I_QIC:
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Named but Undefined
  Required Work: Definition
  Claim Status: unassigned unless separately supported

Read_QIC:
  Scientific Status: Scientifically Open
  Operational Status: Blocked
  Definition State: Partially Defined
  Required Work: measurement-semantics definition

Pres_QM:
  Claim Status: Compatible
  Scope: structural compatibility condition
```

QIC may not inherit TIG status from repository proximity.

### 10.5 SIR Mathematical Recursion

SIR mathematical claims require explicit local definitions and proof conditions. They may not become physical claims without typed bridge, physical interpretation, and validation.

Descriptive phrases such as `exploratory mathematical structure` are not Claim Status values.

### 10.6 Cube Research

```text
Cube research corpus != completed Cube theory
Cube hypothesis != derived physical ontology
Working Cube scale != derived Cube scale
Planck-scale manifestation != Cube identity
Cube state != Σ_QIC without bridge
fractal research question != fractal law
Cube transience question != established Cube transience
```

Cube-local labels must be mapped onto canonical axes. `WORKING DERIVATION` does not mean Claim Status Derived unless the derivation is complete and auditable.

`Blocked`, `Scientifically Open`, `Recognized`, `not yet formalized`, and similar descriptions must remain on their proper axes or descriptive fields rather than Claim Status.

### 10.7 SSC Deferred Application Projection

SSC remains outside active scientific-core derivation scope. It may not define TIG, QIC, SIR, Cube structures, the common substrate, or upgrade core claims.

---

## 11. QIC/TIG Anti-Collapse Controls

| Repository / Object | Scientific Domain | Status Boundary |
|---|---|---|
| `Quantum_Integrity_Core` repository | Repository container | Contains TIG gravitational architecture; name does not establish QIC identity |
| `Iμν[g,r_c]` | TIG gravitational architecture | Claim Status Physical Candidate inside a scoped effective realization; independent foundation open |
| `I_QIC` | QIC quantum-bridge research | Named but Undefined object; Scientifically Open and Blocked; no Claim Status inferred from those values |
| `Σ_QIC` | QIC quantum-bridge research | Claim Status Selected; minimum abstract state-set scope |
| TIG field-equation architecture | TIG gravitational architecture | Physical Candidate under scope; not QIC theory |
| QIC bridge program | QIC quantum-bridge research | Scientifically Open; not completed QM and not a Claim Status assignment |

---

## 12. OQ-031 Governance Completion and Closure Criterion

OQ-031 does not require the common substrate, `Rel_TIG`, `DefectSpace`, `B_TIG`, `I_QIC`, Cube ontology, Cube-to-QIC bridge, or SSC projection to be scientifically solved.

Terminology-governance completion requires every unresolved object or bridge to remain:

- explicitly identified,
- assigned to the correct repository container and scientific domain,
- given exact applicability and applicable status-axis values,
- given a canonical Claim Status only when supported,
- left with Claim Status unassigned when no canonical value is supported,
- given exact Definition State and Bridge State,
- protected by Relation Class, Relation Target, Allowed Transfer, and Forbidden Transfer,
- and prevented from silent status or axis upgrade.

```text
scientifically open object != incomplete terminology governance
missing bridge != incomplete terminology governance when absence is correctly controlled
unassigned Claim Status != governance failure when no canonical value is supported
```

For OQ-030 and OQ-031:

```text
Scientific Status Applicability: NOT APPLICABLE
Scientific Status: no value assigned
```

OQ-031 closure additionally requires:

1. global Completion Readiness `AUDIT PASSED` in `registry/repository_status.md`;
2. an accepted audit result covering the controlled artifact set;
3. explicit registry application of that result;
4. Question State changed from `OPEN` to `CLOSED` in both local and master registries.

---

## 13. Review Checklist

Before accepting, transferring, or upgrading a claim or question, check:

- Is the exact axis or applicability control named?
- Is a generic `Status` field being used for mixed semantics?
- Is every assigned Claim Status one exact canonical Claim Status value?
- Is Scientific Status being written as Claim Status?
- Is Operational Status being written as Claim Status?
- Is Required Work being written as Claim Status?
- Is Object Type or Scope being written as Claim Status?
- Is Artifact Status, Maturity Status, or Definition State being written as Claim Status?
- Is an unsupported Claim Status being invented rather than left unassigned?
- Is Scientific Status Applicability explicit where ambiguity is possible?
- Is `NOT APPLICABLE` being used incorrectly as a Scientific Status value?
- Is a Scientific Status value assigned despite applicability being `NOT APPLICABLE`?
- Is Question State explicit for a registered question?
- Is `OPEN` being confused with Scientifically Open?
- Is `CLOSED` being confused with Resolved?
- Is Registered being confused with CLOSED?
- Is Blocked being confused with Question State or Claim Status?
- Is AUDIT PASSED being treated as automatic closure?
- Is Progress Classification being treated as Question State or Claim Status?
- Is Completion Readiness being assigned outside `registry/repository_status.md` as a global authority claim?
- Are `Partial` and `Partially Defined` separated?
- Are Candidate and Candidate Bridge separated?
- Is Preliminary used only as Maturity Status?
- Is selection being written as derivation?
- Is compatibility being written as derivation?
- Is operational closure being written as scientific or registry closure?
- Is a mathematical object being written as physical?
- Is an effective description being written as fundamental?
- Is a canonical artifact being treated as completed theory?
- Is an audit result being treated as proof?
- Is formal readout being treated as physical measurement?
- Is QIC being collapsed into TIG?
- Is Cube research being promoted to ontology?
- Is SSC application language entering the core prematurely?
- Is scientific openness being treated as governance failure?

---

## 14. Synchronization Result

This revision reconciles the taxonomy with:

- `shared/terminology_inventory.md` content SHA `61c983e7d40792d6d93b67f5e1b2351b1e098203`, and
- `shared/terminology_drift_matrix.md` content SHA `349bf02c81ad471f16adf2518676673957036822`.

It preserves and records:

1. local OQ status contribution `READY FOR COMPLETION AUDIT` because no taxonomy-local correction remains;
2. Claim Status limited to the thirteen canonical Claim Status values;
3. Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State prohibited as Claim Status assignments;
4. unsupported Claim Status required to remain unassigned;
5. Required Work, Object Type, and Scope as explicit separate control fields;
6. Scientific Status Applicability as a separate control field;
7. only `Scientifically Open` and `Resolved` as Scientific Status values;
8. prohibition of `Scientific Status: NOT APPLICABLE`;
9. no Scientific Status value when applicability is `NOT APPLICABLE`;
10. Question State as a separate canonical axis;
11. Registry admission, Operational Status, Progress Classification, and Completion Readiness as separate controls;
12. the explicit governance-question closure sequence;
13. generic mixed-semantics `Status` prohibition;
14. `registry/repository_status.md` as sole global synchronization and Completion Readiness authority;
15. no global synchronization count or authoritative globally pending-file list in this taxonomy;
16. all QIC/TIG, Cube, SIR, SSC, evidence, bridge, and status anti-collapse controls;
17. the substantive Claim-Status normalization as already adopted across the preceding downstream chain;
18. the current revision as a SHA reconciliation only, without reopening or reversing the adopted controls.

---

## 15. OQ-030 / OQ-031 Status Contribution

Current local contribution:

```text
Question State: OPEN
Registry Status: Registered
Scientific Status Applicability: NOT APPLICABLE
Progress Classification: READY FOR COMPLETION AUDIT
```

No Scientific Status value is assigned to OQ-030 or OQ-031 because the axis is not applicable to these governance questions.

This taxonomy is reconciled with the current inventory and drift-matrix SHAs.

It does not authoritatively assign global Completion Readiness and does not report a global synchronization count.

Those values are controlled only by:

```text
registry/repository_status.md
```

The earlier progress/applicability propagation and the substantive Claim-Status normalization were completed across the downstream control chain before this temporal-status correction.

This revision records that completed substantive propagation. Because the inventory, drift matrix, and taxonomy now have new content SHAs, the boundary matrix and registries must be reconciled to those SHAs in dependency order. That SHA reconciliation does not reopen or reverse the already adopted Claim-Status controls.

This statement is not a global synchronization report.

---

## 16. Maintenance Rule

Any document introducing or changing a claim-bearing or question-bearing artifact must use this taxonomy or explicitly justify an equivalent local mapping.

Any stronger status requires the evidence or registry action required for that exact transition.

Any new status phrase must be decomposable into the independent axes and control fields defined here.

Any change to the terminology inventory or drift matrix invalidates this taxonomy's local reconciliation until explicitly updated against the new content SHAs.

This taxonomy must never report the global current-HEAD synchronization count, assign global Completion Readiness, or supersede `registry/repository_status.md`.

No taxonomy update may create scientific evidence, definition, proof, validation, bridge, ontology, theory, audit passage, or question closure absent from the governing sources.
