# THEORY ledger — Run295
- Exact all-word functional equivalence: **proved** for both divergent and stable reachable-zero gates. The original 3 recurrent coordinates do not depend on appended coordinates; z2>=z1>=0 inductively; g'=relu(z1-z2-1)=0; readout of g is nonzero but g always zero.
- Backward structural output-ancestor pruning retains all 6 coordinates for both variants, across 242 gradient-trained checkpoints.
- Diagnostic changed for 191/242 divergent cases **and 49/242 stable cases**.
- Frozen primary criterion **FAILED** because stable control did not preserve 242/242 scores. This is a stronger attack on structural pruning, not confirmation of the frozen specific divergence mechanism.
- Width and box-LP constraints are plausible competing explanations; no model-agnostic law.
- Priority: inductive RNN verification and reachable-state abstractions are established (Jacoby et al ATVA 2020; Ryou et al CAV 2021; DeepAbstract 2020). Do not claim novelty for invariant reachability itself.
- Next: reachability-conditioned quotient/projection that is exact on the output-relevant reachable manifold, followed by genuinely new task/architecture prospective prediction.
