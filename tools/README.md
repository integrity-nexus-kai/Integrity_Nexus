# Tools

## Purpose

This directory contains tooling for generating audit exports, dashboards, and future machine-readable repository views.

---

## Current Tools

```text
build_audit_export.py
```

The initial tool is a lightweight Python script design for collecting selected repository files into a single Markdown audit export.

---

## Principle

```text
Repositories remain source of truth.
Tools generate review surfaces.
```

Generated exports should not introduce new claims.

They should only collect, summarize, or render existing repository material.

---

## Future Tooling

Potential future tools:

```text
build_repo_space_export.py
build_maturity_dashboard.py
build_open_problem_dashboard.py
validate_object_schema.py
validate_claim_boundaries.py
```

---

## Current Status

Initial tooling layer established.
