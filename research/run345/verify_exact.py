#!/usr/bin/env python3
"""Exact dyadic audit for Run345; requires archived Run342 JSON files."""
import json,sys,hashlib
from fractions import Fraction as Q
from pathlib import Path
raw=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest()=="c20f44b3bd56893880974c638b6202ad75a5ea253b64f72eeaa094e8d973112e"
rows={r["seed"]:r["p"] for r in json.loads(raw)["rows"] if r["epoch"]==200}
outcomes=json.loads(Path(sys.argv[2]).read_text())["rows"]
seeds=sorted(r["seed"] for r in outcomes if r["correct_through_12_numpy"] and r["seed"]!=31089)
W=sorted(set(["1"]+["1"+"0"*k for k in range(16)]+["1"+"0"*a+"1"+"0"*b for a in range(15) for b in range(15-a)]),key=lambda w:(len(w),w))
assert len(W)==136 and len(seeds)==87
prefixes=sorted({w[:i] for w in W for i in range(len(w)+1)},key=lambda w:(len(w),w))
for seed in seeds:
 p=[Q.from_float(float(x)) for x in rows[seed]]
 A=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
 b=[p[32+4*x:36+4*x] for x in (0,1)]
 h={"":(Q(0),)*4}
 for w in prefixes[1:]:
  z=h[w[:-1]];x=int(w[-1])
  h[w]=tuple(max(Q(0),sum((A[x][i][j]*z[j] for j in range(4)),b[x][i])) for i in range(4))
 for w in W:
  logit=sum((p[40+i]*h[w][i] for i in range(4)),p[44])
  assert (logit>0)==bool(w.count("1")%2),(seed,w)
print("PASS",len(seeds)*len(W))
