# NOESIS K001 Run272 — frozen protocol
Local pre-training SHA256: f900d2dfc30435cfd1f11faaae95f623318b776c33988d16cdd419848684e920
1. Question: Can a gradient-trained scalar ReLU latch model pass sampled finite training yet fail unrestricted correctness due to weakly positive RESET gain?
2. Literature: Ryou et al. CAV 2021 (RNN verification), Van Rossem & Saxe ICML 2025 (infinite generalization).
3. Exact success: >=1 all-position sampled-perfect uncertified trained model with independent exact error; >=1 certified trained comparator; zero invalid certificates.
4. Competitor: engineered adversarial RESET prior causes failure, not ordinary gradient training.
5. Falsification: matched paired training, unchanged Run270 checker, frozen block-family attacks, exact independent replay.
6. Publication: replicate without engineered prior on unseen task/architecture, mechanism prediction, priority audit.
7. Learning: all eight weights updated by Adam, matched seeds and data; intervention differentiable.
8. Kill: after three failed incremental discrimination attempts, reformulate.

Training: 24 paired seeds 19300..19323; h0=0; h'=ReLU(a[x]*h+b[x]), z=v*h+c, symbols 0 HOLD,1 SET,2 RESET. 256 random length20 sequences plus 27 length3 prefixes padded to20. All-position BCE, float64 deterministic Adam lr=.03, 500 updates. Checkpoints epochs 0,100,300,500. Baseline BCE only; intervention BCE+10*(a_RESET-2^-12)^2, no clamping. Frozen adversary: exhaustive all words through length8, and SET^k HOLD^n RESET with k=1,2,3,4,8,16 and n=0..128,192,256,384,512,768,1024,2048. Exact independent Fraction replay required. Retain all failures and abstentions. This is an intentionally engineered diagnostic stress test, not a natural acquisition law.

Inactive backups: parity representation merger; non-gated full-alphabet polyhedral simulation.
