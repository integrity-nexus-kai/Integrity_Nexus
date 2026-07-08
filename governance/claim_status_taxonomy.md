# Claim Status Taxonomy

**Repository:** Integrity_Nexus  
**Scope:** Complete TIG Research Ecosystem  
**Status:** CANONICAL / LOCKED MODE  
**Related Open Questions:** OQ-030, OQ-031  
**Date:** 2026-07-08

---

## 1. Purpose

This file defines the permitted status vocabulary for claims inside the TIG Research Ecosystem.

It exists to prevent silent status upgrades such as:

- candidate becoming final
- compatible becoming derived
- declared becoming established
- operationally addressed becoming scientifically solved
- effective becoming fundamental
- mathematical becoming physical
- registry status becoming truth

This file is a governance artifact. It does not solve scientific open questions and does not create new theory.

---

## 2. Universal Rule

A claim must always carry its exact status.

The protected rule is:

> Claim status may never be upgraded by wording, location, registry entry, file maturity, or cross-repository transfer.

A stronger status requires explicit evidence, derivation, proof, validation, or bridge documentation.

---

## 3. Status Categories

| Status | Meaning | What It Allows | What It Does Not Allow |
|---|---|---|---|
| Raw Note | Unprocessed idea, note, or fragment | Preservation for later review | No canonical claim |
| Working Assumption | Temporarily used assumption for exploration | Local reasoning under explicit scope | No proof, no final status, no global transfer |
| Candidate | Proposed object, relation, equation, representation, gate, or model | Testing, audit, comparison, refinement | Not final, not selected, not established |
| Declared | Named or introduced structure without full derivation | Reference as declared object | Not proven, not derived, not validated |
| Partial | Some components are present or supported | Scoped use with unresolved remainder | No complete result claim |
| Compatible | Does not violate a target structure under stated conditions | Compatibility statement | No derivation, no uniqueness, no physical selection |
| Admissible | Passes a stated gate, predicate, or constraint under declared scope | Gate-specific continuation | No truth claim beyond the gate |
| Operationally Addressed | A workflow item, gate, or queue object has been processed | Operational tracking closure | No scientific solution claim |
| Registered | Entered into a registry, backlog, queue, or index | Traceability and governance control | Not canonized as truth |
| Canonical Artifact | Repository-recognized file or governance object | Stable reference inside the ecosystem | Not automatically a true or completed scientific result |
| Derived | Obtained from stated premises through documented reasoning | Use as derived within scope | No broader status than the derivation supports |
| Proven | Mathematically or logically proven under explicit assumptions | Proof-level use under assumptions | No physical or empirical claim unless separately bridged |
| Validated | Checked against declared criteria or evidence class | Validation within scope | No universal completion beyond validation scope |
| Physical Candidate | Candidate with an explicit physical interpretation path | Physical investigation under scope | No empirical confirmation, no final ontology |
| Empirically Supported | Supported by observational or experimental evidence under declared model | Model-dependent empirical discussion | No unrestricted truth or final theory claim |
| Fundamental Candidate | Candidate for underlying structure or ontology | Foundational investigation | Not fundamental truth unless separately established |
| Resolved | Open question or blocker closed by explicit accepted evidence | Status closure of that item | Does not automatically resolve dependent or neighboring items |
| Scientifically Open | Requires further definition, derivation, proof, validation, or review | Continued research | No closure claim |

---

## 4. Status Upgrade Requirements

| From | To | Required Evidence |
|---|---|---|
| Raw Note | Working Assumption | Explicit scope and reason for temporary use |
| Working Assumption | Candidate | Candidate definition and testable/auditable criteria |
| Candidate | Admissible | Named gate or predicate passed under declared scope |
| Candidate | Derived | Documented derivation from accepted premises |
| Declared | Derived | Independent derivation without circular premise |
| Compatible | Derived | Derivation showing target structure follows, not merely fits |
| Operationally Addressed | Resolved | Scientific closure evidence, not only process completion |
| Registered | Canonical Artifact | Repository acceptance or canonical placement |
| Canonical Artifact | Proven | Explicit proof; file status alone is insufficient |
| Validated | Resolved | Validation must address the exact open question and dependencies |
| Mathematical | Physical Candidate | Explicit physical interpretation bridge |
| Effective | Fundamental Candidate | Argument showing non-effective underlying status candidate |
| Physical Candidate | Empirically Supported | Observational or experimental evidence under declared model |
| Fundamental Candidate | Fundamental Structure | Not available as default status; requires extraordinary explicit support |

---

## 5. Forbidden Status Upgrades

The following upgrades are forbidden unless separately documented:

| Forbidden Upgrade | Reason |
|---|---|
| Candidate → Final | Candidate status is non-final by definition |
| Compatible → Derived | Compatibility does not prove origin or necessity |
| Declared → Established | Naming an object does not establish it |
| Operationally Addressed → Scientifically Solved | Process closure is not scientific closure |
| Registered → True | Registry status is governance metadata |
| Canonical Artifact → Completed Theory | Canonical files may still describe open work |
| Effective → Fundamental | Scoped effective structures are not ontology |
| Mathematical → Physical | Physical reading requires bridge and validation |
| Local Validation → Global Validation | Validation scope must not expand silently |
| Shared Term → Identical Definition | Terminology requires domain-specific type control |

---

## 6. Required Claim Header Template

New research or governance documents should include a claim-status header when they introduce or modify claim-bearing content.

```text
Status:
Claim Type:
Scope:
Dependencies:
Allowed Claims:
Non-Claims:
Evidence Required For Upgrade:
```

Recommended values for `Claim Type` include:

- governance
- registry
- audit
- candidate
- compatibility
- derivation
- proof
- validation
- physical candidate
- mathematical structure
- empirical program
- bridge document
- terminology control

---

## 7. Domain-Specific Status Controls

### 7.1 Governance Claims

Governance claims may define process, registry, dependency, role, scope, and review obligations.

They may not define physical theory, mathematical proof, ontology, or empirical truth.

---

### 7.2 Mathematical Claims

Mathematical claims require explicit definitions and proof conditions.

They may not become physical claims without bridge documentation.

---

### 7.3 Physical Claims

Physical claims require explicit physical interpretation, model scope, and validation path.

A physical candidate is not empirical confirmation and not final ontology.

---

### 7.4 Operational Claims

Operational claims describe workflow state, queue state, gate processing, or repository maintenance.

They do not close scientific questions unless the scientific closure criteria are explicitly satisfied.

---

### 7.5 Compatibility Claims

Compatibility claims state that a structure can coexist with or satisfy a target constraint under stated conditions.

They do not establish derivation, uniqueness, selection, or physical necessity.

---

## 8. Review Checklist

Before accepting or transferring a claim, check:

- What is the current status of the claim?
- Is the status explicitly stated?
- Is the claim being upgraded by wording?
- Is the claim being upgraded by repository location?
- Is the claim being upgraded by being registered?
- Is compatibility being written as derivation?
- Is operational closure being written as scientific closure?
- Is a mathematical object being written as physical?
- Is an effective description being written as fundamental?
- Is a canonical artifact being treated as completed theory?
- Is the evidence sufficient for the claimed status?

---

## 9. OQ-030 / OQ-031 Status

This file partially advances:

- OQ-030 — Cross-Repository Claim Boundaries
- OQ-031 — Shared Terminology Without Domain Collapse

It does not resolve either open question.

Remaining work includes:

1. Interface-specific boundary documents where needed
2. Cross-references from registry and repository-status files
3. Future machine-readable claim-status schema under OQ-032

---

## 10. Maintenance Rule

Any document that introduces or changes a claim-bearing artifact should use this taxonomy.

If a stronger status is needed, the document must provide the evidence required for that upgrade or explicitly leave the claim at its weaker status.
