# LEARNING ledger — Run265

Reused 64 independently initialized gradient-trained 2D ReLU RNNs from Run264, set/reset latch with 3-symbol alphabet and length-20 training. Eligibility: exactly perfect finite training accuracy at epochs 100,300,600; 37 checkpoint instances. Tested SET+HOLD and RESET+HOLD for all 37. Predictions were hashed and committed before new long-horizon replay.

Exact long-delay witnesses: 19 checkpoint/prefix pairs spanning 12 independent seeds; first error hold index ranges 33..411 among these. The two additional wrong-attractor predictions had float candidate first errors at hold indices 1066 and 2873; neither was independently exact-replayed as part of this run. All 19 witnessed errors were replayed independently using integer dyadic arithmetic. Reusing checkpoints limits prospective interpretation to the newly frozen prefix-conditioned evaluation, not independent acquisition replication.

Full checkpoint and proof files are preserved in the Run265 archive. Remote mirror incomplete; PR remains draft. Next decisive objective: prospective full-alphabet positive certificates on independently acquired algorithms, or a mechanism-derived cross-task prediction. No intervention justified yet.
