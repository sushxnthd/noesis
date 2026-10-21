"""Independent SymPy rational verification of Run320; no imports from run320."""
import json
from pathlib import Path
from itertools import permutations
import sympy as s
P=Path(__file__).resolve().parent
Q=lambda v:s.Rational(*float(v).as_integer_ratio())
v=[Q(x) for x in json.loads((P.parent/'run319/seed22242_epoch80.json').read_text())]
A=[s.Matrix(3,3,v[9*x:9*x+9]) for x in (0,1)]
B=[s.Matrix(3,1,v[18+3*x:21+3*x]) for x in (0,1)]
W=s.Matrix(1,3,v[24:27]);C=v[27]
K=s.Rational(7,10)*W[0]/W[2];T=2*W[2]
vertices=[s.Matrix([0,0,T]),s.Matrix([K*T,0,T])]
rays=[s.Matrix([0,0,1]),s.Matrix([K,0,1])]
def nonnegative(u,z):
    return all((u*t)[0]+z>=0 for t in vertices) and all((u*t)[0]>=0 for t in rays)
def canonical(a,b,w,c):
    pos=[i for i in range(3) if w[i]>0];neg=[i for i in range(3) if w[i]<0]
    if len(pos)!=2 or len(neg)!=1 or any(x==0 for x in w):return None
    f=sorted((w[i]*max(0,b[1][i]),i) for i in pos)
    if f[0][0]==f[1][0]:return None
    order=[f[0][1],neg[0],f[1][1]];S=s.zeros(3)
    for i,j in enumerate(order):S[i,j]=abs(w[j])
    return [S*M*S.inv() for M in a],[S*x for x in b],w*S.inv(),c
def verify(m):
    if m is None:return False
    a,b,w,c=m
    if c>=0 or any(x>0 for x in b[0]):return False
    e=s.Matrix([max(0,x) for x in b[1]])
    if not(e[1]==0 and 0<=e[0]<=K*e[2] and e[2]>=T):return False
    for x in (0,1):
        if not nonnegative(-a[x].row(1),-b[x][1]):return False
        if not nonnegative(a[x].row(2),b[x][2]-T):return False
        if not nonnegative(K*a[x].row(2)-a[x].row(0),K*b[x][2]-b[x][0]):return False
    return nonnegative(w,c-s.Rational(1,1000))
base=canonical(A,B,W,C)
assert verify(base)
scales=[(1,1,1),(2,1,s.Rational(1,2)),(s.Rational(1,3),3,2),(5,s.Rational(1,5),1)]
count=0
for perm in permutations(range(3)):
    for d in scales:
        S=s.zeros(3)
        for i,j in enumerate(perm):S[i,j]=d[j]
        m=canonical([S*M*S.inv() for M in A],[S*x for x in B],W*S.inv(),C)
        assert m==base and verify(m)
        count+=1
bad=[Q(x) for x in json.loads((P/'seed22642_epoch80.json').read_text())]
bad_a=[s.Matrix(3,3,bad[9*x:9*x+9]) for x in (0,1)]
bad_b=[s.Matrix(3,1,bad[18+3*x:21+3*x]) for x in (0,1)]
assert not verify(canonical(bad_a,bad_b,s.Matrix(1,3,bad[24:27]),bad[27]))
assert not verify((base[0],base[1],base[2],s.Rational(1,10)))
assert not verify((base[0],base[1],base[2],-s.Rational(100)))
print('INDEPENDENT PASS',count,'gauge certificates, delayed trained negative, two mutations')
