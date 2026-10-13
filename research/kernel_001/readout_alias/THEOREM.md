# Kernel 001 — exact readout-aliasing counterexample

**Model:** u'=ReLU(u+s), v'=ReLU(v+s)-ReLU(v+s-M), s in {-1,+1}, u=v=0 initially, integer M>=1. A two-parameter linear readout y=a*u+b*v is gradient-trained on reflected-counter values.

**Theorem:** On every input word of length <=H<=M, u=v=n. Thus squared-error loss is Q(a+b-1)^2, and full-batch gradient descent with equal learning rates preserves b-a. An exact unbounded counter exists in the hidden state but training cannot distinguish it from the finite-cap decoy.

For M=8, H=5, exhaustive 63-word training gives Q=61/21 and eta=21/244. One exact GD step sends (-1/4,3/4) to (0,1) and (3/4,-1/4) to (1,0). Both have identical initial loss 61/84, gradient (-61/21,-61/21), and final training loss zero. The first output is a finite heuristic, the second correct at all lengths.

**Shortest counterexamples:** For y=v, first integer-count failure is +^(M+1), length M+1. First zero-test failure is +^(M+1)-^M, length 2M+1. A discrepancy requires exceeding cap M and then at least M decrements to return v to zero while u>0. Independent exhaustive word search checked M=1..6 (21,834 words); separate exact product-state BFS checked M=1..12.

**Necessary output coupling in this class:** If a+b=1, all-length exact count correctness iff b=0. A finite-horizon latent simulation and local output checks are insufficient.

**Wildcard:** Minimum-norm interpolator a=b=1/2 miscounts at M+1 but is all-length correct for zero-testing, because 0<=v<=u.

**Limits:** Hidden transitions are fixed and already implement u=n. Only the readout is learned. This is a restricted diagnostic spoof, not spontaneous learned algorithm acquisition or a novelty claim.
