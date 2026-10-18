"""Independent Run250 candidate generator; frozen-Jacobian ranking, no oracle lookahead."""
import numpy as np
POOL=(6,8,10,12,16,20,24,32,40,48,64,80,96,128,160,192,224,256)
FIXED=(8,12,20,32,48,80,128,224)
def arms(row):
 p=row['params'];a=np.array(p['A']);e=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 score={n:-float('inf') for n in POOL}
 for s in (1,2):
  h=np.maximum(0,e[s]+b)
  for _ in range(4):h=np.maximum(0,a@h+e[0]+b)
  g=(a@h+e[0]+b>0).astype(float);m=g[:,None]*a;d=g*(e[0]+b)
  for n in range(6,257):
   h=m@h+d
   if n in score:score[n]=max(score[n],(v@h+c)*(1 if s==2 else -1))
 ns=sorted(POOL,key=lambda n:(-score[n],n))[:8]
 w=[tuple([s]+[0]*(n-1)) for n in ns for s in (1,2)]
 rng=np.random.default_rng(250000+row['seed']);hold=[tuple(map(int,rng.choice(3,size=len(x),p=(.85,.075,.075)))) for x in w]
 rng=np.random.default_rng(350000+row['seed']);uni=[tuple(map(int,rng.choice(3,size=len(x),p=(1/3,1/3,1/3)))) for x in w]
 fixed=[tuple([s]+[0]*(n-1)) for n in FIXED for s in (1,2)]
 return {'jacobian':w,'hold_biased':hold,'uniform':uni,'fixed_tail':fixed},ns
