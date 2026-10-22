#!/usr/bin/env python3
"""Exact trained-RNN readout horizon and one-step representation-collapse proof (stdlib only)."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
P=Path(__file__).resolve().parent
m=json.loads((P/'model344.json').read_text())
old=json.loads((P.parent/'run343/model343.json').read_text())
assert m['seed']==old['seed']==31089 and len(old['p'])==45
assert m['source_sha256']=='c20f44b3bd56893880974c638b6202ad75a5ea253b64f72eeaa094e8d973112e'
W=['1','100000000000000','11001000000100','100000000000001','100000000000010']
Y=[w.count('1')%2 for w in W]
assert Y==[1,1,0,0,0]

def network(params):
 p=[Q.from_float(float(x)) for x in params]
 A=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
 b=[p[32+4*x:36+4*x] for x in (0,1)]
 def step(h,x):return tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(4)),b[x][i])) for i in range(4))
 def logit(h):return sum((p[40+j]*h[j] for j in range(4)),p[44])
 return step,logit

def states_of_words(step):
 out=[]
 for w in W:
  h=(Q(0),)*4
  for x in w:h=step(h,int(x))
  out.append(h)
 return out

def exact_enumerate(step,readout,limit):
 h=[(Q(0),)*4];count=0;minmargin=None
 for length in range(1,limit+1):
  h=[step(z,x) for z in h for x in (0,1)]
  for j,z in enumerate(h):
   s=readout(z)
   margin=s if j.bit_count()%2 else -s
   assert margin>0,(length,j,float(margin))
   if minmargin is None or margin<minmargin:minmargin=margin
  count+=len(h)
 return count,minmargin

def solve_exact(M,b):
 n=len(b);T=[[Q(z) for z in row]+[Q(b[i])] for i,row in enumerate(M)]
 for col in range(n):
  k=next((r for r in range(col,n) if T[r][col]),None)
  assert k is not None,'singular witness matrix'
  T[col],T[k]=T[k],T[col]
  q=T[col][col];T[col]=[z/q for z in T[col]]
  for r in range(n):
   if r!=col and T[r][col]:
    q=T[r][col];T[r]=[T[r][j]-q*T[col][j] for j in range(n+1)]
 return [T[i][-1] for i in range(n)]

def hull_witness(H):
 M=[[int(i<2) for i in range(5)],[int(i>=2) for i in range(5)]]
 for j in (0,1,3):M.append([H[i][j]*(1 if i<2 else -1) for i in range(5)])
 q=solve_exact(M,[1,1,0,0,0])
 assert all(z>0 for z in q)
 assert sum(q[:2])==sum(q[2:])==1
 for j in range(4):assert sum((q[i]*H[i][j]*(1 if i<2 else -1) for i in range(5)),Q(0))==0
 return q

def obj(z):return {'num':str(z.numerator),'den':str(z.denominator)}

proof={'words':W,'labels':Y,'original_trajectories_sha256':m['source_sha256'],'epochs':{}}
summary={'seed':31089,'epochs':{},'exact_semantics':'binary64 weights interpreted as dyadic rationals'}
for epoch in (140,141,200):
 p=m['epochs'][str(epoch)]['p'] if epoch!=200 else old['p']
 step,logit=network(p);H=states_of_words(step)
 summary['epochs'][str(epoch)]={}
 if epoch in (140,141):
  count,margin=exact_enumerate(step,logit,12)
  assert count==8190 and m['epochs'][str(epoch)]['accuracy']==1.
  summary['epochs'][str(epoch)]={'original_correct_through_12':count,'original_min_margin':float(margin),'train_bce':m['epochs'][str(epoch)]['bce']}
 if epoch==140:
  v=[Q(-11433659925499,250000000000),Q(-631738902161,500000000000),Q(0),Q(192206955691,40000000000),Q(12012218623103,250000000000)]
  margins=[sum((v[j]*h[j] for j in range(4)),v[4])*(1 if y else -1) for h,y in zip(H,Y)]
  assert min(margins)>0
  proof['epochs']['140']={'kind':'strict_affine_separator','readout':list(map(obj,v))}
  summary['epochs']['140']['strict_five_word_repairable']=True
 else:
  q=hull_witness(H)
  proof['epochs'][str(epoch)]={'kind':'convex_hull_intersection','weights':list(map(obj,q))}
  summary['epochs'][str(epoch)]['five_word_affine_repairable']=False
  summary['epochs'][str(epoch)]['irreducible_selected_support_size']=5
 if epoch==200:
  v=[Q(0),Q(0),Q(-6352381486487,1000000000000),Q(862353370801,1000000000000),Q(-1)]
  count,margin=exact_enumerate(step,lambda h:sum((v[j]*h[j] for j in range(4)),v[4]),14)
  assert count==32766 and margin>=1
  proof['epochs']['200']['length14_affine_readout']=list(map(obj,v))
  summary['epochs']['200'].update({'exact_repairable_through_14':count,'exact_unrepairable_by_length_15':True,'exact_minimum_margin_through_14':float(margin)})
assert m['epochs']['141']['bce']<m['epochs']['140']['bce']
payload=json.dumps(proof,sort_keys=True,separators=(',',':'))+'\n'
(P/'witness344.json').write_text(payload)
summary['witness_sha256']=hashlib.sha256(payload.encode()).hexdigest()
(P/'results344.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
