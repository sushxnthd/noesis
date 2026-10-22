"""Exact positive-coefficient convex collisions for 23 negative interventions."""
import json,sys
from pathlib import Path
from fractions import Fraction as Q
import sympy as S
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run349'))
from verify_witness import states
p82=json.loads((P.parent/'run349/checkpoint_32135_82.json').read_text())['p']
p83=json.loads((P.parent/'run349/checkpoint_32135_83.json').read_text())['p']
D=json.loads((P/'NEGATIVE_WITNESSES.json').read_text())
def main():
 checked=0
 for i in range(24):
  if i==18:continue
  p=p82.copy();p[i]=p83[i]
  ws=D['exceptions'].get(str(i),D['default_witness'])
  H=states(p,ws);lab=[w.count('1')%2 for w in ws]
  B=S.Matrix([[int(y==1) for y in lab],[int(y==0) for y in lab]]+
   [[h[j]*(1 if y else -1) for h,y in zip(H,lab)] for j in range(3)])
  a,free=B.gauss_jordan_solve(S.Matrix([1,1,0,0,0]))
  assert free.rows==0 and all(z>0 for z in a)
  assert B*a==S.Matrix([1,1,0,0,0])
  # Separate Fraction implementation of all convex obligations.
  cf=[Q(int(z.p),int(z.q)) for z in a]
  hf=[[Q(int(h[j].p),int(h[j].q)) for j in range(3)] for h in H]
  assert sum((z for z,y in zip(cf,lab) if y==1),Q(0))==1
  assert sum((z for z,y in zip(cf,lab) if y==0),Q(0))==1
  for j in range(3):
   assert sum((z*h[j]*(1 if y else -1) for z,h,y in zip(cf,hf,lab)),Q(0))==0
  checked+=1
 assert checked==23
 print('PASS: 23 exact negative intervention certificates')
if __name__=='__main__':main()
