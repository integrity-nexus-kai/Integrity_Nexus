# Claim Status Taxonomy

**Repository:** Integrity_Nexus  
**Scope:** Scientific-core TIG Research Ecosystem with controlled Cube-domain coverage  
**Status:** CANONICAL / LOCKED MODE  
**Synchronization Base:** `shared/terminology_inventory.md` content SHA `d835d2224113f8f09799db9ca97c8cc269d92cf8`; `shared/terminology_drift_matrix.md` content SHA `fc0b4c975960c30d6e8c68964ac6338510ae578d`  
**Position in Control Chain:** terminology inventory → terminology drift matrix → this taxonomy → claim-boundary matrix → registries → repository-status index  
**OQ Status Contribution:** PARTIALLY RESOLVED — CORRECTION REQUIRED  
**Related Open Questions:** OQ-030 / OQ-NEXUS-001; OQ-031 / OQ-NEXUS-002  
**Last Updated:** 2026-07-12

---

## 1. Purpose

This file defines the permitted status vocabulary for claims and control artifacts inside the scientific-core TIG Research Ecosystem.

It exists to prevent silent status upgrades such as:

- candidate becoming final,
- selected becoming necessary or derived,
- compatible becoming derived,
- declared becoming established,
- preliminary becoming validated,
- operationally addressed becoming scientifically solved,
- effective becoming fundamental,
- mathematical becoming physical,
- registry status becoming truth,
- canonical artifact becoming completed theory,
- Cube hypothesis becoming Cube ontology,
- QIC bridge work becoming completed quantum theory,
- and SSC application terminology becoming a scientific-core definition.

This file is a governance artifact.

It does not:

- solve scientific open questions,
- define new theory,
- create physical interpretation,
- establish ontology,
- define a common substrate,
- define `Rel_TIG`, `DefectSpace`, `B_TIG`, or `I_QIC`,
- establish QIC as identical to TIG,
- establish Cube theory,
- or resolve OQ-030 or OQ-031 by file existence alone.

OQ-031 terminology-governance completion is compatible with scientifically open objects when those objects remain correctly classified, scoped, typed, bounded, and protected from silent transfer.

---

## 2. Universal Rule

A claim-bearing statement must carry the exact values applicable to each independent status axis.

The protected rule is:

> No status may be upgraded by wording, repository location, scientific-domain placement, registry entry, canonical status, maturity label, audit passage, relation name, or cross-repository transfer.

A stronger status requires the evidence appropriate to that exact upgrade.

Depending on the target status, this may require:

- an explicit definition,
- an independent derivation,
- a mathematical proof,
- a completed validation protocol,
- empirical evidence,
- a typed bridge,
- dependency closure,
- or explicit human scientific acceptance.

---

## 3. Canonical Status Axes

The following axes are distinct and must not be compressed into one label.

| Axis | Question Answered | Canonical Example Values |
|---|---|---|
| Claim Status | What evidential strength or claim role does the statement have? | Working Assumption, Candidate, Declared, Partial, Compatible, Admissible, Selected, Derived, Proven, Validated, Physical Candidate, Empirically Supported, Fundamental Candidate |
| Scientific Status | Is the exact scientific question open or closed? | Scientifically Open, Resolved |
| Registry Status | Has the object been admitted to a registry? | Registerable, Registered |
| Operational Status | What happened in the workflow? | Pending, Addressed, Blocked, Operationally Closed |
| Artifact Status | What is the repository acceptance status of the file or input? | Raw Note, Non-Canonical Input, Canonical Artifact |
| Maturity Status | How developed is the artifact, analysis, track, or repository? | Preliminary, M0–M5, explicitly declared local L-levels such as L2 Repository Registered |
| Definition State | Is the object explicitly defined? | Defined, Partially Defined, Declared but Not Fully Defined, Named but Undefined, Undefined |
| Bridge State | Is the cross-domain interface established? | Not Required, Required, Missing, Candidate Bridge, Partial Bridge, Established Within Scope |
| Progress Classification | How far has a governed question progressed without changing its registry or scientific status? | PARTIALLY RESOLVED — CORRECTION REQUIRED; READY FOR COMPLETION AUDIT only after evidence supports it |
| Completion Readiness | Has the controlled artifact chain passed the required completion audit? | NOT ESTABLISHED, READY FOR AUDIT, AUDIT PASSED |
| Scientific Domain | In which scientific or governance domain does the claim operate? | Integrity_Nexus governance, TIG-E research architecture, TIG gravitational architecture, QIC quantum-bridge research, SIR mathematical recursion, Cube research, SSC deferred application projection |
| Repository Container | In which repository is the artifact stored? | Integrity_Nexus, TIG-E, Quantum_Integrity_Core, Structural_Integrity_Recursion, Structural_State_Controller |

### 3.1 Exact-Spelling Rule

The following near-duplicates are not interchangeable:

```text
Partial != Partially Defined
Candidate != Candidate Bridge
Operationally Closed != Closed Operationally
Established Within Scope != Established
Preliminary != Validated
Registry Status OPEN != Scientifically Open
Progress Classification != Scientific Status
```

### 3.2 Multi-Axis Example

A single object may simultaneously be:

```text
Claim Status: Candidate
Scientific Status: Scientifically Open
Registry Status: Registered
Artifact Status: Canonical Artifact
Maturity Status: Preliminary
Definition State: Partially Defined
Bridge State: Missing
```

None of these values cancels or upgrades another.

---

## 4. Scientific-Domain Model

Repository container and scientific domain must be recorded separately.

| Scientific Domain | Role | Default Status Boundary |
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

| Status | Meaning | What It Allows | What It Does Not Allow |
|---|---|---|---|
| Working Assumption | Temporarily used assumption under explicit scope | Local exploratory reasoning | No proof, no finality, no unrestricted transfer |
| Candidate | Proposed object, relation, equation, representation, gate, or model | Testing, audit, comparison, refinement | Not final, not selected by nature, not established |
| Declared | Named or introduced claim-bearing structure without full derivation | Reference as a declared claim object | Not proven, not derived, not validated |
| Partial | Some components of a claim are supported while a declared remainder stays open | Scoped use with unresolved remainder | No complete-result claim; does not mean Partially Defined unless Definition State says so |
| Compatible | Does not violate a target structure under stated conditions | Compatibility statement | No derivation, uniqueness, necessity, or physical selection |
| Admissible | Passes a stated gate, predicate, or constraint under declared scope | Gate-specific continuation | No truth claim beyond the gate |
| Selected | Chosen as a minimum, working option, or local implementation under explicit scope | Controlled downstream use of that selection | No derivation of necessity, uniqueness, or ontology |
| Derived | Obtained from stated premises through documented reasoning | Use within exact derivation scope | No broader status than premises and derivation support |
| Proven | Mathematically or logically proven under explicit assumptions | Proof-level use under those assumptions | No physical or empirical claim unless separately bridged |
| Validated | Checked successfully against declared criteria or evidence class | Validation within exact scope | No universal completion beyond validation scope |
| Physical Candidate | Candidate with an explicit physical interpretation path | Physical investigation under scope | No empirical confirmation and no final ontology |
| Empirically Supported | Supported by observational or experimental evidence under a declared model | Model-dependent empirical discussion | No unrestricted truth or final-theory claim |
| Fundamental Candidate | Candidate for underlying structure or ontology | Foundational investigation | Not a fundamental structure or truth |

### 5.2 Scientific Status

| Status | Meaning | Boundary |
|---|---|---|
| Scientifically Open | Further definition, derivation, proof, validation, empirical work, or scientific review is required | Scientific openness does not imply failed terminology governance |
| Resolved | The exact scientific question or blocker is closed by explicit accepted evidence | Does not close dependencies or neighboring questions automatically |

### 5.3 Registry Status

| Status | Meaning | Boundary |
|---|---|---|
| Registerable | Meets stated conditions for possible registry admission | Not yet registered; not scientifically accepted |
| Registered | Entered into a registry, backlog, queue, or index | Not true, physically selected, or scientifically resolved |

`OPEN` in an open-question registry is a registry-level question state meaning that the question has not been fully closed. It must not be confused with the Scientific Status value `Scientifically Open` or with absence of partial progress.

### 5.4 Operational Status

| Status | Meaning | Boundary |
|---|---|---|
| Pending | Declared workflow work has not yet been processed | No scientific inference |
| Addressed | Declared workflow item was processed within stated operational scope | Not scientifically solved |
| Blocked | Work cannot proceed until named dependencies are satisfied | Does not establish impossibility |
| Operationally Closed | Workflow or gate sequence is closed within declared process scope | Scientific dependencies may remain open |

`Operational` is the name of the axis, not a permitted status value.

### 5.5 Artifact Status

| Status | Meaning | Boundary |
|---|---|---|
| Raw Note | Unprocessed note, idea, or fragment | No canonical scientific claim |
| Non-Canonical Input | Preserved material not accepted as current canonical claim-bearing output | Must not be cited as current canonical result |
| Canonical Artifact | Repository-recognized file or governance object | Not automatically true, proven, validated, or a completed theory |

### 5.6 Maturity Status

| Status | Meaning | Boundary |
|---|---|---|
| Preliminary | Analysis, result, or artifact exists but remains incomplete, provisional, or not fully validated | Preliminary is not a Claim Status and does not mean Validated |
| M0–M5 | Repository or artifact maturity under `governance/maturity_model.md` | Maturity is not scientific truth |
| Explicit Local L-Level | Repository-local maturity label such as `L2 Repository Registered`, when defined by its local audit | Local level must not be generalized without mapping |

### 5.7 Definition State

| Definition State | Meaning |
|---|---|
| Defined | Object has an explicit local definition and type under scope |
| Partially Defined | Some defining structure is explicit; essential elements remain open |
| Declared but Not Fully Defined | Object is introduced and partially described, but definition or typing is incomplete |
| Named but Undefined | Recognized scientific object with no sufficient definition |
| Undefined | No accepted definition exists |

The Claim Status `Declared` and the Definition State `Declared but Not Fully Defined` are distinct values on distinct axes.

### 5.8 Bridge State

| Bridge State | Meaning |
|---|---|
| Not Required | No cross-domain transfer is being claimed |
| Required | Transfer cannot be accepted without an explicit bridge |
| Missing | A required bridge is absent |
| Candidate Bridge | A proposed bridge structure exists but is not established |
| Partial Bridge | Some interface components exist; completion remains open |
| Established Within Scope | A typed and accepted interface exists under explicit limits |

Mandatory boundary:

```text
bridge name != bridge existence
Candidate != Candidate Bridge
bridge candidate != Established Within Scope
```

### 5.9 Progress Classification and Completion Readiness

`PARTIALLY RESOLVED — CORRECTION REQUIRED` is a Progress Classification, not a Scientific Status and not a Registry Status.

It means:

- material progress is repository-supported,
- the question is not fully closed,
- critical synchronization or consistency corrections remain,
- and Completion Readiness is `NOT ESTABLISHED`.

`READY FOR COMPLETION AUDIT` may be used only when:

- all required artifacts are synchronized to current HEAD,
- no known blocking inconsistency remains,
- the exact completion criterion is stated,
- and a completion audit is the only remaining closure step.

`AUDIT PASSED` is a Completion Readiness value and does not by itself change a scientific question to `Resolved`; the governing registry must apply the accepted audit result under its closure rule.

---

## 6. Composite Status Phrases

Composite phrases are permitted only when every component can be decomposed into the axes above.

### Scoped Canonical Field-Equation Architecture

```text
Artifact Status: Canonical Artifact
Claim Status: Physical Candidate or Declared, as locally evidenced
Scope: Explicitly scoped
Scientific Status: Scientifically Open where completion dependencies remain
```

It does not mean complete theory.

### Selected Minimum Placeholder

```text
Claim Status: Selected
Definition State: Defined or Partially Defined, as locally evidenced
Scope: Minimum placeholder only
```

It does not mean uniquely derived or final ontology.

### Preliminary Effective Stress Analysis

```text
Maturity Status: Preliminary
Object Context: Effective realization
Scientific Status: Scientifically Open where interpretation remains unresolved
```

It does not mean independently validated physical stress-energy.

### PARTIALLY RESOLVED — CORRECTION REQUIRED

```text
Axis: Progress Classification
Completion Readiness: NOT ESTABLISHED
Registry Status: unchanged
Scientific Status: unchanged
```

A composite phrase must never hide a weaker component status.

---

## 7. Status Upgrade Requirements

| From | To | Required Evidence |
|---|---|---|
| Raw Note | Non-Canonical Input | Preservation decision and source context |
| Non-Canonical Input | Canonical Artifact | Explicit repository acceptance or canonical placement |
| Working Assumption | Candidate | Candidate definition and testable or auditable criteria |
| Candidate | Admissible | Named gate or predicate passed under declared scope |
| Candidate | Selected | Explicit local selection rule and selection scope |
| Candidate | Derived | Documented derivation from accepted premises |
| Declared | Derived | Independent derivation without circular premise |
| Compatible | Derived | Derivation showing that the target structure follows, not merely fits |
| Selected | Derived | Derivation showing necessity or origin; selection alone is insufficient |
| Preliminary | Validated | Completed validation against declared criteria; this is a cross-axis maturity-to-claim transition and must be stated explicitly |
| Addressed | Resolved | Scientific closure evidence, not workflow processing alone |
| Operationally Closed | Resolved | Exact scientific closure criteria and dependencies satisfied |
| Registerable | Registered | Registry admission under registry rules |
| Registered | Canonical Artifact | Separate artifact-acceptance action; registry placement alone is insufficient |
| Canonical Artifact | Proven | Explicit proof; file status alone is insufficient |
| Validated | Resolved | Validation addresses the exact scientific question and required dependencies |
| Mathematical Object | Physical Candidate | Explicit physical interpretation bridge |
| Effective Description | Fundamental Candidate | Argument showing why the object is a plausible underlying candidate rather than only effective |
| Physical Candidate | Empirically Supported | Observational or experimental evidence under a declared model |
| Fundamental Candidate | Fundamental Structure | Not available as a default taxonomy upgrade; requires extraordinary explicit support and acceptance |
| Required or Missing | Established Within Scope | Typed interface, mapping, assumptions, and validation of transfer |
| Named but Undefined | Defined | Explicit object definition, domain, type, scope, and non-circular dependencies |
| PARTIALLY RESOLVED — CORRECTION REQUIRED | READY FOR COMPLETION AUDIT | All required artifacts synchronized and all known blocking inconsistencies corrected |
| READY FOR COMPLETION AUDIT | AUDIT PASSED | Completion audit passes against explicit closure criteria |

---

## 8. Forbidden Status Upgrades

The following upgrades are forbidden unless separately documented with the required evidence:

| Forbidden Upgrade | Reason |
|---|---|
| Candidate → Final | Candidate status is non-final by definition |
| Candidate → Selected by Nature | Local selection is not physical selection |
| Selected → Derived | Choice does not prove necessity or origin |
| Compatible → Derived | Compatibility does not prove origin or necessity |
| Declared → Established | Naming an object does not establish it |
| Partial → Complete | Supported components do not close the remainder |
| Partially Defined → Defined | Partial definition does not supply missing elements |
| Preliminary → Validated | Preliminary maturity has not completed validation |
| Addressed → Scientifically Solved | Process handling is not scientific closure |
| Operationally Closed → Resolved | Workflow closure does not close scientific dependencies |
| Registerable → Accepted Physical Law | Registry eligibility is not scientific selection |
| Registered → True | Registry status is governance metadata |
| Canonical Artifact → Completed Theory | Canonical files may still describe open work |
| Effective → Fundamental | Scoped effective structures are not ontology |
| Mathematical → Physical | Physical reading requires bridge and validation |
| Local Validation → Global Validation | Validation scope must not expand silently |
| Foundational → Fundamental | Research level does not establish ontology |
| Fundamental Candidate → Fundamental Structure | Candidate status remains non-final |
| Audit Passage → Proof | Audit and proof are different evidence classes |
| Formal Readout → Physical Measurement | Measurement semantics require an explicit bridge |
| Shared Term → Identical Definition | Terminology requires domain-specific type control |
| Repository Container → Scientific Domain Identity | Repository placement does not identify the scientific object |
| Cube Corpus → Completed Cube Theory | Corpus existence is not theory completion |
| Cube Hypothesis → Cube Ontology | Hypothesis and ontology are different claim levels |
| Planck Manifestation → Cube Identity | Observable lower-bound assumption does not identify the Cube |
| QIC Compatibility → QM Derivation | Compatibility does not reconstruct quantum mechanics |
| TIG Field-Equation Architecture → QIC Theory | TIG and QIC are distinct scientific domains |
| SSC Application Projection → Core Scientific Definition | Downstream application language cannot define the core |
| Scientifically Open → Failed Governance | Open science is compatible with completed terminology governance when boundaries are exact |
| AUDIT PASSED → Scientific Truth | A governance audit does not create scientific evidence |

---

## 9. Required Claim Header Template

New or materially revised claim-bearing documents should include:

```text
Claim Status:
Scientific Status:
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

Recommended `Claim Type` values include:

- governance,
- registry,
- audit,
- candidate,
- compatibility,
- derivation,
- proof,
- validation,
- physical candidate,
- mathematical structure,
- empirical program,
- bridge document,
- terminology control,
- foundational research direction,
- working assumption,
- preliminary analysis.

`Claim Type` is descriptive metadata and is not a status axis.

---

## 10. Scientific-Domain Status Controls

### 10.1 Integrity_Nexus Governance

Governance claims may define:

- process,
- registry,
- dependency,
- role,
- scope,
- status vocabulary,
- maturity vocabulary,
- review obligations,
- and transfer rules.

They may not define:

- physical theory,
- mathematical proof,
- scientific ontology,
- or empirical truth.

### 10.2 TIG-E Research Architecture

TIG-E claims may define:

- gates,
- candidate lifecycle,
- registry admission,
- blocker states,
- audit procedures,
- preservation conditions,
- and operational research workflow.

They may not silently convert:

- gate passage into scientific truth,
- compatibility into derivation,
- registration into physical selection,
- or operational closure into scientific closure.

### 10.3 TIG Gravitational Architecture

TIG physical-candidate claims require:

- explicit model scope,
- mathematical structure,
- physical interpretation,
- declared open dependencies,
- and validation path.

The current scoped field-equation architecture must not be promoted to:

- complete covariant theory,
- completed dynamical theory,
- independent fundamental tensor theory,
- or empirical confirmation.

### 10.4 QIC Quantum-Bridge Research

QIC claims must preserve:

```text
Σ_QIC = selected minimum abstract placeholder only
I_QIC = named but undefined scientific object
Read_QIC = formal readout concept; physical measurement bridge open
Pres_QM = structural compatibility condition; not QM derivation
```

QIC may not inherit TIG status merely because TIG and QIC material appear within related repositories.

### 10.5 SIR Mathematical Recursion

SIR mathematical claims require explicit local definitions and proof conditions.

They may not become physical claims without:

- a typed bridge,
- physical interpretation,
- and the required validation.

SIR canonical repository status is an artifact status, not scientific truth.

### 10.6 Cube Research

Cube status language must preserve:

```text
Cube research corpus != completed Cube theory
Cube hypothesis != derived physical ontology
Working Cube scale != derived Cube scale
Planck-scale manifestation != Cube identity
Cube state != Σ_QIC without bridge
fractal research question != fractal law
Cube transience question != established Cube transience
```

Cube-specific labels such as:

- FOUNDATIONAL HYPOTHESIS,
- FOUNDATIONAL RESEARCH DIRECTION,
- ACTIVE AUDIT,
- ACTIVE RESEARCH,
- WORKING DERIVATION,
- WORKING ASSUMPTION,
- and OPEN

must be mapped explicitly onto the canonical axes rather than treated as self-explanatory global statuses.

`WORKING DERIVATION` does not mean Claim Status `Derived` unless the derivation is complete and independently auditable.

### 10.7 SSC Deferred Application Projection

SSC remains outside the active scientific-core derivation scope.

SSC application terminology may later be evaluated for projection compatibility.

It may not currently:

- define TIG,
- define QIC,
- define SIR,
- define Cube structures,
- identify the common substrate,
- or upgrade any scientific-core claim.

---

## 11. QIC/TIG Anti-Collapse Controls

The following distinctions are mandatory:

| Repository / Object | Scientific Domain | Status Boundary |
|---|---|---|
| `Quantum_Integrity_Core` repository | Repository container | Contains TIG gravitational architecture; container name does not establish QIC identity |
| `Iμν[g,r_c]` | TIG gravitational architecture | Scoped effective tensor realization; independent foundation open |
| `I_QIC` | QIC quantum-bridge research | Named but undefined object |
| `Σ_QIC` | QIC quantum-bridge research | Selected minimum abstract state set |
| TIG field-equation architecture | TIG gravitational architecture | Physical candidate under scope; not QIC theory |
| QIC bridge program | QIC quantum-bridge research | Scientifically open; not completed QM |

Forbidden upgrades:

```text
Iμν -> I_QIC
TIG architecture -> QIC theory
Σ_QIC -> TIG spacetime state
QIC compatibility -> QM derivation
repository name -> scientific object identity
```

---

## 12. OQ-031 Governance Completion Criterion

OQ-031 does not require the common substrate, `Rel_TIG`, `DefectSpace`, `B_TIG`, `I_QIC`, Cube ontology, Cube-to-QIC bridge, or SSC projection to be scientifically solved.

It requires that every unresolved object or bridge remain:

- explicitly identified,
- assigned to the correct repository container and scientific domain,
- given its exact Claim Status, Scientific Status, Definition State, Bridge State, and scope,
- protected by relation and transfer boundaries,
- and prevented from silent status upgrade.

Therefore:

```text
scientifically open object != incomplete terminology governance
```

Terminology governance is incomplete only when the open object is absent, ambiguously typed, inconsistently classified, falsely bridged, silently upgraded, or transferred outside its declared boundary.

---

## 13. Review Checklist

Before accepting, transferring, or upgrading a claim, check:

- What is the exact Claim Status?
- What is the exact Scientific Status?
- What is the Registry Status?
- What is the Operational Status?
- What is the Artifact Status?
- What is the Maturity Status?
- What is the Progress Classification?
- What is the Completion Readiness?
- What is the Definition State?
- What is the Bridge State?
- What is the repository container?
- What is the scientific domain?
- Are exact canonical spellings used?
- Is `Partial` being confused with `Partially Defined`?
- Is `Candidate` being confused with `Candidate Bridge`?
- Is `Preliminary` being treated as Claim Status rather than Maturity Status?
- Is status being upgraded by wording, location, canonical placement, or registration?
- Is selection being written as derivation?
- Is compatibility being written as derivation?
- Is preliminary work being written as validated?
- Is operational closure being written as scientific closure?
- Is a mathematical object being written as physical?
- Is an effective description being written as fundamental?
- Is a canonical artifact being treated as completed theory?
- Is an audit result being treated as proof?
- Is a formal readout being treated as physical measurement?
- Is QIC being collapsed into TIG?
- Is Cube research being promoted to ontology?
- Is SSC application language entering the core prematurely?
- Is scientific openness being incorrectly treated as governance failure?
- Is the evidence sufficient for the exact requested upgrade?

---

## 14. Synchronization Result

This revision synchronizes the taxonomy with:

- `shared/terminology_inventory.md` content SHA `d835d2224113f8f09799db9ca97c8cc269d92cf8`, and
- `shared/terminology_drift_matrix.md` content SHA `fc0b4c975960c30d6e8c68964ac6338510ae578d`.

It corrects the Completion & Consistency Audit findings by:

1. assigning `Preliminary` exclusively to Maturity Status;
2. preserving `Partial` as Claim Status and `Partially Defined` as Definition State;
3. standardizing `Operationally Closed` and removing `Closed Operationally`;
4. standardizing `Established Within Scope` and replacing ambiguous `Established` bridge wording;
5. separating `Candidate` from `Candidate Bridge`;
6. separating Registry Status `OPEN`, Scientific Status `Scientifically Open`, Progress Classification, and Completion Readiness;
7. formalizing `PARTIALLY RESOLVED — CORRECTION REQUIRED` as Progress Classification;
8. adding the OQ-031 governance-completion criterion;
9. preventing scientifically open objects from being treated as automatic governance failures;
10. adding `Relation Target` to the cross-domain claim header;
11. recording the one-way control-chain position;
12. removing stale wording that treated earlier registry synchronization as historically absent.

---

## 15. OQ-030 / OQ-031 Status

This file partially advances:

- OQ-030 / OQ-NEXUS-001 — Cross-Repository Claim Boundaries
- OQ-031 / OQ-NEXUS-002 — Shared Terminology Without Domain Collapse

Current supported values:

```text
Registry Status: OPEN
Progress Classification: PARTIALLY RESOLVED — CORRECTION REQUIRED
Completion Readiness: NOT ESTABLISHED
```

The corrected terminology inventory, terminology drift matrix, and this claim-status taxonomy are synchronized at current HEAD.

The following downstream artifacts require targeted resynchronization:

1. `governance/cross_repository_claim_boundary_matrix.md`
2. `registry/open_questions.md`
3. `registry/master_open_question_backlog.md`
4. `registry/repository_status.md`

Completion Readiness remains `NOT ESTABLISHED` until those artifacts are synchronized, stale Cube backlog entries are corrected, and the final Completion & Consistency Re-Audit passes.

Interface-specific boundary documents remain conditional requirements when an actual new transfer or bridge is attempted. Their absence does not by itself block OQ-031 governance completion for relations already classified as Missing, Required, Deferred, Undefined, or Explicitly Non-Equivalent.

---

## 16. Maintenance Rule

Any document that introduces or changes a claim-bearing artifact must use this taxonomy or explicitly justify an equivalent local mapping.

Any stronger status must provide the evidence required for that exact upgrade or remain at the weaker status.

Whenever a new status phrase appears, it must be decomposable into the separate axes defined here.

Any change to the terminology inventory or drift matrix invalidates this taxonomy's synchronization claim until it is explicitly reconciled against the new content SHAs.

No taxonomy update may create scientific evidence, definition, proof, validation, bridge, ontology, or theory absent from the source repositories.
