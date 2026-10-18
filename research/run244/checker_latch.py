from fractions import Fraction as F
S=1024
def check(row,cert):
 p=row['params'];f=lambda x:F.from_float(float(x))
 W=[[[f(x) for x in a] for a in m] for m in p['W']];b=[[f(x) for x in a] for a in p['b']];v=list(map(f,p['v']));c=f(p['c'])
 assert cert['grid_scale']==S
 B={(x['q'],tuple(x['suffix'])):(x['lo'],x['hi']) for x in cert['cells']}
 assert len(B)==len(cert['cells']) and (0,()) in B
 lo,hi=B[0,()];assert all(lo[i]<=x<=hi[i] for i,x in enumerate((512,-512,256,128)))
 for (q,s),(lo,hi) in B.items():
  assert q in (0,1) and len(s)<=2 and all(-S<=a<=z<=S for a,z in zip(lo,hi))
  if s:
   zlo=c*S+sum(v[k]*(lo[k] if v[k]>=0 else hi[k]) for k in range(4))
   zhi=c*S+sum(v[k]*(hi[k] if v[k]>=0 else lo[k]) for k in range(4))
   assert zlo>0 if q else zhi<0
  for t in range(3):
   dest=(0 if t==2 else (1 if t==1 else q),(s+(t,))[-2:]);assert dest in B
   dl,du=B[dest]
   for j in range(4):
    a=b[t][j]*S+sum(W[t][j][k]*(lo[k] if W[t][j][k]>=0 else hi[k]) for k in range(4))
    z=b[t][j]*S+sum(W[t][j][k]*(hi[k] if W[t][j][k]>=0 else lo[k]) for k in range(4))
    assert F(dl[j])<=max(-S,min(S,a)) and min(S,max(-S,z))<=F(du[j])
 return True
