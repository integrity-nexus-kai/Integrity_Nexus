# Discovery Engine Architecture

## Purpose

This document defines TIG-E as a universal discovery engine.

TIG-E is not limited to physics. Physics is the first reference domain. The engine itself is a domain-neutral architecture for structured discovery in complex search spaces.

## Core Mission

```text
TIG-E automates the governance of the discovery process, not the final scientific decision.
```

The engine structures inputs, classifies candidates, detects level errors, manages registries, prepares review queues, and preserves traceability.

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
- and possible domain assignments.

## Governance Layer

The Governance Layer applies:

- candidate admission rules,
- generator/projection testing,
- integrity checks,
- circularity checks,
- dependency checks,
- domain-boundary checks,
- and review routing.

## Registry Layer

The Registry Layer preserves state.

It stores:

- candidates,
- open questions,
- dependencies,
- decisions,
- rejected structures,
- emergent projections,
- and review status.

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
- or escalate.

## Repository Layer

Repository integration may create:

- draft pull requests,
- issue comments,
- registry updates,
- dependency maps,
- review reports,
- and change logs.

Direct canonical modification requires explicit review authorization.

## Domain Packs

Domain packs provide domain-specific ontologies, candidate types, evidence standards, and terminology.

Examples:

- physics,
- medicine,
- pharma,
- AI alignment,
- psychology,
- materials science,
- software architecture.

Domain packs are applications of the discovery engine. They do not define the engine itself.
