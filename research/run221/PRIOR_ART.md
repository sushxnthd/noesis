# Priority and scope audit (17 October 2026)

The neural-learning premise is not novel by itself: van Rossem and Saxe, *Algorithm Development in Neural Networks: Insights from the Streaming Parity Task* (2025), https://arxiv.org/abs/2507.09897, directly studies learned infinite-generalization transitions and representational merging on streaming parity. Our finite-prefix certificates and transition observations must be compared against this paper before any novelty claim.

Ryou et al., *Scalable Polyhedral Verification of Recurrent Neural Networks*, CAV 2021, https://www.sri.inf.ethz.ch/publications/ryou2021scalable, establishes RNN verification and abstraction refinement. Bollig et al., *Analysis of recurrent neural networks via property-directed verification of surrogate models* (2022), https://doi.org/10.1007/s10009-022-00684-w, studies RNN counterexample discovery using property-directed automata.

**Smallest claim in Run221:** nonnested beam-width selection on one previously trained 3D RNN can miss a rigorously certified, globally shortest wrong input even when a narrower beam finds it. This is a reproducible evaluation pathology, not a new universal theorem.
