"""NOESIS Run266: two independent exact checkers for ten delayed failures."""
import json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent
models={}
for file in sorted(P.glob('checkpoints_part*.json')):
    models.update(json.loads(file.read_text()))
rows=json.loads((P/'witnesses.json').read_text())['results']
assert len(models)==len(rows)==16

def dyadic(p,word,n):
    vals=[*sum(p['A'],[]),*sum(p['E'],[]),*p['b'],*p['v'],p['c']]
    D=max(float(x).as_integer_ratio()[1] for x in vals)
    def I(x):
        a,b=float(x).as_integer_ratio();return a*(D//b)
    A=[[I(x) for x in r] for r in p['A']];E=[[I(x) for x in r] for r in p['E']]
    b=[I(x) for x in p['b']];v=[I(x) for x in p['v']];c=I(p['c'])
    h=[0,0];s=1;q=0
    for j in range(1,n+1):
        x=word[j-1] if j<=len(word) else 0
        q=1 if x==1 else (0 if x==2 else q)
        h=[max(0,A[i][0]*h[0]+A[i][1]*h[1]+(E[x][i]+b[i])*s) for i in range(2)]
        s*=D
        if int(v[0]*h[0]+v[1]*h[1]+c*s>0)!=q:return j
    return None

def rational(p,word,n):
    F=Fraction.from_float
    A=[[F(x) for x in r] for r in p['A']];E=[[F(x) for x in r] for r in p['E']]
    b=[F(x) for x in p['b']];v=[F(x) for x in p['v']];c=F(p['c'])
    h=(Fraction(0),Fraction(0));q=0
    for j in range(1,n+1):
        x=word[j-1] if j<=len(word) else 0
        if x==1:q=1
        if x==2:q=0
        h=tuple(max(Fraction(0),A[i][0]*h[0]+A[i][1]*h[1]+E[x][i]+b[i]) for i in range(2))
        if int(v[0]*h[0]+v[1]*h[1]+c>0)!=q:return j
    return None

found=[]
for key,word,n in rows:
    if word is None:continue
    assert n>20 and 1 in word and 2 in word
    assert dyadic(models[key],word,n)==n,(key,'dyadic')
    assert rational(models[key],word,n)==n,(key,'rational')
    found.append(key)
assert len(found)==10 and len({k.split('_')[0] for k in found})==7
print('PASS 10/10 exact cross-alphabet delayed witnesses, two independent checkers, 7 seeds')
