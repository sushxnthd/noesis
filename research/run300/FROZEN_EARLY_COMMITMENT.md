# NOESIS Run300 — frozen early-score commitment

New holdout: 384 seeds 22200–22583 inclusive, unmodified width-3 ReLU RNN persistent-latch training from Run297. Early snapshot at epoch20, before late-stage training.

Early checkpoint SHA256: `0aa10a00406a6316d2808a7d1424022724c7ce75a5cbbdc741dd0ad44ef2f6a1`.

Frozen early score JSON SHA256: `aad9098f97fbffba02c54cd468477b90b229c95da4ef93771ee52cc7cce3bb40`.

Finite gauge scores: 384/384. Sampled-perfect at epoch20: 1/384.

**Primary fixed test**: Delta = ROC-AUC(epoch20 negative BCE) - ROC-AUC(epoch20 gauge LP), restricted to exactly resolved epoch80 endpoints. Delta >=0.20 with >=4 exactly certified positives and >=50 exact negative witnesses. No reclassification of unresolved. Bootstrap 2000 stratified replicates seed 300.

Scoring function and exact scalar-cone certificate are unchanged from Run297 and Run299, respectively. This commitment predates late-stage training and endpoint evaluation. Outcome labels not inspected.
