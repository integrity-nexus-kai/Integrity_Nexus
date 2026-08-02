# Claude Independent TRGS Audit Prompt

Perform an independent read-only governance audit of the provided `Integrity_Nexus` candidate snapshot only after the repository implementation preflight has been corrected and a new fixed snapshot has been supplied.

If the supplied snapshot still states `CORRECTION PASS REQUIRED BEFORE INDEPENDENT GOVERNANCE AUDIT`, stop and report `PRECONDITION NOT MET`.

`TRGS` means `TIG Research Governance Standard`. It is the draft candidate in:

```text
governance/tig_research_governance_standard.md
```

Audit it strictly against:

```text
governance/academic_quality_benchmark.md
governance/references.bib
audit/trgs_meta_self_audit_2026-08-02.md
```

Verify all benchmark items `AQB-01` through `AQB-14` against actual repository evidence. Check for missing controls, contradictions, non-operational rules, unsupported status claims, circular authority, unverifiable source references, and gaps that would prevent research governance at rigorous leading-academic quality.

Do not audit the scientific truth of TIG. Do not modify files. Do not begin auditing the other seven repositories. Do not repeat correct repository contents.

Output only:

| Nr. | Severity | AQB-ID | File | Exact governance gap | Required correction |
|---|---|---|---|---|---|

Use at most 15 independently evidenced findings. If no blocking or major findings remain, say so explicitly.

End with exactly one verdict:

```text
READY FOR AUTHOR APPROVAL
```

or

```text
NOT READY FOR AUTHOR APPROVAL
```
