"""Run296 exact trained-checkpoint evaluation with raw per-seed outcomes."""
import json,hashlib,os,sys
from pathlib import Path
from fractions import Fraction as F
from reachability296 import unpack,pack,quotient,switched
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run294'))
from clock294 import score
EXCLUDED={21440,21441,21442,21450,21451,21452,21453,21454,21455,21494,21501,21549,21585,21674}
SEEDS=[s for s in range(21440,21696) if s not in EXCLUDED]
assert len(SEEDS)==242

def old_augment(p,divergent):
 A,B,v,c=unpack(p,3)
 X=[[[F(0)]*6 for _ in range(6)] for _ in range(2)]
 Y=[[F(0)]*6 for _ in range(2)]
 for x in (0,1):
  for i in range(3):X[x][i][:3]=A[x][i];Y[x][i]=B[x][i]
  X[x][3][3]=F(2) if divergent else F(1,2)
  X[x][4][4]=F(4) if divergent else F(1,2)
  X[x][5][3]=F(1);X[x][5][4]=F(-1)
  Y[x][3:]=[F(1),F(3),F(-1)]
 return pack(X,Y,v+[F(0),F(0),F(1)],c)

def exact_output(p,w,word):
 A,B,v,c=unpack(p,w);h=[F(0)]*w
 for x in word:h=[max(F(0),sum(A[x][i][j]*h[j] for j in range(w))+B[x][i]) for i in range(w)]
 return sum(v[i]*h[i] for i in range(w))+c

def main():
 ck=Path(os.environ.get('NOESIS_CHECKPOINTS',str(P.parent/'run294/checkpoints291.json')))
 raw=ck.read_bytes();data=json.loads(raw);rows={(r['seed'],r['epoch']):r for r in data['rows']}
 assert len(rows)==1280
 old=[]
 for seed in SEEDS:
  p=rows[(seed,20)]['p'];canonical=pack(*unpack(p,3))
  for label,div in (('stable',False),('divergent',True)):
   q=old_augment(p,div);reduced,w,proof=quotient(q,6)
   assert proof is not None and w==3 and reduced==canonical,(seed,label)
  old.append({'seed':seed,'recovered':2})
 print('OLD',len(old)*2,flush=True)
 novel=[]
 for i,seed in enumerate(SEEDS[:64]):
  p=rows[(seed,20)]['p'];q=switched(p)
  reduced,w,proof=quotient(q,6)
  assert proof is not None and w==3 and reduced==pack(*unpack(p,3)),seed
  s0=score(p,3);s1=score(q,6);sfix=score(reduced,3)
  assert abs(s0-sfix)<1e-12,seed
  novel.append({'seed':seed,'original':s0,'switched':s1,'quotient':sfix,'delta':s1-s0,'proof':proof})
  if i%16==0:print('NEW',i,seed,flush=True)
 p=rows[(SEEDS[0],20)]['p'];q=switched(p);mutations=[]
 for label,x,i,delta in [('gate0',0,5,F(3)),('gate1',1,5,F(3)),('u1',1,3,F(5)),('v1',1,4,F(-5))]:
  A,B,v,c=unpack(q,6);B[x][i]+=delta;bad=pack(A,B,v,c)
  _,_,proof=quotient(bad,6)
  assert proof is None,label
  witness=None
  for length in (1,2,3):
   for k in range(1<<length):
    word=[(k>>j)&1 for j in range(length)]
    if exact_output(q,6,word)!=exact_output(bad,6,word):
     witness=''.join(map(str,word));break
   if witness is not None:break
  assert witness is not None,label
  mutations.append({'label':label,'witness':witness,'rejected':True})
 changed=sum(abs(r['delta'])>1e-6 for r in novel)
 result={'run':296,'old_recovered':484,'new_recovered':64,'total_recovered':548,
         'new_changed':changed,'mutations':mutations,'frozen_exact_pass':True,
         'learning_relevance_pass':changed>=10,
         'checkpoint_sha256':hashlib.sha256(raw).hexdigest()}
 (P/'rows296_public.json').write_text(json.dumps({'old':old,'new':novel},sort_keys=True,indent=2)+'\n')
 (P/'results296_public.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RESULTS',json.dumps(result,sort_keys=True),flush=True)
 assert changed>=10
if __name__=='__main__':main()
