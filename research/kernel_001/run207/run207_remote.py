"""Run207 frozen predictor: early geometry vs eventual independently certified reset parity.
The frozen protocol was committed before holdout training. Uncertified != incorrect.
"""
import csv,hashlib,json,math,platform
from pathlib import Path
import numpy as np,torch
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'run206'))
import train,certify

SEEDS=(353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647)

def feature(row):
 p=row['params'];w=np.asarray(p['w']);b=np.asarray(p['b']);v=p['v'];c=p['c']
 h=np.full(729,.5);state=np.zeros(729,dtype=np.int64)
 x=train.words().numpy()
 for t in range(6):
  tok=x[:,t];h=np.tanh(w[tok]*h+b[tok]);state=np.where(tok==2,0,state^(tok==1))
 mu=[float(np.median(h[state==q])) for q in (0,1)]
 D=abs(mu[1]-mu[0])
 if D<1e-10:return {'score':-1e6,'mu':mu,'D':D,'residual':None,'jacobian':None,'readout_margin':None}
 residual=0.;J=0.
 for q in (0,1):
  for a in (0,1,2):
   dest=0 if a==2 else q^(a==1)
   y=math.tanh(w[a]*mu[q]+b[a])
   residual=max(residual,abs(y-mu[dest])/D)
   J=max(J,abs(w[a])*(1-y*y))
 M=min(-(v*mu[0]+c),v*mu[1]+c)/(abs(v)*D+1e-12)
 return {'score':min(.5-residual,M)-max(0.,J-1.),'mu':mu,'D':D,'residual':residual,'jacobian':J,'readout_margin':M}

def auc(scores,labels):
 p=[s for s,y in zip(scores,labels) if y];n=[s for s,y in zip(scores,labels) if not y]
 if min(len(p),len(n))<5:return None
 return sum(1 if x>y else .5 if x==y else 0 for x in p for y in n)/(len(p)*len(n))

def run():
 summaries=[];checkpoints=[];proofs=[];errors=[]
 for seed in SEEDS:
  rows=train.train(seed);early=next(r for r in rows if r['epoch']==50);late=next(r for r in rows if r['epoch']==800)
  f=feature(early);candidate=certify.propose(late)
  certified=False;failure=None;proof=None
  if candidate['accepted']:
   try:
    proof=certify.exact(late,candidate)
    assert certify.independent(late,candidate)
    certified=True
   except Exception as e:failure=repr(e)
  summaries.append({'seed':seed,'geometry':f['score'],'loss_baseline':-early['loss'],
   'heldout_baseline':-early['heldout64']['errors'],'train_acc50':early['train_accuracy'],
   'train_acc800':late['train_accuracy'],'heldout64_errors50':early['heldout64']['errors'],
   'heldout256_errors800':late['heldout256']['errors'],'certified':certified,
   'feature_detail':f,'candidate':candidate,'checker_failure':failure})
  if certified:proofs.append({'seed':seed,'epoch':800,'candidate':candidate,'exact':proof,'independent':True})
  checkpoints.extend(rows)
  print(seed,'certified',certified,'score',round(f['score'],6),flush=True)
 labels=[int(s['certified']) for s in summaries]
 A={key:auc([s[key] for s in summaries],labels) for key in ('geometry','loss_baseline','heldout_baseline')}
 npos=sum(labels);valid=npos>=5 and 48-npos>=5
 passed=bool(valid and A['geometry']>=.70 and A['geometry']>=max(A['loss_baseline'],A['heldout_baseline'])+.05)
 result={'protocol':'FROZEN_PROTOCOL.md','seeds':SEEDS,'n_positive':npos,'n_uncertified':48-npos,
  'auc':A,'criterion_valid':valid,'frozen_pass':passed,'summary':summaries,'proofs':proofs,
  'note':'Negative labels denote abstentions, not proven failures','python':platform.python_version(),
  'torch':torch.__version__,'numpy':np.__version__}
 HERE.joinpath('RUN207_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 HERE.joinpath('RUN207_CHECKPOINTS.json').write_text(json.dumps({'seeds':SEEDS,'rows':checkpoints},indent=2)+'\n')
 with HERE.joinpath('RUN207_SUMMARY.csv').open('w',newline='') as f:
  fields=['seed','geometry','loss_baseline','heldout_baseline','train_acc50','train_acc800','heldout64_errors50','heldout256_errors800','certified']
  writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
  writer.writerows({k:s[k] for k in fields} for s in summaries)
 files=('RUN207_RESULTS.json','RUN207_CHECKPOINTS.json','RUN207_SUMMARY.csv')
 HERE.joinpath('RUN207_HASHES.txt').write_text(''.join(hashlib.sha256(HERE.joinpath(f).read_bytes()).hexdigest()+'  '+f+'\n' for f in files))
 print('PRIMARY',{'n_positive':npos,'auc':A,'frozen_pass':passed,'valid':valid})
if __name__=='__main__':run()
