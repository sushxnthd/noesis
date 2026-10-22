import json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
rows={r['seed']:r for r in json.loads((P/'trajectories342.json').read_text())['rows'] if r['epoch']==200}
obs=json.loads((P/'outcomes342.json').read_text())['rows']
def exact_logit(p,word):
 p=[F.from_float(float(z)) for z in p];h=[F(0)]*4
 for char in word:
  x=int(char)
  h=[max(F(0),sum((p[x*16+i*4+j]*h[j] for j in range(4)),F(0))+p[32+x*4+i]) for i in range(4)]
 return sum((p[40+j]*h[j] for j in range(4)),p[44])
records=[]
for o in obs:
 f=o['first_failure']
 if f is None:continue
 z=exact_logit(rows[o['seed']]['p'],f['word'])
 assert (z>0)!=bool(f['expected'])
 records.append({'seed':o['seed'],'word':f['word'],'length':f['length'],'expected':f['expected'],'exact_sign':1 if z>0 else (-1 if z<0 else 0)})
assert len(records)==40
(P/'exact_failures342.json').write_text(json.dumps({'verified_count':len(records),'records':records},indent=2)+'\n')
print('exactly verified first failures',len(records))
