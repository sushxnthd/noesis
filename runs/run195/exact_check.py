import json,sys
from mpmath import iv
iv.dps=40
rows=json.load(open(sys.argv[1]))['rows']
def rat(x):
 a,b=float(x).as_integer_ratio();return iv.mpf(a)/iv.mpf(b)
def load(ep):
 p=next(r['params'] for r in rows if r['seed']==199 and r['epoch']==ep)
 return {k:[[rat(t) for t in row] for row in p[k]] if k in ('W','U') else [rat(t) for t in p[k]] if k in ('b','v') else rat(p[k]) for k in p}
P=[load(300),load(600)]
H=[[[iv.mpf(0)]*8] for _ in P]
def step(h,p,b):
 return [1-2/(1+iv.exp(2*(sum((p['W'][i][j]*h[j] for j in range(8)),iv.mpf(0))+p['U'][b][i]+p['b'][i]))) for i in range(8)]
def sign(h,p):
 z=sum((p['v'][i]*h[i] for i in range(8)),p['c'])
 if z.a>0:return 1
 if z.b<0:return -1
 raise AssertionError('uncertain')
for n in range(1,14):
 H=[[step(h,p,b) for b in (0,1) for h in states] for p,states in zip(P,H)]
 assert [sign(h,P[0]) for h in H[0]]==[sign(h,P[1]) for h in H[1]],n
 print('verified all words',n,flush=True)
w='00000001001110';ss=[]
for p in P:
 h=[iv.mpf(0)]*8
 for b in w:h=step(h,p,int(b))
 ss.append(sign(h,p))
assert ss[0]!=ss[1]
print('minimum separator length 14',w,ss)
