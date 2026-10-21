# Kernel 001 / Run313: retrospective exact acquisition pair

This is a retrospective cross-archive audit. Seed 22242 was known from Runs 307 and 312. It is **not** a prospective experiment.

1. **Question:** Did one gradient-trained RNN change from an epoch-20 representation that loses the latch bit even with arbitrary deterministic length-aware readout, to an epoch-80 network correct on all finite binary strings?
2. **Primary-literature frontier:** Inductive RNN verification, polyhedral invariants, and automata extraction are established (Jacoby, Barrett & Katz, ATVA 2020; Weiss, Goldberg & Yahav, ICML 2018; Ryou et al., CAV 2021). No priority claim for these mathematical tools.
3. **Single exact criterion:** Verify both equal-length epoch-20 collision h(000000)=h(100000) with opposite target labels, and unrestricted epoch-80 correctness by an exact inductive invariant. Independent checker must agree.
4. **Competing explanation:** Only the output readout or its calibration changed. The early equal-length hidden-state collision excludes all deterministic final-state readouts, including nonlinear and length-aware ones.
5. **Cheapest falsification:** Exact binary64-rational simulation of early checkpoint; independent vertex/ray verification of late cone; eight mutated-model negative controls.
6. **Publishable threshold:** Prospective prediction on unseen trained networks, advantage over training loss, cross-task/architecture transfer, spoof controls, independent reproduction, and primary-priority audit. This audit alone does not meet it.
7. **Learning relevance:** Both checkpoints are unmodified members of the same gradient-training trajectory (seed 22242).
8. **Kill condition:** Any source mismatch, failed exact equality, failed invariant inequality, or failed independent checker invalidates this paired-transition claim.

One active kernel only: K001, sound learned-algorithm acquisition diagnostics. Backup kernels: none. THEORY and LEARNING are documented separately. No paid compute or user-laptop usage.
