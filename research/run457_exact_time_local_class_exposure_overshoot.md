# R457: Exact time-local class-2 exposure overshoot under globally balanced physical DFA laws

**Frozen classical necessary-condition audit, NOT a neural breakthrough.** No new neural training/forward pass, mechanism attribution, population inference, or prospective external replication. No earlier frozen thresholds/objectives were retuned.

Frozen pre-outcome protocol SHA256 `3a39aee9a524f19d22c729ce4732991255202477458509b70dc0392bca214b42`; primary source SHA256 `47f2a1a465cc38363920e7513203eac40018ab8e3bcca0901c9ff872b8088215`.

The physical input laws use the original R418 Task A (ones mod 3) and Task B (01 count mod 3, initial previous bit **1**) at lengths 15/35/55. Constraints: nonnegative complete-DFA/last-3-bit time-expanded flows, exact bit marginal 1/2 at every position, uniform aggregate expected 1–4-gram counts, exact aggregate expected class counts L/3, and uniform terminal 24-state law. These are **expected distributions**, not iid or realized balanced training corpora.

For class 2, which is impossible at the first r=1 (A) or r=3 (B) positions, minimize the maximum **positive** post-burn-in positional overshoot z = max_{t>r}(P(Y_t=2)-1/3). The elementary bound r/[3(L-r)] is insufficient under the other physical constraints.

| Task | L | Independently exact rational dual lower bound | Numerical upper bound | Exact primal |
|---|---:|---:|---:|---|
| A | 15 | 3/64 (4.6875 percentage points) | 3/64 | YES |
| A | 35 | 1/24 (4.1667 pp) | approximately 1/24 | NO |
| A | 55 | 1/24 (4.1667 pp) | approximately 1/24 | NO |
| B | 15 | 29/192 (15.1042 pp) | 29/192 | YES |
| B | 35 | 29/672 (4.3155 pp) | approximately 29/672 | NO |
| B | 55 | 29/1152 (2.5174 pp) | approximately 29/1152 | NO |

**Only the two length-15 optima are exact sharp theorems**, with independent exact primal and dual certificates (Task A 357/357 and Task B 339/339 primal constraints). Independent pure-Fraction reconstruction, without importing the primary matrix builder, verified all six dual lower-bound certificates, respectively 543, 1503, 2463, 511, 1471 and 2431 variable inequalities. Four longer-length upper bounds remain numerical only and MUST NOT be presented as exact optima. All six LPs solved numerically with maximum equality residual < 4e-13.

At L15, a globally aggregate-balanced law necessarily has at least one post-burn-in position with class-2 probability >= 73/192 = 38.0208% (A), or >= 31/64 = 48.4375% (B). This is a classical positional exposure constraint, **not** evidence of neural errors or a new causal retention mechanism.

Independent exact negative controls confirmed the early class-2 reachability exclusions, first-token class-0 possibility, and that iid fair bits do NOT satisfy the frozen exact aggregate class balance at these lengths. Existing severe constraints remain: Task A readout floor, R425 early ceiling, R443 seed pseudoreplication, R450 length shift, R454 compute/power, and R455–456 corpus dependence. No new training is justified.

**Complete immutable archive:** `/mnt/data/NOESIS_R457_Reproducibility.zip`, SHA256 `72f5ad1e3ea392c9bf19f3d4c03a6d9a896ee80d124169b23cf559e54e5986fb`; 34 entries/33 SHA256-verified payloads, nested immutable R456->historical checkpoints, 14/14 clean deterministic artifact replays, original frozen source, all raw numerical outputs, exact primal/dual certificates, negative controls, independent checker and logs.

Prior art: [Metric Automata Theory (NeurIPS 2025)](https://papers.nips.cc/paper_files/paper/2025/hash/c03c2e3e2ad8057aefc3da880476784d-Abstract-Conference.html), [Brandoit et al. 2026](https://arxiv.org/abs/2609.32447), [Chung et al. 2026](https://arxiv.org/abs/2605.07755). The mathematical method is classical constrained occupation-measure LP duality.
