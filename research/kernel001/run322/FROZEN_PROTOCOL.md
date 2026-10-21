# NOESIS K001 Run322 frozen protocol

Frozen before outcomes. Input: original 96 Run315 epoch80 gradient-trained checkpoints, SHA256 72a273a42258e55f1092dc26664fd91777a8d2e56d6d598469e2abc0e63fab20. Labels fixed: 4 certified, 43 incorrect, 49 unresolved.

1. Question: can exact original-head tail evaluation identify previously unresolved finite-range failures?
2. Literature frontier: classical RNN extraction/verification and counterexample-guided testing, not a novel mathematical principle.
3. Single exact criterion: >=1 previously unresolved epoch80 checkpoint with strict wrong-sign logit on 0^n (logit > 0) or 10^(n-1) (logit < 0) at 11<=n<=128, AND zero such witnesses on four certified models. Ties are reported separately.
4. Competing explanation: head miscalibration, not loss of recurrent information.
5. Cheapest falsification: scan original exact binary64 rational recurrent parameters/readouts, n=1..128, 96 checkpoints, independently verify new witnesses.
6. Publishable threshold: mechanism-derived unseen-cohort prediction >=0.05 AUROC beyond loss, >=10 certified positives, >=30 witnessed negatives, spoof and priority audits.
7. Learning relevance: unmodified gradient-trained checkpoint with strict wrong-sign witness, not a post-hoc edit.
8. Kill: zero new unresolved failures or any contradiction with a previously certified checkpoint.

THEORY: exact wrong-sign readout is a counterexample to unrestricted correctness, not to the existence of another head.
LEARNING: distinguish output-head failures from representation collisions, compare with Run321; no causal acquisition claim.
