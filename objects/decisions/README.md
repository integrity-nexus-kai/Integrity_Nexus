# Decision Objects

## Purpose

This directory contains canonical decision objects.

A decision object records a major governance, research, publication, or operational decision and its rationale.

---

## Object Type

```text
Decision
```

---

## Required Fields

```yaml
id: "DEC-NEXUS-000"
type: "decision"
title: ""
status: "draft"
priority: "medium"
decision: ""
rationale: ""
impact: ""
affected_repositories: []
linked_risks: []
linked_audits: []
linked_publications: []
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Rule

A decision object should be created for changes that alter structure, governance, maturity, publication direction, or cross-repository dependencies.
