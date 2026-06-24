# Sub-Repository Governance Protocol

This protocol defines how Integrity Nexus governs, synchronizes, and navigates connected sub-repositories.

Integrity Nexus does not control scientific content by authority.

It governs through standards, status tracking, dependency mapping, and claim-boundary discipline.

---

# Governance Principle

The master repository defines cross-repository standards.

Each sub-repository owns its domain-specific research content.

Integrity Nexus owns:

- repository status indexing,
- cross-repository relationship mapping,
- shared terminology orientation,
- claim-boundary standards,
- citation standards,
- and maturity classification.

---

# Required Sub-Repository Artifacts

A Nexus-aligned sub-repository should provide:

- `README.md`
- `EXECUTIVE_SUMMARY.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`
- `GOVERNANCE.md`
- `LIMITATIONS.md`
- `CITATION.cff`
- `AUTHOR.md`
- `governance/DEVELOPMENT_STATUS.md`
- `registry/` where applicable

---

# Synchronization Rule

A major change in a sub-repository requires three updates:

1. Update the affected sub-repository registry or governance file.
2. Update the sub-repository `governance/DEVELOPMENT_STATUS.md`.
3. Update `Integrity_Nexus/registry/repository_status.md` if maturity or cross-repository relevance changed.

---

# Cross-Repository Claim Rule

A sub-repository may reference another repository only under an explicit relationship class.

Relationship classes:

- navigation reference,
- shared terminology,
- conceptual analogy,
- governance dependency,
- evidence-supported dependency,
- formal dependency.

No conceptual analogy may be presented as a proof.

---

# Promotion Rule

A repository may be promoted in maturity only when:

- required artifacts exist,
- claim boundaries are explicit,
- limitations are visible,
- dependencies are mapped,
- and unresolved structures are registered.

---

# Meta-Repository Update Rule

Integrity Nexus must be updated when:

- a new repository is added,
- a repository maturity level changes,
- a cross-repository dependency changes,
- a shared concept is introduced,
- or a public-facing claim changes.

---

# Non-Goal

Integrity Nexus does not erase domain autonomy.

TIG, SIR, SSC, and future repositories retain their own internal research structures.

Integrity Nexus maintains the map, not the territory.
