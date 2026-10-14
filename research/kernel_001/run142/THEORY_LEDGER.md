# THEORY — Run 142

For a 3-state ReLU RNN h'=ReLU(Ah+E_t), suppose a coordinate j has b=E_plus[j]>0, A[j,j]=1, E_minus[j]=-b, and A[i,j], E_plus[i], E_minus[i] <= 0 for i!=j. Induction proves h=b*q*e_j for every binary word, where q is the reflected count. The original readout y=w_j*b*q requires gain correction by 1/(w_j*b) for exact task output unless gain is already 1.

With neutral embedding c=E_neutral[j] nonzero and off-ray neutral inputs nonpositive, the calibrated error on neutral^n (c>0) is n*c/b; on plus neutral^n (c<0) it is min(1,n*|c|/b). First n with error >0.1 in these families is floor(b/(10*|c|))+1. No claim of globally shortest ternary failure.

Classical isolated-coordinate invariant; see El-Naggar et al., ICGI 2023. This is not a new theorem or a model-agnostic certificate. Exact rational semantics of stored binary floats, not finite-precision rollout.
