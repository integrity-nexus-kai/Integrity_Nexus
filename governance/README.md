# Governance Layer

The governance layer defines how Integrity Nexus preserves cross-repository coherence without inflating scientific claims or collapsing independent status axes.

## Authority Boundary

Integrity Nexus governance may:

- define repository and domain boundaries;
- control terminology, status vocabularies, applicability, evidence paths, and transfers;
- register dependencies and unresolved questions;
- require reproducible audits and synchronization gates;
- coordinate repository-level maturity and completion workflows;
- control canonicalization readiness, placement, and authorization.

It may not:

- create scientific evidence;
- define TIG, QIC, SIR, Cube, or SSC scientific objects;
- turn registration, repository placement, maturity, audit passage, or canonicalization into scientific truth;
- infer a bridge from a relation name;
- close an Open Question without the canonical closure sequence;
- or assign unsupported Claim Status.

Core rules:

```text
repository container != scientific domain
governance authority != scientific truth authority
definition != derivation
selection != necessity
compatibility != derivation
audit result != proof
canonicalization != evidence
registered != Question State CLOSED
```

## Canonical Control Architecture

| Control function | Canonical source |
|---|---|
| Repository maturity | `maturity_model.md` |
| Claim Status, applicability, lifecycle, and closure sequence | `claim_status_taxonomy.md` |
| Cross-repository and cross-domain transfers | `cross_repository_claim_boundary_matrix.md` |
| Research-question and Shared Frontier classification | `research_frontier_question_classification.md` |
| Repository conformance requirements | `repository_standard.md` |
| Claim-boundary requirements | `claim_boundary_standard.md` |
| Citation discipline | `citation_standard.md` |
| Canonicalization readiness and admission decisions | `canonicalization_threshold.md` |
| Global repository roles, synchronization, Progress Classification, and Completion Readiness | `../registry/repository_status.md` |
| Local Open Question lifecycle | `../registry/open_questions.md` |
| Master question lifecycle and dependencies | `../registry/master_open_question_backlog.md` |
| Shared terminology | `../shared/terminology_inventory.md` |
| Terminology-drift protection | `../shared/terminology_drift_matrix.md` |

This table is an entry-point map. The governance directory may contain additional controlled amendments, matrices, protocols, and audit-support artifacts.

## Canonicalization Boundary

The Canonicalization Threshold determines whether a research object is sufficiently explicit, bounded, traceable, reviewed, reconstructable, and authorized for canonical preservation.

It does not determine whether the object is ultimately true.

```text
Canonicalization Threshold != Truth Threshold
Canonicalization Threshold != Proof Threshold
Canonicalization Threshold != Open-Question Closure
Canonicalization Threshold != Publication Acceptance
```

An unresolved object may cross the Canonicalization Threshold when its unresolved status, provenance, dependencies, evidence limits, non-claims, and authority are represented accurately.

Possible outcomes include:

```text
CANONICALIZE
RETURN FOR RECONSTRUCTION
RETURN FOR EVIDENCE
RETURN FOR AUDIT
REVISE STATUS
PARK
ARCHIVE
REJECT
```

Governance authorizes a repository state. It does not manufacture the scientific support required for that state.

## TRGS Review Candidate

The proposed integrated control plane is prepared for future independent review; that review has not started:

```text
tig_research_governance_standard.md
academic_quality_benchmark.md
references.bib
research_record_and_disclosure_standard.md
integrity_concern_protocol.md
competence_risk_collaboration_standard.md
trgs_candidate_implementation_record.md
../registry/repository_governance_conformance.md
```

These preparation artifacts do not alter the canonical control architecture, scientific status, or global synchronization before independent audit and explicit author approval.

## Status-Axis Separation

The following controls remain distinct:

```text
Claim Status
Scientific Status Applicability
Scientific Status
Question State
Registry Status
Operational Status
Artifact Status
Maturity Status
Definition State
Bridge State
Progress Classification
Completion Readiness
Canonicalization Readiness
```

No value may be transferred from one axis to another without evidence and an authorized transition defined for the target axis.

Passing the Canonicalization Threshold does not automatically change any scientific-status axis.

## Repository and Domain Separation

The canonical repository-to-domain mapping is controlled by:

```text
../registry/repository_status.md
```

In particular:

```text
TIG-E repository != one single scientific domain
Quantum_Integrity_Core repository != QIC scientific object
Cube research domain != independent repository container
SSC application projection != active scientific-core authority
```

## Synchronization Rule

A navigation or governance-document update does not by itself change:

- scientific Claim Status;
- Scientific Status;
- Question State;
- bridge existence;
- global Completion Readiness;
- Canonicalization Readiness of unrelated objects;
- or the synchronization state controlled by `registry/repository_status.md`.

Cross-repository scientific synchronization requires a fixed source snapshot, accepted audit evidence, explicit authorization, and an update of the controlling registry artifacts.

## Relationship to the Foundation Layer

The Foundation Layer defines the research architecture and lifecycle that governance controls but does not replace.

Relevant sources include:

```text
../foundation/07_integrity_centered_research_lifecycle.md
../foundation/08_research_signal_to_noise_optimization.md
../foundation/09_bottleneck_detection_architecture.md
../foundation/10_methodology_of_structured_discovery.md
../foundation/12_externalized_cognition_and_canonical_memory.md
```

Core separation:

```text
Foundation architecture -> defines process and research-state relationships
Governance -> controls admissible transitions, authority, and preservation
Scientific evidence -> supports or falsifies domain claims
```

## Current Status

```text
Governance Layer: CANONICAL / ACTIVE
Root Navigation: synchronized to current repository-role and Foundation architecture
Canonicalization Threshold: ACTIVE WORKING CONTROL
Scientific Status Authority: retained by scientific evidence and controlling source artifacts
Global Synchronization Authority: registry/repository_status.md
TIG-E Phase 1B audit-result transfer: NOT PERFORMED BY THIS README UPDATE
Open Question closure: NOT PERFORMED
```
