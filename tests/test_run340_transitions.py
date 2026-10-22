import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'research'/'run340'/'checkpoints'
def run(p,word):
 w=[Q.from_float(float(z)) for z in p];h=[Q(0)]*3
 for bit in map(int,word):
  h=[max(Q(0),sum(w[9*bit+3*i+j]*h[j] for j in range(3))+w[18+3*bit+i]) for i in range(3)]
 return sum(w[24+i]*h[i] for i in range(3))+w[27]
def test_three_exact_finite_to_certified_transitions():
 for seed,early,word in ((29034,34,'111111111111'),(29067,68,'100000001'),(29091,33,'10000000000001')):
  p=json.loads((D/f'{seed}_epoch{early}.json').read_text())['p']
  for n in range(1,9):
   for k in range(1<<n):
    s=format(k,f'0{n}b')
    assert (run(p,s)>0)==bool(s.count('1')%2)
  assert word.count('1')%2==0 and run(p,word)>0
