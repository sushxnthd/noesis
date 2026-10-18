# NOESIS Run240 — prospectively frozen cross-task predictor FAILED
Protocol frozen on branch at commit b2a2ccbc79838dec4b2fcf832bba301fa244492a before any Run240 holdout training. 48 new 4D hardtanh gradient-trained RNNs (seeds 6201–6224, baseline/saturation) on RESET PARITY, not the development RESET LATCH task.
## Frozen primary
- Resolved endpoints: 31/48 = 64.58%, below >=70% required.
- Among resolved: 12 CERTIFIED, 19 independently provably INCORRECT; 17 ABSTAIN.
- Frozen early epoch100 predictor AUC: 0.9605263.
- Early finite training accuracy AUC: 0.8947368; gain +0.0657895, below +0.15 required.
- Early mean absolute training logit AUC: 0.7192982; gain +0.2412281.
- Thus primary FAILED despite strong resolved-subset discrimination. Do not relax criteria.
- Across all 2^17 assignments of abstentions to correct/incorrect, full-cohort score AUC ranges from 0.7196429 to 0.9709619; missing labels are consequential.
## Secondary exact observations
Epoch200 baseline: 5 certified, 10 incorrect, 9 abstain. Saturation: 7 certified, 9 incorrect, 8 abstain. Seed 6202 baseline is strictly incorrect at shortest witness 112222221 (length 9), while matched saturation is all-length certified (5 reachable states); both fit all training prefixes perfectly. Opposite direction: seed 6208 baseline certified (17 states), saturation incorrect at 101 (length 3). Thus intervention effects are heterogeneous, not evidence for a universal saturation mechanism.
Two independently implemented exact arithmetic checkers agreed on all 96 endpoint classifications. Stored float64 weights are interpreted as exact dyadic rationals. Signed-coordinate representation controls preserve graph counts (144/144 and 120/120); two corrupted readouts were correctly rejected.
## Smallest claim
A development-chosen state-graph/functional-margin score showed high prospective resolved-subset AUC on an unseen task, but FAILED its preregistered acceptance criterion and cannot establish a model-agnostic acquisition law. The training intervention produced one strict rescue and one strict reversal. Unresolved endpoints and prior-art collisions remain substantial.
