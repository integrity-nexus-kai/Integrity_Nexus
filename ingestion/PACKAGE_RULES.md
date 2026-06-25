# Package Rules

## Purpose

This document defines rules for constructing ZIP packages for external tools with file-count limits.

---

## Primary Rule

```text
Maximum 10 files per ZIP package.
```

A package may contain fewer than ten files.

---

## Package Types

```text
core

governance

registry

objects

publication

operations

metrics

repo-specific

master-space
```

---

## Naming Convention

Use:

```text
<repo_or_scope>_<package_type>_<number>_manifest.txt
```

Examples:

```text
integrity_nexus_core_01_manifest.txt
integrity_nexus_governance_02_manifest.txt
integrity_nexus_objects_04_manifest.txt
master_repo_space_manifest.txt
```

---

## Source Rule

Package manifests should list source repository files only.

Generated ZIPs are temporary review artifacts.

---

## Claim Rule

Packages must preserve the repository's existing claim boundaries.

A package may summarize file purpose, but it must not introduce new theory, new claims, or new maturity status.

---

## Review Rule

After external audit, findings should be returned to the repository through:

```text
audit/open_audit_findings.md
audit/audit_log.md
operations/research_board.md
metrics/governance_metrics.md
```
