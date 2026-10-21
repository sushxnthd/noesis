#!/usr/bin/env python3
"""Frozen Run310: exact causal recurrent-block swaps on 19 paired trained RNNs."""
import json,hashlib
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
EXPECTED='5cb41eaefe2957f01d9b306537bf76cdf3a730ae2baf1ab3e007cad34534de71'

def qparams(p):
    return [F.from_float(float(z)) for z in p]

def cone_search(p):
    z=qparams(p);v=z[24:27]
    if any(w<0 for w in v) or not any(v) or any(z[18+i]>0 for i in range(3)):
        return None
    entry=sum(v[i]*max(F(0),z[21+i]) for i in range(3))
    lo=F(0);hi=entry;mus=[]
    for x in (0,1):
        q=[sum(v[i]*z[9*x+3*i+j] for i in range(3)) for j in range(3)]
        if any(v[j]==0 and q[j]<0 for j in range(3)):
            return None
        mu=min(q[j]/v[j] for j in range(3) if v[j]>0)
        if mu<0:return None
        mus.append(mu)
        beta=sum(v[i]*z[18+3*x+i] for i in range(3))
        if mu==1:
            if beta<0:return None
        elif mu>1:lo=max(lo,-beta/(mu-1))
        else:hi=min(hi,beta/(1-mu))
    if hi<=0 or lo>hi:return None
    T=hi
    bias=-T/2
    proof={'T':str(T),'mu':list(map(str,mus)),'chosen_bias':str(bias)}
    hybrid=[float(z0) for z0 in p];hybrid[-1]=float(bias)
    return proof,hybrid

def trans(a,h,x):
    return tuple(max(F(0),sum(a[9*x+3*i+j]*h[j] for j in range(3))+a[18+3*x+i]) for i in range(3))

def collision(p):
    a=qparams(p);zero=(F(0),)*3;positive={}
    for n in range(1,9):
        nextpos={}
        for h,word in positive.items():
            for x in (0,1):
                nxt=trans(a,h,x)
                if nxt not in nextpos:nextpos[nxt]=word+str(x)
        one=trans(a,zero,1)
        if one not in nextpos:nextpos[one]='0'*(n-1)+'1'
        zero=trans(a,zero,0);positive=nextpos
        if zero in positive:return {'negative':'0'*n,'positive':positive[zero]}
    return None

def main():
    source=P/'run304_pairs.json'
    if not source.exists():
        selected=json.loads((P/'selected_checkpoints304.json').read_text())
        results=json.loads((P/'results304.json').read_text())
        proofs={r['seed']:r['epoch80_certificate'] for r in results['rows']}
        pairs=[{'seed':r['seed'],'early':r['epoch20'],'late':r['epoch80'],
                'certificate':proofs[r['seed']]} for r in selected]
        source.write_text(json.dumps(pairs,sort_keys=True,separators=(',',':'))+'\n')
    raw=source.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED
    pairs=json.loads(raw)
    rows=[(r['seed'],r['early']['p'],r['late']['p']) for r in pairs]
    rows.append((22241,json.loads((P/'seed22241_epoch20.json').read_text()),json.loads((P/'seed22241_epoch80.json').read_text())))
    assert len(rows)==19 and len({r[0] for r in rows})==19
    output=[]
    for seed,early,late in sorted(rows):
        hybrid=late[:24]+early[24:27]+[0.0]
        candidate=cone_search(hybrid)
        hit=collision(early)
        output.append({'seed':seed,'early_exact_collision':hit,
                       'hybrid_certified':candidate is not None,
                       'hybrid_proof':candidate[0] if candidate else None,
                       'early_readout_direction':early[24:27]})
    n=sum(r['hybrid_certified'] for r in output)
    nc=sum(r['hybrid_certified'] and r['early_exact_collision'] is not None for r in output)
    res={'run':310,'design':'late recurrent transition + early readout direction + one exact rational bias',
         'source_sha256':EXPECTED,'rows':output,
         'summary':{'n':19,'certified':n,'certified_with_early_collision':nc,'frozen_primary_pass':n>=5 and nc>=1,
                    'uncertified_are_not_claimed_incorrect':True}}
    (P/'results310.json').write_text(json.dumps(res,indent=2)+'\n')
    print(json.dumps(res['summary']))
    print('CERTIFIED_SEEDS',[(r['seed'],bool(r['early_exact_collision'])) for r in output if r['hybrid_certified']])
if __name__=='__main__':main()
