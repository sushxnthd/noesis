"""Run 192: exhaustive interval check, exact binary64 weights, all prefixes <=12."""
import json
from pathlib import Path
from fractions import Fraction
from mpmath import iv
R=Path(__file__).resolve().parent
iv.dps=60
def exact(x):
 f=Fraction.from_float(float(x));return iv.mpf(f.numerator)/iv.mpf(f.denominator)
def load(epoch):
 path=R/("seed163_epoch600_params.json" if epoch==600 else "../run191/seed163_epoch300_params.json")
 def cv(x):return [cv(y) for y in x] if isinstance(x,list) else exact(x)
 return {k:cv(v) for k,v in json.loads(path.read_text()).items()}
def dot(a,b):return sum((x*y for x,y in zip(a,b)),iv.mpf(0))
def step(h,p,bit):
 return [1-2/(1+iv.exp(2*(dot(p["W"][i],h)+p["U"][bit][i]+p["b"][i]))) for i in range(8)]
def output(h,p):return dot(p["v"],h)+p["c"]
def check():
 p,q=load(300),load(600);states=[([iv.mpf(0)]*8,[iv.mpf(0)]*8)];n=0;minimum=1e9
 for depth in range(1,13):
  nxt=[]
  for a,b in states:
   for bit in (0,1):
    x=step(a,p,bit);y=step(b,q,bit);u=output(x,p);v=output(y,q)
    su=1 if u.a>0 else -1 if u.b<0 else 0
    sv=1 if v.a>0 else -1 if v.b<0 else 0
    assert su!=0 and su==sv,("mismatch",depth,bit)
    minimum=min(minimum,float(abs(u).a),float(abs(v).a))
    nxt.append((x,y));n+=1
  states=nxt
 assert n==8190
 result={"proved":True,"prefixes":n,"disagreements":0,"minimum_abs_logit_lower":minimum}
 print(json.dumps(result));return result
if __name__=="__main__":check()
