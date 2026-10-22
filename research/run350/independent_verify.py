"""Independent Fraction/SymPy verifier of causal repair and infinite spoof."""
import json,sys
from pathlib import Path
from fractions import Fraction as Q
import sympy as S
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run349'))
from wordgen import generate
p82=json.loads((P.parent/'run349/checkpoint_32135_82.json').read_text())['p']
p83=json.loads((P.parent/'run349/checkpoint_32135_83.json').read_text())['p']
one=p82.copy();one[18]=p83[18]
def states(p,ws):
 p=[Q.from_float(float(z)) for z in p];c={'':(Q(0),Q(0),Q(0))}
 def h(w):
  if w not in c:
   z=h(w[:-1]);x=int(w[-1])
   c[w]=tuple(max(Q(0),sum((p[9*x+3*i+j]*z[j] for j in range(3)),p[18+3*x+i])) for i in range(3))
  return c[w]
 return [h(w) for w in ws]
def count(p,ws):
 q=[Q.from_float(float(z)) for z in p]
 return sum((2*(w.count('1')%2)-1)*sum((q[24+i]*h[i] for i in range(3)),q[27])>0
            for w,h in zip(ws,states(p,ws)))
def main():
 W=generate(23);W25=generate(25)
 assert len(W)==2644 and len(W25)==2766
 assert [count(p,W) for p in (p82,one,p83)]==[2556,2644,2623]
 assert count(one,W25)==2766
 ww=['00000000000000000000010','00000000000000000000011',
     '00000000000000000000111','10100000000000000000000']
 H=states(p82,ww);a,c,b,d=H[0][0],H[2][1],H[3][0],H[1][1]
 assert 0<a<b and 0<d<c
 assert H[0][1:]==H[3][1:]==(0,0)
 assert H[1][0]==H[1][2]==H[2][0]==H[2][2]==0
 det=Q(1,a)*Q(1,d)-Q(1,b)*Q(1,c)
 x=(Q(1,d)-Q(1,c))/det;y=(Q(1,a)-Q(1,b))/det
 assert 0<x<min(a,b) and 0<y<min(c,d)
 q=[Q.from_float(float(z)) for z in one]
 w='101'+'0'*23;h=states(one,[w])[0];x0=h[0]
 alpha=q[0];beta=q[18];fixed=beta/(1-alpha)
 assert h[1:]==(0,0) and 0<alpha<1 and 0<x0<fixed
 assert all(q[3*i]<0 and q[18+i]<0 for i in (1,2))
 assert q[24]>0 and q[24]*x0+q[27]>0
 r=lambda z:S.Rational(z.numerator,z.denominator)
 assert r(q[24])*r(x0)+r(q[27])>0 and r(alpha)<1 and r(x0)<r(fixed)
 print('PASS: exact original-head 2766/2766 through L25; infinite failures 1010^n for n>=23')
if __name__=='__main__':main()
