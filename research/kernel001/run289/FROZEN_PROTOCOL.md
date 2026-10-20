# NOESIS K001 Run289 — Frozen before evaluation (2026-10-20)
Active kernel: K001-R, function-preserving gauge attack on Run288's prospective LP-distance diagnostic.

1. Question: Does the Run288 early LP feasibility-distance score change when a gradient-trained ReLU RNN is reparameterized without changing its function?
2. Frontier: Run288 achieved prospective AUC 0.816 for same-verifier certification at epoch80, not independent behavioral correctness. Neural formal-language learning and RNN verification are prior art; priority not cleared.
3. ONE EXACT PRIMARY CRITERION: For the 256 saved epoch20 trained checkpoints, score s=-relaxed_margin from Run288. Transform by G=diag(8,1/8). If max_seed |s(Gp)-s(p)|>1e-6, the score is falsified as representation-invariant.
4. Competing explanation: Raw score may change while ranking/AUC remain predictive. Numerical LP conditioning may also change.
5. Cheapest falsification: Frozen checkpoint digest d525a26b8858a0e3ce1edbc1a0b1174c1a57a9335624c0d691bbcf55b5a8e858. Compute gauge scores without training or label fitting. Independently check exact functional conjugacy on finite strings, and calculate unchanged-label AUC. Additional fixed gauges diag(1/8,8), diag(64,1/64), diag(1/64,64) are exploratory only.
6. Publishable threshold: Independent proof and verification plus concrete trained checkpoint, then prospective normalized replacement on unseen models with behavior-based endpoints and spoof controls.
7. Learning relevance: Every checkpoint comes from ordinary Adam/BCE training. Future epoch80 labels must remain unchanged. Report ranking/AUC even if primary noninvariance is detected.
8. Kill: If primary fails invariance, retire raw unnormalized LP slack as a model-agnostic acquisition diagnostic. Reformulate toward gauge-normalized scores. Do not infer noncertified models are incorrect.

THEORY: For positive diagonal G, ReLU(Gz)=G ReLU(z), hence A'_x=G A_x G^-1, b'_x=G b_x, v'=v G^-1, c'=c preserve all exact-real input-output predictions by induction. Whether LP slack is invariant is unproved.
LEARNING: 256 genuinely trained Run288 models, no new training. Gauge changes representation only.
Inactive backups: independently witnessed true-correctness endpoint; different recurrent activation.
