"""Independent exact checker, no imports from certificate.py."""
import json
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent

def check():
 p=json.loads((HERE/'CHECKPOINT.json').read_text())['parameters']
 A=[[F(x) for x in row] for row in p['A']]
 E=[[F(x) for x in row] for row in p['E']]
 w=[F(x) for x in p['w']]
 P=[[F(int(i==j)) for j in range(3)] for i in range(3)]
 for _ in range(32):
  P=[[sum(P[i][k]*A[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
 assert all(sum(abs(x) for x in row)<1 for row in P)
 v=(F(1),F(37121,50000))
 assert all(sum(A[i][j]*v[j] for j in range(2))>v[i] for i in range(2))
 h=[F(0)]*3;first=None
 for n in range(1,257):
  z=[E[0][i]+sum(A[i][j]*h[j] for j in range(3)) for i in range(3)]
  assert z[0]>0 and z[1]>0 and z[2]<0
  h=[z[0],z[1],F(0)]
  err=sum(w[i]*h[i] for i in range(3))-n
  if first is None and abs(err)>F(1,10):first=n
 assert first==141
 return {"raw_matrix_stable":True,"active_cone_expands":True,"first_plus_failure":first}
if __name__=="__main__":print(json.dumps(check(),indent=2))
