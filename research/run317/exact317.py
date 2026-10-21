"""Exact all-length certificate for a repaired gradient-trained recurrent core."""
from fractions import Fraction as Q
from pathlib import Path
import json
P=Path(__file__).resolve().parent
p=[Q.from_float(x) for x in json.loads((P/'seed22642_epoch80.json').read_text())]
original=p[:];p[0]=Q(11,10);p[27]=-Q(1,100)
Z=(Q(0),)*3

def step(h,x,params=p):
    return tuple(max(Q(0),sum(params[9*x+3*i+j]*h[j] for j in range(3))+params[18+3*x+i]) for i in range(3))
def affine_nonneg(a,c,d):
    # Polyhedron C: h1=0, h0>=1, 0<=h2<=3*h0.
    # Its two vertices and recession rays are (1,0) and (1,3).
    return a+d>=0 and a+3*c+d>=0 and a>=0 and a+3*c>=0

def coeff(x,i):return (p[9*x+3*i],p[9*x+3*i+2],p[18+3*x+i])
assert step(Z,0)==Z and p[27]<0
entry=step(Z,1)
assert entry[1]==0 and entry[0]>=1 and 0<=entry[2]<=3*entry[0]
for x in (0,1):
    a,c,d=coeff(x,1)
    assert affine_nonneg(-a,-c,-d)  # h1' == 0
    a,c,d=coeff(x,0)
    assert affine_nonneg(a,c,d-1)   # h0' >= 1
    u,v,e=coeff(x,2)
    assert affine_nonneg(3*a-u,3*c-v,3*d-e) # h2' <= 3*h0'
assert affine_nonneg(p[24],p[26],p[27]-Q(1,100))
assert all(original[i]==p[i] for i in range(28) if i not in (0,27))
control=original[:];control[27]=-Q(1,100)
a=b=Z
for n in range(1,12):
    a=step(a,0,control)
    b=step(b,1 if n==1 else 0,control)
assert a==b==Z
print('PASS exact all-length invariant, bias-only collision at n=11, original checkpoint retained')
