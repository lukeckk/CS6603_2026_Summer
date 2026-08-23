# Draft → report.tex examples

Pattern details: [format-reference.md](format-reference.md)  
Starter file: [template.tex](template.tex)

## Draft fragment

```text
- [x] Task 2: Summary of Bias in Public Artifact (20 Pts)
This report shows how automated hiring tools used by major companies are biased
against job seekers with certain ethinicity.

1. Privileged / Unprivileged Groups
- Unprivileged Groups: Black and Asian applicants
- Privileged Group: White job applicants
```

## Generated LaTeX

```latex
\section{Task 2: Summary of Bias in Public Artifact}
This report shows how automated hiring tools used by major companies are biased against job seekers with certain ethinicity.

\section{Task 3: Discussion of Artifact/Evidence Metrics Demonstrating Bias}
\subsection{Privileged/unprivileged groups}
\begin{itemize}
    \item Unprivileged Groups: Black and Asian applicants
    \item Privileged Group: White applicants
\end{itemize}
```

## Table from draft numbers

Draft:

```text
Unfavorable (Declined): privileged 815, unprivileged 366
Favorable (Approved): privileged 9652, unprivileged 4167
```

LaTeX — use style B from format-reference (`[H]` + `lrr` + empty header row).

## Figure from attached image

Save as `Figures/figure_1.png`, then:

```latex
\begin{figure}[H]
	\centering
	\includegraphics[height=6cm]{Figures/figure_1.png}
	\caption{Caption from draft}
	\label{fig:figure_1}
\end{figure}
```

Use `height=30cm` for tall pseudo-code screenshots.

## Citation from draft

Draft mentions a paper with URL → add `\bibitem` block from format-reference
References section, then `\printbibliography[heading=none]`.

Luke compiles PDF himself when the `.tex` looks good.
