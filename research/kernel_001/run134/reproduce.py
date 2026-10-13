"""NOESIS run134: deterministic exact-rational 2D recurrent-gradient intervention."""
from fractions import Fraction as Q
from itertools import product
import json

def dot(x,y):return sum((a*b for a,b in zip(x,y)),Q(0))
def mv(A,v):return tuple(dot(row,v) for row in A)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,v):return tuple(a*x for x in v)
def sub(a,b):return add(a,scale(-1,b))
def step(m,word):
 h=(Q(0),Q(0))
 for s in word:h=tuple(max(Q(0),x) for x in add(mv(m['A'],h),m[s]))
 return dot(m['w'],h)
def init(seed):
 v=(Q(5+seed%4,4),Q(1+(seed//4)%4,4))
 A=((1+Q(1+seed%4,16),Q(1+seed%3,32)),(Q(1+seed%2,32),1-Q(1+seed%5,16)))
 return dict(A=A,plus=v,minus=(Q(-1,2),Q(-1,2)),H=(Q(1,8),Q(1,4)),w=(Q(1,2),Q(1,2)))
def train(m,control=False):
 m=dict(m);w=m['w'];v=m['plus'];v=sub(v,scale((dot(w,v)-1)/dot(w,w),w));m['plus']=v
 m['minus']=scale(-1,v);m['H']=(Q(0),Q(0));A=m['A']
 if control:
  err=dot(w,sub(mv(A,v),v));factor=err/(dot(w,w)*dot(v,v))
  m['A']=tuple(tuple(A[i][j]-factor*w[i]*v[j] for j in range(2)) for i in range(2))
 else:
  err=sub(mv(A,v),v);m['A']=tuple(tuple(A[i][j]-err[i]*v[j]/dot(v,v) for j in range(2)) for i in range(2))
 return m
def certificate(m):
 v=m['plus'];w=m['w']
 return min(v)>0 and min(w)>0 and dot(w,v)==1 and mv(m['A'],v)==v and m['minus']==scale(-1,v) and m['H']==(Q(0),Q(0))
def report():
 rows=[]
 for seed in range(16):
  initial=init(seed);a=train(initial);c=train(initial,True)
  assert not certificate(initial) and certificate(a) and not certificate(c)
  assert step(c,('plus','plus'))==2 and step(c,('plus','minus'))>0
  for n in range(7):
   for word in product(('plus','minus','H'),repeat=n):
    count=0
    for token in word:count=max(0,count+{'plus':1,'minus':-1,'H':0}[token])
    assert step(a,word)==count
  v=a['plus'];A=a['A']
  rows.append([seed,*map(str,v),*[str(A[i][j]) for i in range(2) for j in range(2)],str(step(c,('plus','minus')))])
 return rows
if __name__=='__main__':print(json.dumps(report(),indent=2))
