# License Harmonization Report

Date: 2026-06-25  
Scope: Integrity Nexus research ecosystem  
Status: completed with intentional exceptions

---

## Purpose

This report records the license and canonical-status harmonization performed across the active Integrity Nexus research ecosystem.

The objective was to align repository-level license visibility, canonical authorship, and modification boundaries with the intended research-governance rule:

```text
Share: yes.
Cite: yes.
Study: yes.
Independent further development: yes.
Modify or redistribute canonical material as canonical: no.
```

---

## License Model

The active repositories are governed by:

```text
Canonical Integrity License v1.0
```

This is a custom research-governance license.

It is not an OSI-approved open-source license.

The purpose of the license is to preserve canonical authorship and repository integrity while allowing public reading, citation, sharing, review, audit, and clearly marked independent further development.

---

## Canonical Rule

Only author-approved changes in the canonical repository are considered canonical material.

Forks, mirrors, adaptations, summaries, continuations, and derivative projects must not present themselves as the canonical repository unless explicitly authorized by Kai Stefan Dietrich.

---

## Repositories Audited

| Repository | Action | Status |
|---|---|---|
| `Integrity_Nexus` | License replaced, README updated, `CANONICAL_STATUS.md` added, citation metadata updated | fixed |
| `Structural_State_Controller` | LICENSE checked, README updated, `AUTHORS.md` added | fixed |
| `Structural_Integrity_Recursion` | LICENSE checked, README updated, `AUTHOR.md` and `AUTHORS.md` added | fixed |
| `Quantum_Integrity_Core` | LICENSE checked, `CITATION.cff` checked, `CANONICAL_STATUS.md` checked | checked only |
| `TIG_YM_Research` | LICENSE checked, README updated, `AUTHOR.md` and `AUTHORS.md` added | fixed |
| `TIG_YM_derivation_architecture` | LICENSE checked, README updated, MIT reference removed, `AUTHOR.md` and `AUTHORS.md` added | fixed |
| `TIG-E-Topological_integrity-_gravity_engine-` | LICENSE checked, README updated, contact corrected, `AUTHOR.md` and `AUTHORS.md` added | fixed |
| `integrity-nexus-kai.github.io` | LICENSE checked, README updated, `AUTHOR.md` and `AUTHORS.md` added | fixed |
| `Kairos-Architects-I` | intentionally left unchanged | inactive / historical |

---

## Intentional Exception: Quantum Integrity Core

`Quantum_Integrity_Core` was checked but not modified.

Reason:

```text
The repository is DOI-sensitive because of its Zenodo connection.
```

The existing files already contain the correct license and canonical-status metadata:

- `LICENSE`
- `CITATION.cff`
- `CANONICAL_STATUS.md`

The README could be made more visibly explicit in the future, but the correction was intentionally deferred because the compliance benefit did not justify the DOI / release-management risk.

---

## Intentional Exception: Kairos Architects I

`Kairos-Architects-I` was intentionally left unchanged.

Reason:

```text
The repository is inactive and represents early exploratory work.
```

No harmonization action is currently required.

---

## Standard Files Used

The harmonized repositories use some or all of the following files:

```text
LICENSE
CANONICAL_STATUS.md
CITATION.cff
AUTHOR.md
AUTHORS.md
README.md
```

`AUTHOR.md` records direct author attribution.

`AUTHORS.md` exists as a plural compatibility alias for external reviewers and automated compliance tools.

`CANONICAL_STATUS.md` records the canonical repository rule and modification boundary.

---

## Compliance Outcome

The active ecosystem now has a consistent canonical-status model:

- author attribution is clearer,
- official contact information is normalized,
- license references are visible in active README files,
- canonical modification boundaries are documented,
- independent further development remains allowed when clearly non-canonical,
- and the active research ecosystem is more audit-ready.

---

## Final Director Note

This harmonization closes the immediate license and canonical-status compliance loop.

Further governance work should not expand unless required by publication, audit, or repository-specific research needs.

Next priority:

```text
Return to research.
```
