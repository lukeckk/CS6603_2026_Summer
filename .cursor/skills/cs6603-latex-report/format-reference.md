# CS6603 LaTeX format reference

Self-contained style guide for Luke's CS6603 reports. Copy blocks verbatim,
then swap in draft content.

Starter file: [template.tex](template.tex)

---

## Preamble (copy exactly; change `\title` only)

```latex
\documentclass[
	%a4paper, % Use A4 paper size
	letterpaper, % Use US letter paper size
]{jdf}

\addbibresource{references.bib}

\author{Kha Kein “Luke” Cheng}
\email{Kcheng314@gatech.edu}
\title{Homework Project \#5: Fairness and Bias}
\usepackage{caption}
\usepackage{tabularx}
\usepackage{float}
\usepackage{xurl} 
\usepackage{hyperref}
\captionsetup{justification=centering}
\begin{document}
%\lsstyle

\maketitle
```

Copy [jdf.cls](jdf.cls) from this skill folder into the assignment folder.

---

## Float placement — always `[H]`

Requires `\usepackage{float}`.

```latex
\begin{table}[H]
```

```latex
\begin{figure}[H]
```

Luke uses `[H]` so tables and figures stay where they are written and do not
float to other pages. Do not use `[h]`, `[htbp]`, or `[H]` only on some floats.

---

## Figures

Standard histogram / plot:

```latex
\begin{figure}[H]
	\centering
	\includegraphics[height=6cm]{Figures/figure_3.png}
	\caption{Histogram for Disparate Impact}
	\label{fig:figure_3}
\end{figure}
```

- Tab-indent `\centering` and `\includegraphics` with a tab (not spaces)
- Path: `Figures/figure_N.png`
- Default height: `6cm`
- Tall pseudo-code screenshot: `height=30cm`

Multiple figures: one `\begin{figure}[H]...\end{figure}` block each, stacked.

---

## Tables — pick the style that fits the draft

### A. Small keyed table

Bordered, caption below:

```latex
\begin{table}[H]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Dataset} & \textbf{Outcome Variable} \\ \hline
Taiwan Credit Data Set & y \\ \hline
\end{tabular}
\caption{Dataset and Outcome Variable}
\label{tab:taiwan_dataset}
\end{table}
```

### B. Group comparison table

No vertical borders; empty second header row:

```latex
\begin{table}[H]
\centering
\begin{tabular}{lrr}
\hline
\textbf{group} & \textbf{Privileged (Young)} & \textbf{Unprivileged (Old)} \\ 
\textbf{} & & \\ \hline
Unfavorable (Declined) & 815 & 366 \\ 
Favorable (Approved) & 9652 & 4167 \\ \hline
\end{tabular}
\caption{Group Outcomes by Privilege Status}
\label{tab:group_outcomes}
\end{table}
```

### C. Fairness metrics table

```latex
\begin{table}[H]
\centering
\begin{tabular}{lrcc}
\hline
\textbf{Fairness metric} & \textbf{Computed value} & \textbf{Acceptable range} & \textbf{Bias} \\ \hline
Disparate Impact & 0.9969 & 0.8 to 1.25 & No \\ 
Equal Opportunity & 0.0022 & -0.1 to 0.1 & No \\ \hline
\end{tabular}
\caption{Fairness Metrics Evaluation}
\label{tab:fairness_metrics}
\end{table}
```

### D. Bordered metric rows

Every row ends with `\hline`:

```latex
\begin{table}[H]
\centering
\begin{tabular}{|l|l|c|c|}
\hline
\textbf{Protected class} & \textbf{Outcome} & \textbf{Statistical Parity Difference} & \textbf{Disparate Impact} \\ \hline
sex & G2\_pass & -0.0864 & 0.8935 \\ \hline
sex & G3\_pass & -0.0574 & 0.9340 \\ \hline
\end{tabular}
\caption{Fairness Metrics Across Protected Classes and Outcomes}
\label{tab:fairness_metrics_outcomes}
\end{table}
```

### E. Crosstab with row header

Wrap in `\begin{table}[H]` … `\end{table}` with caption and label:

```latex
\begin{table}[H]
\centering
\begin{tabular}{lrr}
\hline
\textbf{G2\_pass} & \textbf{Fail} & \textbf{Pass} \\ 
\textbf{sex} & & \\ \hline
F & 72 & 311 \\ 
M & 73 & 193 \\ \hline
\end{tabular}
\caption{G2 Pass/Fail Status by Sex}
\label{tab:g2_pass_sex}
\end{table}
```

### F. Stage / summary table (three columns)

```latex
\begin{table}[H]
\centering
\begin{tabular}{|l|c|l|}
\hline
\textbf{Stage} & \textbf{Disparate Impact} & \textbf{Change compared to previous} \\ \hline
Original Dataset & 0.9340 & NA \\ \hline
After Transforming Dataset & 1.0000 & Positive change \\ \hline
\end{tabular}
\caption{Sex vs G3\_pass --- Disparate Impact}
\label{tab:sex_g3_disparate_impact}
\end{table}
```

### G. Wide tables (many columns or long cells)

Use `\begin{table}[H]` + `tabularx` + `booktabs` (`\toprule`, `\midrule`,
`\bottomrule`). Only when styles A–F do not fit.

```latex
\begin{table}[H]
\centering
\small
\begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}p{4cm} >{\raggedright\arraybackslash}p{3cm} >{\raggedright\arraybackslash}X}
\toprule
\textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
\midrule
row & data & more data \\
\bottomrule
\end{tabularx}
\caption{Wide Table Caption}
\label{tab:wide_example}
\end{table}
```

---

## Lists and section layout

**Short answers** — `\begin{itemize} \item ... \end{itemize}`

**Exam / homework sections:**

```latex
\section{Task 2: Summary of Bias in Public Artifact}
```

Paragraph text directly under `\section` (no extra wrapper).

**Numbered steps (final project style):**

```latex
\section{ Data Selection }

1. 
\begin{itemize}
    \item Student Performance Dataset (student-por.csv, Portuguese language course)
\end{itemize}
```

Section titles may have leading/trailing spaces: `\section{ Data Exploration}`

**Analysis paragraphs** — plain text under `\section` or `\subsection`; can
span multiple paragraphs with no extra environment.

---

## Text escaping

| Character | LaTeX |
|-----------|-------|
| `_` in variable names | `G2\_pass`, `PAY\_0` |
| `%` | `28\%`, `less than 1\%` |
| `&` in text | rare; in tables column separator only |
| `$` | `\$` if needed |
| Bold emphasis from draft | `\textbf{...}` |

---

## References

Manual bibliography — not biblatex-only:

```latex
\begin{thebibliography}{2}

\bibitem{eeoc_guidelines}
U.S. Equal Employment Opportunity Commission. (1979, March 2). ``Questions and answers to clarify and provide a common interpretation of the uniform guidelines on employee selection procedures.'' \textit{EEOC}. 
\textsc{url}: \url{https://www.eeoc.gov/laws/guidance/questions-and-answers-clarify-and-provide-common-interpretation-uniform-guidelines}.

\bibitem{d_aquin_2024}
d'Aquin, G. M. (2024). ``Algorithmic fairness: a comprehensive survey.'' \textit{AI and Ethics}. 
\textsc{url}: \url{https://link.springer.com/article/10.1007/s43681-024-00541-3}.

\end{thebibliography}
\printbibliography[heading=none]
```

Rules:

- Paper titles in ``LaTeX double quotes''
- Journal/source in `\textit{...}`
- URL line: `\textsc{url}: \url{https://...}`
- Author ampersand: `\&`
- Always end with `\printbibliography[heading=none]` after `\end{thebibliography}`

---

## End of document

```latex
\end{document}
```

No extra sections after references unless the draft requires it.
