# Audit Protocol

## Purpose

This document defines how audits are performed across Integrity Nexus and connected repositories.

---

## Audit Scope

Audits may cover:

- repository structure,
- governance compliance,
- maturity classification,
- claim boundaries,
- dependency maps,
- publication readiness,
- citation metadata,
- and open problem registration.

---

## Audit Method

Every audit must identify:

- fixed repository snapshot, release, or commit;
- auditor identity or review system;
- auditor independence and relevant conflicts;
- exact scope and exclusions;
- governing standards and evidence paths;
- finding severity, correction condition, and unresolved uncertainty.

Each audit should answer:

1. Are required documents present?
2. Are claims bounded by evidence and proof status?
3. Are limitations visible?
4. Are dependencies mapped?
5. Are open problems registered?
6. Is maturity classification justified?
7. Are publication candidates audit-ready?
8. Are literature, data, code, and provenance controls appropriate to the artifact?
9. Is material AI use disclosed and human-verified?
10. Are authorship, contributor roles, funding, conflicts, ethics, privacy, security, and licensing handled where applicable?

An audit performed by the producer of a material change is a self-audit and must be labeled as such. It cannot be represented as independent assurance.

---

## Audit Outcomes

Allowed outcomes:

```text
PASS
PASS_WITH_FINDINGS
NEEDS_REVISION
BLOCKED
```

---

## Finding Classes

```text
F1 — missing document
F2 — stale status
F3 — claim-boundary issue
F4 — dependency gap
F5 — citation gap
F6 — publication-readiness gap
F7 — maturity mismatch
```

---

## Maintenance Rule

Every audit outcome must update `audit/audit_log.md` and unresolved findings must be added to `audit/open_audit_findings.md`.

A finding may be closed only after the correction is verified against a fixed corrected snapshot. Audit passage does not establish scientific proof, external peer review, institutional approval, or Completion Readiness unless the separately authorized controlling process assigns that state.
