import json,sys
from fractions import Fraction as Q
from pathlib import Path
rows=json.loads(Path(sys.argv[1]).read_text())["rows"]
def ranks(a):
 ix=sorted(range(len(a)),key=lambda i:a[i]);r=[None]*len(a);i=0
 while i<len(ix):
  j=i+1
  while j<len(ix) and a[ix[j]]==a[ix[i]]:j+=1
  for k in range(i,j):r[ix[k]]=Q(i+j+1,2)
  i=j
 return r
def auc(y,r):
 p=sum(y);n=len(y)-p
 return (sum((r[i] for i in range(len(y)) if y[i]),Q(0))-Q(p*(p+1),2))/(p*n)
for split in ("dev","heldout"):
 group=[r for r in rows if r["split"]==split and r["outcome"]!="unresolved"]
 y=[int(r["outcome"]=="certified") for r in group]
 a=auc(y,ranks([r["score"] for r in group]));b=auc(y,ranks([r["loss"] for r in group]))
 print(split,len(group),sum(y),str(a),str(b),str(a-b))
