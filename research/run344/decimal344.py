import json
from pathlib import Path
from decimal import Decimal as D, localcontext
P=Path(__file__).resolve().parent
params=json.loads((P.parent/'run343/model343.json').read_text())['p']
with localcontext() as ctx:
 ctx.prec=2000
 p=[D.from_float(float(x)) for x in params]
 a=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
 b=[p[32+4*x:36+4*x] for x in (0,1)]
 v=[D(0),D(0),D(-6352381486487)/D(10)**12,D(862353370801)/D(10)**12,D(-1)]
 def step(h,x):
  return tuple(max(D(0),sum((a[x][i][j]*h[j] for j in range(4)),b[x][i])) for i in range(4))
 states=[(D(0),)*4];count=0
 for length in range(1,15):
  states=[step(h,x) for h in states for x in (0,1)]
  for j,h in enumerate(states):
   z=sum((v[i]*h[i] for i in range(4)),v[4])
   margin=z if j.bit_count()%2 else -z
   assert margin>=1
  count+=len(states)
 assert count==32766
print(json.dumps({'independent_decimal':True,'exact_32766':count,'margin_ge_1':True}))
