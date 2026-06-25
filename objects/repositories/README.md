# Repository Objects

## Purpose

This directory contains canonical repository objects.

A repository object tracks the role, maturity, status, dependencies, publication candidates, and audit state of a connected repository.

---

## Object Type

```text
Repository
```

---

## Required Fields

```yaml
id: "REPO-NEXUS-000"
type: "repository"
title: ""
status: "active"
priority: "medium"
repository_name: ""
repository_url: ""
domain: ""
role: ""
maturity: ""
linked_open_problems: []
linked_claims: []
linked_dependencies: []
linked_publications: []
audit_status: ""
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Rule

The repository object should become the canonical input for repository status dashboards and maturity dashboards.
