from fractions import Fraction as Q
import json
from pathlib import Path
P=Path(__file__).resolve().parent
for seed,epoch,words in [(29067,68,('010001','1000000000000001','100000000000')),(29091,33,('10000000000100','1000000000000010','1000000000000000'))]:
 p=[Q.from_float(float(z)) for z in json.loads((P.parent/'run340/checkpoints'/f'{seed}_epoch{epoch}.json').read_text())['p']]
 A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
 b=[p[18+3*x:21+3*x] for x in (0,1)]
 def state(w):
  h=(Q(0),)*3
  for bit in w:
   x=int(bit);h=tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(3)),b[x][i])) for i in range(3))
  return h
 a,d,c=map(state,words);j=next(i for i in range(3) if a[i]!=d[i]);q=(c[j]-d[j])/(a[j]-d[j])
 assert 0<q<1 and all(q*a[i]+(1-q)*d[i]==c[i] for i in range(3))
 print(seed,'exact readout-impossibility proof',float(q))
