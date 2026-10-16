import sys
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/"run192"))
from verify_finite import load,step,output,iv
iv.dps=45
P=[load(300),load(600)]
Z=iv.mpf(0)
def sign(x):
 return 1 if x.a>0 else -1 if x.b<0 else 0
def verify():
 counts=[0]*18
 diffs=[[] for _ in range(18)]
 stack=[(0,[Z]*8,[Z]*8,0)]
 while stack:
  d,a,b,w=stack.pop()
  if d:
   u,v=output(a,P[0]),output(b,P[1])
   su,sv=sign(u),sign(v)
   assert su and sv,("uncertain",d,w)
   counts[d]+=1
   if su!=sv:
    diffs[d].append((format(w,f"0{d}b"),su,sv,str(u),str(v)))
  if d<17:
   for bit in (1,0):
    stack.append((d+1,step(a,P[0],bit),step(b,P[1],bit),w*2+bit))
 assert counts[1:]==[2**d for d in range(1,18)]
 assert all(not x for x in diffs[1:17])
 assert len(diffs[17])==2
 print({"first_separator_length":17,"counts":counts[1:],"witnesses":diffs[17]})
if __name__=="__main__":verify()
