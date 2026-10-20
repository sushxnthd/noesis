import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from clock294 import augment,exact_projection,prune,score
P=Path(__file__).resolve().parent
EXCLUDE={21450,21451,21452,21453,21454,21455,21494,21501,21549,21585,21674}
SEEDS=[s for s in range(21440,21696) if s not in EXCLUDE]
def main():
 raw=(P/'checkpoints291.json').read_bytes()
 digest=hashlib.sha256(raw).hexdigest()
 rows={(r['seed'],r['epoch']):r for r in json.loads(raw)['rows']}
 assert len(rows)==1280
 print('CHECKPOINT_HASH',digest,flush=True)
 out=[]
 for k,seed in enumerate(SEEDS):
  p=rows[(seed,20)]['p'];old=score(p,3)
  r={'seed':seed,'original':old}
  for name,gain in [('stable',F(1,2)),('divergent',F(2))]:
   q=augment(p,gain)
   assert exact_projection(p,q)
   rawscore=score(q,4)
   reduced,keep=prune(q,4)
   assert keep==[0,1,2]
   assert reduced==[F.from_float(float(x)) for x in p]
   restored=score(reduced,3)
   assert abs(restored-old)<1e-9
   r[name]={'raw_score':rawscore,'restored_score':restored,'delta':rawscore-old}
  out.append(r)
  if k%50==0:print('PROGRESS',k,flush=True)
 (P/'rows294.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
