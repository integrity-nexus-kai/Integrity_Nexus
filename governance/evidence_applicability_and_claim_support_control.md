# Evidence Applicability and Claim Support Control

**Repository:** Integrity_Nexus  
**Control ID:** INX-EVID-APP-001  
**Version:** v1.0  
**Date:** 2026-09-26  
**Artifact Status:** Canonical Artifact  
**Scientific Status Applicability:** NOT APPLICABLE  
**Scope:** Cross-repository governance for determining what kind of support a claim requires at its current status and whether missing empirical evidence is a defect, a promotion barrier, or not applicable  
**Status Vocabulary Authority:** `governance/claim_status_taxonomy.md`  
**Canonicalization Control:** `governance/artifact_canonicalization_and_open_question_control.md`  
**Global Synchronization Authority:** `registry/repository_status.md`

---

## 1. Purpose

This control prevents the invalid inference:

```text
no empirical evidence
→ claim defective
```

Before an auditor, agent, or repository workflow may raise a missing-evidence finding, it must first determine:

1. the exact claim being assessed;
2. the claim's support class;
3. the support type required for the current claim;
4. whether empirical evidence is applicable at the current status;
5. whether missing evidence invalidates the current claim or only blocks a stronger promotion.

This control does not lower scientific standards. It makes the required standard claim-specific.

---

## 2. Protected Non-Identities

```text
no empirical evidence != no justification
not yet empirically tested != logically defective
not yet empirically tested != definition failure
not yet empirically tested != formal derivation failure

definition != empirical claim
formal derivation != empirical observation
theoretical candidate != empirical fact
physical existence claim != theoretical candidate
universal empirical claim != scoped empirical claim

missing promotion evidence != defect in current weaker status
required current evidence missing = current claim support defect
```

---

## 3. Claim Support Class

Every load-bearing claim that is challenged for missing evidence must be assigned one primary support class:

```text
DEFINITIONAL
FORMAL_DERIVATION
THEORETICAL_STRUCTURAL
EMPIRICAL
PHYSICAL_EXISTENCE
HISTORICAL_DOCUMENTARY
GOVERNANCE_CONTROL
MIXED
UNCLASSIFIED
```

### DEFINITIONAL

A stipulative or constitutive definition.

Primary support requirement:
- explicit scope;
- type consistency;
- non-circularity;
- relation to authoritative definitions;
- internal consistency.

Empirical evidence is not automatically required merely to define the term.

### FORMAL_DERIVATION

A mathematical or logical derivation.

Primary support requirement:
- explicit premises;
- valid derivation/proof chain;
- type/domain correctness;
- reproducibility.

Empirical evidence is not automatically required for the validity of the formal derivation itself.

### THEORETICAL_STRUCTURAL

A theoretical mechanism, structural hypothesis, candidate relation, explanatory architecture, or necessity/sufficiency proposal that is not yet asserted as observed physical fact.

Primary support requirement may include:
- explicit premises;
- derivational or argumentative support;
- scope;
- necessary/sufficient distinction;
- consistency;
- countermodels;
- falsification/discriminant route where applicable.

Empirical evidence may be required for later promotion, but is not automatically required at the current candidate status.

### EMPIRICAL

A claim that an observed, measured, or experimentally tested effect exists or has a stated magnitude/pattern.

Primary support requirement:
- appropriate empirical evidence;
- method and provenance;
- uncertainty/control treatment;
- scope-matched inference.

### PHYSICAL_EXISTENCE

A claim that a proposed entity, field, state, mechanism, or relation exists physically in nature.

Primary support requirement:
- empirical/observational support appropriate to the claim;
- physical bridge/interpretation where applicable;
- alternative explanations controlled to the required scope.

A purely theoretical construction is insufficient for this claim class.

### HISTORICAL_DOCUMENTARY

A claim about what a source, repository, event, person, paper, or prior state contained or did.

Primary support requirement:
- documentary/source provenance;
- version/date identity where relevant.

### GOVERNANCE_CONTROL

A rule, status definition, workflow constraint, registry convention, or authority assignment.

Primary support requirement:
- explicit authority;
- provenance;
- internal consistency;
- non-conflict with higher authority.

Scientific empirical evidence is normally not applicable.

### MIXED

A statement containing more than one support class.

Mixed claims must be decomposed before a missing-evidence finding is assigned, unless decomposition is impossible and the reason is documented.

### UNCLASSIFIED

Temporary fail-closed state.

No missing-evidence defect may be assigned until the support class is determined.

---

## 4. Empirical Evidence Requirement

This is a separate control axis from Claim Status and Scientific Status.

Allowed values:

```text
NOT_APPLICABLE_TO_CURRENT_CLAIM
NOT_REQUIRED_AT_CURRENT_STATUS
REQUIRED_FOR_PROMOTION
REQUIRED_FOR_CURRENT_CLAIM
UNASSESSED
```

### NOT_APPLICABLE_TO_CURRENT_CLAIM

Empirical evidence is not the relevant support type for the claim as currently formulated.

Examples:
- governance rule;
- pure definition;
- formal theorem under stated premises.

### NOT_REQUIRED_AT_CURRENT_STATUS

Empirical evidence could become relevant later, but the present bounded claim does not require it.

### REQUIRED_FOR_PROMOTION

The current claim may stand at its present weaker status, but empirical evidence is required before promotion to a stronger empirical/physical/generalized status.

### REQUIRED_FOR_CURRENT_CLAIM

The present wording/status already makes an empirical or physical assertion. Appropriate evidence is required now.

### UNASSESSED

The requirement has not yet been classified.

No final missing-evidence finding may be issued while this field is `UNASSESSED`.

---

## 5. Evidence State

When empirical or documentary evidence is applicable, use:

```text
NOT_ASSESSED
SATISFIED
PARTIALLY_SATISFIED
MISSING
CONTRADICTED
NOT_APPLICABLE
```

Evidence State does not itself assign Claim Status.

---

## 6. Mandatory Evidence-Applicability Gate

Before writing:

```text
"there is no evidence"
"evidence is missing"
"unsupported"
"not evidenced"
```

as a defect or negative verdict, the assessor must record:

```text
CLAIM_ID
CLAIM_TEXT
CLAIM_SUPPORT_CLASS
CURRENT_CLAIM_STATUS
REQUIRED_SUPPORT_TYPE
EMPIRICAL_EVIDENCE_REQUIREMENT
EVIDENCE_STATE
CURRENT_STATUS_IMPACT
PROMOTION_IMPACT
SOURCE / EVIDENCE POINTERS
```

Allowed outcomes:

### A. NO CURRENT EVIDENCE DEFECT

```text
Empirical Evidence Requirement:
NOT_APPLICABLE_TO_CURRENT_CLAIM
or
NOT_REQUIRED_AT_CURRENT_STATUS
```

No missing-empirical-evidence finding is permitted.

Other defects may still exist, e.g. circularity, undefined terms, weak derivation, or missing provenance.

### B. PROMOTION BARRIER ONLY

```text
Empirical Evidence Requirement:
REQUIRED_FOR_PROMOTION

Evidence State:
MISSING or PARTIALLY_SATISFIED
```

The current weaker claim may remain valid as typed.

The absent evidence blocks only the named stronger transition.

### C. CURRENT CLAIM SUPPORT DEFECT

```text
Empirical Evidence Requirement:
REQUIRED_FOR_CURRENT_CLAIM

Evidence State:
MISSING
```

A missing-evidence finding is permitted and must identify the exact overreaching claim.

### D. CONTRADICTED

Evidence materially contradicts the current claim.

This is stronger than missing evidence and requires explicit source/evidence binding.

---

## 7. Theory-Development Rule

For a theoretical candidate, structural hypothesis, mechanism proposal, or necessity/sufficiency candidate:

```text
absence of empirical confirmation
!=
automatic theory defect
```

The appropriate immediate tests may instead be:

- premise validity;
- type consistency;
- derivation;
- necessary vs sufficient distinction;
- countermodel search;
- alternative hypothesis comparison;
- internal contradiction search;
- boundary/edge cases;
- falsification target;
- discriminant/prediction construction.

This does not permit a theoretical candidate to be presented as empirically established.

---

## 8. Audit Wording Rule

Prefer precise statements.

Incorrect or underspecified:

```text
There is no evidence for this.
```

Required form:

```text
Claim Support Class: THEORETICAL_STRUCTURAL
Empirical Evidence Requirement: REQUIRED_FOR_PROMOTION
Evidence State: MISSING
Current Status Impact: NONE
Promotion Impact: blocks promotion to Empirically Supported / physical existence claim
```

or:

```text
Claim Support Class: EMPIRICAL
Empirical Evidence Requirement: REQUIRED_FOR_CURRENT_CLAIM
Evidence State: MISSING
Current Status Impact: defect / wording must be weakened or evidence supplied
```

---

## 9. Relation to Canonicalization

A missing empirical-evidence item blocks Artifact Status `Canonical Artifact` only when:

1. empirical evidence is `REQUIRED_FOR_CURRENT_CLAIM`; and
2. the unsupported claim is load-bearing within the artifact's declared canonical scope; and
3. the defect is not repaired by narrowing/retyping the claim.

By contrast:

```text
REQUIRED_FOR_PROMOTION + MISSING
!=
automatic canonicalization blocker
```

A canonical artifact may accurately contain a theoretical candidate with open empirical validation, provided its status, scope, non-claims, and promotion boundary are explicit.

---

## 10. Adoption Rule

Repositories importing this control must:

1. classify claim support before raising missing-evidence defects;
2. keep empirical-evidence requirement separate from Claim Status and Scientific Status;
3. distinguish current-claim requirements from promotion requirements;
4. route theoretical challenges to derivation/countermodel/falsification/discriminant controls where appropriate;
5. prevent absent empirical confirmation from being treated as a generic defect in definitions, formal derivations, governance controls, or bounded theoretical candidates;
6. prevent candidate/theoretical wording from being silently promoted to empirical or physical fact.

This file governs evidence applicability. It does not create evidence and does not weaken evidence requirements where the current claim genuinely requires them.
