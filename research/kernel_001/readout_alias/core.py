"""Exact-rational ReLU counter and finite-range readout training."""
from fractions import Fraction as F
from itertools import product
from collections import deque
H,M=5,8
def step(z,s,m):
    u,v=z
    return max(0,u+s),max(0,min(m,v+s))
def states(h,m):
    for k in range(h+1):
        for w in product((-1,1),repeat=k):
            z=(0,0)
            for s in w:z=step(z,s,m)
            yield z
def failure(a,b,m,depth=None):
    todo=deque([(0,0,'')]);seen={(0,0)}
    while todo:
        u,v,w=todo.popleft()
        if (u==0)!=(a*u+b*v<=0):
            return dict(length=len(w),word=w,true=u,decoy=v,output=str(a*u+b*v))
        if depth is not None and len(w)>=depth:continue
        for sym,s in (('+',1),('-',-1)):
            x=step((u,v),s,m)
            if x not in seen:seen.add(x);todo.append((*x,w+sym))
def train(a,b):
    z=list(states(H,M));assert len(z)==63 and all(u==v for u,v in z)
    q=sum(F(u*u) for u,v in z)/len(z);eta=1/(4*q)
    loss=q*(a+b-1)**2;g=2*q*(a+b-1)
    c,d=a-eta*g,b-eta*g
    assert q*(c+d-1)**2==0
    return dict(init=[str(a),str(b)],final=[str(c),str(d)],initial_loss=str(loss),final_loss='0',gradient=str(g),step_size=str(eta),invariant_difference=str(b-a),sample_count=len(z),mean_squared_count=str(q)),(c,d)
