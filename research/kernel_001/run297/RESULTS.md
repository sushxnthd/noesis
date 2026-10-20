# Run297 frozen latch transfer: FAILED

New 128 gradient-trained width-three ReLU RNNs, seeds 21800..21927. Epoch80 sampled-perfect: 63. Exact incorrectness witnesses: 70, independently checked with rational arithmetic. No exact unrestricted-correctness certificates; 58 unresolved, including 58 sampled-perfect. Five sampled-perfect models are provably incorrect on longer inputs: seeds 21815,21822,21856,21895,21912. Seed 21815 fails on eight zeros, having trained on length six.

Frozen ROC-AUC primary criterion failed: no certified positive endpoints, so ROC-AUC is undefined. Exploratory expanded state-0 box produced no certificates. Do not relabel unresolved as incorrect.

THEORY: two-box diagnostic not established as cross-task correctness predictor. LEARNING: five exact finite-horizon generalization failures in gradient-trained networks; no new acquisition transitions.

Frozen score SHA256 9db6047ca36e307a9577696187ec0a977060eda793792f6936b4ed452b2af662; checkpoint SHA256 620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473.
