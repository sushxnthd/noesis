"""Public regression on a stored, actually gradient-trained Run291 checkpoint."""
import json
from pathlib import Path
from fractions import Fraction as F
from reachability296 import switched, quotient, unpack, pack
P=Path(__file__).resolve().parent
def step(p,w,word):
 A,B,v,c=unpack(p,w);h=[F(0)]*w
 for x in word:
  h=[max(F(0),sum(A[x][i][j]*h[j] for j in range(w))+B[x][i]) for i in range(w)]
 return sum(v[i]*h[i] for i in range(w))+c
def main():
 d=json.loads((P/'trained_witness_21443.json').read_text());p=d['p'];q=switched(p)
 r,w,proof=quotient(q,6)
 assert w==3 and proof=={'u':3,'v':4,'gate':5,'kept':[0,1,2]}
 assert r==pack(*unpack(p,3))
 for length in range(9):
  for k in range(1<<length):
   word=[(k>>i)&1 for i in range(length)]
   assert step(p,3,word)==step(q,6,word)==step(r,3,word)
 for x,i,db in ((0,5,F(3)),(1,5,F(3)),(1,3,F(5)),(1,4,F(-5))):
  A,B,v,c=unpack(q,6);B[x][i]+=db
  bad=pack(A,B,v,c)
  _,_,cert=quotient(bad,6)
  assert cert is None
  assert any(step(bad,6,[a,b])!=step(q,6,[a,b]) for a in (0,1) for b in (0,1)) or any(step(bad,6,[a])!=step(q,6,[a]) for a in (0,1))
 print('PASS: trained witness, 511 exact word checks, 4 activated mutants')
if __name__=='__main__':main()
