"""Float64 candidate search only; strict witnesses checked separately."""
import numpy as np,json
from pathlib import Path
R=Path(__file__).parent
D=json.load(open(R/'CHECKPOINTS.json'))
def search(row,depth=8):
 p=row['params'];W=np.array(p['W']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 h=np.array([[.5,-.5,.25]]);q=np.array([0],dtype=np.int8);words=np.array([0],dtype=np.int64)
 for length in range(1,depth+1):
  H=np.vstack([np.tanh(h@W[t].T+b[t]) for t in range(3)])
  Q=np.concatenate([q,np.ones_like(q),np.zeros_like(q)])
  codes=np.concatenate([words*3+t for t in range(3)])
  wrong=np.where(((H@v+c)>0)!=Q)[0]
  if len(wrong):
   i=int(wrong[0]);code=int(codes[i]);w=[0]*length
   for j in range(length-1,-1,-1):w[j]=code%3;code//=3
   return dict(status='NUMERIC_CANDIDATE',length=length,word=w,logit=float(H[i]@v+c),correct=int(Q[i]))
  h,q,words=H,Q,codes
 return dict(status='NO_NUMERIC_ERROR_THROUGH',length=depth)
out=[]
for row in D['rows']:
 r=search(row,8);out.append(dict(seed=row['seed'],epoch=row['epoch'],**r))
 print(row['seed'],row['epoch'],r['status'],r['length'],flush=True)
(R/'NUMERIC_WITNESSES.json').write_text(json.dumps(out,indent=2)+'\n')
