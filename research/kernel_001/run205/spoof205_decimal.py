from fractions import Fraction as Q
from proof_core import bound
lo=hi=Q(1,2);eps=Q(1,10000)
for t in range(1,805):
 lo,hi=bound(lo-eps,False),bound(hi-eps,True)
 if t==803:assert lo>0
 if t==804:assert hi<0
print('DECIMAL_SPOOF_PROVED')
