"""Independently exact-check all frozen Run240 endpoints."""
import json
from pathlib import Path
from verify import check as fraction
from independent import check as dyadic
R=Path(__file__).parent
D=json.load(open(R/'CHECKPOINTS.json'))
rows={(r['seed'],r['arm'],r['epoch']):r for r in D['rows']}
assert len(rows)==144
out=[]
for seed in range(6201,6225):
 for arm in ('baseline','saturation'):
  for ep in (0,200):
   row=rows[(seed,arm,ep)];a=fraction(row);b=dyadic(row)
   assert a['status']==b['status'],(seed,arm,ep,a,b)
   if a['status']=='CERTIFIED':assert a['states']==b['states']
   if a['status']=='INCORRECT':assert a['witness']==b['witness']
   out.append(dict(seed=seed,arm=arm,epoch=ep,**a,independent_agreement=True))
   print(seed,arm,ep,a['status'],flush=True)
(R/'EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
