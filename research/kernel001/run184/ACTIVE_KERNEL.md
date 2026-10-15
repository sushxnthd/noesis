# Sole active Kernel 001 — matched-difficulty algorithm acquisition
1. **Question:** Can a task-coupled structural diagnostic predict a trained network's compositional generalization beyond training MSE and its 32-cycle trajectory, without mistaking one-word periodic correctness for a reusable algorithm?
2. **Primary frontier:** El-Naggar et al., PMLR 217 (2023) exact ReLU counting conditions; Dave et al., PMLR 284 (2025) counter/Dyck learnability. Run 183 proves one-word periodic correctness, not algorithm acquisition.
3. **Scalar success:** On prospectively frozen, independently trained unseen checkpoints, AUROC improvement >=0.05 over strongest training-loss and 32-cycle baseline, with >=8 positives and >=8 negatives.
4. **Strongest competitor:** Short-horizon slopes already explain generalization; cyclic-phase errors are ordinary affine order sensitivity.
5. **Cheapest falsification:** Evaluate all rotations of a previously certified balanced word on an unchanged trained checkpoint, then compare to frozen 32-cycle baseline.
6. **Publishable threshold:** Multi-seed/architecture transfer, independent exact checker, spoof baselines, unseen prediction, priority audit, explicit smallest claim.
7. **Learning threshold:** Predict or track a genuine gradient-training transition on unseen networks, not just analyze one checkpoint.
8. **Kill condition:** After three substantive failed prospective improvements, kill this formulation or reformulate; never promote periodic invariants to a global algorithm law.
**Backups (inactive, <=2):** gradient-stage matched transfer; adversarial mixed-word semigroup test.
