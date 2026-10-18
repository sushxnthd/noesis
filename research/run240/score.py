"""Frozen task-conditioned predictor. Does not tune on held-out outcomes."""
import json,math
from pathlib import Path
import numpy as np
from graph import graph_size
R=Path(__file__).parent
D=json.load(open(R/'CHECKPOINTS.json'))['rows']
E={(r['seed'],r['arm'],r['epoch']):r['status'] for r in json.load(open(R/'EXACT.json'))}
seq=np.array([[(n//3**(6-j))%3 for j in range(7)] for n in range(3**7)],dtype=np.int64)
q=np.zeros(len(seq),dtype=np.int64)
for j in range(7):q=np.where(seq[:,j]==2,0,np.where(seq[:,j]==1,1-q,q))
out=[]
for row in D:
 if row['epoch']!=100:continue
 p=row['params'];W=np.array(p['W']);b=np.array(p['b']);v=np.array(p['v'])
 h=np.tile(np.array([.5,-.5,.25,.125]),(len(seq),1))
 for j in range(7):h=np.clip(np.einsum('nij,nj->ni',W[seq[:,j]],h)+b[seq[:,j]],-1,1)
 z=h@v+p['c'];m=float(np.min(np.where(q==1,z,-z)));a=float(np.mean(np.abs(z)));n=graph_size(row)
 out.append(dict(seed=row['seed'],arm=row['arm'],final_status=E[(row['seed'],row['arm'],200)],score=m/(a+.01)-.3*math.log2(1+n),min_margin=m,mean_abs_logit7=a,reachable_count=n,train_accuracy=row['train_accuracy'],train_confidence=row['train_confidence']))
 print(row['seed'],row['arm'],out[-1]['final_status'],round(out[-1]['score'],4),n,flush=True)
(R/'PREDICTIONS.json').write_text(json.dumps(out,indent=2)+'\n')
