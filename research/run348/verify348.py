#!/usr/bin/env python3
"""Independent exact Run348 endpoint and negative-control audit."""
import json,sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
import sympy as S
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run340'))
from cert340 import certificate,verify
rows={(r['seed'],r['epoch']):r for r in json.loads((P/'trajectories348.json').read_text())['rows']}
expected={32098:(0,),32135:(2,),32158:(2,),32187:(0,)}
for seed,E in expected.items():
 p=rows[(seed,200)]['p']
 assert certificate(p)==E and verify(p,E)
 print('CERTIFIED',seed,E)
W=sorted(set([format(i,f'0{n}b') for n in range(1,9) for i in range(2**n)]+['1'*k for k in range(9,17)]+['1'+'0'*a+'1'+'0'*b for a in range(15) for b in range(15-a)]+['1'+'0'*k for k in range(16)]+['111111111111','100000001','10000000000001']),key=lambda w:(len(w),w))
assert len(W)==618
for seed,epoch,failure in [(32135,81,'10100000000'),(32135,82,'10100000000000'),(32187,37,'111111111111')]:
 p=[Q.from_float(float(z)) for z in rows[(seed,epoch)]['p']]
 A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in range(2)]
 b=[p[18+3*x:21+3*x] for x in range(2)]
 cache={'':(Q(0),)*3}
 def h(w):
  if w not in cache:
   z=h(w[:-1]);x=int(w[-1])
   cache[w]=tuple(max(Q(0),sum((A[x][i][j]*z[j] for j in range(3)),b[x][i])) for i in range(3))
  return cache[w]
 def y(w):
  return sum((p[24+j]*h(w)[j] for j in range(3)),p[27])>0
 assert all(y(w)==bool(w.count('1')%2) for w in W if len(w)<=8)
 assert y(failure)!=bool(failure.count('1')%2)
 H=np.array([[float(z) for z in h(w)] for w in W])
 signs=np.array([1 if w.count('1')%2 else -1 for w in W])
 scale=np.maximum(np.max(np.abs(H),axis=0),1)
 V=np.column_stack((H/scale,np.ones(len(W))))
 r=linprog(np.zeros(4),A_ub=-signs[:,None]*V,b_ub=-np.ones(len(W)),bounds=[(None,None)]*4,method='highs')
 assert r.success
 co=[Q.from_float(float(z)) for z in r.x[:3]/scale];d=Q.from_float(float(r.x[3]))
 margins=[signs[i]*sum((co[j]*h(w)[j] for j in range(3)),d) for i,w in enumerate(W)]
 assert min(margins)>0
 for i,w in enumerate(W):
  z=S.Rational(d.numerator,d.denominator)+sum(S.Rational(co[j].numerator,co[j].denominator)*S.Rational(h(w)[j].numerator,h(w)[j].denominator) for j in range(3))
  assert (z>0)==bool(w.count('1')%2)
 print('EARLY',seed,epoch,'short=510','failure=',failure,'exact_affine_separator_618=PASS')
print('FROZEN CRITERION FAILED: zero exact convex obstructions in 3 eligible early checkpoints')
