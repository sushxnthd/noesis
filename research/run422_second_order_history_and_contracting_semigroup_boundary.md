# R422 — Second-order neutral-word history and finite-memory identifiability

**Date:** 2026-10-25  
**Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles  
**Outcome:** retrospective stage-1 feasibility PASSED; frozen conjunctive stage-2 primary FAILED (one full certificate, not two architectures). No prospective training or publication-grade novelty.

## Pre-outcome freezes and sample

Stage-1 protocol SHA256 `65f3d1e94d4447a0bfb151f9c36ea78ff49e0fb7a2701b22cf7cd9f355c12531`. Stage-2 scientific protocol SHA256 `0b327948125ad98df815c7f1c795f52dc705b3b80ab74817ab0c5ade688485dd`. Exact classical theorem protocol SHA256 `228b139d3b22cd0114f44862594055d0070619edaf9736eab693ac9a5dd60d51`.

Eight immutable R418 Task-B class-size-eight contexts were preselected: all four originally two-word-certified cases and four negative controls. The full 108-context R418 universe was tracked; 100 contexts remained unevaluated in this R422 pilot. No new neural weights were trained.

The new graph has 64 nodes indexed by ordered pairs of the last two full-DFA-neutral lexical-class words, with all 512 edges `(i,j) --k--> (j,k)`. Each word has length 20 and matches the 1–5-gram histogram and boundary conditions. Centers were computed from the exact-zero prefix followed by `u^14` and the two node words, with serialized binary64 centers and weights interpreted as exact dyadics. The only certified entry histories are prefix+`u^16` and prefix+`u^14 v^2`. The frozen scales were 2, 8, 32, using the original R418 residual-based coordinate radii. All proof inequalities used 1024-bit directed MPFR.

## Neural feasibility and exact-real certificates

**Stage 1 PASSED all frozen gates:** two of four original positives across LSTM and MGU met complete 64-node point-image coverage, entry and oracle-readout conditions. Three of four negative controls failed; one MGU control also met point feasibility but was not reclassified as an original positive. Thus three of eight total cases met point feasibility. The other two LSTM positives had strict MPFR point-image exclusions. The stage-1 raw records contain 2,052 directed MPFR point-edge checks. Point coverage alone does not prove invariant boxes.

**Stage 2 frozen conjunctive primary FAILED:** exactly **one** complete 64-node graph certificate, versus the frozen requirement of at least two across two architectures.

- **Positive:** LSTM Task B, seed 99960, complete DFA state `2|1`, scale 8. Both frozen exact-zero entry states lie in their prescribed nodes. All 64 node boxes have strictly correct suffix-1 oracle readout. All **512/512** full-word graph edges satisfy strict 1024-bit directed-MPFR uniform interval-Jacobian/residual mean-value inclusion, with minimum certified slack lower bound **4.509035263719461e-7**. Classical graph induction gives conditional **all-future correct readout under arbitrary switching among all eight lexical-class neutral words after either specified entry**, for the idealized exact-real network.
- **Negative:** the same LSTM failed scale 2 at edge `(5,4) --4--> (4,4)`, coordinate 6, where the mean-value lower bound exceeded the frozen radius. MGU Task B seed 99963 state `2|1` failed the frozen interval-Jacobian inequality at scales 2, 8 and 32, at edge `(7,6) --2--> (6,2)`. The MGU upper enclosure exceeded the radius while its lower enclosure did not; this is a **failure to certify**, not proof of actual instability or incorrect retention.

The first sequential exact-Jacobian implementation was interrupted due runtime and preserved with its logs. A separately frozen **implementation-only** change prioritized candidate edges using approximate Torch Jacobians, but made **every scientific decision solely with directed MPFR**. Four exact-MPFR workers checked 31 stored 16-edge chunks plus 16 priority edges for the successful LSTM: 512 distinct edges, all with positive strict slack. The frozen scientific radii, cases, graph and gates were never changed.

## Independent checks and finite observations

A separate 320-digit mpmath.iv recurrence agreed on 11/11 selected point-image inclusion/exclusion decisions. An independent interval forward-mode Jacobian implementation and directed MPFR agreed on **7/7 actual selected uniform-Jacobian edge decisions**. Two exploratory *expected-pass* labels for MGU were contradicted by **both** interval backends and preserved. This selected audit does not independently verify all 512 edges or establish formal correctness of mpmath.iv transcendental outward rounding.

Eight cases × two entry histories × six frozen switching patterns × n=0…512 yielded **96 trajectories and 49,248 float64 classifications**. First errors occurred at n=1 in 20 trajectories, n=3 in four, and n=6 in four; 68 had no observed error through n=512. All 12 trajectories for the certified LSTM case had no finite contradiction. Exact stdlib DFA/neutral-word and suffix-1 oracle checks passed on all **49,248** switched contexts, with 384 lexical checks. NumPy, Numba, Torch and 120/160/220-digit calculations agreed on **84/84** selected classifications. These finite results are not the basis of the infinite-horizon certificate.

## Exact classical history-order lower bound

For every integer `m >= 2`, define the two abstract neutral-transition maps
`F_a(y_1,...,y_m)=(y_2/2,...,y_m/2,a)`, `a in {0,1}`, from zero. Both are globally Euclidean **1/2-contractions**. A length-m history `h` reaches `(h_1/2^(m-1),...,h_m)`. The fixed affine-threshold readout `1[y_1>2^-m]` has reachable-state margin `2^-m`.

Any two distinct histories first differing at position j are distinguished in readout after a common continuation of length j-1; all shorter continuations are observationally identical. Hence the minimal exact Moore machine has **2^m** future-output-distinguishable states, with worst-case depth m-1. Remembering only the last k<m neutral words is insufficient in this family. The construction gives `N=2^m=1/margin`, showing that a uniform contraction factor alone does not bound required history order independently of dimension and margin.

Independent exact Fraction checks covered **43,434 unordered history pairs** across m=2,…,8, with independent SymPy checks for m=2,…,5. This is **classical automata/affine-system science**, not a new RNN theorem or exact learned-LSTM realization.

## Limitations, prior art and next work

The graph-induction method is classical; see Ahmadi, Jungers, Parrilo and Roozbehani, *SIAM Journal on Control and Optimization* (2014), DOI 10.1137/110855272, and Angeli et al., *Path-Complete Graphs and Common Lyapunov Functions* (2016). Future-output distinguishability is classical Myhill–Nerode/Moore theory. The single LSTM certificate is retrospective, architecture-limited and conditional on the MPFR exact-real model, not an IEEE/Torch execution theorem or publication-grade neural novelty. **The frozen cross-architecture primary remains failed.**

**R423 direction:** stop enlarging or retuning graph certificates. Instead freeze quantitative finite-data/parameter identifiability and future-output distinguishability hypotheses for actual archived learned RNN neutral-transition semigroups, with strong n0…2 margin/CE/d32 baselines, independent numerical checks and no fresh cohort until non-ceiling feasibility is demonstrated.

Complete frozen protocols, original source, errors, all negative cases, 31 MPFR edge chunks, 43,434 exact pairwise witnesses, 49,248 finite raw classifications, independent checks and immutable nested prior checkpoints are preserved in the local archive `NOESIS_R422_Reproducibility.zip`, SHA256 `4a8e091d54dea17788da7d5f2e41b45301f86fd621f8fdb7b34eec0447447986`. Raw data are not uploaded to GitHub. No personal spend, user-laptop access, new branch/PR, force push or merge.
