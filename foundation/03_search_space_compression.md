# Search Space Compression

## Purpose

Search Space Compression is the process by which TIG-E reduces an initially unbounded or weakly structured problem space into a smaller, governed, auditable set of candidate paths.

The goal is not to guess the answer faster. The goal is to remove invalid, redundant, misplaced, or non-fundamental paths before costly work begins.

## Definition

```text
Search Space Compression = structured reduction of possible solution paths by governance, dependency mapping, candidate classification, and generator/projection testing.
```

## Why It Matters

Complex research problems often fail not because no answer exists, but because the search space is too large, too noisy, or organized at the wrong explanatory level.

TIG-E reduces this risk by asking:

- What is the actual claim?
- What assumptions does it require?
- Which candidates are being introduced?
- Are they generators or projections?
- Which dependencies must be solved first?
- Which paths are circular, domain-specific, or premature?

## Compression Methods

TIG-E compresses search spaces by:

1. **Claim Extraction**
   - Convert free input into explicit claims.

2. **Assumption Extraction**
   - Identify hidden premises and dependency chains.

3. **Candidate Classification**
   - Mark candidates as fundamental, emergent, rejected, or open.

4. **Dependency Mapping**
   - Determine which questions must precede others.

5. **Level Control**
   - Separate universal architecture from domain-specific application.

6. **Contradiction Detection**
   - Identify circular reasoning, missing premises, and invalid mixture of levels.

7. **Review Routing**
   - Send unresolved or high-impact structures to human review.

## Output

A compressed search space does not necessarily produce a final answer.

It produces:

- fewer candidate paths,
- better question order,
- clearer dependencies,
- visible open questions,
- explicit rejection reasons,
- and a structured route for further work.

## Governance Rule

```text
Each iteration must either reduce the search space or make its structure more explicit.
```

If an iteration produces neither, it is not a successful TIG-E step.

## Relation to Emergence

Search Space Compression prepares the conditions under which useful emergence may occur.

Emergence is not invoked as magic. It is prepared by removing invalid structures until the remaining candidate space can produce new configurations under controlled review.
