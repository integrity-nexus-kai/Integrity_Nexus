# AUD-00 v0.10 — Internal Authoritative Working Baseline Decision

**Decision date:** 2026-08-16  
**Repository:** `integrity-nexus-kai/Integrity_Nexus`  
**Program Owner / Human Authority:** Kai Stefan Dietrich  
**Decision class:** Program-Owner baseline/status decision  
**Status:** ACTIVE — INTERNAL AUTHORITATIVE WORKING BASELINE ESTABLISHED  

---

## 1. Decision

Following closure of governance finding:

`AUD02-AUD00V09-TGCR-20260813-01-R001`

under targeted re-audit:

`AUD02-AUD00V10-TCR-20260816-01`

and separate Strategy Main 3 reconciliation against the recovered primary evidence, the Program Owner establishes the frozen AUD-00 v0.10 governance text identified by SHA-256:

`d1be9ded676c3679648fa5a2e0caf3c538f6c303e1e7c55a8d784af92a6b1df2`

as the **internal authoritative working baseline** for the next controlled authoring and synchronization steps.

This decision means:

`AUD-00 v0.10 = INTERNAL AUTHORITATIVE WORKING BASELINE`

for internal governance authoring, synchronization, and downstream auditor-Master-Prompt regeneration.

---

## 2. Explicit non-promotions

This decision does **not** establish any of the following:

- `RATIFIED`;
- external independent assurance;
- Bootstrap-Hold release;
- full Automated Ratification Architecture validation;
- runtime implementation correctness;
- live delegation-registry validity;
- `AUD-00 v1.0`;
- unrestricted external-release readiness.

The following remain unchanged:

`RATIFICATION STATUS = NOT RATIFIED`

`BOOTSTRAP HOLD = ACTIVE`

`EXTERNAL INDEPENDENCE = NOT CLAIMED`

---

## 3. R001 state

The following state is authoritative for the defined targeted scope:

`R001 = AUDIT-CLOSED`

Closure is limited to the governance-text defect and direct regression surface defined by the targeted R001 closure instruction.

The closure record is:

`audit/AUD02_AUD00V10_R001_closure_verification_2026-08-16.md`

---

## 4. Baseline identity and provenance

Frozen target identity:

- Artifact: `AUD-00_IMMUNIT_Audit_Charter_and_Rules_v0.10_DRAFT.md`
- Transport filename used during audit: `AUD-00_v0_10_WORKING_DRAFT.md`
- SHA-256: `d1be9ded676c3679648fa5a2e0caf3c538f6c303e1e7c55a8d784af92a6b1df2`

Primary-evidence provenance is recorded under:

`audit/evidence/AUD00_R001/`

No historical v0.9 artifact is altered by this decision.

---

## 5. Downstream authority of this baseline

This baseline is the only permitted governance source for the immediate downstream sequence:

1. synchronize the AUD-00 Governance Artifact and the governing AUD-00 Master Prompt;
2. preserve all non-promoted status boundaries above;
3. freeze the synchronized post-closure authoring baseline with explicit version/hash provenance;
4. regenerate operational Auditor Master Prompts from that controlled baseline;
5. audit each operational Auditor Master Prompt before installation or operational use.

Previously generated Auditor Master Prompts derived from an incorrect, unresolved, or superseded AUD-00 base paper are not valid current authoring candidates.

They may remain historical artifacts only.

---

## 6. Synchronization rule

Synchronization must be status-preserving and provenance-preserving.

It may update downstream representations to reflect:

- `R001 = AUDIT-CLOSED`;
- this Program-Owner baseline decision;
- the correct internal-authoritative-working-baseline identity.

It must not silently introduce:

- Ratification;
- external-independence claims;
- Bootstrap-Hold release;
- new governance authority;
- unrelated architectural redesign.

If the existing governing AUD-00 Master Prompt cannot be recovered exactly, the missing artifact must be retrieved before synchronization rather than reconstructed by guesswork.

---

## 7. Decision provenance

Program Owner instruction recorded in Strategy Main 3 on 2026-08-16:

`Freigabe wie empfohlen.`

The decision authorized the recommended transition to an internal authoritative working baseline while preserving all explicit non-promotions and remaining gates.

---

## 8. Current next action

`AUD-00 MASTER-PROMPT / GOVERNANCE-ARTIFACT SYNCHRONIZATION`

If the governing AUD-00 Master Prompt is not present in the repository or otherwise exactly recoverable, obtain the exact current artifact from its existing source before making any synchronized downstream version.
