# Citation Standard

## Purpose and Authority

This document defines the cross-repository citation and authorship-metadata standard for repositories connected through Integrity Nexus.

Citation discipline preserves traceability, authorship, version identity, license identity, and scientific credibility. It does not merge scientific objects or transfer claim status between repositories.

---

## Repository Citation

Each active connected research repository must provide:

- exactly one root `CITATION.cff` as the machine-readable repository citation record;
- `AUTHOR.md` as the authoritative human-readable authorship record;
- the exact repository name and URL;
- applicable license name and version;
- a stable release, version, DOI, or commit identifier when the cited state requires one.

`AUTHORS.md` is an optional compatibility alias. When present, it must agree with `AUTHOR.md` on names, roles, and public contact metadata. It must not become a competing authorship authority.

Metadata changes must preserve historical attribution and must not silently rewrite a DOI- or release-bound record.

A case-variant or secondary `citation.cff` must not compete with the root `CITATION.cff`. If historical metadata must be retained, it must be archived under a non-authoritative name and must identify the canonical record.

The license field in `CITATION.cff` must match the effective root `LICENSE`. A DOI may be recorded only when it has actually been assigned. A version or commit identifier must describe a real cited state and must not be invented merely to fill a field.

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

The external sources used to benchmark Integrity Nexus governance are recorded in:

```text
governance/references.bib
```

That bibliography governs the Meta-Repository governance benchmark only. It is not a universal bibliography for the connected scientific repositories.

### Bibliography Ownership

- Different repositories must maintain bibliographies appropriate to their own scientific domains.
- Different publication artifacts may maintain different bibliographies when their citation scopes differ.
- There is no mandatory ecosystem-wide universal `.bib` file.
- A repository-level master bibliography is optional.
- Each publication artifact must declare its canonical bibliography path or its reproducible derivation from a repository-level master bibliography.
- Multiple versions of the same publication must share one source bibliography or explicitly document why their bibliographies differ.
- An empty `.bib` file must not be created merely for filename conformance.

Recommended publication-local path:

```text
papers/<artifact>/references.bib
```

An established domain-specific equivalent is allowed when it is documented from the repository governance or publication entry point.

### BibTeX Integrity

For every released or review-ready publication artifact:

- every citation key used by the artifact must resolve;
- every publication-local bibliography entry must be traceable to a real source;
- author or editor, title, year, and publication source must be recorded where applicable;
- DOI, arXiv identifier, URL, volume, issue, and page data must be included when verified and relevant;
- metadata must not be reconstructed from memory when a primary bibliographic record is available;
- duplicate records and key collisions must be resolved without breaking release-bound citations;
- primary sources should be preferred for scientific, mathematical, and historical priority claims;
- review literature may support orientation but must not be represented as primary evidence;
- material contrary evidence and credible alternative interpretations must not be omitted merely because they weaken the preferred position;
- quotations and citations must accurately represent the cited source and the scope in which it is used;
- citation of a source does not transfer validation, proof, or authority to a repository claim.

Citation-key syntax may remain repository-specific, but it must be stable and documented. Renaming a release-bound key requires an explicit migration or compatibility record.

### AI-Assisted Bibliography Boundary

AI systems may assist with discovery, formatting, and duplicate detection. They must not be treated as bibliographic authorities. Every externally released entry and every identifier must be verified against the source publication, publisher record, DOI registry, arXiv record, or another authoritative bibliographic record.

Unverified suggestions must remain outside the canonical `.bib` file.

---

## Release and DOI Boundary

Before changing citation or author metadata associated with a published release or DOI:

1. identify the release-bound metadata;
2. determine whether the change is corrective, additive, or version-forming;
3. preserve the historical record;
4. apply the repository's publication and review gate.

A citation update does not alter scientific status, Claim Status, canonicality, or Completion Readiness.
