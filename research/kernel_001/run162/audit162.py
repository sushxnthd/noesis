"""Run 162: binary32 execution audit of Run 160 repaired trained RNNs.
Only exact-real arithmetic is covered by the Run 160 induction.
"""
import hashlib, json, struct
from pathlib import Path
from fractions import Fraction as Q
HERE=Path(__file__).resolve().parent
SEEDS={222:2,239:4}
LIMIT=2000000
def f32(x):
    return struct.unpack('<f',struct.pack('<f',float(x)))[0]
def load(seed,k):
    raw=(HERE/('RUN157_SEED_%d.json'%seed)).read_bytes()
    obj=json.loads(raw,parse_float=str)[0]
    assert obj['seed']==seed and obj['variant']=='latent'
    a=obj['parameters']
    p={key:([[Q(x) for x in row] for row in a[key]] if key!='w' else [Q(x) for x in a[key]]) for key in ('A','E','w')}
    A,E,w=p['A'],p['E'],p['w'];d=len(w);u=E[0][k]
    assert A[k][k]==1 and u>0
    assert all(A[j][k]<=0 and E[0][j]<=0 for j in range(d) if j!=k)
    E[1][k]=-u;E[2][k]=Q(0);w[k]=1/u
    for t in (1,2):
        for j in range(d):
            if j!=k and E[t][j]>0:E[t][j]=Q(0)
    assert all(A[j][k]<=0 and all(E[t][j]<=0 for t in range(3)) for j in range(d) if j!=k)
    return p,hashlib.sha256(raw).hexdigest()
def scalar32(u,w,limit=LIMIT):
    h=f32(0)
    for n in range(1,limit+1):
        h=f32(h+u);y=f32(w*h)
        if abs(y-n)>0.1:return n,h,y
    return None,h,f32(w*h)
def full32(p,limit):
    A=[[f32(v) for v in row] for row in p['A']]
    E=[[f32(v) for v in row] for row in p['E']]
    w=[f32(v) for v in p['w']];d=len(w);h=[f32(0)]*d
    for n in range(1,limit+1):
        nh=[]
        for i in range(d):
            z=f32(0)
            for j in range(d):z=f32(z+f32(A[i][j]*h[j]))
            nh.append(max(f32(0),f32(z+E[0][i])))
        h=nh;y=f32(0)
        for j in range(d):y=f32(y+f32(w[j]*h[j]))
        if abs(y-n)>0.1:return n,h,y
    return None,h,y
def scalar64(u,w,limit=LIMIT):
    h=0.0
    for n in range(1,limit+1):
        h+=u;y=w*h
        if abs(y-n)>0.1:return n,h,y
    return None,h,w*h
def run():
    out=[]
    for seed,k in SEEDS.items():
        p,sha=load(seed,k)
        n,h,y=scalar32(f32(p['E'][0][k]),f32(p['w'][k]))
        fn,fh,fy=full32(p,n if n else LIMIT)
        assert fn==n and fy==y and all(v==0 for j,v in enumerate(fh) if j!=k)
        n64,h64,y64=scalar64(float(p['E'][0][k]),float(p['w'][k]))
        out.append({'seed':seed,'checkpoint_sha256':sha,'active_coordinate':k,
                    'binary32_first_increment_failure':n,'binary32_output':y,
                    'binary32_signed_error':y-n if n else None,
                    'full_matrix_matches_scalar':True,'binary64_first_failure_le_2m':n64,
                    'binary64_end_error':y64-(n64 or LIMIT)})
    return {'run':162,'threshold':0.1,'limit':LIMIT,
            'semantics':'round each product and sum to binary32, no FMA',
            'frozen_primary_success':all(x['binary32_first_increment_failure'] is not None for x in out),
            'outcomes':out}
if __name__=='__main__':print(json.dumps(run(),indent=2))
