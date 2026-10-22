# NOESIS Kernel 001-S: Run 350 frozen protocol
Frozen before generating any new training data.

Question: Can a fixed deep readout-obstruction probe detect representational impossibility that a shallow probe misses in new gradient-trained parity RNNs, followed by unrestricted correctness later in the same trajectory?
Primary frontier: Weiss et al. (2018) automata extraction; Jacoby et al. (2020) inductive RNN verification; classical convex separation.
Cohort: 192 seeds 33000..33191; width-3 ReLU RNN; 200 Adam steps; float64; prefix-parity training length 8; unchanged Run348 trainer except seed range.
Endpoint: unchanged Run340 exact support-cone certificate at epoch 200. For certified endpoints, scan earlier epochs in increasing order, requiring perfect training accuracy, exact correctness on every binary word of lengths 1..8, and an exact longer error. Apply unchanged Run347 shallow 618-word generator and unchanged Run349 deep 7006-word generator. Exact deep convex-hull collision and exact strict shallow affine separator required. Numeric LP alone does not count. Independent rational verifier required.
Success scalar: at least one new seed with deep exact obstruction, shallow exact separability, and later exact unrestricted certificate. Report all 192 outcomes and any numerical false positives. Zero means failed replication. No tuning after observing outcomes.
Competing explanation: favorable width-three hidden geometry and selection conditioned on certified endpoints, not a model-agnostic learning law.
Cheapest falsification: fixed new cohort plus exact readout geometry; no extra architectures or hyperparameter searches.
Publishable threshold: exact independent proof, strong adversarial controls, unseen architecture/task replication, literature audit, and smallest supported claim.
Learning relevance: original gradient-trained hidden representation must transition from provable readout obstruction to certified unrestricted correctness.
Kill condition: invalid exact proof immediately invalidates the claim; no qualifying seed records negative replication; three substantive strengthening failures require kernel reformulation.
THEORY ledger: convex-hull intersection obstructs every affine readout; support-cone induction suffices for all-length parity, neither necessary nor universal.
LEARNING ledger: original trained weights, exact earlier failure and later unrestricted correctness; no claim about exact acquisition epoch.
