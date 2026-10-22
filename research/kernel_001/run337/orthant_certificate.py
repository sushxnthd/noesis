"""Exact sufficient parity certificate for a trained width-2 ReLU RNN.
Exploratory post-hoc Run337; not the frozen two-box criterion.
"""
from fractions import Fraction as Q

def verify(p,j,margin=Q(1,100000)):
    p=[Q.from_float(float(x)) for x in p]
    A=[[p[4*x+2*i:4*x+2*i+2] for i in range(2)] for x in (0,1)]
    b=[p[8+2*x:10+2*x] for x in (0,1)]
    v=p[12:14];c=p[14]
    L=b[1][j]
    if L<=0:return False,'no positive lower threshold'
    if c>-margin:return False,'even output'
    if any(t>0 for t in b[0]):return False,'even zero not fixed'
    if any(t<0 for t in v):return False,'odd output not monotone'
    if v[j]*L+c<margin:return False,'odd output margin'
    if any(a<0 for a in A[0][j]):return False,'odd invariant nonmonotone'
    if A[0][j][j]*L+b[0][j]<L:return False,'odd not closed under 0'
    if any(a>0 for row in A[1] for a in row):return False,'odd reset nonmonotone'
    if any(A[1][i][j]*L+b[1][i]>0 for i in range(2)):
        return False,'odd input 1 not zero'
    return True,'PASS'
