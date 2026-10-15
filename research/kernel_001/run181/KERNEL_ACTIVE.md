# NOESIS — exactly one active Kernel 001 (post-Run181)

**Status:** Neutral-composition probe D retired as a predictor. Bounded verification remains auxiliary. No backup kernels promoted.

1. **Precise question.** Is the apparent sufficiency of a 32-cycle output-drift baseline for long-horizon balanced-composition transfer a peculiarity of gradient-trained ReLU recurrent cells, or does it survive a held-out gated architecture?
2. **Primary-literature frontier.** Weiss, Goldberg & Yahav (ACL 2018) compare finite-precision recurrent counting capacities; Chen, Ma & Li (ICML 2025) formalize non-asymptotic length generalization; Huang et al. (NeurIPS 2025) analyze learned state-tracking mechanisms. Architecture-specific numerical heuristics are prior art.
3. **Single exact success criterion.** In a prospectively frozen cohort of at least 64 GRU checkpoint–balanced-word evaluations with training MSE <1e-3, observe at least eight misclassifications by the unchanged 32-cycle linear extrapolation baseline at 2,048 repetitions. Otherwise the proposed architecture reversal is unsupported.
4. **Strongest competing explanation.** Low training error and short-horizon drift already determine the evaluated generalization outcomes; a new structural diagnostic cannot improve on them.
5. **Cheapest decisive falsification.** Before running long-horizon evaluation, freeze GRU seeds, training objective, word families, 32-cycle baseline and all checkpoint selection rules. Train on the same length-six counting traces; compute frozen predictions; evaluate the unseen repeated compositions with an independent replay.
6. **Publishable threshold.** A newly motivated, spoof-resistant predictor prospectively beats loss and drift baselines across GRU and ReLU, unseen seeds, a second task family, independent checker and priority audit. Eight baseline errors alone are not publishable.
7. **Learning relevance threshold.** Models must actually undergo gradient training. Demonstrate that a new diagnostic predicts changes across checkpoints, not only post-hoc automata.
8. **Kill condition.** After three substantive GRU/architecture-transfer tests without baseline errors, kill this line. Do not scale merely to search for a positive; preserve all negatives.

**THEORY:** Finite-horizon agreement remains insufficient for unbounded algorithm acquisition.
**LEARNING:** Run181: 48 trained snapshots, five sampled bounded-horizon fail-to-pass transitions, zero AUC advantage. Retrospective matching search found **zero** opposite-label pairs matched within 0.25 log10 units on both MSE and 32-cycle B; thus matched-pair mining of this cohort is not a viable primary direction.

**No second active kernel.** Wildcard probes remain isolated and may not contaminate frozen evaluation.
