# NOESIS Run 188 — adversarial reachable-state falsification (frozen search specification)

Status: protocol fixed before running the new search. This is an adaptive adversarial falsification, **not** a prospectively held-out estimate of generalization performance.

Source artifact: Run 187 TRAINED.json (SHA256 c5eddbd14ffa77d73feb94da553863b62a402b8c7755914490ba7c2bd37c1508). Target checkpoints: independently trained width-8 tanh RNNs, seeds 101 and 107, epoch 600. Frozen training dataset: all length-6 binary words, token-level parity.

**Exact success criterion:** one explicit binary input on which either checkpoint makes a wrong token-prefix parity prediction, verified by an independent PyTorch implementation using unchanged checkpoint parameters. Search length <=512. A counterexample is a decisive falsification of all-length correctness for that trained checkpoint, not a failure of training-transition evidence.

**Search:** first exhaustive binary prefixes through length 16; then a deterministic parity-stratified beam search, beam width 512 per parity, retaining 50% lowest signed-output-margin states, 25% states farthest in normalized hidden-state Euclidean distance from retained states (diversity), and 25% deterministic pseudo-random reservoir states, RNG seed 188. Expand each retained prefix by 0 and 1, to depth 512. Stop at first verified failure. Record every prefix's actual margin, witness, and checkpoints. This search is adaptive and does not provide a statistical rate estimate.

**Strongest competing explanation:** a finite-range parity heuristic with a very large failure length; successful random tests through 4096 do not refute this. A beam miss cannot establish all-length correctness.

**Independent check:** a separate PyTorch forward pass over the complete discovered word; compare each prefix against parity; fail the run if it does not reproduce the first incorrect prefix.

**Publishable threshold:** new reproducible failure mode on independently trained models with prior-art audit and an evaluation recommendation; a single adversarial witness is not a field-level breakthrough.

**Learning relevance threshold:** counterexample must be for an unchanged gradient-trained checkpoint, with training procedure and source checkpoint hash; otherwise classify as purely symbolic.

**Kill condition:** no adversarial witness and no improvement over existing certificate at 3 substantive attempts; pivot to reachability-based invariant synthesis, not more blind horizon scaling.

**Wildcard budget:** none in this run, as this is a targeted falsification.

**Claim boundary:** absence of failure under finite search cannot certify unbounded parity; proof requires an inductive invariant and independently sound arithmetic.
