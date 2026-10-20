#!/usr/bin/env python3
"""Run292 function-preserving duplication attack; requires Run291 archive."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P))
import diagnostic291 as D

def duplicate(p):
    D.W=3
    a,b,v,c=D.unpack(p)
    A=np.zeros((2,4,4));B=np.zeros((2,4))
    for x in range(2):
        for i in range(3):
            A[x,i,:3]=a[x,i,:]
            A[x,i,0]/=2
            A[x,i,3]=a[x,i,0]/2
        A[x,3,:]=A[x,0,:]
        B[x,:3]=b[x,:]
        B[x,3]=b[x,0]
    V=[F.from_float(float(v[0]))+100,float(v[1]),float(v[2]),F(-100)]
    D.W=4
    return A.ravel().tolist()+B.ravel().tolist()+V+[c]

def score(p,w):
    D.W=w
    return -D.lp(D.canonical(p))

def run():
    source=json.loads((P/'checkpoints291.json').read_text())
    original={(x['seed'],x['epoch']):x['p'] for x in source['rows']}
    labels={x['seed']:x['epoch80']['label'] for x in json.loads((P/'outcomes291.json').read_text())['rows']}
    rows=[]
    for seed in range(21450,21696):
        p=original[seed,20]
        rows.append(dict(seed=seed,label=labels[seed],
                         score_original=score(p,3),
                         score_duplicate=score(duplicate(p),4)))
    for x in rows:x['difference']=x['score_duplicate']-x['score_original']
    (P/'results292_reproduced.json').write_text(json.dumps(rows,sort_keys=True,indent=2)+'\n')
    print('n',len(rows),'changed',sum(abs(x['difference'])>1e-8 for x in rows))
    clean=[x for x in rows if x['seed'] not in (21494,21501,21549,21585,21674)]
    print('untouched',len(clean),'changed',sum(abs(x['difference'])>1e-8 for x in clean))
if __name__=='__main__':run()
