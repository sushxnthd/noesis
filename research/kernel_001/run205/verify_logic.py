import csv
from pathlib import Path
from fractions import Fraction as Q
from proof_core import bound,f
R=Path(__file__).resolve().parent
def verify(r,c):
 w=[f(r['w0']),f(r['w1'])];b=[f(r['b0']),f(r['b1'])];v=f(r['v']);bias=f(r['c'])
 box=[(Q(c[a]),Q(c[z])) for a,z in [('even_lo','even_hi'),('odd_lo','odd_hi')]]
 def step(lo,hi,bit):
  x=w[bit]*(lo if w[bit]>=0 else hi)+b[bit]
  y=w[bit]*(hi if w[bit]>=0 else lo)+b[bit]
  return bound(x,False),bound(y,True)
 for bit in (0,1):
  a,z=step(Q(1,2),Q(1,2),bit)
  assert box[bit][0]<=a<=z<=box[bit][1]
 for par in (0,1):
  lo,hi=box[par];ymin=v*(lo if v>=0 else hi)+bias;ymax=v*(hi if v>=0 else lo)+bias
  assert ymin>0 if par else ymax<0
  for bit in (0,1):
   a,z=step(lo,hi,bit);l,h=box[par^bit]
   assert l<=a<=z<=h
