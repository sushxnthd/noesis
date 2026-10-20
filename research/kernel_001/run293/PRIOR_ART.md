# Run293 primary-literature collision audit
Phuong & Lampert, ICLR 2020, Functional vs. Parametric Equivalence of ReLU Networks: positive scaling and permutation symmetry are established (https://research-explorer.ista.ac.at/record/7481).
Kumar, Serra & Ramalingam, 2019, Equivalent and Approximate Transformations of Deep Neural Networks: changing neuron count while preserving network function is prior art (https://arxiv.org/abs/1905.11428).
Abstraction and Refinement: Towards Scalable and Exact Verification of Neural Networks, ACM TOSEM 2024: merge and refinement techniques are established (https://doi.org/10.1145/3644387).
Internal NOESIS Run231 already examined signed relational quotients in trained tanh RNNs (draft PR #2).
Decision: exact proportional-neuron quotient is a known-style representational repair. The only supported new empirical claim is recovery of the particular Run291 predictor under Run292-style attacks on previously trained models.
