import json
from pathlib import Path
import sympy as S
Z=S.Integer(0)
def image(a,b,lo,hi):
 if hi==S.oo:
  if a>0:return max(Z,a*lo+b),S.oo
  if a<0:return Z,max(Z,a*lo+b)
  return max(Z,b),max(Z,b)
 t=[max(Z,a*lo+b),max(Z,a*hi+b)]
 return min(t),max(t)
def verify(p):
 a,b,v,c=p[:3],p[3:6],p[6],p[7];L=max(Z,b[2]);U=b[1]
 if not(v>0 and U>L and v*L+c<0 and v*U+c>0):return False
 regions=[(Z,L),(U,S.oo)]
 for state,source in enumerate(regions):
  for sym,dest in enumerate(((0,1,0),(1,1,0))[state]):
   lo,hi=image(a[sym],b[sym],*source)
   low,high=regions[dest]
   if not(lo>=low and hi<=high):return False
 return True
if __name__=='__main__':
 data=json.loads((Path(__file__).parent/'derived_results.json').read_text())
 for r in data['models']:
  assert not verify([S.Rational(x) for x in r['original']])
  assert verify([S.Rational(x) for x in r['repaired']])
  assert verify([S.Rational(x) for x in r['dyadic']])
 print('Independent SymPy: 11/11 repairs, 11/11 dyadic, 11/11 negative controls PASS')
