# Example review output

Illustrates the format in SKILL.md. Not a real submission.

## Verdict

Needs fixes before submit

## Requirements

| # | Requirement | Status | Where / note |
|---|-------------|--------|--------------|
| 1 | Task 2 bias summary (~paragraph) | Present | §Task 2 |
| 2 | Privileged / unprivileged groups | Present | §3.1 itemize |
| 3 | Analysis of mitigation tradeoffs | Partial | §Post analysis exists but stops mid-sentence on last page |
| 4 | Pseudo-code figure for method | Missing | Method text present; no figure / no `Figures/` reference |

## Voice (AI-polish risk)

**Medium**

- Quote: "Furthermore, the report demonstrates how aggregate visualizations can obscure subgroup disparities..."
  - Signal: formal transition + paper voice (`demonstrates`, `obscure subgroup disparities`)
  - Note: rewrite down toward "To make it worse" / "hiding bias" style

- Quote: rest of Task 2 and Tesla-style critique paragraphs
  - Signal: none — matches gold samples

## Other issues

- Disparate Impact in prose says 0.9969; table says 0.9969 — OK
- Placeholder not found

## Priority fixes

1. Add the missing method figure (or remove claim that one is included)
2. Finish / repair the cut-off analysis paragraph
3. Rewrite the flagged "Furthermore... demonstrates..." sentence down to Luke's voice
