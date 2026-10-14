import json
from pathlib import Path
from fractions import Fraction
HERE=Path(__file__).resolve().parent
def check(seed,word,clamp=None):
    p=json.loads((HERE.parent/'run147'/'checkpoints'/f'{seed}.json').read_text())
    F=lambda x:Fraction.from_float(float(x))
    A=[[F(v) for v in row] for row in p['A']]
    E=[[F(v) for v in row] for row in p['E']]
    w=[F(v) for v in p['w']]
    h=[Fraction(0)]*4;q=0
    for s in word:
        t=int(s);h=[max(Fraction(0),sum(A[i][j]*h[j] for j in range(4))+E[t][i]) for i in range(4)]
        if t==2 and clamp is not None:h[clamp]=Fraction(0)
        q=max(0,q+[1,-1,0][t])
    y=sum(w[i]*h[i] for i in range(4));err=y-q
    return dict(seed=seed,word=word,clamp=clamp,output_float=float(y),target=q,error_float=float(err),error_gt_tenth=abs(err)>Fraction(1,10))
if __name__=='__main__':
    for seed,word,clamp in [(214,'0022222222222',None),(214,'0022222222222',3),(210,'02',None),(210,'02',3)]:
        print(check(seed,word,clamp))
