# Risk Objects

## Purpose

This directory contains canonical risk objects.

A risk object records a threat to research progress, governance integrity, publication readiness, or repository coherence.

---

## Object Type

```text
Risk
```

---

## Required Fields

```yaml
id: "RISK-NEXUS-000"
type: "risk"
title: ""
status: "draft"
priority: "medium"
severity: ""
probability: ""
risk_statement: ""
impact: ""
mitigation: ""
owner: ""
linked_audits: []
linked_decisions: []
linked_open_problems: []
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Severity Values

```text
low
medium
high
critical
```

---

## Rule

Risks should be reviewed during weekly operations and linked to audits or decisions when applicable.
