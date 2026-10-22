# NOESIS Run 344 frozen protocol (2026-10-22)
Active kernel 001-S. This is a preregistered *analysis of a known checkpoint*, not an unseen-cohort prospective experiment.

1. Question: Is the original gradient-trained seed 31089 epoch 200 parity RNN's hidden representation irreparable by **any affine output readout**, despite its 8190/8190 correct words through length 12?
2. Frontier: Weiss et al. ICML 2018 automata extraction; Jacoby et al. ATVA 2020 RNN verification; classical convex-hull separation. No novelty claimed for the LP theorem.
3. Exact criterion: Find and independently verify one rational convex-hull intersection of positive/negative hidden states from binary words length <=16 (ideally <=6 words), proving no affine readout can correctly classify those words.
4. Alternative: The hidden dynamics are adequate, and only the learned output weights are wrong.
5. Cheapest falsification: Enumerate hidden states from unchanged original 45 float64 weights, solve parity readout LP on all words length 1..13, then extend to 16 if needed. Positive logit >=1; negative logit <=0; weights and bias unrestricted.
6. Publication gate: exact dual proof, independent checker, adversarial controls, unseen trained task/architecture, mechanism-derived prediction, and priority audit.
7. Learning gate: original gradient-trained model, no parameter modification; diagnose whether output-only retraining could ever fix it.
8. Kill: if readout remains feasible through 16, mark this irreparability attempt negative; do not claim unrestricted correctness. If exact checker fails, retract.

Exact semantics: float64 source coefficients are exact dyadic rationals. Numerical LP failure alone is inconclusive. If LP feasible, record rational readout and re-evaluate all bounded words, plus the known infinite-failure family. If infeasible, extract sparse convex-hull witness and verify with Python Fraction and independent SymPy. Keep solver outputs, negative attempts, source, ledgers, tests, and CI. Do not train or use paid compute.