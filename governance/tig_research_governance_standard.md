# TIG Research Governance Standard (TRGS)

## Status and Quality Boundary

```text
Status: DRAFT / INDEPENDENT REVIEW REQUIRED
Version: 0.2
Intended authority after approval: Integrity Nexus global governance layer
Scientific effect: NONE
```

TRGS is the candidate common research-governance control plane for the eight active repositories in the TIG research ecosystem. Its quality target is rigorous, reviewable scholarly practice comparable to leading academic research-integrity expectations. The quality target does not claim affiliation with, endorsement by, certification from, or equivalence to Harvard University, Princeton University, or any other institution.

Until independent audit and explicit author approval, TRGS has no canonical effect. The existing canonical governance modules remain authoritative.

TRGS is designed to integrate those modules after approval. It does not replace scientific evidence, validate a theory, promote a Claim Status, close an Open Question, or change Completion Readiness.

The sole global synchronization and Completion Readiness authority remains:

```text
Integrity_Nexus/registry/repository_status.md
```

## External Benchmark Basis

The controlled comparison against leading academic and international research-integrity practice is recorded in:

```text
academic_quality_benchmark.md
references.bib
```

The benchmark uses official Harvard and Princeton research-integrity resources as institutional reference points and ALLEA, DFG, COPE, TOP, FAIR, CRediT, Citation File Format, and European responsible-AI guidance as operational standards. No external source is treated as endorsing TIG or Integrity Nexus.

## Fundamental Integrity Principles

All governed research must preserve:

- reliability in design, method, analysis, and use of resources;
- honesty in development, review, reporting, and communication;
- respect for contributors, research objects, reviewers, affected communities, and the environment where applicable;
- accountability for the complete research record, including corrections and post-publication maintenance;
- independence between research production, approval, and assurance whenever feasible;
- documented handling of uncertainty, negative results, alternative explanations, and unresolved objections.

---

## 1. Authority and Repository Scope

- Integrity Nexus governs ecosystem-wide structure, status-axis interoperability, accepted synchronization, cross-repository traceability, and publication boundaries.
- TIG-E governs its research methodology and operating procedures within the authority boundary defined in `subrepo_governance_protocol.md`.
- Each domain repository remains authoritative for its own observed content, scientific objects, evidence, derivations, proofs, limitations, and local registries.
- Publication surfaces communicate approved states but are not scientific Sources of Truth.
- Repository content, scientific domain, governance authority, and scientific truth authority remain separate.

Canonical controls:

- `repository_constitution.md`
- `repository_standard.md`
- `subrepo_governance_protocol.md`
- `../registry/repository_status.md`

---

## 2. Claim and Status Discipline

- Research questions and methods must be developed against the documented state of relevant knowledge, including credible contrary results and alternative explanations.
- Researchers must work within their demonstrated competence, document material competence limits, and obtain qualified review where a claim exceeds that boundary.
- Every material scientific statement must identify its applicable Claim Status or explicitly leave Claim Status unassigned when unsupported.
- Claim Status, Scientific Status, Question State, Operational Status, Artifact Status, Maturity Status, Definition State, Bridge State, Progress Classification, and Completion Readiness must not be collapsed.
- Definition is not derivation; construction is not physical theory; selection is not necessity; compatibility is not proof; audit passage is not scientific validation.
- Local terminology requires an explicit Nexus-axis mapping or `NO DIRECT EQUIVALENCE`.
- No filename, directory, citation, publication, audit, or mapping may promote a claim automatically.

Canonical controls:

- `claim_status_taxonomy.md`
- `claim_boundary_standard.md`
- `cross_repository_claim_boundary_matrix.md`

---

## 3. Evidence and Provenance

Every material result, correction, transfer, or closure decision must preserve:

- the governing repository and exact artifact path;
- the fixed source snapshot, release, or commit identifier where required;
- the relation between source, interpretation, and conclusion;
- assumptions, limitations, dependencies, and unresolved objections;
- a reproducible evidence path;
- the human decision or authorization when a governance transition occurs.

Planned, absent, inaccessible, or merely named artifacts are not current evidence. External literature can support context, methods, comparisons, or premises, but it does not by itself prove a TIG-ecosystem claim.

Research records must be sufficient to reconstruct the asserted result. Fabrication, falsification, plagiarism, selective omission that materially distorts the record, concealed source substitution, and invented bibliographic metadata are prohibited.

Material records must be retained through versioned repository history or a documented external archive appropriate to the artifact. A correction must not erase the prior record when preservation is legally and technically possible.

---

## 4. Literature and Citation

- `citation_standard.md` is the canonical ecosystem-wide citation rule.
- Each repository and each publication artifact owns the bibliography required by its actual subject and citations.
- There is no mandatory universal ecosystem `.bib` file.
- A repository-level master bibliography is optional; a publication-specific bibliography must contain or reproducibly derive the sources actually cited by that artifact.
- Repository citation metadata (`CITATION.cff`) and external research bibliographies (`.bib`) are different objects and must not be conflated.
- Source metadata must be verified; DOI, arXiv identifiers, versions, page data, authorship, and URLs must never be invented.

---

## 5. Reproducibility and Validation

The applicable validation path must be declared for each result class:

- formal results: definitions, assumptions, proof obligations, derivation steps, and scope;
- computational results: code version, parameters, inputs, environment, seeds where relevant, and output provenance;
- empirical results: data provenance, method, uncertainty, exclusion criteria, and limitations;
- interpretive results: source basis, inferential step, alternatives, and non-claims.

Reproducibility is scoped to the asserted result. A reproducible procedure does not establish physical truth unless the required scientific validation bridge also exists.

Data, code, parameters, prompts that materially affect a result, and derived artifacts must be made as accessible as reasonably possible and as restricted as necessary. Privacy, security, legal, ethical, licensing, intellectual-property, and export-control restrictions must be recorded rather than bypassed.

Where data or code exist, their metadata should be findable, accessible under stated conditions, interoperable where practical, reusable within the declared license, and linked to provenance. When no data or code exist for a formal result, the record must say `NOT APPLICABLE` rather than creating empty artifacts.

Research planning must identify applicable ethical, legal, safety, security, dual-use, societal, and environmental risks. Material risks require mitigation, an explicit acceptance decision, or a stop condition before external release or implementation.

---

## 6. Open Questions and Dependencies

- Unresolved mathematical, methodological, computational, empirical, and shared-frontier questions must remain registered on the correct axis.
- A Question State changes only through its authorized closure sequence and accepted evidence.
- Dependencies and reverse dependencies must be checked before a material status, interface, publication, or synchronization change.
- Cross-repository transfers require an authorized Relation Class, evidence path, scope, allowed transfer, forbidden transfer, and impact record.
- External collaborations must record goals, roles, decision rights, authorship expectations, data and IP handling, integrity rules, conflict handling, and publication approval before material joint work is represented as accepted collaboration.

Canonical controls:

- `research_frontier_question_classification.md`
- `../registry/open_questions.md`
- `../registry/master_open_question_backlog.md`
- `cross_repository_claim_boundary_matrix.md`

---

## 7. Review, Audit, and Correction

- Research creation, integration, and independent audit are separate functions.
- Findings must identify evidence, affected scope, severity, and correction condition.
- Corrections must preserve prior attribution and relevant history.
- A closed finding requires verification against the corrected fixed snapshot.
- Audit outcomes report governance or review state only; they do not establish scientific proof.
- Material governance changes require a change-log entry and a downstream impact check.
- Reviewers must disclose relevant conflicts, protect confidential material, remain within their competence, and distinguish detected error from scientific disagreement.
- A person or AI system that produced a material change may not be represented as its independent assurance authority.
- Post-release errors require a proportionate correction, withdrawal, replacement, or retraction record linked to the affected version.
- Allegations of fabrication, falsification, plagiarism, concealed conflicts, or material record manipulation require evidence preservation, a fair response opportunity, and review by a qualified person not responsible for the disputed work whenever available.
- Good-faith reporting of integrity concerns must not trigger retaliation within the research workflow.

Minimum integrity-concern procedure:

1. register the concern without presuming guilt;
2. preserve the relevant fixed snapshot and evidence;
3. separate honest error or scientific disagreement from alleged misconduct;
4. disclose conflicts and appoint a qualified independent reviewer where available;
5. notify the affected person and allow a documented response;
6. apply a stated evidence standard and record reasons;
7. correct the research record proportionately;
8. provide reconsideration when material new evidence or procedural error is shown;
9. preserve confidentiality and protect good-faith reporters from retaliation to the extent possible.

Canonical controls:

- `../audit/audit_protocol.md`
- `../audit/open_audit_findings.md`
- `../operations/change_log.md`

---

## 8. Publication, Authorship, and AI Transparency

Before external release, every publication candidate must provide:

- an identified source repository and versioned artifact;
- explicit claims, limitations, non-claims, and maturity boundary;
- verified bibliography and citation metadata;
- authorship and contributor attribution;
- applicable license and release boundary;
- disclosure of material AI-assisted drafting, analysis, coding, or review when it affected the released artifact;
- human verification and responsibility for all released content;
- applicable conflict-of-interest, funding, data, code, and ethics statements.

Authorship requires accountable intellectual contribution, approval of the released version, and willingness to answer for the work. Gift, guest, coercive, and concealed ghost authorship are prohibited. Other contributions must be acknowledged or described through an appropriate contributor-role statement. CRediT roles may be used when useful, but role labels do not determine authorship automatically.

Peer-review status must be stated exactly. Internal review, AI review, commissioned private review, repository audit, preprint posting, journal peer review, acceptance, and publication are different states and must not be collapsed.

Open dissemination is preferred where compatible with law, privacy, security, intellectual property, contractual duties, and the repository license. Restricted access must state the reason and the available metadata or verification path.

An AI system is not treated as an author, scientific authority, evidence source, or approval authority. AI output must be verified against primary artifacts and cited literature before it can support a released research artifact.

Material AI use must record, at a level proportionate to its effect:

- tool or model identity where known;
- task and research stage;
- whether confidential or unpublished material was processed;
- human verification performed;
- limitations, unresolved uncertainty, and retained provenance;
- whether AI was used in drafting, translation, coding, mathematical work, literature discovery, analysis, image generation, or review.

Sensitive, confidential, unpublished, export-controlled, or personal data must not be submitted to an external AI service without an authorized protection basis. AI-generated citations, quotations, calculations, and factual claims require source-level verification.

Canonical controls:

- `citation_standard.md`
- `../publication/publication_pipeline.md`
- `../publication/publication_checklist.md`
- `../publication/publication_status.md`

---

## 9. Repository Conformance and Synchronization

Each active repository must expose, directly or through registered equivalent paths:

1. repository identity, scope, authorship, citation, license, and release boundary;
2. local governance authority and its mapping to TRGS;
3. status-axis mappings, including `NO DIRECT EQUIVALENCE` where required;
4. claim, evidence, limitation, Open Question, and dependency paths appropriate to its domain;
5. publication and bibliography paths where publication artifacts exist;
6. its current conformance evidence without claiming unperformed synchronization.

The controlled conformance record is:

```text
../registry/repository_governance_conformance.md
```

Conformance records do not alter global synchronization, Progress Classification, Completion Readiness, Claim Status, Scientific Status, or Question State.

---

## Maintenance Rule

TRGS changes require:

1. an explicit change proposal;
2. conflict review against the canonical modules listed above;
3. impact analysis across all eight active repositories;
4. author approval;
5. a change-log entry;
6. an updated conformance review.

No local repository may silently redefine TRGS under the same canonical filename or authority label.

Activation additionally requires:

1. a completed Meta-Repository self-audit;
2. an independent read-only audit against `academic_quality_benchmark.md`;
3. disposition of all blocking findings;
4. explicit approval by Kai Stefan Dietrich;
5. replacement of the draft status with an approved canonical version.
