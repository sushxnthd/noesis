# NOESIS K001 Run313 — second exact representation-acquisition trajectory

Run: `python research/kernel001/run313/reproduce313.py` and `python research/kernel001/run313/check313.py`. Both use only Python stdlib and original 28-number binary64 checkpoints.

**Exact result:** seed 22242 epoch20 h(000000)=h(100000)=(0,0,0), first such equal-length collision at n=6; for any suffix s, states remain identical although latch labels differ. Epoch80 is correct for all finite binary strings by the exact cone h1=0, 0<=h0<=7h2/10, h2>=2. Eight adversarial parameter mutations are rejected by the primary checker. An independent rational checker verifies the result using a different implementation.

Provenance: Run304 archived `source_checkpoints300_early.json` SHA256 `0aa10a00406a6316d2808a7d1424022724c7ce75a5cbbdc741dd0ad44ef2f6a1`; `source_checkpoints300_late.json` SHA256 `71f384d19e4e5ae95198b6bce2ec35f29f547b166ba293ffae60fe8a2d2d6f8d`. Epoch80 parameter array also matches Run312 source checkpoint. The two small JSON arrays here are copied from the source cohort; original whole-cohort source archives remain separately retained.

**Claim boundary:** retrospective exact second within-trajectory representation transition, not a model-agnostic predictor, new invariant theorem, or verified training mechanism.
