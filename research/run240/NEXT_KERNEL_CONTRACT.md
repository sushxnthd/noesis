# Sole active Kernel001 after Run240 (one prospective strengthening failure)
Question: Can a task-conditioned, representation-tolerant state-dynamics observable at a **provably incorrect** early checkpoint predict subsequent transition to exact all-length correctness, rather than mere detection of already-correct networks?
Frontier: Wang & Niepert 2019, Oliva & Lago-Fernandez 2020, van Rossem & Saxe 2025. Finite-state emergence and state regularization are not new.
Scalar criterion for next prospective test: freeze before any holdout; evaluate ROC-AUC on independently proven INCORRECT early checkpoints with independently resolved correct/incorrect final endpoints, at least 8 positive transitions and >=70% final resolution, score AUC>=.8 and >=.15 over both finite-fit and confidence controls. Avoid class-imbalanced retrospective selection. If insufficient transitions, primary fails rather than pooling already-certified networks.
Competitor: predicting current algorithmicity, certificate discoverability, or optimizer progress, not future acquisition.
Cheapest falsification: use existing new-task Run240 as development data only, then unseen seeds/architecture/task; exact checker on both early and final endpoints.
Publishable: independent public reproduction, mechanism-derived held-out prediction, spoof controls, priority audit and explicit limits.
Learning relevance: true gradient-trained incorrect-to-correct transitions; no positive selected from already-correct early checkpoints.
Kill: three failed prospective strengthening attempts total, or representation-equivalent adversarial reversal. Run240 counts as failure 1/3.
Backup (inactive): relational verification. No other active kernels.
