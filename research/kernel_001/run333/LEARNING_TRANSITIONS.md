# Run333 exact training-trajectory audit

Original float64 gradient-trained width-three ReLU OR-latch checkpoints, trained on length-six examples (Adam-like training setup inherited from Run326; no new training here). Exact rational evaluation of epoch-20 weights found a wrong classification for the one-symbol word "0" in all five subsequently certified seeds:

seed 24066: wrong logit +1.387485508117569
seed 24139: wrong logit +0.5677269184592508
seed 24152: wrong logit +0.775935966662782
seed 24202: wrong logit +0.24609280402599554
seed 24305: wrong logit +1.1660731002688294

At epoch 80, both exact checkers certify all-length correctness for each of the five unmodified trained networks. Thus these five trajectories change from provably incorrect at epoch 20 to provably correct for all finite binary input lengths by epoch 80, under exact-real inference semantics.

LIMITS: the early errors are on length-one input, not finite-perfect heuristics. The first correct epoch is unknown (only epochs 0, 20, 80 were saved). This is not a mechanism-derived prospective prediction, causal explanation, or architecture-independent acquisition law. Full original early checkpoint vectors and exact logit fractions are in the Run333 evidence archive.
