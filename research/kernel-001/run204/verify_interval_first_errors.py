"""Exact-binary64 outward-interval all-word checker; no floating-point decisions."""
import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/"run203"))
from proof203_core import iv,q,step,cls
SHA="5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32"
def run():
 source=R/"CHECKPOINTS.json"
 assert hashlib.sha256(source.read_bytes()).hexdigest()==SHA
 rows=json.loads(source.read_text())["rows"];out=[]
 for epoch,limit,witness in ((400,8,"11100010"),(800,9,"110100010")):
  raw=next(x["params"] for x in rows if (x["seed"],x["epoch"])==(307,epoch))
  p={k:([[q(v) for v in a] for a in raw[k]] if k in ("W","U","V") else [q(v) for v in raw[k]]) for k in ("W","U","V","b","c")}
  states=[([iv.mpf(0)]*12,"")];counts=[]
  for n in range(1,limit+1):
   nxt=[];bad=[]
   for h,w in states:
    for a in "01":
     ww=w+a;hh=step(h,p,int(a));label=cls(hh,p)
     if label!=ww.count("1")%3:bad.append((ww,label))
     nxt.append((hh,ww))
   counts.append({"length":n,"count":len(nxt),"errors":len(bad),"witnesses":bad})
   states=nxt
   print("interval",epoch,n,"checked",len(nxt),"errors",len(bad),flush=True)
  assert all(x["errors"]==0 for x in counts[:-1])
  assert counts[-1]["witnesses"]==[(witness,2)]
  out.append({"epoch":epoch,"L":limit,"verified_words":sum(x["count"] for x in counts),"counts":counts,"status":"PASS"})
 return out
if __name__=="__main__":print(json.dumps(run(),indent=2))
