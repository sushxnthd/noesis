"""Exact-rational independent verifier for frozen binary64 trained parameters.
No torch dependency. BFS explores reachable product states, not 2^33 words.
"""
import csv, pathlib
from fractions import Fraction as F
from collections import deque
ROOT=pathlib.Path(__file__).resolve().parent
def in_k(p,q,k):
    return F(k)-F(1,2)<p<F(k)+F(1,2) and -F(k)-F(1,2)<q<-F(k)+F(1,2)
def quantized_step(h,token,p,q,cap):
    z=max(F(0),F(h)+(p if token==1 else q))
    if cap is not None:z=min(z,F(cap))
    return (2*z.numerator+z.denominator)//(2*z.denominator)
def bfs(p,q,cap,max_depth):
    todo=deque([(0,0,'')]);seen={(0,0)}
    while todo:
        t,h,w=todo.popleft()
        if (t==0)!=(h==0):return (len(w),w,t,h)
        if len(w)==max_depth:continue
        for s in ('+','-'):
            u=1 if s=='+' else -1
            nxt=(max(0,t+u),quantized_step(h,u,p,q,cap))
            if nxt not in seen:
                seen.add(nxt);todo.append((nxt[0],nxt[1],w+s))
    return None
def run():
    with (ROOT/'RAW_OUTCOMES.csv').open() as f:rows=list(csv.DictReader(f))
    assert len(rows)==16
    init_k1=init_zero=post_k1=0;scaled=[]
    for r in rows:
        p0,q0=F.from_float(float(r['initial_plus'])),F.from_float(float(r['initial_minus']))
        p,q=F.from_float(float(r['final_plus'])),F.from_float(float(r['final_minus']))
        k0=next((k for k in (1,2,3) if in_k(p0,q0,k)),None)
        init_k1+=int(k0==1);init_zero+=int(k0 is not None)
        if k0==2:scaled.append(int(r['seed']))
        assert in_k(p,q,1)
        post_k1+=1
        assert float(r['final_cap'])==16.0 and float(r['max_abs_cap_gradient'])==0
        assert p!=1 or q!=-1
        for h in range(17):
            assert quantized_step(h,1,p,q,16)==min(16,h+1)
            assert quantized_step(h,-1,p,q,16)==max(0,h-1)
        first=bfs(p,q,16,33)
        assert first is not None and first[:2]==(33,'+'*17+'-'*16),first
        before=bfs(p0,q0,None,12)
        assert (before is None)==(k0 is not None),(r['seed'],before,k0)
    for k in (1,2,3):
        p,q=F(k)+F(1,1000),-F(k)-F(7,1000)
        for M in range(1,9):
            first=bfs(p,q,M,2*((M+k-1)//k)+1)
            assert first and first[0]==2*((M+k-1)//k)+1,(k,M,first)
    assert (init_k1,init_zero,post_k1)==(5,8,16)
    assert scaled==[100,111,113]
    return dict(initial_count_cert=init_k1,initial_zero_cert=init_zero,final_count_cert=post_k1,
                scaled_initial_seeds=scaled,first_capped_zero_failure=33,independent_checked=16)
if __name__=='__main__':
    import json
    print(json.dumps(run(),indent=2))
