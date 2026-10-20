# NOESIS Run292 — function-preserving duplication falsifies representation independence

**Decision:** retain Kernel 001, retire the interpretation of gauge-normalized box-LP distance as a model-agnostic algorithmicity law. The score can still be a fixed-architecture predictor.

**THEORY:** With E(h0,h1,h2)=(h0,h1,h2,h0), exact rational A'_x E=E A_x, b'_x=E b_x, v'E=v and ReLU(Ez)=E ReLU(z) imply exactly identical logits for every finite word. An independent checker verified these identities on all 246 trained parameter sets.

**LEARNING:** Epoch20 gradient-trained Run291 width3 networks: 116/246 scores change by >1e-8. The strictly untouched sensitivity subset excludes five previously probed acquisition seeds: 113/241 changed, 4273 ranking inversions. Maximum difference 0.8165373583020912 at seed 21546 (original -0.1802546453772237; duplicate -0.9967920036793149). On the 101 exactly resolved untouched endpoints (19 certified / 82 incorrect), conditional ROC-AUC 0.9226573 -> 0.9050064. This is a diagnostic failure mode, not a new learning transition.

**Caveats:** Seeds 21494, 21501, 21549, 21585, 21674 were explored before full evaluation, so the full 246 are not prospectively untouched. Initial contents-API writes were blocked, and protocol was committed using Git data API after local computation. Do not call the experiment publicly preregistered. LP scores are numerical; all-word function preservation is exact rational. Prior art includes positive rescaling invariance and known limitations of non-relational interval/box abstractions. Do not claim neuron duplication itself is novel.

**Reproduction:** Obtain `checkpoints291.json`, `outcomes291.json`, and `diagnostic291.py` from the complete Run292 evidence archive. Run `python independent292.py` and `python run292_attack.py` from the same directory. The archive also contains all 246 raw scores, tests, ledgers, SHA256SUMS, and the failed initial float-rounding check provenance.

**Active kernel eight fields:** Question: function-level invariance of learned-algorithm diagnostic. Frontier: known ReLU gauge invariance and box abstraction weaknesses. Exact success: >=50 of 246 score changes (and >=50 of 241 clean sensitivity). Competing explanation: representation-dependent box relaxation. Cheapest falsification: exact duplicated-unit identity plus paired LP. Publishable threshold: independently verified all-word equality and nontrivial trained-model effect with prior-art audit. Learning threshold: genuine gradient-trained checkpoints and frozen endpoints. Kill: <5 untouched changes; otherwise revise score/abstraction.

**Backups (inactive):** (1) cross-task/architecture independently resolved correctness, (2) relational certificate for duplicate-correlated neurons.
