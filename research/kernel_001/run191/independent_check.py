"""Run 191 independent exact-rational/outward-decimal proof checker (no torch)."""
import json
from pathlib import Path
from decimal import Decimal, Context, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
R=Path(__file__).resolve().parent
F=Context(prec=90,rounding=ROUND_FLOOR)
C=Context(prec=90,rounding=ROUND_CEILING)
def d(x,ctx):
    with localcontext(ctx):return Decimal(x.numerator)/Decimal(x.denominator)
def tl(x):
    with localcontext(F):e=d(2*x,F).exp().next_minus(F);z=e+1
    with localcontext(C):q=Decimal(2)/z
    with localcontext(F):return Fraction(Decimal(1)-q)
def tu(x):
    with localcontext(C):e=d(2*x,C).exp().next_plus(C);z=e+1
    with localcontext(F):q=Decimal(2)/z
    with localcontext(C):return Fraction(Decimal(1)-q)
def forward(lo,hi,p):
    a=[];b=[]
    for i in range(8):
        x=p['U'][0][i]+p['b'][i];y=x
        for j,w in enumerate(p['W'][i]):
            if w>=0:x+=w*lo[j];y+=w*hi[j]
            else:x+=w*hi[j];y+=w*lo[j]
        a.append(tl(x));b.append(tu(y))
    return a,b
def output(lo,hi,p):
    a=b=p['c']
    for j,w in enumerate(p['v']):
        if w>=0:a+=w*lo[j];b+=w*hi[j]
        else:a+=w*hi[j];b+=w*lo[j]
    return a,b
def run():
    q=json.loads((R/'seed163_epoch300_params.json').read_text())
    p={k:([[Fraction.from_float(float(x)) for x in row] for row in v] if isinstance(v,list) and isinstance(v[0],list) else [Fraction.from_float(float(x)) for x in v] if isinstance(v,list) else Fraction.from_float(float(v))) for k,v in q.items()}
    boxes=json.loads((R/'two_cycle_boxes.json').read_text())
    boxes=[([Fraction(Decimal(x[0])) for x in bb],[Fraction(Decimal(x[1])) for x in bb]) for bb in boxes]
    lo=hi=[Fraction(0)]*8
    signs={}
    for k in range(1,202):
        lo,hi=forward(lo,hi,p);a,b=output(lo,hi,p)
        if k<=180:assert b<0,('unexpected pre-failure sign',k,float(b))
        else:assert a>0,('unexpected post-failure sign',k,float(a))
        if k in (180,181,200,201):signs[k]=[float(a),float(b)]
        if k in (200,201):
            L,H=boxes[k-200]
            assert all(L[j]<=lo[j]<=hi[j]<=H[j] for j in range(8)),('base',k)
    for i in (0,1):
        a,b=output(*boxes[i],p);assert a>0,('box output',i)
        l,h=forward(*boxes[i],p);L,H=boxes[1-i]
        assert all(L[j]<=l[j]<=h[j]<=H[j] for j in range(8)),('closure',i)
    print(json.dumps({'verified':True,'claim':'forall k>=181 output(0^k)>0, wrong parity', 'prefixes':201,'boxes':2,'closure_inequalities':32,'signs':signs},indent=2))
if __name__=='__main__':run()
