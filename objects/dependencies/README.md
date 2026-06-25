# Dependency Objects

## Purpose

This directory contains canonical dependency objects.

A dependency object records relationships between repositories, claims, open problems, proof obligations, publications, or governance structures.

---

## Object Type

```text
Dependency
```

---

## Required Fields

```yaml
id: "DEP-NEXUS-000"
type: "dependency"
title: ""
status: "draft"
priority: "medium"
dependency_class: ""
source_object: ""
target_object: ""
source_repository: ""
target_repository: ""
relationship: ""
boundary: ""
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
summary: ""
```

---

## Dependency Classes

```text
D0 — navigation reference
D1 — shared terminology
D2 — conceptual analogy
D3 — governance dependency
D4 — evidence-supported dependency
D5 — formal dependency
```

---

## Rule

A dependency must state its boundary clearly.

Conceptual dependencies must not be represented as formal proof dependencies.
