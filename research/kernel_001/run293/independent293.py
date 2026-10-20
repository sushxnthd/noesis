"""Independent exact Run293 checker. Requires augmented293.json from evidence archive."""
from pathlib import Path
from fractions import Fraction as F
import json

def parse(z,w):
    q=[F(s) for s in z]
    a=[[[q[x*w*w+i*w+j] for j in range(w)] for i in range(w)] for x in range(2)]
    o=2*w*w
    b=[[q[o+x*w+i] for i in range(w)] for x in range(2)]
    o+=2*w
    return a,b,q[o:o+w],q[o+w]

def verify(p,q,alpha):
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

if __name__=='__main__':
    p=Path(__file__).with_name('augmented293.json')
    rows=json.loads(p.read_text())['rows']
    assert len(rows)==241
    for r in rows:
        verify(r['original'],r['simple'],F(1))
        verify(r['original'],r['shear_scale'],F(7))
    print('PASS: 482/482 exact all-length intertwining identities')
