"""Independent 80-bit all-word search with symbol-major traversal."""
import json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
def check(p):
    A=np.asarray(p["A"],dtype=np.longdouble)
    E=np.asarray(p["E"],dtype=np.longdouble)
    w=np.asarray(p["w"],dtype=np.longdouble)
    h=np.zeros((1,4),dtype=np.longdouble)
    q=np.zeros(1,dtype=int)
    for n in range(1,14):
        h=np.concatenate([np.maximum(0,h@A.T+E[s]) for s in range(3)])
        q=np.concatenate([np.maximum(0,q+d) for d in (1,-1,0)])
        if np.max(np.abs(h@w-q))>np.longdouble(".1"):
            return n
if __name__=="__main__":
    for name,expected in (("baseline",13),("latent",10),("output",13)):
        p=json.loads((HERE/"checkpoints"/(name+".json")).read_text())
        observed=check(p)
        print(name,observed)
        assert observed==expected
