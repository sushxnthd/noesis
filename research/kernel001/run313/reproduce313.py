"""Run313 exact rational proof on two gradient-trained RNN checkpoints."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
R=Path(__file__).resolve().parent
K,T=F(7,10),F(2)

def params(epoch):
    return [F.from_float(x) for x in json.loads((R/f'seed22242_epoch{epoch}.json').read_text())]

def step(p,h,x):
    return tuple(max(F(0),p[18+3*x+i]+sum(p[9*x+3*i+j]*h[j] for j in range(3))) for i in range(3))

def state(p,s):
    h=(F(0),)*3
    for x in s: h=step(p,h,int(x))
    return h

def nonnegative(a,c,d):
    return min(d+c*T,d+(a*K+c)*T)>=0 and min(c,a*K+c)>=0

def early(p):
    z=(F(0),)*3
    assert step(p,z,0)==z
    assert state(p,'000000')==state(p,'100000')==z
    for n in range(1,6):
        for bits in product('01',repeat=n):
            s=''.join(bits)
            if '1' in s: assert state(p,s)!=state(p,'0'*n)
    for suffix in ('','0','1','010','111000'):
        assert state(p,'000000'+suffix)==state(p,'100000'+suffix)

def late(p):
    A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
    b=[[p[18+3*x+i] for i in range(3)] for x in (0,1)]
    assert all(v<=0 for v in b[0]) and p[27]<0
    e=step(p,(F(0),)*3,1)
    assert e[1]==0 and e[0]>=0 and e[2]>=T and e[0]<=K*e[2]
    for x in (0,1):
        assert nonnegative(-A[x][1][0],-A[x][1][2],-b[x][1])
        assert nonnegative(A[x][2][0],A[x][2][2],b[x][2]-T)
        assert nonnegative(K*A[x][2][0]-A[x][0][0],K*A[x][2][2]-A[x][0][2],K*b[x][2]-b[x][0])
    assert nonnegative(p[24],p[26],p[27]-F(1,1000))
    return p[26]*T+p[27]

def run():
    e,l=params(20),params(80)
    early(e); margin=late(l)
    muts=[(20,20,F(1)),(20,8,F(2)),(20,23,F(100)),(80,22,F(1)),
          (80,27,F(1)),(80,8,F(-10)),(80,11,F(100)),(80,26,F(-5))]
    for ep,i,value in muts:
        q=(e if ep==20 else l).copy();q[i]=value
        try: early(q) if ep==20 else late(q)
        except AssertionError: continue
        raise AssertionError(f'mutation accepted: {ep} {i}')
    print('PASS Run313: exact first collision n=6; all-length late invariant; 8/8 mutations rejected; margin',margin)
    return True
if __name__=='__main__': run()
