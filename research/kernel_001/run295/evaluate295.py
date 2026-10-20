#!/usr/bin/env python3
"""Run295: frozen reachability-gate adversarial evaluation, on Run291 trained checkpoints."""
import os,sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run294'))
from clock294 import unpack,pack,score
EXCLUDED={21440,21441,21442,21450,21451,21452,21453,21454,21455,21494,21501,21549,21585,21674}
SEEDS=[s for s in range(21440,21696) if s not in EXCLUDED]
assert len(SEEDS)==242

def augment(p,divergent):
 a,b,v,c=unpack(p,3)
 A=[[[F(0)]*6 for i in range(6)] for x in range(2)]
 B=[[F(0)]*6 for x in range(2)]
 for x in range(2):
  for i in range(3): A[x][i][:3]=a[x][i]; B[x][i]=b[x][i]
  A[x][3][3]=F(2) if divergent else F(1,2)
  A[x][4][4]=F(4) if divergent else F(1,2)
  A[x][5][3]=F(1); A[x][5][4]=F(-1)
  B[x][3:]=[F(1),F(3),F(-1)]
 return pack(A,B,v+[F(0),F(0),F(1)],c)

def structural_cone(q):
 A,B,v,c=unpack(q,6); active={i for i in range(6) if v[i]}
 while True:
  nxt=active|{j for i in active for j in range(6) if any(A[x][i][j] for x in range(2))}
  if nxt==active:return sorted(active)
  active=nxt

def run(start,stop):
 data=(P/'checkpoints291.json').read_bytes()
 rows={(r['seed'],r['epoch']):r for r in json.loads(data)['rows']}
 assert len(rows)==1280
 out=[]
 for k in range(start,stop):
  seed=SEEDS[k];p=rows[(seed,20)]['p'];original=score(p,3)
  rec={'seed':seed,'epoch':20,'original':original}
  for name,divergent in [('stable',False),('divergent',True)]:
   q=augment(p,divergent)
   assert structural_cone(q)==list(range(6))
   new=score(q,6)
   rec[name]={'score':new,'delta':new-original,'prune_kept':6}
  out.append(rec)
  if k%40==0:print('PROGRESS',k,seed,flush=True)
 (P/f'partial_{start}_{stop}.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
 print('PARTIAL',start,stop,len(out),flush=True)

def finalize():
 out=[]
 for start,stop in ((0,80),(80,160),(160,242)):
  a=json.loads((P/f'partial_{start}_{stop}.json').read_text())
  assert len(a)==stop-start
  out+=a
 assert len(out)==242 and len({r['seed'] for r in out})==242
 changed=sum(abs(r['divergent']['delta'])>1e-6 for r in out)
 stable=sum(abs(r['stable']['delta'])<=1e-8 for r in out)
 result={'n':242,'divergent_changed':changed,'stable_unchanged':stable,
         'structural_pruning_retains_all':484,'threshold':140,
         'frozen_primary_pass':changed>=140 and stable==242,
         'checkpoint_sha256':hashlib.sha256((P/'checkpoints291.json').read_bytes()).hexdigest(),
         'pilot_excluded':[21440,21441,21442]}
 (P/'rows295.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
 (P/'results295.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RESULTS',json.dumps(result,sort_keys=True),flush=True)
 assert result['divergent_changed']==191 and result['stable_unchanged']==193,'Reproduction differs from archived local results'
 # Do NOT assert frozen_primary_pass: preserve negative outcome as a completed experiment.

if __name__=='__main__':
 if '--finalize' in sys.argv:finalize()
 else:
  start=int(os.getenv('RUN295_START','0'));stop=int(os.getenv('RUN295_STOP','80'))
  assert (start,stop) in ((0,80),(80,160),(160,242))
  run(start,stop)
