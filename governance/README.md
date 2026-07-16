# Governance Layer

The governance layer defines how Integrity Nexus preserves cross-repository coherence without inflating scientific claims or collapsing independent status axes.

## Authority Boundary

Integrity Nexus governance may:

- define repository and domain boundaries;
- control terminology, status vocabularies, applicability, evidence paths, and transfers;
- register dependencies and unresolved questions;
- require reproducible audits and synchronization gates;
- coordinate repository-level maturity and completion workflows.

It may not:

- create scientific evidence;
- define TIG, QIC, SIR, Cube, or SSC scientific objects;
- turn registration, repository placement, maturity, or audit passage into scientific truth;
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
| Global repository roles, synchronization, Progress Classification, and Completion Readiness | `../registry/repository_status.md` |
| Local Open Question lifecycle | `../registry/open_questions.md` |
| Master question lifecycle and dependencies | `../registry/master_open_question_backlog.md` |
| Shared terminology | `../shared/terminology_inventory.md` |
| Terminology-drift protection | `../shared/terminology_drift_matrix.md` |

This table is an entry-point map. The governance directory may contain additional controlled amendments, matrices, protocols, and audit-support artifacts.

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
```

No value may be transferred from one axis to another without evidence and an authorized transition defined for the target axis.

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
- or the synchronization state controlled by `registry/repository_status.md`.

Cross-repository scientific synchronization requires a fixed source snapshot, accepted audit evidence, explicit authorization, and an update of the controlling registry artifacts.

## Current Status

```text
Governance Layer: CANONICAL / ACTIVE
Root Navigation: synchronized to current repository-role and domain architecture
Scientific Status Authority: retained by scientific evidence and controlling source artifacts
Global Synchronization Authority: registry/repository_status.md
TIG-E Phase 1B audit-result transfer: NOT PERFORMED BY THIS README UPDATE
Open Question closure: NOT PERFORMED
```
