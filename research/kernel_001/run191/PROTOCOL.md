NOESIS RUN191 FROZEN PROTOCOL 2026-10-16
Question: Can frozen zero-tail probes falsify all-length parity in unseen gradient-trained RNN checkpoints that pass exhaustive length-12 parity?
Primary scalar: number of distinct new seeds with an epoch300 or epoch600 checkpoint that passes all 4096 length12 binary sequences at every prefix but has wrong-sign prediction on any frozen zero-tail input length >=13 and <=518. Success >=1; otherwise negative.
Frozen seeds: 157,163,167,173. Model: width8 float64 tanh RNN, W,U,v Gaussian scale .3; b,c zero; Adam .02; 600 updates; all 64 length6 binary words with every-prefix parity supervision. Checkpoints 0,300,600.
Frozen zero-tail prefixes: 0,1,101000,101001; append 0^k for k=0..512. Evaluate every prefix. All 4096 length12 strings evaluated for every checkpoint. Additional random length128: 128 sequences per checkpoint with numpy RNG seed191; nonprimary.
A finite wrong-sign witness refutes all-length parity. Independent mpmath.iv at 70-digit intervals on stored float64 parameters required for positive witness. No all-length claim from absence of witness.
Frontier: Van Rossem/Saxe ICML2025 parity algorithm emergence; Jacoby/Barrett/Katz ATVA2020 invariant verification; Ryou et al CAV2021 polyhedral RNN verification.
Strongest competitor: this is merely longer test horizon, not mechanism or algorithm certificate.
Cheapest falsification: no length12-perfect checkpoint with held-out zero-tail failure.
Publishable threshold: independent infinite-family failure, prospective superiority over length-matched random/periodic baselines, unseen architecture/task transfer and priority audit.
Learning relevance: new gradient-trained checkpoint artifacts, training loss, exact counterexamples.
Kill condition: three consecutive failed mechanism-transfer runs, reformulate or kill.
No personal spend. Keep separate THEORY and LEARNING ledgers and all negative results. Branch research/kernel-001-run191-zero-tail-mechanism.
