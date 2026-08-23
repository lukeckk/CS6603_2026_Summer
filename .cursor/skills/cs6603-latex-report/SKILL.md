---
name: cs6603-latex-report
description: >-
  Turns Luke's CS6603 draft answers (txt, docx, or notes) plus figure images
  into report.tex using jdf.cls and Luke's CS6603 LaTeX style. Use when
  converting assignment, exam, critique, or final project drafts to LaTeX.
  Does not compile PDF. Self-contained — read format-reference.md and
  examples.md in this skill folder only. Pair with simple-assignment-prose
  for paragraph text.
---

# CS6603 LaTeX Report Builder

Turn draft + images into `report.tex`. **Stop when the `.tex` is done** — do not
run `latexmk` or `pdflatex`.

## Style docs (read these; nothing else)

All formatting lives in this skill folder:

1. [format-reference.md](format-reference.md) — preamble, `[H]` floats, tables,
   figures, references, escaping
2. [examples.md](examples.md) — draft → LaTeX mapping examples
3. [template.tex](template.tex) — copy-paste starter file
4. [jdf.cls](jdf.cls) — Joyner Document Format class file (copy into assignment
   folder if missing)

Do not look for example reports in the repo. Everything needed is above.

## Inputs

1. **Draft** — `draft.txt`, Word export, or pasted notes (checkboxes OK).
2. **Images** — PNG/JPG histograms, screenshots, pseudo-code.
3. **Assignment folder** — where `report.tex` will live.
4. Optional: assignment PDF for section order.

## Outputs

```
AssignmentFolder/
├── draft.txt
├── report.tex         ← deliverable
├── jdf.cls            ← copy from this skill folder if missing
├── references.bib     ← can stay empty
└── Figures/
```

## Workflow

1. Read [format-reference.md](format-reference.md) and [examples.md](examples.md).
2. Read the draft. Strip `- [x]` / `- [ ]`. Map sections → `\section`, labels →
   `\subsection` or `\itemize`. Keep Luke's wording; use
   [simple-assignment-prose](../simple-assignment-prose/SKILL.md) only when
   drafting new paragraphs (if that skill is installed).
3. Copy images into `Figures/`. Name `figure_1.png`, `figure_2.png`, etc.
4. Start from [template.tex](template.tex). Write `report.tex` using blocks from
   format-reference — not from memory.
5. Copy [jdf.cls](jdf.cls) into the assignment folder if it is not there.
6. Sanity-check: escaped `_` `%` `&`, closed environments, figure paths. Do
   not compile.

## Non-negotiables

- `\usepackage{float}` + **`[H]` on every `\begin{table}` and `\begin{figure}`**
- Preamble packages: `caption`, `tabularx`, `float`, `xurl`, `hyperref`, plus
  `\captionsetup{justification=centering}`
- Figures: tab-indented block, `\includegraphics[height=6cm]{Figures/...}` (or
  `height=30cm` for tall pseudo-code screenshots)
- References: manual `\begin{thebibliography}{2}` + `\bibitem` +
  `\printbibliography[heading=none]`
- Author line: `Kha Kein "Luke" Cheng` with curly quotes

## Checklist

- [ ] Preamble matches [template.tex](template.tex)
- [ ] All tables and figures use `[H]`
- [ ] Table style picked from [format-reference.md](format-reference.md)
- [ ] Images in `Figures/` with correct paths
- [ ] Bibliography block present if draft has citations
- [ ] `jdf.cls` in assignment folder
- [ ] Prose still sounds like Luke
- [ ] Did not compile PDF

## What not to do

- Do not use `[h]`, `[htbp]`, or other float specifiers
- Do not compile PDF
- Do not invent numbers or citations
- Do not switch away from `jdf` document class
