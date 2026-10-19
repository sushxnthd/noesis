#!/usr/bin/env python3
"""Independent SymPy exact closed-form and region-image checker."""
import json
from pathlib import Path
from sympy import Rational as R
P=Path(__file__).resolve().parent
B=json.loads((P/'baseline_epoch500.json').read_text())
A=json.loads((P/'adverse_epoch500_part1.json').read_text())
def q(x):n,d=float(x).as_integer_ratio();return R(n,d)
def unpack(p):return [q(x) for x in p[0]],[q(x) for x in p[1]],q(p[2]),q(p[3])
for seed,p in B.items():
 a,b,v,c=unpack(p);L=max(R(0),b[2]);U=b[1]
 assert v>0 and c<0 and 0<=L<U and v*L+c<0<v*U+c
 assert a[0]>=0 and max(R(0),a[0]*L+b[0])<=L
 assert max(R(0),a[0]*U+b[0])>=U
 assert a[1]>=0 and b[1]>=U and a[2]<=0 and max(R(0),b[2])<=L
expected={'19403':31,'19405':18,'19406':25,'19408':21,'19410':18,'19412':20,'19413':20,'19421':25,'19425':21}
for seed,p in A.items():
 a,b,v,c=unpack(p);f=b[0]/(1-a[0]);s=max(R(0),b[1])
 assert a[0]>1 and a[2]>0 and v>0 and c<0 and f>=0 and s>f
 def out(n):return v*max(R(0),a[2]*(f+(s-f)*a[0]**n)+b[2])+c
 N=expected[seed];assert out(N)>0 and (N==0 or out(N-1)<=0)
print('INDEPENDENT_SYMPY_PASS 18 positive, 9 negative proofs')
