# Citation Standard

## Purpose and Authority

This document defines the cross-repository citation and authorship-metadata standard for repositories connected through Integrity Nexus.

Citation discipline preserves traceability, authorship, version identity, license identity, and scientific credibility. It does not merge scientific objects or transfer claim status between repositories.

---

## Repository Citation

Each active connected research repository must provide:

- `CITATION.cff` as the machine-readable citation record;
- `AUTHOR.md` as the authoritative human-readable authorship record;
- the exact repository name and URL;
- applicable license name and version;
- a stable release, version, DOI, or commit identifier when the cited state requires one.

`AUTHORS.md` is an optional compatibility alias. When present, it must agree with `AUTHOR.md` on names, roles, and public contact metadata. It must not become a competing authorship authority.

Metadata changes must preserve historical attribution and must not silently rewrite a DOI- or release-bound record.

---

## Contact Metadata

An author-approved public contact channel should be supplied where the repository is intended for collaboration, citation, or public release.

Contact metadata must:

- be consistent across `AUTHOR.md`, optional `AUTHORS.md`, `CITATION.cff`, and publication metadata;
- use only information already approved for that repository's publication boundary;
- avoid exposing private contact information by inference or by copying it from an unrelated repository.

Absence of a public contact channel is a citation or collaboration finding, not permission to invent or disclose one.

---

## Cross-Repository Citation

Integrity Nexus must cite connected repositories as separate research objects.

Cross-repository citation must preserve:

- source repository;
- source artifact and stable identifier;
- authorship;
- applicable license;
- scope and relation class where a claim or object is transferred.

Authorship, claims, evidence, status, and DOI identity must not be collapsed across repositories.

---

## External Research Citation

When a connected repository relies on external scientific work, that work must be referenced in the repository-specific bibliography or evidence path.

Integrity Nexus may provide navigation to those references, but it must not become the sole citation source for domain-specific scientific work.

---

## Release and DOI Boundary

Before changing citation or author metadata associated with a published release or DOI:

1. identify the release-bound metadata;
2. determine whether the change is corrective, additive, or version-forming;
3. preserve the historical record;
4. apply the repository's publication and review gate.

A citation update does not alter scientific status, Claim Status, canonicality, or Completion Readiness.
