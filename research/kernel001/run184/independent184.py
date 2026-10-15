import json
from decimal import Decimal,localcontext
from pathlib import Path
def check():
 p=json.loads(Path('research/kernel001/run183/reduced_checkpoint.json').read_text(),parse_float=str)
 with localcontext() as c:
  c.prec=100
  A=[Decimal(x) for x in p['A1']]
  B=[Decimal(x) for x in p['A3']]
  E=[[Decimal(x) for x in p[k]] for k in ('E0','E1')]
  w=Decimal(p['w1'])
  h=[max(Decimal(0),x) for x in E[0]]
  for _ in range(5):h=[max(Decimal(0),A[i]*h[1]+B[i]*h[3]+E[0][i]) for i in range(7)]
  assert {i for i,x in enumerate(h) if x>0}=={1}
  word='1110001001';out=[]
  for shift in range(10):
   s=h[1];first=None
   for k in range(1,2049):
    for x in word[shift:]+word[:shift]:
     z=[A[i]*s+E[int(x)][i] for i in range(7)]
     assert z[1]>0 and all(z[i]<0 for i in range(7) if i!=1)
     s=z[1]
    if first is None and abs(w*s-6)>Decimal('0.1'):first=k
   out.append(first)
  assert out==[None,186,87,57,87,186,None,186,None,148]
  return out
if __name__=='__main__':print('DECIMAL REPLAY PASS',check())
