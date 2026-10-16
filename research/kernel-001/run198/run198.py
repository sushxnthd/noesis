"""NOESIS Run198: frozen seeds and task-aligned sparse probe."""
import sys,json,math
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'run197'))
import run197 as m
SEEDS=(269,271,277,281)
def train():
 m.SEEDS=SEEDS
 m.train(R/'CI_CHECKPOINTS.json')
def evaluate():
 rows=json.loads((R/'CI_CHECKPOINTS.json').read_text())['rows']
 words=[format(i,'015b') for i in range(32768) if i.bit_count()==3]
 assert len(words)==455
 probe=[]
 for row in rows:
  p=m.params(row);h=np.zeros((455,m.WIDTH));y=np.zeros(455,dtype=np.int8)
  for t in range(15):
   bits=np.array([int(w[t]) for w in words],dtype=np.int8)
   for b in (0,1):
    ix=np.flatnonzero(bits==b)
    if len(ix):h[ix]=m.advance(h[ix],p,b)
   y=(y+bits)%3
  bad=np.flatnonzero(m.logits(h,p).argmax(-1)!=y)
  probe.append({'seed':row['seed'],'epoch':row['epoch'],'errors':len(bad),'words':[words[i] for i in bad]})
 (R/'CI_PROBE_FIRST.json').write_text(json.dumps(probe,indent=1)+'\n')
 result=[]
 for row,pr in zip(rows,probe):
  p=m.params(row);h=np.zeros((1,m.WIDTH));y=np.zeros(1,dtype=np.int8)
  for t in range(15):
   h=np.concatenate((m.advance(h,p,0),m.advance(h,p,1)))
   y=np.concatenate((y,(y+1)%3))
  E=int(np.sum(m.logits(h,p).argmax(-1)!=y));e=pr['errors']
  result.append({'seed':row['seed'],'epoch':row['epoch'],'probe_errors':e,'all_errors':E})
 e=sum(x['probe_errors'] for x in result);E=sum(x['all_errors'] for x in result)
 score=(e/455)/(E/32768) if E else None
 output={'rows':result,'R':score,'threshold':3.0,'success':score is not None and score>=3 and e>0}
 (R/'CI_RESULTS.json').write_text(json.dumps(output,indent=1)+'\n')
 print(output)
if __name__=='__main__':
 import sys
 if sys.argv[1]=='train':train()
 else:evaluate()
