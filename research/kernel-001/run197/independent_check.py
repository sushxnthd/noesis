"""Independent outward-interval verifier for Run197 seed257 epoch800.
Proves exact-real float64-weight signs for a specific witness and, optionally,
all words through a requested finite depth. Does NOT certify all lengths.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction
from mpmath import iv
iv.dps=45
R=Path(__file__).resolve().parent
row=next(r for r in json.loads((R/'CHECKPOINTS.json').read_text())['rows'] if r['seed']==257 and r['epoch']==800)
P=row['params']

def q(x):
    f=Fraction.from_float(float(x));return iv.mpf(f.numerator)/iv.mpf(f.denominator)
W=[[q(x) for x in r] for r in P['W']]
U=[[q(x) for x in r] for r in P['U']]
b=[q(x) for x in P['b']]
V=[[q(x) for x in r] for r in P['V']]
c=[q(x) for x in P['c']]

def advance(h,bit):
    z=[sum((W[i][j]*h[j] for j in range(12)),U[bit][i]+b[i]) for i in range(12)]
    return [1-2/(1+iv.exp(2*x)) for x in z]

def output(h):
    return [sum((V[i][j]*h[j] for j in range(12)),c[i]) for i in range(3)]

def is_correct(z,cls):
    return all(bool((z[cls]-z[j]).a>0) for j in range(3) if j!=cls)

def is_wrong(z,cls):
    return any(bool((z[j]-z[cls]).a>0) for j in range(3) if j!=cls)

def witness(word):
    h=[iv.mpf(0)]*12;cls=0
    for bit in map(int,word):h=advance(h,bit);cls=(cls+bit)%3
    z=output(h)
    assert is_wrong(z,cls),('witness not certified wrong',z,cls)
    return {'witness':word,'true_residue':cls,'interval_logits':[[str(x.a),str(x.b)] for x in z],
            'certified_wrong':True,'precision_decimal_digits':45}

def all_short(maxdepth):
    # Depth-first traversal prevents the exponential memory blowup of storing
    # every interval state simultaneously. This supersedes the timed-out BFS.
    counts={d:0 for d in range(1,maxdepth+1)}
    t=time.time()
    def visit(h,cls,depth):
        if depth>0:
            z=output(h)
            if not is_correct(z,cls):
                raise AssertionError(('short failure or ambiguous',depth,cls,z))
            counts[depth]+=1
        if depth==maxdepth:return
        for bit in (0,1):visit(advance(h,bit),(cls+bit)%3,depth+1)
    visit([iv.mpf(0)]*12,0,0)
    print('INTERVAL_DFS_DONE',maxdepth,round(time.time()-t,2),flush=True)
    return {'max_verified_length':maxdepth,'prefixes_checked':sum(counts.values()),
            'all_correct':True,'precision_decimal_digits':45}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--maxdepth',type=int,default=0);args=ap.parse_args()
    result={'witness':witness('000000101010000')}
    if args.maxdepth:result['minimality']=all_short(args.maxdepth)
    (R/'INDEPENDENT_INTERVAL.json').write_text(json.dumps(result,indent=1)+'\n')
    print(json.dumps(result,indent=1),flush=True)