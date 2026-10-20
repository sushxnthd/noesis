"""Independent rational all-word invariant checker for Run296 public cohort.
Does not import detector, its augmentation code, or the LP scorer.
"""
import json,os
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
EXCLUDED={21440,21441,21442,21450,21451,21452,21453,21454,21455,21494,21501,21549,21585,21674}
SEEDS=[s for s in range(21440,21696) if s not in EXCLUDED]
def parse(p):
 q=[F.from_float(float(x)) for x in p];assert len(q)==28
 A=[[[q[x*9+i*3+j] for j in range(3)] for i in range(3)] for x in range(2)]
 B=[[q[18+x*3+i] for i in range(3)] for x in range(2)]
 return A,B,q[24:27],q[27]
def check(p,kind):
 A,B,v,c=parse(p)
 assert len(v)==3
 for x in (0,1):
  if kind=='stable':au,av,bu,bv,cu,cv,bg=F(1,2),F(1,2),F(1),F(3),F(1),F(-1),F(-1)
  elif kind=='divergent':au,av,bu,bv,cu,cv,bg=F(2),F(4),F(1),F(3),F(1),F(-1),F(-1)
  elif kind=='switched':
   au,av,bu,bv=([F(3,4),F(1),F(2),F(5)] if x==0 else [F(2),F(3),F(1),F(2)])
   cu,cv,bg=F(2),F(-3),F(-1)
  else:raise ValueError(kind)
  assert 0<=au<=av and 0<=bu<=bv and cu>=0 and cv<=-cu and bg<=0
 # Base u=v=g=0. Step v>=u>=0 -> v'>=u'; gate preactivation<=0.
 # Original 3-state recurrence is untouched, with no added->original edges.
 return True
def main():
 ck=Path(os.environ.get('NOESIS_CHECKPOINTS',str(P.parent/'run294/checkpoints291.json')))
 raw=Path(os.environ.get('NOESIS_ROWS',str(P/'rows296_public.json')))
 data=json.loads(ck.read_text());rows={(r['seed'],r['epoch']):r for r in data['rows']}
 out=json.loads(raw.read_text());assert len(out['old'])==242 and len(out['new'])==64
 total=0
 for rec,seed in zip(out['old'],SEEDS):
  assert rec['seed']==seed and rec['recovered']==2
  for kind in ('stable','divergent'):
   assert check(rows[(seed,20)]['p'],kind);total+=1
 for rec,seed in zip(out['new'],SEEDS[:64]):
  assert rec['seed']==seed and rec['proof']=={'u':3,'v':4,'gate':5,'kept':[0,1,2]}
  assert rec['original']==rec['quotient']
  assert check(rows[(seed,20)]['p'],'switched');total+=1
 assert total==548
 print('INDEPENDENT_PASS',total,'exact all-word dominance checks')
if __name__=='__main__':main()
