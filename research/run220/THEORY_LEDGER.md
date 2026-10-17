# THEORY ledger — Run220
KNOWN (local, independently checked): For six frozen 3D tanh checkpoints at epoch200 and one at epoch50, a finite partition indexed by parity and recent symbols forms a sound interval inductive invariant. Base inclusion, output separation and all three successor closures were verified by mpmath.iv and independently by directed Decimal at high precision. The guarantee is exact-real evaluation of exact binary64 parameters, all finite input lengths, all prefixes.

KNOWN: A strict interval wrong-sign witness disproves all-length correctness; 18 early and one late were checked.

LIMIT: An invariant-search failure is an abstention, not a behavioral failure. These certificates are architecture-specific proofs, not a model-agnostic law.

PRIOR ART: Jacoby, Barrett & Katz (ATVA 2020) already establish invariant-inference verification for RNNs; Weiss, Goldberg & Yahav (ICML 2018) establish automata extraction with queries and counterexamples. No novel universal theorem claimed.
