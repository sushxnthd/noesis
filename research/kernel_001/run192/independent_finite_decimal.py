"""Independent directed-Decimal check of all 8190 finite binary prefixes."""
import json
from independent_decimal import I,load,step,out
p,q=load(300),load(600)
states=[([I(0)]*8,[I(0)]*8)]
count=0
for depth in range(1,13):
 nxt=[]
 for a,b in states:
  for bit in (0,1):
   x=step(a,p,bit);y=step(b,q,bit)
   u=out(x,p);v=out(y,q)
   su=1 if u.a>0 else -1 if u.b<0 else 0
   sv=1 if v.a>0 else -1 if v.b<0 else 0
   assert su!=0 and su==sv,("mismatch",depth,bit)
   nxt.append((x,y));count+=1
 states=nxt
assert count==8190
print(json.dumps({"independent":True,"prefixes":count,"disagreements":0}))
