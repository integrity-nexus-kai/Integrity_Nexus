# Repository Standard

## Status and Authority

This document defines the cross-repository structural standard for research repositories connected through Integrity Nexus.

Integrity Nexus is authoritative for ecosystem-wide repository structure, governance interoperability, status-axis compatibility, and cross-repository traceability. Domain repositories remain authoritative for their own scientific content, evidence, and local research objects.

This standard distinguishes required interoperability functions from recommended presentation structure. It does not require empty placeholder files where the same function is already provided by a registered equivalent path.

---

## Required Interoperability Core

Each active connected repository must provide, either at the named root path or through an explicitly registered equivalent:

- `README.md` — identity, purpose, scope, and navigation;
- `AUTHOR.md` — authoritative human-readable authorship metadata;
- `CITATION.cff` — machine-readable citation metadata;
- `LICENSE` — applicable license text and version;
- `CANONICAL_STATUS.md` — repository authenticity, author-approval boundary, and applicable release boundary;
- a governance entry point — local authority, permissions, and review rules;
- a limitations or boundary statement — explicit non-claims and current scope;
- a development-state or registry entry point — current work, dependencies, and open questions where applicable.

`AUTHORS.md` is an optional compatibility alias. When present, it must not contradict `AUTHOR.md`.

The effective path for every required function must be discoverable from `README.md` or the repository governance entry point.

Upon author-approved activation of TRGS, the local governance entry point must also identify:

- its mapping to `Integrity_Nexus/governance/tig_research_governance_standard.md`;
- any local governance extensions and their limited scope;
- every local status vocabulary and its Nexus-axis mapping;
- `NO DIRECT EQUIVALENCE` where no safe mapping exists; and
- its citation and bibliography paths where publication or external-evidence artifacts exist.

Until activation, this is a review requirement and has no canonical effect. The mapping may be contained in an existing governance file. A new placeholder file is not required.

---

## Recommended Presentation Files

The following root files remain recommended where they improve navigation and are not already represented by a registered equivalent:

- `EXECUTIVE_SUMMARY.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`
- `GOVERNANCE.md`
- `LIMITATIONS.md`

Repositories must not create empty files merely to satisfy a filename checklist. Existing domain-specific files may fulfill these functions when their mapping is explicit.

---

## Recommended Directories

Connected repositories should use directories appropriate to their domain. Common structural layers include:

- `docs/`
- `governance/`
- `registry/`
- `research/`
- `paper/`

Directory names do not assign scientific status, maturity, author approval, or canonicality.

---

## Registry Standard

Where applicable, repositories must maintain or project registries for:

- open questions and problems;
- assumptions;
- threats and blockers;
- claims and evidence;
- dependencies and relation classes;
- glossary terms;
- domain-specific invariants or proof obligations.

Global synchronization and Completion Readiness remain controlled by `Integrity_Nexus/registry/repository_status.md`. Local registries report local observed state and must not silently override the Nexus record.

---

## Status and Vocabulary Interoperability

The canonical Claim Status axis is defined by `governance/claim_status_taxonomy.md` in Integrity Nexus.

A repository may retain a domain-specific or historical vocabulary only when it provides an explicit Nexus mapping that:

1. identifies the local axis and meaning;
2. distinguishes Claim Status from evidence, question, operational, maturity, and release states;
3. records `NO DIRECT EQUIVALENCE` where no safe mapping exists;
4. prohibits automatic status promotion; and
5. preserves the local term for historical traceability without presenting it as the global standard.

No filename, directory, mapping, import, audit result, or publication location may raise a claim status automatically.

---

## Purpose

This standard makes repositories readable and interoperable for:

- human reviewers;
- scientific collaborators;
- governance auditors;
- machine-assisted analysis systems.

Interoperability must preserve domain autonomy, evidence boundaries, and the separation between repository identity and scientific truth.
