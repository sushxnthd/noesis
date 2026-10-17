# Frozen Run 214 protocol (before training)

Seeds: 953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171.

Use Run 213 coupled-2D reset-parity training, epochs 0,50,100,200. At epoch 100 compare task-retention minimum signed margin on 10^k1 (k=0..8, 54 token steps) to generic minimum signed final and prefix margins on nine fixed ternary words of lengths 2..10 from numpy default_rng(2142026), also 54 token steps. Additional baselines: negative training loss and negative heldout prefix errors as Run 213.

Endpoint epoch200 labels require two independent interval checkers: all-length inductive proof = CORRECT; strict wrong-word witness = INCORRECT; otherwise UNRESOLVED. No inference from abstention.

PASS iff AUROC(retention) exceeds strongest of four baselines by >=0.10, with >=4 CORRECT, >=4 INCORRECT, <=6 UNRESOLVED. Otherwise FAIL or INCONCLUSIVE if labels insufficient. Do not tune after results. Kill retention superiority claim on FAIL. Publishable only with priority audit, independent proof, adversarial spoofs, unseen architecture and task. THEORY: finite probes spoofable; induction sufficient not necessary. LEARNING: prospectively test whether task-specific margin predicts real trained outcomes.
