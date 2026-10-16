# NOESIS Kernel 001 — Run 210 frozen protocol (2026-10-17)

**Question.** Does the Run 208–209 globally shortest-error signature `1 0^k 1` transfer from scalar input-gated tanh networks to gradient-trained, fully coupled **two-dimensional** input-gated tanh networks on resettable parity?

**Primary literature frontier.** Existing recurrent neural network formal verification/invariant methods can prove model-specific behaviors; neural parity/algorithm-acquisition experiments predate NOESIS. The scalar monotone-extrema method from Runs 208–209 cannot be assumed for coupled 2D hidden states. No universal certificate is claimed.

**Architecture/task.** Two hidden coordinates; `h_0=(0.5,-0.5)`, `h_{t+1}=tanh(W[x_t] h_t+b[x_t])`, `W` shape 3x2x2, `b` shape 3x2, linear binary readout. Target reset parity: 0 preserve, 1 toggle, 2 reset. Train on all 3^6=729 length-six words, every prefix supervised, full-batch Adam lr .03, 800 updates, torch float64 CPU deterministic, seeds **751,757,761,769,773,787,797,809**. All seeds fixed before training. Epoch-800 is the primary endpoint.

**Exact scalar criterion.** For all epoch-800 models with a globally shortest *verified* incorrect input of length <= 10, score the fraction whose lexicographically earliest shortest incorrect word is exactly `1 0^k 1`. Require >=3 verified failures; transfer PASS iff fraction >=0.8, FAIL iff fraction <0.8. If <3 verified failures, record INCONCLUSIVE. A verified first error requires interval-certified incorrect output at the witness and interval-certified correct outputs for **every** shorter word, not merely floating-point search. Tie-breaking lexicographic order; multiple shortest errors must be enumerated and recorded.

**Strongest competing explanation.** The scalar architecture's order structure, rather than an algorithmic memory-retention law, forces the earlier family.

**Cheapest falsification.** Breadth-first finite reachability on the 2D network through depth 10, followed by rigorous interval replay of all shorter words and all tied shortest witnesses. No global all-length claim from finite search.

**Publishable threshold.** A nontrivial architecture-transfer result with frozen evaluation, independent proof checker, rigorous spoof controls, mechanistic prediction on unseen trajectories, primary-literature audit, and reproducible public CI.

**Learning relevance threshold.** At least three *actually gradient-trained* independently seeded 2D networks with rigorously verified shortest errors; exact weights, training code/loss, and evaluation preserved.

**Kill condition.** If score <0.8 with >=3 verified failures, kill cross-architecture universality of the signature and reformulate Kernel 001 around architecture-conditional reachable-set certificates. If no 3 verified failures, record inconclusive and do not cherry-pick seeds. Three substantive failures to strengthen the active kernel force pivot.

**THEORY ledger.** Run 208–209 scalar extrema are not valid for coupled 2D states; interval checking is required for finite claims. Full-alphabet all-length inductive simulation remains the positive certificate.

**LEARNING ledger.** This is prospective architecture transfer; finite training accuracy is not algorithmicity.

**Backups (inactive):** (i) reachable-set inductive abstraction for coupled RNNs, (ii) causal intervention on identity-symbol memory. **Wildcard budget:** at most one cheap post-primary anomaly probe, kept separate.

**Provenance.** Commit this protocol and trainer before running any seed. Keep failures, ambiguous cases, all raw outcomes and weights. Never touch main. Zero spend; assistant CPU only.
