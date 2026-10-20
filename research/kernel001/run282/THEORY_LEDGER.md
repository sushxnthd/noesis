# THEORY — Kernel 001 / Run 282

**Exact sufficient simulation:** h_even=0 and h_odd=b1>0 under h'=ReLU(a_x h+b_x). The six dyadic parameters satisfy b0<=0, a0*b1+b0<=0, (a1+1)*b1<=0, c<0 and v*b1+c>0. These conditions imply every possible RESET/TOGGLE transition preserves the correct symbolic state. All-length correctness follows by induction; the independent checker enumerates the full two-state transition table using Fraction.

**Exact spoof family:** For -1<a1<0 and b1>0, pure-TOGGLE hidden states satisfy h_n=b1(1-a1^n)/(1-a1), strictly positive. Even n approach h*=b1/(1-a1) from below; odd n from above. If v>0 and threshold t=-c/v differs from h*, one parity must eventually be misclassified, and every later n of that parity also fails. The earliest observed family witnesses for five sampled-perfect trained checkpoints have lengths 14,17,9,36,244.

**Limits:** The certificate is a sufficient two-point representation-specific property of a scalar symbol-conditioned ReLU RNN. It is neither necessary for all correct RNNs nor model-agnostic. Exact-real weights interpreted from stored binary64, not a hardware-rounding guarantee. No general novelty or law claim.
