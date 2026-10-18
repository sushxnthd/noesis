"""Reject readout-flipped variants of two all-length certified trained models."""
import json,copy
from pathlib import Path
from verify import check as a
from independent import check as b
R=Path(__file__).parent
rows=json.load(open(R/'CHECKPOINTS.json'))['rows']
E={(r['seed'],r['arm']):r for r in json.load(open(R/'EXACT.json')) if r['epoch']==200}
cert=[r for r in rows if r['epoch']==200 and E[(r['seed'],r['arm'])]['status']=='CERTIFIED']
assert len(cert)>=2
out=[]
for row in cert[:2]:
 r=copy.deepcopy(row);r['params']['v']=[-x for x in r['params']['v']];r['params']['c']=-r['params']['c']
 x=a(r);y=b(r)
 assert x['status']==y['status']=='INCORRECT' and x['witness']==y['witness']
 out.append(dict(seed=r['seed'],arm=r['arm'],status=x['status'],witness=x['witness']))
(R/'NEGATIVE_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
