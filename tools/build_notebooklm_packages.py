#!/usr/bin/env python3
"""
Build NotebookLM-compatible upload packages from manifest files.

Purpose:
    Some external review tools restrict ZIP uploads to a maximum number of files.
    This script creates package folders and ZIP archives from curated manifests.

Rule:
    Each manifest should contain at most 10 source files.

Usage:
    python tools/build_notebooklm_packages.py \
        --root . \
        --manifest-dir ingestion/packages \
        --output-dir exports/notebooklm_packages

The script creates:
    exports/notebooklm_packages/<manifest-name>/...
    exports/notebooklm_packages/<manifest-name>.zip
"""

from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path


MAX_FILES_PER_PACKAGE = 10


def read_manifest(path: Path) -> list[str]:
    files: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if not item or item.startswith("#"):
            continue
        files.append(item)
    return files


def copy_file(root: Path, rel: str, package_dir: Path) -> None:
    src = root / rel
    dst = package_dir / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists() and src.is_file():
        shutil.copy2(src, dst)
    else:
        dst.write_text(f"MISSING SOURCE FILE: {rel}\n", encoding="utf-8")


def zip_dir(package_dir: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(package_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(package_dir))


def build_package(root: Path, manifest: Path, output_dir: Path) -> None:
    files = read_manifest(manifest)
    if len(files) > MAX_FILES_PER_PACKAGE:
        raise ValueError(
            f"Manifest {manifest} contains {len(files)} files; "
            f"maximum allowed is {MAX_FILES_PER_PACKAGE}."
        )

    package_name = manifest.stem.replace("_manifest", "")
    package_dir = output_dir / package_name
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)

    for rel in files:
        copy_file(root, rel, package_dir)

    zip_path = output_dir / f"{package_name}.zip"
    zip_dir(package_dir, zip_path)
    print(f"Built {zip_path} with {len(files)} files")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build NotebookLM-compatible ZIP packages.")
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument("--manifest-dir", default="ingestion/packages", help="Directory containing manifest txt files")
    parser.add_argument("--output-dir", default="exports/notebooklm_packages", help="Output directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest_dir = root / args.manifest_dir
    output_dir = root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    manifests = sorted(manifest_dir.glob("*_manifest.txt"))
    if not manifests:
        raise SystemExit(f"No manifest files found in {manifest_dir}")

    for manifest in manifests:
        build_package(root, manifest, output_dir)


if __name__ == "__main__":
    main()
