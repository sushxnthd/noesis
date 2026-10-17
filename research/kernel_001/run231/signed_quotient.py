"""NOESIS Run231 exact signed-coordinate relational quotient (tanh oddness).
Correctness of the reduced network requires an independently checked source
certificate; structural reduction alone is not a correctness certificate.
"""
from fractions import Fraction as Q
import json,sys,copy
F=lambda x:Q.from_float(float(x))
K=Q(1<<14);D=Q(1,8)
def source(rec):
 p=rec["row"]["params"]
 return dict(dim=len(p["v"]),W=[[[F(x) for x in r] for r in m] for m in p["W"]],b=[[F(x) for x in a] for a in p["b"]],v=[F(x) for x in p["v"]],c=F(p["c"]),h0=[Q(x) for x in rec["initial"]])
def augment(rec,shear=False):
 a=source(rec);d=a["dim"];W=[];b=[]
 for t in range(3):
  m=[r+[Q(0)] for r in a["W"][t]]+[[-x for x in a["W"][t][0]]+[Q(0)]]
  bt=a["b"][t]+[-a["b"][t][0]]
  if shear:
   for i in range(d+1):
    delta=D if i==0 else (-D if i==d else (D if i%2==0 else -D))
    m[i][0]+=delta;m[i][d]+=delta
  W.append(m);b.append(bt)
 return dict(dim=d+1,W=W,b=b,v=[a["v"][0]+K]+a["v"][1:]+[K],c=a["c"],h0=a["h0"]+[-a["h0"][0]])
def compatible(a,i,j,s):
 if a["h0"][j]!=s*a["h0"][i]:return False
 for t in range(3):
  m=a["W"][t]
  if a["b"][t][j]!=s*a["b"][t][i]:return False
  if any(m[j][k]!=s*m[i][k] for k in range(a["dim"]) if k not in (i,j)):return False
  if m[j][i]+s*m[j][j]!=s*(m[i][i]+s*m[i][j]):return False
 return True
def quotient(a,i,j,s):
 keep=[k for k in range(a["dim"]) if k!=j]
 return dict(dim=len(keep),W=[[[a["W"][t][r][c]+(s*a["W"][t][r][j] if c==i else 0) for c in keep] for r in keep] for t in range(3)],b=[[a["b"][t][r] for r in keep] for t in range(3)],v=[a["v"][c]+(s*a["v"][j] if c==i else 0) for c in keep],h0=[a["h0"][c] for c in keep],c=a["c"])
def discover(a):
 for i in range(a["dim"]):
  for j in range(i+1,a["dim"]):
   for s in (-1,1):
    if compatible(a,i,j,s):return (i,j,s,quotient(a,i,j,s))
 return None
def independent_audit(a,f):
 if f is None:return False
 i,j,s,q=f;keep=[x for x in range(a["dim"]) if x!=j]
 if a["h0"][j]!=s*a["h0"][i]:return False
 for t in range(3):
  for k in keep:
   left=a["W"][t][j][k]+(s*a["W"][t][j][j] if k==i else 0)
   right=s*(a["W"][t][i][k]+(s*a["W"][t][i][j] if k==i else 0))
   if left!=right:return False
  if a["b"][t][j]!=s*a["b"][t][i]:return False
  for r in keep:
   for k in keep:
    coeff=a["W"][t][r][k]+(s*a["W"][t][r][j] if k==i else 0)
    if coeff!=q["W"][t][keep.index(r)][keep.index(k)]:return False
 return q["v"]==[a["v"][k]+(s*a["v"][j] if k==i else 0) for k in keep]
def run(rec):
 records=[]
 for shear in (False,True):
  a=augment(rec,shear);f=discover(a)
  assert f is not None and f[2]==-1
  assert independent_audit(a,f) and f[3]==source(rec)
  records.append(dict(sheared=shear,pass_=True,pair=list(f[:3])))
 a=augment(rec,True);d=a["dim"]-1
 for kind in ("row","bias","initial"):
  z=copy.deepcopy(a)
  if kind=="row":z["W"][0][d][1]+=D
  if kind=="bias":z["b"][0][d]+=D
  if kind=="initial":z["h0"][d]+=D
  assert discover(z) is None,kind
 return records
if __name__=="__main__":
 rec=json.load(open(sys.argv[1] if len(sys.argv)>1 else "representative.json"))
 print(json.dumps({"status":"PASS","checkpoint":rec["id"],"transforms":run(rec),"claim":"exact signed relation, conditional source certificate"}))
