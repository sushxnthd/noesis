# Run 307 — frozen exact evaluation

Question: Does a gradient-trained epoch-20 RNN exhibit an exact opposite-label collision between binary words of equal length <=8, while the same seed's epoch-80 network has an independently verified unrestricted-correctness certificate?

Inputs: all 384 seeds 22200..22583 from Run300, epochs 20/80, unmodified checkpoints. Enumerate all binary words of lengths 1..8, exact rational ReLU state evaluation. Independent checker required.

Primary success: at least one exact equal-length collision in an epoch-20 network with certified-correct epoch-80 counterpart. Strongest competitor: length-aware decoding rescues unequal-length Run306 collisions. Cheapest falsification: exact exhaustive enumeration. Publishable: 10 independent transitions plus prospective predictive improvement over loss. Learning relevance: same trained trajectory. Kill: no such witness in this frozen window; do not extrapolate absence to correctness.

Theory and learning ledgers must remain separate. Preserve all outcomes and failures. Prior art: Weiss et al. ICML 2018; Jacoby et al. ATVA 2020; Ryou et al. CAV 2021. No novelty claimed for the elementary collision lemma.
