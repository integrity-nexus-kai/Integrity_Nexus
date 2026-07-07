# TIG-E Operations Protocol

## Purpose

This protocol defines the operational workflow for TIG-E as a universal discovery engine.

It specifies who does what, in which order, and under which governance constraints.

## Mission

```text
Automate the governance of discovery, not the final research result.
```

## Phase 1 — Input Submission

**Responsible:** Human researcher or external user.

The user submits:

- free text,
- research question,
- hypothesis,
- candidate,
- observation,
- issue,
- commit,
- or domain-specific problem statement.

The system must preserve expressive freedom at the input boundary.

## Phase 2 — Structuring Agent

**Responsible:** LLM / structuring agent.

The agent converts input into structured objects:

- Claim
- Assumptions
- Candidate structures
- Dependencies
- Open Questions
- Evidence requirements
- Possible generator/projection relations
- Domain context

## Phase 3 — Fundamentality Filter

**Responsible:** Governance agent.

The filter asks:

```text
Is this candidate being treated as a generator, or is it already a projection?
```

Output classifications include:

- Fundamental Candidate
- Candidate
- Emergent Projection
- Rejected
- Needs Evidence
- Needs Formalization
- Open Question

## Phase 4 — Integrity Filter

**Responsible:** Governance agent.

The filter checks for:

- circular reasoning,
- missing assumptions,
- inconsistent levels,
- domain-boundary violations,
- unresolved dependencies,
- contradictory claims,
- premature finalization,
- and invalid mixture of fundamental and emergent structures.

## Phase 5 — Candidate Registry Update

**Responsible:** Registry agent.

The registry records:

- candidate status,
- rationale,
- dependencies,
- open questions,
- rejection reasons,
- review status,
- and traceability links.

## Phase 6 — Review Queue

**Responsible:** Human researcher / designated reviewer.

TIG-E generates reviewable proposals only.

The reviewer decides whether a structure is accepted, rejected, deferred, split, merged, reclassified, or escalated.

## Phase 7 — GitHub Actions / CI Governance

**Responsible:** GitHub Actions.

Triggered by:

- pull request,
- issue update,
- candidate submission,
- registry edit,
- or domain-pack update.

Actions may run:

- Fundamentality Filter,
- Integrity Filter,
- Registry Check,
- Open Question Dependency Check,
- Documentation Consistency Check.

Actions may produce:

- CI status,
- review report,
- PR comment,
- issue label,
- registry-update suggestion,
- or blocked merge status.

Actions must not produce canonical scientific decisions without review authorization.

## Phase 8 — Repository Integration

**Responsible:** Repository workflow.

Outputs may include:

- draft pull requests,
- issue comments,
- registry updates,
- dependency maps,
- candidate records,
- open-question updates,
- and audit logs.

Direct canonical updates require explicit approval.

## Phase 9 — Emergence Cycle

Approved updates may create:

- new candidates,
- new dependencies,
- new questions,
- new domain-pack requirements,
- or new review routes.

The cycle then restarts.

## Operating Principles

1. Generator before projection.
2. Mark emergent structures; do not delete them.
3. Reduce search space before claiming solutions.
4. Automate governance, not truth.
5. Preserve traceability.
6. Keep universal foundation and domain application separate.
7. Require review before canonical promotion.

## Minimal MVP

The MVP requires:

- free input interface,
- structuring agent,
- fundamentality filter,
- integrity filter,
- candidate registry,
- review queue,
- GitHub Actions governance,
- repository output layer.
