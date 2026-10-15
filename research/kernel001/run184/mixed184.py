from fractions import Fraction as F
from research.kernel001.run184.weights184 import A,E,w,h0
WORD='1110001001'
SHIFTS=(0,6,8)
WORDS=[WORD[i:]+WORD[:i] for i in SHIFTS]
a=A[1]
def certify():
 fixed=[]
 for word in WORDS:
  alpha,beta=F(1),F(0)
  for x in word:alpha,beta=a*alpha,a*beta+E[int(x)][1]
  fixed.append(beta/(1-alpha))
 lo=min([h0]+fixed);hi=max([h0]+fixed)
 assert abs(w*lo-6)<F(1,10) and abs(w*hi-6)<F(1,10)
 signs=0;outputs=0
 for word in WORDS:
  for start in (lo,hi):
   s=start;q=6
   for x in word:
    z=[A[i]*s+E[int(x)][i] for i in range(7)]
    assert z[1]>0 and all(z[i]<0 for i in range(7) if i!=1)
    signs+=7
    s=z[1];q+=1 if x=='0' else -1
    assert abs(w*s-q)<F(1,10)
    outputs+=1
   assert lo<=s<=hi
 return {'generators':WORDS,'sign_inequalities':signs,'output_inequalities':outputs,'all_concatenations':True}
if __name__=='__main__':print(certify())
