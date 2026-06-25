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

Each audit should answer:

1. Are required documents present?
2. Are claims bounded by evidence and proof status?
3. Are limitations visible?
4. Are dependencies mapped?
5. Are open problems registered?
6. Is maturity classification justified?
7. Are publication candidates audit-ready?

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
