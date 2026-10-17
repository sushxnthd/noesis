import json
from pathlib import Path
from decimal_lib import I,exact,tanh
p=json.loads((Path(__file__).parent/"SEED1429_E200.json").read_text())["params"]
W=[[[exact(x) for x in row] for row in mat] for mat in p["W"]]
b=[[exact(x) for x in row] for row in p["b"]]
v=[exact(x) for x in p["v"]];c=exact(p["c"])
frontier=[([I(".5"),I("-.5"),I(".25")],0,"")]
counts=[];all_wrong=[]
for length in range(1,9):
 new=[];good=0;wrong=[];unknown=[]
 for h,q,word in frontier:
  for t in range(3):
   hh=[tanh(sum((W[t][j][k]*h[k] for k in range(3)),I(0))+b[t][j]) for j in range(3)]
   qq=0 if t==2 else q^(t==1)
   z=sum((v[k]*hh[k] for k in range(3)),c);w=word+str(t)
   if (z.lo>0 if qq else z.hi<0):good+=1
   elif (z.hi<0 if qq else z.lo>0):wrong.append(w)
   else:unknown.append(w)
   new.append((hh,qq,w))
 counts.append(dict(length=length,correct=good,wrong=len(wrong),unknown=len(unknown)))
 all_wrong.extend(wrong)
 assert not unknown,(length,unknown[:3])
 frontier=new
assert all_wrong==["20011100","20011101"],all_wrong
assert all(x["wrong"]==0 for x in counts[:7])
print(json.dumps(dict(checker="decimal",counts=counts,wrong=all_wrong)))
