"""Independent exact proof of separation below Run349 collision horizons."""
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction as Q
import sympy as S
from wordgen import generate
from verify_witness import weights,states

def prove_separator(epoch,L):
    words=generate(L)
    H=states(weights(epoch),words)
    Z=np.array([[float(z) for z in h] for h in H])
    sign=np.array([1 if w.count('1')%2 else -1 for w in words])
    scale=np.maximum(np.max(np.abs(Z),axis=0),1)
    X=np.column_stack((Z/scale,np.ones(len(words))))
    lp=linprog(np.zeros(4),A_ub=-sign[:,None]*X,b_ub=-np.ones(len(words)),
        bounds=[(None,None)]*4,method='highs')
    assert lp.success
    coeff=[S.Rational(*Q.from_float(float(v)).as_integer_ratio()) for v in lp.x[:3]/scale]
    bias=S.Rational(*Q.from_float(float(lp.x[3])).as_integer_ratio())
    margins=[sign[i]*(sum(coeff[j]*h[j] for j in range(3))+bias)
        for i,h in enumerate(H)]
    assert min(margins)>0
    print('EXACT SEPARATOR',epoch,'L',L,'words',len(words),'positive',True)
    return True
if __name__=='__main__':
    assert len(generate(17))==2326 and len(generate(22))==2586
    prove_separator(81,17)
    prove_separator(82,22)
