# Audit Objects

## Purpose

This directory contains canonical audit objects.

An audit object records an audit event, scope, findings, result, and follow-up actions.

---

## Object Type

```text
Audit
```

---

## Required Fields

```yaml
id: "AUD-NEXUS-000"
type: "audit"
title: ""
status: "draft"
priority: "medium"
audit_scope: ""
audit_type: ""
repository: ""
result: ""
findings: []
linked_risks: []
linked_decisions: []
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
next_action: ""
```

---

## Result Values

```text
PASS
PASS_WITH_FINDINGS
NEEDS_REVISION
BLOCKED
```

---

## Rule

Every completed audit object should update audit views and unresolved findings.
