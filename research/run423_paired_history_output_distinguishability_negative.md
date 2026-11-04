# NOESIS R423 — Paired-history future-output distinguishability negative

**Frozen retrospective primary: FAILED.** No new training, no neural novelty, no infinite-horizon theorem. Same scientific kernel: learned DFA-state retention under full-state-neutral cycles.

## Frozen design and all-ITT analysis

Frozen pre-outcome protocol SHA256 `38c0a036584f00bf34a12587b460cbf159c3b7e0ed9061fe673a484a9bc31385`. All 24 immutable R418 ERM networks (LSTM/GRU/MGU, both DFA tasks, four seeds 99960–99963), all nine complete DFA states and 108 contexts. For each context, three predefined pairs of distinct neural histories reaching the same DFA state: `u^16` vs `u^14v^2`, `u^16` vs `v^16`, and `u^14uv` vs `u^14vu`. Both 20-bit words were verified full-state-neutral, 1–5-gram and boundary matched. Oracle is the DFA label **after suffix bit 1**.

For each of 324 history pairs, exhaustive common-word continuation tree depth 0–8: 511 continuations per pair. Early agreement means both histories classify the correct oracle for **every** continuation depth 0–2 (7 nodes). Late separation means different predicted labels on some common continuation depth 3–8. Frozen conjunctive gate demanded >=6 late separations across both tasks, >=2 architectures, >=3 seeds, plus non-ceiling controls. No threshold adjustments.

**Result:** 0/324 early-correct/late-separating pairs; frozen primary FAILED. 236 early-correct pairs had no separation through depth 8; 88 pairs were early-incorrect. Of 324 pairs, first observed separating depths were 0 in 30, 1 in 8, 2 in 3, and not observed by 8 in 283. All 41 detected pairwise separations were already visible by depth 2. **165,564 continuation nodes and 331,128 float64 classifications**. This is finite-horizon retrospective evidence, not infinite equivalence or a universal negative theorem.

## Separately frozen diagnostic

Post-primary diagnostic protocol SHA256 `96e918e560e1c244bc6c0bac58ea7e7a8e69b9ffc926189a6b00a77000bd831a`, frozen before inspecting per-node distributions. All 236 early-correct pairs remained oracle-correct at all 511 tested continuations. Yet 172/236 had initial hidden-state infinity-distance >=0.01, 65/236 >=0.1, maximum 0.875906. Early minimum signed oracle margin was 0.19948; 230/236 had minimum early margin >=1. Thus finite classification indistinguishability does not require close latent states. Do **not** infer a learned quotient, invariant region, or infinite retention.

## Classical exact results

If both states remain in a common invariant region, each shared transition map is uniformly L-Lipschitz (L<1), and each pairwise logit gap is K-Lipschitz, then the difference of any gap after n common transitions is <=K L^n ||x-y||. If the states have different winning classes with each winning margin >=gamma, necessarily 2gamma<=K L^n ||x-y||. Elementary triangle inequality and iterated contraction; **no uniform L is claimed for the archived RNNs**. Sharp rational scalar example F(x)=x/2, gap g(x)=2x, x=1,y=-1: 9/9 Fraction equalities and independent SymPy checks.

Separate exact six-state two-letter Moore-machine example: two states agree on all outputs at continuation depths 0–2 but are first separated by `uuv` at depth 3. Exhaustive enumeration and independent equivalence refinement agree. Classical automata, not R422 shift register and not an RNN theorem.

## Independent checks, prior art, limitations

Outcome-independent SHA selection `FROZEN_R423_INDEPENDENT.json` SHA256 `9ea73fb53594fc2427fc363914abc1f54989ce9c5bc42a44a201a8be5c9b93b5`. **48/48** selected paired-history/continuation classifications agreed across independent NumPy, Torch, Numba and mpmath at 120/160/220 digits. Maximum Torch–220-digit state difference 1.308e-10. Pointwise only, no directed proof of the full tree.

Moore (1956), *Gedanken-experiments on Sequential Machines*: https://www.cs.cmu.edu/~cdm/resources/Moore1956-gedanken-experiments.pdf . Ahmadi–Jungers–Parrilo–Roozbehani (2014), *SIAM J. Control Optim.*, DOI 10.1137/110855272: https://epubs.siam.org/doi/10.1137/110855272 . All mathematical bounds are classical; no publication-grade neural novelty or predictive advantage beyond early n0–2 margins/CE.

**Decision:** Retire this paired-history late-classification distinguishability candidate. R424 should investigate distinct finite-output **parameter-identifiability** in the actual archived RNNs: pre-frozen early logit-trace parameter Jacobian rank/null directions and out-of-sample sensitivity, all tasks/architectures/seeds, independent checks, no reuse of R382–383 instantaneous readout-nullspace as novelty. No fresh training until non-ceiling feasibility.

## Reproducibility and governance

Complete 355-entry SHA256-verified local archive `NOESIS_R423_Reproducibility.zip`, SHA256 `5a1447a405b6436a8a2a1c67ab27943f3da5c0b732b24ee206ba93b8ccf96534`, includes all 324 raw compressed trees, frozen protocols, all negative results, sources, errors and interrupted high-precision logs, independent checks, and immutable R418 checkpoint dependency. No personal spend or user laptop; no branch/PR creation, force push or merge.
