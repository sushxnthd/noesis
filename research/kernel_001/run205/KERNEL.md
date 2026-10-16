# Active Kernel 001 — full-alphabet inductive simulation

1. **Question:** Can hidden-state inductive simulation certify unbounded streaming parity in an actually gradient-trained, previously unused input-gated RNN architecture?
2. **Frontier:** Weiss et al. (2018) automata extraction; Jacoby et al. (2020) invariant inference; Ryou et al. (2021) RNN verification; van Rossem and Saxe (2025) learned parity. Novelty audit remains incomplete.
3. **Scalar criterion:** >=1 independently double-verified all-length certificate at frozen epochs 400/800 over seeds 211/223/227/229, and zero false accepts on finite-horizon spoofs.
4. **Alternative:** The scalar input-gated architecture makes parity structurally easy; certificate transfer does not imply a model-agnostic acquisition law.
5. **Falsification:** Exact both-bit interval closure, initial-state inclusion, strict output separation; reject 803-step same-architecture drift spoof.
6. **Publishable threshold:** Prospective unseen-task/architecture prediction beyond parity, sound independent proof, adversarial spoofs, priority audit.
7. **Learning threshold:** At least one gradient-trained checkpoint certified, with checkpoint-wise transition evidence.
8. **Kill:** Any false positive or three distinct unsuccessful transfer attempts without diagnostic improvement.

Backups (inactive): perturbation-stable certificates; causal hidden-state interventions. No second active kernel.
