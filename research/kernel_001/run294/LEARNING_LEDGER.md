# LEARNING ledger
245 untouched *previously gradient-trained* width-three RNN checkpoints from Run291; no new training in local experiment. Source checkpoint SHA256 860b9f3856b7bfa8a22fcf7cbebc1cbb65403fdea9691546e2faf5b728f195c6.

192/245 output-equivalent divergent-clock augmentations changed diagnostic score by >1e-6 (frozen threshold 150). Bounded stable control 0/245 changes. Pruning recovered 490/490 scores. The added coordinate is engineered post-training, not naturally learned. This is a negative diagnostic-robustness result, not a new acquisition transition.

Next decisive target: prospectively frozen transfer to a different learned algorithm/task with correctness outcomes independently resolved, and task-observable certificates.
