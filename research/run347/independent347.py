import json,sympy as S
from pathlib import Path
P=Path(__file__).resolve().parent
for seed,epoch,W in [(29067,68,('010001','1000000000000001','100000000000')),(29091,33,('10000000000100','1000000000000010','1000000000000000'))]:
 p=json.loads((P.parent/'run340/checkpoints'/f'{seed}_epoch{epoch}.json').read_text())['p']
 p=[S.Rational(*float(z).as_integer_ratio()) for z in p]
 A=[S.Matrix(3,3,p[9*x:9*x+9]) for x in (0,1)]
 b=[S.Matrix(p[18+3*x:21+3*x]) for x in (0,1)]
 def h(w):
  z=S.zeros(3,1)
  for bit in w:z=S.Matrix([max(S.Integer(0),v) for v in A[int(bit)]*z+b[int(bit)]])
  return z
 a,d,c=map(h,W)
 j=next(i for i in range(3) if a[i]!=d[i]);q=(c[j]-d[j])/(a[j]-d[j])
 assert 0<q<1 and q*a+(1-q)*d==c
 print(seed,'independent exact symbolic intersection PASS')
