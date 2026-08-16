# Auditor Master Prompt Workstream — Controlled Restart after AUD-00 R001 Closure

**Date:** 2026-08-16  
**Repository:** `integrity-nexus-kai/Integrity_Nexus`  
**Owner:** Kai Stefan Dietrich  
**Working front:** Strategy Main 3 / Claude / AUD-00 / operational auditor Master Prompts  
**Status:** ACTIVE — BASELINE CONTROL BEFORE PROMPT REGENERATION

---

## 1. Purpose

This record defines the controlled restart of the operational Auditor Master Prompt workstream after closure of AUD-00 finding R001.

The objective is to produce installable, internally coherent, governance-compliant Master Prompts for the operational auditors and to validate each prompt through an iterative author/reviewer loop before installation or operational use.

---

## 2. Root-cause context

A prior set of auditor Master Prompts had been generated while the underlying AUD-00 base paper was incorrect, unresolved, or not yet sufficiently reconciled.

Those prompts must **not** be treated as the authoritative authoring baseline for the new cycle.

They may be retained as historical evidence if needed, but they must not be silently repaired and represented as if they had been generated from the corrected governance baseline.

Protection rule:

`PROMPT GENERATED FROM INVALID / UNRESOLVED BASELINE ≠ VALID CURRENT CANDIDATE`

---

## 3. AUD-00 R001 gate status

Finding:

`AUD02-AUD00V09-TGCR-20260813-01-R001`

Targeted closure audit:

`AUD02-AUD00V10-TCR-20260816-01`

Repository closure record:

`audit/AUD02_AUD00V10_R001_closure_verification_2026-08-16.md`

Current controlled result:

`R001 = AUDIT-CLOSED`

Scope boundary:

- governance-text closure for R001 and its defined direct regression surface;
- no runtime implementation verification;
- no external independent assurance;
- no Ratification;
- no Bootstrap-Hold release;
- no automatic Canonical promotion.

---

## 4. Required baseline sequence before new auditor prompts

The next valid sequence is:

1. preserve R001 closure and primary-evidence provenance in the repository;
2. Program Owner makes the separate baseline/status decision permitted by the governance model;
3. synchronize the AUD-00 Governance Artifact with the governing AUD-00 Master Prompt;
4. freeze and identify the correct post-closure AUD-00 authoring baseline;
5. only then issue a new Claude authoring instruction for operational auditor Master Prompts;
6. old prompts generated from the wrong/unresolved baseline are not used as the new source-of-truth.

No step may be silently skipped.

---

## 5. Auditor Master Prompt validation loop

For each operational auditor, work proceeds sequentially unless an explicit dependency analysis permits otherwise.

### Authoring / correction side

Claude produces the complete current Master Prompt from the controlled baseline.

### Independent internal review side

Strategy Main 3 audits the complete candidate against:

- AUD-00 governance rules;
- role identity and scope;
- authority boundaries;
- provenance requirements;
- independence disclosures;
- evidence discipline;
- finding / severity / confidence logic;
- closure semantics;
- fail-closed behavior;
- cross-auditor dependencies;
- domain-routing boundaries;
- installation completeness;
- regression surface introduced by corrections.

### Correction cycle

If material defects remain:

1. Strategy Main 3 identifies the exact defect;
2. only the smallest necessary correction delta is requested;
3. Claude returns the **complete revised Master Prompt**, not fragments;
4. Strategy Main 3 re-audits the corrected findings plus their direct regression surface;
5. repeat until material closure.

Protection rules:

- Claude `PASS` or `FIXED` labels are not closure evidence by themselves.
- Text modification is not closure by itself.
- No broad redesign when a local delta suffices.
- No prompt is represented as validated or installable before its audit cycle closes.
- The user is not manual middleware assembling fragments.

---

## 6. Output integrity rule

Every Claude authoring or correction instruction must request one complete, self-contained current Master Prompt.

Every Strategy Main 3 correction instruction returned to Claude must be one complete, self-contained work order.

No workflow step may require the Program Owner to manually merge prompt fragments.

---

## 7. Repository trace requirements per auditor

For each auditor prompt that enters the controlled cycle, the repository record should preserve at minimum:

- auditor ID / canonical role;
- candidate version;
- source baseline identity and hash where available;
- authoring model/provider;
- candidate artifact path;
- audit/review record;
- findings;
- correction version transition;
- closure verification;
- residual limitations;
- installation/readiness status;
- downstream dependencies.

Where feasible, immutable hashes of frozen prompt candidates and review targets should be retained.

---

## 8. Status semantics

The following distinctions are mandatory:

`DRAFT / CANDIDATE ≠ VALIDATED`

`VALIDATED FOR INTERNAL SCOPE ≠ EXTERNALLY INDEPENDENT`

`AUDIT-CLOSED FINDING ≠ RATIFIED ARTIFACT`

`RATIFIED ≠ CANONICAL` unless the applicable governance explicitly establishes that transition.

No status promotion occurs by implication.

---

## 9. Current next action

The workstream is currently positioned **before new auditor-prompt generation**.

Immediate next action:

`PROGRAM-OWNER BASELINE/STATUS DECISION -> AUD-00 MASTER-PROMPT / GOVERNANCE-ARTIFACT SYNCHRONIZATION -> FREEZE CORRECT AUTHORING BASELINE`

Only after that sequence is recorded may Claude be instructed to regenerate the operational auditor Master Prompts from the correct baseline.

---

## 10. Historical preservation

Previously generated prompts from the invalid/unresolved baseline are not deleted by this record.

If retained, they are historical artifacts only and must be labelled so that no later workflow can mistake them for current validated candidates.

Negative knowledge is preserved:

**The prior prompt-generation run is evidence that an apparently complete downstream artifact set can be invalidated by an unresolved upstream governance baseline.**

This dependency lesson is part of the audit trail and must not be lost.
