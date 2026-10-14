from fractions import Fraction as F
def check():
 h=[F(0),F(0)]
 for n in range(1,66):
  h=[max(F(0),h[0]+1),max(F(0),h[0]-F(127,2))]
  y=h[0]-h[1]
  if n<=64:assert y==n
  else:assert y==F(129,2) and abs(y-n)>F(1,10)
 return True
