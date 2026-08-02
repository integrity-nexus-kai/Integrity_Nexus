# Open Audit Findings

## Purpose

This document records unresolved audit findings across Integrity Nexus and connected repositories.

---

# Active Findings

## F-NEXUS-TRGS-001 — Evidence-Based Implementation Correction

Class: governance implementation  
Scope: Integrity Nexus TRGS candidate  
Severity: high

Finding:

```text
The 2026-08-02 implementation preflight found AQB-02 present and the other thirteen
academic-quality controls partial. Rule text alone was previously treated as sufficient evidence.
```

Correction work:

- correct the self-audit and benchmark matrix;
- separate C0-C4 statement grades from canonical Relation Classes;
- add audit, disclosure, correction, integrity-concern, AI-use, competence, risk, and collaboration evidence paths;
- expose incomplete publication bibliography and disclosures without inventing values;
- verify the corrected fixed snapshot in a fresh read-only run.

Status: correction in progress.  
Closure condition: a fresh fixed-snapshot implementation check verifies each correction and updates the conformance register.  
Scientific effect: none.

---

## F-NEXUS-001 — Initial Full Audit Required

Class: F2 — status validation  
Scope: Integrity Nexus  
Severity: medium

Finding:

```text
The operating structure has been created, but a full post-creation audit has not yet been completed.
```

Required action:

```text
Run initial Integrity Nexus audit and update metrics.
```

Status: open.

---

## F-TIG-001 — Nexus Alignment Audit Pending

Class: F4 — dependency / governance alignment  
Scope: TIG  
Severity: medium

Finding:

```text
TIG status and registry structure should be checked against Nexus maturity and repository standards.
```

Status: open.

---

## F-SIR-001 — Nexus Alignment Audit Pending

Class: F4 — dependency / governance alignment  
Scope: SIR  
Severity: medium

Finding:

```text
SIR status and registry structure should be checked against Nexus maturity and repository standards.
```

Status: open.

---

## Maintenance Rule

Closed findings should be moved into `audit/audit_log.md` with closure notes.
