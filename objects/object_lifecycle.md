# Research Object Lifecycle

## Purpose

This document defines the lifecycle of canonical research objects.

---

## Lifecycle

```text
draft
  ↓
active
  ↓
in_review
  ↓
audited
  ↓
closed
  ↓
archived
```

A blocked object may return to active when the blocker is resolved.

---

## Lifecycle Meaning

## draft

The object exists but is not yet canonical.

## active

The object is part of the working research program.

## blocked

The object cannot progress until a dependency or decision is resolved.

## in_review

The object is ready for audit or crystallization.

## audited

The object has passed a defined review.

## closed

The object is resolved, replaced, or no longer active.

## archived

The object is retained for traceability but no longer operational.

---

## Maintenance Rule

Changing an object's lifecycle state should update `last_updated` and, where relevant, linked roadmap, audit, or metrics views.
