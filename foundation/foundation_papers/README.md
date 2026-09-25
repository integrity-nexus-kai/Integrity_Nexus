# Foundation Papers — Controlled Audit-Package Intake

Status: ACTIVE WORKING INTAKE / NOT CANONICAL
Version: v0.1
Repository: integrity-nexus-kai/Integrity_Nexus
Owner layer: Integrity Nexus meta-repository

## Purpose

This directory is the controlled collection point for the program-level Foundation Papers that must be reconciled before downstream construction, cross-paper integration, or external release.

It exists to assemble and audit the current four-paper corpus and to allow additional load-bearing Foundation Papers to be added without changing the collection architecture.

This directory is an intake, reconciliation, and audit-package location. Its existence does not promote any paper, claim, definition, relation, World Model, HT/HTMAX statement, or external-reference statement to canonical or proven status.

## Boundary

The collection is distinct from the domain-neutral Foundation Layer documents in the parent directory. A paper placed here is not thereby inserted into the universal Foundation Layer. Each paper retains its own scientific owner, scope, source binding, epistemic status, and audit status.

Human-readable main text is the primary review object. Technical claim registers, source manifests, status matrices, repair ledgers, and machine-readable audit records belong after the readable main text or in explicitly linked package artifacts.

## Current intake slots

| ID | Working object | Intake status |
|---|---|---|
| FOUNDATION-PAPER-01 | HTMAX evidence / performance foundation | INTAKE REQUIRED; exact source identity to freeze |
| FOUNDATION-PAPER-02 | Kristallisation des World Models / Gesamtpapier | INTAKE REQUIRED; R6 last usable readable basis; later R7 repair candidate withdrawn |
| FOUNDATION-PAPER-03 | Bidirektionale Nicht-Substituierbarkeit | INTAKE REQUIRED; source identity to freeze |
| FOUNDATION-PAPER-04 | Human Reference Pole Necessity | INTAKE REQUIRED; source identity to freeze |
| FOUNDATION-PAPER-05+ | Additional load-bearing Foundation Papers | RESERVED; add only with explicit scope and owner |

## Required intake record for every paper

Each paper must enter the package with:

1. exact filename and document type;
2. scientific/architectural owner;
3. version, date, and status;
4. source location and SHA-256;
5. readable main text;
6. technical appendix or machine-readable audit companion, if one exists;
7. claim list with epistemic classification;
8. definition and dependency bindings;
9. existing audit findings and repair state;
10. open questions, missing evidence, and release blockers.

## Package workflow

INTAKE → SOURCE FREEZE → HUMAN-READABLE REVIEW → CLAIM/DEFINITION RECONCILIATION → CROSS-PAPER CONSISTENCY AUDIT → REPAIR → FRESH AIL-1 RE-AUDIT → JOINT FREEZE → DOWNSTREAM RELEASE GATE

Materialisation, audit, and governance are separate states. A repaired file is not automatically audited; an audited file is not automatically proven; a repository-visible file is not automatically canonical.

## Cross-paper control

The package must maintain a contradiction and dependency register covering at least:

- terminology and type boundaries;
- World Model, Integrity State, Integrity Field, P1, Emergenz, Schutz, Timing, Bewusstsein, Human Reference Pole, HT, and HTMAX;
- claim direction and claim strength;
- source and authorship attribution;
- status transitions;
- downstream dependencies and blocked consumers;
- unresolved contradictions and alternative explanations.

## Prohibited transitions

- no silent harmonisation;
- no claim promotion through document polish;
- no transfer of status from one paper to another;
- no use of chronology or repository activity as proof by itself;
- no external release before the four-paper package passes its defined audit gates;
- no canonical pointer before explicit Human-Authority decision.

## Current package state

The collection point is initialized. The four papers are not yet declared jointly frozen, mutually consistent, audited, canonical, or release-ready. The next operation is source intake and freeze of the actual current versions.