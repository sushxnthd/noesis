# NOESIS Kernel 001 — Run 310 frozen falsification protocol
Date: 2026-10-21. Parent: Run309. Status: prospective protocol, outcomes NOT YET evaluated.

## Active kernel (one only)
1. **Question:** Does disappearance of an exact equal-length opposite-label hidden-state collision during gradient training imply learned unrestricted persistent-latch correctness, or can gradient-trained networks spoof this diagnostic?
2. **Primary frontier:** Weiss, Goldberg & Yahav (ICML 2018), automata extraction; Jacoby, Barrett & Katz (ATVA 2020), invariant-based RNN verification; Ryou et al. (CAV 2021), polyhedral verification. Exact collision obstruction is elementary; absence is not a sufficiency theorem.
3. **Exact success criterion:** >=1 of the four previously unresolved, collision-resolving, epoch80 sampled-perfect checkpoints has a strictly incorrect exact-rational output on a predeclared family of binary words.
4. **Strongest competitor:** Collision disappearance is a genuine mechanism change but insufficient by itself; late networks may still fail on long or patterned sequences.
5. **Cheapest decisive falsification:** Evaluate unmodified Run300 epoch80 trained parameters, fixed seeds 22242,22287,22361,22573. Candidate words: 0^n, 10^n, 1^n, (10)^n, (01)^n, 110^n, 1001^n for n=0..4096 (nonempty words only). Scan with float64 as a discovery filter, verify any claimed failures by exact binary-rational recurrence and output sign. For 22241, independently recheck the existing Run309 all-length positive certificate; do not use it as a new discovery.
6. **Publishable threshold:** >=2 distinct newly exact-witnessed failures, independent rational checker, and public CI reproducibility; write smallest negative sufficiency claim only.
7. **Learning relevance:** At least one exact failure must be on a genuine unmodified gradient-trained checkpoint with previously exact early collision and no observed late collision through length 8.
8. **Kill condition:** If three substantive attempts using different fixed families/stronger exact methods fail to establish a new useful diagnostic distinction, kill/reformulate the collision-disappearance sufficiency subhypothesis.

**Prior evidence:** Run307: 5 collision-resolving sampled-perfect endpoints (22241,22242,22287,22361,22573); Run309: 22241 exactly certified unrestricted correct, leaving 4 unresolved. Run307 collision absence is only checked through length 8, not arbitrary length.

**Prespecified semantics:** RNN hidden h0=(0,0,0), h_{t+1}=ReLU(A_x h_t+b_x), output logit w·h+c. Correct label is 1 iff the word contains a 1; predict 1 iff logit>0. An exact rational zero logit is treated as incorrect for positive labels and correct for negative labels.

**Separation:** Discovery float scans are not proofs. The independent checker must recompute all claimed witnesses directly from the original float64 parameters via Fraction.from_float, not reuse discovery intermediate states. Preserve negative outcomes and every infrastructure failure. Do not modify original checkpoints.

**THEORY ledger target:** Whether finite collision resolution can be falsified as a sufficient certificate. **LEARNING ledger target:** Trained-network evidence, not an abstract automaton.
**Wildcards:** None in this run (reserve ~10% across runs, never contaminate this frozen evaluation).
