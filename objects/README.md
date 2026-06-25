# Research Objects

## Purpose

This directory defines the object-centered research model for Integrity Nexus.

The goal is to move from document-centered governance to object-centered research state management.

---

## Core Principle

```text
One object is the source of truth.
Markdown documents are views.
```

A research object should be updated once and then referenced or rendered into roadmap, audit, metrics, publication, and operations documents.

---

## Object Types

```text
claims/
open_problems/
dependencies/
proof_obligations/
publications/
repositories/
audits/
decisions/
risks/
```

---

## Operating Rule

Do not maintain the same status manually in five places.

Maintain the canonical object.

Dashboards and summaries should eventually be generated from objects.

---

## Current Status

Initial object model layer established.

This is the foundation for a future generator or GitHub Actions workflow that can build dashboards and status documents automatically.
