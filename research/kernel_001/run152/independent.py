"""Independent alternate traversal using extended precision; numerical corroboration."""
import json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
def check(p,depth=14):
    A=np.asarray(p['A'],dtype=np.longdouble)
    E=np.asarray(p['E'],dtype=np.longdouble)
    w=np.asarray(p['w'],dtype=np.longdouble)
    h=np.zeros((1,len(w)),dtype=np.longdouble)
    q=np.zeros(1,dtype=np.int16)
    for _ in range(depth):
        h=np.concatenate([np.maximum(0,h@A.T+E[s]) for s in range(3)],axis=0)
        q=np.concatenate([np.maximum(0,q+inc) for inc in (1,-1,0)])
    return float(np.max(np.abs(h@w-q)))
def main():
    models=json.loads((HERE/'CHECKPOINTS.json').read_text())
    report=json.loads((HERE/'RAW_OUTCOMES.json').read_text())
    expect={(r['seed'],r['variant']):r['depth14_max'] for r in report['records']}
    results=[]
    for row in models:
        value=check(row['parameters'])
        delta=abs(value-expect[row['seed'],row['variant']])
        assert delta<1e-8,(row['seed'],row['variant'],value,delta)
        results.append({'seed':row['seed'],'variant':row['variant'],'max80bit':value,'abs_delta':delta})
        print(row['seed'],row['variant'],value,delta,flush=True)
    assert len(results)==24
    (HERE/'INDEPENDENT_OUTCOMES.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
