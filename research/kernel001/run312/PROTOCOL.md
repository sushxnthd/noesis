# NOESIS K001 Run312 — sound endpoint resolution

**Retrospective disclosure:** A longer protocol-write attempt was blocked before the experiment. The exact seed-22242 cone was subsequently discovered locally. This file is committed **after** discovery; do not call the result prospectively frozen.

1. Question: can a sound, exactly checked invariant classify an unresolved gradient-trained latch checkpoint?
2. Frontier: inductive RNN verification and automata extraction already exist (Jacoby et al., ATVA 2020; Weiss et al., ICML 2018; Ryou et al., CAV 2021).
3. Exact success: at least one of four previously unresolved seeds (22242, 22287, 22361, 22573) is classified by an exact all-length certificate or exact wrong-output word.
4. Strongest alternative: bounded perfection and collision disappearance are not sufficient for arbitrary-length correctness.
5. Cheapest falsification: check entry, zero-only behavior, closure, and output margins with exact binary64 rational arithmetic.
6. Publishable threshold: unseen-model predictions beyond training loss plus independent checking, adversarial spoofs, and priority audit.
7. Learning relevance: the certificate applies to an unmodified, genuinely gradient-trained epoch-80 ReLU RNN.
8. Kill: if no new sound endpoint after three attempts, reformulate.

Prior evidence: Run311 tested 28,488 bounded examples without finding errors in the four models. No additional training, API spend, or user-device computation. Preserve all negative results.
