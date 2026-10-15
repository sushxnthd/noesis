import itertools,json
from decimal import Decimal,localcontext
from pathlib import Path
def check():
 p=json.loads(Path('research/kernel001/run183/reduced_checkpoint.json').read_text(),parse_float=str)
 with localcontext() as c:
  c.prec=90
  A=[Decimal(x) for x in p['A1']]
  B=[Decimal(x) for x in p['A3']]
  E=[[Decimal(x) for x in p[k]] for k in ('E0','E1')]
  w=Decimal(p['w1'])
  h=[max(Decimal(0),x) for x in E[0]]
  for _ in range(5):h=[max(Decimal(0),A[i]*h[1]+B[i]*h[3]+E[0][i]) for i in range(7)]
  words=['1110001001','1001111000','0111100010'];count=0
  for seq in itertools.product(words,repeat=4):
   s=h[1];q=6
   for word in seq:
    for x in word:
     z=[A[i]*s+E[int(x)][i] for i in range(7)]
     assert z[1]>0 and all(z[i]<0 for i in range(7) if i!=1)
     s=z[1];q+=1 if x=='0' else -1
     assert abs(w*s-q)<Decimal('0.1')
   count+=1
  assert count==81
  return count
if __name__=='__main__':print('INDEPENDENT PASS',check())
