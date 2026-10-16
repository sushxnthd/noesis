# THEORY ledger — Run 205

The frozen experiment tested two rational hidden-state intervals, one per parity state, on a scalar input-gated tanh RNN: h'=tanh(w_bit*h+b_bit), output logit v*h+c. Induction requires: h0 successors lie in the respective intervals; each interval maps into the parity-updated interval under BOTH bits; output logit has strict correct sign throughout each interval. These are sufficient for all-length streaming parity.

Primary Fraction/85-digit outward Decimal.exp and independent mpmath.iv/75-digit interval implementations agreed on 14 accepted checkpoints of 28. No positive candidate was rejected by either checker. There were 14 abstentions, NOT 14 proofs of incorrectness. Frozen endpoint checkpoint score: 6/8 accepted at epochs 400/800.

Adversarial in-class spoof: w0=1,w1=-1,b0=-1/10000,b1=1/10000,v=-1,c=0,h0=1/2. Define z=(-1)^parity*h. Then z'=tanh(z-(-1)^parity/10000)>=tanh(z-1/10000). Inductively z_t>=a_t where a0=1/2 and a'=tanh(a-1/10000). Independent interval checkers prove a803>0 and a804<0. Therefore ALL words through length 803 are correct, but 0^804 is wrong. The inductive-certificate synthesizer abstains on this same-architecture spoof. This negative control was developed after the primary frozen protocol; it is exploratory.

Smallest claim: the checker gives sound, model-specific all-length parity certificates for 14 gradient-trained scalar gated RNN checkpoints. No model-agnostic law, acquisition-time theorem, or novel invariant method established.
