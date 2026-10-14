NOESIS Run 147 frozen before training, 2026-10-14.
Question: can constant ReLU activation masks observed at plus-only lengths 33..64 predict first error >0.1 through length 512 in eight unseen gradient-trained four-state RNNs?
Seeds 208..215, float32, all ternary length-six words, Adam 1200 steps lr .025, no hidden-state supervision or output calibration.
Eligibility: mask constant at steps 33..64, no zero preactivations. Predictor: continue affine masked recurrence from h64 to h512 with exact-rational stored weights. Independent truth: full nonlinear exact-rational rollout. Score: exact first-failure index or no failure, abstentions fail; success >=6/8.
Competing explanation: late mask switch. Falsification: independent exact checker and ReLU cap spoof changing at length 65. Publishable only after cross-architecture and all-alphabet certification. Learning relevance: new trained model with delayed failure. Kill if <6/8 or spoof accepted as certificate. Record MSE and linear-error baseline; do not tune thresholds.
Prior work: El-Naggar et al. ICGI 2023 on exact ReLU counting; piecewise-affine reachability classical.
