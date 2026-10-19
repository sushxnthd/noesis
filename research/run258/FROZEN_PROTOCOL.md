# NOESIS Run 258 — frozen independent-acquisition transfer protocol (2026-10-19)

**Active kernel:** K001, prospective all-length certificate transfer. No broad search.

1. **Precise question:** Can the eight-cell exact reset-parity invariant geometry discovered for seed 13037 certify independently initialized, gradient-trained ReLU recurrent networks, or is transfer confined to its own local parameter basin?
2. **Primary-literature frontier:** Prior polyhedral RNN verification supplies sound invariants; prior work on neural algorithm acquisition establishes transitions. Neither finite training accuracy nor finite-horizon closure is a correctness certificate. NOESIS Runs 254–257 establish one all-length proof and repaired descendant proofs, not independent acquisition.
3. **Scalar criterion:** At least one independently initialized seed among 17001–17064 receives an exact all-length certificate with zero incorrect controls falsely certified. Failure to find one is not a theorem of nontransfer.
4. **Strongest competitor:** Exact geometry is narrowly tuned to original trained solution; all independently trained candidates may be incorrect or require different invariant geometry.
5. **Cheapest falsification:** Deterministic CPU training from scratch, finite accuracy screening, exact long-horizon adversarial witnesses, and fixed-geometry/adaptive-dual proof attempt on eligible models.
6. **Publishable threshold:** At least two independently acquired certified models including a different task family, independently checked and priority audited.
7. **Learning relevance:** All positive models must be independently initialized and gradient trained, not perturbed descendants. Preserve epochs and seeds.
8. **Kill condition:** If no independently acquired positive candidate is available, label transfer inconclusive; if eligible models exist but fixed geometry fails, retire *fixed-geometry transfer*, not the sound certificate framework. After three substantive mechanism-specific failures reformulate.

**Freeze:** seeds 17001–17064; architecture 4-unit ReLU RNN, float64 weights, symbols hold/toggle/reset, 5-step exhaustive supervised training, 200 Adam updates at lr 0.03, same initialization family as Run255. Exact stored float64 coefficients are treated as rationals. Evaluate perfect training models with predefined probes: hold tails to 512, periodic patterns to 256, seeded random to 256, then attempt original eight-cell geometry with adaptive sparse dual supports. No use of previously certified weights for initialization or selection. Prospectively freeze before any new training.

**Claim boundary:** Positive proof requires exact independent checker; negative finite search never certifies correctness. Retain all checkpoints, failures, tests, protocol, and CI state. No merges into main. Public CPU only.
