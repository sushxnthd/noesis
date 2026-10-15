"""Independent high-precision full trajectory check; separate from interval/cone proof."""
import json,sys
from decimal import Decimal, localcontext

def run(path):
    d=json.load(open(path),parse_float=Decimal)[0]['parameters']
    with localcontext() as c:
        c.prec=125
        A=d['A'];E=d['E'];w=d['w'];h=[Decimal(0)]*3
        def step(h,token):
            z=[sum(A[i][j]*h[j] for j in range(3))+E[token][i] for i in range(3)]
            return [max(Decimal(0),z[i]) for i in range(3)],tuple(int(t>0) for t in z)
        for _ in range(6):h,_=step(h,0)
        prev=sum(w[i]*h[i] for i in range(3))-6
        first=None;mask_changes=0
        for k in range(1,7902):
            h,m0=step(h,0);h,m1=step(h,1)
            if m0!=(1,1,0) or m1!=(1,1,0):mask_changes+=1
            e=sum(w[i]*h[i] for i in range(3))-6
            assert e<prev, ('monotonicity failed',k)
            if k<=7900:assert abs(e)<Decimal('.1'), ('early failure',k)
            if k==7901:assert e<-Decimal('.1')
            prev=e
            if first is None and abs(e)>Decimal('.1'):first=k
        return dict(first_failure=first,mask_changes=mask_changes,error_7901=str(prev),verified_cycles=7901)
if __name__=='__main__':print(json.dumps(run(sys.argv[1]),indent=2))
