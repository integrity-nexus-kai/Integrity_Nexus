# Exports

## Purpose

This directory contains compact audit-export documents for external compliance tools such as NotebookLM, Gemini, or other LLM-based repository reviewers.

The goal is to avoid uploading full repository ZIP files when external tools have file-count or ingestion limits.

---

## Principle

```text
GitHub remains the source of truth.
Exports are audit snapshots.
```

Exports are not canonical research sources.

They are generated or maintained summaries designed for external review.

---

## Export Types

```text
Integrity_Nexus_AUDIT_EXPORT.md
MASTER_REPO_SPACE_AUDIT_EXPORT.md
```

Future exports may include:

```text
SSC_AUDIT_EXPORT.md
TIG_AUDIT_EXPORT.md
SIR_AUDIT_EXPORT.md
```

---

## Workflow

```text
Repository files
  ↓
Audit export
  ↓
External compliance tool
  ↓
Findings
  ↓
Nexus audit log / open findings
  ↓
Repository fixes
```

---

## Rules

1. Exports must not introduce stronger claims than source files.
2. Exports must identify source repositories and source files.
3. Exports must preserve claim boundaries.
4. Exports must show author/contact information correctly.
5. Exports should be regenerated after major repository changes.

---

## Current Status

Initial export layer established.
