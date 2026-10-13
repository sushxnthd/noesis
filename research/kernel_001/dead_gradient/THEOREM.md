# Exact dead-gradient witness (restricted neural counter)
Model: n'=max(0,n+s), h'=ReLU(h+s)-ReLU(h+s-M)=min(M,max(0,h+s)), s in {+1,-1}, M>0 trainable.

**Theorem A.** For noninteger M in (m-1,m), m=ceil(M), the globally shortest zero-test failure is +^(m+1)-^m, length 2m+1, with true count 1 and neural state 0. Proof: h<=n always, so only false negatives are possible. To deplete the clipped hidden state while the symbolic counter stays positive requires at least m net decrements following clipping and at least m+1 increments overall. The witness attains this bound. Independent exact BFS verifies all 12 frozen cases.

**Theorem B.** On this witness, final squared count regression loss (h-n)^2=1 throughout M in (m-1,m), hence dL/dM=0 despite a wrong prediction. On the prefix +^(m+1), L=(M-m-1)^2, dL/dM=2(M-m-1). Starting at M=m-2/3, one GD step of size 1/4 gives M'=m+1/6, increasing shortest failure length from 2m+1 to 2m+3, without eliminating finite saturation.

**Control.** The balanced high-depth word +^(m+1)-^(m+1) touches saturation but has final loss and gradient 0.

**Limits.** Count regression training, zero-test evaluation; ideal-real arithmetic; fixed identity recurrence and saturation form; no spontaneous algorithm acquisition or novelty claim.
