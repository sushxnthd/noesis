# NOESIS Run262 frozen protocol (pre-training)

Frozen 2026-10-19 before new seed18201–18216 training.

**Question:** Can a sound exact wrong-attractor invariant (2D ReLU RNN, pure-hold input) predict delayed failure in independently gradient-trained finite-perfect set/reset latch models without long-horizon screening?

**Cohort:** 16 new seeds 18201–18216, two-unit float64 ReLU RNN, 512 random length-20 examples plus all length-3 prefixes padded with hold, Adam lr 0.03, 600 epochs. Epoch600 only for primary endpoint. Retain 0/100/300/600 checkpoints.

**Pre-outcome diagnostic:** Enumerate four activation masks, exact binary-rational affine fixed points; seek forward-invariant weighted-infinity boxes (k<=16 hold steps) or exact convex polygons (k<=16, width<=8). Positive fixed-point output plus verified Schur stability and forward invariance is a *sound eventual hold-failure certificate*. Otherwise abstain. No long-horizon labels used for proof construction.

**Scalar success:** >=3 independent finite-training-perfect networks with exact incorrect-attractor certificates using <=16 hold steps, zero false positive certificates. Check exact first hold error up to 2048 afterwards; exact proof itself establishes eventual error beyond finite horizon.

**Competing explanation:** diagnostic only rediscovers immediate failures. **Learning relevance:** >=3 finite-perfect scratch-trained models with failures beyond length-20 training. **Publishable:** independently replayed proofs, exact witnesses, priority audit, external reproduction. **Kill:** fewer than 3 finite-perfect detected, or independent checker invalidates a certificate.

**Theory ledger:** soundness conditional on exact invariant and Schur-stable affine mode; not a model-agnostic acquisition law. **Learning ledger:** independently trained network failures, not seeded from certified model. **Backups:** reparameterization-invariant templates; mixed-input abstractions (inactive).

**Prior-art frontier:** polyhedral RNN verification and neural algorithm acquisition already exist; this run tests an executable trained-system diagnostic, not priority for those theories.

Frozen source SHA256:
- train_frozen.py 89820499b5f57a0ca39bebba5083e7de04d20ae4b7672296e168beeadcf2ebc0
- attractor_certify.py 098a7d88db70988f2fd55f74198b17ceffdbf76fc3cf290922e4b5020c83f00b
- FROZEN_PROTOCOL.md 77924a86d1bfde46c7bb9f1d1a7f447bdb6d3623fe3acfef2f147354a62a0a11

The full frozen files and evidence will be included in the run archive; branch must remain isolated from main.