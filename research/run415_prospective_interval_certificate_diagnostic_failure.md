# NOESIS R415: prospective neutral-word interval certificates and diagnostic falsification

**Frozen conjunctive primary: FAILED (8/9 gates).** This is not a successful frozen primary, not publication-grade novelty, and not a formal IEEE floating-point execution theorem. The separate prospective numerical certificate outcomes are useful but must not be relabeled.

## Pre-outcome protocol and cohort

- Fresh design SHA256: 41ff0e8a62c3fc8b29863dbbbff84a285673298c56fcc51b03f4c67adfd8b58b.
- Fresh quantitative protocol SHA256: 5a8aaf2a7b19ab3764b869df8fee8d684c5a779999496c4341039f1ef27aeda3. Both frozen before any R415 neural training/outcomes.
- 24 new float64 ERM networks: LSTM, GRU, MGU-style x Task A/B x four disjoint seeds 99940–99943. Same 196 length-8 training strings and 50 Adam updates, all models intention-to-test. All six architecture/task mean short accuracies exceed frozen .95.
- 216 fresh contexts across all 3 Task-A and all 6 Task-B complete DFA states, one unseen 14-bit prefix and two unseen 20-bit neutral words/state. Word twins match exact overlapping 1..5-gram histograms and four-bit boundaries. All seeds, prefixes and words disjoint from R410/R411 and R413/R414.
- Frozen radii 2^-36, 2^-28, 2^-20, 2^-12. Exact binary64 serialized weights interpreted as dyadic real numbers, n16 state enclosed from exact zero with 240-decimal-digit mpmath.iv. Full-box 20-symbol interval forward-mode Jacobian, mean-value residual invariant inequality, and oracle suffix-1 readout dominance.

The classical sufficient condition is: if the exact n16 state lies in B(c,r), each coordinate obeys |F_i(c)-c_i| + sum_j sup_B |dF_i/dx_j| r_j < r_i, and the correct suffix-1 logit dominates throughout B, then repeated application of this *one fixed neutral word* preserves the oracle readout for all n>=16 in the exact-real recurrence. No arbitrary-word switching or finite-precision execution claim.

## All prospective outcomes

**137/216 conditional numerical certificates**: Task A 64, Task B 73; LSTM 28/72, GRU 60/72, MGU-style 49/72; seeds 28/29/33/47. **79 negatives preserved.** 136 positives passed at radius 2^-36, one at 2^-28. Minimum positive invariance slack lower bound 5.0514e-13; minimum oracle margin lower bound .101146. Naive direct interval-image invariance baseline **0/216**.

Frozen primary required >=12 positives, >=4/task, >=2 architectures, >=3 seeds, >=6 negatives, all 24 models ITT, six short-accuracy means >=.95, **and every approximate Torch float64 point Jacobian inside the interval Jacobian at every radius**. The first eight gates passed, the last FAILED: 34/216 contexts and 114/864 radius checks (all LSTM/Task B) had approximate Torch Jacobian elements outside the narrow exact-real interval. **No gate removed or threshold retuned.**

## Independent MPFR and methodological falsification

Independent audit specification SHA256 db1a2897f28f2f642ac040340c91725e73f34c55b594a9ea601f578d56aca6dd was frozen before complete certificate outcomes, but after partial evaluation began. SHA256-stratified post-outcome selection (selection SHA256 423369f1574f369d9a36dde98362cecf32ce3c250b040a5a4664f5aa86909ae4) chose one positive from each of six architecture/task cells and two negatives, before any independent MPFR/HP checks.

- Independent 1024-bit libmpfr.so.6 RNDD/RNDU interval implementation, not the mpmath.iv code; 3,741/3,741 deterministic exact-rational and exponential selftests passed.
- **32/32** selected MPFR-vs-mpmath certificate decisions agree across all four frozen radii: six positives (one per architecture/task cell), two negatives. MPFR validation is limited to these selected cases; not all 137.
- **32/32** selected n0,n1,n2,n16 labels agree across independent NumPy, Torch and 120/160/220-digit pointwise calculations; maximum state discrepancy 8.88e-16, logit discrepancy 4.22e-15.
- Separately frozen POSTHOC Jacobian diagnostic selected three cases with Torch point-Jacobian exclusion. Torch was outside in 27/100, 27/100, 9/100 entries, whereas the independent **MPFR exact-real point derivatives were inside both the MPFR and original mpmath interval Jacobians in 300/300 entries**. Max exact-MPFR-vs-Torch differences 6.37e-15, 7.03e-15, 7.87e-15. Thus the frozen Torch-point inclusion gate is a scientifically invalid *necessary condition* for exact-real interval enclosure: approximate float64 derivatives can lie outside a correct narrow exact-real interval. This does **not** rescue the frozen primary.

## Full finite trajectories and limitations

All 216 contexts have complete n0..512 full hidden states, signed margins and labels: 110,808 float64 classifications, odd/even cycles, first errors, n0..2 margins, n32 state displacement, and depth0..4 DFA quotient checks. Independent stdlib: 108 matched 1..5-gram pairs, 216 neutral/oracle checks, 1,080 quotient checks, all 216 raw reconciled. **Zero** certified-case finite contradictions from n16..512.

All 70 finite oracle-error contexts first failed at n0 (38), n1 (28), or n2 (4). The n0..2 baseline already identifies these finite errors, so no additional finite-horizon predictive superiority is established. Of 146 finite-error-free cases, 137 were numerically certified, nine were not. A sufficient invariant certificate is not a necessary condition.

The method is classical validated numerics (Krawczyk, Alefeld, Lohner, interval Jacobian mean-value bounds). Conditional mpmath.iv numerical outcomes, selected independent MPFR checks, and a methodological float64-gate counterexample are **not** publication-grade new neural-memory mathematics. No exact-real theorem is claimed for other words, other weights, arbitrary switching, or IEEE execution.

## Next scientific direction

R416 should freeze a distinct **MPFR-first shared-invariant-set pilot for two neutral words**, testing arbitrary switching/concatenation of the two word maps after certified entry. Remove the logically invalid Torch-point diagnostic only in a genuinely NEW frozen R416 protocol, never by retroactively changing R415. First test retrospective feasibility on immutable R415 checkpoints, then independently freeze fresh prospective cohorts only if feasible. This is a stronger transition-semigroup question, not merely another point-Jacobian fit.

**Reproducibility:** full 52-entry SHA256-verified local archive NOESIS_R415_Reproducibility.zip, SHA256 b6e6c8db9834ff39e4cc4b624718b146fad3ff08353545fae3ad220cf7088468. Includes every raw trajectory, 24 checkpoints, all negatives, frozen manifests, independent MPFR/HP, source and immutable R414 dependency. Raw stays off GitHub. Existing branch only; PR #22 remains draft/unmerged. Zero personal spending and no user laptop.
