# THEORY ledger — Run252
Question: Does a previously unwitnessed gradient-trained ReLU checkpoint implement the all-length reset-parity algorithm?
Result: No proof of correctness or incorrectness. 25,322 distinct deterministic probes and an exploratory 89,976-node beam search found no counterexample on local checkpoint; same results on independent public Run251 checkpoint. This is bounded evidence only.
Finite-horizon consistency remains falsified as a sufficient all-length certificate. No new law is claimed.
Priority: Van Rossem and Saxe (ICML 2025) established parity algorithm acquisition and representation mergers; Dankowiakowski and Ronca (NeurIPS 2025) developed metric automata theory for RNNs; RNN reachability and abstraction refinement are established. New contribution must be proof-carrying evidence on gradient-trained systems, not abstract automata theory.
Decision: retire activation-switching-frequency as the primary diagnostic. It failed against strong nonadaptive baselines; further post-hoc optimization has low information gain.
