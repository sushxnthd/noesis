# THEORY ledger — Kernel 001
**KNOWN (exact):** T_x(h)=max(0,h+x) and S_{M,x}(h)=ReLU(h+x)-ReLU(h+x-M), x∈{-1,+1}, h0=0. For integer M>=1 they agree on *every* word of length <=M. Globally shortest count-value failure is '+' repeated M+1 (output M vs M+1).

**KNOWN (task-relevant strengthened theorem):** With zero-test decoder h==0, globally shortest failure length is **2M+1**, witnessed by '+'^(M+1) followed by '-'^(M). Independently enumerated product-state BFS for M=1..12. Proof in ZERO_TEST_THEOREM.md.

**KNOWN (local finite-jet invisibility):** For any finite observed word set of max length H, and p near 1, choose M>H(1+epsilon). The capped and uncapped networks agree on an open neighborhood of p. All existing derivatives of any order with respect to shared parameters are equal there. Gradient wrt cap is identically zero. Does not cover regularizers or all optimization schemes.

**FALSIFIED as sufficient:** Finite-horizon transition closure/composition and on-support gradients cannot certify unbounded counting or zero-testing even in a two-ReLU neural recurrent cell.

**UNTESTED:** Task-relevant inductive simulation relations with unbounded distinguishing suffixes in *trained* networks.

**CAVEAT:** This is a deliberately engineered spoof, not evidence that unconstrained RNNs spontaneously learn saturation. Elementary construction, novelty unestablished.

**Run 145 — exact trained-model negative:** On ordinary-gradient-trained seed 205 (3-state ReLU), exact rational ||A^32||_infinity=0.9874237072485514<1 certifies rho(raw A)<1. On repeated increments, h3 stays zero and active 2x2 B has a strictly positive expanding cone v=(1,37121/50000). Hence output grows exponentially and counting error is unbounded. First |error|>0.1 on repeated increments occurs at n=141. This falsifies raw-matrix spectral-radius-only stability/algorithmicity screening. Not a new nonlinear stability theorem. Source: run145/certificate.py and independent_check.py.
