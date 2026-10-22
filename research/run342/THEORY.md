# THEORY ledger — Run 342
**Proposition tested:** A proof-obligation deficit based on coordinate-support inductive regions may predict independently evaluated length-generalization of gradient-trained parity RNNs. This is an empirical hypothesis, not a theorem.

**Existing mathematical claim:** The Run340/341 support-cone obligations are sufficient to prove unrestricted parity correctness under exact-real inference semantics, provided every obligation holds. The deficit is a continuous relaxation of those inequalities; small deficit is NOT a certificate. No completeness or model-agnosticity is established.

**Decisive falsification:** On unseen width-four trained models, the precommitted deficit score fails to outperform epoch-30 BCE at predicting correctness through length 12. Paired AUROC delta -0.11875. The metric is independent of certificate satisfaction.

**Adversarial witnesses:** Four original trained models are exactly correct for all 510 nonempty inputs through length 8, but fail at length 9, 9, 11, or 12. Exact dyadic arithmetic verifies every short input and each longer witness. The other 88 positive endpoints have bounded correctness only.

**Smallest supported claim:** The previously successful certificate-proximity predictor does not transfer to this independently measured width-four bounded-generalization endpoint. No unrestricted-correctness claims follow from this experiment.

**Prior art / novelty:** Neural automata extraction and invariant-based recurrent verification are established; the current negative finding is a methodological caution, not a field-level breakthrough.