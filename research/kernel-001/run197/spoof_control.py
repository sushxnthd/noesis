"""Finite-horizon cap spoof: correct mod-3 through six steps, then wrong."""
from itertools import product

def cap_predict(word):
    residue=sum(word)%3
    return residue if len(word)<=6 else (residue+1)%3

def verify():
    checked=0
    for n in range(1,7):
        for word in product((0,1),repeat=n):
            assert cap_predict(word)==sum(word)%3
            checked+=1
    failures=[]
    for word in product((0,1),repeat=7):
        if cap_predict(word)!=sum(word)%3:failures.append(''.join(map(str,word)))
    assert len(failures)==128
    return {'pass_short':checked,'length7_failures':len(failures),'first_failure':failures[0],
            'certificate_rejected_by_witness':True,'gradient_trained':False}

if __name__=='__main__':
    import json
    print(json.dumps(verify(),indent=1))