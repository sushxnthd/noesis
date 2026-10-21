"""Exact equal-length collision census; expects Run300 checkpoint JSONs here."""
import json
from fractions import Fraction as Q
def check(p):
 a=list(map(Q.from_float,p)); S=[((Q(0),)*3,False)]
 for n in range(1,9):
  N=[]
  for h,label in S:
   for x in (0,1):
    z=tuple(max(Q(0),sum(a[9*x+3*i+j]*h[j] for j in range(3))+a[18+3*x+i]) for i in range(3))
    N.append((z,label or x==1))
  zeros={h for h,y in N if not y}
  if any(y and h in zeros for h,y in N):return n
  S=N
 return 0
for epoch in ('early','late'):
 d=json.load(open('checkpoints300_'+epoch+'.json'))['rows']
 assert len(d)==384
 hits=[(r['seed'],check(r['p'])) for r in d]
 print(epoch,sum(bool(n) for _,n in hits))
