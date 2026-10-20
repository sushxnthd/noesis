#!/usr/bin/env python3
"""NOESIS Run299: exact dyadic all-word latch certificates on trained Run297 networks."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parent
SHA="620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473"
LATE={21800:"0"*15,21864:"0"*24,21881:"1"+"0"*12,21885:"1"+"0"*36}
def unpack(p):
 z=list(map(F.from_float,p));assert len(z)==28
 A=[[[z[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
 b=[[z[18+3*x+i] for i in range(3)] for x in (0,1)]
 return A,b,z[24:27],z[27]
def candidate(p):
 A,b,v,c=unpack(p)
 if c>=0 or any(t>0 for t in b[0]) or any(t<0 for t in v) or not any(v):return None
 init=sum(v[i]*max(F(0),b[1][i]) for i in range(3))
 mu=[];beta=[]
 for x in (0,1):
  q=[sum(v[i]*A[x][i][j] for i in range(3)) for j in range(3)]
  if any(v[j]==0 and q[j]<0 for j in range(3)):return None
  m=min(q[j]/v[j] for j in range(3) if v[j]>0)
  if m<0:return None
  mu.append(m);beta.append(sum(v[i]*b[x][i] for i in range(3)))
 for k in range(1,65):
  T=F(k,4)
  if T+c>0 and init>=T and all((mu[x]-1)*T+beta[x]>=0 for x in (0,1)):
   return {"T":str(T),"mu":[str(z) for z in mu],
           "initial_margin":str(init-T),"output_margin":str(T+c),
           "transition_margins":[str((mu[x]-1)*T+beta[x]) for x in (0,1)]}
 return None
def independent(p,cert):
 if cert is None:return False
 z=list(map(F.from_float,p));v=z[24:27];c=z[27];T=F(cert["T"]);mu=list(map(F,cert["mu"]))
 if not(T>0 and c<0 and T+c>0 and all(w>=0 for w in v) and any(v)):return False
 if any(z[18+i]>0 for i in range(3)):return False
 if sum(v[i]*max(F(0),z[21+i]) for i in range(3))<T:return False
 for x in (0,1):
  if mu[x]<0:return False
  for j in range(3):
   if sum(v[i]*z[9*x+3*i+j] for i in range(3))<mu[x]*v[j]:return False
  if mu[x]*T+sum(v[i]*z[18+3*x+i] for i in range(3))<T:return False
 return True
def wrong(p,word):
 A,b,v,c=unpack(p);h=[F(0)]*3;q=0
 for s in word:
  x=int(s);q|=x
  h=[max(F(0),sum(A[x][i][j]*h[j] for j in range(3))+b[x][i]) for i in range(3)]
  if (sum(v[i]*h[i] for i in range(3))+c>0)!=bool(q):return True
 return False
def main():
 raw=Path(sys.argv[1]).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
 prev=json.loads(Path(sys.argv[2]).read_text());data=json.loads(raw)
 by={r["seed"]:r for r in data["rows"] if r["epoch"]==80}
 assert len(by)==len(prev)==128
 unresolved={r["seed"] for r in prev if r["outcome"]=="unresolved"}
 assert len(unresolved)==58 and set(LATE)<=unresolved
 for s,w in LATE.items():assert wrong(by[s]["p"],w)
 cohort=sorted(unresolved-set(LATE));assert len(cohort)==54
 assert all(by[s]["accuracy"]==1.0 for s in cohort)
 known=[r for r in prev if r["outcome"]=="incorrect"];assert len(known)==70
 for r in known:assert wrong(by[r["seed"]]["p"],r["witness"])
 out=[]
 for s in cohort:
  cert=candidate(by[s]["p"])
  if cert:assert independent(by[s]["p"],cert),s
  out.append({"seed":s,"cert":cert,"status":"certified" if cert else "unresolved"})
 accepted=[r["seed"] for r in out if r["cert"]]
 assert accepted==[21832,21903,21926],accepted
 assert all(candidate(by[s]["p"]) is None for s in [r["seed"] for r in known]+list(LATE))
 base=list(by[21832]["p"]);cert=next(r["cert"] for r in out if r["seed"]==21832)
 mutations=[]
 p=base.copy();p[18]=0.1;mutations.append((p,cert))
 p=base.copy();p[27]=0.1;mutations.append((p,cert))
 p=base.copy();p[24]=-abs(p[24]);mutations.append((p,cert))
 c=dict(cert);c["T"]="1/1000";mutations.append((base,c))
 c=dict(cert);c["mu"]=["100","100"];mutations.append((base,c))
 assert all(not independent(p,c) for p,c in mutations)
 result={"run":299,"cohort":54,"certified":3,"seeds":accepted,"nonpilot":1,
         "still_unresolved":51,"known_wrong_rejected":74,"mutations_rejected":5,
         "frozen_success":True,"checkpoint_sha256":SHA}
 (P/"rows299_public.json").write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
 (P/"results299_public.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
 (P/"certified_checkpoints299.json").write_text(json.dumps({str(s):by[s] for s in accepted},sort_keys=True,indent=2)+"\n")
 print("RUN299_PUBLIC",json.dumps(result,sort_keys=True),flush=True)
if __name__=="__main__":main()
