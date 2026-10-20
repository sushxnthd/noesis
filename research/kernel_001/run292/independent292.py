#!/usr/bin/env python3
"""Independent exact rational all-word equivalence checker for Run292."""
import json
from pathlib import Path
from fractions import Fraction as Q
P=Path(__file__).resolve().parent
J=json.loads((P/'checkpoints291.json').read_text())
R={(r['seed'],r['epoch']):r['p'] for r in J['rows']}
def verify(seed):
    p=list(map(Q.from_float,R[seed,20]));w=3
    A=[[[p[x*9+i*3+j] for j in range(3)] for i in range(3)] for x in range(2)]
    b=[[p[18+x*3+i] for i in range(3)] for x in range(2)]
    v=p[24:27]
    E=[[Q(1),0,0],[0,Q(1),0],[0,0,Q(1)],[Q(1),0,0]]
    V=[v[0]+100,v[1],v[2],Q(-100)]
    for x in range(2):
        Ap=[[A[x][i][0]/2,A[x][i][1],A[x][i][2],A[x][i][0]/2] for i in (0,1,2,0)]
        bp=[b[x][i] for i in (0,1,2,0)]
        for i in range(4):
            assert bp[i]==sum(E[i][k]*b[x][k] for k in range(3))
            for j in range(3):
                assert sum(Ap[i][k]*E[k][j] for k in range(4))==sum(E[i][k]*A[x][k][j] for k in range(3))
    for j in range(3):
        assert sum(V[k]*E[k][j] for k in range(4))==v[j]
    # ReLU(E z)=E ReLU(z), and E 0=0, so these identities imply
    # exact equality of logits for every finite word by induction.
if __name__=='__main__':
    for seed in range(21450,21696):verify(seed)
    print('PASS 246 exact rational parameter intertwining checks')
