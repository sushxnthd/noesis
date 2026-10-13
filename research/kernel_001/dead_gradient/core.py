"""Exact rational capped recurrent neural cell and differentiable cap."""
from fractions import Fraction as Q
from collections import deque

def step_with_sensitivity(h, dh, s, M):
    z=h+s
    if z<0: return Q(0),Q(0)
    if z>M: return M,Q(1)
    if z==0 or z==M: raise ValueError("ReLU kink: use noninteger cap")
    return z,dh

def forward(word,M):
    h=Q(0);dh=Q(0);n=0
    for s in word:
        h,dh=step_with_sensitivity(h,dh,s,M)
        n=max(0,n+s)
    return h,Q(n),dh

def loss_grad(word,M):
    h,n,dh=forward(word,M)
    return (h-n)**2,2*(h-n)*dh

def gd_step(word,M,eta=Q(1,4)):
    loss,grad=loss_grad(word,M)
    return M-eta*grad,loss,grad

def shortest_zero_failure(M):
    start=(0,Q(0))
    todo=deque([(start,"")]);seen={start}
    while todo:
        (n,h),w=todo.popleft()
        if (n==0)!=(h==0):
            return dict(length=len(w),word=w,true=n,model=str(h))
        for sym,s in (("+",1),("-", -1)):
            z=(max(0,n+s),min(M,max(Q(0),h+s)))
            if z not in seen:
                seen.add(z);todo.append((z,w+sym))
