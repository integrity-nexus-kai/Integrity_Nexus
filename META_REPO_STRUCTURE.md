# Meta-Repo Structure

Integrity Nexus is the meta-repository for the integrity-oriented research ecosystem.

It does not replace domain repositories. It provides the universal navigation, governance, registry, operations, and foundation architecture that keeps the ecosystem coherent.

## Top-Level Structure

```text
foundation/     universal discovery principles and TIG-E kernel documents
domains/        domain packs applying the Foundation Layer to specific problem spaces
operations/     execution workflows, review process, automation, and CI governance
registry/       candidates, open questions, dependencies, decisions, and status maps
governance/     canonical rules, claim boundaries, review standards, and integrity rules
```

## Layer Logic

```text
Foundation Layer
    ↓
Domain Packs
    ↓
Operations / Registry / Governance
    ↓
Concrete Research Artifacts
```

## Separation Principle

```text
The meta-repository defines the discovery architecture.
Domain repositories and domain packs apply it.
```

The physics program is the first reference implementation. It is not identical with the universal TIG-E discovery engine.

## Current Priority

The immediate priority is to establish the Foundation Layer, then connect it to operations, registries, GitHub Actions, and the physics reference domain.
