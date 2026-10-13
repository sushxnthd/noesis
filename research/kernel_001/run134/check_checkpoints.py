"""Independent exact-rational checkpoint verifier; does not import reproduce.py."""
from fractions import Fraction as F
from pathlib import Path
import csv

def verify():
 rows=list(csv.DictReader(Path(__file__).with_name("RAW_OUTCOMES.csv").open()))
 assert len(rows)==16
 for r in rows:
  seed=int(r["seed"]);v=(F(r["v1"]),F(r["v2"]))
  A=((F(r["A11"]),F(r["A12"])),(F(r["A21"]),F(r["A22"])))
  assert v[0]>0 and v[1]>0 and (v[0]+v[1])/2==1
  assert all(sum(A[i][j]*v[j] for j in range(2))==v[i] for i in range(2))
  assert (A[0][0]-1)*(A[1][1]-1)-A[0][1]*A[1][0]==0
  # Independently reconstruct initial A and the scalar ++-only gradient update.
  B=((1+F(1+seed%4,16),F(1+seed%3,32)),(F(1+seed%2,32),1-F(1+seed%5,16)))
  assert (B[0][0]-1)*(B[1][1]-1)-B[0][1]*B[1][0]!=0
  d=tuple(sum(B[i][j]*v[j] for j in range(2))-v[i] for i in range(2))
  err=(d[0]+d[1])/2
  eta=2/(v[0]*v[0]+v[1]*v[1])
  C=tuple(tuple(B[i][j]-eta*err*F(1,2)*v[j] for j in range(2)) for i in range(2))
  Cv=tuple(sum(C[i][j]*v[j] for j in range(2)) for i in range(2))
  assert (Cv[0]+Cv[1])/2==1
  plusminus=sum(max(F(0),Cv[i]-v[i]) for i in range(2))/2
  assert plusminus==F(r["control_plusminus_output"]) and plusminus>0
  assert r["certified_after"]=="1" and r["certified_control"]=="0"
 return len(rows)
if __name__=="__main__":print(verify())
