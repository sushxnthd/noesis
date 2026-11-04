# R430 — Frozen real-valued Hankel predictive-state experiment (negative)

**Frozen retrospective primary FAILED: 6/8 conjunctive gates.** No new neural training, no prospective replication, no new learned-RNN theorem, no claimed publication novelty.

## Pre-outcome freeze

Neural protocol SHA256 `811dd8085bec658353a30d76acbc0433fe96bee77d874f3ae4198076559a3148`; source SHA256 `39e2416cc0f0ffca60d06c30304b2ae468542d77a19a25dc123ff96688bf9e24`. The experiment used the immutable R418 checkpoints, all 108 complete-DFA-state contexts (24 networks, LSTM/GRU/MGU, both tasks, four seeds), unchanged exact 20-bit state-neutral u/v words, prefixes and oracle suffix bit 1.

For each context, n=0,2,16 u-cycles from exact-zero prefix were used. Two real oracle-vs-rival logit gaps were measured on all 63 training mixed-word continuations of lengths 0..5. All 192 continuations of lengths 6 and 7 were strictly held out from model fitting. A 7x7 Hankel block H[p,s]=f(ps), shifted H_a[p,s]=f(pas), rank by fixed singular-value ratio 0.005 (clipped 1..4), and fixed pseudoinverse 1e-10 produced weighted-automaton extrapolations. Comparators: empty-word constant, last-two-symbol empirical mean and ridge 0.01 on counts/bigrams, fitted only on training. Frozen success: >=12 non-ceiling cases with spectral heldout MAE <=0.85 the best baseline, both tasks, >=2 architectures, >=3 seeds, >=12 negative controls and other gates.

## Frozen outcomes

At n16 **11/108** cases met the improvement gate (threshold 12), **all Task B** (Task A 0/36, Task B 11/72). Both-task and >=12-positive gates failed; the other six passed. Non-ceiling cases: 14/108. Positives span LSTM2, GRU4, MGU5 and seed IDs 99960/99962/99963, but not 99961. Operator-swapped controls were worse in 108/108; this easy control is not mechanistic identification.

Pooled n16 heldout MAE: spectral 0.124620, per-case best baseline 0.368624; Task A 0.100542 versus 0.093000 (worse), Task B 0.136659 versus 0.506437 (better). These retrospective mean improvements arise from a small non-ceiling Task-B subset and do **not** rescue the failed cross-task gate. At n0/n2 there were 13/10 positives. Near-zero baseline errors make median error ratios unstable; use absolute MAE and the frozen non-ceiling gates. The earlier R404 latent path-order experiment has no matched numerical comparator here; do not claim to beat it.

## Exact classical results, independently checked

Before neural outcomes: rational weighted automaton f(w)=3+(-1)^{#u(w)} always has the same positive classification but its 2x2 Hankel minor is [[4,2],[2,4]], determinant 12, rank 2 versus rank 1 for a constant positive series. SymPy and rational parity independently checked 511 words and 3969 concatenations. This is classical WFA theory, **not** a learned-RNN theorem.

Separately frozen **after** the failed primary: f0(w)=4 and f1(w)=4+1{w=u^6} agree on every one of the 63 training words length<=5 but differ at heldout u^6. The indicator has a 7x7 identity Hankel minor, rank 7; an independent Fraction elimination/finite-state implementation verified 511 exact words. Finite observed Hankel blocks are not globally complete. This standard identifiability counterexample does not rescue the neural experiment.

## Independent audit and preservation

Outcome-independent SHA-selected audit was frozen after primary, before independent computation: selection SHA256 `8a0b4534d76485c22f470ab3b1574e950c0a6fa42f0beb651396809182b8b6e0`. One selected case per architecture×task, two length-7 words each: NumPy 12/12, Torch 12/12, mpmath at 120/160/220 digits 36/36 and exact oracle 12/12 matched the Numba float64 outputs within 1e-8; max discrepancy 3.55e-15. This is **not** a directed MPFR interval theorem.

Full SHA256-verified archive: `NOESIS_R430_Reproducibility.zip`, SHA256 `bfe2eca32258b02120acba00c1cce07c745f5f7be6c3a62970de00c6be7ada2e`. 31 entries including frozen protocols, 324 complete raw response/prediction arrays, source, all negatives, exact symbolic/independent checks, error logs, and immutable full R429 dependency SHA256 `df7d4878f3449870973c84012c98b841f555661a4504363591b8306cc7d576fd`. Local manifest verified every payload entry and ZIP integrity.

**Direction:** retire short-block Hankel extrapolation as a cross-task neural mechanism; no rank/threshold/regularization retuning or doomed fresh cohort. Next test only a genuinely distinct causal semigroup hypothesis after excluding overlap with R404 path-order and R406–407 factorial studies, or preserve a sharp exact obstruction.

Prior art: Carlyle–Paz/Fliess Hankel rank; Balle et al. (2014), DOI 10.1007/s10994-013-5416-x; Li, Precup & Rabusseau (2020), arXiv:2010.10029. Classical spectral learning, not new neural discovery.
