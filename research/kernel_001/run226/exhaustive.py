"""Vectorized exhaustive NUMERIC search, not an all-length certificate."""
import json,numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent
rows=json.loads((R/'CHECKPOINTS.json').read_text())['rows']
row=next(r for r in rows if r['seed']==1301 and r['epoch']==100)
p=row['params'];W=np.asarray(p['W'],dtype=np.float64);b=np.asarray(p['b'],dtype=np.float64)
v=np.asarray(p['v'],dtype=np.float64);c=float(p['c'])
H=np.asarray([[.5,-.5,.25]],dtype=np.float64);q=np.asarray([0],dtype=np.int8)
for length in range(1,13):
 n=len(H);nh=np.empty((n*3,3),dtype=np.float64);nq=np.empty(n*3,dtype=np.int8)
 for t in range(3):
  nh[t::3]=np.tanh(H@W[t].T+b[t]);nq[t::3]=0 if t==2 else (q^(t==1))
 H,q=nh,nq
 z=H@v+c;signed=np.where(q==1,z,-z)
 bad=np.flatnonzero(signed<0)
 print(length,len(q),len(bad),float(np.min(signed)),flush=True)
 if len(bad):break
