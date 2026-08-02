# Research Record and Disclosure Standard

## Purpose

This standard converts TRGS record, reproducibility, authorship, disclosure, and AI requirements into an artifact-level evidence record. It does not require empty data or code artifacts.

## Required Artifact Record

Every review-ready research or publication artifact must record:

```text
Artifact and version:
Responsible human:
Contributors and roles:
Source repository and fixed snapshot:
Claims and limitations:
Canonical bibliography path, or NOT APPLICABLE with reason:
Data availability, or NOT APPLICABLE with reason:
Code availability, or NOT APPLICABLE with reason:
Computational environment, parameters, inputs, seeds, and output provenance, or NOT APPLICABLE with reason:
Funding statement:
Competing-interest statement:
Ethics statement, or NOT APPLICABLE with reason:
Privacy and personal-data statement:
Security, dual-use, export-control, and safety statement:
License and intellectual-property boundary:
Material AI use:
Human verification performed:
Retention location and correction path:
Reviewer and review date:
```

Unknown information must be recorded as `NOT YET CONFIRMED`, not guessed. `NOT APPLICABLE` requires a reason.

## Material AI Use

Where AI materially affected an artifact, record the tool or model where known, task, research stage, data sensitivity, retained provenance, verification, limitations, and responsible human. Legacy use with incomplete session metadata must be labeled `INCOMPLETE LEGACY RECORD`.

## Retention

The fixed repository history or a documented external archive is the retention path. A correction must preserve the affected prior version where legally and technically possible and must link to `audit/post_publication_actions.md` when externally released material is affected.
