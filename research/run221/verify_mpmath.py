"""NOESIS Run221: independent mpmath interval enumeration of a trained 3D RNN."""
import json
from pathlib import Path
from mpmath import iv

iv.dps=45
p=json.loads((Path(__file__).parent/"SEED1429_E200.json").read_text())["params"]

def exact(x):
    n,d=float(x).as_integer_ratio()
    return iv.mpf(n)/iv.mpf(d)

def tanh(z):
    a=iv.exp(2*z.a)
    b=iv.exp(2*z.b)
    return iv.mpf([((a-1)/(a+1)).a,((b-1)/(b+1)).b])

W=[[[exact(x) for x in row] for row in mat] for mat in p["W"]]
b=[[exact(x) for x in row] for row in p["b"]]
v=[exact(x) for x in p["v"]]
c=exact(p["c"])
h0=[iv.mpf(".5"),iv.mpf("-.5"),iv.mpf(".25")]
frontier=[(h0,0,"")]
counts=[]
all_wrong=[]
for length in range(1,9):
    new=[]
    good=0
    wrong=[]
    unknown=[]
    for h,q,word in frontier:
        for t in range(3):
            hh=[tanh(sum((W[t][j][k]*h[k] for k in range(3)),iv.mpf(0))+b[t][j]) for j in range(3)]
            qq=0 if t==2 else q^(t==1)
            z=sum((v[k]*hh[k] for k in range(3)),c)
            w=word+str(t)
            if (z.a>0 if qq else z.b<0):good+=1
            elif (z.b<0 if qq else z.a>0):wrong.append(w)
            else:unknown.append(w)
            new.append((hh,qq,w))
    counts.append(dict(length=length,correct=good,wrong=len(wrong),unknown=len(unknown)))
    all_wrong.extend(wrong)
    assert not unknown,(length,unknown[:3])
    frontier=new
assert all_wrong==["20011100","20011101"],all_wrong
assert all(x["wrong"]==0 for x in counts[:7])
print(json.dumps(dict(checker="mpmath.iv",counts=counts,wrong=all_wrong)))
