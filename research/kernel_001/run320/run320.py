"""Run320: exact readout-canonicalized inductive certificate on trained RNN."""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as F
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'run319'))
from base319 import a,b,w,c

def canonical(A,B,W,C):
    pos=[i for i in range(3) if W[i]>0];neg=[i for i in range(3) if W[i]<0]
    if len(pos)!=2 or len(neg)!=1 or any(v==0 for v in W):return None
    key=sorted((W[i]*max(F(0),B[1][i]),i) for i in pos)
    if key[0][0]==key[1][0]:return None
    p=[key[0][1],neg[0],key[1][1]];d=[abs(W[j]) for j in p]
    return ([[[d[i]*A[x][p[i]][p[j]]/d[j] for j in range(3)] for i in range(3)] for x in range(2)],
            [[d[i]*B[x][p[i]] for i in range(3)] for x in range(2)],
            [W[p[i]]/d[i] for i in range(3)],C)

K=F(7,10)*w[0]/w[2];T=2*w[2]
def ge(u,v,z):return min(z+v*T,z+(u*K+v)*T,v,u*K+v)>=0

def proof(m):
    if m is None:return False
    A,B,W,C=m;e=[max(F(0),v) for v in B[1]]
    if not(all(v<=0 for v in B[0]) and C<0 and e[1]==0 and 0<=e[0]<=K*e[2] and e[2]>=T):return False
    for x in range(2):
        if not ge(-A[x][1][0],-A[x][1][2],-B[x][1]):return False
        if not ge(A[x][2][0],A[x][2][2],B[x][2]-T):return False
        if not ge(K*A[x][2][0]-A[x][0][0],K*A[x][2][2]-A[x][0][2],K*B[x][2]-B[x][0]):return False
    return ge(W[0],W[2],C-F(1,1000))

base=canonical(a,b,w,c);assert proof(base)
scales=[(F(1),)*3,(F(2),F(1),F(1,2)),(F(1,3),F(3),F(2)),(F(5),F(1,5),F(1))]
passed=0
for p in permutations(range(3)):
    for d in scales:
        aa=[[[d[p[i]]*a[x][p[i]][p[j]]/d[p[j]] for j in range(3)] for i in range(3)] for x in range(2)]
        bb=[[d[p[i]]*b[x][p[i]] for i in range(3)] for x in range(2)]
        ww=[w[p[i]]/d[p[i]] for i in range(3)]
        cm=canonical(aa,bb,ww,c)
        assert cm==base and proof(cm)
        passed+=1
assert passed==24
z=[F.from_float(float(x)) for x in json.loads((Path(__file__).parent/'seed22642_epoch80.json').read_text())]
na=[[[z[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in range(2)]
nb=[[z[18+3*x+i] for i in range(3)] for x in range(2)]
assert not proof(canonical(na,nb,z[24:27],z[27]))
assert not proof((base[0],base[1],base[2],F(1,10)))
print('PASS 24/24 exact canonical gauges; trained delayed-memory checkpoint rejected; mutation rejected')
