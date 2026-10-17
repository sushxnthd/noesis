"""Independent stdlib-only directed-Decimal verification of trained RNN transition."""
import json
from pathlib import Path
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING,localcontext
P=90;F=Context(prec=P,rounding=ROUND_FLOOR);C=Context(prec=P,rounding=ROUND_CEILING)
class I:
 def __init__(self,a,b=None):
  self.a=Decimal(a);self.b=Decimal(b) if b is not None else self.a
  assert self.a<=self.b
 def __add__(self,y):
  y=asI(y);return I(F.add(self.a,y.a),C.add(self.b,y.b))
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __mul__(self,y):
  y=asI(y);xs=[F.multiply(a,b) for a in (self.a,self.b) for b in (y.a,y.b)];ys=[C.multiply(a,b) for a in (self.a,self.b) for b in (y.a,y.b)]
  return I(min(xs),max(ys))
 __rmul__=__mul__
 def __truediv__(self,y):
  y=asI(y);assert y.a>0 or y.b<0
  return I(min(F.divide(a,b) for a in (self.a,self.b) for b in (y.a,y.b)),max(C.divide(a,b) for a in (self.a,self.b) for b in (y.a,y.b)))
def asI(x):return x if isinstance(x,I) else I(x)
def exact(x):
 n,d=float(x).as_integer_ratio();return I(F.divide(Decimal(n),Decimal(d)),C.divide(Decimal(n),Decimal(d)))
def exppt(x):
 with localcontext(Context(prec=P)):
  z=x.exp()
 ulp=Decimal(2).scaleb(z.adjusted()-P+1)
 return I(F.subtract(z,ulp),C.add(z,ulp))
def tanh(x):
 a=exppt(F.multiply(Decimal(2),x.a));b=exppt(C.multiply(Decimal(2),x.b))
 def frac(e):return (e+I(-1))/(e+I(1))
 return I(frac(a).a,frac(b).b)
R=Path(__file__).resolve().parent
rows={r['epoch']:r for r in json.loads((R/'CHECKPOINTS.json').read_text())['rows']}
cert=json.loads((R/'CERTIFICATE.json').read_text())
def model(row):
 p=row['params'];W=[[[exact(x) for x in r] for r in M] for M in p['W']];b=[[exact(x) for x in r] for r in p['b']];v=[exact(x) for x in p['v']];c=exact(p['c'])
 def step(h,t):return [tanh(sum((W[t][j][i]*h[i] for i in range(3)),I(0))+b[t][j]) for j in range(3)]
 def logit(h):return sum((v[j]*h[j] for j in range(3)),c)
 return step,logit
def verify():
 step,logit=model(rows[100]);boxes={}
 for key,rec in cert['boxes'].items():
  q,s=key.split(':');boxes[(int(q),s)]=[I(rec['lo'][j],rec['hi'][j]) for j in range(3)]
 assert len(boxes)==5 and cert['k']==1
 def good(q,h):
  z=logit(h);return z.a>0 if q else z.b<0
 for t in range(3):
  h=step([I('.5'),I('-.5'),I('.25')],t);q=int(t==1);box=boxes[(q,str(t))]
  assert good(q,h)
  assert all(h[j].a>=box[j].a and h[j].b<=box[j].b for j in range(3))
 for (q,s),h in boxes.items():
  assert good(q,h)
  for t in range(3):
   qq=0 if t==2 else q^(t==1);dest=boxes[(qq,str(t))];nh=step(h,t)
   assert all(nh[j].a>=dest[j].a and nh[j].b<=dest[j].b for j in range(3))
 step,logit=model(rows[50]);h=[I('.5'),I('-.5'),I('.25')]
 for t in (1,1):h=step(h,t)
 assert logit(h).a>0
 return True
if __name__=='__main__':
 assert verify();print('PASS independent Decimal all-length and epoch50 witness')
