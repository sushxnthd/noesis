import json
from itertools import product
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
rows={r['seed']:r for r in json.loads((P/'trajectories342.json').read_text())['rows'] if r['epoch']==200}
seeds=[31012,31033,31034,31103]
def exact(p,word):
 p=[F.from_float(float(z)) for z in p];h=[F(0)]*4
 for char in word:
  x=int(char)
  h=[max(F(0),sum((p[x*16+i*4+j]*h[j] for j in range(4)),F(0))+p[32+x*4+i]) for i in range(4)]
 return sum((p[40+j]*h[j] for j in range(4)),p[44])
for seed in seeds:
 for n in range(1,9):
  for bits in product('01',repeat=n):
   word=''.join(bits);z=exact(rows[seed]['p'],word)
   assert (z>0)==(sum(map(int,word))%2==1),(seed,word)
 print('exactly correct through length 8:',seed,'510 words')
