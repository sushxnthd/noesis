"""Exact check on minimized trained checkpoint witnesses (no torch dependency)."""
import json
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent

def evaluate():
    cases=json.loads((HERE/'ELIGIBLE_CHECKPOINTS.json').read_text())
    out=[]
    for x in cases:
        assert Q.from_float(x['a'])==1 and Q.from_float(x['b'])>0
        assert all(Q.from_float(e)<=0 and Q.from_float(a)<=0 for e,a in x['other'])
        g=Q.from_float(x['w'])*Q.from_float(x['b'])
        delta=abs(g-1)
        n=None if delta==0 else int(Q(1,10)//delta)+1
        if n is not None:
            assert (n-1)*delta<=Q(1,10)<n*delta
        out.append({'seed':x['seed'],'dim':x['dim'],'dtype':x['dtype'],
                    'first_failure':n,'gain_minus_one':str(g-1)})
    return out

def test_compact():
    out=evaluate()
    assert len(out)==8 and all(x['first_failure'] is not None for x in out)
    assert sorted(x['first_failure'] for x in out)==sorted([12173660,881096922110118,1400043,5204928,1638808763908189,4440637,3824100,2218939927293197])

if __name__=='__main__':
    print(json.dumps(evaluate(),indent=2))
