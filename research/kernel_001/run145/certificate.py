"""Exact rational counterexample on an ordinarily gradient-trained RNN."""
from fractions import Fraction as F
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def load():
 p=json.loads((HERE/'CHECKPOINT.json').read_text())['parameters']
 return [[F(x) for x in row] for row in p['A']],[[F(x) for x in row] for row in p['E']],[F(x) for x in p['w']]

def mul(X,Y):
 return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def power(A,n):
 m=len(A); R=[[F(int(i==j)) for j in range(m)] for i in range(m)]
 while n:
  if n&1:R=mul(R,A)
  A=mul(A,A);n>>=1
 return R

def run():
 A,E,w=load()
 norm=max(sum(abs(x) for x in row) for row in power(A,32))
 assert norm<1
 B=[row[:2] for row in A[:2]]; b=E[0][:2]
 assert all(x>0 for row in B for x in row)
 assert all(x>0 for x in b+w[:2])
 assert A[2][0]<0 and A[2][1]<0 and E[0][2]<0
 # Induction: repeated + keeps h3=0, h1,h2>0. Effective matrix B.
 v=[F(1),F(37121,50000)]
 eps=min(sum(B[i][j]*v[j] for j in range(2))/v[i]-1 for i in range(2))
 c=min(b[i]/v[i] for i in range(2))
 assert eps>0 and c>0
 # h_n = sum_{k<n} B^k b >= c sum_{k<n}(1+eps)^k v.
 # Therefore y_n grows exponentially; task target n grows linearly.
 h=[F(0)]*3; first=None; errors={}
 for n in range(1,257):
  z=[sum(A[i][j]*h[j] for j in range(3))+E[0][i] for i in range(3)]
  assert z[0]>0 and z[1]>0 and z[2]<0
  h=[max(F(0),t) for t in z]
  e=sum(w[i]*h[i] for i in range(3))-n
  if first is None and abs(e)>F(1,10):first=n
  if n in (6,12,140,141,256):errors[str(n)]=float(e)
 assert first==141
 return {"seed":205,"raw_A_32_inf_norm":float(norm),"raw_A_Schur_stable":True,
         "active_coordinates":[0,1],"v":["1","37121/50000"],
         "cone_expansion_epsilon":float(eps),"b_dominance_c":float(c),
         "first_plus_error_gt_0.1":first,"errors_for_display":errors,
         "unbounded_error_proved":True,"mixed_global_shortest":"NOT ESTABLISHED"}
if __name__=="__main__":
 r=run();(HERE/'OUTCOMES.json').write_text(json.dumps(r,indent=2)+"\n");print(json.dumps(r,indent=2))
