# Bottleneck Detection Architecture

**Status:** Working foundation architecture  
**Repository authority:** Integrity Nexus  
**Author:** Kai Stefan Dietrich  
**Date:** 2026-08-06

---

## 1. Purpose

This document defines Bottleneck Detection as a recursive prioritization mechanism within the TIG-E research architecture.

It does not claim that every difficult or unresolved problem is a bottleneck. It defines how the currently dominant obstruction to admissible progress may be identified, tested, selected, revised, or rejected.

---

## 2. Working Definition

> **A bottleneck is the currently dominant unresolved dependency, ambiguity, missing structure, contradiction, or constraint whose clarification or resolution is expected to produce the greatest admissible reduction in uncertainty, search-space size, or blocked downstream work.**

Bottleneck status is always relative to:

- the active scope;
- the target state;
- the current system state;
- available evidence;
- dependency order;
- resource limits;
- and repository authority.

---

## 3. What a Bottleneck Is Not

```text
Bottleneck ≠ every open problem
Bottleneck ≠ the largest visible task
Bottleneck ≠ the most interesting question
Bottleneck ≠ the most difficult question
Bottleneck ≠ the preferred solution
Bottleneck ≠ a symptom automatically
```

A local difficulty may be important without being the dominant bottleneck of the wider system.

---

## 4. Bottleneck Classes

### 4.1 Epistemic Bottleneck

A missing explanation, definition, distinction, or evidence relation prevents reliable understanding.

### 4.2 Structural Bottleneck

A missing architecture, dependency map, object boundary, or formal relation blocks downstream construction.

### 4.3 Methodological Bottleneck

A research mechanism exists in practice but is not yet explicit, operationalized, or auditable.

### 4.4 Governance Bottleneck

Authority, status, scope, claim boundaries, or transition rules are insufficiently defined.

### 4.5 Validation Bottleneck

A candidate cannot progress because required evidence, derivation, proof obligation, test, or audit is missing.

### 4.6 Implementation Bottleneck

A required software, data, workflow, integration, or execution capability is absent.

### 4.7 Cognitive-Infrastructure Bottleneck

Work is slowed or destabilized by memory loss, repeated reconstruction, inaccessible context, asset fragmentation, or cognitive overload.

---

## 5. Scope and Priority Distinctions

The architecture distinguishes:

```text
local bottleneck        ↔ ecosystem bottleneck
primary bottleneck      ↔ secondary bottleneck
active bottleneck       ↔ parked bottleneck
actual bottleneck       ↔ apparent symptom
upstream bottleneck     ↔ downstream bottleneck
temporary bottleneck    ↔ persistent bottleneck
```

Multiple bottlenecks may coexist, but only one should be designated as the active primary bottleneck within a controlled work scope unless explicit parallelization is justified.

---

## 6. Detection Cycle

```text
Current System State
        ↓
Bottleneck Candidate Detection
        ↓
Dependency and Impact Analysis
        ↓
Candidate Comparison
        ↓
Active Bottleneck Selection
        ↓
Constraint Extraction
        ↓
Focused Search-Space Compression
        ↓
Targeted Work
        ↓
Changed System State
        ↓
Bottleneck Re-Detection
        ↺
```

Bottleneck Detection is therefore not a one-time stage. It is a recursive steering function.

---

## 7. Candidate Detection Sources

Bottleneck candidates may be detected through:

- unresolved dependency chains;
- repeated failure at the same transition;
- contradictory source authority;
- inability to state the next admissible action;
- missing definitions or object identities;
- excessive search-space growth;
- repeated manual reconstruction;
- audit findings;
- stalled downstream work;
- unformalized intuition signals;
- or recurring requests for an absent mechanism, artifact, or decision.

---

## 8. Intuition as Bottleneck Sensor

Intuition may act as an early low-authority sensor that a bottleneck exists.

```text
Intuitive Signal
        ↓
Possible Bottleneck Record
        ↓
State Reconstruction
        ↓
Dependency and Impact Analysis
        ↓
Confirm / Revise / Reject / Park
```

An intuitive sense of blockage does not itself establish bottleneck status.

The candidate must be reconstructed and compared against plausible alternatives.

---

## 9. Bottleneck Selection Criteria

A bottleneck candidate gains priority when its resolution is expected to:

- release multiple blocked dependencies;
- substantially compress the active search space;
- reduce repeated errors or ambiguity;
- improve evidence discrimination;
- restore reliable continuation;
- increase cross-repository coherence;
- prevent premature claim escalation;
- or unlock a required validation or canonicalization step.

Selection must consider both expected impact and confidence in the diagnosis.

---

## 10. Bottleneck Record

```yaml
bottleneck_record:
  bottleneck_id: BN-YYYY-NNNN
  scope: ""
  detected_from: []
  candidate_type: epistemic | structural | methodological | governance | validation | implementation | cognitive_infrastructure
  affected_objects: []
  blocked_dependencies: []
  expected_release_value: ""
  competing_bottlenecks: []
  known_constraints: []
  evidence_for_selection: []
  evidence_against_selection: []
  current_status: candidate
  selected_as_primary: false
  next_test: ""
  re_detection_trigger: ""
```

This schema is an initial candidate and requires later Runtime alignment.

---

## 11. Internal Observational Case Series

The following pattern has been observed within the TIG-E development process:

```text
Unexplained gravitation
→ epistemic bottleneck

Missing product definition
→ architectural bottleneck

Missing software architecture
→ implementation bottleneck

Missing asset preservation
→ cognitive-infrastructure bottleneck

Unoperationalized emergence
→ methodological bottleneck

Unseparated crystallization meanings
→ conceptual and governance bottleneck

Unoperationalized intuition
→ epistemic-methodological bottleneck

Missing externalized cognition model
→ cognitive-architecture bottleneck
```

This recurrence supports registration of Bottleneck Detection as a methodological candidate.

It does not prove universal reliability, causal necessity, or cross-domain superiority.

---

## 12. False Bottleneck Risks

A bottleneck diagnosis may be wrong when:

- the visible problem is only a downstream symptom;
- the selected problem is emotionally salient but structurally secondary;
- one domain's priority is imposed on the whole ecosystem;
- a familiar problem is preferred over a more consequential hidden dependency;
- resource scarcity is confused with conceptual necessity;
- recent events dominate attention without impact analysis;
- or the candidate is protected from comparison by intuition, authority, or prior investment.

---

## 13. Validation Strategy

A bottleneck diagnosis should be tested by asking:

1. Which downstream objects become actionable if this is resolved?
2. Which dependencies remain blocked even after resolution?
3. Does the active search space materially shrink or clarify?
4. Is the problem upstream or merely visible?
5. Are there competing bottlenecks with greater release value?
6. Can another reviewer reconstruct the diagnosis?
7. Does targeted work change the system state as predicted?
8. After intervention, does the bottleneck disappear, move, or persist?

A diagnosis should be revised when the predicted release does not occur.

---

## 14. Relationship to Signal-to-Noise Optimization

Bottleneck Detection identifies where intervention is expected to improve the research signal-to-noise ratio most strongly.

```text
Signal-to-Noise Objective
        ↓
Bottleneck Detection
        ↓
Priority Selection
        ↓
Focused Compression and Work
```

It is therefore the principal prioritization mechanism of the structured discovery cycle.

---

## 15. Current Status

- **Bottleneck definition:** working candidate;
- **Class taxonomy:** working candidate;
- **Recursive steering role:** methodologically supported by internal observation;
- **Selection metric:** not formalized;
- **Cross-domain reliability:** open;
- **Comparative validation:** open;
- **Runtime schema:** initial candidate;
- **Universal law claim:** not made.

---

## 16. Governing Statement

> Do not ask only what is unresolved. Ask which unresolved structure currently prevents the greatest amount of admissible progress.
