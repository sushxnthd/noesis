# Run 139 — task-coupled failure horizons

Source: Run138 ordinary gradient training of 22 ReLU RNNs, Adam 1200 steps, all A/E/w optimized; source RAW_OUTCOMES.json SHA256 `4b8841844b7b32a443588e95144a77f7f7da2cd4e13d48bd7baf9f4f1847b10f`. Eight eligible trained checkpoint witnesses are minimized in ELIGIBLE_CHECKPOINTS.json. Full 22-checkpoint raw artifact is in the local reproducibility package, **not yet mirrored to GitHub**.

THEORY: If A[j,j]=1, Eplus[j]=b>0, Eplus[k]<=0 and A[k,j]<=0 for all k!=j, induction gives h(+^n)=n*b*e_j. With output gain g=w[j]*b, exact first strict error > 0.1 is floor(0.1/|g-1|)+1 for g!=1. Only plus-only real-arithmetic recurrence is certified; not all words or hardware float execution.

LEARNING: Eight ordinarily trained checkpoints across 2D/3D and float32/float64 satisfy the exact internal ray; 8/8 passed length-256 tests, but 0/8 has exact output gain. Exact first failure horizons: 12173660, 881096922110118, 1400043, 5204928, 1638808763908189, 4440637, 3824100, 2218939927293197. For paired eligible seeds 80/95/206, float64-to-float32 horizon ratios are 7.24e7, 3.15e8, and 5.80e8. This is post hoc analysis, not a held-out predictor validation.

INDEPENDENT: Local integer-ratio checker independently verified 8/8 rays, 11 exact states per case, and both n-1/n minimality inequalities. Compact GitHub checker uses Fraction. Local pytest 3/3; compact pytest 1/1.

WILDCARD: Seed80 float64 readout one-ULP changes moved predicted failure horizon from 881096922110118 to 318599112815325 (+ULP) or 1150956121293694 (-ULP).

Smallest claim: finite-horizon accuracy and an exact learned internal recurrent mode do not suffice for exact task-level output counting. Elementary restricted theorem, not a model-agnostic certificate or priority-established novel result.

Primary literature: El-Naggar et al. ICGI 2023 https://proceedings.mlr.press/v217/el-naggar23a.html ; El-Naggar et al. EACL SRW 2023 https://aclanthology.org/2023.eacl-srw.15/ .

Active Kernel 001 only. Kill condition: any independent minimality mismatch or lack of precision/architecture coverage kills the empirical extension. Next: prospectively frozen approximate task-coupled predictor versus hidden-gate spoofing.
