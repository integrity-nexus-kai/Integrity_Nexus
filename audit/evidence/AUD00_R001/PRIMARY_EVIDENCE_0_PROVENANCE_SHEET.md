# PRIMARY EVIDENCE EXPORT — AUD-00 v0.10 TARGET + R001 INSTRUCTION

Retrieval only. No new audit, no new evaluation, no new decision, no recommendation.
This sheet records the provenance, recovery state, and cryptographic identities of the recovered primary-evidence package.

**Repository persistence correction — 2026-08-16:** the earlier wording "accompanying byte-identical files" described the recovered export package, not the files actually committed in commit `dccf1447df0cd1bf74385f23b733fb9686794c93`. That commit contained this provenance sheet only. The three full primary texts were recovered and hash-verified in the Strategy Main working evidence set, but were not themselves committed by that commit. This distinction is now explicit and must not be inferred otherwise.

---

## 1. AUD-00 v0.10 — EXACT FROZEN TARGET

`PROVENANCE: EXACT FROZEN TARGET`

- **File:** `PRIMARY_EVIDENCE_1_AUD-00_v0.10_FROZEN_TARGET.md`
- **SHA-256:** `d1be9ded676c3679648fa5a2e0caf3c538f6c303e1e7c55a8d784af92a6b1df2`
- **Match to audit `AUD02-AUD00V10-TCR-20260816-01` frozen target:** exact.
- Full, unmodified text (1925 lines, §0–§28). Not summarised, not reformulated, not updated, not corrected, no status change, no sections omitted.
- **Recovery state:** EXACTLY RECOVERED.
- **Repository full-text persistence at time of this record:** NOT YET COMMITTED AS A STANDALONE FILE.

---

## 2. ORIGINAL R001 TARGETED-CLOSURE INSTRUCTION

The instruction is split across two distinct primary documents. They are different artifacts and must not be merged or mislabelled.

### 2a — R001 ORIGIN (v0.9 closure re-audit where R001 was first raised)

`PROVENANCE: EXACT ORIGINAL INSTRUCTION`

- **File:** `PRIMARY_EVIDENCE_2a_R001_ORIGIN_v0.9_closure.md`
- **SHA-256:** `d7e3b3984c9ed3c53b1182dd72be66710962126302ab5bd54dca7c3eff05c76f`
- This is the file named `AUD02_Targeted_Governance_Closure_Reaudit_v0.9_R001_Source.md` in the retrieval request.
- **Contains:** Source Audit `AUD00V08-IAGR-20260813-01`; remediated target AUD-00 v0.9; F001–F004 closure evidence; original R001 finding `AUD02-AUD00V09-TGCR-20260813-01-R001`; original defect; governance risk; minimum necessary correction; closure summary; next controlled step.
- **Does NOT contain:** R001-T1…R001-T10 test criteria; those are in 2b.
- **Recovery state:** EXACTLY RECOVERED.
- **Repository full-text persistence at time of this record:** NOT YET COMMITTED AS A STANDALONE FILE.

### 2b — R001 TARGETED-CLOSURE INSTRUCTION (instruction that drove audit `AUD02-AUD00V10-TCR-20260816-01`)

`PROVENANCE: EXACT ORIGINAL INSTRUCTION`

- **File:** `PRIMARY_EVIDENCE_2b_R001_TARGETED_INSTRUCTION.md`
- **SHA-256:** `d23b0a0fa7da75e29ea10c7f878463dc6d0073a4508b049c8bdb06a7774fa916`
- **Contains:** purpose and scope (R001 only); frozen target `AUD-00_..._v0.10_DRAFT.md` with SHA-256 `d1be9ded…`; required source set; R001 restatement; mandatory R001-T1 … R001-T10; verdict logic; output structure; downstream boundary; anti-drift rules.
- **Recovery state:** EXACTLY RECOVERED.
- **Repository full-text persistence at time of this record:** NOT YET COMMITTED AS A STANDALONE FILE.

**Naming note:** the T1–T10 criteria are physically in 2b, not 2a. Both artifacts are required to preserve the evidence chain.

---

## 3. RECOVERY / REPOSITORY STATUS

| Artifact | Recovery status | Standalone full text in repository |
|---|---|---|
| AUD-00 v0.10 exact frozen target | `EXACTLY RECOVERED` | `PENDING` |
| R001 origin — v0.9 closure re-audit | `EXACTLY RECOVERED` | `PENDING` |
| R001 targeted-closure instruction with T1–T10 | `EXACTLY RECOVERED` | `PENDING` |

The SHA-256 values above remain the identity anchors for later persistence verification.

No new factual evaluation. No new audit decision. No new recommendation.

`END OF PRIMARY EVIDENCE EXPORT / PERSISTENCE STATUS RECORD`
