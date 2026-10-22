# Run 343 — a trained parity RNN that passes 8,190 inputs and fails infinitely often

## Decisive exact result
From the 88 original Run342 width-four gradient-trained parity RNNs classified correct on every nonempty binary word of length <=12, an exhaustive search at lengths 13..16 found **one** failure: seed 31089, epoch 200, word `1000000000000`. Expected parity 1; exact-real output logit is -1610.55188505182399... (negative). The other 87 models had no observed failure through length 16; **not** certified unrestricted-correct.

Independent exact Fraction arithmetic verified all 8190 words through length 12 for this checkpoint, and SymPy separately confirmed the length-13 error. Thus the length-13 witness is deletion-minimal.

## Infinite family proof (post-hoc mechanism, exact arithmetic)
For the original trained ReLU recurrence, after processing `1` followed by 15 zeros (length 16), the state enters the cone
`K={h0>=4, h1>=10*h0, h2=h3=0}`.
Exact rational inequalities prove zero-input transition invariance of K and strictly negative output throughout K. Exact direct evaluation confirms negative outputs at lengths 13,14,15. Therefore every word `1` followed by k zeros with integer k>=12 is incorrectly classified, although the network is correct on every word through length 12.

The proof code checks the cone using exact original float64 dyadic coefficients; it is not a floating-point simulation claim. A separate SymPy checker agreed locally. The public CI verifier uses independent Fraction and high-precision Decimal calculations.

## Frozen test and provenance
- Protocol branch commit: `2507b1bd7a9f88c81f44a4afdec03743376695f5` created before the length-13..16 search.
- Frozen criterion: >=1 exactly verified longer failure among the 88 length-12-perfect networks.
- Search: 10,813,440 new model-word pairs across lengths 13..16; one network with a failure.
- Model weights: `model343.json`, copied unchanged from Run342 archived `trajectories342.json` seed 31089 epoch 200.
- Scripts: `search343.py` reproduces the frozen cohort search given Run342 archive; `verify_witness.py` verifies exact finite correctness, independent longer failure, and infinite-family induction without the archive.
- One local infrastructure failure: initial optional SymPy verifier used an unavailable `Rational.from_float`; corrected to `Rational(*x.as_integer_ratio())` and rerun successfully. This is a checker API error, not an invalid proof.
- Complete original 128-network training trajectories remain in the Run342 research archive and workflow artifact, not permanently mirrored to this branch.

## Smallest supported claim
A **gradient-trained** width-four ReLU parity network can correctly classify all 8,190 nonempty binary inputs through length 12 yet fail on an infinite, explicitly characterized family beginning at length 13. Consequently, a length-12-perfect label is not a sound algorithmicity certificate for this cohort. This does not establish a universal acquisition law or show that the other 87 models are algorithmic.

## Kernel 001-S status
1. Question: Can inductive learned-state invariants distinguish reusable computation from bounded heuristics in gradient-trained RNNs?
2. Frontier: RNN invariant verification and automata extraction already exist (Jacoby et al. 2020; Weiss et al. 2018).
3. Run343 scalar: >=1 exact longer failure after 12-perfect (PASSED: 1/88).
4. Competing explanation: the prior independent endpoint only measured a longer but still finite heuristic range.
5. Cheapest falsification: exact exhaustive length13..16 plus independent proof.
6. Publishable threshold: priority audit, distinct mechanistic novelty, unseen architectures/tasks, external replication.
7. Learning threshold: original trained weights, not a hand-coded spoof (MET).
8. Kill: reject this spoof claim if exact checker disagrees; three substantive failures trigger active kernel reformulation.

No backup kernel active. This is a stronger **negative evaluation-practice result**, not a breakthrough certificate.
