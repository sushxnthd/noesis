# NOESIS K001 Run272 — exact trained-model certificate loss

Frozen protocol SHA256: f900d2dfc30435cfd1f11faaae95f623318b776c33988d16cdd419848684e920. Train code/data and full evidence are archived separately pending GitHub mirroring.

24 paired random seeds (19300–19323), scalar symbol-conditioned ReLU RNN, all 8 parameters trained by Adam on 256 random plus 27 padded length-20 latch words. Baseline: BCE only. Intervention: BCE + 10*(a_RESET-2^-12)^2. This is an engineered adversarial prior, not natural acquisition evidence.

At epoch100, five models per arm were sampled-perfect and had exact full-alphabet certificates. At epoch300 and epoch500, all five baseline models remained certified; all five intervention models remained sampled-perfect but LOST the sufficient certificate and had exact delayed-reset counterexamples.

Seed | Epoch300 all-future SET HOLD^n RESET failure for n>= | Epoch500 n>=
19302 | 23 | 23
19305 | 21 | 21
19318 | 20 | 19
19321 | 18 | 18
19322 | 20 | 20

All ten all-future claims follow exact dyadic rational inequalities: a_HOLD>1, fixed point F=-b_HOLD/(a_HOLD-1)>=0, h_SET=max(0,b_SET)>F, a_RESET>0, v>0. Then h_n=F+a_HOLD^n*(h_SET-F) increases without bound; RESET readout eventually exceeds zero and stays incorrect for every greater n. Each minimal threshold n was found exactly, with exact nonfailure at n-1. Independent Decimal reimplementation checked all ten.

Full-alphabet interval-image checker independently validated 20 positive certificate instances across epochs100/300/500; ten adversarial witnesses and 20 corrupted/truncated controls passed independent checking.

Primary frozen criterion MET. This demonstrates a matched gradient-training intervention can destroy unrestricted algorithm correctness while sampled finite training accuracy stays perfect. It does NOT establish a model-agnostic acquisition law or a natural SGD transition. The intervention intentionally biases RESET gain positive.

Run271 immediately preceding: 24 matched pairs under a different intervention, 5 sampled-perfect and certified per arm, zero incremental discrimination; preserved as a negative result. Next: freeze a held-out cohort predicting the sign-crossing transition without tuning.
