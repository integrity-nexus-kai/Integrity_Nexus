# Domain Packs

Domain packs define concrete applications of the universal TIG-E discovery architecture.

The Foundation Layer defines domain-neutral principles. Domain packs translate those principles into specific candidate ontologies, evidence standards, terminology, registries, and review rules.

## Current / Planned Domain Packs

- `physics/` — first reference implementation; includes Integrity Field, field-equation work, physics candidates, and physics open questions.
- `pharma/` — future application domain for molecular and biomedical search spaces.
- `ai_alignment/` — future application domain for AI safety and governance problems.
- `psychology/` — future application domain for psychological and behavioral model spaces.
- `materials/` — future application domain for material-property search spaces and structural candidates.

## Core Rule

```text
Domain packs apply the Foundation Layer. They do not redefine it.
```

A domain-specific primitive may be fundamental within its domain model, but it must not be promoted into the universal Foundation Layer without explicit foundation-level review.

## Separation Principle

```text
Foundation is universal.
Domain packs are applications.
```

This directory is a routing layer, not a final taxonomy.
