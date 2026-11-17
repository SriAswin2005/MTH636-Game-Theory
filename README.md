# MTH636: Game Theory -- Complete Coursework & Distilled Notes

[![Course](https://img.shields.io/badge/Course-MTH636%20Game%20Theory-blue.svg)](.)
[![Lectures](https://img.shields.io/badge/Lectures-37%20Complete-green.svg)](lecture_pdfs/)
[![Notes](https://img.shields.io/badge/Format-Digitalized%20PDFs-orange.svg)](lecture_pdfs/)
[![Problem%20Sets](https://img.shields.io/badge/Problem%20Sets-1%20to%205-purple.svg)](problem_statements/)

A complete, digitalized, and typeset archive of **MTH636: Game Theory**. This repository contains unabridged, color-coded digitalized PDFs for all 37 lectures, quick-reference survival guides, problem sets, and guided solutions.

---

## Repository Structure

```text
├── README.md                      # Repository overview & syllabus map
├── LECTURE_PDFS.md                # Comprehensive catalog of all 37 lecture PDFs
├── .gitignore                     # Build artifacts, OS files, and caches
│
├── lecture_pdfs/                  # Final compiled lecture note PDFs
│   ├── Lecture_1.pdf ... Lecture_37.pdf
│   ├── GT_Survival_Guide.pdf      # 4-page condensed exam cheat sheet
│   └── GT_Short_Notes.pdf         # Problem-solving intuition & tricks
│
├── problem_statements/            # Practice problem sets & guided solutions
│   ├── Practice Problem Set 1.pdf ... Practice Problem Set 5.pdf
│   ├── Problem_Set_1_Solutions.pdf
│   └── Problem_Set_1_Solutions.tex
│
└── lectures/                      # Original handwritten lecture scans
    ├── Lecture 1.pdf ... Lecture 32.pdf
    └── Lecture 33-37.pdf
```

---

## Course Roadmap & Syllabus

The course develops the mathematical foundations of strategic interaction across five modules:

1. **Strategic Form Games & Nash Equilibrium (Lectures 1--10)**
   - Normal form representation $\langle N, (S_i), (u_i) \rangle$
   - Dominance: IESDS, order independence of strict domination
   - Pure and mixed strategy Nash Equilibrium
   - Kakutani's Fixed Point Theorem & proof of Nash's Existence Theorem
   - Continuous strategies: Cournot, Bertrand, and Hotelling models

2. **Two-Player Zero-Sum Games & Minimax Theory (Lectures 11--14)**
   - Maximin and minimax values, security levels
   - Von Neumann's Minimax Theorem ($\underline{v} = \bar{v}$)
   - Saddle points and the Rectangle Property
   - Linear programming formulation and duality

3. **Extensive Form Games with Perfect Information (Lectures 15--21)**
   - Game trees, decision nodes, and terminal utilities
   - Backward induction algorithm and Zermelo's Theorem
   - Subgame Perfect Equilibrium (SPE) and credibility of threats
   - Games with Chance (Nature) nodes
   - Kuhn's Theorem for perfect information games & determinacy of Chess

4. **Imperfect Information, Behavior Strategies & Kuhn's Theorem (Lectures 22--28)**
   - Information partitions $H = (H_i)_{i \in N}$ and the **Perfect Recall** condition
   - Mixed strategies vs. **Behavior strategies** ($b_i$)
   - Reaching probabilities $\rho(n; \sigma)$ and outcome equivalence
   - **Kuhn's Equivalence Theorem (1957)** and behavior strategy NE
   - Subgames in imperfect information trees and general SPE existence

5. **Incomplete Information, Correlated Equilibria & Auctions (Lectures 29--37)**
   - Strategic Form $\longleftrightarrow$ Extensive Form conversions
   - Harsanyi Games of Incomplete Information $\langle N, (T_i), p, S, (u_t) \rangle$
   - Ex-ante vs. Interim expected utility and **Bayesian Nash Equilibrium (BNE)**
   - **Agent Form Game representation** and BNE $\iff$ Agent Form NE equivalence (Lecture 32)
   - **Correlated Equilibrium (Aumann, 1974)**, traffic game, linear incentive constraints, and convex polytope geometry (Lecture 33)
   - **Auction Theory (Lectures 34--37)**: IPV model, sealed-bid auctions (first-price, second-price)
   - Dominant strategy (truthful) BNE in second-price auctions; multiple equilibria (Lectures 35--36)
   - English (open ascending-bid) auctions and strategic equivalence (Lecture 36)
   - First-price auction equilibrium: bid shading and symmetric BNE derivation (Lecture 36)
   - **Revenue Equivalence Theorem**: first-price = second-price expected revenue (Lecture 37)

For the full detailed index with clickable links, see **[LECTURE_PDFS.md](LECTURE_PDFS.md)**.
