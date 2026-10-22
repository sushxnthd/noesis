"""Run332 exact-rank AUROC and sharp missing-label bounds. Usage: python audit332.py scores332.json"""
import json,sys
from fractions import Fraction as F
rows=json.load(open(sys.argv[1]))['rows']
def ranks(v):
 ix=sorted(range(len(v)),key=lambda i:v[i]);r=[None]*len(v);i=0
 while i<len(ix):
  j=i+1
  while j<len(ix) and v[ix[j]]==v[ix[i]]:j+=1
  for k in range(i,j):r[ix[k]]=F(i+1+j,2)
  i=j
 return r
def auc(y,r):
 p=sum(y);q=len(y)-p
 return (sum((r[i] for i in range(len(y)) if y[i]),F(0))-F(p*(p+1),2))/(p*q)
for split in ('dev','heldout'):
 a=[x for x in rows if x['split']==split];known=[x for x in a if x['outcome']!='unresolved'];y=[int(x['outcome']=='certified') for x in known]
 s=auc(y,ranks([x['score'] for x in known]));l=auc(y,ranks([x['loss'] for x in known]))
 pos=[i for i,x in enumerate(a) if x['outcome']=='certified'];unk=[i for i,x in enumerate(a) if x['outcome']=='unresolved']
 d=[x-z for x,z in zip(ranks([x['score'] for x in a]),ranks([x['loss'] for x in a]))];fixed=sum((d[i] for i in pos),F(0))
 ext=[]
 for maximize in (False,True):
  ix=sorted(unk,key=lambda i:(d[i],a[i]['seed']),reverse=maximize);v=fixed;best=None
  for k in range(len(ix)+1):
   n=len(pos)+k;value=v/(n*(len(a)-n))
   if best is None or (value>best[0] if maximize else value<best[0]):best=(value,k)
   if k<len(ix):v+=d[ix[k]]
  ext.append([str(best[0]),float(best[0]),best[1]])
 print(json.dumps({'split':split,'known':len(known),'positive':sum(y),'negative':len(known)-sum(y),'unresolved':len(a)-len(known),'auc_g64':float(s),'auc_loss':float(l),'delta_exact':str(s-l),'delta':float(s-l),'lower':ext[0],'upper':ext[1]},sort_keys=True))
