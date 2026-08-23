---
name: cs6603-report-reviewer
description: >-
  Reviews Luke's finished CS6603 reports (PDF, report.tex, or draft) against
  the assignment requirements and against his simple spoken English tone.
  Use when Luke asks to review a report before submission, check rubric
  coverage, or check that prose does not sound AI-polished. Does not rewrite
  the report unless asked. Self-contained — read tone-checklist.md in this
  skill folder.
---

# CS6603 Report Reviewer

Review a finished report before submission. Two jobs only:

1. **Requirements** — does it answer every assignment ask?
2. **Voice** — does the prose sound like Luke (simple spoken English), not
   polished AI / academic filler?

**Default: review only.** List findings. Do not rewrite unless Luke says to fix
something. If he asks for fixes, rewrite paragraphs **down** using the tone
rules in [tone-checklist.md](tone-checklist.md) (or
`simple-assignment-prose` if that skill is installed).

## Inputs Luke provides

1. **Report** — `report.tex`, PDF, or draft text
2. **Assignment instructions** — PDF or FAQ (required for a full requirements
   check; if missing, say so and only do voice + structural review)
3. Optional: his `draft.txt` to compare what he meant vs what is in the report

## How to review

### Step 1 — Build a requirements checklist

From the assignment PDF / FAQ:

- List every graded task, numbered question, required figure, table, metric,
  dataset name, citation, notebook deliverable, page limit, filename rule
- Mark each as: **Present** / **Partial** / **Missing** / **Unclear**
- Quote the assignment wording for anything Missing or Partial
- Do not invent requirements that are not in the instructions

### Step 2 — Check the report against that checklist

For each requirement:

- Point to where it appears (`section X`, table caption, figure path)
- Flag wrong values, empty analysis sections, placeholder text
  (`I am a team of one` alone when analysis was required, TBD, lorem)
- Flag missing figures/tables that the rubric asks for
- Flag LaTeX issues only if they would break grading (missing figure file
  referenced, empty required section) — not style nitpicks unless asked

### Step 3 — Voice / AI-polish check

Read every **paragraph** (skip pure bullet lists, tables, captions, bib).

Use [tone-checklist.md](tone-checklist.md) as the ground truth.

Flag passages that sound AI-polished or unlike Luke. For each flag:

- Quote the sentence or short paragraph
- Name the signal (e.g. `furthermore`, perfect academic arc, hedging pile)
- Give a one-line note: rewrite down / keep if Luke prefers

Do **not** flag:

- Course terms used correctly (Disparate Impact, privileged group, etc.)
- Simple grammar quirks that match Luke (`there is not much`, mixed I/we)
- Short bullet answers that are meant to be short
- Accidental typos unless they change meaning or look like a broken sentence
  the grader cannot parse

Do **not** tell Luke to add fake mistakes. Human voice = simple wording and
spoken structure, not errors.

### Step 4 — Consistency spot-check

- Numbers in prose match tables/figures nearby
- Privileged / unprivileged labels stay consistent
- Section titles match the assignment's naming when the rubric is picky

## Output format

Use this structure every time:

```markdown
# Report review

## Verdict
One short line: ready / needs fixes before submit / needs assignment PDF to finish review

## Requirements
| # | Requirement | Status | Where / note |
|---|-------------|--------|--------------|
| 1 | ... | Present / Partial / Missing | ... |

## Voice (AI-polish risk)
- **High / Medium / Low** overall
- Quoted flags with signal names (or "none — prose matches Luke's samples")

## Other issues
- Numbers, missing figures, placeholders, etc. (or "none")

## Priority fixes
1. ...
2. ...
```

Keep the review pointed. Prefer a short table and a few quotes over a long essay.

## What not to do

- Do not rewrite the whole report in the review pass
- Do not "upgrade" Luke's tone into professional English as a "fix"
- Do not claim the report will pass an AI detector — only that it matches
  his documented voice (detectors are unreliable; tone match is the goal)
- Do not invent rubric items
- Do not compile LaTeX unless he asks

## Related skills

- Tone when rewriting: [tone-checklist.md](tone-checklist.md), or
  `simple-assignment-prose` if present
- Building `report.tex`: `cs6603-latex-report` if present
