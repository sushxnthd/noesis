# Run 192: certified finite agreement, infinite unary disagreement

Two gradient-trained checkpoints from one seed-163 width-8 tanh RNN, Adam epochs 300 and 600, give identical parity classification on **all 8,190 nonempty binary prefixes of length <=12**. Exact interval enumeration: 0 disagreements; smallest certified absolute logit >1.706142320858205.

**Epoch 300:** every 0^k with k>=181 is wrong (Run191 two-cycle proof).
**Epoch 600:** every 0^k with k>=1 is correct (Run192 rational transformed contraction box). The epoch600 proof checks 80 direct prefixes, a radius-1e-8 invariant, transformed row norm <0.694995640 and output upper bound <-8.95933613.

Training BCE 0.05032711561123008 -> 0.04521537906826043. Token training accuracy unchanged 0.9869791666666666; length-12 sequence pass count unchanged 3120/4096; random length-128 sequences passing deteriorate 2/128 -> 0/128.

This is **post-hoc** and does not demonstrate acquisition of unrestricted parity: epoch600 still fails other strings. Finite-window indistinguishability and parity learning are established prior art. Local verification used two independent interval arithmetic implementations (mpmath.iv and directed Decimal); remote CI not yet established.

Input SHA256 for archived Run191 TRAINED.json: 592939a6f4da487eff78252c20141df9bccbcc3769324fe94d4ef3eeb71a60df.
