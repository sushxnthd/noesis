# NOESIS Run 203 — Frozen output-quotient falsification

**Parent evidence:** Run202 exact binary64 gradient-trained width-12 tanh RNN checkpoints; source SHA256 `5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32`.

**Active Kernel 001:** task-state quotient inductive simulation, not another finite-query accuracy score.

**Question:** Is the simplest output-aligned three-region quotient actually closed under both symbol transitions on states reached by a genuinely trained checkpoint? A reachable violation disproves this proposed coarse quotient, not all possible task-aligned refinements.

**Frozen primary checkpoint:** seed 307, epoch 400 (selected because Run202 certified the all-zero infinite family correct). Secondary heldout evaluation: seed 307, epoch 800. No retuning or selecting a seed after seeing outcomes.

**Exact screen:** deterministic BFS of all binary words from length 0 through 14; for each prefix `u`, evaluate the model's predicted class `q(u)` and the predicted classes of `u0` and `u1`. For each residue `r` and symbol `a`, find lexicographically first two prefixes `u,v` with `q(u)=q(v)=r` but `q(ua)!=q(va)`. Prefer the shortest maximum prefix length, then shortest total length, then lexicographic pair. Empty prefix may be used only as a mathematical hidden state and must be separately marked; primary witness must use nonempty prefixes. Also check true residue and prediction correctness for each witness word. Save raw enumeration counts, shortest witnesses and all numerical margins.

**Scalar success criterion:** one primary seed-307/epoch-400 reachable two-prefix witness with independently proven strict output classes at all four words `u,v,ua,va`, including exact binary64 parameter interpretation. PASS = 1; otherwise FAIL/ABSTAIN. This is a *falsification* success, not a positive learned-algorithm certificate.

**Strongest competing explanation:** output partition is intentionally too coarse; a refined reachable invariant could still prove all-length correctness. A witness can simply expose an already-known finite error.

**Cheapest decisive falsification:** bounded exhaustive BFS followed by outward interval verification of the four witness outputs. The independent checker must use a distinct arithmetic implementation (Decimal directed rounding vs mpmath intervals). No inference from float64 alone.

**Publishable threshold:** this alone is not publishable. Require a prospectively successful refined quotient across unseen trained architectures/tasks, spoof rejection, independent proofs, and a predictive training-transition result.

**Learning relevance threshold:** witnesses must be reachable by the actual gradient-trained model, not artificial hidden states; report whether they are correct on the prefixes and how the successor error changes evaluation.

**Kill condition:** if the coarse output quotient is falsified, kill *that quotient* immediately, not the full Kernel001; if three consecutive distinct refinement/proof attempts fail, reformulate Kernel001. Any unsound acceptance triggers immediate kill.

**Separation:** THEORY ledger records quotient counterexample and proof status; LEARNING ledger records checkpoint training and task correctness. No result from the exploratory second checkpoint enters the primary score.

**Infrastructure:** preserve failures; run on free public CI when possible; branch only, never main. The frozen protocol precedes local inference.
