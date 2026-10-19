# NOESIS Run268 — two-architecture prospective transfer: negative result

**Frozen before replay:** 2026-10-19, predictions SHA256 a52aa3776bc6721c95248c6936acd2a9e37e2ffbf1f9a6118bfeee06538fd94b. Training/checkpoint SHA256: 2D 27cce2082daa498136716be2c9b3c9ea6c398510a283c7ef92e0482ff9d88abf; 3D e03147140e3c9a10afe936feed62463911ef0d873704fa068d757f9a0fe3c777.

## LEARNING ledger

32 independently initialized gradient-trained ReLU latch networks (16 with hidden size 2; 16 with hidden size 3), 600 Adam updates, 20-token training sequences. Thirteen had exactly 100% finite training accuracy at epoch 600 (five 2D; eight 3D). In two frozen families SET HOLD^n RESET and RESET HOLD^n SET, n<=2048, twelve of thirteen had wrong outputs; independent exact dyadic and Fraction replay confirmed a witness for each.

seed dimension first_error_position family/error
18501 2 51 RESET HOLD^50 (hold)
18504 2 46 RESET HOLD^45 (hold)
18511 2 45 RESET HOLD^44 (hold)
18513 2 331 RESET HOLD^330 (hold)
18514 2 86 RESET HOLD^85 (hold)
18602 3 552 RESET HOLD^551 (hold)
18604 3 181 RESET HOLD^180 (hold)
18605 3 unresolved through n=2048 for these two families
18609 3 40 SET HOLD^39 (hold)
18610 3 113 RESET HOLD^112 (hold)
18611 3 125 SET HOLD^124 (hold)
18612 3 69 RESET HOLD^67 SET (switch)
18616 3 218 RESET HOLD^216 SET (switch)

No claim of global shortest counterexamples or unrestricted correctness for seed 18605. Four finite-perfect models fail by n<=64; nine remain for frozen delayed-switch scoring. Only two of those nine have delayed final-switch failures. The frozen trend extrapolator predicts both, and the spectral-radius baseline also predicts both but falsely flags 18605. Balanced accuracy: trend 1.0, spectral (1+6/7)/2 = 0.928571; difference 0.071429, below the preregistered >=0.10 criterion. Moreover only 9 early-error-free models remain, below the preregistered minimum of 10. **Frozen primary success criterion NOT MET.**

## THEORY ledger

A one-dimensional local margin trend can identify delayed switch failures but is not a sufficient diagnostic of complete algorithmicity: ten of the twelve independently checked incorrect networks fail on HOLD after a SET or RESET prefix without any observed final-switch failure in the two frozen families. This is a trained-neural-system counterexample to using switch-margin trends alone as a full-alphabet certificate. The only sound inference of failure is an exact witness. An absence of witnesses within n<=2048 is an abstention, not a positive certificate.

## Kernel decision

**Kill this linear-extrapolation predictor as an independent breakthrough candidate** (no prospective advantage meeting criterion). Keep K001 active as switch-robust algorithm acquisition, but do not tune this threshold on the evaluated cohort. Next discriminating step: design an inductive full-alphabet abstraction with explicit reachable-set coverage and demonstrate it on new independently trained models, or obtain a genuinely prospective training-transition prediction on unseen architectures/tasks. Backups unchanged.

## Limits

No second task family, only second hidden dimension; no proof of generality; 32 is not a population prevalence estimate. Existing polyhedral RNN verification and neural algorithm acquisition are prior art. GitHub Actions reproduction is pending until public CI completes. All checkpoints, frozen predictions, exact witnesses, logs, and negative results are preserved in the Run268 archive.
