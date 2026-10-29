# NOESIS R444: Sharp hidden-box readout feasibility audit under physical neutral cycles

**Frozen conjunctive primary FAILED 13/15 gates.** Classical geometry and a retrospective neural audit; no neural causal breakthrough, prospective replication, or exact-real RNN theorem.

## Pre-outcome freeze and scope
Frozen protocol SHA256 `4c180b2ec9c902805f4a9b005493c1c5d4cc489da79571e4d13853a952e9f41b`; primary source SHA256 `1f110924af373572ffae43a6104e3c950f75e46b3bd1cc8079aa8e7f919e384d`. All 108 immutable R418 contexts, both tasks, LSTM/GRU/MGU, four seeds, original per-state legal 20-bit u/v words, original prefixes, cycles n=0,1,2,16,32, and actual suffix1. Original R425 early baselines unchanged. No training or post-outcome threshold retuning.

## Exact classical outer-box theorem
For affine logits z_j(h)=w_j·h+b_j and a correct oracle c at h0 in [-1,1]^d, write gamma_j=z_c(h0)-z_j(h0)>0 and v_j=w_j-w_c. For ||h-h0||inf<=epsilon and h in [-1,1]^d, the maximum rival-gap increase is exactly
`C_j(epsilon)=sum_{v_ji>0}v_ji min(epsilon,1-h0_i)+sum_{v_ji<0}(-v_ji)min(epsilon,1+h0_i)`.
Every coordinate can optimize independently in the **outer hidden box**. If C_j(epsilon)<gamma_j for all rivals, the class cannot flip. The sharp outer-box threshold rho_box is at least the standard dual-norm margin radius rho_dual=min_j gamma_j/||v_j||1. This is classical linear optimization, not a novel RNN mechanism; outer-box extrema need not be physically reachable. Exact rational control h0=(99/100,0), rival v=(9,1), gamma=1/2 gives rho_dual=1/20 and rho_box=41/100, with a synthetic physically word-controlled rival win at (1,42/100).

## Critical DFA scope correction
A stronger independent checker mistakenly required each R418 word to fix **every** complete DFA state. That fails 36/90 checks, all Task B. The actual frozen design requires each word to preserve **its designated complete state q**; 18/18 checks pass. For Task B (substring01 count mod3, previous bit), any nonempty word sets the previous-bit component to its final bit. Therefore no nonempty word can be a global identity across all six states. The invalid assertion, 90 raw cross-state checks and frozen scope erratum are preserved. No physical R444 intervention changed.

## Neural results and frozen failure
All 108 contexts, 864 nonzero-cycle physical comparisons. Baseline suffix1 correct in 98/108 contexts (Task A 36/36, Task B 62/72). At n16/32, 432 comparisons: standard dual-norm protected 274; hidden-box protected 286. The **12 additional protected comparisons came from only four model-state contexts**, Task A 6 / Task B 6, GRU/MGU, seeds 99962/99963 only. **Zero** of these extras were R425-early-nonrobust. Thus two frozen gates failed: >=3 distinct seeds (actual 2) and >=6 new early-nonrobust protections (actual 0). Other 13 gates passed. There were 146 late unprotected comparisons and 48 late class flips from a correct baseline (Task A 2, Task B 46), none contradicting a protection certificate. Repeated cycles and DFA states are not independent seeds.

Independent Torch 120/120 (max 1.56e-14), mpmath120/160/220 72/72 (max 1.56e-15), independent SymPy radii 12/12 (max 1.11e-16), designated DFA neutrality 18/18, exact Fraction synthetic controls 5/5. Archived R441 suffix1 logits reproduced with max difference 0. Rational geometry is exact on sampled binary64 hidden snapshots and weights, **not** a directed exact-real neural execution proof. No prospective cohort, causal-path mediation, or publication novelty.

## Prior art and next direction
Elsayed et al. (2018) large-margin deep networks; Singla & Feizi (ICML 2020) provable decision-boundary robustness; Zhang et al. (2021) L-infinity robustness. R444 is classical affine robustness geometry, distinct from R435 known-head reconstruction and R442 proper-score bounds but not novel science.

**R445:** retire hidden-box geometry as breakthrough candidate. Do not retune original suffixes, horizons, R425 baselines, R418 graph boxes, R438 switches, R440 precision or prior thresholds. Seek a genuinely different, physically implementable neural-specific causal total-input effect with non-ceiling readout and matched n0..2 controls across both tasks/architectures/seeds; respect per-state (not global) Task-B neutrality. If no feasible hypothesis survives audit, execute a separately frozen distinct exact impossibility/necessary-condition experiment with independent rational checks. No doomed prospective training.

Full SHA256-verified 42-entry archive: `/mnt/data/NOESIS_R444_Reproducibility.zip`, SHA256 `d1b49b535b9d50e3bb17e63c4f480795ebcb5444e94ba9c066f82097278aab3a`; 41/41 manifested payload hashes and 5/5 clean deterministic output replays pass. Includes immutable R443->R418 checkpoint chain and all raw/negative/error/independent checks. Zero spend, no user laptop.
