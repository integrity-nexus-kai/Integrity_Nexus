# Architecture

## Separation principle

The target repository is deliberately stratified so provenance and epistemic status remain visible in the filesystem.

- `00_GOVERNANCE/` — authority, status axes, claim discipline, source registration, notation, change control, open questions, decisions.
- `01_SOURCE_CORPUS/` — source artifacts exactly as received/acquired, with provenance; placement does not imply endorsement or truth.
- `02_MATHEMATICAL_FOUNDATIONS/` — reconstructed classical baseline with theorem conditions and source traceability.
- `03_RESEARCH_PROGRAM/` — research questions, strategy families, hypotheses, proof-obligation maps, negative-result tracking.
- `04_COMPUTATION/` — reproducible code, data, precision settings, and computational evidence.
- `05_PROOF_ATTEMPTS/` — original derivations and proof attempts; inactive until Phase 0/1 gates pass.
- `06_AUDIT_AND_RESULTS/` — mathematical audits, contradiction tests, refutations, closure records, stabilized bounded results.

## Knowledge classes

- **A — Classical mathematics**
- **B — External research programmes**
- **C — Nexus/TIG-origin hypotheses**

Class C must never retroactively redefine Class A. Any C→A relation is a separate bridge object with premises, scope, and proof obligations.

## Promotion rule

No directory, filename, merge, audit result, computational result, or author preference promotes a mathematical claim automatically.