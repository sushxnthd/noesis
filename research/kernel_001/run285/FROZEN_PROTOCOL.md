# NOESIS K001 — Run 285 frozen protocol (2026-10-20)

One active kernel: K001. Input: unchanged Run283 gradient-trained width-two ReLU RESET/TOGGLE parity checkpoints and Run284 exact certificate outcomes. No retraining and no alteration of evaluation examples.

1. **Precise question:** Does excluding a finite initial transient from a task-conditioned inductive invariant strictly increase all-length correctness certification of genuinely gradient-trained width-two RNNs, without accepting known finite-horizon spoofs?
2. **Primary-literature frontier:** Neural network invariant verification and automata extraction already use inductive reachable-set abstractions; novelty is not presumed. Consult Run284 PRIORITY_AUDIT.md.
3. **Single exact success criterion:** At least **two additional** epoch160 sampled-perfect networks (beyond Run284's 20) receive exact, independently checked full-alphabet certificates, with **zero** known-failing Run283 checkpoints certified.
4. **Strongest competing explanation:** Two-box failure reflects crude axis-aligned overapproximation or numerical LP search, not missing algorithmicity; a finite-prefix exclusion could merely improve ordinary reachability analysis.
5. **Cheapest decisive falsification:** Freeze the 62 epoch160 sampled-perfect checkpoints and six known-failing earlier checkpoints; attempt depth-k (k=1,2,3,4) exact-prefix + two-box inductive certificates. Verify all candidates using a separate exact arithmetic implementation.
6. **Publishable threshold:** Improvement must be paired with prospective acquisition prediction on unseen training seeds/tasks and primary-literature priority audit; increased retrospective coverage alone is not publishable.
7. **Learning relevance threshold:** At least two newly certified models must be genuinely gradient-trained epoch160 checkpoints, with training provenance preserved.
8. **Kill condition:** If no additional certificates or any false certificate, reject this refinement as the next diagnostic; three failed strengthening attempts trigger reformulation of K001.

**Procedure:** For each k, enumerate all 2^k binary prefixes, compute exact rational hidden states and outputs on every prefix; require correct classification on all prefixes. Place their depth-k hidden states in parity-indexed axis-aligned rational boxes. Require exact full-alphabet closure and readout sign for both boxes. Use floating-point candidate discovery only; never use it to accept a proof. Independently recheck exact certificates with a second implementation. Preserve unsuccessful attempts and intermediate outputs. Do not treat lack of a certificate as proof of incorrectness.

**Data handling:** No access to the user's laptop, no paid compute. Preserve Run283 original checkpoint SHA256 and Run284 certificate set. THEORY and LEARNING ledgers separate. No claim of universal law.
