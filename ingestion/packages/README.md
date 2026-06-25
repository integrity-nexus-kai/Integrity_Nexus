# Ingestion Package Manifests

## Purpose

This directory contains file manifests for creating external-review ZIP packages.

Each manifest should contain at most ten source files.

---

## Current Manifests

```text
integrity_nexus_core_01_manifest.txt
integrity_nexus_governance_02_manifest.txt
integrity_nexus_registry_03_manifest.txt
integrity_nexus_objects_04_manifest.txt
integrity_nexus_operations_05_manifest.txt
master_repo_space_manifest.txt
```

---

## Workflow

Use the manifests with:

```text
tools/build_notebooklm_packages.py
```

The tool can create package folders or ZIP files while preserving the ten-file package rule.

---

## Rule

These package manifests are not canonical research sources.

They are operational review packaging instructions.
