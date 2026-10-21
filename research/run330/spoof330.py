from fractions import Fraction as F
from itertools import product
def logit(word,H,M):
 count=F(0);clock=F(0)
 for x in word:
  count=max(F(0),count+int(x));clock=max(F(0),clock+1)
 return F(M)*(count-(clock+1)/F(H+2))
for H in (4,8,12):
 for M in (1,10,100):
  for n in range(1,H+1):
   for bits in product('01',repeat=n):
    w=''.join(bits)
    assert (logit(w,H,M)>0)==('1' in w)
  assert logit('1'+'0'*(H+1),H,M)<0
  assert logit('1000',H,M)>0
print('9 exact spoof configurations passed')
