"""Independent NumPy full-matrix checker for the first binary32 failure."""
import json
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
HERE=Path(__file__).resolve().parent
def verify(seed,k):
    raw=json.loads((HERE/('RUN157_SEED_%d.json'%seed)).read_text(),parse_float=str)[0]
    p=raw['parameters']; A=np.array(p['A'],dtype=np.float32)
    E=np.array(p['E'],dtype=np.float32);w=np.array(p['w'],dtype=np.float32)
    u=Q(p['E'][0][k]);assert Q(p['A'][k][k])==1
    E[1,k]=np.float32(float(-u));E[2,k]=np.float32(0);w[k]=np.float32(float(1/u))
    for t in (1,2):
        for j in range(len(w)):
            if j!=k and Q(p['E'][t][j])>0:E[t,j]=np.float32(0)
    h=np.zeros(len(w),dtype=np.float32)
    for n in range(1,5001):
        nxt=np.empty_like(h)
        for i in range(len(w)):
            z=np.float32(0)
            for j in range(len(w)):z=np.float32(z+np.float32(A[i,j]*h[j]))
            nxt[i]=np.maximum(np.float32(0),np.float32(z+E[0,i]))
        h=nxt;y=np.float32(0)
        for j in range(len(w)):y=np.float32(y+np.float32(w[j]*h[j]))
        if abs(float(y)-n)>0.1:return {'seed':seed,'first':n,'output':float(y)}
    return {'seed':seed,'first':None}
if __name__=='__main__':
    outcomes=[verify(222,2),verify(239,4)]
    assert [x['first'] for x in outcomes]==[3679,3582]
    print(json.dumps({'independent_numpy':outcomes},indent=2))
