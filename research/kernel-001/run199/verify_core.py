import json
from pathlib import Path
from mpmath import iv
iv.dps=60
D=Path(__file__).parent
def q(x):
 n,d=float(x).as_integer_ratio()
 return iv.mpf(n)/iv.mpf(d)
def verify(row,word):
 p=row['params']
 W=[[q(x) for x in r] for r in p['W']]
 U=[[q(x) for x in r] for r in p['U']]
 V=[[q(x) for x in r] for r in p['V']]
 b=list(map(q,p['b'])); c=list(map(q,p['c']))
 h=[iv.mpf(0)]*12
 for bit in word:
  h=[2/(1+iv.exp(-2*(b[i]+U[int(bit)][i]+sum(W[i][j]*h[j] for j in range(12)))))-1 for i in range(12)]
 z=[c[i]+sum(V[i][j]*h[j] for j in range(12)) for i in range(3)]
 t=sum(map(int,word))%3
 assert any(i!=t and z[i].a>z[t].b for i in range(3))
