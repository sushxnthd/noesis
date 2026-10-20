# Run 303: exact cone certificate

Retrospective recheck of 384 Run300 gradient-trained persistent-latch RNNs. The quarter-step threshold grid previously certified 17. Analytic rational threshold search certifies 18, adding seed 22438. The compact exact certificate for this seed is T=71/25, mu0=1127/1000, mu1=17/1000.

THEORY: v>=0, b0<=0, v A_x >= mu_x v and mu_x T+v b_x>=T imply an inductive reachable cone after first input 1. T+c>0 gives the positive output. No new universal theorem or priority claim.

LEARNING: epoch20 of seed 22438 fails on input 1; epoch80 is certified correct on every finite input. Thus this trajectory crosses from incorrect to unrestricted-correct somewhere between the checkpoints. No transition epoch, mechanism, or intervention is identified.

Cohort after Run303: 18 exact positives, 181 exact negatives, 185 unresolved. The full 384-row retrospective scan and source files remain in the local evidence archive; only the newly certified trained checkpoints are mirrored here. Do not relabel unresolved cases.

Active K001: predict all-length correctness beyond early BCE, resisting function-preserving spoofs; frozen unseen task/architecture AUC improvement >=0.10 with >=10 positives and >=50 negatives. Kill after three substantive failures. Backups remain inactive.
