# Discovery Engine Architecture

## Locked Mode Scope

This document defines the architecture of TIG-E as a universal discovery engine.

It does not define a domain theory, prove any result, select any ontology, or promote any candidate into canonical status.

## Purpose

TIG-E is a domain-neutral architecture for structured discovery in complex search spaces.

Physics is the first reference domain. It is not identical with the engine itself.

## Core Mission

```text
TIG-E automates the governance of the discovery process, not the final scientific decision.
```

The engine structures inputs, classifies candidates, detects level errors, manages registries, prepares review queues, supports search-space compression, and preserves traceability.

## High-Level Architecture

```text
Free Input
  ↓
Structuring Agent
  ↓
Fundamentality Filter
  ↓
Integrity Filter
  ↓
Candidate Registry
  ↓
Search Space Compression
  ↓
Emergence Protocol
  ↓
Review Queue
  ↓
Repository Integration
```

## Input Layer

TIG-E accepts flexible input:

- free text,
- research questions,
- hypotheses,
- mathematical proposals,
- observations,
- code commits,
- GitHub issues,
- paper fragments,
- or domain-specific candidate submissions.

The system must not require expert formatting at the input boundary.

Instead, it translates free input into structured research objects.

## Structuring Layer

The Structuring Agent extracts:

- claims,
- assumptions,
- candidates,
- dependencies,
- open questions,
- evidence requirements,
- generator/projection relations,
- domain assignments,
- and review risks.

Structuring is not validation.

```text
Structured ≠ accepted.
Extracted ≠ true.
```

## Governance Layer

The Governance Layer applies:

- candidate admission rules,
- generator/projection testing,
- integrity checks,
- circularity checks,
- dependency checks,
- domain-boundary checks,
- and review routing.

Governance does not create final results. It controls whether a structure may proceed to review, registry update, or further compression.

## Registry Layer

The Registry Layer preserves state.

It stores:

- candidates,
- open questions,
- dependencies,
- decisions,
- rejected structures,
- emergent projections,
- review status,
- and traceability links.

Registry status is a workflow state, not a truth claim.

## Search Space Compression Layer

The compression layer reduces or clarifies the active search space by removing, marking, or routing invalid, premature, circular, redundant, or misplaced paths.

Each iteration must either:

- reduce the search space,
- clarify its structure,
- expose a dependency,
- or route a decision to review.

## Emergence Layer

The Emergence Protocol may propose new candidate structures only after sufficient structuring, filtering, registry classification, and search-space compression.

Emergent outputs remain candidates.

```text
Emergence produces reviewable proposals, not canonical results.
```

## Review Layer

TIG-E does not finalize truth claims.

It prepares structured decisions for human review.

The reviewer decides whether to:

- accept,
- reject,
- defer,
- split,
- merge,
- reclassify,
- request evidence,
- request formalization,
- or escalate.

## Repository Layer

Repository integration may create:

- draft pull requests,
- issue comments,
- registry updates,
- dependency maps,
- review reports,
- change logs,
- and CI status outputs.

Direct canonical modification requires explicit review authorization.

## Domain Packs

Domain packs provide domain-specific ontologies, candidate types, evidence standards, terminology, registries, and review rules.

Examples:

- physics,
- pharma,
- medicine,
- AI alignment,
- psychology,
- materials science,
- software architecture.

Domain packs are applications of the discovery engine. They do not define the engine itself.

## Locked Mode Constraint

```text
Engine ≠ domain theory.
Workflow state ≠ truth claim.
Candidate ≠ final.
Emergence ≠ proof.
Automation ≠ scientific authority.
```

The architecture accelerates structured review. It does not bypass review.
