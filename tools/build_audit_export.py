#!/usr/bin/env python3
"""
Build a compact Markdown audit export from selected repository files.

Purpose:
    External LLM compliance tools may fail when ingesting many small files.
    This script creates one consolidated Markdown file from a curated file list.

Source-of-truth rule:
    Repository files remain canonical.
    The generated export is only an audit snapshot.

Usage:
    python tools/build_audit_export.py \
        --root . \
        --output exports/Integrity_Nexus_AUDIT_EXPORT.generated.md

Optional:
    python tools/build_audit_export.py \
        --root . \
        --manifest tools/audit_export_manifest.txt \
        --output exports/Integrity_Nexus_AUDIT_EXPORT.generated.md
"""

from __future__ import annotations

import argparse
from pathlib import Path
from datetime import date


DEFAULT_FILES = [
    "README.md",
    "EXECUTIVE_SUMMARY.md",
    "AUTHOR.md",
    "CITATION.cff",
    "LICENSE",
    "ARCHITECTURE.md",
    "COMMON_DENOMINATOR.md",
    "REPOSITORY_MAP.md",
    "NAVIGATION.md",
    "COMPLIANCE_AUDIT_BRIEF.md",
    "COMPLIANCE_CORE_PACKAGE.md",
    "governance/repository_constitution.md",
    "governance/repository_standard.md",
    "governance/claim_boundary_standard.md",
    "governance/citation_standard.md",
    "governance/subrepo_governance_protocol.md",
    "governance/maturity_model.md",
    "registry/repository_status.md",
    "registry/cross_repo_dependencies.md",
    "registry/shared_concepts.md",
    "registry/open_questions.md",
    "shared/glossary.md",
    "architecture/research_program_map.md",
    "publication/publication_pipeline.md",
    "publication/publication_status.md",
    "publication/publication_checklist.md",
    "audit/audit_protocol.md",
    "audit/open_audit_findings.md",
    "metrics/maturity_dashboard.md",
    "metrics/governance_metrics.md",
    "objects/README.md",
    "objects/object_model.md",
    "objects/object_lifecycle.md",
    "exports/README.md",
]


def read_manifest(path: Path) -> list[str]:
    files: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if not item or item.startswith("#"):
            continue
        files.append(item)
    return files


def fenced_language(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix in {".yaml", ".yml"}:
        return "yaml"
    if suffix == ".json":
        return "json"
    if suffix == ".py":
        return "python"
    if suffix == ".cff":
        return "yaml"
    return "markdown"


def build_export(root: Path, files: list[str]) -> str:
    chunks: list[str] = []
    chunks.append("# Generated Audit Export")
    chunks.append("")
    chunks.append(f"Generated: {date.today().isoformat()}")
    chunks.append("")
    chunks.append("Source-of-truth rule: repository files remain canonical. This export is an audit snapshot.")
    chunks.append("")
    chunks.append("---")
    chunks.append("")

    missing: list[str] = []

    for rel in files:
        path = root / rel
        chunks.append(f"# File: `{rel}`")
        chunks.append("")
        if not path.exists():
            missing.append(rel)
            chunks.append("```text")
            chunks.append("MISSING FILE")
            chunks.append("```")
            chunks.append("")
            chunks.append("---")
            chunks.append("")
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            chunks.append("```text")
            chunks.append("BINARY OR NON-UTF-8 FILE OMITTED")
            chunks.append("```")
            chunks.append("")
            chunks.append("---")
            chunks.append("")
            continue

        lang = fenced_language(rel)
        chunks.append(f"```{lang}")
        chunks.append(content.rstrip())
        chunks.append("```")
        chunks.append("")
        chunks.append("---")
        chunks.append("")

    if missing:
        chunks.append("# Missing Files")
        chunks.append("")
        for item in missing:
            chunks.append(f"- `{item}`")
        chunks.append("")

    return "\n".join(chunks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a compact repository audit export.")
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument("--manifest", default=None, help="Optional file list manifest")
    parser.add_argument("--output", required=True, help="Output Markdown file")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if args.manifest:
        files = read_manifest(Path(args.manifest))
    else:
        files = DEFAULT_FILES

    export = build_export(root, files)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(export, encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
