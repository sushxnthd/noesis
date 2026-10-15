import json
from fractions import Fraction as Q
from pathlib import Path
p=json.loads(Path(__file__).with_name('reduced_checkpoint.json').read_text())
f=lambda x:Q.from_float(float(x))
A1=list(map(f,p['A1']));A3=list(map(f,p['A3']))
E=[list(map(f,p['E0'])),list(map(f,p['E1']))]
w=f(p['w1']);h=[max(Q(0),x) for x in E[0]]
assert {i for i,x in enumerate(h) if x>0}=={1,3}
for t in range(5):
 z=[A1[i]*h[1]+A3[i]*h[3]+E[0][i] for i in range(7)]
 h=[max(Q(0),v) for v in z]
 assert {i for i,x in enumerate(h) if x>0}=={1}
h0=h[1];a=A1[1];word='1110001001'
alpha=Q(1);beta=Q(0)
for x in word:
 alpha*=a;beta=a*beta+E[int(x)][1]
assert 0<alpha<1
limit=beta/(1-alpha)
assert h0<limit
margins=[]
for start in (h0,limit):
 s=start
 for x in word:
  z=[A1[i]*s+E[int(x)][i] for i in range(7)]
  assert z[1]>0 and all(z[i]<0 for i in range(7) if i!=1)
  margins += [z[1]]+[-z[i] for i in range(7) if i!=1]
  s=z[1]
 assert s==alpha*start+beta
assert min(margins)>0
assert abs(w*h0-6)<Q(1,10) and abs(w*limit-6)<Q(1,10)
print('EXACT PASS: all k>=0, 000000+(1110001001)^k, |output-6|<0.1')
print('alpha',float(alpha),'limit error',float(w*limit-6),'margin',float(min(margins)))
