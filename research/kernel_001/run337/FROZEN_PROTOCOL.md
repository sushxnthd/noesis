# NOESIS Run 337 — frozen parity transfer (2026-10-22)

**Active kernel:** 001-S, Learned-State Inductive Certificates. This is a distinct task family from prefix-OR and tests nonabsorbing, reversible two-state computation.

1. **Precise question:** Can a gradient-trained width-two ReLU RNN trained only on short prefix-parity sequences acquire a machine-checked, unbounded parity algorithm, rather than bounded-range parity behavior?
2. **Primary-literature frontier:** Jacoby, Barrett & Katz, ATVA 2020 (invariant inference for RNN verification); Michalenko et al., 2019 (automaton-state interpretation); Fan, Chi & Rudnicky, 2023 (regular-language generalization). No novelty claimed for box induction.
3. **Single exact success criterion:** >=1 original epoch-200 checkpoint from 192 newly trained seeds passes an independently checked two-region inductive parity certificate for *every* finite binary word.
4. **Strongest competing explanation:** The network memorizes finite parity prefixes; a restrictive axis-aligned box proof may reject genuinely correct networks.
5. **Cheapest decisive falsification:** Run the frozen checker on all epoch-200 checkpoints and test a hand-constructed length-cap spoof that is correct through the training horizon.
6. **Publishable threshold:** Positive certified parity learning, independent proof checker, matched spoof controls, finite-perfect-to-certified transition or a prospectively predicted transition, and a primary-priority audit.
7. **Learning relevance:** All positive claims must concern untouched Adam-trained checkpoints. Hand-built controls are negative baselines only.
8. **Kill condition:** Any false-positive certificate, or three failed attempts to strengthen this learned-state certificate kernel; report unknown separately from false.

**Frozen training:** seeds 27000..27191 inclusive; width=2; input alphabet {0,1}; h'=ReLU(A_x h+b_x); logit=v.h+c; 192 seeded random length-8 sequences + four fixed motifs per seed; prefix parity targets (running XOR); Adam lr=0.025, float64, 200 updates, initialization N(0,0.5^2) with generator seed+51000, 15 parameters per network, torch deterministic algorithms, CPU, single thread. No parameter projection or architecture-level hardcoding of parity.

**Frozen certificate:** Two closed axis-aligned boxes B_even and B_odd in hidden space, containing h0=0 in B_even; for all h in B_q, logit negative if q=even and positive if q=odd (strict margin >=1e-7); and F_x(B_q) subseteq B_(q XOR x) for x=0,1. Candidate boxes inferred from exhaustive short trajectories and widened by deterministic interval iteration. The final checker uses exact dyadic rationals of original float64 weights and candidate box endpoints. A separately implemented rational checker verifies all accepted certificates. No finite-prefix success alone counts.

**Frozen diagnostics:** Record training-prefix accuracy and exhaustive length<=10 correctness, certificate acceptance, failure reason, any exact finite counterexamples, and independently checked spoof rejection. Evaluate all 192 seeds, not just successes. If no certificates, record a failed transfer attempt, not a claim that parity cannot be learned.

**Data provenance:** Preserve raw 201-checkpoint trajectories, code, exact certificate candidates, proof outcomes, hashes, tests, and two ledgers. Keep main untouched.
