# NOESIS R414 — residual/interval-Jacobian retention enclosures

**Retrospective feasibility PASSED, 12/18; classical numerical certificate, NOT a prospective replication, novel theorem, or formal IEEE rounding proof.**

Frozen pre-outcome protocol SHA256: `d1704eeb220af82b19fcc1bc0f30024e1978492eb89602efdad4df824d1ca62b`. Reused **all 18 unchanged R413 preselected cases** (LSTM/GRU/MGU-style × taskA/taskB × seeds99920–99922), same prefixes, 20-bit full-DFA-neutral words, exact binary64 checkpoint weights interpreted as dyadic reals, and n16. No model training or cherry-picking. Frozen radii 2^-36,2^-28,2^-20,2^-12, interval precision 240 decimal digits, frozen gate ≥6 certified, both tasks, ≥2 architectures, 3 seeds.

**Method change from failed R413 naive forward-box test:** recompute the full n16 state enclosure from exact zero with 240-digit `mpmath.iv`; center a candidate weighted box at an independently recomputed float64 n16 state (treated as exact dyadic); choose positive coordinate weights from a point Jacobian **as a heuristic only**; then enclose the full 20-symbol word-map Jacobian **uniformly over the box** with interval forward-mode automatic differentiation. For every coordinate, test the mean-value sufficient inequality

`|F(c)_i-c_i| + sum_j sup_B |dF_i/dx_j| * r*v_j < r*v_i`.

Together with initial n16 state inclusion and suffix-1 oracle logit dominance **throughout** the box, this gives a conditional all-future neutral-word readout certificate for the specified exact-real dyadic-weight network and prefix/word. A pointwise Jacobian alone is never used as proof.

**Frozen outcome:** 12/18 all-future numerical interval certificates. TaskA 8/9; taskB 4/9. LSTM 3/6; GRU 5/6; MGU-style 4/6. Each of the three seeds certified 4/6. All 12 positives passed at the smallest frozen radius 2^-36. Six negatives remain preserved, with non-dominating oracle readout at n16. No threshold or selection retuning. This is a feasibility result on archived checkpoints, NOT prospective architecture replication.

**Independent verification:** frozen post-outcome audit SHA256 `c095669a1bf1a93a5d4ee34f1eadc338b1be24f807a58b94d4a0c490695166ea`; 144/144 deterministic independent Torch-autograd point Jacobians inside interval Jacobian bounds, 24/24 240-vs-300-digit certificate decisions agree on six preselected arch/task cases, 18/18 independently checked full-state-neutral symbolic words and suffix1 oracles. Initial dual-operator typing failure and evaluation interruption after 15 cases preserved; only the three missing cases computed on resume, 18 unique raw cases.

**Scope and limitations:** mpmath.iv numerical directed enclosures are relied upon; independent MPFI/Arb or formal proof-assistant validation of transcendental outward rounding was NOT performed. These are conditional numerical interval certificates, not formally audited exact-real proofs or float64-execution infinite-horizon guarantees. They do not generalize to other prefixes, words, seeds, or architectures. Weighted boxes, mean-value enclosures, and wrapping mitigation are classical (Garloff–Krawczyk 1986; Alefeld–Gienger–Potra 1994; Lohner-type rigorous integration). No publication-grade novelty.

**Reproducibility:** complete 28-entry SHA256-verified archive `NOESIS_R414_Reproducibility.zip`, SHA256 `91afd06b8a5d4439a386b60db42d4709686aad84de45174ef5e61c7b34454e04`. It contains every R414 source/frozen manifest/raw positive and negative/independent audit/error/resume log, plus immutable full R413 dependency ZIP (R411 checkpoint lineage). Raw and model checkpoints are local archive, NOT committed to GitHub.

**Next:** independently freeze fresh, disjoint-model/seed/neutral-word **prospective** replication across both tasks/all complete DFA states and architectures, with stronger independent directed transcendental verification; never reuse R414 cases as prospective. Zero personal spend, no user laptop, no new branch/PR, no merge or force-push.