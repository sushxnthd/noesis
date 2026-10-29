# NOESIS R450 — exact training-support and DFA-label-exposure audit

**Date:** 2026-10-26. **Verdict:** substantive classical experimental-design audit, NOT a new neural causal mechanism, neural theorem, or prospective replication. No new training, thresholds retuned, or user hardware/spend.

## Frozen design and original failure
Protocol frozen before seed-specific training reconstruction or new retrospective neural aggregation: SHA256 7e6b28688563d58a4dbb73cac8c35fb7c7fe337772dc1c87c2a6ecfde1cfb4e4. Original primary source SHA256 0a5c18df7e5aa6bd2232b0bb0449cfa11a44dc87fe7549a0d378d8fea0996bde. It failed with a KeyError because archived R449 policy is named u, not pure_u. Original source/error retained; frozen field-name-only erratum SHA256 76b785a37685219833cb4d1a668cc4d6bb744b8d68ed7dadf7191022e9191e80; corrected source SHA256 4489e4cef0e026a7f23291af9391fc17228c1956dc486f7383704a61b6e5f155. Independent checker protocol SHA256 eceffa1378505c6bc590643d1c687186dca74211f3bb9c880725931301f91099.

## Exact R418 training-support audit
The original R418 models were trained on 196 length-eight binary strings per seed, 192 Torch-seeded random plus four fixed, with tokenwise labels. The four seed-specific inputs have 139, 136, 139, and 143 UNIQUE eight-bit strings. Reconstructed training X/Y tensors match every archived bytewise SHA256 digest for both tasks and all three architectures. Training inputs are reused across architectures and tasks for a given seed; states and architectures are not independent training-dataset replications.

Each actual R418 evaluation readout has physical input length 14+20n+1: at n=0,1,2,16,32 these are 15,35,55,335,655 bits. **All 108 evaluation contexts are outside the empirical full-sequence length support even at n=0.** Under the empirical training input distribution, probability of these complete strings is zero. This does NOT imply the trained networks cannot extrapolate, does not invalidate measured deterministic total-input contrasts, and does not invalidate R418's conditional graph certificates.

All original 18 twenty-bit legal designated-state-neutral words have complete 1..6-gram coverage in every seed-specific training corpus. At k7, 14/24 TaskA and 17/48 TaskB task-seed-word comparisons contain unseen windows. At k8, 24/24 TaskA and 48/48 TaskB contain unseen windows. First eight bits of original evaluation prefixes appear in training for 9/12 TaskA and 17/24 TaskB seed-prefix combinations. Local short-gram coverage therefore does NOT imply full-string support.

## Exact task-dependent label exposure
Independent DFA dynamic programming and exhaustive enumeration of all 256 eight-bit words agree on 16/16 task-position label vectors. Under uniformly sampled eight-bit strings, class-2 token exposure across all eight supervised positions is exactly 597/2048 = 29.150390625% for TaskA (ones mod3), but 193/1024 = 18.84765625% for TaskB (01-count mod3). TaskB class2 is absent at positions 1..3 and occurs in only 1/16 length-four prefixes. Reconstructed empirical class2 exposure: TaskA 29.018%,28.890%,28.890%,30.804%; TaskB 19.196%,19.452%,19.069%,18.367%. This imbalance is real, but NOT causally identified as the source of TaskB neural failures.

## Archived neural negative control, explicitly retrospective
All 108 immutable R449 model-state contexts were reaggregated without retraining or tuning. Pure-u suffix1 n0 errors: TaskA 0/36, TaskB 10/72; at n32: TaskA 1/36, TaskB 18/72. Original R425 early-robust counts remain TaskA 22/36 and TaskB 24/72. These are reused outcomes and cannot establish population inference from four deterministic seeds. They do not identify a neural-specific causal transition mechanism.

## Independent checks and preservation
Independent source reconstructed all seed-specific training strings, enumerated the DFA over all 256 length8 inputs, and recomputed every original word and archived neural error flag. PASS: 16 DFA position vectors, 8 training uniqueness checks, 8 token-label reconstructions, 64 kgram coverage checks, 36 prefix8 support checks, 72 word-gram reconstructions, 72 word-neutrality checks, 108 neural oracle checks, 1080 archived policy error flags, and exact length-support condition.

Complete reproducibility archive NOESIS_R450_Reproducibility.zip SHA256 4b14c9c58cb5305a016f92038e7e4cd2f0d7fe63284bc722c3cd5de4df92a853, 26 entries/25 independently SHA256-manifested payloads, four clean deterministic output SHA replays PASS. Includes frozen source, original error/erratum, all primary/independent raw and outputs, and immutable nested R449->R418 checkpoint dependency.

## Scope and next decision
R450 is a methodological correction, not an original length-generalization result. The existing cohort does not by itself disentangle long-sequence extrapolation from neutral-cycle effects. A new neural mechanism claim requires a prospectively frozen length-aware matched control and genuinely disjoint independently trained checkpoints, both DFA tasks, three architectures, meaningful non-ceiling readout target, strongest early n0..2 signed-margin/CE/d32 controls, and external novelty review. No automatic retraining or post-hoc rescue of R449.

Prior art: Buitrago Ruiz & Gu, ICML2025 https://proceedings.mlr.press/v267/buitrago25a.html ; Dan/Bastani/Roth 2022 https://arxiv.org/abs/2202.09717 ; Dave et al 2025 https://proceedings.mlr.press/v284/dave25a.html ; Chen/Ma/Li 2025 https://arxiv.org/abs/2506.03085 ; Dankowiakowski/Ronca NeurIPS2025 https://proceedings.nips.cc/paper_files/paper/2025/hash/c03c2e3e2ad8057aefc3da880476784d-Abstract-Conference.html . R412 finite-trace classical theorem and R431 mediation obstruction are not claimed anew.
