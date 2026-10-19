"""Independent minimal exact reproducer for seven finite-perfect Run263 checkpoints."""
import json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
Q=lambda x:F.from_float(float(x))
def cert(p):
 A=[[Q(x) for x in row] for row in p['A']]
 e=[Q(p['E'][0][i])+Q(p['b'][i]) for i in range(2)]
 v=[Q(x) for x in p['v']];c=Q(p['c'])
 pre=lambda x:[sum(A[i][j]*x[j] for j in range(2))+e[i] for i in range(2)]
 step=lambda x:tuple(max(F(0),z) for z in pre(x))
 orbit=[(F(0),F(0))]
 for _ in range(24):orbit.append(step(orbit[-1]))
 for mask in ((0,0),(0,1),(1,0),(1,1)):
  B=[[mask[i]*A[i][j] for j in range(2)] for i in range(2)]
  b=[mask[i]*e[i] for i in range(2)]
  d=(1-B[0][0])*(1-B[1][1])-B[0][1]*B[1][0]
  if d==0:continue
  f=(((1-B[1][1])*b[0]+B[0][1]*b[1])/d, (B[1][0]*b[0]+(1-B[0][0])*b[1])/d)
  tr=B[0][0]+B[1][1];dt=B[0][0]*B[1][1]-B[0][1]*B[1][0]
  if min(1-dt,1-tr+dt,1+tr+dt)<=0:continue
  z=sum(v[i]*f[i] for i in range(2))+c
  if z<=0:continue
  def signs(x):return all((a>=0 if m else a<=0) for a,m in zip(pre(x),mask))
  def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
  def hull(points):
   pts=sorted(set(points));low=[];high=[]
   for x in pts:
    while len(low)>1 and cross(low[-2],low[-1],x)<=0:low.pop()
    low.append(x)
   for x in reversed(pts):
    while len(high)>1 and cross(high[-2],high[-1],x)<=0:high.pop()
    high.append(x)
   return low[:-1]+high[:-1]
  def contains(poly,x):
   if len(poly)==1:return x==poly[0]
   if len(poly)==2:return cross(poly[0],poly[1],x)==0 and all(min(a,b)<=q<=max(a,b) for a,b,q in zip(poly[0],poly[1],x))
   return all(cross(poly[i],poly[(i+1)%len(poly)],x)>=0 for i in range(len(poly)))
  for k in range(17):
   poly=hull(orbit[k:k+9]+[f])
   if all(signs(x) for x in poly) and all(contains(poly,step(x)) for x in poly) and contains(poly,orbit[k]) and step(f)==f:
    return ('polygon',k,pre,step,v,c)
  C=[[abs(B[i][j]) for j in range(2)] for i in range(2)]
  dc=(1-C[0][0])*(1-C[1][1])-C[0][1]*C[1][0]
  if dc<=0:continue
  w=[((1-C[1][1])+C[0][1])/dc,(C[1][0]+(1-C[0][0]))/dc]
  if min(w)<=0 or not all(sum(C[i][j]*w[j] for j in range(2))<w[i] for i in range(2)):continue
  for k,h in enumerate(orbit[:17]):
   scale=max(abs(h[i]-f[i])/w[i] for i in range(2));rad=[scale*w[i] for i in range(2)]
   corners=[(f[0]+a*rad[0],f[1]+b*rad[1]) for a in (-1,1) for b in (-1,1)]
   if all(signs(x) for x in corners):return ('box',k,pre,step,v,c)
 return None
def main():
 rows=json.loads((P/'SEVEN_CHECKPOINTS.json').read_text())
 expected={18305:48,18307:45,18310:72,18314:399,18321:400,18325:39,18327:45}
 assert set(x['seed'] for x in rows)==set(expected)
 for row in rows:
  seed=row['seed'];r=cert(row['params']);assert r is not None,seed
  kind,k,pre,step,v,c=r
  h=(F(0),F(0));first=None
  for n in range(1,401):
   h=step(h)
   if sum(v[i]*h[i] for i in range(2))+c>0:first=n;break
  assert first==expected[seed],(seed,first,expected[seed])
  print('PASS',seed,'invariant',kind,'k',k,'exact_first',first)
 print('ALL 7 EXACT CERTIFICATES AND WITNESSES VERIFIED')
if __name__=='__main__':main()
