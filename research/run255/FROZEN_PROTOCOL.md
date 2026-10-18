# NOESIS Run255: frozen prospective transfer
Date: 2026-10-19. Active kernel 001.
Question: Does exact q-by-ReLU-mask rational polyhedral certification transfer to previously unseen gradient-trained networks on both reset-parity and reset-latch?
Frontier: inductive neural verification and trained RNN algorithm acquisition already established; do not claim method novelty without priority audit.
Primary scalar: at least two all-length exact certificates, one per task, and zero false certificates.
Competing explanation: Run254 was a retrospectively favorable seed.
Training: 8 parity seeds 14001..14008 and 8 latch seeds 15001..15008, 4-dimensional tied-transition ReLU, length-five full ternary training, 201 epochs (0..200), float64, Adam learning rate 0.03, BCE, deterministic CPU, checkpoints at 0/50/100/200.
Testing: evaluate all 16 without selecting favorable seeds. Exhaustive words through length seven; longer deterministic adversarial holds and periodic sequences through length 512. Negative search does not imply correctness.
Certification: fixed q x activation-mask disjunctive rational-polyhedral inductive invariant, exact dual checks for all input/mask cases and outputs; at most 120 seconds synthesis per model. Do not modify checkpoint parameters. Reject every candidate without an independent exact checker.
Publishable: two tasks, exact proof, spoof controls, prospective acquisition evidence, independent reproduction and novelty audit.
Learning relevance: at least two independently trained trajectories with exact incorrect earlier checkpoints and certified later checkpoint.
Kill: three failed transfer attempts retire/reformulate this template. Attempt 1/3.
Backup kernels: none. Keep negative results, raw checkpoints, failed infrastructure and smallest supported claims.
