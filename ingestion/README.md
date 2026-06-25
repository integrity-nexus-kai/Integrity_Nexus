# Ingestion

## Purpose

This directory defines the ingestion workflow for external review systems such as NotebookLM, Gemini, or other LLM-based compliance agents.

The goal is to make repository review scalable even when external tools restrict ZIP uploads by file count.

---

## Problem

Some external tools limit ZIP ingestion to a small number of files.

For NotebookLM-style workflows, the relevant limit may be:

```text
maximum 10 files per ZIP upload
```

This is not compatible with governance-heavy repositories containing many small Markdown and YAML files.

---

## Solution

Integrity Nexus supports two ingestion modes:

```text
1. Audit exports
2. Upload packages
```

## 1. Audit Exports

Use compact single-file exports from:

```text
exports/
```

These are best for high-level compliance review.

## 2. Upload Packages

Use curated package manifests from:

```text
ingestion/packages/
```

Each package should contain no more than ten files.

---

## Source of Truth Rule

```text
GitHub repositories remain the source of truth.
Ingestion packages are review surfaces.
```

Ingestion files must not introduce stronger claims than the source repository.

---

## Current Status

Initial ingestion workflow layer established.
