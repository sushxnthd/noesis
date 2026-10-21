#!/usr/bin/env python3
"""Public Run310 exact reproduction from frozen Run304 combined trained checkpoints."""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
SEEDS=(22242,22287,22361,22573)
EXPECTED="750da83715d79f3f6e1aeb9ab7dfbf33087dc7c9f27f8d10a20842df10f4d6f9"
def verify(p):
 a=list(map(Q.from_float,p))
 states=[(Q(0),)*3]
 total=0
 for n in range(1,17):
  nxt=[]
  for j,h in enumerate(states):
   for x in (0,1):
    v=tuple(max(Q(0),a[18+3*x+i]+sum(a[9*x+3*i+k]*h[k] for k in range(3))) for i in range(3))
    nxt.append(v)
    z=a[27]+sum(a[24+k]*v[k] for k in range(3))
    if (z>0)!=((j*2+x)!=0):
     raise AssertionError((n,format(j*2+x,f"0{n}b"),str(z)))
  states=nxt
  total+=len(nxt)
 return total
def main():
 src=Path(sys.argv[1])
 assert hashlib.sha256(src.read_bytes()).hexdigest()==EXPECTED,"checkpoint artifact hash changed"
 rows=json.loads(src.read_text())["rows"]
 models={r["seed"]:r["p"] for r in rows if r["epoch"]==80 and r["seed"] in SEEDS}
 assert len(models)==4
 counts={seed:verify(models[seed]) for seed in SEEDS}
 assert all(n==131070 for n in counts.values())
 print(json.dumps({"run":310,"exact_checks":sum(counts.values()),"per_seed":counts,"all_length_certificate":False},sort_keys=True))
if __name__=="__main__":main()
