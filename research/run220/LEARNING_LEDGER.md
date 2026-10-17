# LEARNING ledger — Run220
24 genuinely newly gradient-trained fully coupled 3D tanh RNNs; Adam lr=0.03, 729 exhaustive length-six words, 200 epochs, CPU float64. All 24 achieved perfect finite training accuracy by epoch200; only 9/24 were perfect at epoch50.

Four exact-real incorrect(epoch50)->certified all-length correct(epoch200) transitions: 1301,1319,1427,1451. One early correct 1409. One persistent failure 1429. Other transitions remain unresolved rather than counted as acquired.

Sign-only suffix predictor did not outperform the strongest equal-compute baseline (AUROC delta=0.0 on the small classifiable subset). With only one verified persistent failure and 18 unresolved transitions, this is INCONCLUSIVE and not publishable evidence for a universal predictor.

Next action: improve proof coverage or obtain a new prospective cohort with sufficient verified persistent failures. Do not tune the frozen diagnostic on Run220.
