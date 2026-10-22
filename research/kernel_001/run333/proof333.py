"""Exact all-length OR-latch proof for original trained width-3 ReLU checkpoints."""
from fractions import Fraction as F
from itertools import combinations
import json,sys

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def feasible(rows):
    verts=[];rays=[]
    for ids in combinations(range(len(rows)),3):
        (a,u),(b,v),(c,w)=(rows[i] for i in ids)
        ab,bc,ca=cross(a,b),cross(b,c),cross(c,a)
        d=dot(a,bc)
        if not d:continue
        h=tuple((u*bc[j]+v*ca[j]+w*ab[j])/d for j in range(3))
        if all(dot(q,h)>=t for q,t in rows):verts.append(h)
    for i,j in combinations(range(len(rows)),2):
        r=cross(rows[i][0],rows[j][0])
        for s in (-1,1):
            q=tuple(s*t for t in r)
            if any(q) and all(dot(a,q)>=0 for a,_ in rows):rays.append(q)
    return verts,rays

def prove(p):
    p=[F.from_float(float(t)) for t in p]
    A=[[p[9*x+3*i:9*x+3*i+3] for i in range(3)] for x in (0,1)]
    b=[p[18+3*x:21+3*x] for x in (0,1)]
    v=p[24:27];c=p[27];T=-c+F(1,100000)
    if c>=0 or any(t>0 for t in b[0]):return False
    if dot(v,[max(F(0),t) for t in b[1]])<T:return False
    for x in (0,1):
        for mask in range(8):
            rows=[(tuple(F(int(i==j)) for i in range(3)),F(0)) for j in range(3)]
            rows.append((tuple(v),T))
            for i in range(3):
                if mask>>i&1:rows.append((tuple(A[x][i]),-b[x][i]))
                else:rows.append((tuple(-z for z in A[x][i]),b[x][i]))
            obj=tuple(sum((v[i]*A[x][i][j] for i in range(3) if mask>>i&1),F(0)) for j in range(3))
            bias=sum((v[i]*b[x][i] for i in range(3) if mask>>i&1),F(0))
            verts,rays=feasible(rows)
            if any(dot(obj,h)+bias<T for h in verts):return False
            if verts and any(dot(obj,r)<0 for r in rays):return False
    return True

if __name__=='__main__':
    raw=json.load(open(sys.argv[1]))
    for row in raw['rows']:
        if row['epoch']==80:print(row['seed'],prove(row['p']))
