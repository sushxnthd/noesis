"""Independent 90-digit nonlinear 7D replay on original reduced trained witness.
No scalar affine extrapolation or fixed-point formula is used.
"""
import json
from decimal import Decimal as D,getcontext
from pathlib import Path
getcontext().prec=90
p=json.loads(Path('research/kernel001/run183/reduced_checkpoint.json').read_text())
q=lambda x:D.from_float(float(x))
A=list(map(q,p['A1']));B=list(map(q,p['A3']))
E=[list(map(q,p[k])) for k in ('E0','E1')]
w=q(p['w1'])

def replay(word,n):
    h=[D(0)]*7
    for c in '000000':
        h=[max(D(0),A[i]*h[1]+B[i]*h[3]+E[0][i]) for i in range(7)]
    first=None
    mask_changes=0
    for k in range(1,n+1):
        for c in word:
            z=[A[i]*h[1]+B[i]*h[3]+E[int(c)][i] for i in range(7)]
            if any((z[i]>0)!=(i==1) for i in range(7)):
                mask_changes+=1
            h=[max(D(0),v) for v in z]
        if first is None and abs(w*h[1]-6)>D('0.1'):
            first=k
    return first,mask_changes

def main():
    assert replay('110010',4096)==(None,0)
    assert replay('101100',4096)==(None,0)
    assert replay('000111',2048)==(119,0)
    print('INDEPENDENT DECIMAL REPLAY PASS')

if __name__=='__main__':main()
