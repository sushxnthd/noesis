from fractions import Fraction as F
from collections import deque
import json,sys
S=1024
def f(x):return F.from_float(float(x))
def floor(x):return x.numerator//x.denominator
def ceil(x):return -((-x.numerator)//x.denominator)
def clip(x):return max(-S,min(S,x))
def task(q,t):return 0 if t==2 else (1 if t==1 else q)
def run(row):
 p=row["params"];W=[[[f(x) for x in a] for a in m] for m in p["W"]];b=[[f(x) for x in a] for a in p["b"]];v=[f(x) for x in p["v"]];c=f(p["c"])
 start=(0,());h=(512,-512,256,128);boxes={start:(h,h)};todo=deque([start]);queued={start};steps=0
 while todo:
  q,s=state=todo.popleft();queued.remove(state)
  for t in range(3):
   steps+=1
   if steps>256*26*3:return {"status":"ABSTAIN","reason":"budget"}
   dest=(task(q,t),(s+(t,))[-2:]);lo,hi=boxes[state];L=[];U=[]
   for j in range(4):
    lower=b[t][j]*S;upper=lower
    for k in range(4):
     w=W[t][j][k];lower+=w*(lo[k] if w>=0 else hi[k]);upper+=w*(hi[k] if w>=0 else lo[k])
    L.append(clip(floor(lower)));U.append(clip(ceil(upper)))
   old=boxes.get(dest)
   new=(tuple(L),tuple(U)) if old is None else (tuple(min(x,y) for x,y in zip(old[0],L)),tuple(max(x,y) for x,y in zip(old[1],U)))
   if new!=old:
    boxes[dest]=new
    if dest not in queued:todo.append(dest);queued.add(dest)
 for (q,s),(lo,hi) in boxes.items():
  if not s:continue
  lower=c*S;upper=lower
  for k in range(4):
   lower+=v[k]*(lo[k] if v[k]>=0 else hi[k]);upper+=v[k]*(hi[k] if v[k]>=0 else lo[k])
  if (q==1 and lower<=0) or (q==0 and upper>=0):return {"status":"ABSTAIN","reason":"readout_overlap","cells":len(boxes),"transitions":steps}
 return {"status":"CERTIFIED","reason":"inductive_box","cells":len(boxes),"transitions":steps,"certificate":{"grid_scale":S,"cells":[{"q":q,"suffix":list(s),"lo":list(lo),"hi":list(hi)} for (q,s),(lo,hi) in sorted(boxes.items())]}}
if __name__=="__main__":
 d=json.load(open(sys.argv[1]));out=[{"seed":r["seed"],**run(r)} for r in d["rows"] if r["epoch"]==200];json.dump(out,open(sys.argv[2],"w"),indent=2);print({k:sum(x["status"]==k for x in out) for k in ("CERTIFIED","ABSTAIN")})
