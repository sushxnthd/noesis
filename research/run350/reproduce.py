"""Run350 frozen 28-intervention scan; exact proof for accepted separators."""
import json,sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run349'))
from wordgen import generate
from verify_witness import states
p82=json.loads((P.parent/'run349/checkpoint_32135_82.json').read_text())['p']
p83=json.loads((P.parent/'run349/checkpoint_32135_83.json').read_text())['p']
W=generate(23);sg=np.array([2*(w.count('1')%2)-1 for w in W])
def scan(p):
 A=np.array(p[:18]).reshape(2,3,3);b=np.array(p[18:24]).reshape(2,3)
 c={'':np.zeros(3)}
 for w in W:
  for k in range(1,len(w)+1):
   z=w[:k]
   if z not in c:c[z]=np.maximum(A[int(z[-1])]@c[z[:-1]]+b[int(z[-1])],0)
 H=np.array([c[w] for w in W]);scale=np.maximum(abs(H).max(axis=0),1.)
 V=np.column_stack((H/scale,np.ones(len(W))))
 lp=linprog(np.zeros(4),A_ub=-sg[:,None]*V,b_ub=-np.ones(len(W)),bounds=[(None,None)]*4,method='highs')
 if not lp.success:return False
 co=[Q.from_float(float(z)) for z in lp.x[:3]/scale];bias=Q.from_float(float(lp.x[3]))
 for w,s,h in zip(W,sg,states(p,W)):
  margin=int(s)*(sum(co[j]*Q(int(h[j].p),int(h[j].q)) for j in range(3))+bias)
  if margin<=0:return False
 return True
def main():
 assert len(W)==2644
 candidates=[('base82',[]),('endpoint83',list(range(24)))]
 candidates += [('coord_%02d'%i,[i]) for i in range(24)]
 candidates += [('block_'+name,list(range(a,b))) for name,a,b in [('A0',0,9),('A1',9,18),('b0',18,21),('b1',21,24)]]
 out=[]
 for name,ids in candidates:
  p=p82.copy()
  for i in ids:p[i]=p83[i]
  out.append({'name':name,'indices':ids,'exact_separator':scan(p)})
 positives=[r['name'] for r in out if r['exact_separator']]
 assert positives==['endpoint83','coord_18','block_b0'],positives
 (P/'reproduction_results.json').write_text(json.dumps(out,indent=2)+'\n')
 print('FROZEN S=1; positives:',positives)
if __name__=='__main__':main()
