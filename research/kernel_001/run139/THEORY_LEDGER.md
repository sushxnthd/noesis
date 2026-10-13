# THEORY ledger — Run 139

For ReLU h'=ReLU(Ah+E[+]), h0=0, y=w^T h, suppose some j has A[j,j]=1, b=E[+,j]>0 and E[+,k]<=0, A[k,j]<=0 for all k!=j. By induction h(+^n)=nb e_j for every n>=0, hence y(+^n)=ng with g=w[j]b. For strict tolerance epsilon>0 and g!=1, the exact first failure is floor(epsilon/abs(g-1))+1. All arithmetic here is mathematical real arithmetic using stored binary floats as exact rationals.

Eight gradient-trained checkpoints meet the recurrent ray assumptions but none has g=1 exactly. Thus exact internal mode is insufficient for exact task-level counting. The result is elementary and plus-only, not an all-word model-agnostic certificate.
