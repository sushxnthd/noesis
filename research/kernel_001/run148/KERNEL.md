# NOESIS Kernel 001 — Run 148 (one active kernel)
1. **Question:** Can an all-plus inductive two-dimensional cone certificate for a genuinely gradient-trained 4-state ReLU counter predict *complete-alphabet* generalization?
2. **Primary frontier:** El-Naggar et al., ICGI 2023, https://proceedings.mlr.press/v217/el-naggar23a.html (exact single-cell ReLU counting conditions); El-Naggar et al., EACL SRW 2023, https://aclanthology.org/2023.eacl-srw.15/ (training failure). Reachability and outward interval arithmetic are established methods.
3. **Exact criterion:** Find and independently verify a mixed ternary word with error >0.1 before the Run147 all-plus failure at 125, and certify all shorter ternary words correct to tolerance. **Met: globally first at 13.**
4. **Competing explanation:** A plus-only cone is a true but task-incomplete invariant; neutral inputs enter a different ReLU region and accumulate output drift.
5. **Cheapest falsification:** Enumerate all 3^n ternary words with outward interval bounds to n=13; independently check the two violating words using exact rational arithmetic.
6. **Publishable threshold:** Prospectively frozen, architecture-spanning, task-coupled invariant predicting first failure and training transitions beyond baseline; not met.
7. **Learning threshold:** Unmodified output-trained 4-state model from Run147; all 3^6 supervised training words; seed 214 is learned, not a handcrafted automaton. Met narrowly, retrospectively selected.
8. **Kill condition:** Kill plus-only cone as a sufficient complete-task certificate on any earlier mixed failure. **Triggered.** Retain only task-coupled all-alphabet reachable-set obligations. If three successive such attempts fail to yield incremental prediction, reformulate kernel.

Backups (inactive, max two): neutral drift pre-screen; architecture-independent adversarial reachable-set partitioning.
