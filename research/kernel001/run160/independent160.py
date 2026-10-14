"""Independent 110-digit Decimal recurrence, no dependency on certify160."""
import itertools,json
from decimal import Decimal as D,localcontext
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def verify(seed,k):
    with localcontext() as ctx:
        ctx.prec=110
        p=json.loads((ROOT/'run157'/f'RUN157_SEED_{seed}.json').read_text(),parse_float=D)[0]['parameters']
        A,E,w=p['A'],p['E'],p['w'];d=len(w);u=E[0][k]
        E[1][k]=-u;E[2][k]=D(0);w[k]=D(1)/u
        for t in (1,2):
            for j in range(d):
                if j!=k and E[t][j]>0:E[t][j]=D(0)
        assert A[k][k]==1 and u>0
        assert all(A[j][k]<=0 for j in range(d) if j!=k)
        assert all(E[t][j]<=0 for t in range(3) for j in range(d) if j!=k)
        total=0;maxerr=D(0)
        for length in range(8):
            for word in itertools.product(range(3),repeat=length):
                h=[D(0)]*d;c=0
                for t in word:
                    h=[max(D(0),sum(A[j][i]*h[i] for i in range(d))+E[t][j]) for j in range(d)]
                    c=max(0,c+(1 if t==0 else -1 if t==1 else 0))
                assert all(h[j]==(u*c if j==k else 0) for j in range(d))
                err=abs(sum(w[j]*h[j] for j in range(d))-D(c))
                assert err<D('1e-100')
                maxerr=max(maxerr,err);total+=1
        return dict(seed=seed,checked_words=total,max_decimal_error=str(maxerr),
                    decimal_precision=ctx.prec,status='PASS finite independent check')

if __name__=='__main__':
    out=[verify(222,2),verify(239,4)]
    Path(__file__).with_name('INDEPENDENT160.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
