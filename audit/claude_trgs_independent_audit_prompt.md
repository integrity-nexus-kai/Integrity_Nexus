# Claude Independent Eight-Repository Governance Audit Prompt

Perform a read-only governance audit of the eight supplied repository snapshots. Do not access GitHub, modify files, audit scientific truth, or repeat correct content.

Use `Integrity_Nexus/governance/tig_research_governance_standard.md`, `academic_quality_benchmark.md`, and `references.bib` as the candidate baseline. `AQB` means Academic Quality Benchmark. Verify requirements 01–14 against actual evidence in each snapshot, including local `governance/TRGS_LOCAL_PROFILE.md` and `audit/TRGS_CANDIDATE_IMPLEMENTATION_RECORD.md` where present.

Check only: authority conflicts; competing taxonomies/registers; status-axis collapse; missing operational evidence; bibliography ownership and unresolved citations; authorship/funding/interests/AI disclosures; review independence; correction, integrity, competence, risk, privacy/security, and collaboration gates; unsupported conformance claims.

Return no more than three highest-severity findings per repository, then a one-line verdict per repository. Use this table only:

| Repository | Severity | Requirement 01–14 | File | Exact gap | Required correction |
|---|---|---|---|---|---|

Finish with exactly one ecosystem verdict:

```text
READY FOR AUTHOR APPROVAL
```

or

```text
NOT READY FOR AUTHOR APPROVAL
```
