"""NOESIS Run293: exact proportional-neuron quotient; no approximate merges."""
import json
from pathlib import Path
from fractions import Fraction as F

def parse(p,n):
    p=[z if isinstance(z,F) else F(str(z)) for z in p]
    a=[[[p[x*n*n+i*n+j] for j in range(n)] for i in range(n)] for x in range(2)]
    b=[[p[2*n*n+x*n+i] for i in range(n)] for x in range(2)]
    v=p[2*n*n+2*n:2*n*n+3*n]
    c=p[-1]
    assert len(p)==2*n*n+3*n+1
    return a,b,v,c

def flatten(a,b,v,c):
    return [z for ax in a for row in ax for z in row]+[z for bx in b for z in bx]+v+[c]

def augment(p,shear=False):
    a,b,v,c=parse(p,3)
    A=[[[F(0) for _ in range(4)] for _ in range(4)] for _ in range(2)]
    B=[[F(0)]*4 for _ in range(2)]
    for x in range(2):
        for i in range(3):
            A[x][i][:3]=a[x][i].copy()
            A[x][i][0]=a[x][i][0]/2
            A[x][i][3]=a[x][i][0]/2
            B[x][i]=b[x][i]
        A[x][3]=A[x][0].copy()
        B[x][3]=B[x][0]
    V=[v[0]+100,v[1],v[2],F(-100)]
    if shear:
        for x in range(2):
            for i in range(4):
                A[x][i][0]+=16
                A[x][i][3]-=16
            A[x][3]=[7*z for z in A[x][3]]
            B[x][3]*=7
            for i in range(4):A[x][i][3]/=7
        V[3]/=7
    return flatten(A,B,V,c)

def quotient(p,n=4):
    a,b,v,c=parse(p,n)
    for i in range(n):
        for j in range(i+1,n):
            ri=[z for x in range(2) for z in a[x][i]+[b[x][i]]]
            rj=[z for x in range(2) for z in a[x][j]+[b[x][j]]]
            ratio=next((t/u for u,t in zip(ri,rj) if u),None)
            if ratio is None or ratio<=0 or any(t!=ratio*u for u,t in zip(ri,rj)):
                continue
            keep=[k for k in range(n) if k!=j]
            aa=[[[a[x][k][z]+(ratio*a[x][k][j] if z==i else 0)
                  for z in keep] for k in keep] for x in range(2)]
            bb=[[b[x][k] for k in keep] for x in range(2)]
            vv=[v[z]+(ratio*v[j] if z==i else 0) for z in keep]
            return flatten(aa,bb,vv,c),ratio
    return None,None

def test_trained_witness():
    path=Path(__file__).resolve().parents[0]/'../run292/witness292.json'
    p=[F.from_float(x) for x in json.loads(path.read_text())['p']]
    for shear,alpha in ((False,F(1)),(True,F(7))):
        q=augment(p,shear)
        reduced,ratio=quotient(q)
        assert ratio==alpha and reduced==p
        a,b,v,c=parse(p,3)
        A,B,V,C=parse(q,4)
        E=[[F(1),0,0],[0,F(1),0],[0,0,F(1)],[alpha,0,0]]
        for x in range(2):
            for i in range(4):
                assert B[x][i]==sum(E[i][k]*b[x][k] for k in range(3))
                for j in range(3):
                    assert sum(A[x][i][k]*E[k][j] for k in range(4))==sum(E[i][k]*a[x][k][j] for k in range(3))
        for j in range(3):
            assert sum(V[k]*E[k][j] for k in range(4))==v[j]
        assert C==c
        A,B,V,C=parse(q,4)
        B[1][3]+=F(1,1024)
        assert quotient(flatten(A,B,V,C))==(None,None)
        A,B,V,C=parse(q,4)
        A[0][3][1]+=F(1,1024)
        assert quotient(flatten(A,B,V,C))==(None,None)
