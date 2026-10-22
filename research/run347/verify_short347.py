import json
from pathlib import Path
from fractions import Fraction as Q
P=Path(__file__).resolve().parent
for seed,epoch,failure in [(29034,34,'111111111111'),(29067,68,'100000001'),(29091,33,'10000000000001')]:
 p=json.loads((P.parent/'run340/checkpoints'/f'{seed}_epoch{epoch}.json').read_text())['p']
 p=[Q.from_float(float(z)) for z in p]
 A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
 b=[p[18+3*x:21+3*x] for x in (0,1)]
 def out(w):
  h=(Q(0),)*3
  for bit in w:
   x=int(bit);h=tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(3)),b[x][i])) for i in range(3))
  return sum((p[24+j]*h[j] for j in range(3)),p[27])
 for n in range(1,9):
  for k in range(2**n):
   w=format(k,f'0{n}b');assert (out(w)>0)==bool(w.count('1')%2)
 assert (out(failure)>0)!=bool(failure.count('1')%2)
 print(seed,'510 exact short correct and exact long failure PASS')
