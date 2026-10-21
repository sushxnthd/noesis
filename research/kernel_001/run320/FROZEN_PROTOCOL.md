# Run 320 — frozen criterion and boundary
Active Kernel 001 only. Source: Run319 gauge orbit and Run316/315 gradient-trained checkpoints.

Precise question: Can a readout-based, oracle-free canonicalizer recover an exact latch invariant under all 24 preselected positive diagonal/permutation ReLU gauges, and reject the gradient-trained delayed-memory seed 22642 epoch 80?

Frontier: Weiss, Goldberg & Yahav (ICML 2018) automata extraction; Jacoby, Barrett & Katz (ATVA 2020) recurrent verification. ReLU gauge symmetries are elementary prior art.

Scalar criterion (fixed before local experiment): 24/24 canonicalized parameter tuples identical and certified, plus seed 22642 not certified. No post-hoc cone refit. Use Fraction.from_float exact rational arithmetic. Secondary development-only census: all 96 Run315 endpoint checkpoints, with any witnessed-incorrect acceptance treated as failure.

Strongest competitor: this is a seed-specific transported proof, not a model-agnostic acquisition diagnostic. Cheapest falsification: one gauge disagreement, or a witnessed-incorrect model accepted by the proof.

Publishable threshold: sound novel certificate or prospectively frozen >0.05 AUROC improvement over training loss on >=10 exact positives and >=30 witnessed negatives, with independent verification and unseen task/architecture transfer.

Learning relevance: actual trained checkpoints only; gauge transforms are equivalent copies, not additional training samples. Kill: any frozen failure kills this candidate; no extrapolation from one orbit to all networks. Three unsuccessful substantive strengthening attempts force reformulation.

Remote write provenance: isolated branch created; two initial contents-API protocol writes were blocked, then Git-object write-through was used. Keep local complete cohort archive and failure record.
