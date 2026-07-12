# Claim Status Taxonomy

**Repository:** Integrity_Nexus  
**Scope:** Scientific-core TIG Research Ecosystem with controlled Cube-domain coverage  
**Status:** CANONICAL / LOCKED MODE  
**Synchronization Base:** `shared/terminology_inventory.md` and `shared/terminology_drift_matrix.md`  
**OQ Status Contribution:** PARTIALLY RESOLVED — CORRECTION REQUIRED  
**Related Open Questions:** OQ-030 / OQ-NEXUS-001; OQ-031 / OQ-NEXUS-002  
**Last Updated:** 2026-07-12

---

## 1. Purpose

This file defines the permitted status vocabulary for claims inside the scientific-core TIG Research Ecosystem.

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

---

## 2. Universal Rule

A claim must always carry its exact status.

The protected rule is:

> Claim status may never be upgraded by wording, repository location, scientific-domain placement, registry entry, canonical status, maturity label, audit passage, or cross-repository transfer.

A stronger status requires the evidence appropriate to that exact upgrade.

Depending on the target status, this may require:

- an explicit definition,
- an independent derivation,
- a mathematical proof,
- a validation protocol,
- empirical evidence,
- a typed bridge,
- dependency closure,
- or explicit human scientific acceptance.

---

## 3. Status Axes Must Remain Separate

The following axes are distinct and must not be compressed into one label:

| Axis | Question Answered | Example Values |
|---|---|---|
| Claim Status | What evidential strength does the claim have? | Working Assumption, Candidate, Derived, Proven, Validated |
| Scientific Status | Is the scientific problem open or resolved? | Scientifically Open, Resolved |
| Registry Status | Has the object been recorded or admitted into a registry? | Registerable, Registered |
| Operational Status | What happened in the workflow? | Pending, Addressed, Blocked, Closed Operationally |
| Artifact Status | Is the file an accepted repository artifact? | Canonical Artifact, Non-Canonical Input |
| Maturity Status | How developed is the artifact or repository? | M0–M5, L2 Repository Registered, Preliminary |
| Definition State | Is the object defined? | Defined, Partial, Named but Undefined, Undefined |
| Bridge State | Is a cross-domain relation established? | Required, Missing, Candidate, Established |
| Scientific Domain | In which scientific or governance domain does the claim operate? | TIG, QIC, SIR, Cube, Nexus, TIG-E, SSC Deferred |

A claim may be, for example:

```text
Registered
Canonical Artifact
Preliminary
Scientifically Open
```

at the same time.

None of these labels cancels the others.

---

## 4. Scientific-Domain Model

Repository container and scientific domain must be recorded separately.

| Scientific Domain | Role | Default Status Boundary |
|---|---|---|
| Integrity_Nexus governance | Meta-governance, registry, dependency, maturity, and claim control | May define governance; may not define physics, mathematics, or ontology |
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

## 5. Canonical Status Vocabulary

### 5.1 Claim and Scientific Statuses

| Status | Meaning | What It Allows | What It Does Not Allow |
|---|---|---|---|
| Raw Note | Unprocessed idea, note, or fragment | Preservation for later review | No canonical scientific claim |
| Working Assumption | Temporarily used assumption under explicit scope | Local exploratory reasoning | No proof, no finality, no unrestricted transfer |
| Candidate | Proposed object, relation, equation, representation, gate, or model | Testing, audit, comparison, refinement | Not final, not selected by nature, not established |
| Declared | Named or introduced structure without full derivation | Reference as a declared object | Not proven, not derived, not validated |
| Partial | Some components are present or supported | Scoped use with unresolved remainder | No complete-result claim |
| Compatible | Does not violate a target structure under stated conditions | Compatibility statement | No derivation, uniqueness, necessity, or physical selection |
| Admissible | Passes a stated gate, predicate, or constraint under declared scope | Gate-specific continuation | No truth claim beyond the gate |
| Selected | Chosen as a minimum, working option, or local implementation under explicit scope | Controlled downstream use of that selection | No derivation of necessity, no uniqueness, no final ontology |
| Derived | Obtained from stated premises through documented reasoning | Use as derived within the exact derivation scope | No broader status than the premises and derivation support |
| Proven | Mathematically or logically proven under explicit assumptions | Proof-level use under those assumptions | No physical or empirical claim unless separately bridged |
| Preliminary | Existing analysis or result that remains incomplete, provisional, or unvalidated | Restricted use with explicit unresolved limitations | No validated, final, or resolved claim |
| Validated | Checked against declared criteria or evidence class | Validation within exact scope | No universal completion beyond validation scope |
| Physical Candidate | Candidate with an explicit physical interpretation path | Physical investigation under scope | No empirical confirmation and no final ontology |
| Empirically Supported | Supported by observational or experimental evidence under a declared model | Model-dependent empirical discussion | No unrestricted truth or final-theory claim |
| Fundamental Candidate | Candidate for underlying structure or ontology | Foundational investigation | Not a fundamental structure or truth |
| Resolved | Exact open question or blocker closed by explicit accepted evidence | Closure of that exact item | No automatic closure of dependencies or neighboring items |
| Scientifically Open | Further definition, derivation, proof, validation, empirical work, or review is required | Continued research | No closure claim |

### 5.2 Registry, Operational, and Artifact Statuses

| Status | Status Domain | Meaning | Boundary |
|---|---|---|---|
| Registerable | Registry lifecycle | Meets stated conditions for possible registry admission | Not yet registered; not scientifically accepted |
| Registered | Registry lifecycle | Entered into a registry, backlog, queue, or index | Not true, selected by nature, or scientifically resolved |
| Operational | Status domain | Concerns workflow, queue, gate, or repository execution | Not itself a scientific status value |
| Addressed | Operational value | Declared workflow item processed within stated operational scope | Not scientifically solved |
| Operationally Closed | Operational value | Workflow or gate sequence closed within declared process scope | Scientific dependencies may remain open |
| Blocked | Operational / dependency value | Work cannot proceed until named dependencies are satisfied | Does not establish impossibility |
| Canonical Artifact | Artifact status | Repository-recognized file or governance object | Not automatically a true or completed scientific result |
| Non-Canonical Input | Artifact status | Preserved material not accepted as canonical claim-bearing output | Must not be cited as current canonical result |

---

## 6. Composite Status Phrases

Composite phrases are permitted only when every component remains independently true.

Examples:

```text
Scoped Canonical Field-Equation Architecture
```

means:

- canonical artifact status,
- architecture-level scientific object,
- explicit scope limitation,
- not complete theory.

```text
Selected Minimum Placeholder
```

means:

- selected locally for current audit use,
- minimal structure only,
- not uniquely derived,
- not final ontology.

```text
Preliminary Effective Stress Analysis
```

means:

- analysis exists,
- effective model context,
- preliminary status,
- not independent physical stress-energy.

```text
PARTIALLY RESOLVED — CORRECTION REQUIRED
```

means:

- material progress is repository-supported,
- the question is not fully open in the sense of having no answer components,
- critical synchronization or evidence corrections remain,
- completion readiness is not yet established.

A composite phrase must never hide a weaker component status.

---

## 7. Status Upgrade Requirements

| From | To | Required Evidence |
|---|---|---|
| Raw Note | Working Assumption | Explicit scope and reason for temporary use |
| Working Assumption | Candidate | Candidate definition and testable or auditable criteria |
| Candidate | Admissible | Named gate or predicate passed under declared scope |
| Candidate | Selected | Explicit local selection rule and selection scope |
| Candidate | Derived | Documented derivation from accepted premises |
| Declared | Derived | Independent derivation without circular premise |
| Compatible | Derived | Derivation showing that the target structure follows, not merely fits |
| Selected | Derived | Derivation showing necessity or origin; selection alone is insufficient |
| Preliminary | Validated | Completed validation against declared criteria |
| Addressed | Resolved | Scientific closure evidence, not workflow processing alone |
| Operationally Closed | Resolved | Exact scientific closure criteria and dependencies satisfied |
| Registerable | Registered | Registry admission under the registry rules |
| Registered | Canonical Artifact | Repository acceptance or canonical placement |
| Canonical Artifact | Proven | Explicit proof; file status alone is insufficient |
| Validated | Resolved | Validation addresses the exact OQ and its required dependencies |
| Mathematical | Physical Candidate | Explicit physical interpretation bridge |
| Effective | Fundamental Candidate | Argument showing why the object is a plausible underlying candidate rather than only effective |
| Physical Candidate | Empirically Supported | Observational or experimental evidence under a declared model |
| Fundamental Candidate | Fundamental Structure | Not available as a default upgrade; requires extraordinary explicit support and acceptance |
| Bridge Required | Bridge Established | Typed interface, mapping, assumptions, and validation of transfer |
| Named but Undefined | Defined | Explicit object definition, domain, type, scope, and non-circular dependencies |

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
| Preliminary → Validated | Preliminary work has not completed validation |
| Addressed → Scientifically Solved | Process handling is not scientific closure |
| Operationally Closed → Scientifically Resolved | Workflow closure does not close scientific dependencies |
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

---

## 9. Required Claim Header Template

New or materially revised claim-bearing documents should include:

```text
Status:
Claim Type:
Repository:
Scientific Domain:
Scope:
Maturity Status:
Definition State:
Bridge State:
Dependencies:
Allowed Claims:
Non-Claims:
Evidence Required For Upgrade:
```

For cross-repository or cross-domain material, also include:

```text
Source Repository:
Target Repository:
Source Scientific Domain:
Target Scientific Domain:
Relation Class:
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

must be interpreted through this taxonomy and the local Cube maturity audit.

`WORKING DERIVATION` does not mean `DERIVED` unless the derivation is complete and independently auditable.

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

## 12. Definition and Bridge Status Controls

Claim status does not replace definition or bridge status.

### Definition State Vocabulary

| Definition State | Meaning |
|---|---|
| Defined | Object has an explicit local definition and type under scope |
| Partially Defined | Some structure is explicit; essential elements remain open |
| Declared | Named or introduced but not fully derived or typed |
| Named but Undefined | Recognized scientific object with no sufficient definition |
| Undefined | No accepted definition exists |

### Bridge State Vocabulary

| Bridge State | Meaning |
|---|---|
| Not Required | No cross-domain transfer is being claimed |
| Required | Transfer cannot be accepted without an explicit bridge |
| Missing | Required bridge is absent |
| Candidate | Proposed bridge structure exists but is not established |
| Partial | Some interface components exist; completion remains open |
| Established Within Scope | Typed and accepted interface exists under explicit limits |

Mandatory boundary:

```text
bridge name != bridge existence
bridge candidate != established bridge
```

---

## 13. Review Checklist

Before accepting, transferring, or upgrading a claim, check:

- What is the exact claim status?
- What is the exact scientific status?
- What is the registry status?
- What is the operational status?
- What is the artifact status?
- What is the maturity status?
- What is the definition state?
- What is the bridge state?
- What is the repository container?
- What is the scientific domain?
- Is status being upgraded by wording?
- Is status being upgraded by repository location?
- Is status being upgraded by canonical placement?
- Is status being upgraded by registration?
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
- Is the evidence sufficient for the exact requested upgrade?

---

## 14. Synchronization Result

This revision synchronizes the taxonomy with the corrected OQ-031 terminology layer by:

1. separating claim, scientific, registry, operational, artifact, maturity, definition, bridge, and domain axes;
2. adding `Selected` as a controlled local status;
3. adding `Preliminary` as a canonical status term;
4. separating `Operational` as a status domain from `Addressed` as a status value;
5. adding `Registerable`, `Operationally Closed`, `Blocked`, and `Non-Canonical Input` controls;
6. formalizing composite status phrases without allowing hidden upgrades;
7. separating repository container from scientific domain;
8. separating TIG gravitational architecture from QIC quantum-bridge research;
9. adding Cube-specific status controls;
10. deferring SSC as an application projection;
11. adding definition-state and bridge-state vocabularies;
12. removing stale remaining-work language that treated already existing artifacts as absent.

---

## 15. OQ-030 / OQ-031 Status

This file partially advances:

- OQ-030 / OQ-NEXUS-001 — Cross-Repository Claim Boundaries
- OQ-031 / OQ-NEXUS-002 — Shared Terminology Without Domain Collapse

Current supported status contribution:

```text
PARTIALLY RESOLVED — CORRECTION REQUIRED
```

The corrected inventory, drift matrix, and claim-status taxonomy are now synchronized at the governance-document level.

They do not resolve either OQ because:

1. `governance/cross_repository_claim_boundary_matrix.md` still requires reconciliation with the scientific-domain split and Cube-domain interfaces;
2. registry and repository-status files still require Cross-ID and scope references;
3. interface-specific boundary documents may still be required;
4. the final OQ-031 completion audit has not been performed;
5. all scientific objects, derivations, and bridges remain at their repository-supported status.

---

## 16. Maintenance Rule

Any document that introduces or changes a claim-bearing artifact must use this taxonomy or explicitly justify an equivalent local mapping.

Any stronger status must provide the evidence required for that exact upgrade or remain at the weaker status.

Whenever a new status phrase appears, it must be decomposable into the separate axes defined here.

No taxonomy update may create scientific evidence, definition, proof, validation, bridge, ontology, or theory absent from the source repositories.
