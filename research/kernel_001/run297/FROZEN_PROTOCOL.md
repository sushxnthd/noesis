# NOESIS K001 Run297 — FROZEN before training

Date 2026-10-20; parent Run296.
1. Question: does the gauge-normalized LP diagnostic transfer from reset/toggle parity to a persistent latch (state q_0=0; q_{t+1}=q_t OR x_t) learned by gradient descent?
2. Frontier: Dan/Bastani/Roth (2022) regular-language generalization; Butoi et al. (2024) formal-language recognition; Khmelnitsky et al. (2023) property-directed RNN verification.
3. Primary exact criterion: epoch20 gauge LP ROC-AUC minus negative epoch20 BCE ROC-AUC >= +0.10 on independently resolved epoch80 correctness, with >=10 certified and >=25 exact incorrectness witnesses. Report all unresolved.
4. Strongest competing explanation: diagnostic predicts its own verifier feasibility, not true unrestricted correctness.
5. Cheapest falsification: 128 new seeds 21800..21927, width3 float64 ReLU RNN, Adam .025, 160 random length6 sequences + four fixed prefixes, 120 epochs, snapshots 0/20/40/80/120. Freeze epoch20 score digest before endpoint evaluation; independent exact rational certificate and witness checking.
6. Publishability: cross-task prospective replication plus public reproducibility, priority audit, spoof baselines, and an unseen-condition prediction.
7. Learning relevance: >=2 sampled-perfect yet exactly incorrect to independently certified correct transitions.
8. Kill: failed primary criterion or three failed strengthening attempts -> reformulate; invalid certificate immediately voids any positive claim.

LP: preserve Run291 constraints, delta=.05, canonical gauge d_i=1/max_x |b[x,i]|; change only state transition to y=s OR x. Label at each step q_t. Baseline negative BCE.
Semantics: exact-real recurrence with float64 parameters interpreted as dyadic rationals, not rounded runtime.
THEORY: cross-task certificate-distance test, no representation-independence claim.
LEARNING: fresh trained cohort, exact outcomes, report abstentions and failures.
