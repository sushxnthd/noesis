# One active kernel after Run204
1. Question: Can an automatically extracted reachable hidden-state relation R(h,q), inductively closed under both binary inputs and output-separating, certify all-length CountMod3 correctness of a gradient-trained RNN while rejecting finite-cap spoofs?
2. Literature frontier: Weiss et al. ICML 2018 automata extraction; Jacoby et al. ATVA 2020 neural invariants; Ryou et al. CAV 2021 RNN verification; van Rossem and Saxe ICML 2025 algorithm acquisition. No novelty asserted for these techniques.
3. Scalar success: >=1 independently checked full-alphabet all-length positive certificate on an unseen trained checkpoint; zero finite-cap spoof false accepts.
4. Competing explanation: task automaton hardcoded into the verifier or hidden cap escapes region closure.
5. Cheapest falsification: both-symbol inductive closure and output separation on held-out checkpoint and adversarial finite-cap controls; any unsound acceptance kills the candidate.
6. Publishable threshold: prospective unseen architecture/task, independent proof, spoof rejection, mechanism-derived prediction, priority audit.
7. Learning relevance: certification predicts or tracks a real gradient-training generalization transition, not finite accuracy alone.
8. Kill: any unsound acceptance or three failed distinct proof attempts without improvement requires reformulation.
Backups inactive: architecture-independent invariant extraction; causal state intervention.
