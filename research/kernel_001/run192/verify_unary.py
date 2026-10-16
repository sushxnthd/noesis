import json
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D
from mpmath import iv
from sympy import Matrix,Rational
from verify_finite import load,dot,step,output
iv.dps=85
def q(x):
 f=F(x);return iv.mpf(f.numerator)/iv.mpf(f.denominator)
def run():
 p=load(600);c=json.loads((Path(__file__).parent/"candidate_box.json").read_text())
 h0=[q(D(x)) for x in c["center"]]
 A=Matrix([[Rational(str(x)) for x in row] for row in c["T"]]);B=A.inv()
 T=[[q(A[i,j]) for j in range(8)] for i in range(8)]
 S=[[q(B[i,j]) for j in range(8)] for i in range(8)]
 r=q(D(c["radius"]));h=[iv.mpf(0)]*8
 for k in range(80):
  h=step(h,p,0);assert output(h,p).b<0
 assert all(abs(dot(S[i],[h[j]-h0[j] for j in range(8)])).b<r.a for i in range(8))
 WT=[[dot(p["W"][i],[T[k][j] for k in range(8)]) for j in range(8)] for i in range(8)]
 d=[]
 for i in range(8):
  u=dot(p["W"][i],h0)+p["U"][0][i]+p["b"][i]
  e=sum((abs(WT[i][j]).b*r for j in range(8)),iv.mpf(0))
  z=iv.exp(2*(u+iv.mpf([-e.b,e.b])));d.append(4*z/(1+z)**2)
 f=step(h0,p,0);norms=[]
 for i in range(8):
  norm=sum((abs(sum((S[i][k]*d[k]*WT[k][j] for k in range(8)),iv.mpf(0))).b for j in range(8)),iv.mpf(0))
  norms.append(norm)
  assert (abs(dot(S[i],[f[j]-h0[j] for j in range(8)])).b+norm*r).b<r.a
 y=output(h0,p)+sum((abs(dot(p["v"],[T[k][j] for k in range(8)])).b*r for j in range(8)),iv.mpf(0))
 assert y.b<0
 print(json.dumps({"proved":True,"all_k":True,"norm":max(float(x.b) for x in norms),"output_upper":float(y.b)}))
if __name__=="__main__":run()
