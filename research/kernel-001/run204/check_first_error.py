"""Independent direct-word numerical first-error screen; not an interval proof."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[1]
SHA="5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32"
def predict(word,p):
 h=[0.0]*len(p["b"])
 for a in word:
  h=[math.tanh(sum(w*v for w,v in zip(row,h))+p["U"][int(a)][i]+p["b"][i]) for i,row in enumerate(p["W"])]
 z=[sum(w*v for w,v in zip(row,h))+p["c"][i] for i,row in enumerate(p["V"])]
 return max(range(3),key=lambda i:z[i])
def run():
 source=R/"CHECKPOINTS.json"
 assert hashlib.sha256(source.read_bytes()).hexdigest()==SHA
 rows=json.loads(source.read_text())["rows"];out=[]
 for epoch,D in ((400,7),(800,8)):
  p=next(x["params"] for x in rows if (x["seed"],x["epoch"])==(307,epoch))
  counts=[]
  for n in range(1,10):
   bad=[format(i,f"0{n}b") for i in range(1<<n) if predict(format(i,f"0{n}b"),p)!=int(i).bit_count()%3]
   counts.append({"length":n,"errors":len(bad),"first":bad[0] if bad else None})
   if bad:break
  L=counts[-1]["length"]
  assert L==D+1 and counts[-1]["errors"]==1
  out.append({"epoch":epoch,"L":L,"D":D,"counts":counts})
 return out
if __name__=="__main__":print(json.dumps(run(),indent=2))
