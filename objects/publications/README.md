# Publication Objects

## Purpose

This directory contains canonical publication objects.

A publication object tracks a paper, technical note, whitepaper, preprint, repository release, or governance specification.

---

## Object Type

```text
Publication
```

---

## Required Fields

```yaml
id: "PUB-NEXUS-000"
type: "publication"
title: ""
status: "draft"
priority: "medium"
repository: ""
publication_type: ""
stage: ""
linked_claims: []
linked_open_problems: []
linked_proof_obligations: []
linked_dependencies: []
audit_required: true
audit_status: "not_started"
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Publication Stages

```text
idea
outline
draft
internal_audit
external_ready
submitted
published
archived
```

---

## Rule

No publication should be marked external-ready without a claim-boundary, limitation, dependency, and citation audit.
