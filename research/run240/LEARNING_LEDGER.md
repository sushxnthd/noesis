# LEARNING ledger — Run240
48 new gradient-trained hardtanh RNNs on unseen reset parity, 24 matched baseline/saturation seeds; 144 checkpoints at epochs 0,100,200. No holdout tuning.
Epoch200: baseline 5 certified/10 incorrect/9 abstain; saturation 7 certified/9 incorrect/8 abstain. Resolved 31/48.
Seed 6202: strict baseline incorrect -> saturation certified, both 100% training fit. Seed 6208: opposite, baseline certified -> saturation incorrect. No universal saturation mechanism claim.
Early predictor resolved-subset AUC 0.960526, training accuracy 0.894737, confidence 0.719298. Frozen primary FAILED due coverage and accuracy-baseline margin. First prospective failure for reformulated kernel.
