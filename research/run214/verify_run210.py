import json,numpy as np
from pathlib import Path
from mpmath import iv
iv.dps=85
R=Path(__file__).parent
def ex(x):
 a,b=float(x).as_integer_ratio()
 return iv.mpf(a)/iv.mpf(b)
def th(x):
 def f(z):
  a=iv.exp(2*z);return (a-1)/(a+1)
 return iv.mpf([f(x.a).a,f(x.b).b])
def step(box,W,b):
 return [th(sum(W[j][k]*box[k] for k in range(2))+b[j]) for j in range(2)]
def advance(B,W,b):
 C={}
 for q,h in B.items():
  for t in range(3):
   r=0 if t==2 else q^(t==1)
   z=step(h,W[t],b[t])
   C[r]=[iv.mpf([min(C[r][j].a,z[j].a),max(C[r][j].b,z[j].b)]) for j in range(2)] if r in C else z
 return C
def ok(B,v,c):
 for q,h in B.items():
  z=sum(v[j]*h[j] for j in range(2))+c
  if (q==0 and not z.b<0) or (q==1 and not z.a>0):return False
 return True
def check(row):
 p=row['params'];W=[[[ex(x) for x in r] for r in m] for m in p['W']]
 b=[[ex(x) for x in r] for r in p['b']];v=[ex(x) for x in p['v']];c=ex(p['c'])
 B={0:[ex(.5),ex(-.5)]}
 A={0:(np.array([.5,-.5]),np.array([.5,-.5]))}
 for n in range(60):
  B=advance(B,W,b)
  if not ok(B,v,c):return {'status':'ABSTAIN','reason':'prefix','n':n+1}
  C={};ww=np.array(p['W']);bb=np.array(p['b'])
  for q,(lo,hi) in A.items():
   for t in range(3):
    r=0 if t==2 else q^(t==1)
    pos=np.maximum(ww[t],0);neg=np.minimum(ww[t],0)
    l=np.tanh(pos@lo+neg@hi+bb[t]);u=np.tanh(pos@hi+neg@lo+bb[t])
    C[r]=(np.minimum(C[r][0],l),np.maximum(C[r][1],u)) if r in C else (l,u)
  A=C
 raw={str(q):{'lo':[format(float(x-1e-7),'.17g') for x in lo],'hi':[format(float(x+1e-7),'.17g') for x in hi]} for q,(lo,hi) in A.items()}
 I={int(q):[iv.mpf([raw[q]['lo'][j],raw[q]['hi'][j]]) for j in range(2)] for q in raw}
 for q in (0,1):
  for j in range(2):
   if not(B[q][j].a>=I[q][j].a and B[q][j].b<=I[q][j].b):return {'status':'ABSTAIN','reason':'base'}
 for q in (0,1):
  for t in range(3):
   r=0 if t==2 else q^(t==1);z=step(I[q],W[t],b[t])
   for j in range(2):
    if not(z[j].a>=I[r][j].a and z[j].b<=I[r][j].b):return {'status':'ABSTAIN','reason':'closure'}
 if not ok(I,v,c):return {'status':'ABSTAIN','reason':'output'}
 return {'status':'CERTIFIED','invariant':raw}
if __name__=='__main__':
 rows=[x for x in json.loads((R/'RUN210_CHECKPOINTS.json').read_text())['rows'] if x['epoch']==800]
 out=[]
 for x in rows:
  a=check(x);a['seed']=x['seed'];out.append(a);print(x['seed'],a['status'],flush=True)
 (R/'RUN210_INTERVAL_PROOFS.json').write_text(json.dumps(out,indent=2)+'\n')
