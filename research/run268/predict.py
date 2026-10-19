"""Frozen local switch-margin extrapolator; run before long-horizon validation."""
import json,hashlib
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
def forward_margin(p,first,last,n):
 A=np.asarray(p['A']);E=np.asarray(p['E']);b=np.asarray(p['b']);v=np.asarray(p['v']);c=p['c']
 h=np.zeros(len(b));h=np.maximum(A@h+E[first]+b,0)
 for _ in range(n):h=np.maximum(A@h+E[0]+b,0)
 h=np.maximum(A@h+E[last]+b,0)
 y=0 if last==2 else 1
 z=float(v@h+c)
 return z if y else -z
def predict(p):
 m={}
 for a,b in ((1,2),(2,1)):
  x=[forward_margin(p,a,b,n) for n in (16,32,64)]
  d1=x[1]-x[0];d2=x[2]-x[1]
  crossing=64+32*x[2]/(-d2) if d1<0 and d2<0 and x[2]>0 else None
  pred=x[2]<=0 or (crossing is not None and crossing<=2048)
  m[f'{a}to{b}']={'m16':x[0],'m32':x[1],'m64':x[2], 'slope1':d1,'slope2':d2,'crossing_estimate':crossing,'prediction':bool(pred)}
 A=np.asarray(p['A']);rho=float(max(abs(np.linalg.eigvals(A))))
 return {'families':m,'predict':any(q['prediction'] for q in m.values()),'baseline_spectral':bool(rho>1),'baseline_n64':any(q['m64']<=0 for q in m.values()),'spectral_radius':rho}
if __name__=='__main__':
 rows=[]
 for dim in (2,3):
  f=json.loads((P/f'CHECKPOINTS_dim{dim}.json').read_text())
  for r in f['rows']:
   if r['epoch']==600:
    rows.append({k:r[k] for k in ('seed','dimension','epoch','train_accuracy','bce')} | predict(r['params']))
 out=P/'FROZEN_PREDICTIONS.json'
 out.write_text(json.dumps({'frozen_before_long_horizon_replay':True,'source_files':['CHECKPOINTS_dim2.json','CHECKPOINTS_dim3.json'],'rows':rows},indent=2,allow_nan=False)+'\n')
 digest=hashlib.sha256(out.read_bytes()).hexdigest()
 (P/'FROZEN_SHA256.txt').write_text(f'{digest}  FROZEN_PREDICTIONS.json\n')
 print('FROZEN_SHA256',digest)
 for r in rows:print(r['seed'],r['dimension'],r['train_accuracy'],r['predict'],r['baseline_spectral'],r['baseline_n64'])
