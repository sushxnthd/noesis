"""Independent high-precision cross-check; not itself a rigorous proof."""
import json,sys
from pathlib import Path
import mpmath as mp
mp.mp.dps=140
for path in sys.argv[1:]:
    r=json.loads(Path(path).read_text(),parse_float=str)[0];p=r["parameters"]
    A=[[mp.mpf(x) for x in row] for row in p["A"]]
    e=[mp.mpf(x) for x in p["E"][0]]
    w=[mp.mpf(x) for x in p["w"]]
    h=[mp.mpf(0)]*len(w);last=None;changes=[]
    for n in range(1,20001):
        z=[sum((a*x for a,x in zip(row,h)),mp.mpf(0))+b for row,b in zip(A,e)]
        mask=[int(x>0) for x in z]
        if mask!=last:changes.append([n,mask]);last=mask
        h=[max(mp.mpf(0),x) for x in z]
        error=sum((a*x for a,x in zip(w,h)),mp.mpf(0))-n
        if abs(error)>mp.mpf("0.1"):
            print(json.dumps({"seed":r["seed"],"first_failure":n,"error":mp.nstr(error,50),"mask_changes":changes}))
            break
    else:raise AssertionError("No failure")
