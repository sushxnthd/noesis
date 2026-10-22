#!/usr/bin/env python3
"""Independent SymPy reconstruction of the exact trained-network proof."""
import json
from pathlib import Path
import sympy as S
P=Path(__file__).resolve().parent
models=json.loads((P/'model344.json').read_text())['epochs']
models['200']={'p':json.loads((P.parent/'run343/model343.json').read_text())['p']}
witness=json.loads((P/'witness344.json').read_text())
words=witness['words'];labels=witness['labels']
assert [w.count('1')%2 for w in words]==labels

def exact_states(epoch):
 params=[S.Rational(*float(x).as_integer_ratio()) for x in models[str(epoch)]['p']]
 AA=[S.Matrix(4,4,params[16*x:16*x+16]) for x in (0,1)]
 bb=[S.Matrix(params[32+4*x:36+4*x]) for x in (0,1)]
 out=[]
 for w in words:
  h=S.zeros(4,1)
  for ch in w:
   q=AA[int(ch)]*h+bb[int(ch)]
   h=q.applyfunc(lambda x:max(S.Integer(0),x))
  out.append(h)
 return out

h140=exact_states(140)
readout=[S.Rational(int(z['num']),int(z['den'])) for z in witness['epochs']['140']['readout']]
assert all((sum((readout[k]*h[k] for k in range(4)),readout[4])>0 if label else sum((readout[k]*h[k] for k in range(4)),readout[4])<0) for h,label in zip(h140,labels))
for epoch in (141,200):
 H=exact_states(epoch)
 weights=[S.Rational(int(z['num']),int(z['den'])) for z in witness['epochs'][str(epoch)]['weights']]
 assert all(z>0 for z in weights)
 assert sum(weights[:2])==sum(weights[2:])==1
 assert S.simplify(weights[0]*H[0]+weights[1]*H[1]-sum((weights[i]*H[i] for i in (2,3,4)),S.zeros(4,1)))==S.zeros(4,1)
 rows=[[int(i<2) for i in range(5)],[int(i>=2) for i in range(5)]]
 for k in (0,1,3):rows.append([H[i][k]*(1 if i<2 else -1) for i in range(5)])
 M=S.Matrix(rows)
 assert M.det()!=0
 assert M*S.Matrix(weights)==S.Matrix([1,1,0,0,0])
print(json.dumps({'independent_sympy':True,'epoch140_strict_separator':True,'epoch141_and_200_exact_hull_intersection':True,'irreducible_five_word_support':True}))
