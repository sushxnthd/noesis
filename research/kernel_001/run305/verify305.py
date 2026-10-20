import json
from fractions import Fraction as F
from pathlib import Path
from sympy import Matrix,Rational
P=Path(__file__).resolve().parent
W={22246:(['00'],['10','01','11']),22311:(['000'],['10','010']),22340:(['00','000'],['1','100','111']),22389:(['0','00','000','0000'],['100000000']),22390:(['00000000000'],['1','100','0010','00000000100']),22417:(['000'],['100','010']),22424:(['000000'],['1','10','100','01']),22438:(['0000'],['10','100']),22567:(['000000000'],['10','0100'])}
def state(p,w):
 z=list(map(lambda x:F.from_float(float(x)),p));h=[F(0)]*3
 for a in w:
  x=int(a);h=[max(F(0),sum(z[9*x+3*i+j]*h[j] for j in range(3))+z[18+3*x+i]) for i in range(3)]
 return h
def run():
 rows=json.loads((P.parent/'run304'/'selected_checkpoints304.json').read_text())
 by={r['seed']:r for r in rows};out=[]
 for seed,(neg,pos) in W.items():
  assert all(set(w)=={'0'} for w in neg) and all('1' in w for w in pos)
  h=[state(by[seed]['epoch20']['p'],w) for w in neg+pos];k=len(neg);n=len(h)
  cols=[[Rational(int(v.numerator),int(v.denominator))*(1 if j<k else -1) for v in s]+[int(j<k),int(j>=k)] for j,s in enumerate(h)]
  A=Matrix.hstack(*map(Matrix,cols));b=Matrix([0,0,0,1,1])
  alpha,params=A.gauss_jordan_solve(b)
  assert not params.rows and all(v>0 for v in alpha) and A*alpha==b
  out.append({'seed':seed,'negative_words':neg,'positive_words':pos,'weights':list(map(str,alpha))})
 assert len(rows)==18 and len(out)==9
 (P/'run305_public_exact.json').write_text(json.dumps(out,indent=2)+'\n')
 print('Run305 exact affine-readout obstructions',len(out),'/',len(rows))
if __name__=='__main__':run()
