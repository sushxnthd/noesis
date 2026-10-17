# Run 223 — independent remote proof replay (pre-execution protocol)

Active kernel: Kernel 001, verified algorithm acquisition in gradient-trained RNNs.
Source: archived Run 222 checkpoint set (SHA256: 8babc30b30e533eb3747a2b3e9c691d54f0289e84d3a323e404fae8f0ec726f4). Run 222 is RETROSPECTIVE; no prospective acquisition claim is made here.

## Question
Can the six previously reported all-length, 0.03-Linf robust certificates be independently reproduced in GitHub-hosted CI with mutation tests, rather than only locally?

## Exact success criterion
6/6 original certificates accepted by an independently implemented interval checker AND at least two predefined corruptions rejected: (i) negated readout on seed 1301, (ii) collapse first box coordinate of lexicographically first box for seed 1301. Also reproduce four epoch-50 wrong-output witnesses.

## Competing explanation
Local certificates reflect a shared arithmetic/implementation defect or evidence-packaging mistake.

## Cheapest falsification
Run independent interval verifier on frozen JSON and run corruption controls on a clean GitHub runner.

## Publishable threshold
This proof replay is infrastructure validation, not a publication-worthy novelty claim. Novel prediction on unseen trained architecture still required.

## Learning relevance
Four incorrect-epoch50 to robustly-correct-epoch200 trajectories are present in archived gradient-trained checkpoints, pending remote proof reproduction.

## Kill condition
If any original proof fails under independent checker, withdraw corresponding robust claim and debug without replacing failed evidence. If three further transfer attempts fail, reformulate the active predictor kernel.

## Frontier
van Rossem and Saxe, ICML 2025, streaming parity algorithm development; Ryou et al., CAV 2021, RNN formal verification.

## Provenance
This protocol is committed before Run223 GitHub-hosted verification. Original Run222 certificate construction and epsilon selection were retrospective.
