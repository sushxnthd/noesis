import json,sys
S=1024
def check(row,cert):
 p=row["params"]
 xs=[x for m in p["W"] for a in m for x in a]+[x for a in p["b"] for x in a]+p["v"]+[p["c"]]
 D=max(float(x).as_integer_ratio()[1] for x in xs)
 def toint(x):
  n,d=float(x).as_integer_ratio();assert D%d==0;return n*(D//d)
 W=[[[toint(x) for x in a] for a in m] for m in p["W"]]
 b=[[toint(x) for x in a] for a in p["b"]];v=[toint(x) for x in p["v"]];c=toint(p["c"])
 assert cert["grid_scale"]==S
 B={}
 for x in cert["cells"]:
  key=(x["q"],tuple(x["suffix"]))
  assert key not in B
  lo=tuple(x["lo"]);hi=tuple(x["hi"])
  assert len(lo)==len(hi)==4 and all(-S<=a<=z<=S for a,z in zip(lo,hi))
  B[key]=(lo,hi)
 assert (0,()) in B
 l,u=B[(0,())];assert all(l[i]<=h<=u[i] for i,h in enumerate((512,-512,256,128)))
 for (q,s),(l,u) in B.items():
  if s:
   zl=c*S;zu=zl
   for k in range(4):
    a=v[k];zl+=a*(l[k] if a>=0 else u[k]);zu+=a*(u[k] if a>=0 else l[k])
   assert (zl>0 if q else zu<0)
  for t in range(3):
   qq=0 if t==2 else (1-q if t==1 else q);key=(qq,(s+(t,))[-2:]);assert key in B
   dl,du=B[key]
   for j in range(4):
    low=b[t][j]*S;up=low
    for k in range(4):
     a=W[t][j][k];low+=a*(l[k] if a>=0 else u[k]);up+=a*(u[k] if a>=0 else l[k])
    low=max(-S*D,min(S*D,low));up=max(-S*D,min(S*D,up))
    assert dl[j]*D<=low and up<=du[j]*D
 return True
if __name__=="__main__":
 rows={r["seed"]:r for r in json.load(open(sys.argv[1]))["rows"] if r["epoch"]==200}
 certs=[r for r in json.load(open(sys.argv[2])) if r["status"]=="CERTIFIED"]
 for r in certs:assert check(rows[r["seed"]],r["certificate"])
 print("PASS",len(certs))
