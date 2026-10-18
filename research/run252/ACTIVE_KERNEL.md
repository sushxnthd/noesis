# Active Kernel 001 — post-Run252 reformulation
1. **Precise question:** Can a sound, task-conditioned relational inductive abstraction certify all-length correctness of a gradient-trained recurrent network, while rejecting known finite-horizon spoofs, and identify an actual incorrect-to-correct training transition?
2. **Primary frontier:** van Rossem and Saxe, ICML 2025 (algorithm-acquisition transition); Dankowiakowski and Ronca, NeurIPS 2025 (metric automata); RNN reachability and neural abstraction refinement. The certificate must have demonstrated learning-system consequences beyond these.
3. **Exact success criterion:** >=1 new all-length neural correctness certificate on a previously unresolved gradient-trained checkpoint, independently checked, with 0/13 false certifications on Run251 known incorrect controls.
4. **Strongest competitor:** a task-specific verification engineering improvement without a generalizable learning mechanism; the target model may simply be incorrect.
5. **Cheapest decisive falsification:** check the candidate invariant against the 13 exact counterexample controls first, then prove inductive closure and output separation under every input symbol using exact rational bounds.
6. **Publishable threshold:** independently reproduced sound proof, adversarial spoof rejection, prospective unseen trained model/architecture, and mechanism-derived prediction of an acquisition transition.
7. **Learning relevance:** at least one certified *gradient-trained* model, plus an earlier checkpoint of the same training trajectory with an exact counterexample, or prospectively frozen acquisition prediction.
8. **Kill condition:** 3 substantive failed attempts to obtain a new certificate or any false certification; then retire/reformulate. Do not relabel abstention as correctness.
Inactive backups: (1) causal invariant-margin intervention; (2) stronger task-conditioned quotient for hardtanh-to-ReLU transfer.
