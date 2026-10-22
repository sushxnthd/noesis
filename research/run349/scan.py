"""Run349 frozen-generator cohort scan: LP proposes; exact arithmetic decides."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import sympy as S
from wordgen import generate
from verify_witness import states
P=Path(__file__).resolve().parent
W=generate()
y=np.array([w.count('1')%2 for w in W])
sg=2*y-1

def scan(seed,epoch):
    p=json.loads((P/f'checkpoint_{seed}_{epoch}.json').read_text())['p']
    A=np.array(p[:18]).reshape(2,3,3);b=np.array(p[18:24]).reshape(2,3)
    cache={'':np.zeros(3)}
    for w in W:
        for t in range(1,len(w)+1):
            q=w[:t]
            if q not in cache:
                cache[q]=np.maximum(A[int(q[-1])]@cache[q[:-1]]+b[int(q[-1])],0)
    H=np.array([cache[w] for w in W])
    scale=np.maximum(np.max(np.abs(H),axis=0),1)
    M=np.vstack(((y==1).astype(float),(y==0).astype(float),(H*sg[:,None]/scale).T))
    lp=linprog(np.zeros(len(W)),A_eq=M,b_eq=[1,1,0,0,0],bounds=(0,None),method='highs')
    result={'seed':seed,'epoch':epoch,'numeric_collision':bool(lp.success),'exact_collision':False}
    if lp.success:
        words=[W[i] for i in np.flatnonzero(lp.x>1e-10)]
        h=states(p,words)
        labels=[w.count('1')%2 for w in words]
        B=S.Matrix([[int(t==1) for t in labels],[int(t==0) for t in labels]]
          +[[z[j]*(1 if label else -1) for z,label in zip(h,labels)] for j in range(3)])
        try:
            c,free=B.gauss_jordan_solve(S.Matrix([1,1,0,0,0]))
            result['exact_collision']=bool(free.rows==0 and all(z>0 for z in c) and B*c==S.Matrix([1,1,0,0,0]))
        except ValueError:
            pass
        result['candidate_words']=words
    return result

if __name__=='__main__':
    rows=[scan(s,e) for s,e in ((32135,81),(32135,82),(32187,37),
       (32135,200),(32187,200),(32098,200))]
    assert sum(r['exact_collision'] for r in rows)==2
    assert all(r['exact_collision'] for r in rows[:2])
    assert not any(r['exact_collision'] for r in rows[2:])
    (P/'scan_results.json').write_text(json.dumps(rows,indent=2)+'\n')
    print('EXACT COHORT SCAN PASS: 2/3 early, 0/3 certified controls')
