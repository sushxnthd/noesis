# THEORY ledger — Run183
Question: Does 32-cycle linear drift predict correctness through 2048 repetitions on previously unseen balanced words in gradient-trained ReLU RNNs?
Frozen cohort: 256 model-word pairs, 129 pass / 127 fail, one baseline error. Primary criterion FAILED.
Exact witness: trained width7 seed409 epoch200, prefix 000000, block 1110001001. An exact-rational proof verifies an invariant single-active-neuron region, affine multiplier 0.9993612218991841, limiting error 0.08678315770415514, and minimum sign margin 0.05742682513278517. Hence output error stays <0.1 for every k>=0 under exact-real semantics of the stored binary64 parameters. Baseline forecast incorrectly predicts failure.
Scope: one repeated word only, not arbitrary compositions or a model-agnostic certificate.
Prior art: Weiss, Goldberg, Yahav ACL 2018 https://aclanthology.org/P18-2117/ ; RNN verification and invariant-set methods predate this witness. No novelty claim for affine invariant mathematics.
