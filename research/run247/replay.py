"""NOESIS Run247: finite exhaustive candidate search + independent exact dyadic replays.
Requires immutable Run246 training outputs; never certifies all-length correctness.
"""
import json, hashlib
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent

def candidate(model):
 p=model['params']; a=np.array(p['A']);e=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 h=np.zeros((1,len(v)));state=np.zeros(1,dtype=np.int8)
 for n in range(1,13):
  t=np.tile(np.arange(3,dtype=np.int8),len(state))
  state=np.repeat(state,3);state[t==1]=1;state[t==2]=0
  h=np.maximum(0,np.repeat(h,3,axis=0)@a.T+e[t]+b)
  bad=np.flatnonzero(((h@v+c)>0)!=state)
  if len(bad):
   i=int(bad[0]);s=[0]*n
   for j in range(n-1,-1,-1):s[j],i=i%3,i//3
   return s
 return None

def verify(model,word,independent=False):
 p=model['params']; f=(lambda x:Q(*x.as_integer_ratio())) if independent else Q.from_float
 a=[[f(x) for x in r] for r in p['A']];e=[[f(x) for x in r] for r in p['E']];b=[f(x) for x in p['b']];v=[f(x) for x in p['v']];c=f(p['c']);h=[Q(0)]*len(v);target=0
 for t in word:
  h=[max(Q(0),sum((a[j][k]*h[k] for k in range(len(h))),e[t][j]+b[j])) for j in range(len(h))]
  if t==1:target=1
  elif t==2:target=0
 z=sum((v[k]*h[k] for k in range(len(h))),c)
 return (int(z>0)!=target,target,int(z>0))

def run():
 cp=ROOT/'run246/CHECKPOINTS.json';old=ROOT/'run246/OUTCOMES.json'
 rows=json.loads(cp.read_text())['rows'];prior=json.loads(old.read_text())
 unresolved={r['seed'] for r in prior if r['epoch']==200 and r['exact']['status']=='ABSTAIN'}
 targets=sorted((r for r in rows if r['epoch']==200 and r['seed'] in unresolved),key=lambda r:r['seed'])
 assert len(targets)==18
 out=[]
 for row in targets:
  w=candidate(row);rec={'seed':row['seed'],'train_accuracy':row['train_accuracy'],'status':'NO_WITNESS_THROUGH_12'}
  if w is not None:
   check1=verify(row,w);check2=verify(row,w,True)
   assert check1==check2 and check1[0],(row['seed'],w,check1,check2)
   rec.update(status='EXACT_INCORRECT',witness=w,exact_target=check1[1],exact_prediction=check1[2])
  out.append(rec)
 (HERE/'OUTCOMES.json').write_text(json.dumps(out,indent=2)+'\n')
 successes=[r for r in out if r['status']=='EXACT_INCORRECT']
 summary={'new_exact_incorrect_count':len(successes),'new_exact_incorrect_seeds':[r['seed'] for r in successes],'no_witness_through_12_count':18-len(successes),'primary_pass':len(successes)>=8,'run246_checkpoint_sha256':hashlib.sha256(cp.read_bytes()).hexdigest()}
 assert summary['run246_checkpoint_sha256']=='b0a31428609da72d9aef54606d61d47d2e22c2bd70dc9412df4f5b3ac7237991'
 (HERE/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
 return summary
if __name__=='__main__':run()
