# NOESIS K001 Run295 — FROZEN 2026-10-20 (before untouched evaluation)
Active kernel: reachability-aware, task-observable diagnostic robustness.
1 Question: Does a provably unreachable output gate spoof the Run294 backward-observability repair on gradient-trained RNNs?
2 Primary literature: Jacoby/Barrett/Katz ATVA 2020 RNN invariants; Ryou et al CAV 2021 polyhedral RNN verification; DeepAbstract 2020 neural abstraction. Reachability and abstraction are prior art, not claimed novel.
3 Single success criterion: on 242 untouched width-3 epoch20 checkpoints, at least 140 have absolute divergent-augmented LP score change >1e-6; exact all-word equivalence and all six coordinates retained by structural pruning in 242/242. Failure of any exact proof fails criterion.
4 Strongest alternative: architecture/box-width artifact, not algorithm acquisition.
5 Cheapest falsification: exact rational structural+reachability checker and LP evaluation. Stable-clock control must preserve 242/242 scores within 1e-8.
6 Publishable: only with priority audit, independent checker, frozen evidence, spoof baselines, new learning prediction, actual trained-system relevance.
7 Learning threshold: >=140 score changes on genuinely gradient-trained original networks. Added neurons are engineered, not learned; no acquisition transition claimed.
8 Kill: primary failure, stable control failure, or three failed substantive improvements to kernel.

Frozen construction: append z1,z2,g to trained width3 ReLU RNN, no feedback into original units; initial all zero. Divergent z1'=ReLU(2*z1+1), z2'=ReLU(4*z2+3); stable z1'=ReLU(z1/2+1), z2'=ReLU(z2/2+3); both g'=ReLU(z1-z2-1), output coefficient of g=1 and z1,z2=0. z2>=z1>=0 inductively, hence g=0 on all finite words. z1,z2->g->output is a nonzero structural path, so Run294 pruning retains all six units. Exact removal of reachable-zero gate and its auxiliary units restores the original score, but is only a narrow repair.

Pilot ONLY 21440,21441,21442, excluded from primary. Primary seeds 21440..21695 excluding {21440,21441,21442,21450,21451,21452,21453,21454,21455,21494,21501,21549,21585,21674}; n=242. These original networks were trained in Run291; this is a frozen adversarial test on existing trained networks, not fresh prospective learning validation. Separate THEORY and LEARNING ledgers; preserve failed experiments and CI.
Backups inactive: cross-task prospective prediction; causal intervention at certification onset.
