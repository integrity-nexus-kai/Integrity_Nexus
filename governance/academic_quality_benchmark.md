# Academic Research Governance Quality Benchmark

## Status and Purpose

```text
Status: CONTROLLED REVIEW BASIS
Version: 1.0
Scope: Integrity Nexus Meta-Repository and the eight-repository governance architecture
Claim Type: Governance benchmark
Dependencies: Official sources listed in governance/references.bib
Scientific effect: NONE
```

This benchmark operationalizes the requested Harvard-/Princeton-level quality target. It does not claim institutional affiliation, endorsement, certification, or literal identity with any university policy system.

Harvard and Princeton are used as leading institutional reference points. The operational baseline is strengthened by international and discipline-neutral standards for research integrity, publication ethics, openness, data stewardship, contributorship, citation metadata, and responsible AI use.

---

## Benchmark Matrix

| ID | Required control | External benchmark basis | Required Integrity Nexus evidence | Fixed-snapshot candidate state |
|---|---|---|---|---|
| AQB-01 | Reliability, honesty, respect, accountability | `allea2023researchIntegrity`; `dfg2025goodResearchPractice` | TRGS fundamental principles; claim/evidence boundaries | PRESENT IN CANDIDATE |
| AQB-02 | Clear authority, scope, roles, and accountable collaboration | `harvardRCRResources`; `princetonResearchIntegrity`; `dfg2025goodResearchPractice` | Constitution; subrepo protocol; ownership and dependency records | PRESENT |
| AQB-03 | Separation of claims, evidence, interpretation, uncertainty, and status | `allea2023researchIntegrity`; `cosTOP2025`; `dfg2025goodResearchPractice` | Claim taxonomy; claim-boundary standards; evidence paths | PRESENT IN CANDIDATE |
| AQB-04 | Verifiable literature and citation metadata | `cffSchema120`; `allea2023researchIntegrity`; `dfg2025goodResearchPractice` | Citation standard; repository-local and publication-local bibliography rules | PRESENT IN CANDIDATE |
| AQB-05 | Research-record preservation and provenance | `harvardRCRResources`; `princetonResearchIntegrity`; `dfg2025goodResearchPractice`; `goFairPrinciples` | Fixed snapshots; version history; evidence paths; retention and correction rules | PRESENT IN CANDIDATE |
| AQB-06 | Data, code, material, and computational reproducibility | `cosTOP2025`; `goFairPrinciples`; `copeCorePractices`; `dfg2025goodResearchPractice` | Reproducibility requirements; access restrictions; metadata and provenance | PRESENT IN CANDIDATE |
| AQB-07 | Authorship, contributorship, and accountability | `harvardRCRResources`; `nisoCredit2022`; `copeCorePractices` | AUTHOR/CITATION records; contributor-role and human-responsibility rules | PRESENT IN CANDIDATE |
| AQB-08 | Funding, competing interests, ethics, privacy, security, and IP | `harvardRCRResources`; `princetonResearchIntegrity`; `allea2023researchIntegrity`; `copeCorePractices` | Publication checklist; disclosure and restriction rules | PRESENT IN CANDIDATE |
| AQB-09 | Independent, competent, confidential, conflict-aware review | `harvardRCRResources`; `copeCorePractices`; `dfg2025goodResearchPractice` | Audit protocol; reviewer independence and conflict rules | PRESENT IN CANDIDATE |
| AQB-10 | Misconduct handling, fair process, evidence preservation, and non-retaliation | `harvardRCRResources`; `princetonResearchIntegrity`; `allea2023researchIntegrity`; `dfg2025goodResearchPractice` | TRGS integrity procedure; audit record; independent review requirement | PRESENT IN CANDIDATE |
| AQB-11 | Corrections, withdrawal/retraction, and post-publication maintenance | `copeCorePractices`; `allea2023researchIntegrity`; `dfg2025goodResearchPractice` | Versioned correction rule; publication pipeline; audit log | PRESENT IN CANDIDATE |
| AQB-12 | Responsible and disclosed AI assistance with human accountability | `ecResponsibleGenAIResearch`; `cffSchema120` | TRGS AI controls; publication checklist; source-level verification | PRESENT IN CANDIDATE |
| AQB-13 | Transparent repository conformance without scientific status inflation | `dfg2025goodResearchPractice`; `allea2023researchIntegrity`; Integrity Nexus authority model | Conformance register; sole synchronization authority preserved | PRESENT IN CANDIDATE |
| AQB-14 | Competence, state-of-the-art review, safeguards, risk mitigation, and accountable collaboration | `allea2023researchIntegrity`; `harvardRCRResources`; `dfg2025goodResearchPractice` | TRGS sections 2, 5, and 6; literature and review requirements | PRESENT IN CANDIDATE |

---

## Assessment Rules

Allowed assessments:

```text
ABSENT
PARTIAL
PRESENT IN CANDIDATE
PRESENT
NOT APPLICABLE
```

`PRESENT IN CANDIDATE` means the control exists in the review snapshot but has not yet passed independent audit and author approval.

The implementation preflight is evidence-based. Rule text by itself is not implementation evidence. The initial preflight found one control `PRESENT` and thirteen controls `PARTIAL`. The direct-main correction at fixed content snapshot `cd642ee0d1173f32b8c6eca32ba086cbce21e921` provides implementation evidence for all fourteen controls and has passed an internal AIL-0 technical recheck. Independent audit and author approval remain separate later gates.

An item passes only when:

1. the rule is explicit;
2. its authority and scope are clear;
3. an implementation or evidence path exists;
4. non-applicable cases are handled without empty artifacts;
5. the rule does not inflate scientific status;
6. conflicts and exceptions are recorded;
7. the fixed snapshot can be independently checked.

---

## Approval Boundary

The benchmark is a review instrument, not an accreditation. A completed matrix supports an internal governance verdict only. It does not authorize claims of Harvard, Princeton, ALLEA, DFG, COPE, or other institutional approval.
