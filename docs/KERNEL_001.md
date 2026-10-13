# Kernel 001 — Transition-closure certificates

## Research question

Can a transition-closure / composition-consistency diagnostic distinguish a learned reusable algorithm from a finite-range heuristic that only agrees on the tested horizon?

## Strongest alternative explanation

Any finite evaluation can be spoofed by a bounded-state transducer that reproduces the target algorithm on every tested state/trajectory and diverges just outside the observed horizon. Therefore finite-horizon closure alone cannot certify unbounded algorithm acquisition.

## First decisive falsification

Before training any neural model, construct the smallest exact spoof family for counter-style transitions. For every finite tested horizon H, build a deterministic bounded transducer that:

- agrees exactly with an unbounded increment algorithm on every tested state 0..H;
- satisfies every transition/composition query whose intermediate states remain inside the tested horizon;
- diverges immediately at H+1 by saturating or cycling.

If this construction succeeds for arbitrary H, any candidate NOESIS certificate must include evidence that cannot be reduced to finite observed transition agreement alone (for example intervention structure, state-representation constraints, extrapolative algebraic invariants, or a causal training-transition prediction).

## State

- **KNOWN:** finite observed behavior is not by itself proof of unbounded generalization.
- **BELIEVED:** naive finite-horizon transition-closure tests are spoofable by bounded transducers.
- **UNTESTED:** whether a stronger representation-level certificate plus adversarial interventions can reject such spoofs in trained neural systems.

## Success criterion

The first kernel step passes if an exact implementation constructs and verifies a spoof for every H in a preregistered finite sweep and an independent checker reproduces the result.

## Kill / reformulation condition

If the naive certificate is spoofed, do not continue optimizing it. Reformulate the active kernel around the weakest additional condition that provably excludes the spoof family while remaining measurable in trained models.

## Claim boundary

This initial result is a baseline impossibility/design constraint, not a novelty claim. Historical novelty requires a primary-literature audit before any theorem-level positioning.
