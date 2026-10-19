# Run 275: Frozen natural acquisition audit
Date: 2026-10-20. Branch: research/kernel-001-run275-natural-acquisition.
ACTIVE KERNEL: exactly one, full-alphabet algorithmicity of gradient-trained recurrent networks.
(1) Question: Can a naturally trained network move from sampled-perfect but provably wrong to sampled-perfect and unrestricted exactly certified, without adverse regularization?
(2) Frontier: Ryou et al., CAV 2021 RNN verification; Van Rossem and Saxe, ICML 2025 RNN algorithm acquisition; NOESIS Runs 270-274.
(3) Exact success: >=1 same-seed trajectory with earlier sampled-perfect and exact counterexample, later sampled-perfect and independently sound all-alphabet inductive certificate.
(4) Competing explanation: symbol-conditioned scalar architecture makes latch learning easy; parameter-sign changes are incidental.
(5) Cheapest falsification: new seeds 19500..19627, 256 seeded random length-20 words plus all 27 3-symbol prefixes padded with HOLD; BCE-only, Adam lr=0.03, float64, 500 epochs, no parameter-sign constraints; snapshots epochs 0,10,20,30,40,50,75,100,150,200,300,500. Certify sampled-perfect snapshots and search exact counterexamples in uncertified ones.
(6) Publishable: independent checker, strongest spoofs, prospective unseen-seed/task prediction, primary priority audit.
(7) Learning relevance: every checkpoint from gradient training; preserve negatives and inconclusive.
(8) Kill: three substantive nontransferable failures, or priority collision.
Backup kernels (inactive): parity-task transfer; natural curriculum intervention.
Definitions: h'=ReLU(a_x*h+b_x), logit=v*h+c, h0=0, x=0 HOLD,1 SET,2 RESET. Binary64 weights interpreted as exact rationals. Absence of a sufficient certificate is not evidence of failure. Never claim an unrestricted certificate from finite tests.
