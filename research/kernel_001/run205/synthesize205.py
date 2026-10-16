"""Untrusted grid candidate generator; exact checkers are authoritative."""
import csv,math
from pathlib import Path
R=Path(__file__).resolve().parent
def down(x):return math.floor((x-1e-7)/1e-6)*1e-6
def up(x):return math.ceil((x+1e-7)/1e-6)*1e-6
def propose(r):
 w=[float(r['w0']),float(r['w1'])];b=[float(r['b0']),float(r['b1'])]
 v=float(r['v']);c=float(r['c'])
 h=[math.tanh(w[i]*.5+b[i]) for i in (0,1)]
 lo=[down(z) for z in h];hi=[up(z) for z in h]
 for _ in range(1000):
  old=(lo[:],hi[:])
  for p in (0,1):
   for bit in (0,1):
    a=math.tanh(w[bit]*(old[0][p] if w[bit]>=0 else old[1][p])+b[bit])
    z=math.tanh(w[bit]*(old[1][p] if w[bit]>=0 else old[0][p])+b[bit])
    q=p^bit;lo[q]=min(lo[q],down(a));hi[q]=max(hi[q],up(z))
  if (lo,hi)==old:
   if all((min(v*lo[p]+c,v*hi[p]+c)>0 if p else max(v*lo[p]+c,v*hi[p]+c)<0) for p in (0,1)):
    return [lo[0],hi[0],lo[1],hi[1]]
   break
 return None
