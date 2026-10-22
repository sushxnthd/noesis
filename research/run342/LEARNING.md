# LEARNING ledger — Run 342
**Training:** 128 new width-four recurrent ReLU parity networks, seeds 31000..31127; 200 Adam updates each; 25,728 archived epoch checkpoints. Training uses length-eight sequences only. No user laptop or paid compute.

**Frozen forecast:** Epoch-30 proof deficit vs epoch-30 training BCE. Outcome is independently evaluated correctness of epoch-200 models on all 8190 nonempty words through length 12. No certificate used to define the endpoint.

**Observed:** 88/128 pass bounded generalization, 40 fail, 0 ambiguous. Deficit AUROC 0.6747159091; BCE AUROC 0.7934659091; difference -0.11875. Frozen threshold +0.05 FAILS. Descriptive stratified bootstrap 95% [-0.23068,-0.00938] (not precommitted).

**Four bounded-perfect heuristics:** Seeds 31012,31033,31034,31103 are exact-perfect through length 8 but fail at lengths 11,12,9,9. This does not establish when or whether they acquire unrestricted algorithms.

**Kernel:** Retain 001-S, one negative independent-endpoint transfer. Do not optimize the diagnostic on this cohort. The next test must distinguish true learning mechanism from representational template proximity.