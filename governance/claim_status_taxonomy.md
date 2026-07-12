# Claim Status Taxonomy

**Repository:** Integrity_Nexus  
**Scope:** Scientific-core TIG Research Ecosystem with controlled Cube-domain coverage  
**Status:** CANONICAL / LOCKED MODE / AUDIT-CORRECTED  
**Synchronization Base:** `shared/terminology_inventory.md` content SHA `74364a3c4f3575363ce3305ea0d68203f1d0e75f`; `shared/terminology_drift_matrix.md` content SHA `77f7e0c37336a262f51c765ae0f3ab314ed3f203`  
**Position in Control Chain:** terminology inventory → terminology drift matrix → this taxonomy → claim-boundary matrix → registries → repository-status index  
**Global Synchronization Authority:** `registry/repository_status.md`  
**OQ Status Contribution:** PARTIALLY RESOLVED — CORRECTION REQUIRED  
**Related Open Questions:** OQ-030 / OQ-NEXUS-001; OQ-031 / OQ-NEXUS-002  
**Last Updated:** 2026-07-12

---

## 1. Purpose

This file defines the permitted status vocabulary for claims, scientific objects, registered questions, workflow states, and control artifacts inside the scientific-core TIG Research Ecosystem.

It exists to prevent silent upgrades such as:

- Candidate becoming final,
- Selected becoming necessary or Derived,
- Compatible becoming Derived,
- Declared becoming established,
- Preliminary becoming Validated,
- Addressed becoming Resolved,
- Operationally Closed becoming Question State `CLOSED`,
- Registered becoming Question State `CLOSED`,
- `AUDIT PASSED` becoming automatic registry closure,
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
- or resolve OQ-030 or OQ-031 by file existence alone.

The sole authority for global current-HEAD synchronization and global Completion Readiness is:

```text
registry/repository_status.md
```

---

## 2. Universal Rule

A claim-bearing or question-bearing statement must carry the exact values applicable to each independent axis.

The protected rule is:

> No status may be upgraded by wording, repository location, scientific-domain placement, registry admission, canonical placement, maturity label, audit passage, relation name, or cross-repository transfer.

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

## 3. Canonical Status Axes

The following axes are distinct and must not be compressed into one generic `Status` field.

| Axis | Question Answered | Canonical Values |
|---|---|---|
| Claim Status | What evidential strength or claim role does the statement have? | Working Assumption, Candidate, Declared, Partial, Compatible, Admissible, Selected, Derived, Proven, Validated, Physical Candidate, Empirically Supported, Fundamental Candidate |
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
| Scientific Domain | In which scientific or governance domain does the claim operate? | Integrity_Nexus governance, TIG-E research architecture, TIG gravitational architecture, QIC quantum-bridge research, SIR mathematical recursion, Cube research, SSC deferred application projection |
| Repository Container | In which repository is the artifact stored? | Integrity_Nexus, TIG-E, Quantum_Integrity_Core, Structural_Integrity_Recursion, Structural_State_Controller |

### 3.1 Exact-Spelling and Axis Rule

```text
Partial != Partially Defined
Candidate != Candidate Bridge
Operationally Closed != Closed Operationally
Established Within Scope != Established
Preliminary != Validated
Question State OPEN != Scientific Status Scientifically Open
Question State CLOSED != Scientific Status Resolved
Registry Status Registered != Question State CLOSED
Completion Readiness AUDIT PASSED != Question State CLOSED
Progress Classification != Question State
Completion Readiness != Scientific Status
```

### 3.2 Multi-Axis Example

A registered scientific question may simultaneously be:

```text
Question State: OPEN
Registry Status: Registered
Scientific Status: Scientifically Open
Claim Status: Candidate
Operational Status: Blocked
Artifact Status: Canonical Artifact
Maturity Status: Preliminary
Definition State: Partially Defined
Bridge State: Missing
```

None of these values cancels or upgrades another.

A registered governance question may instead be:

```text
Question State: OPEN
Registry Status: Registered
Scientific Status: NOT APPLICABLE
Progress Classification: READY FOR COMPLETION AUDIT
Completion Readiness: controlled globally by registry/repository_status.md
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

### 5.2 Scientific Status

| Value | Meaning | Boundary |
|---|---|---|
| Scientifically Open | Further definition, derivation, proof, validation, empirical work, or scientific review is required | Does not imply failed terminology governance or Question State `OPEN` by itself |
| Resolved | The exact scientific question or blocker is closed by explicit accepted scientific evidence | Does not close a governance question, dependency, or neighboring question automatically |

### 5.3 Question State

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

`AUDIT PASSED` is therefore necessary but not sufficient for Question State `CLOSED`.

### 5.4 Registry Status

| Value | Meaning | Boundary |
|---|---|---|
| Registerable | Meets stated conditions for possible registry admission | Not yet Registered; not scientifically accepted; not CLOSED |
| Registered | Entered into a registry, backlog, queue, or index | Not true, scientifically resolved, or Question State CLOSED |

`OPEN` and `CLOSED` are not Registry Status values. They belong only to Question State.

### 5.5 Operational Status

| Value | Meaning | Boundary |
|---|---|---|
| Pending | Declared workflow work has not yet been processed | No scientific inference |
| Addressed | Declared workflow item was processed within stated operational scope | Not Resolved and not CLOSED |
| Blocked | Work cannot proceed until named dependencies are satisfied | Does not establish impossibility or alter Question State |
| Operationally Closed | Workflow or gate sequence is closed within declared process scope | Scientific dependencies and Question State remain separate |

`Operational` is the axis name, not a status value.

### 5.6 Artifact Status

| Value | Meaning | Boundary |
|---|---|---|
| Raw Note | Unprocessed note, idea, or fragment | No canonical scientific claim |
| Non-Canonical Input | Preserved material not accepted as current canonical claim-bearing output | Must not be cited as current canonical result |
| Canonical Artifact | Repository-recognized file or governance object | Not automatically true, Proven, Validated, Resolved, or completed theory |

### 5.7 Maturity Status

| Value | Meaning | Boundary |
|---|---|---|
| Preliminary | Analysis, result, or artifact exists but remains incomplete, provisional, or not fully validated | Not Claim Status Validated |
| M0–M5 | Repository or artifact maturity under `governance/maturity_model.md` | Maturity is not scientific truth |
| Explicit Local L-Level | Repository-local maturity label when explicitly defined and mapped | Local level must not be generalized without mapping |

### 5.8 Definition State

| Value | Meaning |
|---|---|
| Defined | Object has an explicit local definition and type under scope |
| Partially Defined | Some defining structure is explicit; essential elements remain open |
| Declared but Not Fully Defined | Object is introduced and partially described, but definition or typing is incomplete |
| Named but Undefined | Recognized object with no sufficient definition |
| Undefined | No accepted definition exists |

Claim Status `Declared` and Definition State `Declared but Not Fully Defined` remain distinct.

### 5.9 Bridge State

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

### 5.10 Progress Classification

| Value | Meaning | Boundary |
|---|---|---|
| PARTIALLY RESOLVED — CORRECTION REQUIRED | Material progress is repository-supported, but known consistency or synchronization corrections remain | Question State remains OPEN; global Completion Readiness is NOT ESTABLISHED |
| READY FOR COMPLETION AUDIT | Required corrections are complete and only independent completion audit remains before possible closure | Question State remains OPEN; global authority must report READY FOR AUDIT |

Progress Classification is not Scientific Status, Question State, or Completion Readiness.

### 5.11 Completion Readiness

| Value | Meaning | Boundary |
|---|---|---|
| NOT ESTABLISHED | The globally controlled chain is not yet ready for completion audit | No closure inference |
| READY FOR AUDIT | Global current-HEAD synchronization and known-correction checks are complete; independent audit is the next step | Does not mean AUDIT PASSED or Question State CLOSED |
| AUDIT PASSED | Independent completion audit accepted the globally controlled state | Governing registry must still apply the result before Question State CLOSED |

Only `registry/repository_status.md` may authoritatively assign these global values.

---

## 6. Composite Status Phrases

Composite phrases are permitted only when every component can be decomposed into canonical axes.

### Scoped Canonical Field-Equation Architecture

```text
Artifact Status: Canonical Artifact
Claim Status: Physical Candidate or Declared, as locally evidenced
Scope: Explicitly scoped
Scientific Status: Scientifically Open where dependencies remain
```

It does not mean complete theory.

### Selected Minimum Placeholder

```text
Claim Status: Selected
Definition State: Defined or Partially Defined, as locally evidenced
Scope: Minimum placeholder only
```

It does not mean uniquely Derived or final ontology.

### Preliminary Effective Stress Analysis

```text
Maturity Status: Preliminary
Object Context: Effective realization
Scientific Status: Scientifically Open where interpretation remains unresolved
```

It does not mean independently Validated physical stress-energy.

### PARTIALLY RESOLVED — CORRECTION REQUIRED

```text
Axis: Progress Classification
Question State: unchanged
Scientific Status: unchanged
Global Completion Readiness: NOT ESTABLISHED
```

### READY FOR COMPLETION AUDIT

```text
Axis: Progress Classification
Question State: OPEN
Global Completion Readiness: READY FOR AUDIT
Next Required Action: independent completion audit
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
| Preliminary | Validated | Completed validation against declared criteria; explicit cross-axis update |
| Addressed | Resolved | Scientific closure evidence; operational processing alone is insufficient |
| Operationally Closed | Resolved | Exact scientific closure criteria and dependencies satisfied |
| Registerable | Registered | Registry admission under registry rules |
| Registered | Canonical Artifact | Separate artifact-acceptance action |
| Registered | Question State CLOSED | Forbidden direct transition; closure rule and accepted result required |
| Canonical Artifact | Proven | Explicit proof |
| Validated | Resolved | Validation addresses the exact scientific question and dependencies |
| Mathematical Object | Physical Candidate | Explicit physical interpretation bridge |
| Effective Description | Fundamental Candidate | Explicit argument beyond effective scope |
| Physical Candidate | Empirically Supported | Observational or experimental evidence under a declared model |
| Required or Missing | Established Within Scope | Typed interface, assumptions, and validation of transfer |
| Named but Undefined | Defined | Explicit definition, type, scope, and non-circular dependencies |
| PARTIALLY RESOLVED — CORRECTION REQUIRED | READY FOR COMPLETION AUDIT | Required artifacts corrected; global authority reports READY FOR AUDIT |
| READY FOR AUDIT | AUDIT PASSED | Independent completion audit passes |
| AUDIT PASSED | Question State CLOSED | Governing registry explicitly applies the accepted audit result to the exact question |

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
Question State OPEN = Scientific Status Scientifically Open
Question State CLOSED = Scientific Status Resolved
Question State CLOSED = scientific truth
Question State CLOSED = closure of dependencies
Completion Readiness AUDIT PASSED = automatic Question State CLOSED
Progress Classification = Question State
local synchronization statement = global synchronization authority
```

---

## 9. Required Claim and Question Header Template

New or materially revised claim-bearing or question-bearing documents should include:

```text
Claim Status:
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
Scope:
Definition State:
Bridge State:
Dependencies:
Allowed Claims:
Non-Claims:
Evidence Required For Upgrade:
Closure Rule:
```

Fields that are not applicable must be marked `NOT APPLICABLE`, not omitted where omission could create ambiguity.

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

They must never be placed in a generic `Status` field.

---

## 10. Scientific-Domain Status Controls

### 10.1 Integrity_Nexus Governance

Governance may define process, registry, dependencies, roles, status vocabulary, maturity vocabulary, review obligations, transfer rules, Question State, and closure rules.

It may not define physics, mathematical proof, scientific ontology, or empirical truth.

### 10.2 TIG-E Research Architecture

TIG-E may define gates, candidate lifecycle, registry admission, blocker states, audit procedures, preservation conditions, and operational workflow.

It may not convert gate passage into truth, compatibility into derivation, registration into physical selection, or Operationally Closed into Question State CLOSED.

### 10.3 TIG Gravitational Architecture

TIG physical-candidate claims require explicit model scope, mathematical structure, physical interpretation, declared dependencies, and validation path.

The current scoped architecture must not be promoted to complete covariant theory, completed dynamics, independent fundamental tensor theory, or empirical confirmation.

### 10.4 QIC Quantum-Bridge Research

```text
Σ_QIC = selected minimum abstract placeholder only
I_QIC = Named but Undefined scientific object
Read_QIC = formal readout concept; physical measurement bridge open
Pres_QM = structural compatibility condition; not QM derivation
```

QIC may not inherit TIG status from repository proximity.

### 10.5 SIR Mathematical Recursion

SIR mathematical claims require explicit local definitions and proof conditions. They may not become physical claims without typed bridge, physical interpretation, and validation.

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

### 10.7 SSC Deferred Application Projection

SSC remains outside active scientific-core derivation scope. It may not define TIG, QIC, SIR, Cube structures, the common substrate, or upgrade core claims.

---

## 11. QIC/TIG Anti-Collapse Controls

| Repository / Object | Scientific Domain | Status Boundary |
|---|---|---|
| `Quantum_Integrity_Core` repository | Repository container | Contains TIG gravitational architecture; name does not establish QIC identity |
| `Iμν[g,r_c]` | TIG gravitational architecture | Scoped effective tensor realization; independent foundation open |
| `I_QIC` | QIC quantum-bridge research | Named but Undefined object |
| `Σ_QIC` | QIC quantum-bridge research | Selected minimum abstract state set |
| TIG field-equation architecture | TIG gravitational architecture | Physical Candidate under scope; not QIC theory |
| QIC bridge program | QIC quantum-bridge research | Scientifically Open; not completed QM |

---

## 12. OQ-031 Governance Completion and Closure Criterion

OQ-031 does not require the common substrate, `Rel_TIG`, `DefectSpace`, `B_TIG`, `I_QIC`, Cube ontology, Cube-to-QIC bridge, or SSC projection to be scientifically solved.

Terminology-governance completion requires every unresolved object or bridge to remain:

- explicitly identified,
- assigned to the correct repository container and scientific domain,
- given exact applicable status-axis values,
- given exact Definition State and Bridge State,
- protected by Relation Class, Relation Target, Allowed Transfer, and Forbidden Transfer,
- and prevented from silent status upgrade.

```text
scientifically open object != incomplete terminology governance
missing bridge != incomplete terminology governance when absence is correctly controlled
```

OQ-031 closure additionally requires:

1. global Completion Readiness `AUDIT PASSED` in `registry/repository_status.md`;
2. an accepted audit result covering the controlled artifact set;
3. explicit registry application of that result;
4. Question State changed from `OPEN` to `CLOSED` in both local and master registries.

Scientific Status remains `NOT APPLICABLE` for OQ-031 as a direct governance-question status.

---

## 13. Review Checklist

Before accepting, transferring, or upgrading a claim or question, check:

- Is the exact axis named?
- Is a generic `Status` field being used for mixed semantics?
- Is Question State explicit for a registered question?
- Is `OPEN` being confused with Scientifically Open?
- Is `CLOSED` being confused with Resolved?
- Is Registered being confused with CLOSED?
- Is Blocked being confused with Question State?
- Is AUDIT PASSED being treated as automatic closure?
- Is Progress Classification being treated as Question State?
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

- `shared/terminology_inventory.md` content SHA `74364a3c4f3575363ce3305ea0d68203f1d0e75f`, and
- `shared/terminology_drift_matrix.md` content SHA `77f7e0c37336a262f51c765ae0f3ab314ed3f203`.

It propagates the audit corrections by:

1. adding Question State as a separate canonical axis;
2. defining only `OPEN` and `CLOSED` on that axis;
3. removing `OPEN` from Registry Status semantics;
4. distinguishing Registry admission from question lifecycle;
5. defining the explicit governance-question closure sequence;
6. separating AUDIT PASSED from automatic closure;
7. prohibiting generic mixed-semantics `Status` fields;
8. classifying `Required Work` as metadata rather than status;
9. establishing `registry/repository_status.md` as sole global synchronization and Completion Readiness authority;
10. removing global synchronization counts and pending-file lists from this taxonomy;
11. preserving all existing QIC/TIG, Cube, SIR, SSC, evidence, and status anti-collapse controls.

---

## 15. OQ-030 / OQ-031 Status Contribution

Current local contribution:

```text
Question State: OPEN
Registry Status: Registered
Progress Classification: PARTIALLY RESOLVED — CORRECTION REQUIRED
```

This taxonomy is reconciled with the current inventory and drift-matrix SHAs.

It does not authoritatively assign global Completion Readiness and does not report a global synchronization count.

Those values are controlled only by:

```text
registry/repository_status.md
```

The boundary matrix and registries must adopt this taxonomy before the question entries may move to Progress Classification `READY FOR COMPLETION AUDIT`.

---

## 16. Maintenance Rule

Any document introducing or changing a claim-bearing or question-bearing artifact must use this taxonomy or explicitly justify an equivalent local mapping.

Any stronger status requires the evidence or registry action required for that exact transition.

Any new status phrase must be decomposable into the independent axes defined here.

Any change to the terminology inventory or drift matrix invalidates this taxonomy's local reconciliation until explicitly updated against the new content SHAs.

This taxonomy must never report the global current-HEAD synchronization count or supersede `registry/repository_status.md`.

No taxonomy update may create scientific evidence, definition, proof, validation, bridge, ontology, theory, audit passage, or question closure absent from the governing sources.
