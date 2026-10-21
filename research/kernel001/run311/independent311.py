#!/usr/bin/env python3
"""Independent exact replay using as_integer_ratio; no shared transition helper."""
import json
from fractions import Fraction as Q
from pathlib import Path
from search311 import weights,SEEDS
P=Path(__file__).resolve().parent
def replay(p,w):
    z=[Q(*float(t).as_integer_ratio()) for t in p]
    h=(Q(0),Q(0),Q(0))
    for digit in w:
        k=ord(digit)-48
        matrix=[z[9*k+3*i:9*k+3*i+3] for i in range(3)]
        bias=z[18+3*k:21+3*k]
        new=[]
        for row,b in zip(matrix,bias):
            v=b
            for a,s in zip(row,h):v+=a*s
            new.append(max(Q(0),v))
        h=tuple(new)
    return z[27]+sum(z[24+i]*h[i] for i in range(3))
def main():
    probes=["0"*512,"1"+"0"*511,"0"*32+"1"+"0"*256,"01"*256,"10"*256,"1"*64+"0"*256]
    for seed in SEEDS:
        for w in probes:
            assert (replay(weights(seed),w)>0)==("1" in w),(seed,len(w))
    # Delayed failure in a separate gradient-trained model, pre-established Run302.
    assert replay(weights(22370),"1"+"0"*196)<0
    out={"exact_probe_checks":24,"known_negative_control":22370,"control_length":197,"passed":True}
    (P/"independent_results311.json").write_text(json.dumps(out,indent=2)+"\n")
    print(out)
if __name__=="__main__":main()
