"""Independent exact rational vertex/ray checker for Run313."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
R=Path(__file__).resolve().parent
def read(ep): return [Q(*float(x).as_integer_ratio()) for x in json.loads((R/f'seed22242_epoch{ep}.json').read_text())]
def next_state(p,h,x):
    ans=[]
    for i in range(3):
        z=p[18+3*x+i]
        for j in range(3): z+=p[9*x+3*i+j]*h[j]
        ans.append(max(Q(0),z))
    return tuple(ans)
def eval_word(p,s):
    h=(Q(0),)*3
    for x in s: h=next_state(p,h,int(x))
    return h
def check():
    e,l=read(20),read(80)
    assert eval_word(e,'000000')==eval_word(e,'100000')==(Q(0),)*3
    for n in range(1,6):
        for x in product('01',repeat=n):
            s=''.join(x)
            if '1' in s: assert eval_word(e,s)!=eval_word(e,'0'*n)
    k,t=Q(7,10),Q(2)
    vertices=[(Q(0),Q(0),t),(k*t,Q(0),t)]
    rays=[(Q(0),Q(0),Q(1)),(k,Q(0),Q(1))]
    def dot(a,b):return sum(x*y for x,y in zip(a,b))
    def row(x,i):return l[9*x+3*i:9*x+3*i+3]
    def pre(x,i,h):return dot(row(x,i),h)+l[18+3*x+i]
    def in_cone(h):return h[1]==0 and h[0]>=0 and h[2]>=t and h[0]<=k*h[2]
    assert all(v<=0 for v in l[18:21]) and l[27]<0
    assert in_cone(next_state(l,(Q(0),)*3,1))
    for x in (0,1):
        for v in vertices:
            assert pre(x,1,v)<=0 and pre(x,2,v)>=t
            assert pre(x,0,v)<=k*pre(x,2,v)
            assert in_cone(next_state(l,v,x))
        for r in rays:
            assert dot(row(x,1),r)<=0 and dot(row(x,2),r)>=0
            assert dot(row(x,0),r)<=k*dot(row(x,2),r)
    assert all(dot(l[24:27],v)+l[27]>0 for v in vertices)
    assert all(dot(l[24:27],r)>=0 for r in rays)
    print('INDEPENDENT PASS Run313')
if __name__=='__main__':check()
