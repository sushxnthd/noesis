# THEORY ledger — Kernel 001
**KNOWN (exact):** T_x(h)=max(0,h+x) and S_{M,x}(h)=ReLU(h+x)-ReLU(h+x-M), x∈{-1,+1}, h0=0. For integer M>=1 they agree on *every* word of length <=M. Globally shortest failing word is '+' repeated M+1 (output M vs M+1). Proof: at time t<=M, reference h<=t and cap is inactive; '+'^(M+1) first reaches a state above M.

**KNOWN (local finite-jet invisibility):** For any finite observed word set of max length H, and p near 1, choose M>H(1+epsilon). The capped and uncapped networks agree on an open neighborhood of p. All existing derivatives of any order with respect to shared parameters are equal there. Gradient wrt cap is identically zero. Does not cover regularizers or all optimization schemes.

**FALSIFIED as sufficient:** Finite-horizon transition closure/composition and on-support gradients cannot certify unbounded counting even in a two-ReLU neural recurrent cell.

**UNTESTED:** Task-relevant inductive simulation relations with unbounded distinguishing suffixes in *trained* networks.

**CAVEAT:** This is a deliberately engineered spoof, not evidence that unconstrained RNNs spontaneously learn saturation. Elementary construction, novelty unestablished.
