# MTH636: Game Theory -- Complete Coursework & Distilled Notes

[![Course](https://img.shields.io/badge/Course-MTH636%20Game%20Theory-blue.svg)](.)
[![Lectures](https://img.shields.io/badge/Lectures-32%20Complete-green.svg)](lecture_pdfs/)
[![LaTeX](https://img.shields.io/badge/Typeset-LaTeX%20%7C%20Tectonic-orange.svg)](lecture_notes/)
[![Problem%20Sets](https://img.shields.io/badge/Problem%20Sets-1%20to%205-purple.svg)](problem_statements/)

A complete, digitalized, and typeset archive of **MTH636: Game Theory**. This repository contains unabridged, color-coded LaTeX transcriptions and compiled PDFs for all 32 lectures, quick-reference survival guides, problem sets, and guided solutions.

---

## Repository Structure

```text
├── README.md                      # Repository overview & syllabus map
├── LECTURE_PDFS.md                # Comprehensive catalog of all 32 lecture PDFs
├── AI_DISTILLATION_GUIDE.md       # Style guide & prompt instructions for AI models
├── .gitignore                     # Build artifacts, OS files, and TeX caches
│
├── lecture_pdfs/                  # Final compiled lecture note PDFs
│   ├── Lecture_1.pdf ... Lecture_32.pdf
│   ├── GT_Survival_Guide.pdf      # 4-page condensed exam cheat sheet
│   └── GT_Short_Notes.pdf         # Problem-solving intuition & tricks
│
├── lecture_notes/                 # Standalone LaTeX source files & preamble
│   ├── preamble.tex               # Master visual styling (tcolorbox, palettes, TikZ)
│   ├── Lecture_1.tex ... Lecture_32.tex
│   ├── GT_Survival_Guide.tex
│   └── GT_Short_Notes.tex
│
├── problem_statements/            # Practice problem sets & guided solutions
│   ├── Practice Problem Set 1.pdf ... Practice Problem Set 5.pdf
│   ├── Problem_Set_1_Solutions.pdf
│   └── Problem_Set_1_Solutions.tex
│
└── lectures/                      # Original handwritten lecture scans (Lectures 1–32)
    ├── Lecture 1.pdf ... Lecture 32.pdf
```

---

## Course Roadmap & Syllabus

The course develops the mathematical foundations of strategic interaction across five modules:

1. **Strategic Form Games & Nash Equilibrium (Lectures 1–10)**
   - Normal form representation $\langle N, (S_i), (u_i) \rangle$
   - Dominance: IESDS, order independence of strict domination
   - Pure and mixed strategy Nash Equilibrium
   - Kakutani's Fixed Point Theorem & proof of Nash's Existence Theorem
   - Continuous strategies: Cournot, Bertrand, and Hotelling models

2. **Two-Player Zero-Sum Games & Minimax Theory (Lectures 11–14)**
   - Maximin and minimax values, security levels
   - Von Neumann's Minimax Theorem ($\underline{v} = \bar{v}$)
   - Saddle points and the Rectangle Property
   - Linear programming formulation and duality

3. **Extensive Form Games with Perfect Information (Lectures 15–21)**
   - Game trees, decision nodes, and terminal utilities
   - Backward induction algorithm and Zermelo's Theorem
   - Subgame Perfect Equilibrium (SPE) and credibility of threats
   - Games with Chance (Nature) nodes
   - Kuhn's Theorem for perfect information games & determinacy of Chess

4. **Imperfect Information, Behavior Strategies & Kuhn's Theorem (Lectures 22–28)**
   - Information partitions $H = (H_i)_{i \in N}$ and the **Perfect Recall** condition
   - Mixed strategies vs. **Behavior strategies** ($b_i$)
   - Reaching probabilities $\rho(n; \sigma)$ and outcome equivalence
   - **Kuhn's Equivalence Theorem (1957)** and behavior strategy NE
   - Subgames in imperfect information trees and general SPE existence

5. **Incomplete Information, Correlated Equilibria & Auctions (Lectures 29–32)**
   - Strategic Form $\longleftrightarrow$ Extensive Form conversions
   - Harsanyi Games of Incomplete Information $\langle N, (T_i), p, S, (u_t) \rangle$
   - Ex-ante vs. Interim expected utility and **Bayesian Nash Equilibrium (BNE)**
   - **Agent Form Game representation** and BNE $\iff$ Agent Form NE equivalence
   - **Correlated Equilibrium (Aumann, 1974)**, traffic game, linear incentive constraints, and convex polytope geometry
   - **Auction Theory**: Independent Private Valuations (IPV) model, sealed-bid auction mechanisms

For the full detailed index with clickable links, see **[LECTURE_PDFS.md](LECTURE_PDFS.md)**.

---

## Compilation Instructions

All lecture notes are written as standalone documents importing `preamble.tex`. You can compile any note using standard `tectonic` or `xelatex`:

### Using Tectonic (Recommended)
```bash
cd lecture_notes
tectonic Lecture_32.tex
```

### Using XeLaTeX / TeX Live
```bash
cd lecture_notes
xelatex Lecture_32.tex
```

---

## AI Distillation & Contribution Guide

To maintain uniform typography, color palette, and pedagogical quality across all current and future lectures, consult **[AI_DISTILLATION_GUIDE.md](AI_DISTILLATION_GUIDE.md)**. It provides explicit rules on:
- Zero skipping policy (100% mathematical fidelity)
- Color-coded box environments (`defbox`, `thmbox`, `exbox`, `warnbox`, `notebox`, `intubox`, `takebox`)
- Mathematical typesetting for payoff matrices, game trees, and strategy profiles
- Gap-filling and reconstruction of smudged or ambiguous handwriting
