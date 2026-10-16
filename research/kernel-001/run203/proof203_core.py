# Run203 independent outward-interval checker
import json,hashlib
from pathlib import Path
from mpmath import iv
R=Path(__file__).parent
iv.dps=70
def q(x):
 n,d=float(x).as_integer_ratio()
 return iv.mpf(n)/iv.mpf(d)
def step(h,p,a):
 return [2/(1+iv.exp(-2*(p['b'][i]+p['U'][a][i]+sum(p['W'][i][j]*h[j] for j in range(12)))))-1 for i in range(12)]
def cls(h,p):
 z=[p['c'][i]+sum(p['V'][i][j]*h[j] for j in range(12)) for i in range(3)]
 wins=[i for i in range(3) if all((z[i]-z[j]).a>0 for j in range(3) if i!=j)]
 assert len(wins)==1
 return wins[0]
