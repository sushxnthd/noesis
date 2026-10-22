# NOESIS Kernel 001-S — Run 352 frozen causal-selection protocol

Frozen before examining intervention outcomes for the 64 held-out seeds **32064–32127**. These seeds were trained in Run 348, but were not used in Run 351's 32000–32063 intervention scan. This is a **prospective intervention analysis on existing trained checkpoints**, not a prospective training experiment.

## Precise question and competing explanation
Does a representation-agnostic, short-horizon **worst signed margin** criterion select a one-coordinate gradient update that improves longer-horizon parity classification more often than a uniform random coordinate? Alternative: the Run 351 calibration effect was seed selection, ordinary margin scaling, or finite-family overfitting. This is not an unrestricted-correctness certificate.

## Data and leakage boundaries
- Source: original `research/run348/train348.py` (width-three ReLU RNN; 28 float64 parameters; seeds 32000–32191; epochs 0–200; parity prefix training at length 8). Source trajectory file: Run 348 evidence archive, not a newly retrained or selected cohort.
- Heldout seeds: integers 32064 through 32127 inclusive; calibration seeds 32000–32063 excluded.
- For each seed choose the **earliest** epoch `t<200` whose original training accuracy equals 1.0; if none, mark ineligible.
- Define original checkpoint `p_t`, next checkpoint `p_{t+1}`. For each recurrent coordinate `j in 0..23`, replace only `p_t[j]` by `p_{t+1}[j]`, preserving all other parameters and the original readout. Include baseline and full update as controls.
- For each candidate compute `m_j = min_{1<=|w|<=8} ((2 parity(w)-1) * logit_j(w))` on all 510 nonempty binary words. Select `j* = argmax_j m_j`, breaking ties toward the **smallest coordinate index**. This selector uses no word longer than length 8 and no longer-horizon outcomes.
- Only after choices are fixed, evaluate the previously defined Run 350 2,644-word frozen generator (length <=23, source `research/run351/evaluate.py`).
- For the primary comparison include only seeds that have a selected epoch and whose **unmodified baseline** is not perfect on the 2,644-word generator. Report excluded ceiling seeds separately; do not drop unfavorable intervention outcomes.

## One scalar criterion
For eligible non-ceiling seeds let `g_s(j)` be improvement in number correct over the baseline on 2,644 words. Let
`D = sum_s [g_s(j*_s) - mean_{j=0..23} g_s(j)]`.
Report `D` and a one-sided Monte Carlo random-coordinate p-value from **100,000** draws (fixed NumPy generator seed 352, one uniformly sampled coordinate independently per seed). Include add-one correction `(1+#{D_random>=D_observed})/(100001)`. Primary PASS iff at least 10 eligible non-ceiling seeds, `D >= 50`, and `p <= 0.01`. No posthoc threshold change. Negative result must be committed.

## Decisive falsification and independent audit
- Publish every heldout seed, chosen coordinate, all 24 gains, baseline and full-update outcomes, and ties.
- Independently recompute exact rational classification for the **three largest strictly positive selected gains** (or all positives if fewer than three) over the entire 2,644-word generator, including the unmodified baseline; independently verify chosen coordinates from exact float64 weights.
- For those selected interventions, search all nonempty binary words through length 12 (not just generator) for an error; if none, probe `1+0^n`, `10^n1`, and `101+0^n` for `0<=n<=128`. Exact-check any found counterexample. Report "unresolved" if no error is found, never "algorithm acquired."
- Strongest spoof baseline: the Run 350 one-coordinate intervention, which improves finite-horizon accuracy but has an exact infinite-failure family. This prevents treating a high finite-family score as a certificate.
- Independent checker must use Python Fraction/SymPy, not the vectorized NumPy evaluator.

## Eight-field active kernel
1. Question: Does a pre-outcome, short-margin causal selector predict longer-horizon improvement in trained RNNs without confusing it with all-length algorithm acquisition?
2. Primary literature frontier: RNN invariant verification, automata extraction, and OOD length-generalization; exact rational convex/inductive certificates are not claimed novel.
3. Scalar success: D and permutation p above, with fixed thresholds.
4. Competing explanation: finite-family margin overfitting or in-family parity-specific behavior.
5. Cheapest falsification: heldout random-coordinate comparison plus exact longer-input adversary.
6. Publishable threshold: independent replication on a second architecture/task, exact adversaries, a defensible mechanism, priority audit.
7. Learning relevance: actual Run 348 gradient checkpoints, intervention from an actual next-epoch parameter.
8. Kill: fail this heldout test and one independent redesign, or three substantive failures in the current reformulation.

## Evidence boundary
This run tests **selection of a causal finite-horizon repair**, not prediction of unrestricted correctness. The original training checkpoints predate the freeze; only their intervention outcomes are held out. Keep THEORY and LEARNING ledgers separate, preserve failures, and leave the research PR draft.
