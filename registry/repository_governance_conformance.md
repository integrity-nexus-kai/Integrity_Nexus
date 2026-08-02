# Repository Governance Conformance Register

## Purpose and Authority Boundary

This register records evidence-based conformance of the eight active repositories with the TIG Research Governance Standard (TRGS).

It is not a scientific status register and does not assign global synchronization, Progress Classification, Completion Readiness, Claim Status, Scientific Status, or Question State. Those authorities remain where assigned by the canonical governance architecture, especially `registry/repository_status.md`.

---

## Allowed Conformance States

```text
NOT ASSESSED
GAPS IDENTIFIED
CORRECTION IN PROGRESS
CONFORMANT WITH FINDINGS
CONFORMANT
```

No repository may receive `CONFORMANT` without a fixed snapshot, evidence paths, completed review, and recorded findings disposition.

---

## Initial Eight-Repository Baseline

| Repository | TRGS mapping | Citation / bibliography mapping | Fixed snapshot | Conformance state |
|---|---|---|---|---|
| `Integrity_Nexus` | Candidate implementation internally verified; independent audit pending | `governance/references.bib`; `publication/briefings/references.bib`; scoped literature record present | `d47e815092e7e7c14544700221e7c8536d5fe766` | CONFORMANT WITH FINDINGS |
| `TIG-E-Topological_integrity-_gravity_engine-` | Local candidate maps authority, legacy status, L0–L5 maturity, and operational status | Artifact-specific bibliography rule; no synthetic empty bibliography | `4942ce072744b99a28fa27af343e1dcb54e535aa` | CONFORMANT WITH FINDINGS |
| `Quantum_Integrity_Core` | Local candidate separates QIC artifact classes from Nexus axes | Inline paper bibliography and arXiv `.bib` assigned distinct roles; competing CFF removed | `30051205ee5c0ed49bf3ad08ace152168d4438de` | CONFORMANT WITH FINDINGS |
| `TIG_YM_derivation_architecture` | Local candidate limits local proof/classification authority | Two publication-specific `.bib` paths mapped; missing cited key added; competing CFF removed | `5d38f0ae2ed7a90df5bcfd10a86ce6b5fb662b6f` | CONFORMANT WITH FINDINGS |
| `TIG_YM_Research` | Local candidate consolidates one open-problem authority and separates lifecycle axes | Initial verified `paper/references.bib`; full manuscript review remains required | `9f05b81387d41c3aa016c89a5ecb85c1c8063e52` | CONFORMANT WITH FINDINGS |
| `Structural_Integrity_Recursion` | Local candidate separates curation labels from Nexus status axes | Paper-specific bibliography gate; conflicting CFF removed | `28e115e4d01dab81b65dcf21cd88710da5a095f5` | CONFORMANT WITH FINDINGS |
| `Structural_State_Controller` | Local candidate unifies the claim-category authority and maps it as evidence type | Publication-specific bibliography and security/dual-use gate | `65f99fcad9773caa66f9fcdaa32c25e3bf8a672d` | CONFORMANT WITH FINDINGS |
| `integrity-nexus-kai.github.io` | Local candidate fixes publication-surface authority | Source-repository bibliography handoff; no synthetic website `.bib` | `9e7cb63d844144b93458c46735d21613cd57070c` | CONFORMANT WITH FINDINGS |

---

## Required Evidence for Assessment

Each assessment must record:

- repository and fixed snapshot identifier;
- effective local governance entry point;
- TRGS authority acknowledgement and local-extension boundary;
- status-axis mapping;
- citation and bibliography paths where applicable;
- open findings and severity;
- reviewer and review date;
- decision evidence for the assigned conformance state.

Absence of a required function is a finding. Absence of an assessment is `NOT ASSESSED`, not evidence of non-conformance.

---

## Maintenance Rule

Update this register only after a fixed-snapshot conformance review or a verified correction pass. Every state change must link to its audit evidence. No conformance state change automatically updates `registry/repository_status.md`.
