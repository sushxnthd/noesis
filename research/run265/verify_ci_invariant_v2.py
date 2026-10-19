# Run265 exact invariant checker: stable wrong attractor on frozen checkpoints
import json
from fractions import Fraction as Q
from pathlib import Path
data=json.loads((Path(__file__).parent/'CI_REPRESENTATIVE_WITNESSES.json').read_text())
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(pts):
 pts=sorted(set(pts));lo=[];hi=[]
 for p in pts:
  while len(lo)>1 and cross(*lo[-2:],p)<=0:lo.pop()
  lo.append(p)
 for p in pts[::-1]:
  while len(hi)>1 and cross(*hi[-2:],p)<=0:hi.pop()
  hi.append(p)
 return lo[:-1]+hi[:-1]
def check(r):
 p=r['params'];A=[[Q(x) for x in row] for row in p['A']]
 E=[[Q(x) for x in row] for row in p['E']]
 b=list(map(Q,p['b']));v=list(map(Q,p['v']));c=Q(p['c'])
 def pre(h,x):return tuple(sum(A[i][j]*h[j] for j in (0,1))+E[x][i]+b[i] for i in (0,1))
 def step(h,x):return tuple(max(Q(0),z) for z in pre(h,x))
 orbit=[step((Q(0),Q(0)),r['prefix'])]
 for _ in range(20):orbit.append(step(orbit[-1],0))
 for m in ((0,0),(0,1),(1,0),(1,1)):
  B=[[m[i]*A[i][j] for j in (0,1)] for i in (0,1)]
  e=[m[i]*(E[0][i]+b[i]) for i in (0,1)]
  D=(1-B[0][0])*(1-B[1][1])-B[0][1]*B[1][0]
  if D==0:continue
  f=((1-B[1][1])*e[0]+B[0][1]*e[1])/D,(B[1][0]*e[0]+(1-B[0][0])*e[1])/D
  tr=B[0][0]+B[1][1];dt=B[0][0]*B[1][1]-B[0][1]*B[1][0]
  if min(1-dt,1-tr+dt,1+tr+dt)<=0 or step(f,0)!=f:continue
  for k in range(13):
   poly=hull(orbit[k:k+9]+[f])
   if len(poly)<3:continue
   inside=lambda x:all(cross(poly[i],poly[(i+1)%len(poly)],x)>=0 for i in range(len(poly)))
   if not inside(orbit[k]):continue
   if not all(all(z>=0 if m[i] else z<=0 for i,z in enumerate(pre(x,0))) for x in poly):continue
   if not all(inside(step(x,0)) for x in poly):continue
   z=sum(v[i]*f[i] for i in (0,1))+c
   if (z<=0 if r['prefix']==1 else z>0):return True
 return False
for r in data:
 assert check(r)
 print('PASS exact invariant',r['seed'])
