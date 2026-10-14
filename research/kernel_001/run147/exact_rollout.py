import json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).parent
EXPECTED={208:12,209:13,210:410,211:50,212:19,213:16,214:125,215:None}
def check(seed):
 r=json.loads((P/'checkpoints'/f'{seed}.json').read_text())
 A=[[F(x) for x in row] for row in r['A']]
 e=list(map(F,r['E'][0]));w=list(map(F,r['w']))
 h=[F(0)]*4;first=None
 for n in range(1,513):
  h=[max(F(0),sum(a*x for a,x in zip(row,h))+b) for row,b in zip(A,e)]
  y=sum(a*x for a,x in zip(w,h))
  if first is None and abs(y-n)>F(1,10):first=n
 assert first==EXPECTED[seed]
 return first
