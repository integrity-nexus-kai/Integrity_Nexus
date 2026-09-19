# Open Audit Findings

## Purpose

This document records unresolved audit findings across Integrity Nexus and connected repositories.

---

# Active Findings

## F-EPA-001 — First-Leg Historical Freeze Reconstruction

Class: F4 — dependency / provenance gap  
Scope: EPA early chain (Kairos → QIC → website → SIR/SSC/TIG-E)  
Severity: medium

Finding:

```text
Several early transition claims are currently supported by later self-description plus selected early commits, but not yet by a complete frozen first-state reconstruction for every repository edge.
```

Required action:

```text
Freeze representative early commits/artifacts and bind each early transition claim to contemporaneous evidence before promoting historical-causality status.
```

Status: open.

---

## F-EPA-002 — AI-Infrastructure 40-Hour Phase Not Provenance-Bound

Class: F4 — timing / provenance gap  
Scope: EPA capability evolution  
Severity: medium

Finding:

```text
The Human Authority reports an approximately 40-hour AI-infrastructure learning/building phase as a major capability inflection, but exact date boundaries and primary artifacts have not yet been bound.
```

Required action:

```text
Identify contemporaneous artifacts, project/chat creation evidence, or other primary records that can delimit the interval and distinguish learning, infrastructure construction, and subsequent capability effects.
```

Status: open.

---

## F-EPA-003 — Current Orchestration Counts Not Telemetry-Verified

Class: F2 — current-state verification  
Scope: EPA Human–AI orchestration architecture  
Severity: low

Finding:

```text
Current counts of 18 open ChatGPT chats and 29 projects are self-reported and structurally plausible, but not independently verified through platform telemetry.
```

Required action:

```text
Retain as SELF-REPORTED unless an appropriate platform/account evidence source is deliberately introduced. The structural role-based architecture may be audited independently of exact counts.
```

Status: open.

---

## F-EPA-004 — Capability Choreography Date / Commit Mismatch Requires Source Binding

Class: F4 — provenance timing gap  
Scope: SSC HT capability reconstruction  
Severity: medium

Finding:

```text
research/homo_transcendens/provenance/2026-08-30/CAPABILITY_CHOREOGRAPHY_RECONSTRUCTION_2026-08-30.md was inspected as committed on 2026-09-11. The path/date label alone cannot establish prospective existence of the full C1–C8 reconstruction on 2026-08-30.
```

Required action:

```text
Bind earlier handoffs or contemporaneous source artifacts for each claimed capability transition before treating them as August prospective evidence.
```

Status: open.

---

## F-EPA-005 — Machine-Readable Evidence Layer Incomplete

Class: F1/F4 — audit artifact / provenance completeness  
Scope: EPA  
Severity: medium

Finding:

```text
The working baseline contains human-readable anchors, but the machine-readable Epistemic Transition Ledger, dual dependency graph, evidence matrix, and complete commit/hash/artifact appendix are not yet materialized.
```

Required action:

```text
Build the machine-readable EPA evidence layer before final Executive Report or closure assessment.
```

Status: open.

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
