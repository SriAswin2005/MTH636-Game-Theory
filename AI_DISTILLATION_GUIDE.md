# AI Distillation & Transcription Guide: Handwritten Notes to LaTeX

This document defines the exact standard, formatting conventions, visual styling, and pedagogical structure used to transcribe and distill handwritten lecture notes for **MTH636: Game Theory** (and mathematical coursework in general). 

Any AI assistant or human contributor transcribing notes for this repository **must strictly adhere** to the guidelines below.

---

## 1. Core Distillation Philosophy

1. **Zero Skipping / Line-by-Line Fidelity**:
   - **Never summarize, condense, or omit content** from the handwritten notes unless explicitly instructed.
   - Every definition, theorem, proposition, corollary, lemma, example, exercise, remark, side note, and scratch calculation must be captured.
   - Do **not** replace full proofs with "proof sketches" unless the handwritten notes themselves only provide a sketch.

2. **Pedagogical Clarity & Visual Appeal**:
   - Raw handwritten notes often contain messy scratchpad equations, shorthand arrows, and informal abbreviations.
   - When digitalizing, expand abbreviations into proper mathematical prose (e.g., "w.r.t." $\to$ "with respect to", "iff" $\to$ "if and only if", "s.t." $\to$ "such that").
   - Frame every formal mathematical entity in a color-coded `tcolorbox` environment to create an engaging, readable, modern document.

3. **Handling Illegible Text & Gaps**:
   - If a page has ink smudges, cropped margins, or illegible handwriting:
     - Check adjacent pages for continuous reasoning.
     - Cross-reference canonical course references (e.g., Eilon Solan, Nicolas Vieille, and Ran Spiegler; Martin J. Osborne; Michael Maschler).
     - Cross-reference secondary class notes if provided.
     - Never silently omit an illegible section; reconstruct the standard mathematical definition/proof faithfully.

---

## 2. Document Template & Preamble Setup

Every lecture note is a standalone LaTeX document that inputs the unified styling preamble:

```latex
\documentclass[12pt, a4paper]{article}

\input{preamble.tex}

\begin{document}

% Title Banner
\begin{center}
  {\LARGE\bfseries\sffamily\color{defblue} MTH636 -- Game Theory}\\[6pt]
  {\Large\sffamily Lecture N: [Topic Title]}\\[4pt]
\end{center}
\vspace{0.5cm}
\hrule height 1.5pt
\vspace{0.3cm}

% --- Content Sections ---
\section{...}

\end{document}
```

---

## 3. Visual Styling & Color-Coded Environments

All styled boxes are defined in `preamble.tex` via `tcolorbox`. Use the appropriate environment for each type of content:

| Environment | Purpose | Header Color | Background Color | Syntax |
| :--- | :--- | :--- | :--- | :--- |
| `defbox` | Formal Definitions | Dark Blue (`#1A5276`) | Soft Ice Blue (`#D6EAF8`) | `\begin{defbox}{Title} ... \end{defbox}` |
| `thmbox` | Major Theorems | Forest Green (`#1E8449`) | Mint Green (`#D5F5E3`) | `\begin{thmbox}{Title} ... \end{thmbox}` |
| `propbox` | Propositions / Corollaries | Olive Green (`thmgreen!70!black`) | Mint Green (`#D5F5E3`) | `\begin{propbox}{Title} ... \end{propbox}` |
| `exbox` | Worked Examples / Exercises | Amber Orange (`#B7770D`) | Warm Cream (`#FEF9E7`) | `\begin{exbox}{Title} ... \end{exbox}` |
| `warnbox` | Warnings & Non-Credible Threats | Crimson Red (`#922B21`) | Soft Pink (`#FADBD8`) | `\begin{warnbox}{Title} ... \end{warnbox}` |
| `notebox` | Remarks, Observations, Notes | Slate Gray (`#2C3E50`) | Light Gray-Blue (`#EBF5FB`) | `\begin{notebox} ... \end{notebox}` |
| `takebox` | Key Takeaways & Summaries | Deep Gold (`#7D6608`) | Crisp White (`#FDFEFE`) | `\begin{takebox} ... \end{takebox}` |
| `intubox` | Geometric & Strategic Intuition | Royal Purple (`#6C3483`) | Lavender Mist (`#F4ECF7`) | `\begin{intubox} ... \end{intubox}` |

### Syntax Notes:
- `defbox`, `thmbox`, `propbox`, `exbox`, and `warnbox` require a mandatory `{Title}` parameter:
  ```latex
  \begin{defbox}{Bayesian Nash Equilibrium}
  ...
  \end{defbox}
  ```
- `notebox`, `takebox`, and `intubox` do **not** take a title parameter:
  ```latex
  \begin{notebox}
  ...
  \end{notebox}
  ```
- Use the standard `proof` environment for all formal proofs:
  ```latex
  \begin{proof}
  ...
  \end{proof}
  ```

---

## 4. Mathematical Conventions & Notation for Game Theory

### 4.1. Payoff Matrices
- Typeset payoff matrices with `tabular` and `\renewcommand{\arraystretch}{1.2}`.
- Use `\payoff{u_1}{u_2}` for payoffs $(u_1, u_2)$.
- Use `\nash{u_1}{u_2}` to indicate underlined best responses or Nash Equilibrium outcomes.
- For diagonal headers, use `Player 1 \setminus Player 2` (avoid `\diagbox` as it requires non-standard CTAN packages in minimal TeX distributions).

Example:
```latex
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{c|cc}
 & $L$ & $R$ \\ \hline
$T$ & \payoff{1}{1} & \payoff{0}{0} \\
$B$ & \payoff{0}{0} & \payoff{2}{2}
\end{tabular}
\end{center}
```

### 4.2. Extensive Form Games & Trees
- Model extensive form games using the formal tuple:
  $$\Gamma = \langle N, V, E, n_0, (V_i)_{i \in N \cup \{0\}}, H=(H_i)_{i \in N}, A=(A(h))_{h \in \bigcup H_i}, (p_n)_{n \in V_0}, (u_i)_{i \in N} \rangle$$
- State information partitions explicitly: $H_i = \{h_1, h_2, \dots\}$.
- Explicitly explain the validity conditions for information sets:
  1. Equal number of outgoing edges for all nodes in an information set $h$.
  2. Every directed path from root $n_0$ crosses $h$ at most once.
- For game trees, describe the tree structure chronologically: root node, actions, intermediate nodes, information sets, and leaf payoffs.

### 4.3. Mixed and Behavior Strategies
- Pure strategy: $s_i : H_i \to \bigcup_{h \in H_i} A(h)$ with $s_i(h) \in A(h)$.
- Mixed strategy: $\sigma_i \in \Delta(S_i)$ where $S_i$ is the pure strategy set.
- Behavior strategy: $b_i : H_i \to \bigcup_{h \in H_i} \Delta(A(h))$, assigning an independent randomization at each information set.
- Reaching probability: $\rho(n; \sigma)$ is the probability node $n$ is reached under strategy profile $\sigma$.
- Strategy equivalence: $\sigma_i \sim b_i \iff \rho(n; (\sigma_i, \sigma_{-i})) = \rho(n; (b_i, \sigma_{-i}))$ for all $n \in V$ and all $\sigma_{-i}$.

### 4.4. Incomplete Information & Bayesian Games
- Harsanyi tuple: $\Gamma = \langle N, (T_i)_{i \in N}, p, S, (u_t)_{t \in T} \rangle$.
- Agent Form Game: $\hat{\Gamma} = \langle \hat{N}, (\hat{S}_\ell)_{\ell \in \hat{N}}, (\hat{u}_\ell)_{\ell \in \hat{N}} \rangle$ with $\hat{N} = \bigcup_{i=1}^n T_i$.
- Interim Expected Utility:
  $$U_i(\sigma \mid t_i) = \sum_{t_{-i} \in T_{-i}} p(t_{-i} \mid t_i) \, u_i((t_i, t_{-i}), (\sigma_i(t_i), \sigma_{-i}(t_{-i})))$$
- Ex-ante Expected Utility:
  $$V_i(\sigma) = \sum_{t \in T} p(t) \, u_i(t, \sigma(t)) = \sum_{t_i \in T_i} p(t_i) \, U_i(\sigma \mid t_i)$$

---

## 5. TeX Formatting & Compilation Rules

1. **Escaped Characters**:
   - Always escape ampersands outside math mode: `\&`.
   - Use standard double-hyphens `--` for en-dashes and `---` for em-dashes (avoid literal unicode en-dashes `–` or em-dashes `—`).
2. **Compiler Compatibility**:
   - All documents are verified with **Tectonic** (a modern, self-contained XeTeX engine).
   - Ensure no package incompatibilities exist. Do not rely on local absolute paths for `\input{preamble.tex}`.
3. **Stand-Alone Compilation**:
   - Each `Lecture_X.tex` must be fully compilable on its own without needing an overarching book master file.
   - Pdfs must be written cleanly into `lecture_pdfs/` for immediate viewing.

---

## 6. Checklist Before Finalizing a Lecture Note

- [ ] Every handwritten page was thoroughly examined.
- [ ] No theorems, definitions, examples, or exercises were skipped.
- [ ] All math formulas are formatted in proper LaTeX math mode (`$...$` or `\[...\]`).
- [ ] Environments (`defbox`, `thmbox`, `exbox`, etc.) are balanced with matching `\begin` and `\end{...}`.
- [ ] Document compiled without errors using `tectonic Lecture_X.tex`.
- [ ] Resulting PDF was checked for visual appeal and copied to `lecture_pdfs/`.
