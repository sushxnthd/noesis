"""Frozen Run 214 AUROC evaluation; all endpoint labels independently checked locally."""
import json,numpy as np
from pathlib import Path
R=Path(__file__).parent
D=json.load(open(R/'RUN214_CHECKPOINTS.json'))
CORRECT={967,971,977,983,991,997,1019,1021,1031,1033,1039,1051,1063,1087,1097,1103,1109,1117,1129,1163,1171}
INCORRECT={1009,1013,1049,1061,1069,1093,1123,1151}
UNRESOLVED={953,1091,1153}
assert len(CORRECT)==21 and len(INCORRECT)==8 and len(UNRESOLVED)==3
rng=np.random.default_rng(2142026)
WORDS=[rng.integers(0,3,size=L).tolist() for L in range(2,11)]
def probes(p):
 W=np.asarray(p['W']);b=np.asarray(p['b']);v=np.asarray(p['v']);c=p['c']
 def run(word):
  h=np.array([.5,-.5]);q=0;m=[]
  for t in word:
   q=0 if t==2 else q^(t==1)
   h=np.tanh(W[t]@h+b[t]);m.append(float((2*q-1)*(h@v+c)))
  return m
 ret=min(run([1]+[0]*k+[1])[-1] for k in range(9))
 generic=[run(word) for word in WORDS]
 return ret,min(m[-1] for m in generic),min(z for m in generic for z in m)
def heldout(p,seed):
 W=np.asarray(p['W']);b=np.asarray(p['b']);v=np.asarray(p['v']);c=p['c']
 rng=np.random.default_rng(seed+310000);xx=rng.integers(0,3,size=(128,64),dtype=np.int64)
 h=np.tile([.5,-.5],(128,1));q=np.zeros(128,dtype=np.int8);errors=0
 for j in range(64):
  t=xx[:,j];q=np.where(t==2,0,q^(t==1))
  h=np.tanh(np.einsum('nij,nj->ni',W[t],h)+b[t]);errors+=int(np.count_nonzero((h@v+c>0)!=q))
 return errors
def auc(v,y):
 v=np.array(v);y=np.array(y,dtype=bool);a=v[y];b=v[~y]
 return float(np.mean(a[:,None]>b)+.5*np.mean(a[:,None]==b))
rows=[];out=[]
for r in D['rows']:
 if r['epoch']!=100:continue
 seed=r['seed'];scores=probes(r['params']);loss=r['loss'];errors=heldout(r['params'],seed)
 rows.append({'seed':seed,'label':'CORRECT' if seed in CORRECT else 'INCORRECT' if seed in INCORRECT else 'UNRESOLVED','retention':scores[0],'generic_final':scores[1],'generic_prefix':scores[2],'negative_loss':-loss,'negative_heldout_errors':-errors})
valid=[r for r in rows if r['label']!='UNRESOLVED'];y=[r['label']=='CORRECT' for r in valid]
metrics={k:auc([r[k] for r in valid],y) for k in ('retention','generic_final','generic_prefix','negative_loss','negative_heldout_errors')}
delta=metrics['retention']-max(v for k,v in metrics.items() if k!='retention')
print(json.dumps({'count':len(valid),'scores':metrics,'delta':delta,'status':'FAIL' if delta<.10 else 'PASS'},indent=2))
assert abs(metrics['retention']-0.8928571428571429)<1e-9
assert abs(metrics['generic_prefix']-0.9523809523809523)<1e-9
assert delta<0
(R/'RUN214_REMOTE_EVALUATION.json').write_text(json.dumps({'metrics':metrics,'delta':delta,'rows':rows},indent=2)+'\n')
