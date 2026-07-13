# Open Questions

**Repository:** Integrity_Nexus  
**Scope:** Meta-governance registry for the TIG Research Ecosystem  
**Status:** CANONICAL REGISTRY / LOCKED MODE / AUDIT-CORRECTED  
**Synchronization Base:** `shared/terminology_inventory.md` content SHA `f606e88848441374355f71bda117e12a52b8c42a`; `shared/terminology_drift_matrix.md` content SHA `4e76c99f7af891ef1309b5f61551679006ce7481`; `governance/claim_status_taxonomy.md` content SHA `d0506e71d47ee08863dae516a61078ef7a8275ca`; `governance/cross_repository_claim_boundary_matrix.md` content SHA `ff4d3debd6864dc056df04c39e4d5483baa7daa1`  
**Position in Control Chain:** terminology inventory → drift matrix → claim-status taxonomy → claim-boundary matrix → this local registry → master backlog → repository-status index  
**Global Synchronization and Completion-Readiness Authority:** `registry/repository_status.md`  
**Local OQ Status Contribution:** READY FOR COMPLETION AUDIT  
**Last Updated:** 2026-07-13

This document records registered questions for Integrity Nexus as a meta-repository.

These questions concern navigation, governance, dependency mapping, terminology control, and cross-repository coherence.

The following axes and control fields are distinct:

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
Required Work
Object Type
Scope
Progress Classification
Completion Readiness
```

Canonical lifecycle and applicability controls are:

```text
Question State: OPEN | CLOSED
Registry Status: Registerable | Registered
Scientific Status Applicability: APPLICABLE | NOT APPLICABLE
Scientific Status: Scientifically Open | Resolved
```

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

Rules:

- `OPEN` and `CLOSED` are Question State values, not Registry Status values.
- `NOT APPLICABLE` is a Scientific Status Applicability marker, not a Scientific Status value.
- When Scientific Status Applicability is `NOT APPLICABLE`, no Scientific Status value is assigned.
- Governance-question lifecycle is controlled by Question State, not Scientific Status.
- A question may remain `OPEN` while substantial repository-supported progress exists.
- Claim Status may use only one exact canonical Claim Status value supported by evidence.
- Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State must not be assigned as Claim Status.
- When no canonical Claim Status is supported, Claim Status remains unassigned.
- An unassigned Claim Status is not a governance failure and must not be replaced by descriptive wording.

This file does not report the global synchronization count and does not authoritatively assign global Completion Readiness. Those values belong only to `registry/repository_status.md`.

---

## Cross-ID Mapping

| Local Registry ID | Master Backlog ID | Title | Relation | Cross-ID Presence |
|---|---|---|---|---|
| OQ-NEXUS-001 | OQ-030 | Cross-Repository Claim Boundaries | Same registered problem core under local and master identifiers | PRESENT |
| OQ-NEXUS-002 | OQ-031 | Shared Terminology Without Domain Collapse | Same registered problem core under local and master identifiers | PRESENT |

The Cross-ID mapping is governance metadata.

It does not change Claim Status, Scientific Status Applicability, Scientific Status, Question State, Registry Status, Operational Status, Progress Classification, or Completion Readiness.

---

# FRQ-001 — Common Emergence Question

What is the underlying structure from which both spacetime and quantum mechanics emerge?

German formulation:

```text
Was ist es, aus dem Raumzeit und Quantenmechanik gemeinsam emergieren?
```

**Question State:** OPEN.  
**Registry Status:** Registered.  
**Scientific Status Applicability:** APPLICABLE.  
**Scientific Status:** Scientifically Open.  
**Claim Status:** No value assigned; this registry entry is a question and does not itself supply evidence for a canonical Claim Status.  
**Canonical Registry:** `registry/foundational_questions.md`.

**Boundary:** This is a research question only. It does not identify a common substrate, derive spacetime, derive quantum mechanics, introduce a field equation, select a physical ontology, or assign Claim Status to an answer candidate.

---

# OQ-NEXUS-001 — Cross-Repository Claim Boundaries

**Master Backlog ID:** OQ-030

How can Integrity Nexus show relationships between repository containers and scientific domains without inflating claims or changing their status during transfer?

**Question State:** OPEN.  
**Registry Status:** Registered.  
**Scientific Status Applicability:** NOT APPLICABLE.  
**Scientific Status:** No value assigned.  
**Claim Status:** No value assigned; governance progress and operational processing do not establish evidential Claim Status.  
**Operational Status:** Addressed.  
**Progress Classification:** READY FOR COMPLETION AUDIT.  
**Completion Readiness:** Authoritative value controlled only by `registry/repository_status.md`.

## Repository-Supported Progress

The current canonical governance layer establishes:

- repository-container versus scientific-domain separation,
- exact preservation of canonical status axes and applicability controls,
- Claim Status limited to the thirteen canonical values,
- unsupported Claim Status remaining unassigned,
- Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State remaining separate from Claim Status,
- Scientific Status Applicability separate from Scientific Status,
- Question State separate from Registry Status and Scientific Status,
- separate Relation Class and Relation Target fields,
- TIG/QIC anti-collapse boundaries,
- SIR mathematical-to-physical transfer boundaries,
- Cube-domain interfaces,
- deferred SSC application projection,
- the distinction between open science and failed governance,
- and `registry/repository_status.md` as the sole global synchronization authority.

## Completion Criterion

OQ-NEXUS-001 does not require every possible future interface to have a dedicated boundary file before closure.

It requires:

- a canonical general boundary architecture,
- explicit applicability and status-axis preservation,
- exact Claim Status assignment only where source evidence supports one,
- no conversion of Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, or Definition State into Claim Status,
- unsupported Claim Status remaining unassigned,
- explicit relation and transfer controls,
- correct classification of Missing or deferred bridges,
- and a rule requiring interface-specific boundary documentation when an actual new transfer or bridge is attempted.

## Remaining Closure Step

The governance corrections represented in this local registry are complete for the current scope.

The question remains `OPEN` until:

1. `registry/repository_status.md` records global Completion Readiness `READY FOR AUDIT`;
2. an independent Completion & Consistency Audit passes;
3. `registry/repository_status.md` records `AUDIT PASSED`;
4. the accepted result is explicitly applied in both local and master registries;
5. Question State is changed to `CLOSED`.

Scientifically open objects, Missing bridges, unassigned Claim Status where unsupported, and deferred SSC projection are not themselves blockers when their absence and transfer prohibitions are correctly represented.

**Boundary:** A canonical boundary matrix does not create scientific evidence, Claim Status, proof, bridge implementation, or physical identity.

---

# OQ-NEXUS-002 — Shared Terminology Without Domain Collapse

**Master Backlog ID:** OQ-031

How can shared concepts such as integrity, boundary, admissibility, invariant, and bounded evolution remain useful without forcing identical technical definitions across the scientific-core TIG Research Ecosystem?

**Question State:** OPEN.  
**Registry Status:** Registered.  
**Scientific Status Applicability:** NOT APPLICABLE.  
**Scientific Status:** No value assigned.  
**Claim Status:** No value assigned; registry admission, operational processing, and governance progress do not establish evidential Claim Status.  
**Operational Status:** Addressed.  
**Progress Classification:** READY FOR COMPLETION AUDIT.  
**Completion Readiness:** Authoritative value controlled only by `registry/repository_status.md`.

## Active Scientific-Core Scope

1. Integrity_Nexus governance
2. TIG-E research architecture
3. TIG gravitational architecture
4. QIC quantum-bridge research
5. SIR mathematical recursion
6. Cube research

Repository container and scientific domain remain separate.

Mandatory non-identities include:

```text
Quantum_Integrity_Core repository != QIC scientific object
QIC != TIG
I_QIC != Iμν
Σ_QIC != TIG spacetime state
Cube state != Σ_QIC without explicit bridge
shared term != identical technical definition
```

## SSC Scope Qualification

SSC remains:

```text
DEFERRED APPLICATION-PROJECTION SCOPE
```

SSC is not authorized at this stage to define TIG, QIC, SIR, Cube, the common substrate, `Rel_TIG`, `DefectSpace`, `B_TIG`, or `I_QIC`.

A later application-projection audit may test whether stabilized core terminology transfers safely into SSC.

Deferred SSC status does not itself block terminology-governance completion when deferral and transfer prohibition are explicit.

## Repository-Supported Progress

The terminology-governance layer controls:

- evidence inventory and terminology drift,
- `bounded evolution`,
- QIC/TIG domain separation,
- named but undefined scientific objects,
- state, transition, process, generator, Hamiltonian, readout, measurement, and observable terminology,
- SIR mathematical terminology,
- Cube state, scale, ontology, Planck manifestation, fractal organization, and transience/persistence,
- Claim Status, Scientific Status Applicability, Scientific Status, Question State, Registry Status, Operational Status, Artifact Status, Maturity Status, Progress Classification, and Completion Readiness,
- Definition State and Bridge State,
- Required Work, Object Type, and Scope as separate controls,
- exact canonical Claim Status assignment only where supported,
- unassigned Claim Status where no canonical value is supported,
- Relation Class and Relation Target,
- Allowed Transfer and Forbidden Transfer,
- and the single-authority global synchronization rule.

## OQ-031 Governance Completion Criterion

OQ-031 does not require the common substrate, `Rel_TIG`, `DefectSpace`, `B_TIG`, `I_QIC`, Cube ontology, Cube-to-QIC bridge, `integrity field`, or SSC projection to be scientifically solved or fully defined.

It requires every unresolved term, object, or interface to be:

- explicitly identified,
- assigned to the correct repository container and scientific domain,
- given exact Scientific Status applicability and exact applicable status-axis values,
- given a canonical Claim Status only where supported,
- left with Claim Status unassigned where no canonical value is supported,
- protected against conversion of Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, or Definition State into Claim Status,
- given exact Definition State and Bridge State,
- assigned a canonical Relation Class and separate Relation Target where applicable,
- scoped correctly,
- protected by Allowed Transfer and Forbidden Transfer,
- and prevented from silent status, applicability, axis, or domain upgrade.

```text
scientifically open object != incomplete terminology governance
missing bridge != incomplete terminology governance when absence is correctly controlled
deferred scientific definition != terminology-governance failure when deferral is explicit
Scientific Status Applicability NOT APPLICABLE != Scientific Status value
unassigned Claim Status != governance failure when no canonical value is supported
```

## Remaining Closure Step

The governance corrections represented in this local registry are complete for the current scope.

The question remains `OPEN` until:

1. global Completion Readiness is `READY FOR AUDIT`;
2. an independent Completion & Consistency Audit passes;
3. global Completion Readiness becomes `AUDIT PASSED`;
4. the governing local and master registries explicitly apply the accepted result;
5. Question State becomes `CLOSED`.

The following are not automatic blockers:

- scientifically undefined named objects,
- explicitly Missing bridges,
- unassigned Claim Status where no canonical Claim Status is supported,
- `integrity field` as a deferred scientific definition,
- deferred SSC projection,
- or future interface-specific additions not triggered by an actual transfer.

**Boundary:** Terminology governance records, types, separates, and constrains scientific language; it does not define or solve the scientific objects it records and does not invent Claim Status.

---

# OQ-NEXUS-003 — Reviewer Navigation

What is the shortest path for a reviewer to understand the research ecosystem without reading all repositories?

**Question State:** OPEN.  
**Registry Status:** Registered.  
**Scientific Status Applicability:** NOT APPLICABLE.  
**Scientific Status:** No value assigned.  
**Claim Status:** No value assigned.  
**Required Work:** Review and navigation design.

---

# OQ-NEXUS-004 — Machine-Readable Research Architecture

How should repository maps, shared concepts, dependency graphs, terminology records, and claim-state structures be organized for LLM-based review and automated research-audit systems?

**Question State:** OPEN.  
**Registry Status:** Registered.  
**Scientific Status Applicability:** NOT APPLICABLE.  
**Scientific Status:** No value assigned.  
**Claim Status:** No value assigned.  
**Required Work:** Schema definition and validation.

---

# OQ-NEXUS-005 — Publication Path

Should Integrity Nexus itself become citable as a research-governance artifact, or should it remain only a navigation layer?

**Question State:** OPEN.  
**Registry Status:** Registered.  
**Scientific Status Applicability:** NOT APPLICABLE.  
**Scientific Status:** No value assigned.  
**Claim Status:** No value assigned.  
**Required Work:** Governance and publication review.

---

## Local Reconciliation Result

This local registry is reconciled with:

- inventory SHA `f606e88848441374355f71bda117e12a52b8c42a`,
- drift-matrix SHA `4e76c99f7af891ef1309b5f61551679006ce7481`,
- taxonomy SHA `d0506e71d47ee08863dae516a61078ef7a8275ca`,
- boundary-matrix SHA `ff4d3debd6864dc056df04c39e4d5483baa7daa1`.

It preserves and records:

1. local OQ status contribution `READY FOR COMPLETION AUDIT`;
2. Claim Status limited to the thirteen canonical Claim Status values;
3. Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State prohibited as Claim Status assignments;
4. unsupported Claim Status required to remain unassigned;
5. no Claim Status inferred from Question State, Registry Status, Operational Status, Progress Classification, or file placement;
6. Scientific Status Applicability as a separate control field;
7. only `APPLICABLE` and `NOT APPLICABLE` as applicability markers;
8. only `Scientifically Open` and `Resolved` as Scientific Status values;
9. prohibition of `Scientific Status: NOT APPLICABLE`;
10. no Scientific Status value when applicability is `NOT APPLICABLE`;
11. applicability `APPLICABLE` for FRQ-001 and `NOT APPLICABLE` for the governance questions in this registry;
12. Question State, Registry Status, Operational Status, Progress Classification, and Completion Readiness as separate controls;
13. OQ-NEXUS-001 and OQ-NEXUS-002 remaining Question State `OPEN` and Progress Classification `READY FOR COMPLETION AUDIT`;
14. `registry/repository_status.md` as sole global synchronization and Completion Readiness authority;
15. the substantive status-axis and Claim-Status controls as historically adopted across the then-current downstream chain;
16. this revision as a local SHA reconciliation without asserting the current state of later artifacts.

The substantive progress/applicability and Claim-Status controls were historically adopted across the then-current downstream chain before the independent audit identified the later temporal and evidence-path findings.

This revision records that historical substantive state and locally reconciles the registry to the corrected inventory, drift matrix, taxonomy, and boundary matrix.

Later artifacts are reconciled to this revision only when their own synchronization bases reference the current upstream SHAs in dependency order and the resulting global state is recorded by `registry/repository_status.md`.

Whether that later reconciliation is currently pending or complete is not asserted by this local registry.

This local reconciliation is not a global synchronization report.

---

## Global-State Authority Rule

This file records question lifecycle and local registry content.

It does not state:

- how many of the seven controlled artifacts are globally synchronized,
- whether global Completion Readiness is `NOT ESTABLISHED`, `READY FOR AUDIT`, or `AUDIT PASSED`,
- or whether the independent completion audit has passed.

Those statements are authoritative only in:

```text
registry/repository_status.md
```

---

## Registry Maintenance and Closure Rule

A registered question must use:

```text
Question State: OPEN | CLOSED
Registry Status: Registerable | Registered
Scientific Status Applicability: APPLICABLE | NOT APPLICABLE
```

Scientific Status may use only:

```text
Scientifically Open
Resolved
```

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

When applicability is `NOT APPLICABLE`, no Scientific Status value is assigned.

When no canonical Claim Status is supported, no Claim Status value is assigned.

A generic `Status` field must not combine lifecycle, operational, scientific, claim, maturity, applicability, or required-work semantics.

`Required Work`, `Object Type`, and `Scope` are descriptive controls, not Claim Status values.

Scientific Status, Operational Status, Required Work, Object Type, Scope, Artifact Status, Maturity Status, and Definition State must never be inserted into Claim Status.

A governance question may be changed to Question State `CLOSED` only when:

- its exact governance closure criteria are satisfied,
- `registry/repository_status.md` records `AUDIT PASSED`,
- the accepted audit result covers the exact question,
- the local and master registries explicitly apply that result,
- unresolved scientific objects remain correctly bounded rather than necessarily solved,
- and no known blocking governance inconsistency remains.

Registry wording must never convert governance progress into Claim Status, scientific proof, bridge implementation, ontology, or theory completion.

Any change to one of the four upstream governance artifacts invalidates this registry's local reconciliation until explicitly updated against the new content SHAs.

This registry must never supersede `registry/repository_status.md` as the global synchronization or Completion Readiness authority.
