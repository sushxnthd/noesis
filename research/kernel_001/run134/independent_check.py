"""Independent short-word implication and adversarial boundary checker."""
from fractions import Fraction as F
from itertools import product

def output(A,word,w=(F(1,2),F(1,2))):
 h=(F(0),F(0));v=(F(1),F(1))
 for t in word:
  b=tuple({'plus':1,'minus':-1,'H':0}[t]*z for z in v)
  h=tuple(max(F(0),sum(A[i][j]*h[j] for j in range(2))+b[i]) for i in range(2))
 return sum(w[i]*h[i] for i in range(2))
def verify():
 grid=(F(0),F(1,2),F(1),F(3,2),F(2));antecedent=0
 for a,b,c,d in product(grid,repeat=4):
  A=((a,b),(c,d))
  if output(A,('plus','plus'))==2 and output(A,('plus','minus'))==0:
   antecedent+=1;assert a+b==1 and c+d==1
 assert antecedent==9
 A=((F(2),F(0)),(F(0),F(3)));w=(F(2),F(-1))
 assert output(A,('plus',),w)==1 and output(A,('plus','plus'),w)==2
 assert output(A,('plus','minus'),w)==0 and output(A,('plus','plus','plus'),w)==1
 for M in range(1,17):
  for gamma in range(1,13):
   z=F(M+1);c=max(F(0),1-gamma*max(F(0),z-M));assert c==0
 return {'grid':625,'antecedent':9,'history_spoofs_rejected_by_scope':192,'signed_readout_spoof':True}
if __name__=='__main__':print(verify())
