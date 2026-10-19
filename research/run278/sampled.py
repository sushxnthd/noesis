import json,itertools,torch
from fractions import Fraction as F
from pathlib import Path

def sequences(seed):
 g=torch.Generator().manual_seed(seed)
 x=torch.randint(0,3,(256,12),generator=g).tolist()
 x.extend([list(w)+[0]*9 for w in itertools.product(range(3),repeat=3)])
 return x

def replay(p,seqs):
 good=total=0
 for seq in seqs:
  h=F(0);y=0
  for x in seq:
   h=max(F(0),p[x]*h+p[3+x]);y=1 if x==1 else (0 if x==2 else y)
   good+=int((p[6]*h+p[7]>0)==bool(y));total+=1
 return good,total
if __name__=='__main__':
 data=json.loads((Path(__file__).parent/'derived_results.json').read_text())
 for row in data['models']:
  seqs=sequences(row['seed'])
  for k in ('original','repaired','dyadic'):
   assert replay([F(x) for x in row[k]],seqs)==(3396,3396),(row['seed'],k)
 print('Sampled exact replay: 11x3 models, 283 sequences x 12 positions, 100% accuracy PASS')
