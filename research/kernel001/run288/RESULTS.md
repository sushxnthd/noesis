# K001 Run288: prospectively frozen invariant-distance diagnostic

Frozen protocol committed before training at 461eaeee7052c469723a714b9067e6013e7f66f1. Pilot/score selection used only old Run286 seeds 20800–20927. Held-out 256 fresh seeds 20928–21183, ordinary float64 BCE/Adam, width-two symbol-conditioned ReLU RNN, 15 trainable parameters, sequence length 6.

**Primary endpoint is existence of an independently exact-checked two-box certificate at epoch 80, NOT unrestricted incorrectness when absent.** Epoch20 scalar is negative minimal common LP slack for invariant feasibility, across four fixed masks and output delta=0.05.

Frozen primary PASSED: 47 certified, 209 noncertified; ROC-AUC(score)=0.8159421765 vs ROC-AUC(-BCE)=0.4325562455; delta=+0.3833859310 (1000-seed bootstrap percentile 95% interval [0.30323515,0.46545661]). AUC(early accuracy)=0.63926499; AUC(-parameter norm)=0.50402117.

Independent exact SymPy checker: 141 certificate checks and 378 exact wrong-word checks across checkpoints; 0 contradictions. At epoch80: 47 certified, 132 exact incorrect witnesses, 77 other noncertified/unknown. Among the 127 epoch80 sampled-perfect models, only 3 had exact wrong-word witnesses; absence of witnesses for other uncertified models is NOT evidence of correctness.

**Learning relevance threshold NOT MET:** 4 (required >=5) epoch20 sampled-perfect, exact incorrect -> epoch80 exact certified transitions, seeds 20977,21000,21012,21113 (early witness lengths 17,30,10,14). This run therefore supports prospective *certificate-onset prediction*, not a validated model-agnostic law of learned algorithm acquisition.

Strongest competing explanation: self-referential certificate geometry. LP slack measures proximity to the same sufficient two-box family used to label the endpoint; the endpoint is not complete. The exploratory Run283 spoof audit gives nonzero LP slack for all 8 previously verified width-two finite-horizon spoofs, but this is an in-family test and not an independent mechanism test. No novelty clearance, no cross-architecture transfer.

Exact full-cohort checkpoint SHA256 d525a26b8858a0e3ce1edbc1a0b1174c1a57a9335624c0d691bbcf55b5a8e858; early-score SHA256 d1fa94298a74ae79f59da22fc239d3e451cc2432a970e0d533bc4bb3245fed8a. Fresh-process training reproduction byte-identical. Raw checkpoint, outcomes, optimizer state (saved as optimizer288.pt), full evidence and failed hypotheses retained in local evidence archive; public CI workflow uploads raw checkpoint and outcomes when successful. No model-agnostic breakthrough claimed.
