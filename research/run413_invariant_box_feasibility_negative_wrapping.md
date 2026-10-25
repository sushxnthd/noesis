# NOESIS R413: invariant-box feasibility negative and exact wrapping obstruction

**2026-10-25.** Same scientific kernel: learned DFA-state retention under full-state-neutral cycles. Retrospective feasibility, not prospective neural replication or novel theorem.

## Frozen certificate attempt

Pre-outcome R413 protocol SHA256 `bcfaa617f5f28f5599e7dbee4a372e02a6eca50bc0c88b59accbc36cffe06837`. Exactly 18 immutable R411 ERM checkpoints: LSTM/GRU/MGU-style × both DFA tasks × seeds 99920–99922, first complete DFA state, first held-out prefix and neutral word. Full-state-neutral 20-bit word, state at n16. Four predeclared box radii `2^-30, 2^-20, 2^-12, 2^-8`. All seeds/cases intention-to-test. mpmath.iv 70-decimal-digit interval propagation of exact binary64 weights; frozen success required at least six invariant, correct-oracle readout boxes spanning both tasks, two architectures and three seeds.

**FAILED: 0/18 full certificates.** Seven cases had n16 contained in at least one candidate box; ten had a correct-oracle readout bound; zero had a strictly invariant box. Interval widths after 16 cycles often became enormous (up to >243) because of interval dependency/wrapping. This is **not evidence of true state explosion, not a falsification of actual neural retention, and not a certified global contraction theorem**. No radius/horizon/seed/word retuning and no confirmatory cohort.

## Independent exploratory diagnostics (not promoted)

Post-failure frozen diagnostic SHA256 `21141ad0e7c3174a65ae47feff1d364e3a2f039a023f5d61dddfe306f2b8ae3f`. Torch-autograd pointwise neutral-word Jacobians at n16: all 18/18 had `rho(J)<1` and `rho(|J|)<1`; max independent centered finite-difference discrepancy `1.6811e-8`. **Pointwise** Jacobians do not validate contraction on any neighborhood or prove invariance. Separate frozen HP selection SHA256 `56161fe365af6240fc9a13371532e730603742a3bfc9cf4dea03d4fc128f1990`: 6/6 selected suffix-1 classifications agree across independent NumPy/Torch/120/160/220-digit mpmath, maximum n16 state discrepancy <=6.67e-16; no interval certificate.

## Separate exact rational counterexample

Exact audit protocol SHA256 `eedc686364ef1f460d739268202ef39511c1a66899651e76cd269cb5009b8ea8`. For `A=(3/5)[[1,-1],[1,1]]`, `A^T A=(18/25)I`, hence `||A||_2=3sqrt(2)/5<1`; yet `rho(|A|)=6/5>1`, so direct interval propagation of centered square radius r produces radius `(6/5)^n r`, and no positive weighted axis-aligned box centered at zero is invariant. Fraction checker 12/12 predeclared n/r pairs and separate SymPy exact checks passed. Classical interval wrapping obstruction, **not** a novel RNN result.

## Decision and preservation

Retire the simple axis-aligned interval-box certificate candidate. Next *distinct* feasibility approach: a posteriori residual plus validated interval-Jacobian/coordinate-transformed enclosure, frozen anew and explicitly checked against classical prior art and R378. No claims from a finite trace or pointwise Jacobian. Complete raw/source/checkpoints/negative results/frozen protocols/independent checks are in SHA256-verified `NOESIS_R413_Reproducibility.zip`, digest `f03f178bf57c47602da975d811ee77c8d98634dda4300bdb3566e995151e3b99` (33 entries, includes immutable R412 dependency and its R411 checkpoints). Full raw is **not** pushed to GitHub.

No personal spending, no user laptop, no new branch/PR, no merge or force-push. Authorized PR #22 remains draft and open.
