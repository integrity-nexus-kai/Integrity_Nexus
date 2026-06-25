# Proof Obligation Objects

## Purpose

This directory contains canonical proof obligation objects.

A proof obligation records something that must be shown, justified, derived, verified, or bounded before a stronger claim can be made.

---

## Object Type

```text
ProofObligation
```

---

## Required Fields

```yaml
id: "PO-NEXUS-000"
type: "proof_obligation"
title: ""
status: "draft"
priority: "medium"
repository: ""
statement: ""
required_for: []
dependencies: []
proof_status: ""
linked_claims: []
linked_open_problems: []
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Proof Status Values

```text
not_started
sketch
partial
blocked
complete
audited
```

---

## Rule

A formal claim should not be promoted unless its proof obligations are either closed or explicitly scoped as open.
