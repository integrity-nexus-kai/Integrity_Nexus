# TIG-E Operations Protocol

## Locked Mode Scope

This protocol defines the operational workflow for TIG-E as a universal discovery engine.

It does not authorize automated canonization, final research decisions, or domain-theory creation.

## Purpose

This protocol specifies who or what acts at each stage, what is produced, what is reviewed, and what may be written back into the repository ecosystem.

## Mission

```text
Automate the governance of discovery, not the final research result.
```

## Phase 1 — Input Submission

**Responsible:** Human researcher or authorized domain user.

The user submits:

- free text,
- research question,
- hypothesis,
- candidate,
- observation,
- issue,
- commit,
- paper fragment,
- or domain-specific problem statement.

The system must preserve expressive freedom at the input boundary.

## Phase 2 — Structuring Agent

**Responsible:** LLM / structuring agent.

The agent converts input into structured objects:

- claim,
- assumptions,
- candidate structures,
- dependencies,
- open questions,
- evidence requirements,
- possible generator/projection relations,
- domain context,
- and review risks.

Structuring does not validate the claim.

```text
Extracted ≠ accepted.
Structured ≠ true.
```

## Phase 3 — Fundamentality Filter

**Responsible:** Governance agent.

The filter asks:

```text
Is this candidate being treated as a generator, or is it already a projection?
```

Output classifications include:

- Fundamental Candidate,
- Candidate,
- Emergent Projection,
- Rejected,
- Needs Evidence,
- Needs Formalization,
- Open Question,
- Review Required.

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
- unsupported escalation,
- and invalid mixture of fundamental and emergent structures.

## Phase 5 — Candidate Registry Update Draft

**Responsible:** Registry agent.

The registry draft records:

- candidate status,
- rationale,
- dependencies,
- open questions,
- rejection reasons,
- review status,
- evidence status,
- formalization status,
- and traceability links.

Registry drafts are not canonical until reviewed.

## Phase 6 — Review Queue

**Responsible:** Human researcher / designated reviewer.

TIG-E generates reviewable proposals only.

The reviewer decides whether a structure is:

- accepted,
- rejected,
- deferred,
- split,
- merged,
- reclassified,
- escalated,
- returned for evidence,
- or returned for formalization.

## Phase 7 — GitHub Actions / CI Governance

**Responsible:** GitHub Actions.

Triggered by:

- pull request,
- issue update,
- candidate submission,
- registry edit,
- foundation edit,
- or domain-pack update.

Actions may run:

- Fundamentality Filter,
- Integrity Filter,
- Registry Check,
- Open Question Dependency Check,
- Documentation Consistency Check,
- Domain/Foundation Separation Check,
- Review Status Check.

Actions may produce:

- CI status,
- review report,
- PR comment,
- issue label,
- registry-update suggestion,
- blocked merge status,
- or review-required status.

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
- audit logs,
- and change logs.

Direct canonical updates require explicit approval.

## Phase 9 — Emergence Cycle

Approved or deferred updates may create:

- new candidates,
- new dependencies,
- new questions,
- new domain-pack requirements,
- new foundation-review requirements,
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
8. Treat registry status as workflow state, not truth.

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

## Locked Mode Constraint

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

The operations protocol accelerates auditable workflow. It does not bypass scientific review.
