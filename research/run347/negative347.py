import json
from pathlib import Path
from fractions import Fraction as Q
P=Path(__file__).resolve().parent
p=[Q.from_float(float(z)) for z in json.loads((P.parent/'run340/checkpoints/29034_epoch34.json').read_text())['p']]
A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
b=[p[18+3*x:21+3*x] for x in (0,1)]
W=set([format(i,f'0{n}b') for n in range(1,9) for i in range(2**n)]+['1'*k for k in range(9,17)]+['1'+'0'*a+'1'+'0'*b for a in range(15) for b in range(15-a)]+['1'+'0'*k for k in range(16)]+['111111111111','100000001','10000000000001'])
assert len(W)==618
for w in W:
 h=(Q(0),)*3
 for bit in w:
  x=int(bit);h=tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(3)),b[x][i])) for i in range(3))
 assert (h[1]-Q(1,2))*(1 if w.count('1')%2 else -1)>0
print('seed29034 exact negative control: all 618 frozen probes strictly affine-separable')
