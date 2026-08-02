# Sub-Repository Governance Protocol

## Purpose

This protocol defines how Integrity Nexus governs, synchronizes, and navigates connected repositories without taking authority over their domain-specific scientific content.

Integrity Nexus governs through standards, status-axis control, accepted synchronization, dependency mapping, relation classification, and claim-boundary discipline.

---

## Authority Hierarchy

Authority is separated by function:

1. **Integrity Nexus — global governance authority**
   - repository scope and navigation;
   - cross-repository standards;
   - accepted synchronization and Completion Readiness;
   - shared status axes and Claim Status vocabulary;
   - cross-repository relation and transfer boundaries;
   - ecosystem-level terminology, citation, maturity, and dependency mapping.

2. **TIG-E — methodological and research-operating authority**
   - TIG-E methodology and workflow design;
   - EKS, bottleneck analysis, constraint navigation, search-space reduction, and emergence-construction methods;
   - domain-neutral procedures for research crystallization, audit preparation, and open-question handling.

3. **Domain repositories — local scientific authority**
   - actually observed local content and repository HEAD;
   - scientific objects, claims, derivations, proofs, evidence, gates, limitations, and local registries within their domain.

4. **Publication surfaces — communication boundary**
   - website, briefing, and recipient-facing material communicate an approved state;
   - they are not scientific Sources of Truth and cannot promote claims.

No layer may silently assume the authority of another. A newer local state does not automatically replace the Nexus-accepted global state.

---

## Required Repository Functions

A Nexus-aligned repository must satisfy the binding interoperability core in `governance/repository_standard.md`.

Recommended filenames may be replaced by registered equivalents. Empty compatibility files are not required. The repository must make the effective paths discoverable from its `README.md` or governance entry point.

---

## Synchronization Rule

A material change in a connected repository requires:

1. an update to the affected local governance, registry, evidence, or development-state record;
2. an impact check covering dependencies, reverse dependencies, open questions, public surfaces, and cross-repository transfers; and
3. a separate Nexus update when accepted synchronization, maturity, cross-repository relevance, terminology, public claims, or Completion Readiness changes.

The local repository is authoritative for its observed content. Integrity Nexus is authoritative for the last accepted global synchronization and Completion Readiness record. On conflict, both states must remain visible until explicitly reconciled; no automatic override is permitted.

---

## Cross-Repository Transfer Rule

Every material cross-repository or cross-domain transfer must use one permitted `Relation Class` from `governance/cross_repository_claim_boundary_matrix.md` and must record:

- source repository and object;
- target repository and object;
- relation target;
- scope;
- evidence path;
- allowed and forbidden transfer;
- dependency and open-question impact.

Semantic resemblance, shared terminology, common authorship, repository proximity, or conceptual analogy does not establish identity, derivation, or proof.

---

## Status-Vocabulary Rule

The canonical ecosystem-wide Claim Status axis is defined by `governance/claim_status_taxonomy.md`.

Local or historical vocabularies may remain in use only when their axis is explicit and an evidence-backed mapping to the Nexus axes exists. Where no safe equivalence exists, the mapping must say `NO DIRECT EQUIVALENCE`.

Mappings must not convert evidence state, question state, operational state, maturity, artifact class, author approval, or release state into Claim Status. They must never promote a claim automatically.

---

## Promotion Rule

A repository artifact may be proposed for a higher maturity, review, or release state only when:

- its effective artifact class is explicit;
- required interoperability functions exist;
- claim and domain boundaries are explicit;
- limitations are visible;
- evidence and source paths are reproducible;
- dependencies and reverse dependencies are mapped;
- unresolved structures are registered; and
- the required human and assurance gates have been satisfied.

Audit passage, publication, mapping, or file placement does not establish scientific truth.

---

## Meta-Repository Update Rule

Integrity Nexus requires review when:

- a repository is added, archived, or reclassified;
- accepted synchronization or maturity changes;
- a cross-repository dependency or Relation Class changes;
- a shared concept or status vocabulary is introduced or altered;
- an open question changes ecosystem-level impact;
- or a public-facing claim changes.

Repository content may prepare a proposed Nexus update, but it does not mutate the global state by implication.

---

## Non-Goal

Integrity Nexus does not erase domain autonomy. TIG, QIC, Yang–Mills, SIR, SSC, TIG-E, and future repositories retain their proper local research structures.

Integrity Nexus maintains the governed map. Domain repositories maintain the scientific territory. TIG-E maintains the transferable research methodology and operating procedures within that map.
