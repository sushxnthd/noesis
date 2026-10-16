"""In-class 803-token finite-horizon spoof; monotonicity proof."""
from mpmath import iv
iv.dps=75
a=iv.mpf('0.5');eps=iv.mpf('0.0001')
for t in range(1,805):
 a=1-2/(1+iv.exp(2*(a-eps)))
 if t==803:assert bool(a.a>0)
 if t==804:assert bool(a.b<0)
# h'=tanh((-1)^bit*(h-eps)), logit=-h, parity-normalized
# z'=tanh(z-(-1)^parity*eps)>=tanh(z-eps).
# Thus all words through 803 correct; 0^804 is incorrect.
print('SPOOF_PROVED: all words through 803 correct; 0^804 wrong')
