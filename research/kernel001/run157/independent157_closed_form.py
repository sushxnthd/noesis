"""Independent 90-digit Decimal check of exact rational closed-form."""
import json,sys
from decimal import Decimal as D,localcontext,ROUND_FLOOR
from pathlib import Path
for path in sys.argv[1:]:
    r=json.loads(Path(path).read_text(),parse_float=str)[0];p=r["parameters"]
    k={222:2,239:4}[r["seed"]]
    with localcontext() as ctx:
        ctx.prec=90
        A=[[D(x) for x in row] for row in p["A"]]
        E=[D(x) for x in p["E"][0]]
        w=[D(x) for x in p["w"]]
        assert A[k][k]==1 and E[k]>0
        assert all(A[j][k]<0 and E[j]<0 for j in range(len(w)) if j!=k)
        delta=w[k]*E[k]-1
        N=int((D("0.1")/delta).to_integral_value(rounding=ROUND_FLOOR))+1
        assert (N-1)*delta<D("0.1")<N*delta
        print(r["seed"],N,"delta",delta,"error_N",N*delta)
