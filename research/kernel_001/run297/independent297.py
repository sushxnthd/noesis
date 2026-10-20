"""Independent Fraction-based checker for all Run297 negative witnesses."""
import json
from pathlib import Path
from fractions import Fraction as Q
P=Path(__file__).resolve().parent
r=json.loads((P/'rows297_compact.json').read_text())
ck=json.loads((P/'checkpoints297.json').read_text())
by={(x['seed'],x['epoch']):x for x in ck['rows']}
count=0
for x in r:
 if x['status']!='incorrect':continue
 p=list(map(Q.from_float,by[(x['seed'],80)]['p']))
 mats=[[p[s*9+i*3:s*9+i*3+3] for i in range(3)] for s in (0,1)]
 bias=[p[18+s*3:18+s*3+3] for s in (0,1)]
 readout=p[24:27];offset=p[27]
 h=(Q(0),)*3;state=0;bad=False
 for sym in x['witness']:
  k=int(sym);state=max(state,k)
  h=tuple(max(Q(0),bias[k][i]+sum(mats[k][i][j]*h[j] for j in range(3))) for i in range(3))
  output=offset+sum(readout[i]*h[i] for i in range(3))
  if (output>0)!=bool(state):bad=True
 assert bad,x['seed'];count+=1
assert count==70,count
print('INDEPENDENT_EXACT_WITNESSES',count)
