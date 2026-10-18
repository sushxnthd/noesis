# Reformulated sole active Kernel001: prospective abstention-aware acquisition prediction (NOT YET RUN)
1. Question: Can an early-training state-dynamics observable prospectively predict later all-length correctness rather than provable incorrectness in gradient-trained neural systems, beyond finite fit and confidence?
2. Frontier: Wang & Niepert 2019 state regularization; Oliva & Lago-Fernández 2020 state stability; van Rossem & Saxe 2025 algorithm development. Finite-state emergence is known.
3. Scalar success: frozen held-out resolved-checkpoint ROC-AUC >=0.80 and >=0.15 above both finite accuracy and output-confidence baselines, with >=70% resolved coverage.
4. Competitor: predicts certificate discoverability or generic optimization, not actual acquisition.
5. Cheapest falsification: freeze observable on prior checkpoints, evaluate unseen seeds and another task family with exact certificates/witnesses; abstentions excluded from AUC but reported.
6. Publishable: independent CI, cross-task/architecture prediction, spoof-resistant mechanism, priority audit.
7. Learning relevance: early prediction on actual trained systems with independently proven positive and negative endpoints and finite-fit controls.
8. Kill: three prospective failures or representation-equivalent adversarial reversal.
Backup inactive: representation-invariant relational verification. No other active kernels.