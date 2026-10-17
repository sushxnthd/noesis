# NOESIS Run 212 — last abstention resolved as correct

**Frozen primary test FAILED to find an error:** the precommitted width-2048 diversity beam found no misclassified seed-787 word through length 256. This is not a correctness proof.

**Decisive stronger secondary result:** a five-cell inductive simulation indexed by (true parity, last input symbol) proves the *same genuinely gradient-trained* 2D RNN computes reset parity for every prefix of every finite ternary input. Two separately implemented local outward interval checkers passed (90 decimal digits, exact dyadic binary64 parameters).

Proof obligations: (i) every prefix length 1..120 classified correctly; (ii) 120th reachable task/last-symbol boxes contained in five rational rectangles; (iii) all 15 symbol transitions map each rectangle into the appropriate successor rectangle; (iv) all five invariant rectangles have strictly correct output signs.

Primary verified minimum margins/slacks: prefix 5.724301856899349, base inclusion 1.0000999999530578e-6, transition closure 9.958506731478929e-9, invariant output 5.7627547166545545. Independent directed-Decimal checker returned matching strict signs.

**THEORY ledger:** Naive two-class axis-aligned rectangles abstained on this correct model. A task-state × one-token-context partition succeeds; abstention is not evidence of heuristic learning. This invariant construction is known-style neural verification, not a new universal theorem.

**LEARNING ledger:** Run 210's eight fully coupled 2D trained models are now seven all-length certified correct (751,757,761,769,787,797,809) and one certified wrong (773, witness from Run 211). All eight had 100% finite training accuracy. No prospective acquisition predictor has been established.

**Claim boundary:** Exact-real evaluation of frozen binary64 checkpoint parameters, not floating-point hardware behavior or model-agnostic acquisition law. Candidate rectangles were discovered post hoc by numerical interval propagation and LP; their soundness rests solely on independently checked interval proof obligations. The Run 212 frozen *counterexample* criterion did not pass; the certificate is a separately labeled secondary result. Publication novelty remains unestablished.

**Provenance:** FROZEN_PROTOCOL.md was committed before the beam; preliminary report and local numerical scripts/logs preserved in the accompanying run archive. Remote workflow result must be checked separately; do not claim remote PASS until observed.

**Active kernel:** full-alphabet, task-relevant hidden-state inductive simulation. Next priority: frozen pre-certificate feature predicting correct-vs-incorrect learning on unseen trajectories; avoid interpreting proof-tool abstentions as negative labels.
