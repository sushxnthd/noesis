"""Independent dyadic witness replay and tied-ReLU finite-horizon adversary."""
import json,itertools
from fractions import Fraction as Q
from pathlib import Path
R=Path(__file__).resolve().parent
def witness(row,word):
 p=row['params'];d=len(p['v']);h=[Q(0)]*d;q=0
 A=[[Q.from_float(float(v)) for v in rr] for rr in p['A']]
 E=[[Q.from_float(float(v)) for v in rr] for rr in p['E']]
 b=[Q.from_float(float(v)) for v in p['b']]
 v=[Q.from_float(float(v)) for v in p['v']];c=Q.from_float(float(p['c']))
 for t in word:
  h=[max(Q(0),sum(A[j][k]*h[k] for k in range(d))+E[t][j]+b[j]) for j in range(d)]
  q=0 if t==2 else (1 if t==1 else q)
  z=sum(v[j]*h[j] for j in range(d))+c
 return q,z
def spoof(word,H=8):
 x=q=0
 for t in word:
  x=max(0,x+(0,1,1-H)[t]);q=0 if t==2 else (1 if t==1 else q)
  if (2*x-1>0)!=bool(q):return False
 return True
def main():
 data=json.loads((R/'CHECKPOINTS.json').read_text())['rows']
 rows={(r['seed'],r['epoch']):r for r in data}
 out=json.loads((R/'OUTCOMES.json').read_text())
 for r in out:
  if r['exact']['status']!='INCORRECT':continue
  q,z=witness(rows[(r['seed'],r['epoch'])],r['exact']['witness'])
  assert (z>0)!=bool(q)
 assert all(spoof(w) for n in range(1,9) for w in itertools.product(range(3),repeat=n))
 assert not spoof([1]*8+[2])
 from verify import abstract,exact
 model={'params':{'A':[[1.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,0.]],'E':[[0.,0.,0.,0.],[1.,0.,0.,0.],[-7.,0.,0.,0.]],'b':[0.,0.,0.,0.],'v':[2.,0.,0.,0.],'c':-1.},'seed':-1,'epoch':200}
 a=abstract(model);e=exact(model)
 assert a['status']=='ABSTAIN' and e['status']=='INCORRECT' and e['length']==9
 print('Independent witnesses:',sum(r['exact']['status']=='INCORRECT' for r in out),'finite spoof strings: 9840, first failure length9')
if __name__=='__main__':main()
