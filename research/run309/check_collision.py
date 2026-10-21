import json
from pathlib import Path
from fractions import Fraction as Q
p=Path(__file__).resolve().parent.parent/'run307'
early=json.loads((p/'seed22241_epoch20.json').read_text())
late=json.loads((p/'seed22241_epoch80.json').read_text())
def step(a,h,x):
 return tuple(max(Q(0),sum(a[9*x+3*i+k]*h[k] for k in range(3))+a[18+3*x+i]) for i in range(3))
def h(params,word):
 a=list(map(Q.from_float,params));z=(Q(0),)*3
 for x in map(int,word):z=step(a,z,x)
 return z
assert h(early,'00')==h(early,'10')
assert h(late,'00')!=h(late,'10')
print('PASS: early same-length collision; late collision resolved')
