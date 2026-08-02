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
| `Integrity_Nexus` | Fourteen academic quality controls implemented; internal AIL-0 verification passed | `governance/references.bib`; `publication/briefings/references.bib`; scoped literature record verified | `cd642ee0d1173f32b8c6eca32ba086cbce21e921` | CONFORMANT WITH FINDINGS |
| `TIG-E-Topological_integrity-_gravity_engine-` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |
| `Quantum_Integrity_Core` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |
| `TIG_YM_derivation_architecture` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |
| `TIG_YM_Research` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |
| `Structural_Integrity_Recursion` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |
| `Structural_State_Controller` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |
| `integrity-nexus-kai.github.io` | Pending repository-by-repository implementation | Pending | Not assessed | NOT ASSESSED |

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
