# Claim Objects

## Purpose

This directory contains canonical claim objects.

A claim object is the source of truth for a research claim, its evidence status, its boundary, and its relation to other objects.

---

## Object Type

```text
Claim
```

---

## Required Fields

```yaml
id: "CL-NEXUS-000"
type: "claim"
title: ""
status: "draft"
priority: "medium"
repository: ""
claim_class: ""
evidence_status: ""
proof_status: ""
boundary: ""
dependencies: []
linked_open_problems: []
linked_publications: []
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
summary: ""
```

---

## Claim Classes

Use the claim classes defined in:

```text
governance/claim_boundary_standard.md
```

---

## Rule

No claim may be promoted beyond its evidence or proof status.
