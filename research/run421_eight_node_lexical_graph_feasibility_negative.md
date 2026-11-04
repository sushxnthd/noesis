# NOESIS R421 — eight-node lexical-class graph feasibility failed

**Date:** 2026-10-25. **Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. Retrospective feasibility only; no prospective replication or new neural theorem.

## Frozen protocol

The pre-outcome protocol SHA256 was `fe1f67d82c175bb1d638f9e9cf64ef9e76a86309ba1b89f8a214610aa5acde42`. It fixed eight immutable R418 Task-B class-size-eight contexts: all four original R418 graph positives (three LSTM, one MGU) and four GRU/MGU negative controls selected by fixed seed/architecture rules. The remaining 100 of the original 108 R418 contexts were retained as **unevaluated** in this limited pilot, not treated as a confirmatory all-ITT cohort. No retraining or checkpoint selection.

Each of eight nodes was centered at the float64 state reached from zero after the fixed 14-bit prefix, 14 repetitions of the original `u`, and two repetitions of its corresponding class word `w_i`. Centers and model weights were interpreted as exact binary64 dyadics. The fixed graph demanded every edge `i --w_j--> j` (64 edges), all exact entry inclusions, and correct oracle suffix-one readout on every box. Coordinate radii were `2^-20 + scale * max(original four-node residuals)` for predeclared scales 2, 8, 32. Every center-image test used 1024-bit directed MPFR. The frozen gate required 2–3 positive cases across >=2 architectures and >=1 negative control; expensive uniform interval-Jacobian graph certification was explicitly gated on stage-one success.

## Frozen primary: FAILED

**1/4** original positives passed all 64 point-image edges, entry and readout: `mgu|substring01|99963|2|1`. The three LSTM positives failed; all four negative controls failed. At scale 32 the four positive contexts covered **8/64, 10/64, 5/64, 64/64** point edges, respectively. Both `positive_min` and `positive_two_arch` gates failed. No uniform interval-Jacobian all-future certificate was attempted; even the MGU success is **point coverage only**, not an infinite-horizon switching certificate. No frozen threshold or geometry was retuned.

## Separately frozen exact-real diagnostic

Post-primary diagnostic SHA256 `61d9edbbf6ea17cf349207569181e26953a6d55017eb77c5b336dcdf659385aa` measured the necessary radius scale for all prescribed edges, without changing centers or targets. Rigorous 1024-bit MPFR lower bounds for the four positive contexts were **954101.9074, 4780.8720, 684114.7263, 0** in the original order. Thus three of four require scale strictly greater than the frozen maximum 32; they had **513/640, 480/640, 525/640** strict coordinate misses at scale 32. These are bounds for the *specified* center/radius/target family, not a global neural impossibility or actual memory failure.

A separate classical rational affine shift register `F_a(x,y)=(y/2,a)` on alphabet `{0,1,2}` has nine distinct two-symbol states `(b/2,a)`, with **27/27** exact graph edges. Any one-box-per-last-letter construction containing all corresponding states needs first-coordinate radius >=1/2, whereas nine singleton two-symbol boxes suffice. Fraction checked **9,837** strings of lengths 2–8, and independent SymPy checked all 27 edges. This is elementary classical finite-state geometry, not an exact learned-RNN theorem or novelty.

Independent audit SHA256 `ade462ddc19b7f472485b8b124241cbd0fc3457cbcb3fbc173f94c71c28ff959` used a separate 320-decimal-digit mpmath interval recurrence on three strict-exclusion witnesses and one MGU inclusion: **4/4** decisions matched directed MPFR. No invalid approximate Torch-Jacobian-in-exact-interval gate was used.

## Interpretation and direction

The **eight-node last-word lexical-class graph construction** failed its frozen cross-architecture feasibility criterion. This does not invalidate R418's two-word certificates, actual trained-network retention, all-word semigroup safety, or graph certification with different states/geometry. The lone MGU point-cover success cannot be promoted without uniform interval-Jacobian proof.

**R422:** change mechanism to a separately frozen history-order/semigroup-state-identifiability study, testing predeclared second-order histories (up to 64 nodes) and minimal distinguishable-history equivalence classes before any new neural training. If feasibility fails, pursue exact finite-data/parameter-identifiability bounds rather than radius rescue. Classical de Bruijn/path-complete graphs and automata distinguishability are prior art; no novelty claim.

All seeds, source, raw point-image outcomes, negative controls, frozen protocols, quantitative diagnostics, independent checks and the immutable R420 dependency are preserved in SHA256-verified `NOESIS_R421_Reproducibility.zip` (SHA256 `61c62828df576ca59ace0d86e8816ac51f51077a04c70a198adc72bff224a3d8`). Full raw/checkpoints are archived, not committed. No personal spend, user-laptop use, branch creation, PR creation, merge or force push.
