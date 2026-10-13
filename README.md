# NOESIS

NOESIS is a Kernellum machine-reasoning research program studying when gradient-trained neural systems acquire reusable algorithms rather than finite-range heuristics.

The repository is research-first. Claims are tracked as **KNOWN / BELIEVED / CONFLICTING / FALSIFIED / ANOMALOUS / UNTESTED**, with negative results preserved.

## Current breakthrough kernel

**Question:** Can transition-closure / composition consistency of a learned latent state serve as a task-agnostic certificate of reusable algorithm acquisition on unbounded-state tasks, while rejecting adversarial finite heuristics that extrapolate over long but bounded ranges?

The active program will prioritize exact enumeration and minimized spoofing counterexamples before scaling to trained-model studies.

## Research workflow

1. Define one falsifiable kernel.
2. Search the smallest finite domains exactly when possible.
3. Construct adversarial heuristics designed to spoof candidate certificates.
4. Preserve counterexamples and failed hypotheses.
5. Derive a new prediction from any surviving mechanism.
6. Test that prediction on an unseen task family or training regime.
7. Audit primary prior art before any novelty claim.

Substantive experiments live on isolated `research/*` branches until their evidence and claim boundaries are clear.
