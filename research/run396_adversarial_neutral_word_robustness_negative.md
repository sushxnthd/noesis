# NOESIS Run 396 — adversarial neutral-word robustness, prospective negative

**Date:** 2026-10-24. **Kernel:** learned DFA-state retention under full-state-neutral cycles. **Status: FROZEN CONJUNCTIVE PRIMARY FAILED.**

Design frozen before pilot: SHA256 `a9b8a941d2f278a3c4a4aeae91987d050454e489c8c4ee9f3777dfaa650a1afc`. Separate R395 pilot seeds 96000–96001 selected two groups per complete DFA state, frozen selection SHA256 `5fa98c6a3b47d1ff20d45453a9a00bc8f891cd3d728e00f8f9b084b256ba3e1e`. Confirmatory protocol frozen **before new training** SHA256 `9fb8d5f38959e7ed26c7b137876c4d52bf3c8fabc74316ca61204d74553b9a60`.

Trained **48 fresh** LSTM/GRU/MGU-style networks, two DFA tasks, eight shared seeds 97000–97007, matched 196 length-eight training strings, 160 Adam steps. **48/48 short-perfect; all ITT.** Held out 1,296 paired cases, 2,592 complete n0..512 trajectories (1,329,696 one-bit labels). The causal input-order/composition contrast uses fixed 16-bit u and two different 16-bit neutral continuations selected by the separate pilot; the 32-bit arms match **exact overlapping 1–4-gram counts and three-bit endpoints**, symbolic full-DFA action, and initial neural state. Five-gram and positional support remain unmatched.

**Frozen task-B primary:** among 852 n0-correct eligible pairs, n2 oracle errors were **90 adversarial vs 69 control**, +**2.4648 percentage points**, below required +5pp. Exact eight-seed one-sided sign-flip **p=20/256=.078125**, not <.05; bootstrap 95% CI **[-.3488,+5.5425] pp**. Architecture effects LSTM +.360pp, GRU +4.895pp, MGU +2.083pp. The conjunctive primary **FAILED**; no thresholds changed or directional reversal. Task A n2 0/432 adversarial vs 3/432 control, secondary reversal. Most task-B differences already visible n1; no first oracle error after n32.

**Important caveat:** Three task-B GRU adversarial rows from seed 97007 alternated classifications every cycle n33..512 despite n256=n512 agreement; these late traces are **posthoc and NOT high-precision arbitrated**, not exact periodic-orbit proof. No n256 invariant-set theorem.

**Verification:** 14,256 stdlib-only symbolic checks over 162 candidate groups and all held-out pairs; independent pure NumPy vs Numba 294/294 selected labels through n512; six n2 arm labels converged at 120/160/220 digits; six n2 labels conditionally certified with 100-digit `mpmath.iv` directed intervals from exact serialized binary64 prefix-end states. Finite-string certificates only. Candidate generator used nonoverlapping `str.count` for preliminary grouping, but independent overlapping Counter checks confirmed **all 162 groups and every held-out pair** actually satisfy the required overlapping 1–4-gram equivalence.

Full raw/checkpoints/pilot/protocol/source/negative results/checkers archived locally as `NOESIS_R396_Reproducibility.zip`, SHA256 **`557ae2574e5d8530df673e2b11189562cf145aa61cad1b6ec6a59aeb211b2e93`**, 51 SHA256-verified entries. Full raw is **not on GitHub**. No novel law or publication readiness.

**Next:** second independent prospective adversarial robustness test using genuinely 5-gram/position-matched compositions and a frozen finite-horizon certified readout-margin predictor against n1/n2 margins, with non-ceiling pilot incidence. Two failed primaries => change mechanism; three => kill/reformulate. Do not tune R396 holdout.
