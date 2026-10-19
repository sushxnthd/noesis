import random
from fractions import Fraction as F
from core import cert

def controls(p,q,seed):
 rng=random.Random(seed+278000)
 changes=[i for i in range(8) if p[i]!=q[i]]
 norm=sum(abs(p[i]-q[i]) for i in changes)
 def draw(same):
  ans=[]
  for j in range(32):
   coords=changes if same else rng.sample(range(8),len(changes))
   signs=[rng.choice((-1,1)) for _ in changes]
   weights=[F(1)] if len(changes)==1 else [F(j+1,33),F(32-j,33)]
   z=p.copy()
   for i,s,w in zip(coords,signs,weights):z[i]+=s*w*norm
   ans.append(bool(cert(z)))
  return ans
 return draw(False),draw(True)
