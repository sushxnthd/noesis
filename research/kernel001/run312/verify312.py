#!/usr/bin/env python3
"""Run312: exact proof on original gradient-trained binary64 checkpoint."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
p=[F.from_float(v) for v in json.loads((ROOT.parent/'run311/seed22242.json').read_text())]
assert len(p)==28
A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
b=[[p[18+3*x+i] for i in range(3)] for x in (0,1)]
w=p[24:27]; bias=p[27]
k=F(7,10); T=F(2)
# C = {h1=0, 0<=h0<=k*h2, h2>=T}.
# Nonnegative affine form a*h0+c*h2+d on C iff all four checks hold.
def nonnegative(a,c,d):
    return min(d+c*T,d+(a*k+c)*T,c,a*k+c)>=0
def check(p_override=None):
    global p,A,b,w,bias
    if p_override is not None:
        p=p_override
        A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
        b=[[p[18+3*x+i] for i in range(3)] for x in (0,1)]
        w=p[24:27];bias=p[27]
    if not(all(z<=0 for z in b[0]) and bias<0):return False
    entry=[max(F(0),z) for z in b[1]]
    if not(entry[1]==0 and entry[0]<=k*entry[2] and entry[2]>=T):return False
    if not nonnegative(w[0],w[2],bias-F(1,1000)):return False
    for x in (0,1):
        if not nonnegative(-A[x][1][0],-A[x][1][2],-b[x][1]):return False
        if not nonnegative(A[x][2][0],A[x][2][2],b[x][2]-T):return False
        if not nonnegative(k*A[x][2][0]-A[x][0][0],k*A[x][2][2]-A[x][0][2],k*b[x][2]-b[x][0]):return False
    return True
assert check()
print('PASS: seed22242 epoch80 is correct on all finite nonempty binary inputs')
print('Exact lower bound on positive logit:',w[2]*T+bias)
