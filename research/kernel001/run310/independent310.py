#!/usr/bin/env python3
"""Independent Run310 exact rational checker, no search-code imports."""
import json,hashlib
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent

def state(p,word):
    a=[Q.from_float(float(z)) for z in p]
    h=(Q(0),Q(0),Q(0))
    for c in word:
        x=int(c)
        h=tuple(max(Q(0),sum(a[9*x+3*i+j]*h[j] for j in range(3))+a[18+3*x+i]) for i in range(3))
    return h

def check(hybrid,cert):
    a=[Q.from_float(float(z)) for z in hybrid[:27]]+[Q(cert['chosen_bias'])]
    T=Q(cert['T']);mu=[Q(x) for x in cert['mu']];v=a[24:27];c=a[27]
    if not (T>0 and c<0 and c+T>0 and len(mu)==2 and all(t>=0 for t in v) and any(v)):
        return False
    if any(a[18+i]>0 for i in range(3)):
        return False
    if sum(v[i]*max(Q(0),a[21+i]) for i in range(3))<T:
        return False
    for x in (0,1):
        if mu[x]<0:return False
        for j in range(3):
            if sum(v[i]*a[9*x+3*i+j] for i in range(3))<mu[x]*v[j]:return False
        if mu[x]*T+sum(v[i]*a[18+3*x+i] for i in range(3))<T:return False
    return True

def main():
    src=(P/'run304_pairs.json').read_bytes()
    assert hashlib.sha256(src).hexdigest()=='5cb41eaefe2957f01d9b306537bf76cdf3a730ae2baf1ab3e007cad34534de71'
    pairs={r['seed']:(r['early']['p'],r['late']['p']) for r in json.loads(src)}
    pairs[22241]=(json.loads((P/'seed22241_epoch20.json').read_text()),json.loads((P/'seed22241_epoch80.json').read_text()))
    rows=json.loads((P/'results310.json').read_text())['rows']
    assert len(pairs)==len(rows)==19
    verified=[];collisions=0;mutations=0
    for row in rows:
        seed=row['seed'];e,l=pairs[seed]
        collision=row['early_exact_collision']
        if collision:
            neg,pos=collision['negative'],collision['positive']
            assert len(neg)==len(pos) and '1' not in neg and '1' in pos
            assert state(e,neg)==state(e,pos)
            collisions+=1
        cert=row['hybrid_proof']
        if cert:
            hybrid=l[:24]+e[24:27]+[0.0]
            assert check(hybrid,cert),seed
            verified.append(seed)
            for change in ('zero_prefix','readout_sign','bias_sign'):
                bad=hybrid.copy();bad_cert=dict(cert)
                if change=='zero_prefix':bad[18]=1.0
                elif change=='readout_sign':bad[24]=-100.0
                else:bad_cert['chosen_bias']='1'
                assert not check(bad,bad_cert),(seed,change)
                mutations+=1
    assert len(verified)==8
    assert not any(row['hybrid_certified'] and row['early_exact_collision'] for row in rows)
    out={'all_pairs':19,'exact_hybrid_certificates':len(verified),
         'verified_early_equal_length_collisions':collisions,'mutations_rejected':mutations,
         'frozen_primary_pass':False,'certified_seeds':verified}
    print('INDEPENDENT310',json.dumps(out,sort_keys=True))
    (P/'independent_results310.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
