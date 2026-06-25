# NotebookLM Upload Workflow

## Purpose

This document defines how Integrity Nexus and connected repositories should be prepared for NotebookLM-style compliance review.

---

## Core Constraint

If NotebookLM enforces a ten-file limit per ZIP upload, do not upload the full repository ZIP.

Instead use one of these workflows:

```text
A. Single-file audit export
B. Curated ten-file ZIP package
C. Multi-package staged audit
```

---

# A. Single-File Audit Export

Use when you need a fast compliance pass.

Upload:

```text
exports/Integrity_Nexus_AUDIT_EXPORT.md
```

or:

```text
COMPLIANCE_CORE_PACKAGE.md
```

Best for:

- author check,
- role check,
- claim-boundary check,
- governance overview,
- maturity snapshot.

---

# B. Curated Ten-File ZIP Package

Use when the auditor needs to inspect source files directly.

Use package manifests in:

```text
ingestion/packages/
```

Each manifest should contain at most ten files.

Example package:

```text
integrity_nexus_core_01_manifest.txt
```

---

# C. Multi-Package Staged Audit

Use when reviewing the full repository space.

Recommended order:

```text
1. Core package
2. Governance package
3. Registry / dependency package
4. Objects package
5. Operations / metrics package
6. Repository-specific exports for SSC, TIG, SIR
7. Master repo-space audit export
```

---

## Recommended First Pass

Upload these first:

```text
exports/Integrity_Nexus_AUDIT_EXPORT.md
exports/MASTER_REPO_SPACE_AUDIT_EXPORT.md
```

Then add repository-specific exports as they are created:

```text
exports/SSC_AUDIT_EXPORT.md
exports/TIG_AUDIT_EXPORT.md
exports/SIR_AUDIT_EXPORT.md
```

---

## Finding Return Path

NotebookLM findings should be copied back into:

```text
audit/open_audit_findings.md
audit/audit_log.md
operations/research_board.md
metrics/governance_metrics.md
```

---

## Rule

Do not let external tool limitations dictate repository architecture.

Keep GitHub structured.

Generate review surfaces for tools.
