from fractions import Fraction as Q
import json
from pathlib import Path
P=Path(__file__).parent
def bad(p,w):
 z=[Q.from_float(float(x)) for x in p];h=[Q(0)]*3;y=0
 for t,c in enumerate(w,1):
  x=int(c);y=max(y,x)
  h=[max(Q(0),z[18+3*x+i]+sum(z[9*x+3*i+j]*h[j] for j in range(3))) for i in range(3)]
  if int(z[27]+sum(z[24+j]*h[j] for j in range(3))>0)!=y:return t
 return None
if __name__=='__main__':
 models={r['seed']:r['p'] for r in json.loads((P/'checkpoints300_late.json').read_text())['rows']}
 for seed,n,first in json.loads((P/'witnesses302.json').read_text())['witnesses']:
  w=str(first)+'0'*(n-1);p=models[seed]
  assert bad(p,w)==n,(seed,'bad witness')
  assert bad(p,w[:-1]) is None,(seed,'not minimal')
 print('PASS 6 exact rational witnesses')
