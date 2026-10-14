# Active Kernel 001 — Learned task-quotient reachability (reformulated after Run161)
1. **Precise question:** Can a measurable, all-alphabet task-quotient invariant of a gradient-trained recurrent network predict a generalization failure or certify unbounded algorithmic behavior, without assuming a single active coordinate?
2. **Primary literature frontier:** El-Naggar et al. (ICGI 2023) exact counter-indicator conditions; neural-network verification/invariant literature. A multidimensional quotient must add learning-relevant predictive value, not merely restate standard inductive verification.
3. **One scalar success criterion:** At least 75% prospective correct failure/certificate classifications on 16 frozen, independently trained checkpoints, including cap spoofs, with no false positive certificates.
4. **Strongest alternative:** Hand-coded task semantics or post-hoc representation fitting; hidden states may not admit a tractable invariant despite genuine algorithmic generalization.
5. **Cheapest falsification:** Exact adversarial cap spoof or a previously unseen activation-region escape violating a proposed invariant.
6. **Publishable threshold:** independent checker, priority audit, unseen architectures and task families, prospective predictions, effect size vs horizon and Jacobian baselines.
7. **Learning relevance threshold:** direct use of unchanged gradient-trained weights; distinguish acquisition from post-training task-aware repair and show predictive training/generalization transition.
8. **Kill condition:** Any false positive unbounded certificate, or three substantive failures to strengthen this reformulation.
**Backups inactive:** intervention predicting training transitions; alternative task-quotient abstractions. No second active kernel.
