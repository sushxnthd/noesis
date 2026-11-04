# NOESIS R453: exact length-aware DFA/4-gram balanced training generator

Date: 2026-10-27. **Classical constructive methodology, NOT a neural mechanism or neural breakthrough.** Single kernel: causal transition dynamics of learned DFA-state retention under per-designated-complete-state-neutral cycles. No training, no expenditure, no user laptop.

## Frozen design and original failure

Original pre-outcome protocol SHA256 `289d0732495b3d3579a6a626c18d2fe8ae1f3094daf54a3fac2fb55cca1ab4d8`: both original R418 DFAs, Task B initial previous bit **1**, lengths 15,35,55. Demand physically reachable stochastic input strings, marginal bit 1/2 at every position, fair-iid expected aggregate counts for every binary 1- through 4-gram, and balanced expected post-token DFA class counts L/3. No new neural outcomes. The first implementation used Python `history[-0:]` for unigrams and falsely declared all six infeasible. Original code/log preserved; implementation-only erratum SHA256 `7875e1f3c3f24844ae5b6670d6639b61f0e994eff7f7411dd269a3321a661e32`. Corrected LP: 6/6 numerically feasible, not an exact proof by itself. Direct rational recovery passed Task A L15/L35; L55 direct exact recovery timed out at 200s, preserved as execution limit.

## Exact stationary-prefix construction

Separately frozen stationary extension SHA256 `21575743e2937814169ef4d884b226f3ab52e04c3f4573c118ad6ff52bea8cd3`. **Both tasks have exact nonnegative rational length-15 prefix edge-flow witnesses** satisfying all constraints and ending at uniform mass 1/24 on each of 24 joint states (DFA count mod3, last 3 bits). Task A witness: 220 positive edges, max denominator 13,272,096, 148 positive-probability physical strings. Task B: 201 positive edges, max denominator 5,539,464, 188 strings.

For any next bit drawn fair independently, uniform joint state gives 48 edges each 1/48, returns uniform joint state, uniform post-token class 1/3, and uniform each ending 1..4-gram. Hence prefix plus stationary fair tail is an **exact constructive physical stochastic generator for every integer length L>=15**, not only 15,35,55. This is classical finite-state occupation-measure theory, not new automata theory. It matches aggregate lexical moments, not complete strings, per-position class balance, 5+-grams, or intermediate DFA paths.

Independent pure-Python Fraction checker did not import the LP source. It verified exact flow, 24 terminal masses, 30 gram patterns, 15 position marginals, 3 class counts, 48 stationary edges, reconstructed all 148/188 positive physical prefixes and checked their probabilities, and checked extensions at lengths **16,35,55,335,655** for both tasks: 10/10 exact heldout task-length combinations. Independent protocol SHA256 `8f4505566f84944985a3c21853716f3d76414e35bdc335bc60d2d125c6523461`.

## Finite-sample caveat and negatives

Separately frozen arithmetic: for N equally weighted length-L strings, exact expected per-pattern k-gram count requires N(L-k+1)/2^k integer (k=1..4); N even; NL divisible by 3. Minimum N passing these **necessary, not sufficient** conditions is 8 at L15 and 24 at L35,55,335,655. Original N196 fails all these lengths (per-3gram expected counts are half-integers); N192 and N216 pass divisibility only. Stochastic expectation is not exact finite-corpus balance. No claim that class imbalance caused Task B errors; R425/R449/R451 early-ceiling negatives stand. Independent trained seed is the replication unit, no population inference.

Prior art: Borkar (1994) constrained Markov occupation measures DOI 10.1137/S1052623491218895; Dankowiakowski/Ronca NeurIPS 2025 Metric Automata; Brandoit et al arXiv:2609.32447 (2026). No neural novelty or prospective replication.

**Preservation:** complete `/mnt/data/NOESIS_R453_Reproducibility.zip`, SHA256 `697727fb27275415f515a561129f54c681a82bb61bdd7c1c02ae7cb00fb37741`, 43 entries/42 SHA256-verified payloads, nested immutable R452->R404 checkpoints. Original bug/error, direct-exact timeout, frozen protocols, sources, all numerical and exact outputs, independent checks and negatives included. Ten clean deterministic output-hash replays passed.

**Next:** R454 should freeze a genuinely neural-specific non-ceiling causal hypothesis and assess independent-seed power/compute before prospective length-aware training. Do not retune past failures or treat this generator as proof of improved neural retention.
