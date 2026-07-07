# TIG-E Operations Protocol

## Purpose

This document defines the operational workflow of TIG-E as a universal discovery engine.

It describes who or what acts at each stage, what is produced, what is reviewed, and what may be written back into the repository ecosystem.

## Mission

```text
TIG-E automates discovery governance, not final discovery claims.
```

The system does not replace the researcher. It structures the research process so that claims, candidates, dependencies, risks, and review decisions remain explicit and auditable.

## Operational Phases

### Phase 1 — Research Input

**Responsible:** Human researcher or authorized domain user.

Input may be free text, hypothesis, open question, candidate proposal, code commit, paper fragment, observation, or domain-specific research object.

### Phase 2 — Structuring Agent

**Responsible:** LLM / structuring agent.

The input is transformed into a structured object containing claim, assumptions, candidates, dependencies, open questions, evidence needs, generator/projection hypotheses, domain classification, and review risks.

### Phase 3 — Fundamentality Filter

**Responsible:** Governance agent.

The system tests whether each candidate is proposed as generator, projection, emergent structure, unresolved candidate, or invalid structure. Emergent candidates are marked, not deleted.

### Phase 4 — Integrity Filter

**Responsible:** Governance agent.

The system checks circular reasoning, level errors, dependency violations, missing assumptions, unsupported claims, inconsistent terminology, and invalid movement between universal and domain-specific layers.

### Phase 5 — Registry Update Draft

**Responsible:** Registry agent.

The system prepares draft updates for candidate registry, open-question registry, dependency map, decision log, review queue, and rejected/emergent structure records.

### Phase 6 — Review Queue

**Responsible:** Human reviewer / researcher.

The reviewer may accept, reject, defer, split, merge, reclassify, request evidence, or escalate. No agent may promote an output to canonical status without review authorization.

### Phase 7 — Repository Integration

**Responsible:** GitHub Actions / repository governance.

Repository integration may create draft pull requests, issue comments, status labels, registry update proposals, audit reports, dependency reports, and change logs. Direct canonical modification requires explicit authorization.

### Phase 8 — Emergence Cycle

Accepted or deferred structures may generate new candidates, open questions, dependencies, domain-pack updates, or foundation-level review needs. The process then restarts.

## GitHub Actions Role

GitHub Actions may act as CI governance.

It may automatically run structuring checks, fundamentality checks, integrity checks, registry consistency checks, dependency checks, and review-status checks.

It may block merge when a candidate is unclassified, a dependency is missing, a circular claim is detected, domain-specific material is inserted into the Foundation Layer, or required review is absent.

GitHub Actions does not decide scientific truth.

## Role Separation

### Human Researcher

Responsible for direction, prioritization, judgment, domain interpretation, and final decisions.

### TIG-E Agents

Responsible for structuring, filtering, consistency checking, registry drafting, and search-space compression.

### Repository Infrastructure

Responsible for traceability, versioning, workflow control, audit visibility, and canonical-state protection.

## Core Governance Rule

```text
No automated process may convert a candidate into a canonical result without an explicit review decision.
```

TIG-E accelerates the path to structured review. It does not bypass review.
