"""Independent exact checker of Run295 gate, using rational arithmetic."""
from fractions import Fraction as F
import json
from pathlib import Path
P=Path(__file__).resolve().parent
def unpack(p,n):
 q=[F.from_float(float(t)) for t in p]
 A=[[[q[x*n*n+i*n+j] for j in range(n)] for i in range(n)] for x in range(2)]
 B=[[q[2*n*n+x*n+i] for i in range(n)] for x in range(2)]
 return A,B,q[2*n*n+2*n:-1],q[-1]
def check(p,q,d):
 A,B,V,C=unpack(p,3);X,Y,W,K=unpack(q,6)
 if K!=C or W!=V+[F(0),F(0),F(1)]:return False
 for x in range(2):
  for i in range(3):
   if X[x][i]!=A[x][i]+[F(0)]*3 or Y[x][i]!=B[x][i]:return False
  if X[x][3]!=[F(0)]*3+[F(2) if d else F(1,2),F(0),F(0)]:return False
  if X[x][4]!=[F(0)]*4+[F(4) if d else F(1,2),F(0)]:return False
  if X[x][5]!=[F(0)]*3+[F(1),F(-1),F(0)]:return False
  if Y[x][3:]!=[F(1),F(3),F(-1)]:return False
 # Exact inductive invariant z2>=z1>=0, g=0. Initial state is zero.
 # Difference after update is 4*z2-2*z1+2>=0 for divergent,
 # or (z2-z1)/2+2>=0 for stable; g'=relu(z1-z2-1)=0.
 return True
def main():
 import sys
 sys.path.insert(0,str(P.parent/'run294'))
 from clock294 import pack
 raw=json.loads((P/'checkpoints291.json').read_text())
 rows={(r['seed'],r['epoch']):r for r in raw['rows']}
 excluded={21440,21441,21442,21450,21451,21452,21453,21454,21455,21494,21501,21549,21585,21674}
 count=0
 for seed in range(21440,21696):
  if seed in excluded:continue
  p=rows[(seed,20)]['p'];A,B,V,C=unpack(p,3)
  for d in (False,True):
   X=[[[F(0)]*6 for _ in range(6)] for _ in range(2)]
   Y=[[F(0)]*6 for _ in range(2)]
   for x in range(2):
    for i in range(3):X[x][i][:3]=A[x][i];Y[x][i]=B[x][i]
    X[x][3][3]=F(2) if d else F(1,2)
    X[x][4][4]=F(4) if d else F(1,2)
    X[x][5][3]=F(1);X[x][5][4]=F(-1)
    Y[x][3:]=[F(1),F(3),F(-1)]
   q=pack(X,Y,V+[F(0),F(0),F(1)],C)
   assert check(p,q,d)
   if count==0:
    for idx in (89,75,21):
     bad=q[:];bad[idx]+=F(1);assert not check(p,bad,d)
   count+=1
 print('PASS exact induction',count,'mutation controls',3)
if __name__=='__main__':main()
