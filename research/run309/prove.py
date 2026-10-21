import json
from fractions import Fraction as F
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'run307'
a=list(map(F.from_float,json.loads((p/'seed22241_epoch80.json').read_text())))
T=a[23];j=2
assert T>0 and a[27]<0 and a[26]*T+a[27]>0
assert all(a[18+i]<=0 for i in range(3))
assert a[21]<=0 and a[22]<=0
for x in (0,1):
 for i in (0,1):
  slope=a[9*x+3*i+j];bias=a[18+3*x+i]
  assert slope<=0 and slope*T+bias<=0
 slope=a[9*x+3*j+j];bias=a[18+3*x+j]
 assert slope>=0 and slope*T+bias>=T
print('PASS: exact all-length latch correctness, seed 22241 epoch80')
