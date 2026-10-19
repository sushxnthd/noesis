import csv,sys,json
from pathlib import Path
from fractions import Fraction as F
import sympy as S
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'run278'))
from independent import verify
from sampled import sequences,replay
from core import witness_wrong
from robust279 import repair,mutants

def certified(p):
    return bool(verify([S.Rational(str(x)) for x in p]))

def main():
    cols=['seed','epoch','a0','a1','a2','b0','b1','b2','v','c','family','n','symbol']
    rows=[]
    for path in sorted((ROOT.parent/'run278').glob('checkpoints_part*.csv')):
        rows += [r for r in csv.DictReader(path.open(),fieldnames=cols) if r['seed']!='seed']
    assert len(rows)==11
    outcomes=[]
    for row in rows:
        seed=int(row['seed'])
        p=[F.from_float(float(row[k])) for k in cols[2:10]]
        q=repair(p)
        edits=[i for i in range(8) if p[i]!=q[i]]
        assert len(edits)<=2 and certified(q)
        assert not certified(p)
        sym=int(row['symbol']) if row['symbol'] else None
        assert witness_wrong(p,row['family'],int(row['n']),sym)
        words=sequences(seed)
        assert replay(p,words)==replay(q,words)==(3396,3396)
        checks=[certified(v) for _,_,v in mutants(q)]
        assert len(checks)==16 and all(checks)
        outcomes.append({'seed':seed,'epoch':int(row['epoch']),'edits':edits,'base_certificate':True,'ulp_passes':sum(checks),'sampled_correct':3396,'new_parameters':[str(x) for x in q]})
    (ROOT/'outcomes279_ci.json').write_text(json.dumps(outcomes,indent=2)+'\n')
    print('Run279 independent verifier: 11/11 models, 176/176 ULP mutants, 11/11 original witnesses PASS')
if __name__=='__main__':main()
