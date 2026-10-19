# THEORY ledger — Run274
Exact dyadic scalar recurrence h'=ReLU(a_x h+b_x), output sign(v*h+c), initial h=0, symbols HOLD=0, SET=1, RESET=2.
Positive proof: low [0,L], high [U,infinity), L=max(0,b_RESET), U=b_SET. Require output separation vL+c<0<vU+c, nonnegative HOLD slope preserving both regions, nonnegative SET slope and SET intercept >=U, nonpositive RESET slope and RESET intercept <=L. Every input symbol maps both symbolic regions to the correct successor region; induction yields all-length correctness.
Negative proof: HOLD a0>1, fixed point F=-b0/(a0-1)>=0, SET hS=max(0,b1)>F, RESET a2>0, v>0, c<0. h_n=F+a0^n(hS-F) strictly increases. Exact positive RESET output at N proves failure for all n>=N. Check N-1 to establish first failure within this specific word family.
This is a restricted architecture-specific sufficient theorem, not a model-agnostic characterization.
