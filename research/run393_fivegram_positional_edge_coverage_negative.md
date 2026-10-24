# NOESIS R393 — five-gram/position-matched movable-edge curriculum (negative)

**24 October 2026.** Kernel: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Second consecutive prospective failure of the DFA-edge-coverage mechanism (R392–R393); retire edge-exposure reallocation as flagship.** This is not a novel law or publication-grade discovery.

## Pre-registered experiment

- No-model-outcome pilot freeze SHA256 `e407cb3368c2f22aff83bfdd002b29935f7e34c0391eee5b5e92d8e749054cff`; feasibility freeze `da9b32dac2f6aadec4e4fc9798fc5847944a5bafafe0e38cf39bdd3ea7120489`.
- Complete frozen training/test design SHA256 `46c3a2cdf889b7b0592d3eacd47afba2641d86f4f30714f593ef29d9699b47f3`; confirmatory protocol SHA256 `79e57035fc8b99363a4db21a1ec598222a0927054394cb1cfd3052dd6c28254f`. All freezes preceded fresh model training and held-out outcomes.
- 144 **fresh** networks: 3 architectures (LSTM, GRU, MGU-style), 2 complete-DFA tasks, 8 shared seeds 94000–94007, 3 seed-matched arms (iid, lexical, targeted). Identical initial parameters per seed/architecture/task, 196 length-20 training strings, 160 Adam updates. All 144 short-perfect; all seeds retained ITT.
- Training words: exact **1–5-gram multiset** and first/last-four-bit matching per word between lexical and targeted arms; exact **aggregate bit-position marginals at all 20 positions** enforced with SciPy/HiGHS MILP. Targeted arm maximizes pilot-undercovered *movable non-event* DFA edge exposure, with no model-outcome feedback.
- Test: 10-bit prefixes from every complete DFA state and independent 20-bit full-state-neutral five-gram-matched word pairs. **7,776 full n0..512 suffix-1 trajectories** (3,989,088 per-cycle labels), raw traces and margins preserved.
- Frozen task-B conjunctive primary: targeted minus lexical n256 oracle accuracy >=+3 pp, targeted minus iid >=+2 pp, exact one-sided 8-shared-seed sign-flip p<.05 for both, nonnegative all architectures, target-edge exposure increase each seed, short accuracy regression <=1 pp.

## Results: primary FAILED

Manipulation succeeded: task-B target edge (residue2,previous0,input0) exposure increased from mean **227.75** to **332.75** per 196-word curriculum (**+47.21%** mean relative increase across seeds); task-A target (residue2,input0) increased 573.50 to 733.50 (**+28.05%**). All 8 seeds improved on both tasks, with all lexical and position constraints satisfied.

Task-B n256 suffix-1 accuracy, 576 cases per architecture/arm:

| Architecture | iid | lexical | targeted |
|---|---:|---:|---:|
| LSTM | 576 | 573 | 576 |
| GRU | 576 | 576 | 576 |
| MGU-style | 576 | 576 | 576 |
| **Total /1728** | **1728** | **1725** | **1728** |

Targeted minus lexical **+0.173611 pp** (frozen threshold +3 pp), exact shared-seed p **0.5**, bootstrap 95% CI **[0,+0.520833] pp**; targeted minus iid **0 pp**, p **1.0**. The three lexical errors all came from **one LSTM seed 94000** and began by n1. All other n256/n512 classifications correct; count-ones task all correct. Crucial **ceiling/power limitation**: with lexical accuracy 1725/1728, even perfect targeted accuracy could improve only 0.173611 pp; the frozen +3 pp threshold was impossible in this realized cohort. This is a failed confirmatory design, **not proof edge exposure never matters**. Do not retune or reverse the frozen primary.

## Independent verification

- 9,408 training-string instances, 3,136 exact five-gram checks, 320 exact position constraints, all passed.
- Independent NumPy vs Numba: **324/324** selected classifications agree across nine horizons.
- All three outcome-selected lexical n256 errors plus six SHA256-stratified controls: **9/9** agree at 120/160 digits; one error additionally 220 digits.
- All three lexical-versus-targeted n1 classification differences conditionally certified by 100-digit `mpmath.iv` directed finite-string intervals with exact serialized binary64 weights; no n256 invariant-set theorem.
- Exhaustive binary enumeration found the shortest exact-five-gram/boundary-equivalent pair with different movable DFA-edge counts at length **10** for both tasks: `0000010000` versus `0000100000`. Elementary combinatorial counterexample, **not novel**.

## Scientific decision and limitations

R392 and R393 are two unsuccessful prospective edge-coverage primaries. Retire simple DFA-edge-exposure reallocation as flagship. Continue the **same kernel** with separately pilot-calibrated, non-ceiling **counterfactual neural transition distinguishability under oracle-neutral word composition**, freeze a sharp predictive/causal test before fresh seeds, require superiority over earliest-response baselines and independent multi-architecture replication. Do not infer infinite-horizon correctness from finite traces. High-order (6+) lexical and joint positional support remain uncontrolled even here.

Prior art: Weiss, Goldberg & Yahav ICML 2018 automata extraction; Brandoit et al arXiv:2609.32447 finite-precision state tracking; further Dan/Bastani/Roth, Merrill/Tsilivis, Muškardin, Vogt, Buitrago/Gu and Metric Automata Theory audit needed.

**Full raw evidence** is preserved off GitHub in SHA256-verified 62-file `NOESIS_R393_Reproducibility.zip`, SHA256 `f6e0b992f3fc4e144f1ed383edb4575f8bd657d494ac0e613ad05d911e7159e7`. Includes frozen protocols, 144 serialized checkpoints, all trajectories, independent checkers, high precision, conditional interval results, source, exact statistics, negatives and figures. No user laptop or paid API used. Existing branch/PR only; no merge/force-push.
