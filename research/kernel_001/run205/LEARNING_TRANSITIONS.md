# Certified learning transitions (post-hoc witnesses; independent proof)
| Seed | Incorrect checkpoint | Short wrong word | Certified wrong logit sign | Later all-length certified checkpoint |
|---|---:|---|---|---:|
| 223 | 0 | 0 | +0.11321596523135895 (even expected) | 20 |
| 227 | 50 | 11 | +0.14591866691287902 (even expected) | 100 |
| 229 | 50 | 10 | -0.421356061966064 (odd expected) | 100 |

Both Fraction/Decimal directed intervals and independent mpmath.iv intervals prove each early classification error. Later all-length proofs were prospectively specified by the frozen Run205 protocol. Therefore three distinct gradient-training trajectories changed from **provably incorrect** to **provably correct at all nonempty input lengths** between sampled checkpoints. This does NOT identify the exact acquisition epoch, establish a model-agnostic law, or prove a causal mechanism. The early witnesses were selected retrospectively after the primary frozen evaluation.
