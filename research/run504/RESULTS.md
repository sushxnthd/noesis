# NOESIS R504: nonexpansive recurrent-state metric rigidity and learned-embedding feasibility

**Frozen before unseen outcomes:** protocol SHA256 `b0a963ba9ce257b4fc90cfd33e1d5c0e5f9e0d86109e38ead8c2d390f7d24f67`; primary source `289d2d7e391d6adbbe32a47199e8d6137c10433ea996a36a2eb2c52a43adf471`; independent source `1cc15f32fbcbcfb6d03b22d55108720154542d3ccabff28bad94aeb515a25f66`.

## Exact conditional result
For TaskC generators 0:(0 1), 1:(1 2), exact implementation on three distinct hidden representatives by two **nonexpansive** recurrent symbol maps forces all three pairwise distances to be equal. Proof: symbol 0 swaps distances d02 and d12; symbol 1 swaps d01 and d02; nonexpansiveness in both directions forces equality. Hence 1D exact distinct-state realization is impossible, while 2D equilateral representatives with two orthogonal Householder reflections realize both generators exactly.

For the fixed skew embedding x0=(0,0), x1=(1,0), x2=(2,1), the joint minimum Lipschitz constant for exact symbol transitions is sqrt(5) (pairwise lower bound and Euclidean Lipschitz extension). Symbol-wise minima are sqrt(5/2), sqrt(5). If both maps are 1-Lipschitz, max representative one-step error is at least (sqrt(5)-1)/2 = 0.61803398875. This is **classical finite-metric geometry conditional on an exact state embedding**, not a new general theorem or a no-go for unconstrained neural models. Equilateral nonlinear/orthogonal escape is explicit.

## New pre-frozen learned neural pilot
Eight new seeds 50401–50408; learned three 2D embeddings and two input-conditioned orthogonal Householder reflections, 800 Adam steps at lr=.05, direct supervision on all six naturally reachable DFA state-symbol transitions. All 8/8 passed frozen gates: max one-step error <=.02, edge CV <=.03, >=99% accuracy on all binary physical words length 0..10, and 100% on natural N/C/S cycles. Observed max one-step error range 1.11e-16..3.61e-16; edge CV <=1.44e-16; all physical word and cycle accuracy 100%. This is **direct state-supervised feasibility with a strong reflection/group-action inductive bias**, NOT learned hidden-state mediation, autonomous automaton discovery, or prospective external/architecture replication. No 32-seed confirmation.

## Independent checks and preservation
Independent pre-outcome NumPy checker reproduced 32,800 physical predictions, zero oracle/scan/classification errors. Separately frozen postprimary symbolic checker verified 6,141 exact word/state cases and exact equilateral construction, zero errors. Two isolated full deterministic replays each matched all 25 scientific hashes (8 checkpoints, 8 raw prediction files, 8 logs, primary results). All negative limitations and prior art (including Howe 2026 Householder recurrence, Metric Automata Theory 2025, Geiger 2025, Buitrago/Gu 2025) recorded.

**Complete SHA256-verified local archive:** `NOESIS_R504_Reproducibility.zip` SHA256 `bca10b76a52c202820b8d88e78c92f462d62c5324db0112db52a976e7c606b88`; 49 verified local payloads, nested immutable R503 archive, ZIP CRC pass. Zero spend, no user's laptop.

**Next:** retire R504 direct-state-supervised Householder/equilateralization and all eight checkpoints. Seek genuinely distinct learned on-support causal transition test with frozen non-ceiling functional intervention, locality and matched sham/no-cycle/lexical/q-changing controls; exact permutation scan alternative. No off-support hidden-do or path mediation claims. Confirm >=32 new seeds only after disjoint frozen feasibility pilot passes. No routine notifications.
