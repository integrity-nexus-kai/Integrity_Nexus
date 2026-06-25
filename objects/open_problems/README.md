# Open Problem Objects

## Purpose

This directory contains canonical open problem objects.

An open problem object is the source of truth for a research problem, its status, dependencies, blockers, and resolution path.

---

## Object Type

```text
OpenProblem
```

---

## Required Fields

```yaml
id: "OP-NEXUS-000"
type: "open_problem"
title: ""
status: "draft"
priority: "medium"
repository: ""
problem_statement: ""
why_it_matters: ""
dependencies: []
blocked_by: []
linked_claims: []
linked_proof_obligations: []
linked_publications: []
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Status Values

```text
draft
active
blocked
in_review
partially_resolved
resolved
archived
```

---

## Rule

If an open problem affects roadmap, publication, audit, or maturity status, the object should become the canonical source for those views.
