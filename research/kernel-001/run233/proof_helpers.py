"""Exact-real binary64 interval replay for 3D tanh checkpoints."""
from mpmath import iv
iv.dps=65
def exact(x):
 n,d=float(x).as_integer_ratio()
 return iv.mpf(n)/iv.mpf(d)
def tanh(z):
 def pt(v):
  e=iv.exp(2*v);return (e-1)/(e+1)
 return iv.mpf([pt(z.a).a,pt(z.b).b])
def evaluate(p,word):
 h=list(map(iv.mpf,['.5','-.5','.25']))
 for t in word:
  h=[tanh(sum((exact(p['W'][t][j][k])*h[k] for k in range(3)),exact(p['b'][t][j]))) for j in range(3)]
 return sum((exact(p['v'][j])*h[j] for j in range(3)),exact(p['c']))
