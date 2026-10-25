# NOESIS R412 — Exact finite-trace identifiability boundary for full-DFA-neutral operators

**25 October 2026.** Kernel unchanged: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Decision:** mathematical boundary audit completed, no new neural model trained, no publication-grade novel theorem or exact LSTM/GRU/MGU realization. R410–411 training-objective mechanism remains retired.

## Frozen design and independent audit

Pre-outcome exact protocol SHA256 `23cc33e4a2f906f191c14de1c958f121b172a765e8351e0c40a3a1d0723bbb17`. Main exact Fraction checker passed **21/21** preselected H in {1,2,3,5,8,13,17}, m in {0,1,2}. Independently implemented SymPy checker passed **9/9** disjoint H in {4,7,11}, m in {0,2,3}; **15/15** independent Hermite full-rank audits passed. No outcome-based selection or threshold retuning.

## Sharp polynomial finite-trace ambiguity (classical)

For any H>=1 and m>=0, define `F_bad(x)=x+1`, `F_good(x)=x+1-[prod_(j=0)^(H-1)(x-j)/H!]^(m+1)`, x0=0, and common affine readout `g(x)=x-(H+1/2)`. Both operators have **identical exact states x_n=n for n=0..H**, and identical transition derivatives through order m at every observed input x0..x(H-1). At H+1 the bad map reaches H+1 (class 1) while the good map reaches H (class 0) and stays there forever. This demonstrates finite-observation ambiguity; the difference polynomial has degree H(m+1), which is the **sharp Hermite interpolation threshold**. A known polynomial degree d < H(m+1) instead identifies the map uniquely from these exact jets. Classical, not novel.

## Stronger bounded analytic contraction counterexample

Let `B(x)=x/2+1/4`, `x_j=(1-2^-j)/2`, `q(x)=exp[-(x-x_H)^2] prod_(j=0)^(H-1)[(x-x_j)/(x_H-x_j)]^(m+1)`. Let `P(y)=sum c_k y^k` be the product with y=x-xH. The rigorous rational envelopes `B0=sum |c_k|k!`, `B1=sum |c_k|[(k! if k>0 else 0)+2(k+1)!]` bound `sup|q|` and `sup|q'|` on R, using `sup |y|^k exp(-y^2)<=k!`. Choose `delta=1/[2^(H+4)*16*(1+B0+B1)]`, `G(x)=B(x)-delta*q(x)`. Both maps are **real entire, globally strict contractions with Lipschitz constant <9/16, and map [0,1] into itself**. They have the same first H+1 states and all m-jets at observed inputs, yet at H+1 their states differ by exactly delta. The shared affine threshold `x_(H+1)-delta/2` yields opposite classes. Thus even *known strict global contraction plus analytic bounded-state dynamics* does not by itself identify the next class without sufficient readout margin. The constructed separation may be tiny. This is an abstract word-map counterexample, **not** a learned RNN realization or novel theorem.

## What *can* certify all-future retention

For a **rigorously known** global L<1 contraction on an invariant state region and affine readout g with Lipschitz constant K, all future classes are unchanged if
`|g(x_H)| > K * L/(1-L) * ||x_H-x_(H-1)||`.
The tail bound is the standard sharp Banach a-posteriori estimate. A pointwise Jacobian, empirical contraction, or finite sequence of correct predictions is insufficient. R408's conservative learned-RNN bounds were vacuous; **R412 did not certify a learned network**.

## Independent DFA and archived-neural checks

The words `0010010100` and `0010100100` share overlapping 1..5-gram counts and four-bit boundaries; independent exact DFA checkers verified both full-neutral for all task-A states and task-B states with previous bit 0, including 99 repetitions. This verifies symbolic embedding only.

Separate retrospective protocol SHA256 `68867d0a2456b23630191568ccd712fbb67318d00343fc63100bdd0f11513265` audited immutable R411 raw: **3,456 contexts, 216 preselected late contexts, 42,120/42,120 matching n0..64 overlaps**. ERM n0..2 oracle-correct followed by an error through n64: task A **2/1,063**, task B **19/1,230**; task-B n0..8 correct then error **1/1,212**. No new failures after n16 in these finite archived samples, **not** an infinite-horizon certificate. Late n512 classifications are unarbitrated float64. A descriptive-only initial script mixed horizons; both flawed and corrected versions/results are archived, frozen estimand unchanged.

## Preservation and next scientific decision

Full **21-entry SHA256-verified R412 reproducibility archive** `NOESIS_R412_Reproducibility.zip` SHA256 **`490787cc1791cee867e472889ac6aa794453d4b33e9e0b9d5a184b639abec46b`**, including all frozen protocols, full exact code/results, independent SymPy checker, descriptive negatives/error correction, complete detailed note and immutable R411 dependency. Full raw is in the archive, not this GitHub note.

**Next:** investigate whether a *non-vacuous rigorously bounded* neutral-word transition contraction and readout margin can be established on held-out actual RNN states. Freeze cases and success gates before neural outcomes; if no valid invariant region or certified L exists, report the feasibility failure rather than claim a theorem. Do not revive retired mechanisms. Prior art: classical Hermite interpolation and Banach fixed-point bounds; Kosut–Lau–Boyd 1992 set-membership identification; Weiss–Goldberg–Yahav ICML/ACL 2018. No publication-grade novelty claim.
