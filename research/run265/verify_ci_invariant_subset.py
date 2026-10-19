"""Exact stable wrong-attractor polygons for three trained ReLU checkpoints."""
import json
from fractions import Fraction as F
from pathlib import Path
rows=json.loads((Path(__file__).parent/'CI_REPRESENTATIVE_WITNESSES.json').read_text())
q=F.from_float
def cross(o,a,b):
 return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
 p=sorted(set(points));lo=[];hi=[]
 for x in p:
  while len(lo)>1 and cross(lo[-2],lo[-1],x)<=0:lo.pop()
  lo.append(x)
 for x in p[::-1]:
  while len(hi)>1 and cross(hi[-2],hi[-1],x)<=0:hi.pop()
  hi.append(x)
 return lo[:-1]+hi[:-1]
def inside(poly,x):
 return len(poly)>=3 and all(cross(poly[i],poly[(i+1)%len(poly)],x)>=0 for i in range(len(poly))
def prove(r):
 p=r['params']
 A=[[q(x) for x in row] for row in p['A']]
 E=[[q(x) for x in row] for row in p['E']]
 b=[q(x) for x in p['b']]
 v=[q(x) for x in p['v']]
 c=q(p['c'])
 def pre(h,x):
  return tuple(sum(A[i][j]*h[j] for j in range(2))+E[x][i]+b[i] for i in range(2))
 def step(h,x):
  return tuple(max(F(0),z) for z in pre(h,x))
 orbit=[step((F(0),F(0)),r['prefix'])]
 for _ in range(20):orbit.append(step(orbit[-1],0))
 for mask in ((0,0),(0,1),(1,0),(1,1)):
  B=[[mask[i]*A[i][j] for j in range(2)] for i in range(2)]
  e=[mask[i]*(E[0][i]+b[i]) for i in range(2)]
  d=(1-B[0][0])*(1-B[1][1])-B[0][1]*B[1][0]
  if not d:continue
  f=((1-B[1][1])*e[0]+B[0][1]*e[1])/d,(B[1][0]*e[0]+(1-B[0][0])*e[1])/d
  tr=B[0][0]+B[1][1]
  dt=B[0][0]*B[1][1]-B[0][1]*B[1][0]
  if min(1-dt,1-tr+dt,1+tr+dt)<=0 or step(f,0)!=f:continue
  for k in range(13):
   poly=hull(orbit[k:k+9]+[f])
   if len(poly)<3:continue
   if not all(all(z>=0 if mask[i] else z<=0 for i,z in enumerate(pre(x,0))) for x in poly):continue
   if not all(inside(poly,step(x,0)) for x in poly):continue
   if not inside(poly,orbit[k]):continue
   logit=sum(v[i]*f[i] for i in range(2))+c
   if (logit<=0 if r['prefix']==1 else logit>0):return True
 return False
for r in rows:
 assert prove(r),(r['seed'],r['epoch'])
 print('PASS exact invariant',r['seed'],r['epoch'],r['prefix'])
