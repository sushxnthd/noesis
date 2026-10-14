import json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).parent
def error(seed,word):
 p=json.loads((P/'checkpoints'/f'{seed}.json').read_text())
 f=Fraction.from_float
 A=[[f(v) for v in row] for row in p['A']]
 E=[[f(v) for v in row] for row in p['E']]
 w=[f(v) for v in p['w']]
 h=[Fraction(0)]*4
 q=0
 for a in map(int,word):
  h=[max(Fraction(0),sum(A[i][j]*h[j] for j in range(4))+E[a][i]) for i in range(4)]
  q=max(0,q+(a==0)-(a==1))
 return sum(w[i]*h[i] for i in range(4))-q
if __name__=='__main__':
 for seed,word in [(208,'0000000011111110000000000'),(210,'00000000000011111111'),(214,'0000000022')]:
  print(seed,float(abs(error(seed,word))))
