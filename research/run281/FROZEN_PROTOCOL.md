# Run 281 — frozen strict-margin repair of Run280 trained parity failures
Frozen 2026-10-20, before evaluating the new repair grid. Single active kernel 001.

1. Question: Can a margin-aware, at-most-two-coordinate intervention certify all-length RESET/TOGGLE parity on actual gradient-trained, sampled-perfect but witness-wrong networks, with simultaneous parameter robustness?
2. Frontier: Van Rossem & Saxe, ICML 2025 parity algorithm acquisition; Ryou et al., CAV 2021 RNN verification. Neither parity generalization nor invariant verification is novel by itself.
3. Single exact success: >=4 of the eight fixed Run280 witness-wrong trained checkpoints receive <=2-coordinate repair preserving every one of 2,600 frozen sampled token predictions, and pass independent full-alphabet all-length correctness checks for every point of the six-parameter L-infinity box radius 2^-12.
4. Competing explanation: direct projection onto a hand-built parity automaton using task-aware regions and biased initialization; no general learning law.
5. Falsification: exact rational interval inequalities, exact sampled replay, independent checker, and real counterexamples to original networks; preserve negative outcomes.
6. Publishable threshold: transfer to an unseen architecture or task and demonstrate an effect beyond known projection/invariant techniques, plus independent reproduction and a priority audit.
7. Learning relevance: only the eight already gradient-trained Run280 checkpoint vectors, not synthetic parity models. No retraining.
8. Kill: <4 robustly repaired or any false-positive certificate; record as negative. After three kernel-strengthening failures reformulate.

Frozen cohort: Run280 witness-wrong checkpoints (seed,epoch): (20406,0),(20411,0),(20415,0),(20419,0),(20449,0),(20457,0),(20478,0),(20400,20). Checkpoint SHA256 1ad489e05732886e1ba0a6f76866ce32a2c59b0213e85df2bfa317ca8c63ad64.

Frozen candidate interventions: at most two coordinates from a_reset,a_toggle,b_reset, leaving b_toggle,v,c fixed. Each coordinate can remain original or be set to a_reset in {-1/2,-1}, a_toggle in {-7/4,-15/8,-2,-9/4}, b_reset in {-b_toggle/64,-b_toggle/32}. Reject candidates editing >2 coordinates. Among robustly certified candidates choose minimal exact L1 parameter displacement (tie break lexicographic candidate vector). The certificate uses E=[0,b_toggle/8], O=[3*b_toggle/4,5*b_toggle/4], exact interval extremes for all six parameters independently varied by 2^-12. Only after selecting a certified repair check all 2,600 original sampled token labels with exact rational inference. Any sampled loss invalidates that repair. Independently verify all successful proofs. Preserve zero-margin Run280 failure.

No main experiments; no user device or paid compute.
