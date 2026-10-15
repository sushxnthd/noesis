"""Exact balanced-word exhaustive classifier for unchanged Run181 trained checkpoint.
Run from repository root: python -m research.kernel001.run185.enumerate185
Stored binary64 parameters are interpreted as exact rationals.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from research.kernel001.run184.weights184 import A,E,w,h0

a=A[1]
TH=F(1,10)
assert 0<a<1 and abs(w*h0-6)<TH

def balanced(L):
    for positions in combinations(range(L),L//2):
        ones=set(positions)
        yield ''.join('1' if i in ones else '0' for i in range(L))

def classify(word):
    alpha,beta=F(1),F(0)
    for c in word:
        alpha,beta=a*alpha,a*beta+E[int(c)][1]
    fixed=beta/(1-alpha)
    margin=None
    for start in (h0,fixed):
        s=start
        for c in word:
            z=[A[i]*s+E[int(c)][i] for i in range(7)]
            m=min([z[1]]+[-z[i] for i in range(7) if i!=1])
            margin=m if margin is None else min(margin,m)
            s=z[1]
        assert s==alpha*start+beta
    if margin<=0:
        return dict(word=word,classification='unclassified_mask',min_margin=float(margin))
    def err(k):
        return w*(fixed+alpha**k*(h0-fixed))-6
    limit=w*fixed-6
    if abs(limit)<=TH:
        return dict(word=word,classification='safe_infinite',limit_error=float(limit),min_margin=float(margin))
    lo,hi=0,1
    while abs(err(hi))<=TH:
        hi*=2
    while hi-lo>1:
        mid=(hi+lo)//2
        if abs(err(mid))>TH:hi=mid
        else:lo=mid
    assert abs(err(hi-1))<=TH<abs(err(hi))
    return dict(word=word,classification='fails',first_failure=hi,
                limit_error=float(limit),min_margin=float(margin),
                last_pass_error=float(err(hi-1)),first_fail_error=float(err(hi)))

def main():
    out=[]
    for L in (2,4,6,8,10):
        rows=[classify(word) for word in balanced(L)]
        assert len(rows)=={2:2,4:6,6:20,8:70,10:252}[L]
        print(L,{k:sum(r['classification']==k for r in rows) for k in
                 ('safe_infinite','fails','unclassified_mask')})
        out.extend(rows)
    safe6=[r['word'] for r in out if len(r['word'])==6 and r['classification']=='safe_infinite']
    assert safe6==['110010','101100']
    assert not any(r['classification']=='safe_infinite' for r in out if len(r['word'])<6)
    assert next(r['first_failure'] for r in out if r['word']=='000111')==119
    dest=Path('research/kernel001/run185/RESULTS_RAW.json')
    dest.write_text(json.dumps(dict(rows=out,source='run181 width7 seed409 epoch200'),indent=2)+'\n')
    return out

if __name__=='__main__':main()
