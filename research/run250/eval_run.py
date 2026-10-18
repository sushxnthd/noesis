"""Independent public replay of Run250; compare exact falsehood witnesses, not float-only proposals."""
import json,hashlib
from pathlib import Path
import numpy as np
from eval_core import arms
from research.run247.replay import verify
from research.run248.replay import independent
D=Path(__file__).resolve().parent
cp=D/'CHECKPOINTS.json';rows=json.loads(cp.read_text())['rows']
models=sorted((r for r in rows if r['epoch']==200 and r['train_accuracy']==1),key=lambda r:r['seed'])[:24]
assert len(models)==24
counts={k:0 for k in ('jacobian','hold_biased','uniform','fixed_tail')};out=[]
for row in models:
 p=row['params'];a=np.array(p['A']);e=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 tests,ns=arms(row);found={}
 for arm,words in tests.items():
  witness=None
  for w in words:
   h=np.zeros(4);q=0
   for t in w:
    h=np.maximum(0,a@h+e[t]+b)
    q=0 if t==2 else 1 if t==1 else q
   if (h@v+c>0)==bool(q):continue
   exact=verify(row,w);other=independent(row,w)
   assert exact==other and exact[0],(row['seed'],arm,exact,other)
   witness={'word':list(w),'length':len(w),'exact':exact};break
  counts[arm]+=witness is not None;found[arm]=witness
 out.append({'seed':row['seed'],'lengths':ns,'arms':found})
 print('SEED',row['seed'],{k:v is not None for k,v in found.items()},flush=True)
(D/'CI_OUTCOMES.json').write_text(json.dumps(out,indent=2)+'\n')
adv=(counts['jacobian']-max(counts['hold_biased'],counts['uniform']))/24
result={'counts':counts,'advantage':adv,'pass_random_control':adv>=.25,'beats_fixed_tail':counts['jacobian']>counts['fixed_tail'],'checkpoint_sha256':hashlib.sha256(cp.read_bytes()).hexdigest()}
(D/'CI_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
assert counts=={'jacobian':23,'hold_biased':15,'uniform':4,'fixed_tail':24},counts
print('REMOTE_CHECKPOINT_SHA256',result['checkpoint_sha256'],'LOCAL_REFERENCE_SHA256','62195006768cce6a3972c185b69d096d30896f926fca7e2a8f4c2035d498bc72')
# Different CPU/BLAS numerical environments can produce distinct exact parameters; compare frozen outcome counts, never silently equate checkpoints.
print('PASS',result)
