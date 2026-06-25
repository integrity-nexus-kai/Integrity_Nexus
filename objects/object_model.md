# Canonical Object Model

## Purpose

This document defines the shared structure for all research objects in Integrity Nexus.

---

## Minimal Object Fields

Every object should contain:

```yaml
id: ""
type: ""
title: ""
status: ""
priority: ""
repository: ""
owner: ""
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
summary: ""
dependencies: []
linked_objects: []
source_files: []
notes: ""
```

---

## Recommended Status Values

```text
draft
active
blocked
in_review
audited
closed
archived
```

---

## Recommended Priority Values

```text
critical
high
medium
low
```

---

## Object Rule

An object should contain enough structured information to be machine-readable and enough prose to remain human-readable.

---

## Future Generator Role

A future generator may read these objects and render:

- roadmap dashboards,
- open problem summaries,
- publication status,
- audit findings,
- maturity dashboards,
- and research board views.
