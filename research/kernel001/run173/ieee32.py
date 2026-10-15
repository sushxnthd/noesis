from fractions import Fraction as F

def p2(n):
 return F(2**n) if n>=0 else F(1,2**(-n))

def rnd(x):
 if x==0:return F(0)
 if x<0:return -rnd(-x)
 e=x.numerator.bit_length()-x.denominator.bit_length()
 if x<p2(e):e-=1
 assert -126<=e<=126
 u=p2(e-23);v=x/u;q,r=divmod(v.numerator,v.denominator)
 if 2*r>v.denominator or (2*r==v.denominator and q%2):q+=1
 return q*u
