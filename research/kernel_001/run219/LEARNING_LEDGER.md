# LEARNING — Run219

12 previously gradient-trained scalar gated-tanh RNNs; evaluation uses epoch100 scores and epoch800 all-length ground truth. Actual certified transitions: 661,701,733. Persistent failures: 677,683,691,739. Already certified at epoch100: 659,673,709,719,727. No training was performed in this run. All five early positive certificates were checked with independent rational Decimal and mpmath interval arithmetic.

Suffix AUROC .7500, generic uniform .5833, histogram-shuffle .6667. Frozen gain +.0833 <+.10; only three verified acquisitions (<4). **Negative result; no retuning on this cohort.**

Current single active kernel remains behavioral sign-only prediction of verified learning transitions, with one failed substantive transfer test (Run219). The next attempt must use newly trained unseen architecture/task, or reformulate if evidence warrants. Inactive backups: proof-guided transition localization and suffix intervention.
