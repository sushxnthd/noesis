# NOESIS K001 Run287 frozen protocol — 2026-10-20
Single active K001. Exact question: Does ordinary gradient training destroy unrestricted correctness in an already certified network while preserving perfect sampled accuracy?
Primary frontier: Neural verification and catastrophic forgetting exist; certificate nonmonotonicity alone is not correctness loss. Do not claim novel forgetting without exact counterexample.
Frozen models: from Run286 seed 20828 and 20872, both exact all-length certified at epoch80, sampled-perfect but uncertified by the frozen box search at epoch120.
One exact success criterion: >=1 independently exact-verified incorrect finite input word at epoch120 for either previously certified model. A failure to find is inconclusive about all-length correctness.
Strongest competing explanation: epoch120 is still correct but our axis-aligned certificate search is incomplete.
Cheapest falsification: exhaustive binary word enumeration through length18, then deterministic bounded targeted adversarial reset/toggle probes (pure toggle <=512, RESET+TOGGLE^n+RESET, TOGGLE^n+RESET+TOGGLE^m, n,m<=128), independent rational checker of any floating candidate. Do not change search order after observing results.
Publishable threshold: replicated nonmonotonic correctness transition across independent trained seeds/architectures, independent proof, priority audit.
Learning relevance: actual gradient-trained 15-parameter width2 ReLU RNNs with sampled-perfect epoch80 and epoch120, same training trajectory.
Kill condition: if no exact counterexample in frozen search, reject behavioral forgetting claim; retain only certificate loss, do not equate to incorrectness.
THEORY: exact box certificate is sufficient, not necessary. LEARNING: possible training-induced loss, currently unverified.
No user laptop; retain negatives and infrastructure. Frozen before the adversarial search.