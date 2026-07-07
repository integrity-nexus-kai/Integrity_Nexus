# GitHub Actions Governance Specification

## Locked Mode Scope

This document defines the automation specification for GitHub Actions within the TIG-E discovery architecture.

It does not define scientific truth, promote candidates, create domain theory, or authorize automated canonization.

## Purpose

GitHub Actions may be used as a CI governance layer for Integrity Nexus and TIG-E workflows.

Its role is to enforce structural discipline, detect missing review conditions, preserve layer separation, and generate auditable reports.

## Mission

```text
Automate governance checks.
Do not automate final research authority.
```

## Trigger Events

GitHub Actions may run on:

- pull request opened or updated,
- issue opened or updated,
- candidate registry edit,
- open-question registry edit,
- foundation document edit,
- domain-pack update,
- operations protocol update,
- governance document update,
- scheduled audit run,
- or manual workflow dispatch.

## Required Checks

### 1. Foundation / Domain Separation Check

Detect whether domain-specific content is being inserted into the universal Foundation Layer without explicit foundation-level abstraction.

Blocked examples:

- treating a physics variable as universal primitive,
- inserting Integrity Field details into Foundation,
- treating a domain equation as a general engine rule,
- promoting a reference-domain concept into the meta-architecture without review.

### 2. Candidate Status Check

Ensure that candidate-bearing changes declare or update status.

Allowed status classes include:

- Fundamental Candidate,
- Candidate,
- Emergent Projection,
- Rejected,
- Needs Evidence,
- Needs Formalization,
- Open Question,
- Review Required.

### 3. Locked Mode Boundary Check

Check that documents do not violate core Locked Mode boundaries:

```text
Candidate ≠ final.
Partial ≠ complete.
Effective ≠ fundamental.
Source-like ≠ physical stress-energy.
Metric-like ≠ spacetime metric.
Compatibility ≠ derivation.
Automation ≠ authority.
Registry status ≠ truth claim.
```

### 4. Dependency Check

Detect whether a claim depends on unresolved open questions, missing prerequisites, or unregistered assumptions.

If dependencies are unresolved, the workflow must mark the change as review-required.

### 5. Registry Consistency Check

Ensure that changes affecting research state are reflected in an appropriate registry or explicitly marked as non-canonical.

```text
If a structure affects research state, it must be registered or explicitly marked non-canonical.
```

### 6. Review Status Check

Ensure that canonical changes require explicit human review.

Automated checks may approve structure, formatting, and consistency readiness.

They must not approve scientific truth.

### 7. Documentation Consistency Check

Check that cross-references, document lists, layer names, and core principles remain consistent across:

- `META_REPO_STRUCTURE.md`,
- `foundation/README.md`,
- `foundation/01_foundation_index.md`,
- `domains/README.md`,
- `operations/README.md`,
- and relevant registry or governance files.

## Outputs

GitHub Actions may produce:

- pass/fail CI status,
- warning status,
- review-required status,
- PR comment,
- issue label,
- audit report,
- registry-update suggestion,
- dependency report,
- or blocked merge status.

## Merge Blocking Conditions

A merge may be blocked if:

- domain-specific material is inserted into Foundation without review,
- a candidate is introduced without status,
- a claim lacks required dependency references,
- an unresolved open question is bypassed,
- a registry-affecting change has no registry update or non-canonical marker,
- a Locked Mode boundary is violated,
- or required human review is absent.

## Non-Blocking Conditions

The workflow may warn without blocking when:

- wording is imprecise but not structurally dangerous,
- a document needs cross-reference cleanup,
- a candidate is mentioned only historically,
- a registry update is recommended but not required,
- or a change affects commentary but not research state.

## Human Review Authority

Human review is required for:

- canonical promotion,
- candidate status upgrade,
- foundation-level abstraction,
- domain-pack ontology changes,
- publication-readiness decisions,
- and any claim that changes the scientific or methodological state of the ecosystem.

## Minimal MVP Workflows

The first automation MVP should implement:

1. Foundation / Domain Separation Check.
2. Candidate Status Check.
3. Locked Mode Boundary Check.
4. Registry Consistency Check.
5. Review Status Check.

The MVP may start with text-pattern and metadata checks before adding more advanced semantic analysis.

## Future Extensions

Future workflows may add:

- LLM-based structuring reports,
- automatic dependency-map proposals,
- candidate registry draft generation,
- open-question routing,
- domain-pack consistency checks,
- reviewer assignment suggestions,
- audit dashboards,
- and release-readiness gates.

## Governance Rule

```text
GitHub Actions may block, warn, route, label, report, or draft.
GitHub Actions may not canonize, prove, derive, or decide final research truth.
```

## Current Status

This specification is v0.1.

It defines the intended automation governance layer. It is not yet an implemented workflow file.
